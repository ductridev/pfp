import sys
import threading
from functools import partial
import time

sys.path.append('../utils')
from utils.sort import sort

sys.path.append('../globalVar')
from globalVar.types import productsQueue

class BackgroundService():
    def __init__(self):
        pass
    
    def backgroundService(self): 
        while True:
            try:
                fProduct = open(self.database)
                fProduct.close()
            except:
                fProduct = open(self.database, 'w+')
                fProduct.close()
            
            fProduct = open(self.database, 'r+')
            
            if productsQueue.empty() == False:
                productWaiting = productsQueue.get()
                           
                nbytes = 1 << 10

                num_lines = sum(1 for line in open(self.database))
                
                if num_lines > 0:
                    for productsData in iter(partial(fProduct.readlines, nbytes), []):
                        for i in range(0,len(productsData)):
                            if productWaiting['action'] == 'add':
                                fProduct.write('%s    %s    %s    %s\n' % (productWaiting['data']['productID'], productWaiting['data']['productName'], productWaiting['data']['productPrice'], productWaiting['data']['productCategory']))
                            elif productWaiting['action'] == 'remove':
                                if productWaiting['data']['productID'].lower() in productsData[i].lower():
                                    continue
                                else:
                                    fProduct.write(productsData[i])
                            elif productWaiting['action'] == 'change':
                                if productWaiting['data']['productID'].lower() in productsData[i].lower():
                                    fProduct.write('%s    %s    %s    %s\n' % (productWaiting['data']['productID'], productWaiting['data']['productName'], productWaiting['data']['productPrice'], productWaiting['data']['productCategory']))
                                else:
                                    fProduct.write(productsData[i])
                            else: 
                                print('Unknow command type: %s!'%(productWaiting['action']))
                    sort(fProduct)
                else:
                    if productWaiting['action'] == 'add':
                        fProduct.write('%s    %s    %s    %s\n' % (productWaiting['data']['productID'], productWaiting['data']['productName'], productWaiting['data']['productPrice'], productWaiting['data']['productCategory']))

            fProduct.close()
            
            time.sleep(0.1)

    def start(self, path):
        self.database = path
        daemon = threading.Thread(target=self.backgroundService, daemon=True, name='Database Async Process')
        daemon.start()

    def getQueueSize(self):
        return productsQueue.qsize()

    def addProduct2Queue(self, productID, productName, productPrice, productCategory):
        productsQueue.put({'action': 'add', 'glocery': 'stationery', 'data': {'productID': productID, 'productName': productName,
                        'productPrice': productPrice, 'productCategory': productCategory
                        }})
        return self.getQueueSize()

    def removeProductFromQueue(self, productID):
        productsQueue.put({'action': 'remove', 'data': {'productID': productID}})
        return self.getQueueSize()

    def changeProductPriceFromQueue(self, productID, productName, newPrice, productCategory):
        productsQueue.put({'action': 'change', 'data': {'productID': productID, 'productName': productName,
                        'productPrice': newPrice, 'productCategory': productCategory
                        }})
        return self.getQueueSize()