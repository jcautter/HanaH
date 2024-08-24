class A:
    A:str = 'A'
    def __init_(self):
        pass

class B(A):
    B:str = 'B'
    def __init_(self):
        pass

class C(A):
    C:str = 'C'
    def __init_(self):
        pass


from data_model.DataModelWaiter import DataModelWaiter

a = DataModelWaiter(login='gar1')

from data_model.DataModelProduct import DataModelProduct

b = DataModelProduct(
    name = 'Batata'
    , short_description = 'Batata frita'
    , description = 'Batata frita média'
    , value = 19.90
    , category = 'Aperitivos'
)

from data_model.DataModelOrder import DataModelOrder

c = DataModelOrder(
    waiter = a
    , product = b
    , quantity = 1
)

d = DataModelOrder(**c._get_dict())

print(d._get_dict())