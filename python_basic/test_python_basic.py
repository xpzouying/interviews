# -*- coding: utf8 -*-

import unittest


"""
    Ref:
        - https://www.toptal.com/python/interview-questions

"""


class PythonBasicTestCase(unittest.TestCase):

    def test_list_with_default_value(self):
        def extendList(val, list=[]):
            list.append(val)
            return list

        list1 = extendList(10)
        list2 = extendList(123,[])
        list3 = extendList('a')

        print "list1 = %s" % list1
        print "list2 = %s" % list2
        print "list3 = %s" % list3

        # NOTE: list1 is equal list3
        self.assertEqual(list1, [10, 'a'])
        self.assertEqual(list2, [123])
        self.assertEqual(list3, [10, 'a'])


    def test_return_loop_mistake(self):
        # Ref: http://docs.python-guide.org/en/latest/writing/gotchas/#late-binding-closures

        def multipliers():
            return [lambda x : i * x for i in range(4)]

        res = [m(2) for m in multipliers()]
        print 'res = ', res

        self.assertEqual(res, [6, 6, 6, 6])


    def test_return_loop_update(self):
        # Ref: http://docs.python-guide.org/en/latest/writing/gotchas/#late-binding-closures

        def multipliers():
            for i in range(4):
                yield lambda x: i * x

        res = [m(2) for m in multipliers()]
        print 'res = ', res

        self.assertEqual(res, [0, 2, 4, 6])


    def test_class_value(self):
        class Parent(object):
            x = 1

        class Child1(Parent):
            pass

        class Child2(Parent):
            pass

        # setting x = 1 in the Parent class makes the class variable x (with a value of 1) referenceable in that class and any of its children.
        # That’s why the first print statement outputs 1 1 1.
        print Parent.x, Child1.x, Child2.x
        self.assertEqual(Parent.x, 1)
        self.assertEqual(Child1.x, 1)
        self.assertEqual(Child2.x, 1)

        # Subsequently, if any of its child classes *overrides* that value (for example, when we execute the statement Child1.x = 2), then the value is changed in that child only.
        # That’s why the second print statement outputs 1 2 1.
        Child1.x = 2
        print Parent.x, Child1.x, Child2.x
        self.assertEqual(Parent.x, 1)
        self.assertEqual(Child1.x, 2)
        self.assertEqual(Child2.x, 1)

        # Finally, if the value is then changed in the Parent (for example,
        # when we execute the statement Parent.x = 3),
        # that change is reflected also by any children that have not yet overridden the value (which in this case would be Child2).
        # That’s why the third print statement outputs 3 2 3.
        Parent.x = 3
        print Parent.x, Child1.x, Child2.x
        self.assertEqual(Parent.x, 3)
        self.assertEqual(Child1.x, 2)
        self.assertEqual(Child2.x, 3)

        # Answer:
        # in Python, class variables are internally handled as dictionaries.
        # overrides the value


    def test_div(self):
        def div1(x,y):
            print "%s/%s = %s" % (x, y, x/y)

            return x/y

        def div2(x,y):
            print "%s//%s = %s" % (x, y, x//y)

            return x//y


        self.assertEqual(div1(5,2), 2)
        self.assertEqual(div1(5.,2), 2.5)
        self.assertEqual(div2(5,2), 2)
        self.assertEqual(div2(5.,2.), 2)


    def test_list_range_1(self):
        list = ['a', 'b', 'c', 'd', 'e']
        print list[10:]

        self.assertEqual(list[10:], [])


    def test_snippet_1(self):
        # NOTE:
        # the key thing to understand here is that the statement
        # list = [ [ ] ] * 5 does NOT create a list containing 5 distinct lists;
        # rather, it creates a a list of 5 references to the same list.

        l = [ [ ] ] * 5
        self.assertEqual(l, [[], [], [], [], []])


        l[0].append(10)
        self.assertEqual(l, [[10], [10], [10], [10], [10]])

        l[1].append(20)
        self.assertEqual(l, [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]])

        l.append(30)
        self.assertEqual(l, [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20],
                             30])
