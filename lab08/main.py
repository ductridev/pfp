import sys
from pynput import keyboard
from functools import partial
import os

from glocery.Product import Product

sys.path.append('../globalVar')
from globalVar.types import DATABASE_DIR

sys.path.append('../task')
from task.backgroundTask import BackgroundService

class Main:
    def __init__(self):
        self.product = Product()
        self.database = ''
    
    def productListAll(self):
        while True:
            productsData = list[str]
            try:
                fProduct = open(DATABASE_DIR + self.database)
                fProduct.close()
            except:
                fProduct = open(DATABASE_DIR + self.database, 'w+')
                fProduct.close()

            num_lines = sum(1 for line in open(DATABASE_DIR + self.database))
    
            if num_lines > 0:
                print('Products List: ')
                fProduct = open(DATABASE_DIR + self.database)
                nbytes = 1 << 10
                
                for productsData in iter(partial(fProduct.readlines, nbytes), []):
                    for i in range(0, len(productsData) ):
                        obj = productsData[i].strip("\n").split()
                        print('---------------------------')
                        print('''%s %s %s %s''' % (obj[0], obj[1], obj[2], obj[3]))
                fProduct.close()
                print('---------------------------')
            else:
                print('No products available currently!')

            print('Press enter to continue, Esc to return the main menu!')
            with keyboard.Events() as events:
                for event in events:
                    if event.key == keyboard.Key.esc:
                        return
                    else:
                        if isinstance(event, keyboard.Events.Release):
                            pass
                        else :
                            input()
                            break  
    
    def productList(self):
        while True:
            productName = input('Which item would you like to search for? ')
            productsData = list[str]
            try:
                fProduct = open(DATABASE_DIR + self.database)
                fProduct.close()
            except:
                fProduct = open(DATABASE_DIR + self.database, 'w+')
                fProduct.close()
                
            num_lines = sum(1 for line in open(DATABASE_DIR + self.database))
    
            if num_lines > 0:
                fProduct = open(DATABASE_DIR + self.database)
                nbytes = 1 << 10
                
                for productsData in iter(partial(fProduct.readlines, nbytes), []):
                    for i in range(0,len(productsData)):
                        if productName.lower() in productsData[i].lower():
                            obj = productsData[i].strip("\n").split()
                            print('''Here is the product information:
%s %s %s %s
                            ''' % (obj[0], obj[1], obj[2], obj[3]))

                            fProduct.close()
                            return

                fProduct.close()

                print('Sorry we do not have %s in the store!' %(productName))
            else:
                print('No products available currently!')

            print('Press enter to continue, Esc to return the main menu!')
            with keyboard.Events() as events:
                for event in events:
                    if event.key == keyboard.Key.esc:
                        return
                    else:
                        if isinstance(event, keyboard.Events.Release):
                            pass
                        else :
                            input()
                            break
    
    def addProduct(self):
        while True:
            productID = input('Product ID: ')
            productName = input('Product name: ')
            productPrice = input('Price of the product: ')
            productCategory = input('Category of products: ')
            try:
                fProduct = open(DATABASE_DIR + self.database)
                fProduct.close()
            except:
                print('No products to remove!')
                return

            num_lines = sum(1 for line in open(DATABASE_DIR + self.database))
    
            if num_lines > 0:
                fProduct = open(DATABASE_DIR + self.database)
                nbytes = 1 << 10

                for productsData in iter(partial(fProduct.readlines, nbytes), []):
                    for i in range(0,len(productsData)):
                        if productID.lower() in productsData[i].lower():
                            print('Product ID must be unique!')
                            return
                        elif productName.lower() in productsData[i].lower():
                            print('Product name must be unique!')
                            return

            print('Adding new product to store. Please wait!')
            self.product.add(productID, productName, productPrice, productCategory)
            print('Press enter to continue, Esc to return the main menu!')
            with keyboard.Events() as events:
                for event in events:
                    if event.key == keyboard.Key.esc:
                        return
                    else:
                        if isinstance(event, keyboard.Events.Release):
                            pass
                        else :
                            input()
                            break
    
    def removeProduct(self):
        while True:
            productID = input('Which is the ID number of the product to delete')
            try:
                fProduct = open(DATABASE_DIR + self.database)
                fProduct.close()
            except:
                print('No products to remove!')
                return

            num_lines = sum(1 for line in open(DATABASE_DIR + self.database))
    
            if num_lines > 0:
                fProduct = open(DATABASE_DIR + self.database)
                nbytes = 1 << 10

                for productsData in iter(partial(fProduct.readlines, nbytes), []):
                    for i in range(0,len(productsData)):
                        if productID.lower() in productsData[i].lower():
                            print('Removing product from database. Please wait!')
                            self.product.remove(productID)

                            fProduct.close()
                            return

                fProduct.close()

            else:
                print('No products available currently!')

            print('Press enter to continue, Esc to return the main menu!')
            with keyboard.Events() as events:
                for event in events:
                    if event.key == keyboard.Key.esc:
                        return
                    else:
                        if isinstance(event, keyboard.Events.Release):
                            pass
                        else :
                            input()
                            break  

    def changeProductPrice(self):
        while True:
            productID = input('Which is the ID number of the item in question?')
            productName = ''
            try:
                fProduct = open(DATABASE_DIR + self.database)
                fProduct.close()
            except:
                print('No products to remove!')
                return

            num_lines = sum(1 for line in open(DATABASE_DIR + self.database))
    
            if num_lines > 0:
                fProduct = open(DATABASE_DIR + self.database)
                nbytes = 1 << 10
                
                for productsData in iter(partial(fProduct.readlines, nbytes), []):
                    for i in range(0,len(productsData)):
                        if productID.lower() in productsData[i].lower():
                            productName = productsData[i].strip("\n").split()[1]

                            newPrice = input('What is the new price for %s?'%(productName))
                            print('Changing product price from database. Please wait!')
                            self.product.changePrice(productID, newPrice)

                            fProduct.close()
                            return

                fProduct.close()

            else:
                print('No products available currently!')

            print('Press enter to continue, Esc to return the main menu!')
            with keyboard.Events() as events:
                for event in events:
                    if event.key == keyboard.Key.esc:
                        return
                    else:
                        if isinstance(event, keyboard.Events.Release):
                            pass
                        else :
                            input()
                            break
    
    def start(self):
        print('Welcome to the glocery store!')
        self.database = str(input("Please input the file you'd like to load into stock: "))
        try:
            fProduct = open(DATABASE_DIR + self.database)
            fProduct.close()
        except:
            fProduct = open(DATABASE_DIR + self.database, 'w+')
            fProduct.close()
        BackgroundService().start(DATABASE_DIR + self.database)
        print('%s has been properly loaded into the database!'%(self.database))

        while True:
            print('''
1. Add new item
2. Delete item
3. Change the cost of item
4. Search for item
5. Display inventory details
6. Quit
                    ''')
            selected = input('Please select a number as an option from the options above: ')
            try:
                selected = int(selected)
            except:
                print("%s is not a number!" %(selected))
                pass
            match selected:
                case 1:
                    self.addProduct()
                case 2:
                    self.removeProduct()
                case 3:
                    self.changeProductPrice()
                case 4:
                    self.productList()
                case 5:
                    self.productListAll()
                case 6:
                    break
                case default:
                    print('Cannot recognize input %s!' %(selected))
                    pass
                
if __name__ == '__main__':
    Main().start()