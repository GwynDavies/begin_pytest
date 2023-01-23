# Need this, in order to use the types from this file, this should be
# the default behavior in Python 3.11
# https://stackoverflow.com/questions/42845972/typed-python-using-the-classes-own-type-inside-class-definition
from __future__ import annotations
from enum import Enum, unique, auto
from typing import Union

# Enum https://docs.python.org/3/library/enum.html


@unique
class Id(Enum):
    """
    For identifying an instruction, internally in the computer

    Usage : Id.from_str('ADD') -> Id.ADD
    Usage : Id.from_str('BAD') -> None
    Usage : Id.from_str('ADD') == Id.ADD -> True
    Usage : Id.from_str('BAD') == None   -> True
    Usage : if Id.from_str('ADD'):
                print('Found')
    """
    ADD = auto()
    SUB = auto()
    STA = auto()
    LDA = auto()
    BRA = auto()
    BRZ = auto()
    BRP = auto()
    INP = auto()
    OUT = auto()
    HLT = auto()
    DAT = auto()

    @staticmethod
    def from_mnemonic(mnemonic: str) -> Union[Id | None]:
        """Take the string value for a mnemonic, and convert it to the corresponding instruction id

        If there is no match for the mnemonic string, then return None"""
        if mnemonic in Id.__members__:
            return Id[mnemonic]
        return None

    @staticmethod
    def mnemonic_has_no_label(mnemonic: str) -> Union[Id | None]:
        """These mnemonics, cannot have a label before them

        If there is no match for the mnemonic string, then return None"""
        if mnemonic in ['INP', 'OUT', 'HLT']:
            return Id[mnemonic]
        return None

    @staticmethod
    def mnemonic_has_label(mnemonic: str) -> Union[Id | None]:
        """These mnemonics, can have a label before them

        If there is no match for the mnemonic string, then return None"""
        if mnemonic in ['ADD', 'SUB', 'STA', 'LDA', 'BRA', 'BRZ', 'BRP']:
            return Id[mnemonic]
        return None


class InstructionBuilder:
    @staticmethod
    def build(instruction_id: Id) -> Union[ADD | SUB | STA | LDA | BRA | BRZ | BRP | INP | OUT | HLT | DAT]:
        instruction_id_lookup = {
            Id.ADD: ADD(),
            Id.SUB: SUB(),
            Id.STA: STA(),
            Id.LDA: LDA(),
            Id.BRA: BRA(),
            Id.BRZ: BRZ(),
            Id.BRP: BRP(),
            Id.INP: INP(),
            Id.OUT: OUT(),
            Id.HLT: HLT(),
            Id.DAT: DAT()
        }

        result = instruction_id_lookup.get(instruction_id)

        if result:
            return result
        raise Exception("Not recognized")


class Instruction:
    def __init__(self, instruction_id: Id):
        self.instruction_id: Id = instruction_id


class ADD(Instruction):
    """
    Internal computer addition instruction
    """

    def __init__(self, address=None):
        Instruction.__init__(self, Id.ADD)
        self.address = address

    def get_code(self) -> int:
        if self.address is not None:
            return 100 + self.address
        raise Exception('Address not set')

    def get_address(self) -> int:
        return self.address

    def set_address(self, address: int):
        self.address = address


class SUB(Instruction):
    """
    Internal computer subtraction instruction
    """

    def __init__(self, address=None):
        Instruction.__init__(self, Id.SUB)
        self.address = address

    def get_code(self) -> int:
        if self.address is not None:
            return 200 + self.address
        raise Exception('Address not set')

    def get_address(self) -> int:
        return self.address

    def set_address(self, address: int):
        self.address = address


class STA(Instruction):
    """
    Internal computer instruction, to store the accumulator into a memory location
    """

    def __init__(self, address=None):
        Instruction.__init__(self, Id.STA)
        self.address = address

    def get_code(self) -> int:
        if self.address is not None:
            return 300 + self.address
        raise Exception('Address not set')

    def get_address(self) -> int:
        return self.address

    def set_address(self, address: int):
        self.address = address


class LDA(Instruction):
    """
    Internal computer instruction, to load the accumulator from a memory location
    """

    def __init__(self, address=None):
        Instruction.__init__(self, Id.LDA)
        self.address = address

    def get_code(self) -> int:
        if self.address is not None:
            return 500 + self.address
        raise Exception('Address not set')

    def get_address(self) -> int:
        return self.address

    def set_address(self, address: int):
        self.address = address


class BRA(Instruction):
    """
    Internal computer instruction, unconditional branch to a memory location
    """

    def __init__(self, address=None):
        Instruction.__init__(self, Id.BRA)
        self.address = address

    def get_code(self) -> int:
        if self.address is not None:
            return 600 + self.address
        raise Exception('Address not set')

    def get_address(self) -> int:
        return self.address

    def set_address(self, address: int):
        self.address = address


class BRZ(Instruction):
    """
    Internal computer instruction, unconditional branch to a memory location - if the accumulator is zero
    """

    def __init__(self, address=None):
        Instruction.__init__(self, Id.BRZ)
        self.address = address

    def get_code(self) -> int:
        if self.address is not None:
            return 700 + self.address
        raise Exception('Address not set')

    def get_address(self) -> int:
        return self.address

    def set_address(self, address: int):
        self.address = address


class BRP(Instruction):
    """
    Internal computer instruction, unconditional branch to a memory location - if the accumulator is positive
    """

    def __init__(self, address=None):
        Instruction.__init__(self, Id.BRP)
        self.address = address

    def get_code(self) -> int:
        if self.address is not None:
            return 800 + self.address
        raise Exception('Address not set')

    def get_address(self) -> int:
        return self.address

    def set_address(self, address: int):
        self.address = address


class INP(Instruction):
    """
    Internal computer instruction, to input a value from the user to the accumulator
    """

    def __init__(self):
        Instruction.__init__(self, Id.INP)

    def get_code(self) -> int:
        return 901


class OUT(Instruction):
    """
    Internal computer instruction, to output a value from the accumulator to the user
    """

    def __init__(self):
        Instruction.__init__(self, Id.OUT)

    def get_code(self) -> int:
        return 902


class HLT(Instruction):
    """
    Internal computer instruction, to halt the currently executing program
    """

    def __init__(self):
        Instruction.__init__(self, Id.HLT)

    def get_code(self) -> int:
        return 0


class DAT(Instruction):
    """
    Mnuemonic assembler instruction, to allocate memory for a value in memory - and optionally set the value
    """

    def __init__(self, initial_value=0):
        Instruction.__init__(self, Id.DAT)
        self.initial_value = initial_value

    def get_code(self) -> int:
        return self.initial_value
