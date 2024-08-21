from meta_class.data_model.DataModel import DataModel
from meta_class.data_model.DataModelProduct import DataModelProduct
from meta_class.data_model.DataModelWaiter import DataModelWaiter

class DataModelOrder(DataModel):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                '_id': str
                , 'product': DataModelProduct
                , 'quantity': int
                , 'waiter': DataModelWaiter
            }
        )
        self._filter_prop(kwargs)