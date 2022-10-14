from enum import IntEnum


class ModelsRevokeCertificateRequestReason(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_8 = 8
    VALUE_999 = 999
    VALUE_NEGATIVE_1 = -1

    def __str__(self) -> str:
        return str(self.value)
