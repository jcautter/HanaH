import warnings

class Neo4jCypherQuerySearchClauseUnknowned(UserWarning):
    pass

class Neo4jCypherQueryNodeRepresentationExistent(UserWarning):
    pass

class Neo4jCypherQueryRelationshipRepresentationExistent(UserWarning):
    pass

class Neo4jCypherQueryNodeRepresentationNotExistent(UserWarning):
    pass

from data.Neo4jSever import Neo4jSever
from data.QueryBuilderCypher import QueryBuilderCypher

class Neo4jCypher:
    
    neo4j_server:Neo4jSever = None
    neo4j_query_builder:QueryBuilderCypher = None
    query:dict = None
    
    def __init__(self, dns, user_id, password, protocol='neo4j+ssc', database_name=None):
        self.neo4j_server = Neo4jSever(dns, user_id, password, protocol)
        self.neo4j_query_builder = QueryBuilderCypher()
        self.reset_query()

    def create_node(self, repre:str, *label, **properties):
        return self.neo4j_server.execute_query(
            "MERGE {node}".format(
                node = self.neo4j_query_builder.node(
                    repre, *label, **properties
                )
            )
        )
    
    def select_node(self, repre:str, *label, return_limit:int=25, **properties):
        return self.neo4j_server.execute_query(
            "MATCH {node} RETURN {repre} LIMIT {return_limit}".format(
                node = self.neo4j_query_builder.node(
                        repre, *label, **properties
                    )
                , repre = repre
                , return_limit = return_limit
            )
        )
    
    def reset_query(self):
        self.query = {
            'nodes': {}
            , 'relationship': {}
            , 'action': None
        }

    def custom_query_add_node(self, repre:str, *label, clause:str='MATCH', reset_query:bool=False, **properties):
        if reset_query:
            self.reset_query()

        if clause.upper() in ['CREATE', 'MATCH', 'MERGE']:
            if repre not in self.query['nodes']:
                self.query['nodes'][repre] = "{clause} {node}".format(
                    clause = clause.upper()
                    , node = self.neo4j_query_builder.node(
                        repre, *label, **properties
                    )
                )
            else:
                warnings.warn(
                    "Neo4j Node representation '{repre}' alredy exists".format(repre=repre)
                    , Neo4jCypherQueryNodeRepresentationExistent
                )
        else:
            warnings.warn(
                "Neo4j Query Search Unknowned: '{clause}'".format(clause=clause)
                , Neo4jCypherQuerySearchClauseUnknowned
            )

    def custom_query_add_relationship(self, node1:str, node2:str, repre:str, label:str, clause:str='MATCH', **properties):
        if clause.upper() in ['CREATE', 'MATCH', 'MERGE']:
            if repre not in self.query['relationship']:
                if node1 in self.query['nodes'] and node2 in self.query['nodes']:
                    self.query['relationship'][repre] = {
                        'node1': node1
                        , 'node2': node2
                        , 'relationship': "{clause} ({node1})-{relationship}->({node2})".format(
                            clause=clause.upper()
                            , node1=node1
                            , relationship=self.neo4j_query_builder.relationship(repre, label, **properties)
                            , node2=node2
                        )
                    }
                else:
                    warnings.warn(
                        "Neo4j Node representation '{node1}' or '{node2}' not exists".format(node1=node1, node2=node2)
                        , Neo4jCypherQueryNodeRepresentationNotExistent
                    )
            else:
                warnings.warn(
                    "Neo4j Relationship representation '{repre}' alredy exists".format(repre=repre)
                    , Neo4jCypherQueryRelationshipRepresentationExistent
                )
        else:
            warnings.warn(
                "Neo4j Query Search Unknowned: '{clause}'".format(clause=clause)
                , Neo4jCypherQuerySearchClauseUnknowned
            )

    def custom_query_action_get_repres(self, *repres):
        query_repres = list(self.query['nodes'].keys()) + list(self.query['relationship'].keys())
        if repres:
            repres = [repre for repre in repres if repre in query_repres]
        else:
            repres = query_repres
        return  repres
    
    def custom_query_action_return(self, *repres):
        repres = self.custom_query_action_get_repres(*repres)
        self.query['action'] = {
            'type': "RETURN"
            , 'query': "RETURN " + ','.join(repres)
        }

    def custom_query_action_delete(self, *repres):
        repres = self.custom_query_action_get_repres(*repres)
        self.query['action'] = {
            'type': "DELETE"
            , 'query': "DELETE " + ','.join(repres)
        }

    def custom_query_action_detach_delete(self, *repres):
        repres = self.custom_query_action_get_repres(*repres)
        self.query['action'] = {
            'type': "DETACH DELETE"
            , 'query': "DETACH DELETE " + ','.join(repres)
        }

    # ['RETURN', 'DELETE', 'DETACH DELETE', 'SET']
    def custom_query_action_set(self, sets:dict):
        repres = self.custom_query_action_get_repres()

        set_list = []
        for repre, props in sets.items():
            if repre in repres:
                for name, val in props.items():
                    set_list.append(
                        "SET {repre}.{name} = {val}".format(
                            repre=repre
                            , name=name
                            , val=val if type(val) is not str else "'{val}'".format(val=val)
                        )
                    )

        self.query['action'] = {
            'type': "SET"
            , 'query': "\n".join(set_list)
        }

    def build_custom_query(self):
        query = []
        repres = []
        for repre, node in self.query['nodes'].items():
            repres.append(repre)
            query.append(node)
        for repre, rel_dict in self.query['relationship'].items():
            repres.append(repre)
            query.append(rel_dict['relationship'])
        if self.query['action']:
            query.append(self.query['action']['query'])
        return "\n".join(query)

    def build_and_execute_custom_query(self):
        query = self.build_custom_query()
        self.reset_query()
        return self.neo4j_server.execute_query(
            query
        )

    def delete_all(self):
        self.custom_query_add_node(
            'n'
            , reset_query=True
        )
        self.custom_query_action_detach_delete()
        return self.build_and_execute_custom_query()