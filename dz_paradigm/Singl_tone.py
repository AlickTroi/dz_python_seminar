class SingletonType:
    _logger = None

    def __new__(cls):
        if cls._logger is None:
            cls._logger = super(SingletonType, cls).__new__(cls)
        return cls._logger
    
    def get_message(object):
        print(object.message())

