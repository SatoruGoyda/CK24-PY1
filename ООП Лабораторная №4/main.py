from abc import ABC, abstractmethod

class ElectronicDevice(ABC):
    """
    Базовый класс для электронных устройств.
    """

    def __init__(self, brand: str, model: str, power: int) -> None:
        """
        Инициализация устройства.
        :param brand: Бренд устройства
        :param model: Модель устройства
        :param power: Потребляемая мощность
        """
        self._brand = brand  # Защищенный, так как не должен изменяться
        self._model = model  # Аналогично с моделью
        self.power = power

    def __str__(self) -> str:
        return f"{self._brand} {self._model} (Мощность: {self.power} Вт)"

    def __repr__(self) -> str:
        return f"ElectronicDevice(brand={self._brand}, model={self._model}, power={self.power})"

    @abstractmethod
    def turn_on(self) -> None:
        """
        Абстрактный метод включения устройства.
        """
        pass

    @abstractmethod
    def turn_off(self) -> None:
        """
        Абстрактный метод выключения устройства.
        """
        pass


class Smartphone(ElectronicDevice):
    """
    Класс для смартфонов.
    """

    def __init__(self, brand: str, model: str, power: int, os: str, storage: int) -> None:
        """
        Инициализация смартфона.
        :param brand: Бренд смартфона
        :param model: Модель смартфона
        :param power: Потребляемая мощность
        :param os: Операционная система
        :param storage: Объем памяти
        """
        super().__init__(brand, model, power)
        self.os = os
        self.storage = storage

    def __str__(self) -> str:
        return f"{self._brand} {self._model} ({self.os}, {self.storage} ГБ)"

    def turn_on(self) -> None:
        print(f"{self._brand} {self._model} включается...")

    def turn_off(self) -> None:
        print(f"{self._brand} {self._model} выключается...")

    def install_app(self, app_name: str) -> None:
        """
        Устанавливает приложение на смартфон.
        :param app_name: Название приложения
        """
        print(f"Установка {app_name} на {self._brand} {self._model}...")


class Laptop(ElectronicDevice):
    """
    Класс для ноутбуков.
    """

    def __init__(self, brand: str, model: str, power: int, ram: int, gpu: str) -> None:
        """
        Инициализация ноутбука.
        :param brand: Бренд ноутбука
        :param model: Модель ноутбука
        :param power: Потребляемая мощность
        :param ram: Объем оперативной памяти
        :param gpu: Графический процессор
        """
        super().__init__(brand, model, power)
        self.ram = ram
        self.gpu = gpu

    def __repr__(self) -> str:
        """
        Переопределение метода __repr__, чтобы отобразить новые атрибуты.
        """
        return f"Laptop(brand={self._brand}, model={self._model}, power={self.power}, ram={self.ram}, gpu={self.gpu})"

    def turn_on(self) -> None:
        print(f"{self._brand} {self._model} запускается...")

    def turn_off(self) -> None:
        print(f"{self._brand} {self._model} выключается...")

    def upgrade_ram(self, additional_ram: int) -> None:
        """
        Увеличение оперативной памяти ноутбука.
        :param additional_ram: Количество добавляемой памяти
        """
        self.ram += additional_ram
        print(f"Оперативная память увеличена до {self.ram} ГБ.")


# Пример использования
if __name__ == "__main__":
    phone = Smartphone("Apple", "iPhone 14", 20, "iOS", 128)
    laptop = Laptop("Dell", "XPS 15", 65, 16, "NVIDIA RTX 3050")

    print(phone)
    phone.turn_on()
    phone.install_app("WhatsApp")
    phone.turn_off()

    print(laptop)
    laptop.turn_on()
    laptop.upgrade_ram(16)
    laptop.turn_off()