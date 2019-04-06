#!/usr/bin/env python3
import boto3


class S3Uploader():
    def __init__(bucket_name):
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3')

    def upload_file(self, file_data, filename):
        self.s3.upload_fileobj(file_data, self.bucket_name, filename)


if __name__ == '__main__':
    s3_uploader = S3Uploader('bucketname')
    s3_uploader.upload_file(b'123', '123.txt')
