from data_model.DataModel import DataModel

from data_model.DataModelOrder import DataModelOrder
from data_model.DataModelClient import DataModelClient
from data_model.DataModelWaiter import DataModelWaiter

class DataModelCart(DataModel):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                'list': DataModelOrder
                , 'client': DataModelClient
                , 'waiter': DataModelWaiter
                , 'date': str 
            }
        )
        self._filter_prop(kwargs)