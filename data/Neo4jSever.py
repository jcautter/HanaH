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