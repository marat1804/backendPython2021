"""
Describing Custom metaclass which add prefix "custom_" for methods and attrs
"""


class CustomMeta(type):
    """
    Metaclass which add prefix "custom_" for methods and attrs
    """
    def __new__(cls, class_name, parents, attributes):
        custom_attributes = {}
        for key, value in attributes.items():
            if not(key.startswith('__') and key.endswith('__')):
                custom_attributes['custom_' + key] = value
            else:
                custom_attributes[key] = value
        return super().__new__(cls, class_name, parents, custom_attributes)

    def __call__(self, *args, **kwargs):
        ready_class = super().__call__(*args, **kwargs)
        custom_attributes = {}
        for key, value in ready_class.__dict__.items():
            if not (key.startswith('__') and key.endswith('__')):
                custom_attributes['custom_' + key] = value
            else:
                custom_attributes[key] = value
        ready_class.__dict__ = custom_attributes
        return ready_class
