# сортировка сложных структур с использованием ключа

from collections import namedtuple
from operator import attrgetter

Person = namedtuple('Person', 'name, age')

p_1 = Person('Коля', 25)
p_2 = Person('Вася', 30)
p_3 = Person('Оля', 20)

people = [p_1, p_2, p_3]
print(people)


def by_age(person):
    return person.age


# [Person(name='Коля', age=25), Person(name='Вася', age=30), Person(name='Оля', age=20)]

result = sorted(people)
print(result)

# [Person(name='Коля', age=25), Person(name='Вася', age=30), Person(name='Оля', age=20)]
# [Person(name='Вася', age=30), Person(name='Коля', age=25), Person(name='Оля', age=20)]

result = sorted(people, key=by_age)
print(result)

# [Person(name='Коля', age=25), Person(name='Вася', age=30), Person(name='Оля', age=20)]
# [Person(name='Вася', age=30), Person(name='Коля', age=25), Person(name='Оля', age=20)]
# [Person(name='Оля', age=20), Person(name='Коля', age=25), Person(name='Вася', age=30)]

result_2 = sorted(people, key=attrgetter('age'))
print(result_2)

# [Person(name='Коля', age=25), Person(name='Вася', age=30), Person(name='Оля', age=20)]
# [Person(name='Вася', age=30), Person(name='Коля', age=25), Person(name='Оля', age=20)]
# [Person(name='Оля', age=20), Person(name='Коля', age=25), Person(name='Вася', age=30)]
# [Person(name='Оля', age=20), Person(name='Коля', age=25), Person(name='Вася', age=30)]

