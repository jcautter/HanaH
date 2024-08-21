from meta_class.data.Data import Data

class DataWaiter(Data):
    ____data = {
        'gar1': {
            '_id': '65db6b1539c5d0b7a38f7b99'
            , 'name': 'gar1'
            , 'company': 'Bar do Gomes'
        }
    }
    
    def __init__(self):
        super().__init__()

    def _get_data(self, login):
        if login in self.____data:
            return self.____data[login]
        return None