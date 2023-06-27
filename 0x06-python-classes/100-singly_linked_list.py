#!/usr/bin/python3
"""class Node that defines a node of a singly linked list"""


class Node:
    """Node of list
    """

    def __init__(self, data, next_node=None):
        """initialization

        Args:
            data (int): data stored in list
            next_node (node): next list node. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter

        Args:
            value (int): data

        Raises:
            TypeError: value must be integer
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """getter

        Returns:
            node: next node on list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter fo next node

        Args:
            value (int): int data

        Raises:
            TypeError: next_node can be None or must be a Node
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list
    """

    def __init__(self):
        """instantiation
        """
        self.__head = None

    def __str__(self):
        """getter

        Returns:
            list: the entire list in stdout line by line
        """
        insert = self.__head
        list = ""

        while insert is not None:
            list += str(insert.data)
            insert = insert.next_node

            if insert is not None:
                list += "\n"

        return list

    def sorted_insert(self, value):
        """inserts a new Node into the correct
        sorted position in the list (increasing order)

        Args:
            value (int): data
        """

        insert = Node(value)
        if self.__head is None:
            self.__head = insert
            return

        tmp = self.__head

        if insert.data < tmp.data:
            insert.next_node = self.__head
            self.__head = insert
            return

        while tmp.next_node:
            if insert.data < tmp.next_node.data:
                break
            tmp = tmp.next_node

        insert.next_node = tmp.next_node
        tmp.next_node = insert

        return
