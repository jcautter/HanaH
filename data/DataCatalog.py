from data.Data import Data

class DataCatalog(Data):
    ____data = []
    
    def __init__(self):
        super().__init__()
        for i in range(100):
            self.____data.append(
                {
                    '_id': str(i)
                    , 'name': 'Suco de Laranja'+str(i)
                    , 'short_description': 'Com ou Sem açúcar'+str(i)
                    , 'description': 'Suco 100% laranja'+str(i)
                    , 'value': float(i)
                    , 'img_path': 'img/Bebida.jpg'
                    , 'category': 'Bebidas'+str(i//10)
                }
            )
        self.____data

    def _get_data(self):
        return self.____data