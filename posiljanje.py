import os
import base64
from datetime import date
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
import pathlib

datum = date.today()
path = pathlib.Path(__file__).parent.absolute()

def posiljanje(recipient="natasak@sanis.si", subject=f"Mass dokumentacija {datum}", message="Sporočilo je bilo avtomatizirano s pomočjo Pythona.\nSestavil, uredil in poslal: Erik Jerman\n", file_path=f'{path}/csv_in_xlsx_datoteke/{datum}.xlsx'):
	print(f"Sending {subject}")
	to_emails = [
    ('vanjermancek@gmail.com'),
    (recipient)
	]
	message = Mail(
	    from_email='vanjermancek@gmail.com',
	    to_emails=to_emails,
	    is_multiple=True,
	    subject=subject,
	    html_content=message
	)
	try:
		with open(file_path, 'rb') as f:
		    data = f.read()
		    f.close()
		encoded_file = base64.b64encode(data).decode()

		attachedFile = Attachment(
		    FileContent(encoded_file),
		    FileName(f'{datum}.xlsx'),
		    FileType('text/xlsx'),
		    Disposition('attachment')
		)
		message.attachment = attachedFile
	except FileNotFoundError:
		print("Datoteka ne obstaja")

	sg = SendGridAPIClient('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')
	response = sg.send(message)
	print(response.status_code, response.body, response.headers)


if __name__ == "__main__":
	posiljanje()

