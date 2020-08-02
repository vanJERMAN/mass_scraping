import schedule
import time
from mass_scraping import scraping
from mass_scraping_HR import scraping_HR
from posiljanje import posiljanje

try:
	def start_task():
	    scraping()

	def start_task_HR():
		scraping_HR()


	schedule.every().day.at("06:30").do(start_task)
	schedule.every().day.at("08:30").do(start_task_HR)

	while True:
	    schedule.run_pending()
	    time.sleep(1)

except:
	try:
		print("Trying again to run start_script.py")
		def start_task():
			scraping()

		def start_task_HR():
			scraping_HR()


		schedule.every().day.at("06:30").do(start_task)
		schedule.every().day.at("08:30").do(start_task_HR)

		while True:
			schedule.run_pending()
			time.sleep(1)
	except Exception as error:
		posiljanje("vanjermancek@gmail.com", "There was an error while running start_script.py", f"{error}")