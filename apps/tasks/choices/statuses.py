from enum import Enum


# creating model Statuses
class Statuses(Enum):
    NEW = 'NEW'
    IN_PROGRESS = 'IN_PROGRESS'
    PENDING = 'PENDING'
    BLOCKED = 'BLOCKED'
    TESTING = 'TESTING'
    CLOSED = 'CLOSED'

    # creating a method to use Enum-values like CHOICES for a django field model
    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]