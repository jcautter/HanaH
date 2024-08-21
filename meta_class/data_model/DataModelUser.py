from meta_class.data_model.DataModel import DataModel
from meta_class.data.DataUser import DataUser

class DataModelUser(DataModel, DataUser):
    def __init__(self, **kwargs):
        super().__init__(
            props={
                '_id': str
                , 'login': str
                , 'name': str
                , 'lang': str
            }
        )
        if 'login' in kwargs:
            self._filter_prop(self._get_data(kwargs['login']))
    def _push_cokies(self, page):
        page.client_storage.set("user", self._get_dict())