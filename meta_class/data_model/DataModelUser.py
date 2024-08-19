from meta_class.data_model.DataModel import DataModel

class DataModelItemMenu(DataModel):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                'id': int
                , 'name': str
                , 'short_description': str
                , 'description': str
                , 'value': float
                , 'img_path': str
            }
        )
        self._filter_prop(kwargs)