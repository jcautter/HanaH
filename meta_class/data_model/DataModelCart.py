from meta_class.data_model.DataModel import DataModel

from meta_class.data_model.DataModelOrder import DataModelOrder
from meta_class.data_model.DataModelClient import DataModelClient
from meta_class.data_model.DataModelWaiter import DataModelWaiter

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