from enum import IntEnum


class KeyfactorApiPAMProviderTypeParameterCreateRequestDataType(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2

    def __str__(self) -> str:
        return str(self.value)
