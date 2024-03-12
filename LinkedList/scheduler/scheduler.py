from queue import Queue
from t2 import CircularQueue
class Scheduler:
    def __init__(self, processArray, processArrayLength, timeQuantum):
        self.processArray = processArray
        self.processArrayLength = processArrayLength
        self.timeQuantum = timeQuantum

    def assignProcessor(self):
        q = CircularQueue(self.processArrayLength)
        for i  in range(self.processArrayLength):
            time = self.processArray[i].processExecTime
            q.enqueue(time) 
            print(time)

        while not q.is_empty():
            i = 0

