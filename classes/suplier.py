"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass
import datetime
class Suplier(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_name','_contact']
    # Class header title
    header = 'Store'
    # field description for use in, for example, input form
    des = ['Id','Name','Contact']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, name, contact):
        super().__init__()
        # Object attributes
        id = Suplier.get_id(id)
        self._id = id
        self._name = name
        self._contact = contact
        # Add the new object to the dictionary of objects
        Suplier.obj[id] = self
        # Add the id to the list of object ids
        Suplier.lst.append(id)
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
    def contact(self):
        return self._contact
    # dob property setter method
    @contact.setter
    def contact(self, contact):
        self._contact = contact

