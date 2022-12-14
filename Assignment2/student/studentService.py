import sys

sys.path.append('../globalVar')
from globalVar.types import studentsQueue
sys.path.append('../task')
from task.backgroundTask import BackgroundService
class Student:
    def __init__(self):
        BackgroundService()
        
    def add(self, studentCode, studentName, birthdate, learningPoint):
        studentsQueue.put({'action': 'add', 'data': {'studentCode': studentCode, 'studentName': studentName,
                        'birthdate': birthdate, 'learningPoint': learningPoint
                        }})
        print('Position in the queue: %i' % (studentsQueue.qsize()))
        
    def remove(self, studentCode):
        studentsQueue.put({'action': 'remove', 'data': {'studentCode': studentCode}})
        print('Position in the queue: %i' % (studentsQueue.qsize()))