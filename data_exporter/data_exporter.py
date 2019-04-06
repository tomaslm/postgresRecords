#!/usr/bin/env python3
from data_extractor.data_extractor import DataExtractor


class DataExporter():
    def __init__(self):
        self.data_extractor = DataExtractor()


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
