from meta_class.data_model.DataModel import DataModel

class DataModelClient(DataModel):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                '_id': str
                , 'name': str
                , 'cpf': str
                , 'associate_number': str

            }
        )
        self._filter_prop(kwargs)