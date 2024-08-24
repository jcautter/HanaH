from data_model.DataModel import DataModel
from data.DataCatalog import DataCatalog
from data_model.DataModelProduct import DataModelProduct

class DataModelCatalog(DataModel, DataCatalog):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                'list': DataModelProduct
            }
        )
        self._filter_prop(kwargs)
        self._populate_list_of(DataModelProduct)