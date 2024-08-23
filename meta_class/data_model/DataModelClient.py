from meta_class.data_model.DataModel import DataModel
from meta_class.data.DataWaiter import DataWaiter

class DataModelCliente(DataModel, DataWaiter):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                '_id': str
                , 'name': str
                , 'company': str
            }
        )
        if 'login' in kwargs:
            self._filter_prop(self._get_data(kwargs['login']))