import sys
import json
from pynput import keyboard

from glocery.Drink import Drink
from glocery.Food import Food
from glocery.Seasoning import Seasoning
from glocery.Stationery import Stationery

sys.path.append('../globalVar')
from globalVar.types import DATABASE_DIR, DATABASE_EXT

class Main:
    def __init__(self):
        self.drink = Drink()
        self.food = Food()
        self.seasoning = Seasoning()
        self.stationery = Stationery()
    
    def productListAll(self, productKind):
        while True:
            productsData = list[str]
            try:
                fProduct = open(DATABASE_DIR + productKind + '.' + DATABASE_EXT)
                productsData = fProduct.readlines()
                fProduct.close()
            except:
                fProduct = open(DATABASE_DIR + productKind + '.' + DATABASE_EXT, 'w+')
                fProduct.write('')
                fProduct.close()

            if len(productsData) > 0:
                print('Students List: ')
                for idx, obj in enumerate(productsData):
                    print('---------------------------')
                    print('''
Student code: %s
Student name: %s
Date of birth: %s
Learning point: %s
                    ''' % (obj['studentCode'], obj['studentName'], obj['birthdate'], obj['learningPoint']))
                    print(studentsData)
            else:
                print('There are no students on the list!')
            print('Press enter to continue, Esc to return the main menu!')
            with keyboard.Events() as events:
                for event in events:
                    if event.key == keyboard.Key.esc:
                        return
                    else:
                        pass
    
    def productList(self, productKind, productName):
        while True:
            studentName = input('Please enter student name: ')
            try:
                fStudents = open(DATABASE_DIR + 'students.json')
                studentsData = json.load(fStudents)
                fStudents.close()
            except:
                fStudents = open(DATABASE_DIR + 'students.json', 'w+')
                fStudents.write('')
                fStudents.close()
                studentsData = []
                
            if len(studentsData) > 0:
                for idx, obj in enumerate(studentsData):
                    if obj['studentName'] == studentName:
                        print('''
Student code: %s
Student name: %s
Date of birth: %s
Learning point: %s
                        ''' % (obj['studentCode'], obj['studentName'], obj['birthdate'], obj['learningPoint']))
                        return
            else:
                print('There are no students on the list!')
            print('Press enter to continue, Esc to return the main menu!')
            with keyboard.Events() as events:
                for event in events:
                    if event.key == keyboard.Key.esc:
                        return
                    else:
                        pass
    
    def addProduct(self, productKind):
        while True:
            studentCode = input('Student code: ')
            studentName = input('Student name: ')
            birthdate = input('Date of birth: ')
            point = input('Learning point: ')
            print('Adding new student to database. Please wait!')
            self.student.add(studentCode, studentName, birthdate, point)
            print('Press enter to continue, Esc to return the main menu!')
            with keyboard.Events() as events:
                for event in events:
                    if event.key == keyboard.Key.esc:
                        return
                    else:
                        pass
    
    def removeProduct(self, productKind, productCode):
        while True:
            try:
                fStudents = open(DATABASE_DIR + 'students.json')
                studentsData = json.load(fStudents)
                fStudents.close()
            except:
                print('No students to remove!')
                return
            for idx, obj in enumerate(studentsData):
                if obj['productCode'] == productCode:
                    print('Removing student from database. Please wait!')
                    self.student.remove(productCode)
            print('Press enter to continue, Esc to return the main menu!')
            with keyboard.Events() as events:
                for event in events:
                    if event.key == keyboard.Key.esc:
                        return
                    else:
                        pass                
    
    def start(self):
        productKind = str()
        allProductKinds = ['Drink', 'Food', 'Seasoning', 'Stationery']
        while True:
            if productKind != '':
                try:
                    changeProductKind = str(input('Do you want to change kind of product? (Y/n)'))
                except:
                    print('Cannot recognize input %s it must be string type!' %(changeProductKind))
                    pass
                if changeProductKind.lower() == 'y':   
                    try:  
                        print('All kinds of product: Drink, Food, Seasoning, Stationery')
                        productKind = str(input('Please enter kind of product: '))
                        if productKind in allProductKinds:
                            continue
                        else:
                            raise Exception()
                    except:
                        print('Cannot recognize input %s Or maybe it must be string type!' %(productKind))
                        pass
            else:
                try:  
                    print('All kinds of product: Drink, Food, Seasoning, Stationery')
                    productKind = str(input('Please enter kind of product: '))
                    if productKind in allProductKinds:
                        continue
                    else:
                        raise Exception()
                except:
                    print('Cannot recognize input %s it must be string type!' %(productKind))
                    pass
            print('''
1. Enter student list
2. Look up student
3. Display student list
4. Add students
5. Remove students
6. Exit
                    ''')
            try:
                selected = int(input('Please select a number as an option from the options above: '))
            except:
                pass
            match selected:
                case 1:
                    self.addProduct(productKind=productKind)
                case 2:
                    productName = print('Enter student name to look up: ')
                    self.productList(productKind=productKind, productName=productName)
                case 3:
                    self.productListAll(productKind=productKind)
                case 4:
                    print('Enter new student:')
                    self.addProduct(productKind=productKind)
                case 5:
                    productCode = print('Enter student code to remove: ')
                    self.removeProduct(productKind=productKind, productCode=productCode)
                case 6:
                    break
                
if __name__ == '__main__':
    Main().start()