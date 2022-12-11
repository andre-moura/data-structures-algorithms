import unittest
from linked_list import LinkedList

class TestClass(unittest.TestCase):
    def test_append_get(self):
        linked_list = LinkedList(2)
        linked_list.append(1)
        self.assertEqual(linked_list.get(0), 2, 'Should be equal 2')
        self.assertEqual(linked_list.get(1), 1, 'Should be equal 1')


    def test_pop_get(self):
        linked_list = LinkedList(2)
        linked_list.append(1)
        linked_list.append(56)
        linked_list.append(99)
        linked_list.pop()
        self.assertEqual(linked_list.get(0), 2, 'Should be equal 2')
        self.assertEqual(linked_list.get(1), 1, 'Should be equal 1')
        self.assertEqual(linked_list.get(2), 56, 'Should be equal 56')
        self.assertEqual(linked_list.get(3), None, 'Should be equal None')



    def test_prepend_get(self):
        linked_list = LinkedList(2)
        linked_list.append(1)
        linked_list.append(19)
        linked_list.prepend(48)
        self.assertEqual(linked_list.get(0), 48, 'Should be equal 48')
        self.assertEqual(linked_list.get(1), 2, 'Should be equal 2')
        self.assertEqual(linked_list.get(2), 1, 'Should be equal 1')
        self.assertEqual(linked_list.get(3), 19, 'Should be equal 19')



if __name__ == '__main__':
    unittest.main()
