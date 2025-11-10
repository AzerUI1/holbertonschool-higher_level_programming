#!/usr/bin/python3
'''Write a class Student that defines a student'''


class Student:
    '''Defines a student by: (based on 10-student.py)'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        '''Retrieve a dictionary representation of a Student instance'''
        return self.__dict__
