from data_model.DataModel import DataModel

class DataModelProduct(DataModel):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                '_id': str
                , 'name': str
                , 'short_description': str
                , 'description': str
                , 'price': float
                , 'img_path': str
                , 'category': str
            }
        )
        self._filter_prop(kwargs)