from meta_class.data_model.DataModel import DataModel
from meta_class.data.DataCatalog import DataCatalog
from meta_class.data_model.DataModelProduct import DataModelProduct

class DataModelCatalog(DataModel, DataCatalog):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                'list': DataModelProduct
            }
        )
        self._filter_prop(kwargs)
        self._populate_list_of(DataModelProduct)