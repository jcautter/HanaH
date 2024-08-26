from data.Data import Data

class DataClients(Data):
    def __init__(self):
        super().__init__()

    def _get_data(self):
        self.cp.reset_query()
        self.cp.custom_query_add_node(
            'company'
            , *['Company']
        )
        self.cp.custom_query_add_node(
            'client'
            , *['Client']
        )
        self.cp.custom_query_add_relationship(
            'client'
            , 'company'
            , 'r'
            , 'CLIENT_OF'
        )

        self.cp.custom_query_action_return('client')

        records, summary, keys = self.cp.build_and_execute_custom_query()

        self._populate_data(records)

        return self.data____