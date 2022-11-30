from abc import ABC, abstractmethod

class Command(ABC): 
    @abstractmethod
    def execute(self) -> None:
        pass

class GarageOpenCommand(Command):
	def __init__(self, garage_receiver):
		self._garage_receiver = garage_receiver


	def execute(self) -> None:
		print("Perintah untuk membuka pintu garasi.")
		self._garage_receiver.open_door()

class GarageCloseCommand(Command):
	def __init__(self, garage_receiver):
		self._garage_receiver = garage_receiver

	def execute(self) -> None:
		
		print("Perintah untuk menutup pintu garasi")
		self._garage_receiver.close_door()

class GarageReceiver:
	def open_door(self):
		print("Membuka Pintu Garasi.")

	def close_door(self):
		print("Menutup pintu garasi")

class ApplicationInvoker:
	"""
    Kode aplikasi untuk menyediakan API untuk membuka dan menutup pintu
	"""

	def __init__(self):
		receiver = GarageReceiver()
		self._open_door = GarageOpenCommand(garage_receiver=receiver)
		self._close_door = GarageCloseCommand(garage_receiver=receiver)

		

	def invoke_open_door(self):
		print("Aplikasi Menginisiasi Pintu Garasi Buka")
		self._open_door.execute()

	def invoke_close_door(self):
		print("Aplikasi Menginisiasi Pintu Garasi Tutup")
		self._close_door.execute()

if __name__ == '__main__':

	# membuat object untuk class ApplicationInvoker
	app = ApplicationInvoker()

	# Mari kita panggil perintah untuk membuka pintu dulu
	app.invoke_open_door()
	print()

	# Mari kita panggil perintah untuk menutup pintu 
	app.invoke_close_door()