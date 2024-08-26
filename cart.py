from data_model.DataModelCart import DataModelCart
from data_model.DataModelWaiter import DataModelWaiter
from data_model.DataModelClient import DataModelClient

from data_model.DataModelOrder import DataModelOrder
from data_model.DataModelProduct import DataModelProduct

from datetime import datetime

prod1 = DataModelProduct(
    **{
        '_id': '001'
        , 'name': 'Suco de Laranja'
        , 'value': 7.5
    }
)

ord1 = DataModelOrder(
    **{
        'product': prod1
        , 'quantity': 2
    }
)

cart = DataModelCart(
    **{
        'date': datetime.now().isoformat(timespec='minutes')
    }
)

cart._append('list', ord1)

prod2 = DataModelProduct(
    **{
        '_id': '002'
        , 'name': 'Coca-cola'
        , 'value': 8.5
    }
)

ord2 = DataModelOrder(
    **{
        'product': prod2
        , 'quantity': 5
    }
)

cart._append('list', ord2)

cart2 = DataModelCart(**cart._get_dict())

waiter = DataModelWaiter(
    **{
        '_id': '021'
        , 'name': 'Luis'
        , 'company': 'Bar do Gomes'
    }
)

client = DataModelClient(
    **{
        '_id': '021'
        , 'name': 'João Paulo de Brito e Cautter'
        , 'cpf': '08561920742'
        , 'associate_number': '0934'
    }
)

for o in cart2._get('list'):
    print()
    print()
    print(o._get_dict())
    o._set('waiter', waiter)
    o._set('client', client)
    print()
    print(o._get_dict())

# print(cart2._get_dict())