from data.Neo4jCypher import Neo4jCypher

class Data:
    data____:list = []
    cp:Neo4jCypher
    def __init__(self):
        self.cp = Neo4jCypher(
            **{
                'dns': '2f9f5fc0.databases.neo4j.io'
                , 'user_id': 'neo4j'
                , 'password': 'o8QAOEnN4-FLy1-LUThFYgL3-QE8LX46dZq7Ws0aLtk'
            }
        )

    def _populate_data(self, records:list):
        for o in records:
            self.data____.append([v for k,v in o.data().items()][0])