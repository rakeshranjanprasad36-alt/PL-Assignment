class Stack:
  def __init__(self):
    self.stack = []
  def push(self, item):
    self.stack.append(item)
    print(f"Added {item} to the stack.")

  def safe_pop(self):
    if not self.stack:
      print("The stack is empty, cannot remove anything.")
      return None
    return self.stack.pop()
  
  def display(self):
    print("Stack contents:", self.stack)

if __name__ == "__main__":
  my_stack = Stack()
  my_stack.safe_pop() 
  my_stack.push(10)
  my_stack.push(20)
  my_stack.display()
  print("Removed item:", my_stack.safe_pop())
  my_stack.display()
```
