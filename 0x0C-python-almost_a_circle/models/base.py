#!/usr/bin/python3
"""Base module"""

import json


class Base:
    """Base class

        Attributes:
            __nb_objects(int): number of objects

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ __init__intializes the class.

        Args:
            id(int): public instance attribute.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Creates JSON string representation of the dictionaries"""

        new_list = "["
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        c = 1
        for d in list_dictionaries:
            new_list = new_list + json.dumps(d)
            if c < len(list_dictionaries):
                new_list = new_list + ", "
                c += 1
        new_list = new_list + "]"
        return new_list

    @classmethod
    def save_to_file(cls, list_objs):
        """The method writes the JSON string representation of
        list_objs to a file.

        Args:
            list_objs(base obj): A list of instances inheriting Base.

        """
        if list_objs is not None and len(list_objs) > 0:
            dictionary = []
            name_prefix = type(list_objs[0]).__name__
            filename = str(name_prefix) + '.json'
            for i in list_objs:
                if isinstance(i, Base):
                    dictionary.append(i.to_dictionary())
            json_string = cls.to_json_string(dictionary)
            with open(filename, "w") as f:
                f.write(json_string)

    def from_json_string(json_string):
        """Function returns a list from the JSON string"""

        new_list = []
        if json_string is None or len(json_string) == 0:
            return new_list
        return list(eval(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 3)
        elif cls.__name__ == "Square":
            dummy = cls(4)
        kwargs = {}
        if dictionary is not None and len(dictionary) > 0:
            for k in dictionary:
                if k == 'id':
                    kwargs[k] = dictionary[k]
                if k == 'width':
                    kwargs[k] = dictionary[k]
                if k == 'height':
                    kwargs[k] = dictionary[k]
                if k == 'x':
                    kwargs[k] = dictionary[k]
                if k == 'y':
                    kwargs[k] = dictionary[k]
                if k == 'size':
                    kwargs[k] = dictionary[k]
            dummy.update(**kwargs)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Function returns a list of instances."""

        dictionary = {}
        new_list = []
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
                json_list = cls.from_json_string(json_string)
                if json_list is not None and len(json_list) > 0:
                    for i in json_list:
                        dummy = cls.create(**i)
                        new_list.append(dummy)
                    return new_list
        except:
            return new_list
