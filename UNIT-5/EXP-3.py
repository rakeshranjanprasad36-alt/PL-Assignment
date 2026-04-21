from collections import deque
class Queue:
  def __init__(self):
    self.queue = deque()

  def enqueue(self, item):
    self.queue.append(item)
    print(f"Added {item} to the queue.")

  def safe_dequeue(self):
    if not self.queue:
        print("The queue is empty, nothing to remove.")
        return None
    return self.queue.popleft()
  
  def display(self):
    print("Queue elements:", list(self.queue))

if __name__ == "__main__":
  my_queue = Queue()
  my_queue.safe_dequeue() 
  my_queue.enqueue(10)
  my_queue.enqueue(20)
  my_queue.display()
  print("Removed item:", my_queue.safe_dequeue())
  my_queue.display()