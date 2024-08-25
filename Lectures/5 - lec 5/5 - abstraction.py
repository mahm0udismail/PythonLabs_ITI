"""
    abstraction:
        hiding of implementation, focusing on specifications.

    # no interfaces
        support multiple inheritance
"""

from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def say_hello(self):
        pass


class SuperHero(Person):

    def say_hello(self):
        print("Hello")


my_object = SuperHero()
my_object.say_hello()




class FileOperations(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def write(self):
        pass



class AWSS3FileOperations(FileOperations):
    def open(self):
        pass

    def write(self):
        pass


class DigitalOceanS3FileOperations(FileOperations):
    def open(self):
        pass

    def write(self):
        pass


class GoogleCloudS3FileOperations(FileOperations):
    def open(self):
        pass

    def write(self):
        pass










