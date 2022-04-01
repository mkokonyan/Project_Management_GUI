from datetime import datetime


def dumper(obj):
    try:
        return obj.to_json()
    except AttributeError:
        if isinstance(obj, datetime):
            return obj.strftime('%H:%M:%S, %Y-%m-%d')
        return obj.__dict__


def object_hook(entity_class):
    def obj_hook(jsdict):
        obj = entity_class()
        obj.__dict__ = jsdict
        return obj

    return obj_hook
