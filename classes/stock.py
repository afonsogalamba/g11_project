"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass
import datetime
from classes.store import Store
from classes.product import Product
class Stock(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_store_id','_product_id', '_level','_restock_date']
    # Class header title
    header = 'Stock'
    # field description for use in, for example, input form
    des = ['Id','Store Id','Product Id','Level','Restock Date']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, store_id, product_id, level, restock_date):
        super().__init__()
        # Object attributes
    
        store_id = int(store_id)
        product_id = int(product_id)
        if store_id in Store.lst:
            if product_id in Product.lst:
                id = Stock.get_id(id)
                self._id = id
                self._store_id = store_id
                self._product_id = product_id
                self._level= level
                self._restock_date = datetime.datetime.strptime(restock_date, "%d/%m/%Y")
                Stock.obj[id] = self
                Stock.lst.append(id)
            else:
                print('Product ', product_id, ' not found')
        else:
            print('Store', store_id, ' not found')

    # id property getter method
    @property
    def id(self):
        return self._id
    @property
    def store_id(self):
        return self._store_id
    @property
    def product_id(self):
        return self._product_id
    # name property getter method
    @property
    def level(self):
        return int(self._level)
    @level.setter
    def level(self, level):
        if level > 0:
            self._level = level
    # dob property getter method
    @property
    def restock_date(self):
        return self._restock_date
    # dob property setter method
    @restock_date.setter
    def restock_date(self, restock_date):
        self._restock_date = restock_date

