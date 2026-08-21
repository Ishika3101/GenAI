#race condition as what data are we modyfing we have no control over it and which thread is controlling it we have no idea of it 
import threading

chai_stock=0

def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock +=1

threads=[threading.Thread(target=restock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print(chai_stock)