class FlatIterator:

    def __init__(self, list_of_lists):
        self.generator = self.flat_generator(list_of_lists)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.generator)

    def flat_generator(self, lst):
        for elem in lst:
            if isinstance(elem, list):
                yield from self.flat_generator(elem)
            else:
                yield elem


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()