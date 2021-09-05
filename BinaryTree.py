class BinarySearchTree:
    def __init__(self, Data):
        self.Data = Data
        self.left = None
        self.right = None

    def insert(self, Data):
        """

        :param Data: 
        :return:None
        """
        if self.Data == Data:
            return
        elif Data < self.Data:
            if self.left:
                self.left.insert(Data)
            else:
                self.left = BinarySearchTree(Data)

        else:
            if self.right:
                self.right.insert(Data)
            else:
                self.right = BinarySearchTree(Data)

    def min(self):
        """

        :return:min
        """
        min_num = self.Data

        if self.left:
            min_num = self.left.min()

        return min_num

    def max(self):
        """

        :return:max
        """
        max_num = self.Data

        if self.right:
            max_num = self.right.max()

        return max_num

    def in_order_traversal(self) -> list:
        """

        :rtype: list
        :return:sorted list
        """
        elements = []

        # visit left tree

        if self.left:
            elements += self.left.in_order_traversal()

        # visit base tree
        elements.append(self.Data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        """

        :return:list
        """
        # visit base tree
        elements = [self.Data]

        # visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.post_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.post_order_traversal()

        # visit base tree
        elements.append(self.Data)

        return elements

