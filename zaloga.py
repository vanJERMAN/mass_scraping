
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from posiljanje import posiljanje
import pathlib


stevilke = {}
mesta = ("LJUBLJANA", "KAMNIK", "KRANJ", "LESCE", "ŠKOFJA LOKA", "CELJE", "MARIBOR", "PTUJ", "MURSKA SOBOTA", "SLOVENJ GRADEC", "VELENJE", "POSTOJNA", "NOVA GORICA", "KOPER", "LESKOVEC PRI KRŠKEM", "NOVO MESTO", "DOMŽALE")

def zaloga(linki_artiklov):
	path = pathlib.Path(__file__).parent.absolute()
	CHROMEDRIVER_PATH = f"{path}/chromedriver"
	options = Options()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')  # Last I checked this was necessary.
	driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
	driver.implicitly_wait(2)


	# driver = webdriver.Chrome(CHROMEDRIVER_PATH)



	driver.get(linki_artiklov)
	driver.find_element_by_id("gdpr_save_close").click()
	driver.find_element_by_xpath("//a[@class='action store-stock small']").click()


	try:
		select = Select(driver.find_element_by_id("product_sku_select"))
		for i in range(36, 47):
			try:
				driver.find_element_by_xpath("//select[@id='product_sku_select']").click()
				select = Select(driver.find_element_by_id("product_sku_select"))
				select.select_by_visible_text(str(i))
				driver.find_element_by_xpath("//a[@class='action primary']").click()


				wait = WebDriverWait(driver, 100)
				element = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "store-name"), "Mass Čopova Ljubljana"))
				search = driver.find_element_by_id("stock-popup").text
				lista = search.split("\n")
				st = lista.index("LJUBLJANA")
				for x in range(0, st):
					lista.remove(lista[0])
				# lista.remove("Iskanje")
				for m in mesta:
					lista.remove(m)
				# print(lista)
				lista_prava = f"{lista[0]}: {lista[2]},\n{lista[3]}: {lista[5]},\n{lista[6]}: {lista[8]},\n{lista[9]}: {lista[11]},\n{lista[12]}: {lista[14]},\n{lista[15]}: {lista[17]},\n{lista[18]}: {lista[20]},\n{lista[21]}: {lista[23]},\n{lista[24]}: {lista[26]}\n{lista[27]}: {lista[29]}\n{lista[30]}: {lista[32]}\n{lista[33]}: {lista[35]}\n{lista[36]}: {lista[38]}\n{lista[39]}: {lista[41]}\n{lista[42]}: {lista[44]}\n{lista[45]}: {lista[47]}\n{lista[48]}: {lista[50]}\n{lista[51]}: {lista[53]}\n{lista[54]}: {lista[56]}\n{lista[57]}: {lista[59]}\n{lista[60]}: {lista[62]}\n{lista[63]}: {lista[65]}\n{lista[66]}: {lista[68]}\n{lista[69]}: {lista[71]}"
				# print(lista_prava)
				# to ustvari variable za vsako št. torej shrani v 'st_36, '
				stevilke[f"st_{i}"] = lista_prava
					
			except:
				print(f"Številka {i} ne obstaja!")
				lista = "-"
				stevilke[f"st_{i}"] = lista

	except NoSuchElementException:
		driver.find_element_by_xpath("//a[@class='action primary']").click()


		wait = WebDriverWait(driver, 100)
		element = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "store-name"), "Mass Čopova Ljubljana"))
		search = driver.find_element_by_id("stock-popup").text
		lista = search.split("\n")
		st = lista.index("LJUBLJANA")
		for x in range(0, st):
			lista.remove(lista[0])
		for m in mesta:
			lista.remove(m)

		lista_prava = f"{lista[0]}: {lista[2]},\n{lista[3]}: {lista[5]},\n{lista[6]}: {lista[8]},\n{lista[9]}: {lista[11]},\n{lista[12]}: {lista[14]},\n{lista[15]}: {lista[17]},\n{lista[18]}: {lista[20]},\n{lista[21]}: {lista[23]},\n{lista[24]}: {lista[26]}\n{lista[27]}: {lista[29]}\n{lista[30]}: {lista[32]}\n{lista[33]}: {lista[35]}\n{lista[36]}: {lista[38]}\n{lista[39]}: {lista[41]}\n{lista[42]}: {lista[44]}\n{lista[45]}: {lista[47]}\n{lista[48]}: {lista[50]}\n{lista[51]}: {lista[53]}\n{lista[54]}: {lista[56]}\n{lista[57]}: {lista[59]}\n{lista[60]}: {lista[62]}\n{lista[63]}: {lista[65]}\n{lista[66]}: {lista[68]}\n{lista[69]}: {lista[71]}"
		# print(lista_prava)
		# lista.remove()
		# print(lista)
		# lista_prava = f"{lista['ola']}"
		# lista_prava = f"{lista[3]}: {lista[5]},\n{lista[6]}: {lista[8]},\n{lista[9]}: {lista[11]},\n{lista[12]}: {lista[14]},\n{lista[15]}: {lista[17]},\n{lista[18]}: {lista[20]},\n{lista[22]}: {lista[24]},\n{lista[26]}: {lista[28]},\n{lista[30]}: {lista[32]}\n{lista[34]}: {lista[36]}\n{lista[38]}: {lista[40]}\n{lista[41]}: {lista[43]}\n{lista[45]}: {lista[47]}\n{lista[48]}: {lista[50]}\n{lista[52]}: {lista[54]}\n{lista[56]}: {lista[58]}\n{lista[60]}: {lista[62]}\n{lista[64]}: {lista[66]}\n{lista[68]}: {lista[70]}\n{lista[72]}: {lista[74]}\n{lista[76]}: {lista[78]}\n{lista[80]}: {lista[82]}\n{lista[84]}: {lista[86]}\n{lista[88]}: {lista[89]}"
		stevilke[f"st_36"] = lista_prava
	# print(lista_prava)

	print("------------------------------------")


	driver.quit()


if __name__ == "__main__":
	zaloga(linki_artiklov)


