from data.Data import Data

class DataUser(Data):
    ____data = {
        'gar1': {
            '_id': '65db6b1539c5d0b7a38f7b99'
            , 'login': 'gar1'
            , 'name': 'Fulano1'
            , 'lang': 'pt-br'
        }
        , 'gar2': {
            '_id': '65db6a9a39c5d0b7a38f7b96'
            , 'login': 'gar2'
            , 'name': 'Fulano2'
            , 'lang': 'pt-br'
        }
    }
    
    def __init__(self):
        super().__init__()

    def _get_data(self, login):
        if login in self.____data:
            return self.____data[login]
        return None