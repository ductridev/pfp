import sys
import json
import time
from pynput import keyboard

from student.studentService import Student

sys.path.append('../globalVar')
from globalVar.types import ASSETS_DIR

class Main:
    def __init__(self):
        self.student = Student()
    
    def studentList(self):
        while True:
            try:
                fStudents = open(ASSETS_DIR + 'students.json')
                studentsData = json.load(fStudents)
                fStudents.close()
            except:
                fStudents = open(ASSETS_DIR + 'students.json', 'w+')
                fStudents.write('')
                fStudents.close()
                studentsData = []

            if len(studentsData) > 0:
                print('Students List: ')
                for idx, obj in enumerate(studentsData):
                    print('''
Student code: %s
Student name: %s
Date of birth: %s
Learning point: %s
                    ''' % (obj['studentCode'], obj['studentName'], obj['birthdate'], obj['learningPoint']))
                    print('---------------------------')
            else:
                print('There are no students on the list!')
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
    
    def studentLookUp(self, studentName):
        while True:
            studentName = input('Please enter student name: ')
            try:
                fStudents = open(ASSETS_DIR + 'students.json')
                studentsData = json.load(fStudents)
                fStudents.close()
            except:
                fStudents = open(ASSETS_DIR + 'students.json', 'w+')
                fStudents.write('')
                fStudents.close()
                studentsData = []
                
            if len(studentsData) > 0:
                for idx, obj in enumerate(studentsData):
                    if str(obj['studentName']).find(studentName) != -1:
                        print('''
Student code: %s
Student name: %s
Date of birth: %s
Learning point: %s
                        ''' % (obj['studentCode'], obj['studentName'], obj['birthdate'], obj['learningPoint']))
                        print('---------------------------')
            else:
                print('There are no students on the list!')
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
    
    def addStudent(self):
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
                        if isinstance(event, keyboard.Events.Release):
                            pass
                        else :
                            input()
                            break
    
    def removeStudent(self, studentCode):
        while True:
            try:
                fStudents = open(ASSETS_DIR + 'students.json')
                studentsData = json.load(fStudents)
                fStudents.close()
            except:
                print('No students to remove!')
                return
            for idx, obj in enumerate(studentsData):
                if obj['studentCode'] == studentCode:
                    print('Removing student from database. Please wait!')
                    self.student.remove(studentCode)
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
        while True:
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
                    print('Enter new student:')
                    self.addStudent()
                case 2:
                    studentName = print('Enter student name to look up: ')
                    self.studentLookUp(studentName=studentName)
                case 3:
                    self.studentList()
                case 4:
                    print('Enter new student:')
                    self.addStudent()
                case 5:
                    studentCode = input('Enter student code to remove: ')
                    self.removeStudent(studentCode)
                case 6:
                    break
                
if __name__ == '__main__':
    Main().start()