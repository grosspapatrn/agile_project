from enum import Enum


class Priorities(Enum):
    VERY_LOW = (1, 'Very Low')
    LOW = (2, 'Low')
    MEDIUM = (3, 'Medium')
    HIGH = (4, 'High')
    CRITICAL = (5, 'Critical')

    # creating a method to formating Enum-values for using fields in model choices
    @classmethod
    def choices(cls):
        return [(key.value[0], key.value[1]) for key in cls]

    def __getitem__(self, item):
        # calling a priority with priority-name
        return self.value[item]