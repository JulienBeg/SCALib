import threading
import queue
import numpy as np

class DataReader(threading.Thread):
    def __init__(self,file_read,max_depth=1):
        super(DataReader,self).__init__()
        self.file_read = file_read
        self.max_depth = max_depth
        self.queue = queue.Queue(maxsize=max_depth)

    def run(self):
        for files in self.file_read:
            rets = ()
            for fname,labels in files:
                read = np.load(fname,allow_pickle=True)
                if labels is None:
                    rets +=([read],)
                else:
                    rets +=([read[l] for l in labels],)
            self.queue.put(rets)
        self.queue.put(None)
        return

