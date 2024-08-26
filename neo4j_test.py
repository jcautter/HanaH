from neo4j import GraphDatabase

class Neo4jSever:
    
    uri = "{protocol}://{dns}"
    protocol = None
    dns = None
    user_id = None
    password = None
    
    conn = None
    
    def __init__(self, dns, user_id, password, protocol='neo4j+ssc', database_name=None):
        self.dns = dns
        self.user_id = user_id
        self.password = password
        self.protocol = protocol
        self.database_name = database_name
        
    def connection(self, dns=None, protocol=None, user_id=None, password=None):
        if not dns:
            dns = self.dns
        if not protocol:
            protocol = self.protocol
        if not user_id:
            user_id = self.user_id
        if not password:
            password = self.password
            
        self.conn = GraphDatabase.driver(
            self.uri.format(protocol = protocol, dns = dns)
            , auth=(user_id, password)
        )
        
    def check_connection(self, dns=None, protocol=None, user_id=None, password=None):
        if not self.conn:
            self.connection(dns, protocol, user_id, password)
            
    def execute_query(self, query, dns=None, protocol=None, user_id=None, password=None):          
        self.check_connection(dns, protocol, user_id, password)
        records, summary, keys = self.conn.execute_query(query)
        self.close()
        return records, summary, keys
    
    def verify_connectivity(self, dns=None, protocol=None, user_id=None, password=None):
        self.check_connection(dns, protocol, user_id, password)
        self.conn.verify_connectivity()
        self.close()
    
    def close(self):
        self.conn.close()
        self.conn = None


import pandas as pd

class QueryBuilderCypher:
    
    def __init__(self):
        pass
        
    def query_build_join_labels(self, *labels):
        return ''.join([':{r}'.format(r=i) for i in labels])
    
    def query_build_join_properties(self, **properties):
        props = ', '.join(
            [
                "{k}: '{v}'".format(k=k,v=v) 
                    if type(v) is str 
                    else "{k}: {v}".format(k=k,v="date('{dt}')".format(dt=v.strftime("%Y-%m-%d")))
                        if type(v) is pd.Timestamp
                        else "{k}: {v}".format(k=k,v=v)
                for k, v in properties.items()
            ]
        )
        return '{'+props+'}' if len(props) > 0 else ''
    
    def query_build_node(self, repre:str, *labels, **properties):
        return '{repre}{lbs} {props}'.format(
                repre=repre
                , lbs=self.query_build_join_labels(*labels)
                , props=self.query_build_join_properties(**properties)
            ).strip()
    
    def query_build_relationship(self, repre:str, label:str, **properties):
        return '{data}'.format(
            data = '{repre}:{lb} {props}'.format(
                repre=repre
                , lb= label
                , props=self.query_build_join_properties(**properties)
            ).strip()
        )
    
    def query_build_relationship_with(self, node1:str, node2:str, repre:str, label:str, **properties):
        return '({node1})-[{relationship}]->({node2})'.format(
            node1=node1
            , relationship=self.query_build_relationship(repre, label, **properties)
            , node2=node2
        )
    
    def get_node_repre(self, node):
        return node.split()[0].split(':')[0].replace('(', '')
    
    def delete_relationship(self, repre:str, label:str, **properties):
        return "MATCH ()-[{relationship}]->() DELETE {repre}".format(
            relationship=self.query_build_relationship(repre, label, **properties)
            , repre=repre
        )
    
    def delete_node(self, repre:str, *label, **properties):
        return "MATCH ()-[{relationship}]->() DELETE {repre}".format(
            relationship=self.query_build_relationship(repre, *label, **properties)
            , repre=repre
        )
    
    def delete_all(self):
        return self.delete_relationship('r') + ''
        self.delete_node('n')
        
    def create_node(self, repre:str, *label, **properties):
        return "MERGE ({node})".format(
            node=self.query_build_node(repre, *label, **properties)
        )
    
    def create_relationship(self, node1, node2, repre:str, label:str, **properties):
        return "MERGE {relationship}".format(
            relationship=self.query_build_relationship_with(
                node1, node2, repre, label, **properties
            )
        )
    

class Neo4jCypher:
    
    neo4j_server = None
    neo4j_query_builder = None
    
    def __init__(self, dns, user_id, password, protocol='neo4j+ssc', database_name=None):
        self.neo4j_server = Neo4jSever(dns, user_id, password, protocol)
        self.neo4j_query_builder = QueryBuilderCypher()
        
    def delete_relationship(self, repre:str, label='', **properties):
        return self.neo4j_server.execute_query(
            self.neo4j_query_builder.delete_relationship(
                repre, label, **properties
            )
        )
        
    def delete_node(self, repre:str, *label, **properties):
        return self.neo4j_server.execute_query(
            self.neo4j_query_builder.delete_node(
                repre, *label, **properties
            )
        )
    
    def delete_all(self):
        return self.neo4j_server.execute_query(
            self.neo4j_query_builder.delete_all()
        )
    
    def create_node(self, repre:str, *label, **properties):
        return self.neo4j_server.execute_query(
            self.neo4j_query_builder.create_node(
                repre, *label, **properties
            )
        )
    
    def create_relationship(self, node1, node2, repre:str, label:str, **properties):
        return self.neo4j_server.execute_query(
            self.neo4j_query_builder.create_relationship(
                node1, node2, repre, label, **properties
            )
        )
    

a = Neo4jCypher(
    **{
        'dns': '2f9f5fc0.databases.neo4j.io'
        , 'user_id': 'neo4j'
        , 'password': 'o8QAOEnN4-FLy1-LUThFYgL3-QE8LX46dZq7Ws0aLtk'
    }
)