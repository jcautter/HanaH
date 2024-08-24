import warnings

class DataWarning(UserWarning):
    pass

class DataTypeWarning(UserWarning):
    pass

class DataModel:
    _prefix_name = '___{name}'
    __props = None
    
    def __init__(self, props:dict):
        super().__init__()
        self.__props = props
        self._create_prop()
    
    def _filter_prop(self, kwargs:dict, props:dict=None):
        if not props:
            props = self.__props
            
        for k in props.keys():
            if k in kwargs:
                self._set(k, kwargs[k])
    
    def _create_prop(self, props:dict=None):
        if not props:
            props = self.__props
            
        for k in props:
            if not hasattr(self, self._prefix_name.format(name=k)):
                if k == 'list':
                    setattr(self, self._prefix_name.format(name=k), [])
                else:
                    setattr(self, self._prefix_name.format(name=k), None)
    
    def _get(self, key:str):
        if hasattr(self, self._prefix_name.format(name=key)):
            return getattr(self, self._prefix_name.format(name=key))
        else:
            warnings.warn(
                "Property does not exist: {prop}".format(prop=key)
                , DataWarning
            )
        
    def _set(self, key:str, val):
        if hasattr(self, self._prefix_name.format(name=key)):
            if val is not None:
                if key == 'list':
                    if issubclass(self.__props[key], DataModel) and type(val) is list:
                        print('oi')
                        print(val)
                        setattr(
                            self
                            , self._prefix_name.format(name=key)
                            , [self.__props[key](**o) if type(val) is dict else o for o in val]
                        )
                    else:
                        setattr(self, self._prefix_name.format(name=key), val)
                elif type(val) == dict and issubclass(self.__props[key], DataModel):
                    setattr(self, self._prefix_name.format(name=key), self.__props[key](**val))
                elif type(val) == self.__props[key]:
                    setattr(self, self._prefix_name.format(name=key), val)
                else:
                    warnings.warn(
                        "Property has a different type: {prop} must be {type_prop}".format(
                            prop=key
                            , type_prop=str(
                                str(self.__props[key]).replace("<class '", '').replace("'>", '')
                            )
                        )
                        , DataTypeWarning
                    )
        else:
            warnings.warn(
                "Property does not exist: {prop}".format(prop=key)
                , DataWarning
            )

    def _append(self, key, val):
        if hasattr(self, self._prefix_name.format(name=key)):
            if type(val) == self.__props[key]:
                lisf_of_object = self._get(key)
                lisf_of_object.append(val)
                self._set(key, lisf_of_object)
            elif type(val) is dict and issubclass(self.__props[key], DataModel):
                self._get(key).append(self.__props[key](**val))
            else:
                warnings.warn(
                    "Property has a different type: {prop} must be {type_prop}".format(
                        prop=key
                        , type_prop=str(
                            str(self.__props[key]).replace("<class '", '').replace("'>", '')
                        )
                    )
                    , DataTypeWarning
                )
        else:
            warnings.warn(
                "Property does not exist: {prop}".format(prop=key)
                , DataWarning
            )

    def _get_dict(self):
        doc = {}
        for k in self.__props.keys():
            if k == 'list':
                if issubclass(self.__props[k], DataModel):
                    doc[k] = [o._get_dict() for o in self._get(k)]
                else:
                    doc[k] = self._get(k)
            elif issubclass(self.__props[k], DataModel):
                o = self._get(k)
                if o is not None:
                    doc[k] = self._get(k)._get_dict()
                else:
                    doc[k] = None
            else:
                doc[k] = self._get(k)
        return doc
    
    def _populate_list_of(self, data_model):
        for product in self._get_data():
            self._append('list', data_model(**product))