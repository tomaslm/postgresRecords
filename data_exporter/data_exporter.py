#!/usr/bin/env python3
from data_extractor.data_extractor import DataExtractor
import os


class DataExporter():
    def __init__(self, database_url, sql_files_path):
        self.data_extractor = DataExtractor(database_url)
        self.sql_files_path = sql_files_path

    def export_data(self, export_type, configs, filters):
        temp_file = DataExtractor.export_to_tempfile(
            sql_file_pahts=sql_file_pahts={
                'data': os.path.join(sql_files_path, export_type,  f'{export_type}_data.sql'),
                'header': os.path.join(sql_files_path, export_type,  f'{export_type}_header.sql'),
            },
            configs=configs,
            filters=filters)


if __name__ == '__main__':
    data_exporter = DataExporter(
        database_url='postgresql://postgres:pass@localhost:5432/extract_data',
    )
    configs = {
        timezone: timezone_sao_paulo
    }
    filters = {
        'ids': (1, 2, 3, 4, 5, 6, 7),
        'date_min': datetime.datetime(2018, 12, 6, 00, 00).astimezone(timezone_sao_paulo),
        'date_max': datetime.datetime(2019, 1, 1, 00, 00).astimezone(timezone_sao_paulo),
    }

    data_exporter.export_data('order', configs, filters)


'''
timezone_sao_paulo = timezone('America/Sao_Paulo')





current_dir = os.path.dirname(os.path.abspath(__file__))
data_exporter.export_to_tempfile(
    sql_file_pahts={
        'data': os.path.join(current_dir, 'sql', 'order', 'order_data.sql'),
        'header': os.path.join(current_dir, 'sql', 'order', 'order_header.sql'),
    },
    configs=configs,
    filters=filters)

'''
