"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass
import datetime
class Store(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_name','_location']
    # Class header title
    header = 'Store'
    # field description for use in, for example, input form
    des = ['Id','Name','Location']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, name, location):
        super().__init__()
        # Object attributes
        id = Store.get_id(id)
        self._id = id
        self._name = name
        self._location = location
        # Add the new object to the dictionary of objects
        Store.obj[id] = self
        # Add the id to the list of object ids
        Store.lst.append(id)
    # id property getter method
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
    # name property getter method
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    # dob property getter method
    @property
    def location(self):
        return self._location
    # dob property setter method
    @location.setter
    def location(self, location):
        self._location = location

