class FlatIterator:
    def __init__(self, list_of_lists):
        # flat_list = []
        # for sublist in list_of_lists:
        #     for elem in sublist:
        #         flat_list.append(elem)
        self.flat_list = [elem for sublist in list_of_lists for elem in sublist]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.flat_list):
            item = self.flat_list[self.index]
            self.index += 1
            print(item)
            return item
        else:
            raise StopIteration()


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()