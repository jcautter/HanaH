from data.Data import Data

class DataClients(Data):
    ____data = [
        {
            '_id': '65db6b1539c5d0b7a38f7b99'
            , 'name': 'João Paulo de Brito e Cautter'
            , 'cpf': '08561920742'
            , 'associate_number': '0934' 
        }
        , {
            '_id': '65db6b1539c5d0b7a38f7b90'
            , 'name': 'Barbara de Pinho Fontes'
            , 'cpf': '09714395755'
            , 'associate_number': '0934'
        }
        , {
            '_id': '65db6b1539c5d0b7a38f7b90'
            , 'name': 'Daniel Fontes e Cautter'
            , 'cpf': '00000000000'
            , 'associate_number': '0934'
        }
        , {
            '_id': '65db6b1539c5d0b7a38f7b90'
            , 'name': 'Convidado'
            , 'cpf': '00000000000'
            , 'associate_number': '0934'
        }
    ]
    
    def __init__(self):
        super().__init__()

    def _get_data(self):
        return self.____data