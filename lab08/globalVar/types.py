import os
import queue

DATABASE_DIR = os.getcwd() + '/database'
studentsQueue = queue.Queue()
DATABASE_EXT = 'txt'