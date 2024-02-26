class Serf:
    """Базовый класс крепостного."""

    def __init__(self, name: str, birthday: int, height: float):
        """
        Создание и подготовка к работе объекта "Крепостной"

        :param name: Имя крепостного
        :param birthday: Год рождения
        :param height: Рост
        """

        self.name = name
        self.birthday = birthday
        self.height = height

    def __str__(self):
        """
        Возвращает строковое представление о крепостном.
               :return: Информация о крепостном.
        """
        return f"Крепостной {self.name}. Год рождения {self.birthday}. Рост {self.height}"

    def __repr__(self):
        """
        Возвращает строку, представляющую объект класса Serf.
        :return: Представление объекта класса Serf.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, birthday={self.birthday!r}), height={self.height!r})"

    def life_expectancy(self):
        """
        Функция которая вычисляет продолжительность жизни крепостного, при условии что текущий год 2024

        :return: Время эксплуатации этого крепостного в годах

        Примеры:
        >>> serf = Serf('Василий', 1980, 1.8)
        >>> serf.life_expectancy()
        """
        return 2024 - self.birthday



class TimeCapableSerf(Serf):
    """ Дочерний класс Крепостного трудоголика. """

    def __init__(self, name: str, birthday: int, height: float, time_capable: int):
        """
        Подготовка крепостного к работе"

        :param name: Имя крепостного
        :param birthday: Год рождения
        :param height: Рост
        :param time_capable: Максимально допустимое время работы в сутки
        """

        super().__init__(name, birthday, height)
        self.time_capable = time_capable

    def __str__(self):
        """Возвращает строковое представление о крепостном.
        :return: Информация о крепостном.
        """

        return f"Крепостной {self.name}. Год рождения {self.birthday}. Рост {self.height}. Максимально допустимое время работы в сутки {self.time_capable} "

    def aSerf(self, a_time: int):
        """
        Функция, которая определяет, может ли крепостной работать отведённое время
        :param a_time: Время, которое должен работать крепостной

        :return: Может ли крепостной работать столько времени

        Примеры:
        >>> timecanle = TimeCapableSerf('Константин', 1960, 1.2, 23)
        >>> timecanle.aSerf(30)
        Крепостной Константин может работать 23 ч
        """

        if a_time <= self.time_capable:
            print(f"Крепостной {self.name} может работать {a_time} ч.")
        else:
            print(f"Крепостной {self.name} не может работать {a_time} ч.")


class CapableSerf(Serf):
    """ Дочерний класс крепостного работяги. """

    def __init__(self, name: str, birthday: int, height: float, capable: int):
        """
        Подготовка крепостного к работе"

        :param name: Имя крепостного
        :param birthday: Год рождения
        :param height: Рост
        :param capable: Максимально выполнимое количество работы
        """

        super().__init__(name, birthday, height)
        self.capable = capable

    def __str__(self):
        """Возвращает строковое представление о крепостном.
        :return: Информация о крепостном.
        """

        return f"Крепостной {self.name}. Год рождения {self.birthday}. Рост {self.height}. Максимально выполнимое количество работы {self.capable} "

    def bSerf(self, a_capable: int):
        """Функция, которая определяет, может ли крепостной работать

        :param a_capable: Работа, которую нужно выполнить

        :return: Может ли крепомтной выполнить эту работу


        Примеры:
        >>> canle = CapableSerf('Степан', 1940, 1.40, 234)
        >>> canle.bSerf(299)
        Крепостной Василий не может выполнить работу 299.
        """

        if a_capable <= self.height:
            print(f"Крепостной {self.name} может выполнить работу {a_capable}.")
        else:
            print(f"Крепостной {self.name} не может выполнить работу {a_capable}.")


if __name__ == "__main__":
    # Write your solution here
    serf = Serf('Василий', 1980, 1.8)
    timecanle = TimeCapableSerf('Константин', 1960, 1.2, 23)
    canle = CapableSerf('Степан', 1940, 1.40, 234)

    import doctest
    doctest.testmod()
    pass