class TravelOrganizer(object):
	def __init__(self):
		print("Agen Travel:: Biarkan saya mengatur perjalanan untuk Anda!")

	def arrangeTravel(self,destination,typeoftravel):
		print("Tujuannya adalah {}".format(destination))

		self.meansoftransport = Transporter(destination = destination,typeoftravel = typeoftravel)
		self.meansoftransport.bookTravel()

		self.meansofsleeping = Hotelier()
		self.meansofsleeping.bookRoom()
		self.meansofsleeping.arrangeFood()

class Transporter(object):
	def __init__(self, destination ,typeoftravel):
		print("Mengatur transportasi ke tujuan: {} naik: {} ---".format(destination,typeoftravel))
		self.destination = destination
		self.typeoftravel = typeoftravel

	def bookTravel(self):
		if self.typeoftravel == 'owncar':
			print("Tidak ada yang dipesan, pelanggan menggunakan mobilnya sendiri!")
		elif self.typeoftravel == 'pesawat':
			print("Pesan kursi untuk bepergian ke: {} naik PESAWAT!".format(self.destination))
		elif self.typeoftravel == 'bus':
			print("Pesan kursi untuk bepergian ke: {} naik BUS!".format(self.destination))

class Hotelier(object):
	def __init__(self):
		print('Mengatur ruangan untuk pelanggan.. ---')

	def roomFree(self):
		print('Memeriksa apakah masih ada kamar kosong?')
		return True

	def bookRoom(self):
		if self.roomFree():
			print('Pesan kamar untuk pelanggan!')

	def arrangeFood(self):
		print('Menyiapkan makanan untuk pelanggan!')

class RoadTripping(object):
	def __init__(self):
		print('Mengatur beberapa tamasya untuk pelanggan. ---')

	def arrangeTour(self):
		print('Mengatur beberapa tempat mewah untuk dikunjungi!')

class You(object):
	def __init__(self, name):
		print('Saya:: Whohoooooo kita jalan-jalan: {}'.format(name))

	def talkToAgent(self):
		print('Saya:: Meminta agen travel untuk mengatur perjalana akhir pekan ini!')
		manager = TravelOrganizer()
		manager.arrangeTravel(destination='Jakarta',typeoftravel='pesawat')

	def __del__(self):
		print('Saya:: Terima kasih tuan manajer telah mengatur kami akhir pekan yang indah ini!')

Me = You('Danil')
Me.talkToAgent()