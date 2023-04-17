# Опишіть класс будь-якого транспортного засобу.
# Скористайтесь двома рівнями наслідування і абстракцією за допомогою ABC
# (використання ABC не рахується за рівень наслідування)

from abc import ABC, abstractmethod


class vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def m_type(self):
        pass


class humvee(vehicle, ABC):
    def move(self):
        pass

    def m_type(self):
        return "Wheel operated lite recon. unit"


class abrams(vehicle, ABC):
    def move(self):
        pass

    def m_type(self):
        return "Main battle tank"


