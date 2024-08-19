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
            if type(val) == self.__props[key]:
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