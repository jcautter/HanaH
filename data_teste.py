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

from meta_class.data_model.DataModelMenu import DataModelMenu

a = DataModelMenu()
for i in a._get('data'):
    print(i)