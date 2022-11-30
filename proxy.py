from abc import ABC, abstractmethod

class Customer:
    """Customer object"""
    def __init__(self,age):
        self.__age = age
        
    def get_age(self):
        return self.__age
    
class IChannel(ABC):
    
    @abstractmethod
    def provide_broadcast(self):
        """Penyiaran"""
        
class Channel(IChannel):
    
    def provide_broadcast(self):
        print("Siaran dimulai...")
        
class ProxyChannel(IChannel):
    
    def __init__(self,customer: Customer):
        self.customer = customer
        self.channel = Channel()
        
    def provide_broadcast(self):
        customer_age = self.customer.get_age()
        if customer_age > 18:
            self.channel.provide_broadcast()
            print("Layanan ini terdaftar untuk penagihan.")
        else:
            print("Maaf, layanan ini tidak diperbolehkan untuk pelanggan di bawah usia 18 tahun.")

Damon = Customer(17)
P = ProxyChannel(Damon)
P.provide_broadcast()

Joe = Customer(21)
P = ProxyChannel(Joe)
P.provide_broadcast()