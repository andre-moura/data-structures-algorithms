import unittest
from linked_list import LinkedList

class TestClass(unittest.TestCase):
    def test_append_get(self):
        linked_list = LinkedList(2)
        linked_list.append(1)
        self.assertEqual(linked_list.get(0).value, 2, 'Should be equal 2')
        self.assertEqual(linked_list.get(1).value, 1, 'Should be equal 1')


    def test_pop_get(self):
        linked_list = LinkedList(2)
        linked_list.append(1)
        linked_list.append(56)
        linked_list.append(99)
        linked_list.pop()
        self.assertEqual(linked_list.get(0).value, 2, 'Should be equal 2')
        self.assertEqual(linked_list.get(1).value, 1, 'Should be equal 1')
        self.assertEqual(linked_list.get(2).value, 56, 'Should be equal 56')
        self.assertEqual(linked_list.get(3), None, 'Should be equal None')


    def test_prepend_get(self):
        linked_list = LinkedList(2)
        linked_list.append(1)
        linked_list.append(19)
        linked_list.prepend(48)
        self.assertEqual(linked_list.get(0).value, 48, 'Should be equal 48')
        self.assertEqual(linked_list.get(1).value, 2, 'Should be equal 2')
        self.assertEqual(linked_list.get(2).value, 1, 'Should be equal 1')
        self.assertEqual(linked_list.get(3).value, 19, 'Should be equal 19')


    def test_pop_first_get(self):
        linked_list = LinkedList(2)
        linked_list.append(1)
        linked_list.append(19)
        linked_list.append(48)
        linked_list.pop_first()
        self.assertEqual(linked_list.get(0).value, 1, 'Should be equal 1')
        self.assertEqual(linked_list.get(1).value, 19, 'Should be equal 19')
        self.assertEqual(linked_list.get(2).value, 48, 'Should be equal 48')


    def test_set_value_get(self):
        linked_list = LinkedList(2)
        linked_list.append(1)
        linked_list.append(19)
        linked_list.set_value(0, 32)
        linked_list.append(48)
        self.assertEqual(linked_list.get(0).value, 32, 'Should be equal 32')
        self.assertEqual(linked_list.get(1).value, 1, 'Should be equal 1')
        self.assertEqual(linked_list.get(2).value, 19, 'Should be equal 19')
        self.assertEqual(linked_list.get(3).value, 48, 'Should be equal 48')


    def test_insert_get(self):
        linked_list = LinkedList(2)
        linked_list.append(1)
        linked_list.insert(1, 19)
        linked_list.set_value(0, 32)
        linked_list.append(48)
        self.assertEqual(linked_list.get(0).value, 32, 'Should be equal 32')
        self.assertEqual(linked_list.get(1).value, 19, 'Should be equal 19')
        self.assertEqual(linked_list.get(2).value, 1, 'Should be equal 1')
        self.assertEqual(linked_list.get(3).value, 48, 'Should be equal 48')


    def test_remove_get(self):
        linked_list = LinkedList(2)
        linked_list.append(1)
        linked_list.append(19)
        linked_list.remove(0)
        linked_list.append(48)
        self.assertEqual(linked_list.get(0).value, 1, 'Should be equal 1')
        self.assertEqual(linked_list.get(1).value, 19, 'Should be equal 19')
        self.assertEqual(linked_list.get(2).value, 48, 'Should be equal 48')


    def test_reverse_get(self):
        linked_list = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.reverse()
        self.assertEqual(linked_list.get(0).value, 4, 'Should be equal 4')
        self.assertEqual(linked_list.get(1).value, 3, 'Should be equal 3')
        self.assertEqual(linked_list.get(2).value, 2, 'Should be equal 2')
        self.assertEqual(linked_list.get(3).value, 1, 'Should be equal 1')
        


if __name__ == '__main__':
    unittest.main()
