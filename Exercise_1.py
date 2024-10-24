# TC O(1) all except show O(n)
# SC O()
class myStack:
  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file
     def __init__(self):
        self.arr=[]
         
     def isEmpty(self):
        return len(self.arr)==0
         
     def push(self, item):
        self.arr.append(item)

     def pop(self):
        if self.isEmpty:
           return None

        return self.arr.pop(-1)

     def peek(self):
        if self.isEmpty():
           return None
        return self.arr[-1]

     def size(self):
        return len(self.arr)
         
     def show(self):
        for i in range(len(self.arr)):
           print(self.arr[i])
         

s = myStack()
# s.push('1')
# s.push('2')
print(s.pop())
print(s.show())
