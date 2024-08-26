# from data.Neo4jCypher import Neo4jCypher

# cp = Neo4jCypher(
#     **{
#         'dns': '2f9f5fc0.databases.neo4j.io'
#         , 'user_id': 'neo4j'
#         , 'password': 'o8QAOEnN4-FLy1-LUThFYgL3-QE8LX46dZq7Ws0aLtk'
#     }
# )

# cp.custom_query_add_node(
#     'n'
#     , reset_query=True
#     , *['Client']
# )

# cp.custom_query_action_return()

# print()

# import json
# print(json.dumps(cp.query, sort_keys=True, indent=4))

# print()

# print(cp.build_custom_query())

# records, summary, keys = cp.build_and_execute_custom_query()

# print()

# print(keys)
# print(summary)
# print(records)

# print('------------------------------')

# list_reg = []
# for o in records:
#     print(list_reg.append([v for k,v in o.data().items()][0]))

# print(json.dumps(list_reg, sort_keys=True, indent=4))

from data_model.DataModelClients import DataModelClients

a = DataModelClients()
for d in a._get('list'):
    print(d._get_dict())