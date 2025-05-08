"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass
import datetime
class Product(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_name','_category', '_price']
    # Class header title
    header = 'Product'
    # field description for use in, for example, input form
    des = ['Id','Name','Category','Price']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, name, category, price):
        super().__init__()
        # Object attributes
        id = Product.get_id(id)
        self._id = id
        self._name = name
        self._category = category
        self._price = price
        # Add the new object to the dictionary of objects
        Product.obj[id] = self
        # Add the id to the list of object ids
        Product.lst.append(id)
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
    def category(self):
        return self._category
    # dob property setter method
    @category.setter
    def category(self, category):
        self._category = category
    
    @property
    def price(self):
        return self._price
    # dob property setter method
    @price.setter
    def price(self, price):
        self._price = price

