#!/usr/bin/env python3
import boto3
import tempfile


class S3Uploader():
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3')

    def upload_file(self, file_data, filename):
        return self.s3.upload_fileobj(file_data, self.bucket_name, filename)


if __name__ == '__main__':
    s3_uploader = S3Uploader('bucketname')
    with tempfile.TemporaryFile() as temporary_file:
        temporary_file.write(b'hello world!')
        s3_uploader.upload_file(temporary_file, '123.txt')
