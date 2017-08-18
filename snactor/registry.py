_REGISTERED_ACTORS = {}
_REGISTERED_EXECUTORS = {}


def get_executor(executor):
    return _REGISTERED_EXECUTORS.get(executor)


def get_actor(actor):
    return _REGISTERED_ACTORS.get(actor)


def registered_executor(name):
    def func(cls):
        if name in _REGISTERED_EXECUTORS:
            raise ValueError("Executor '{}' has been already registered previously".format(name))
        cls.type = name
        _REGISTERED_EXECUTORS[name] = cls
        return cls
    return func


def registered_actor(name):
    def func(cls):
        if name in _REGISTERED_ACTORS:
            raise ValueError("Actor '{}' has been already registered previously".format(name))
        cls.type = name
        _REGISTERED_ACTORS[name] = cls
        return cls
    return func
