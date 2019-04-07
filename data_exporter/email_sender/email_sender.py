#!usr/bin/lib python3
import requests


class EmailSender:
    def __init__(self, email_sender, url_email_service):
        self.email_sender = email_sender
        self.url_email_service = url_email_service

    def send_email(self, recipients, export_type, url_exported_file):
        body = (
            f'Link to download export file of type "{export_type}": {url_exported_file}'
        )

        payload = {"sender": self.email_sender,
                   "recipients": recipients, "body": body}

        requests.post(self.url_email_service, data=payload)


if __name__ == "__main__":
    email_sender = EmailSender(
        email_sender="Sender Name <sender@example.com>",
        url_email_service="http://www.email-service.com/send-email",
    )
    email_sender.send_email(
        recipients=("recipient@example.com"),
        export_type='order',
        url_exported_file='http://s3-external-1.amazonaws.com/bucket/123',
    )
