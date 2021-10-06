import json
from typing import Dict
import codecs

class Student():
    def __init__(self, basic_information: str) -> None:
        self._basic_information = basic_information

    def operation(self, additional_information: str) -> None:
        b = json.dumps(self._basic_information)
        a = json.dumps(additional_information)
        print('Основная информация - ' +codecs.decode(r'' +b,'unicode-escape') +'. Дополнительная информация - ' +codecs.decode(r'' +a, 'unicode-escape'))

class StudentFactory():
    _students: Dict[str, Student] = {}

    def __init__(self, initial_students: Dict) -> None:
        for state in initial_students:
            self._students[self.get_key(state)] = Student(state)

    def get_key(self, state: Dict) -> str:
        return " ".join((state))

    def get_student(self, basic_information: Dict) -> Student:
        key = self.get_key(basic_information)

        if not self._students.get(key):
            print("База студентов: Инфорамации об этом студенте ещё нету в базе, добавляем информацию о новом студенте в базу.")
            self._students[key] = Student(basic_information)
        else:
            print("База студентов: Информация о этом студенте уже есть в базе.")

        return self._students[key]

    def list_student(self) -> None:
        count = len(self._students)
        print(f"База студентов: {count} информации о студентах сохранено в базе")
        print("\n".join(map(str, self._students.keys())), end="")


def add_student(
    factory: StudentFactory, surname: str, name: str, year_of_birth: str,
    height: str, blood_group: str
) -> None:
    print("\n\nДобавление информации о студенте в базу")
    student = factory.get_student([surname, name, year_of_birth])
    student.operation([height, blood_group])


if __name__ == "__main__":
    factory = StudentFactory([
        ["Иванов", "Иван", "2000"],
        ["Максимов", "Максим", "2000"],
        ["Степанов", "Степан", "2001"],
    ])

    factory.list_student()

    add_student(factory, "Степанов", "Степан", "2001", "180", "I+")
    add_student(factory, "Петров", "Пётр", "1999", "180", "I-")
    print("\n")

    factory.list_student()