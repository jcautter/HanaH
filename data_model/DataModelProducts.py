from data_model.DataModel import DataModel
from data.DataProducts import DataProducts
from data_model.DataModelProduct import DataModelProduct

class DataModelProducts(DataModel, DataProducts):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                'list': DataModelProduct
            }
        )
        self._filter_prop(kwargs)
        self._populate_list_of(DataModelProduct)