from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from random import randint


class Building(ABC):
    """
    Інтерфейс компонента оголошує метод прийняття,
    який може приймати будь-який об'єкт, який
    реалізує інтерфейс відвідувача як аргумент.

     Кожен конкретний компонент повинен реалізувати
     метод прийняття, щоб він забезпечив метод
     відвідувача, що відповідає класу компонентів.
     """

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

    @abstractmethod
    def type_building(self) -> None:
        pass


class Home(Building):
    def accept(self, visitor: Visitor) -> str:
        """
        Зверніть увагу, що ми називаємо Visit_Home, що
        відповідає імені поточного класу. Таким чином,
        ми дозволяємо відвідувачу дізнатися, з яким
        класом компонента він працює.
        """
        return visitor.visit_home(self)

    @staticmethod
    def type_building(**kwargs):
        return "Дім"


class Factory(Building):
    def accept(self, visitor: Visitor) -> str:
        return visitor.visit_factory(self)

    @staticmethod
    def type_building(**kwargs):
        return "Фабрика"


class Store(Building):
    def accept(self, visitor: Visitor) -> str:
        return visitor.visit_store(self)

    @staticmethod
    def type_building(**kwargs):
        return "Магазин"

    """
    Конкретні компоненти можуть мати спеціальні методи, 
    які не оголошені у своєму базовому класі чи інтерфейсі. 
    Відвідувач все ще може використовувати ці методи, 
    оскільки він знає про конкретний клас компонента.
    """

    @staticmethod
    def buying(product: str) -> str:
        return f"придбав {product} на {randint(1,2000)} грн. {randint(0,99)} коп."


class Visitor(ABC):
    """
    Інтерфейс відвідувача оголошує набір відвідувань компонентів,
    що відповідають класам. Підпис методу відвідування дозволяє
    відвідувачу визначати конкретний клас компонента, з яким він займається.
    """

    @abstractmethod
    def visit_home(self, element: Home) -> str:
        pass

    @abstractmethod
    def visit_factory(self, element: Factory) -> str:
        pass

    @abstractmethod
    def visit_store(self, element: Store) -> str:
        pass


"""
Конкретні відвідувачі реалізують кілька версій одного і того ж алгоритму, 
які можуть працювати з усіма класами конкретних компонентів.

Ви відчуєте максимальну користь від візерунка до відвідувача, 
використовуючи його зі складною структурою об'єктів, наприклад, дерево шару. 
У цьому випадку було б корисно зберігати певний проміжний стан алгоритму 
під час виконання методів відвідувачів над різними об'єктами структури.
"""


class Builder(Visitor):
    _for_print = "відвіданий БУДІВЕЛЬНИКОМ"

    def visit_factory(self, element: Factory) -> str:
        return f"{element.type_building()} {self._for_print}, час працювати"

    def visit_home(self, element: Home) -> str:
        return f"{element.type_building()} {self._for_print}"

    def visit_store(self, element: Store) -> str:
        return f"{element.type_building()} {self._for_print}, та {element.buying('будівельні матеріали')}"


class Student(Visitor):
    _for_print = "відвіданий СТУДЕНТОМ"

    def visit_factory(self, element: Factory) -> str:
        return f"{element.type_building()} {self._for_print} для практики"

    def visit_home(self, element: Home) -> str:
        return f"{element.type_building()} {self._for_print}, час виконувати лабораторні роботи"

    def visit_store(self, element: Store) -> str:
        return f"{element.type_building()} {self._for_print}, та {element.buying('канцелярії')}"


def client_code(components_list: List[Building], visitor: Visitor) -> None:
    """
    Клієнтський код може виконувати операції відвідувача на будь-якому наборі елементів,
    не з’ясовуючи їх конкретні класи. Операція з прийняттям надсилає дзвінок
    до відповідної операції в закладі відвідувача.
    """
    for component in components_list:
        print(component.accept(visitor))


if __name__ == "__main__":

    print("Студент вирішив прогулятися:")
    components = [Home(), Factory(), Store(), Home()]
    student = Student()
    client_code(components, student)

    print("\nПісля отримання професії:")
    components = [Home(), Factory(), Store(), Home()]
    client_code(components, Builder())
