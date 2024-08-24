from data_model.DataModel import DataModel
from data_model.DataModelProduct import DataModelProduct
from data_model.DataModelWaiter import DataModelWaiter
from data_model.DataModelClient import DataModelClient

class DataModelOrder(DataModel):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                '_id': str
                , 'product': DataModelProduct
                , 'quantity': int
                , 'waiter': DataModelWaiter
                , 'client': DataModelClient
            }
        )
        self._filter_prop(kwargs)