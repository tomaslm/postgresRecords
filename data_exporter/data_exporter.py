#!/usr/bin/env python3
from data_extractor.data_extractor import DataExtractor
from s3_uploader.s3_uploader import S3Uploader
from email_sender.email_sender import EmailSender
import os
import time


class DataExporter():
    def __init__(self,
                 database_url,
                 sql_files_path,
                 s3_bucket_name,
                 email_sender,
                 url_email_service):
        self.data_extractor = DataExtractor(database_url)
        self.sql_files_path = sql_files_path

        self.s3_uploader = S3Uploader(s3_bucket_name)

        self.email_sender = EmailSender(email_sender, url_email_service)

    def export_data(self, export_type, configs, filters):
        with DataExtractor.export_to_tempfile(
                export_type=export_type,
                configs=configs,
                filters=filters) as temporary_file:
            s3_uri = s3_uploader.upload_file(
                temporary_file, f'{export_type}_{time.strftime("%Y%m%d-%H%M%S")}.csv')
        self.email_sender.send_email(s3_uri)


if __name__ == '__main__':
    data_exporter = DataExporter(
        database_url='postgresql://postgres:pass@localhost:5432/extract_data',
        s3_bucket_name='bucketname'
        email_sender='Sender Name <sender@example.com>',
        url_email_service='http://www.email-service.com/send-email',
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

    data_exporter.export_data('order', configs, filters)
