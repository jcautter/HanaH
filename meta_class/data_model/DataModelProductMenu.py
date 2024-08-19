from meta_class.data_model.DataModel import DataModel

class DataModelProductMenu(DataModel):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                '_id': int
                , 'name': str
                , 'short_description': str
                , 'description': str
                , 'value': float
                , 'img_path': str
                , 'category': str
            }
        )
        self._filter_prop(kwargs)