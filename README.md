# mass_scraping
Script will scrap Mass.si webpage and make new xlsx file depending on the current date. The xlsx file will contain all data about Guess articles and will also have graphs about current availability in 24 different Mass shops all around Slovenia + 1 month sale history

# When you run start_script.py, will automatically schedule every day at specific time, to start each one of two scripts (mass_scraping.py and mass_scraping_HR.py).
# One is for Slovenian Mass web shop and the other (mass_scraping_HR.py) is for Croatian web shop. It will scrap all the Guess products from the page and create
# a .csv file with all the data.
# zaloga.py and zaloga_HR.py (again the one with _HR at the end is for Croatian web shop) will scrape the Javascript part of the page, with help of the selenium module.
# Selenium module works headless, so it spares some CPU :D
# vstavitev_slik.py and vstavitev_slik_HR.py will insert photos of articles to the first column
# grafi.py and grafi_HR.py scripts will first create graphs and after that will insert them on their specific location in the .xlsx file. It will create pie graph for every
# number of a specific article + pie graph for all numbers of a specific article + bar graph for history of all numbers of specific article + pie graph of all articles
# and at the end will also create bar graph for history of all articles.
# at the end posiljanje.py and posiljanje_HR.py will send mail, with included .xlsx file to the recepient or multiple recepients.
# In mass_scraping.py and mass_scraping_HR.py is also try/except for every part of this app, in case if there is an error, that it retries again and if it fails
# for the second time, it sends email to the recepient or multiple recepients with error message.


# for any message feel free to contact me on: vanjermancek@gmail.com  :)
