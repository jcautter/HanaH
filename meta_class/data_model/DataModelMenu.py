from meta_class.data_model.DataModel import DataModel
from meta_class.data.DataMenu import DataMenu

class DataModelMenu(DataModel, DataMenu):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                'data': list
            }
        )
        self._filter_prop(kwargs)
        self._set('data', self._get_data())