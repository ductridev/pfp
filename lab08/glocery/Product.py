import sys

sys.path.append('../task')
from task.backgroundTask import BackgroundService

class Product:
    def __init__(self):
        pass
        
    def add(self, productID, productName, productPrice, productCategory):
        print('Order of commands in the queue: %i' % (BackgroundService().addProduct2Queue(productID, productName, productPrice, productCategory)))
        
    def remove(self, productID):
        print('Order of commands in the queue: %i' % (BackgroundService().removeProductFromQueue(productID)))

    def changePrice(self, productID, productName, newPrice, productCategory):
        print('Order of commands in the queue: %i' % (BackgroundService().changeProductPriceFromQueue(productID, productName, newPrice, productCategory)))