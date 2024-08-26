import hashlib
from data.Neo4jCypher import Neo4jCypher

cp = Neo4jCypher(
    **{
        'dns': '2f9f5fc0.databases.neo4j.io'
        , 'user_id': 'neo4j'
        , 'password': 'o8QAOEnN4-FLy1-LUThFYgL3-QE8LX46dZq7Ws0aLtk'
    }
)

cp.delete_all()

###############
### Company ###
###############

cp.custom_query_add_node(
    'company'
    , *['Company']
    , clause='CREATE'
    , **{
        '_id': hashlib.sha256(bytes(
            'Bar do Gomes' + '99999'
            , 'utf-8'
        )).hexdigest()
        , 'name':'Bar do Gomes'
        , 'cnpj': '99999'
    }
)

###############
### Clients ###
###############

cp.custom_query_add_node(
    'n1'
    , *['Client']
    , clause='CREATE'
    , **{
        '_id': hashlib.sha256(bytes(
            'João Paulo de Brito e Cautter' + '08561920742' + '0934'
            , 'utf-8'
        )).hexdigest()
        , 'name':'João Paulo de Brito e Cautter'
        , 'cpf':'08561920742'
        , 'associate_number': '0934'
        , 'email': 'jcautter@gmail.com'
    }
)

cp.custom_query_add_relationship(
    'n1'
    , 'company'
    , 'rc1'
    , 'CLIENT_OF'
    , clause='CREATE'
)

cp.custom_query_add_node(
    'n2'
    , *['Client']
    , clause='CREATE'
    , **{
        '_id': hashlib.sha256(bytes(
            'Barbara de Pinho Fontes' + '09714395755' + '0934'
            , 'utf-8'
        )).hexdigest()
        , 'name':'Barbara de Pinho Fontes'
        , 'cpf':'09714395755'
        , 'associate_number': '0934'
    }
)

cp.custom_query_add_relationship(
    'n2'
    , 'company'
    , 'rc2'
    , 'CLIENT_OF'
    , clause='CREATE'
)

cp.custom_query_add_node(
    'n3'
    , *['Client']
    , clause='CREATE'
    , **{
        '_id': hashlib.sha256(bytes(
            'Daniel Fontes e Cautter' + '00000000000' + '0934'
            , 'utf-8'
        )).hexdigest()
        , 'name':'Daniel Fontes e Cautter'
        , 'associate_number': '0934'
    }
)

cp.custom_query_add_relationship(
    'n3'
    , 'company'
    , 'rc3'
    , 'CLIENT_OF'
    , clause='CREATE'
)

cp.custom_query_add_node(
    'n4'
    , *['Client']
    , clause='CREATE'
    , **{
        '_id': hashlib.sha256(bytes(
            'Convidado' + '00000000000' + '0934'
            , 'utf-8'
        )).hexdigest()
        , 'name':'Convidado'
        , 'associate_number': '0934'
    }
)

cp.custom_query_add_relationship(
    'n4'
    , 'company'
    , 'rc4'
    , 'CLIENT_OF'
    , clause='CREATE'
)

###############
### Product ###
###############

for i in range(100):
    cp.custom_query_add_node(
        'p{i}'.format(i=i)
        , *['Product']
        , clause='CREATE'
        , **{
            'name': 'Suco de Laranja'+str(i)
            , 'short_description': 'Com ou Sem açúcar'+str(i)
            , 'description': 'Suco 100% laranja'+str(i)
            , 'value': float(i)
            , 'img_path': 'https://denorteasulburguer.com.br/wp-content/uploads/2023/03/fritas-grande.png'
            , 'category': 'Bebidas'+str(i//10)
        }
    )

    cp.custom_query_add_relationship(
        'p{i}'.format(i=i)
        , 'company'
        , 'rp{i}'.format(i=i)
        , 'CATALOG_OF'
        , clause='CREATE'
        , **{
            'status': 'active'
        }
    )

# print()

# import json
# print(json.dumps(cp.query, sort_keys=True, indent=4))

# print()

print(cp.build_custom_query())

cp.build_and_execute_custom_query()