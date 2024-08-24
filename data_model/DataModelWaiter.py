from data_model.DataModel import DataModel
from data.DataWaiter import DataWaiter

class DataModelWaiter(DataModel, DataWaiter):
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