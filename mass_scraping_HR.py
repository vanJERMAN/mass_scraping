# https://www.rithmschool.com/blog

import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep
from datetime import date
from random import randint, randrange
import urllib.request
import os
from PIL import Image
import pandas as pd
from vstavitev_slik_HR import vstavitev_slike
from zaloga_HR import stevilke, zaloga
from grafi_HR import izdelava_grafov, izdelava_stolpcev, vstavitev_grafov
from posiljanje_HR import posiljanje
import pathlib
# import numpy as np
# https://www.rithmschool.com/blog


def scraping_HR(): 
	path = pathlib.Path(__file__).parent.absolute()   
	print("Start scraping!")
	i = 1

	pages = "https://www.mass-shoes.com/marke/guess"
	datum = date.today()

	linki = []

	with open(f"{path}/csv_in_xlsx_datoteke_HR/mass_data_HR.csv", "w") as csv_file:
		csv_writer = writer(csv_file)
		csv_writer.writerow(["SLIKA", f"PRODAJA ARTIKLA NA DAN: {datum}", "ZGODOVINA PRODAJE ARTIKLA", "BRAND", "ARTIKEL", "VRSTA ARTIKLA", "STARA CENA", "NOVA CENA", "RAZLIKA %", "LINK", "ZALOGA št.36", "ZALOGA št.37", "ZALOGA št.38", "ZALOGA št.39", "ZALOGA št.40", "ZALOGA št.41", "ZALOGA št.42", "ZALOGA št.43", "ZALOGA št.44", "ZALOGA št.45", "ZALOGA št.46"])

	while pages:
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
		response = requests.get(pages, headers)
		r = requests.head(pages)
		print(r.status_code)
		# print(response.text)
		soup = BeautifulSoup(response.text, "html.parser")
		articles = soup.find_all(class_="product-grid-image-container")
		next_button = soup.find(class_="item pages-item-next")
		pages = next_button.find("a")["href"] if next_button else None


		with open(f"{path}/csv_in_xlsx_datoteke_HR/mass_data_HR.csv", "a") as csv_file:
			csv_writer = writer(csv_file)
			rand = randint(5, 10)

			for article in articles:
				
				rand1 = randint(1, 2)
				# cena = article.find(class_="prices").get_text()
				try:
					artikel = article.find(class_="subbrand-name").get_text()
				except AttributeError:
					artikel = article.find(class_="product-title").get_text()
				
				try:
					vrsta_artikla = article.find(class_="type-1").get_text()
				except AttributeError:
					vrsta_artikla = "-"
				
				try:
					brand = article.find(class_="brand-name").get_text()
				except AttributeError:
					brand = "-"

				stara_cena = article.select("[data-price-amount]")[0].get_text()
				
				try:
					nova_cena = article.select("[data-price-amount]")[1].get_text()
				except IndexError:
					nova_cena = "-"

				try:
					stara_cena = stara_cena.replace(".", "")
					procent_brez_znaka = round(100 - (((float(nova_cena[:5].replace(",", ".")) * 100) / float(stara_cena[:-3].replace(",", ".")))))
					procent = f"{procent_brez_znaka}%"
				except ValueError:
					procent = "-"

				file_path = f"{path}/slike_HR/"
				url = article.find("img")["data-src"]
				filename = url[-22:]
				full_path = f"{file_path}{filename}"
				file_path_check = f"{path}/slike_HR/{filename}"
				isFile = os.path.isfile(file_path_check)
				print(isFile)


				if isFile == False:
					urllib.request.urlretrieve(url, full_path)
					print(f"{filename} saved")

					in_file = full_path  # 1600, 900
					out_file = full_path
					 
					img = Image.open(in_file)
					 
					size = (img.size[0]/3,  img.size[1]/3)
					img.thumbnail(size)
					 
					img.save(out_file)


				elif isFile == True:
					print(f"Slika {filename} že obstaja")

				else:
					print("Nekaj je narobe pri branju/pisanju slik")


				linki_artiklov = article.find("a")["href"]
				zaloga(linki_artiklov)
				st_36 = stevilke.get("st_36")
				print(st_36)
				st_37 = stevilke.get("st_37")
				st_38 = stevilke.get("st_38")
				st_39 = stevilke.get("st_39")
				st_40 = stevilke.get("st_40")
				st_41 = stevilke.get("st_41")
				st_42 = stevilke.get("st_42")
				st_43 = stevilke.get("st_43")
				st_44 = stevilke.get("st_44")
				st_45 = stevilke.get("st_45")
				st_46 = stevilke.get("st_46")

				linki.append(linki_artiklov)
				

				# img = np.array(Image.open(file_path_check))


				# url = article.find("img")["data-src"]




			

				# url = article.find("a")["href"]
				# # print(url)

				# img_name = randrange(1, 500)
				# full_name = str(img_name)+".jpg"
				# urllib.request.urlretrieve(url, full_name)


				# image_url = article.find("img")["data-src"]
				# filename = image_url
				# urllib.request.urlretrieve(image_url, filename)
				# print(image_url)
				# i +=1


				# i += 2
				# url = article.find("a")["href"]
				# zaloga = 
				# url = a_tag["href"]
				# date = article.find("time")["datetime"]
				csv_writer.writerow([full_path, " ", " ", brand, artikel, vrsta_artikla, stara_cena, nova_cena, procent, url, st_36, st_37, st_38, st_39, st_40, st_41, st_42, st_43, st_44, st_45, st_46])
				# print(brand)
				# print(stara_cena)
				# print(nova_cena)
				sleep(rand1)




			sleep(rand)
			# print(rand)

	# print(linki)
	read_file = pd.read_csv (rf"{path}/csv_in_xlsx_datoteke_HR/mass_data_HR.csv")
	read_file.to_excel (rf"{path}/csv_in_xlsx_datoteke_HR/{datum}.xlsx", index = None, header=True)


	while True:
		try:
			vstavitev_slike()
		except:
			try:
				vstavitev_slike()
			except Exception as error:
				posiljanje("vanjermancek@gmail.com", "There was an error while running vstavitev_slike()_HR", f"{error}")
				break
		try:
			izdelava_grafov()
		except:
			try:
				izdelava_grafov()
			except Exception as error:
				posiljanje("vanjermancek@gmail.com", "There was an error while running izdelava_grafov()_HR", f"{error}")
				break
		try:
			izdelava_stolpcev()
		except:
			try:
				izdelava_stolpcev()
			except Exception as error:
				posiljanje("vanjermancek@gmail.com", "There was an error while running izdelava_stolpcev()_HR", f"{error}")
				break
		try:
			vstavitev_grafov()
		except:
			try:
				vstavitev_grafov()
			except Exception as error:
				posiljanje("vanjermancek@gmail.com", "There was an error while running vstavitev_grafov()_HR", f"{error}")
				break
		try:
			os.remove(f"{path}/csv_in_xlsx_datoteke_HR/mass_data_HR.csv")
			print("mass_data_HR.csv Removed!")
			posiljanje()
			print("POSLALO! Čaki še 10 sekund")
			sleep(10)
			print("ekola konec!")
			break
		except:
			try:
				posiljanje()
			except Exception as error:
				posiljanje("vanjermancek@gmail.com", "There was an error while running posiljanje()_HR", f"{error}")
				break

	
if __name__ == "__main__":
	scraping_HR()

