

from abc import ABC, abstractmethod
class NotificationSystem:
    """Централизованная система наблюдения."""
    
    def __init__(self):
        self.__observers = set()
    
    def attach(self, observer):
        self.__observers.add(observer)
   
   
    def notify(self):
        for observer in self.__observers:
            observer.make_message()


class AbstractObserver(ABC):
    @abstractmethod
    def make_message(self):
        pass
class Notification(AbstractObserver):
    """Камера наблюдения."""
    
    def __init__(self, name):
        self.name = name
    def make_message(self):
        print('{} отправть сообщение'.format(self.name))

