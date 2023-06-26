import unittest
from unittest.mock import patch
from random import choice, randint
from Visitor import Building, Home, Factory, Store, Visitor, Student, Builder

class LiteTest(unittest.TestCase):
   def test_lite(self):
       self.assertEqual(Home().accept(Student()), "Дім відвіданий СТУДЕНТОМ, час виконувати лабораторні роботи")
       self.assertEqual(Store().accept(Student())[:54], "Магазин відвіданий СТУДЕНТОМ, та придбав канцелярії на")
       self.assertEqual(Factory().accept(Student()), "Фабрика відвіданий СТУДЕНТОМ для практики")

       self.assertEqual(Store().accept(Builder())[:68], "Магазин відвіданий БУДІВЕЛЬНИКОМ, та придбав будівельні матеріали на")
       self.assertEqual(Home().accept(Builder()), "Дім відвіданий БУДІВЕЛЬНИКОМ")
       self.assertEqual(Factory().accept(Builder()), "Фабрика відвіданий БУДІВЕЛЬНИКОМ, час працювати")

   def test_hard_push(self):
       for i in range(10000):
           self.assertEqual(Home().accept(Student()), "Дім відвіданий СТУДЕНТОМ, час виконувати лабораторні роботи")
           self.assertEqual(Store().accept(Student())[:54], "Магазин відвіданий СТУДЕНТОМ, та придбав канцелярії на")
           self.assertEqual(Factory().accept(Student()), "Фабрика відвіданий СТУДЕНТОМ для практики")
           self.assertEqual(Store().accept(Builder())[:68],
                            "Магазин відвіданий БУДІВЕЛЬНИКОМ, та придбав будівельні матеріали на")
           self.assertEqual(Home().accept(Builder()), "Дім відвіданий БУДІВЕЛЬНИКОМ")
           self.assertEqual(Factory().accept(Builder()), "Фабрика відвіданий БУДІВЕЛЬНИКОМ, час працювати")

class TestBuilding(unittest.TestCase):
    def test_accept(self):
        with self.assertRaises(TypeError):
            Building().accept(choice([Student(), Builder()]))

class TestHome(unittest.TestCase):
    def test_accept(self):
        home = Home()
        with self.assertRaises(TypeError):
            home.accept(Visitor())

    def test_type_building(self):
        home = Home()
        self.assertEqual(home.type_building(), "Дім")

class TestFactory(unittest.TestCase):
    def test_accept(self):
        factory = Factory()
        with self.assertRaises(TypeError):
            factory.accept(Visitor())

    def test_type_building(self):
        factory = Factory()
        self.assertEqual(factory.type_building(), "Фабрика")

class TestStore(unittest.TestCase):
    def test_accept(self):
        store = Store()
        with self.assertRaises(TypeError):
            store.accept(Visitor())

    def test_type_building(self):
        store = Store()
        self.assertEqual(store.type_building(), "Магазин")

    def test_buying(self):
        store = Store()
        self.assertEqual(store.buying("product")[:18], "придбав product на")


class TestStudent(unittest.TestCase):
    def test_visit_home(self):
        home = Home()
        self.assertEqual(Student().visit_home(home), "Дім відвіданий СТУДЕНТОМ, час виконувати лабораторні роботи")

    def test_visit_factory(self):
        factory = Factory()
        self.assertEqual(Student().visit_factory(factory), "Фабрика відвіданий СТУДЕНТОМ для практики")

    @patch('random.randint')
    def test_visit_store(self, mock_randint):
        mock_randint.side_effect = lambda a, b: randint(a, b)
        store = Store()
        result = Student().visit_store(store)
        self.assertIn("Магазин відвіданий СТУДЕНТОМ, та придбав канцелярії на", result)


class TestBuilder(unittest.TestCase):
    def test_visit_home(self):
        home = Home()
        self.assertEqual(Builder().visit_home(home), "Дім відвіданий БУДІВЕЛЬНИКОМ")

    def test_visit_factory(self):
        factory = Factory()
        self.assertEqual(Builder().visit_factory(factory), "Фабрика відвіданий БУДІВЕЛЬНИКОМ, час працювати")

    @patch('random.randint')
    def test_visit_store(self, mock_randint):
        mock_randint.side_effect = lambda a, b: randint(a, b)
        store = Store()
        result = Builder().visit_store(store)
        self.assertIn("Магазин відвіданий БУДІВЕЛЬНИКОМ, та придбав будівельні матеріали на", result)

if __name__ == "__main__":
    unittest.main()
