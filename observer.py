from abc import ABC, abstractmethod

class AvengersTeam(ABC):
    @abstractmethod
    def attach(self, observer):
        pass
    
    @abstractmethod
    def detach(self, observer):
        pass
    
    @abstractmethod
    def notify(self):
        pass


class ConcreteAvengersTeam(AvengersTeam):
    _observers_list = list()

    def attach(self, observer):
        print(f'{observer.name} ditambahkan ke tim Avengers!')
        self._observers_list.append(observer)

    def detach(self, observer):
        print(f'{observer.name} Dihapus dari Tim Avengers!')
        self._observers_list.remove(observer)

    def notify(self):
        print('Avengers berkumpul!')
        for observer in self._observers_list:
            observer.update()

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class IronMan(Observer):
    name = "Iron Man"

    def update(self):
        print('Iron Man SIAPPP!!!')

class CaptainAmerica(Observer):
    name = "Captain America"

    def update(self):
        print('Captain America SIAPPP!!!')

class Thor(Observer):
    name = "Thor"

    def update(self):
        print('Thor SIAPPP!!!')

class BlackWidow(Observer):
    name = "Black Widow"

    def update(self):
        print('Black Widow SIAPPP!!!')

class Hulk(Observer):
    name = "Hulk"

    def update(self):
        print('Hulk SIAPPP!!!')

class SpiderMan(Observer):
    name = "Spider Man"

    def update(self):
        print('Spider Man SIAPPP!!!')



if __name__ == "__main__":

    publisher = ConcreteAvengersTeam()

    iron_man = IronMan()
    publisher.attach(iron_man)

    captain_america = CaptainAmerica()
    publisher.attach(captain_america)

    thor = Thor()
    publisher.attach(thor)

    black_widow = BlackWidow()
    publisher.attach(black_widow)

    hulk = Hulk()
    publisher.attach(hulk)

    spider_man = SpiderMan()
    publisher.attach(spider_man)

    publisher.detach(spider_man)

    print('\nSpider Man: mengapa kalian selalu melakukan ini padaku?\n')

    publisher.notify()