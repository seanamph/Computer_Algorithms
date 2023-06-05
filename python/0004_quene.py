from queue import Queue

queue = Queue()  # 創建一個空的隊列

queue.put(1)  # 將元素1放入隊列
queue.put(2)  # 將元素2放入隊列
queue.put(3)  # 將元素3放入隊列

print(queue.qsize())  # 輸出隊列中的元素數量

queue.get()  # 從隊列中取出元素

print(queue.qsize())  # 再次輸出隊列中的元素數量
