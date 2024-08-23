from meta_class.data_model.DataModel import DataModel
from meta_class.data.DataClients import DataClients
from meta_class.data_model.DataModelClient import DataModelClient

class DataModelClients(DataModel, DataClients):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                'list': DataModelClient
            }
        )
        self._filter_prop(kwargs)
        self._populate_list_of(DataModelClient)