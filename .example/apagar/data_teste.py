# from meta_class.data_model.DataModelItemMenu import DataModelItemMenu

# a = DataModelItemMenu(name='Batata Frita', value=49.50)

# k = 'name'
# print(k, a._get(k))

# k = 'value'
# print(k, a._get(k))

# k = 'img_path'
# print(k, a._get(k))

# k = 'quadro'
# print(k, a._get(k))


# from meta_class.data.DataUser import DataUser

# a = DataUser()
# print(a._get_data('gar2'))


# from meta_class.data.DataCatalog import DataCatalog
# from meta_class.data_model.DataModelProduct import DataModelProduct

# a = DataCatalog()
# for i in a._get_data():
#     x = DataModelProduct(**i)
#     break

# for i in x._DataModel__props.keys():
#     print(x._get(i))


from data_model.DataModelCatalog import DataModelCatalog

a = DataModelCatalog()
for i in a._get('list'):
    for j in i._DataModel__props.keys():
        print(i._get(j))
    print()