import pandas as pd

class QueryBuilderCypher:
    
    def __init__(self):
        pass
    
    # Metodos Privados

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
    
    # Metodos Públicos

    def node(self, repre:str, *label, **properties):
        return "({node})".format(
            node=self.query_build_node(repre, *label, **properties)
        )
    
    def relationship(self, repre:str, label:str, **properties):
        return "[{rel}]".format(
            rel=self.query_build_relationship(repre, label, **properties)
        )
    
    # Não validado
    
    def delete_relationship(self, repre:str, label:str, **properties):
        return "MATCH ()-[{relationship}]->() DELETE {repre}".format(
            relationship=self.query_build_relationship(repre, label, **properties)
            , repre=repre
        )
    
    def delete_node(self, repre:str, *labels, **properties):
        return "MATCH ()-[{relationship}]->() DELETE {repre}".format(
            relationship=self.query_build_relationship(repre, *labels, **properties)
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