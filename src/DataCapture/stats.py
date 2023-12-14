from typing import List


class Stats(object):
    def __init__(self, items: List[int] = []) -> None:
        self.data = list(items)
        self.data.sort()
        self.__min = min(self.data)
        self.__max = max(self.data)

    def less(self, value: int) -> int:
        try:
            if type(value) == int:
                if value not in self.data:
                    tmp_lst = [x for x in self.data if x > value]
                    p = None if len(tmp_lst) == 0 else tmp_lst[0]
                else:
                    p = self.data.index(value)
                return len(self.data[0:p])
            else:
                raise ValueError
        except ValueError:
            print("Invalid Value: must to be a integer")
        return -1

    def greater(self, value: int) -> int:
        try:
            if type(value) == int:
                reverse_data = self.data[::-1]
                if value not in self.data:
                    tmp_lst = [x for x in reverse_data if x < value]
                    p = None if len(tmp_lst) == 0 else tmp_lst[0]
                else:
                    p = reverse_data.index(value)
                return len(reverse_data[0:p])
            else:
                raise ValueError
        except ValueError:
            print("Invalid Value: must to be a integer")
        return -1

    def between(self, num1: int, num2: int) -> int:
        try:
            if type(num1) == int and type(num2) == int:
                if num2 < num1:
                    num1, num2 = num2, num1
                tmp_lst = [x for x in self.data if num1 <= x <= num2]
                return len(tmp_lst)
            else:
                raise ValueError
        except ValueError:
            print("Invalid Value: must to be a integer")
        return -1

    def __repr__(self) -> str:
        return str(self.data)
