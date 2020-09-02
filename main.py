# DO NOT modify this code
class Node:
    def __init__(self, alpha_init, num_init):
        self.__alpha = alpha_init  # should be 'string'
        self.__num = num_init  # should be 'int'
        self.__next = None

    def get_alpha(self):
        return self.__alpha

    def get_num(self):
        return self.__num

    def get_next(self):
        return self.__next

    def set_data(self, new_alpha, new_num):
        self.__alpha = new_alpha
        self.__num = new_num

    def set_next(self, new_next):
        self.__next = new_next


class LinkedList:
    def __init__(self):
        self.__head = None

    def __len__(self):
        current = self.__head
        cnt = 0
        while current != None:
            cnt += 1
            current = current.get_next()
        return cnt

    def __getitem__(self, idx):
        current = self.__head
        for _ in range(idx):
            if current == None:
                raise IndexError
            current = current.get_next()
        return current

    def __str__(self):
        message = ''
        current = self.__head
        while current != None:
            if current.get_next() == None:
                message = message + current.get_alpha() + current.get_num()
            else:
                message = message + current.get_alpha() + current.get_num() + ' '
            current = current.get_next()
        message = '[' + message + ']'
        return message

    def push_back(self, item):
        current = self.__head
        if current == None:
            temp = Node(item[0], item[1])
            self.__head = temp
        else:
            while current.get_next() != None:
                current = current.get_next()

            temp = Node(item[0], item[1])
            current.set_next(temp)

    def sort_select(self):
        for fill_slot in range(self.__len__() - 1, 0, -1):
            pos_min = 0
            for loc in range(1, fill_slot + 1):
                if self[loc].get_num() <= self[pos_min].get_num():
                    pos_min = loc
            current = self.__head
            previous = None
            after = None
            pos = self.__head
            pos_previous = None

            for i in range(fill_slot):
                previous = current
                current = current.get_next()
                after = current.get_next()

            for j in range(pos_min):
                pos_previous = pos
                pos = pos.get_next()

            if current == pos:
                current = current

            else:
                if pos == self.__head:
                    previous.set_next(pos)
                    current.set_next(pos.get_next())
                    pos.set_next(after)
                    self.__head = current
                else:
                    pos_previous.set_next(current)
                    previous.set_next(pos)
                    current.set_next(pos.get_next())
                    pos.set_next(after)

    def sort_quick(self):
        self.quick_sort_helper(0, self.__len__() - 1)

    def quick_sort_helper(self, first, last):
        if first < last:
            split_point = self.partition(first, last)

            self.quick_sort_helper(first, split_point - 1)
            self.quick_sort_helper(split_point + 1, last)

    def partition(self, first, last):
        pivot_value = self[first]
        left_mark = first + 1
        right_mark = last
        done = False

        while not done:
            while left_mark <= right_mark and self[left_mark].get_alpha() <= pivot_value.get_alpha():
                if self[left_mark].get_alpha() == pivot_value.get_alpha():
                    if self[left_mark].get_num() <= pivot_value.get_num():
                        left_mark = left_mark + 1
                    else:
                        break
                else:
                    left_mark = left_mark + 1

            while self[right_mark].get_alpha() >= pivot_value.get_alpha() and right_mark >= left_mark:
                if self[right_mark].get_alpha() == pivot_value.get_alpha():
                    if self[right_mark].get_num() >= pivot_value.get_num():
                        right_mark = right_mark - 1
                    else:
                        break
                else:
                    right_mark = right_mark - 1

            if right_mark < left_mark:
                done = True
            else:
                left = self.__head
                right = self.__head
                left_pre = None
                right_pre = None
                right_after = None
                for i in range(left_mark):
                    left_pre = left
                    left = left.get_next()
                for j in range(right_mark):
                    right_pre = right
                    right = right.get_next()
                    right_after = right.get_next()

                left_pre.set_next(right)
                right_pre.set_next(left)
                right.set_next(left.get_next())
                left.set_next(right_after)

        current = self.__head
        previous = None
        right = self.__head
        right_pre = None
        right_after = None
        for k in range(right_mark):
            right_pre = right
            right = right.get_next()
            right_after = right.get_next()
        for h in range(first):
            previous = current
            current = current.get_next()

        if current == right:
            current = current

        else:
            if self.__head == current:
                right_pre.set_next(current)
                right.set_next(current.get_next())
                current.set_next(right_after)
                self.__head = right
            else:
                previous.set_next(right)
                right_pre.set_next(current)
                right.set_next(current.get_next())
                current.set_next(right_after)

        return right_mark
# This code is for validation; DO NOT change this code
linked_list = LinkedList()
print('-' * 40)

codes = ['C8', 'A3', 'D7', 'B8', 'A6', 'B5', 'D3', 'C1']
for code in codes:
    linked_list.push_back(code)
print(linked_list)
print('-' * 40)
linked_list.sort_select()
print(linked_list)
print('-' * 40)
linked_list.sort_quick()
print(linked_list)
print('-' * 40)