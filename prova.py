from posiljanje import posiljanje

try:
	def ola():
		x = input("vnsei st: ")
		print(int(x))
	ola()


except:
	try:
		ola()
	except Exception as error:
		posiljanje("vanjermancek@gmail.com", "prislo je do napake", f"{error}")
