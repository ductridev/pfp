import sys

sys.path.append('../globalVar')
from globalVar.types import studentsQueue

class Drink:
    def __init__(self):
        pass
        
    def add(self, studentCode, studentName, birthdate, learningPoint):
        studentsQueue.put({'action': 'add', 'glocery': 'drink', 'data': {'studentCode': studentCode, 'studentName': studentName,
                        'birthdate': birthdate, 'learningPoint': learningPoint
                        }})
        print('Position in the queue: %i' % (studentsQueue.qsize()))
        
    def remove(self, studentCode):
        studentsQueue.put({'action': 'remove', 'data': {'studentCode': studentCode}})
        print('Position in the queue: %i' % (studentsQueue.qsize()))