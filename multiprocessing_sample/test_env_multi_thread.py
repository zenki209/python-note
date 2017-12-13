import os
import time
import threading

def worker1():
    os.environ["ABC"] = "process 1"
    while True:
        time.sleep(2)
        print("ppppppppppppppppp 1: {}".format(os.environ["ABC"]))
     

def worker2():
    os.environ["ABC"] = "process 2"
    while True:
        time.sleep(2)
        print("ppppppppppppppppp 2: {}".format(os.environ["ABC"]))
     

p1 = threading.Thread(target=worker1, args=())
p1.start()

p2 = threading.Thread(target=worker2, args=())
p2.start()

os.environ["ABC"] = "process 0"
while True:
    time.sleep(2)
    print("ppppppppppppppppp 0: {}".format(os.environ["ABC"]))
