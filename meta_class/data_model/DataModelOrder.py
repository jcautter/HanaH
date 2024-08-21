from meta_class.data_model.DataModel import DataModel

class DataModelOrder(DataModel):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                '_id': str
                , 'product': dict
                , 'quantity': int
                , 'waiter': dict
            }
        )
        self._filter_prop(kwargs)