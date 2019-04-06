#!/usr/bin/env python3
import records
import os
import csv
import tempfile
import datetime
import pytz
from pytz import timezone
import tempfile


class DataExtractor():
    def __init__(self, url):
        self.db = records.Database(url)

    def select_data(self, sql_file_data_path, filters):
        results = self.db.query_file(sql_file_data_path, **filters)
        return (result for result in results)

    def get_header_with_labels(self, sql_file_header_path):
        return self.db.query_file(sql_file_header_path,
                                  fetchall=True).as_dict(ordered=True)

    def export_upload_and_send_email(self, sql_file_pahts, configs, filters):
        tempfile = export_to_tempfile(sql_file_pahts, configs, filters)

    def export_to_tempfile(self, sql_file_pahts, configs, filters):
        results = self.select_data(sql_file_pahts.get('data'), filters)

        header = self.get_header_with_labels(sql_file_pahts.get('header'))

        header_labels = [item.get('label') for item in header]
        header_properties = [item.get('property') for item in header]
        with open('mydump.csv', 'w') as outfile:
            outcsv = csv.writer(outfile, dialect="excel", delimiter=";")
            outcsv.writerow(header_labels)

            def format_values(row):
                return [self.format_value_by_type(row.get(prop), configs) for prop in header_properties]

            outcsv.writerows(format_values(row) for row in results)

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

    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_exporter.export_to_tempfile(
        sql_file_pahts={
            'data': os.path.join(current_dir, 'sql', 'order', 'order_data.sql'),
            'header': os.path.join(current_dir, 'sql', 'order', 'order_header.sql'),
        },
        configs=configs,
        filters=filters)
