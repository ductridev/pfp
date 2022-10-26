import sys
import threading
import json
import time

sys.path.append('../globalVar')
from globalVar.types import DATABASE_DIR, studentsQueue

class BackgroundService():
    def __init__(self):
        daemon = threading.Thread(target=self.backgroundService, daemon=True, name='JSON Files Async')
        daemon.start()

    def backgroundService(self): 
        while True:
            try:
                fStudents = open(DATABASE_DIR + 'students.json')
                studentsData = json.load(fStudents)
                fStudents.close()
            except:
                fStudents = open(DATABASE_DIR + 'students.json', 'w+')
                fStudents.write('')
                fStudents.close()
                studentsData = []
            
            fStudents = open(DATABASE_DIR + 'students.json', 'w')
            
            studentsWaiting = studentsQueue.get()
            
            for idx, obj in enumerate(studentsData):
                for idx_, obj_ in enumerate(studentsWaiting): 
                    if obj['studentCode'] == obj_['data']['studentCode']:
                        studentsData.pop(idx)
                    if obj_['action'] == 'add':
                        studentsData.append(obj_['data'])
                    
            studentsData = sorted(studentsData, key=lambda k: k['studentName'])
            
            fStudents.write(json.dumps(studentsData, indent=4))
            
            time.sleep(0.1)