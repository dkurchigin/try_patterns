"""EXAMPLE FOR COMPOSITE IN PYTHON"""
from abc import ABC, abstractmethod


class Element(ABC):
    """ABSTRACT CLASS FOR SOME OBJECT AND COMPOSITE"""
    def add(self, some_object):
        """ABSTRACT METHOD FOR ADD ELEMENTS"""
        pass

    @abstractmethod
    def print_type(self, padding):
        """ABSTRACT METHOD FOR PRINTING OBJECT INFO"""
        pass


class SomeObject(Element):
    """CLASS FOR SOME OBJECT"""
    def __init__(self, title):
        self.title = title

    def print_type(self, padding=0):
        print(' ' * padding, self.__class__.__name__, '-', self.title)

    def __repr__(self):
        return self.title


class Composite(Element):
    """CLASS FOR COMPOSITE"""
    def __init__(self, title):
        self._children = []
        self.title = title

    def print_type(self, padding=0):
        print(' ' * padding, self.__class__.__name__, self.title, 'contains:', self._children)

    def add(self, some_object):
        """ADD ELEMENT TO COMPOSITE"""
        self._children.append(some_object)

    def print_content(self):
        """PRINT CONTENT"""
        self.print_recursive(self)

    def print_recursive(self, some_obj, padding=0):
        """PRINT COMPOSITE STRUCTURE RECURSIVE"""
        padding += 2
        if isinstance(some_obj, Composite):
            some_obj.print_type(padding)
            for one_element in some_obj._children:
                self.print_recursive(one_element, padding)
        else:
            some_obj.print_type(padding)

    def __repr__(self):
        return self.title


if __name__ == '__main__':
    simple_obj1 = SomeObject('simple_obj1')
    simple_obj2 = SomeObject('simple_obj2')
    simple_obj3 = SomeObject('simple_obj3')

    main_tree = Composite('main_tree')
    main_tree.add(simple_obj1)

    sub_tree = Composite('sub_tree')
    empty_tree = Composite('empty_tree')

    sub_tree.add(simple_obj2)
    sub_tree.add(simple_obj3)
    main_tree.add(sub_tree)
    main_tree.add(empty_tree)

    print('Print structure:')
    main_tree.print_content()
