#!/usr/bin/env python3
import records
import os
import csv
import tempfile
import datetime
import pytz
from pytz import timezone


class DataExtractor():
    def __init__(self, url):
        self.db = records.Database(url)
        self.sql_folder = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'sql')

    def select_data(self, export_type, filters):
        file_path = os.path.join(
            self.sql_folder, export_type, f'{export_type}_data.sql')
        results = self.db.query_file(file_path, **filters)
        return (result for result in results)

    def get_header_with_labels(self, export_type):
        file_path = os.path.join(
            self.sql_folder, export_type, f'{export_type}_header.sql')
        return self.db.query_file(file_path,
                                  fetchall=True).as_dict(ordered=True)

    def export_to_tempfile(self, export_type, configs, filters, filename):
        results = self.select_data(export_type, filters)

        header = self.get_header_with_labels(export_type)

        header_labels = [item.get('label') for item in header]
        header_properties = [item.get('property') for item in header]

        temporary_file = tempfile.TemporaryFile()
        temp_csv = csv.writer(temporary_file, dialect="excel", delimiter=";")
        temp_csv.writerow(header_labels)

        def format_values(row):
            return [self.format_value_by_type(row.get(prop), configs) for prop in header_properties]

        temp_csv.writerows(format_values(row) for row in results)

        return temporary_file

    def format_value_by_type(self, value, configs):
        value_type = type(value)
        if value_type is datetime.datetime:
            return value.astimezone(configs.get("timezone", timezone('GMT')))
        else:
            return value


if __name__ == '__main__':
    data_exporter = DataExtractor(
        url='postgresql://postgres:pass@localhost:5432/extract_data',
    )

    timezone_sao_paulo = timezone('America/Sao_Paulo')

    configs = {
        timezone: timezone_sao_paulo
    }

    filters = {
        'ids': (1, 2, 3, 4, 5, 6, 7),
        'date_min': datetime.datetime(2018, 12, 6, 00, 00).astimezone(timezone_sao_paulo),
        'date_max': datetime.datetime(2019, 1, 1, 00, 00).astimezone(timezone_sao_paulo),
    }

    data_exporter.export_to_tempfile(
        export_type='order',
        configs=configs,
        filters=filters,
        filename='temp',
    )
