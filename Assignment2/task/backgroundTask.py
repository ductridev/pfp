import sys
import threading
import json
import time

sys.path.append('../globalVar')
from globalVar.types import ASSETS_DIR, studentsQueue

class BackgroundService():
    def __init__(self):
        print('Starting background task')
        daemon = threading.Thread(target=self.backgroundService, daemon=True, name='JSON Files Async')
        daemon.start()

    def backgroundService(self): 
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
            
            studentsWaiting = studentsQueue.get()
            
            for idx, obj in enumerate(studentsData): 
                if obj['studentCode'] == studentsWaiting['data']['studentCode']:
                    studentsData.pop(idx)

            if studentsWaiting['action'] == 'add':
                studentsData.append(studentsWaiting['data'])
                    
            studentsData = sorted(studentsData, key=lambda k: k['studentName'])
            
            fStudents = open(ASSETS_DIR + 'students.json', 'w+', encoding='utf8')
            fStudents.write(json.dumps(studentsData, indent=4))
            fStudents.close()
            
            time.sleep(0.1)