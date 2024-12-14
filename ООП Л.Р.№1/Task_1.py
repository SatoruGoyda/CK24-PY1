class Tree:
    """
    Класс для описания дерева.
    """

    def __init__(self, age: int, height: float, species: str):
        """
        Инициализация объекта.

        :param age: Возраст дерева в годах. Должен быть неотрицательным.
        :param height: Высота дерева в метрах. Должна быть положительным числом.
        :param species: Вид дерева.
        :raises ValueError: Если возраст отрицательный или высота неположительная.
        """
        if age < 0:
            raise ValueError("Возраст дерева должен быть неотрицательным.")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом.")

        self.age = age
        self.height = height
        self.species = species

    def photosynthesize(self) -> None:
        """
        Метод для фотосинтеза.
        """
        pass

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст и высоту дерева.

        :param years: Количество лет, в течение которых дерево растет. Должно быть положительным.
        :raises ValueError: Если передано отрицательное количество лет.

        >>> tree.grow(5)  # Дерево растет 5 лет
        """
        pass

    def shed_leaves(self) -> None:
        """
        Метод для описания опадания листьев.
        """
        pass


class AbstractSocialMediaPlatform:
    """
    Класс для описания медиа платформы.
    """

    def __init__(self, name: str, user_count: int, is_public: bool):
        """
        Инициализация объекта медиа платформы.

        :param name: Название платформы.
        :param user_count: Количество пользователей. Должно быть неотрицательным.
        :param is_public: Флаг, указывающий, является ли платформа публичной.
        :raises ValueError: Если количество пользователей отрицательное.
        """
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")

        self.name = name
        self.user_count = user_count
        self.is_public = is_public

    def post_content(self, content: str) -> None:
        """
        Метод для публикации контента.

        :param content: Контент для публикации. Должен быть непустым.
        :raises ValueError: Если контент пустой.

        >>> platform.post_content("Hello, world!")  # Публикуем пост
        """
        pass

    def ban_user(self, user_id: int) -> None:
        """
        Метод для бана пользователя.

        :param user_id: ID пользователя для блокировки. Должен быть положительным.
        :raises ValueError: Если ID пользователя неположительный.

        >>> platform.ban_user(12345)  # Блокируем пользователя с ID 12345
        """
        pass

    def change_privacy(self, is_public: bool) -> None:
        """
        Метод для изменения приватности платформы.

        :param is_public: Новый статус приватности (True для публичного, False для приватного).

        >>> platform.change_privacy(False)  # Переводим платформу в приватный режим
        """
        pass


class AbstractTable:
    """
    Класс для описания стола.
    """

    def __init__(self, material: str, number_of_legs: int, weight: float):
        """
        Инициализация объекта стола.

        :param material: Материал, из которого сделан стол.
        :param number_of_legs: Количество ножек стола. Должно быть больше 0.
        :param weight: Вес стола в килограммах. Должен быть положительным.
        :raises ValueError: Если количество ножек или вес не соответствует ограничениям.
        """
        if number_of_legs <= 0:
            raise ValueError("Количество ножек должно быть больше 0.")
        if weight <= 0:
            raise ValueError("Вес стола должен быть положительным.")

        self.material = material
        self.number_of_legs = number_of_legs
        self.weight = weight

    def support_weight(self, load_weight: float) -> bool:
        """
        Проверяет, выдерживает ли стол заданный вес.

        :param load_weight: Вес нагрузки. Должен быть положительным.
        :return: True, если стол выдерживает нагрузку, иначе False.
        :raises ValueError: Если вес нагрузки отрицательный.

        >>> table.support_weight(50.0)  # Проверяем, выдерживает ли стол 50 кг
        True
        """
        pass

    def adjust_height(self, height: float) -> None:
        """
        Регулирует высоту стола.

        :param height: Новая высота стола. Должна быть положительным числом.
        :raises ValueError: Если высота неположительная.

        >>> table.adjust_height(0.8)  # Устанавливаем высоту стола 0.8 метра
        """
        pass

    def disassemble(self) -> None:
        """
        Разбирает стол на составные части.

        >>> table.disassemble()  # Разбираем стол
        """
        pass