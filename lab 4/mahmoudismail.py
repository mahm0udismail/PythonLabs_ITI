# 1 - 
# Class Person:
# 		attributes: name, age
# 		methods: say_hello, say_age

# class SuperHero: that inherits from person
# 		 attributes += secret_identity, nemesis
# 		 methods: reveal_secret_identity, say_hello, old_say_age, say_age
import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print("Hello my name is " + self.name)
    def say_age(self,num=0):
        print(self.age-num)

class SuperHero(Person):
    def __init__(self, name, age, secret_identity,nemesis):
        super().__init__(name, age)
        self.secret_identity = secret_identity
        self.nemesis = nemesis
    def reveal_secret_identity(self):
        print(self.secret_identity)
    def old_say_age(self):
        super().say_age(num=1)
        


print("q1--------------------------")
p1 = Person(name="ismail",age=24)
p1.say_hello()
p1.say_age()
sh1 = SuperHero(name="ismail",age=24,secret_identity= "me",nemesis="any")
sh1.reveal_secret_identity()
sh1.old_say_age()
sh1.say_age()


# 2 - A Queue is a linear structure which follows a particular order in which the operations are performed.
# The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a
# resource where the consumer that came first is served first.

# We need to implement a python class that represents the queue data structure:

# 	The class should have these operations:
# 		- enqueue(value) => inserts a new value at the rear of the queue
# 		- dequeue() 	 => returns and removes a value from the front of the queue.
# 				    We should return None and print a warning message if we tried to pop value from an empty queue
# 		- is_empty() 	 => which returns True or False to represent whether the queue is empty or not

class Queue:
    def __init__(self):
        self.l=[]
    def enqueue (self,x):
        self.l.append(x)
        print(self.l)
    def dequeue (self):
        return self.l.pop(0)
    def is_empty (self):
        return len(self.l) == 0

print("q2--------------------------")        
q1 = Queue()
q1.enqueue(5)
print(q1.is_empty())  
print(q1.dequeue())
print(q1.is_empty())  


# 3 - We need to implement another queue class that has the same properties as previous but with the following changes:
# 	A. The queue should have a name that is provided as a parameter for its initializer
# 	B. The queue should have a size that is provided as a parameter of its initializer 
# 	   and if we tried to insert more values than its size raises a custom created exception called QueueOutOfRangeException
# 	C. The Queue class keeps track of all queues instances that has been created through this class 
# 	   and we can get any queue of them using its name
# 	D. The queue class should have two class methods called (save, load) 
# 	   which saves all created queues instances to a file and load them when needed. (bonus)
class QueueOutException(Exception):
    def __init__(self, message="Queue size limit exceeded"):
        self.message = message
        super().__init__(self.message)

class QueueUpdate(Queue):
    filename='data.json'
    track = {}
    def __init__(self,name,size):
        super().__init__()
        self.name = name
        self.size = size
        QueueUpdate.track[name] = self
    def enqueue(self,value):
        if len(self.l) >= self.size:
            raise QueueOutException(f"Cannot add {value} to {self.name}; size is {self.size}.")
        self.l.append(value)
        print(f"add {value} to {self.name} {self.l}.")
    @classmethod
    def getAllQueues(cls,name):
        if name in cls.track:
            return cls.track
        else:
            return "not in queue"
    @classmethod
    def save(cls):
        # Save the state of all queue instances to a file
        with open(cls.filename, 'w') as file:
            data = {key: {'size': value.size, 'queue': value.l} for key, value in cls.track.items()}
            json.dump(data, file, indent=4)
        print(f"All saved at {cls.filename}")

    @classmethod
    def load(cls):
        with open(cls.filename, 'r') as file:
            data = json.load(file)
            cls.track = {key: value for key, value in data.items()}
            print(cls.track )
        print(f"All loaded from {cls.filename}")


    
print("q3--------------------------")
q2 = QueueUpdate("new",2)
q2.enqueue(1)
q2.enqueue(2)
# q2.enqueue(3)
# q2.enqueue(4)
# print(q2.dequeue())
print(q2.is_empty())
q2.save()

print(QueueUpdate.getAllQueues("new"))

q23 = QueueUpdate("new2",2)
q23.enqueue(8)
q23.enqueue(5)
# q2.enqueue(3)
# q2.enqueue(4)
# print(q2.dequeue())
print(q23.is_empty())
q23.save()
q23.load()