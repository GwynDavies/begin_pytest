from lmc.hardware.instruction import ADD, SUB, STA, LDA, BRA, BRZ, BRP, INP, OUT, HLT, Instruction
from lmc.computer.integer_opcode import IntegerOpcode


class Processor:
    """
    Processes the internal computer instructions, that are stored in the computer's memory
    """

    def __init__(self, program_counter, memory, accumulator, inp, out):
        self.program_counter = program_counter
        self.memory = memory
        self.accumulator = accumulator
        self.inp = inp
        self.out = out

    def run_program(self):
        """
        Execute the integer opcodes that are storied in the computer memory.

        To do this, convert the opcodes into the corresponding computer instruction,
        which can then be executed by the processor
        """

        # Initialize program counter, to first memory address
        self.program_counter.set_value(0)

        integer_opcode_decoder = IntegerOpcode()
        while True:
            opcode: int = self.memory.get_value(
                self.program_counter.get_value())
            instruction: Instruction = integer_opcode_decoder.convert_to_instruction(
                opcode)

            # If the instruction is HLT, then stop executing the program
            if isinstance(instruction, HLT):
                break

            # Process the computer instruction
            self.process_instruction(instruction)

    def process_instruction(self, instruction):
        """
        Process a known computer instructions

        If the instruction is not recognized, it is just ignored as it requires no processing - such
        as a instruction
        """
        if isinstance(instruction, ADD):
            self.do_add(instruction.get_address())
        elif isinstance(instruction, SUB):
            self.do_sub(instruction.get_address())
        elif isinstance(instruction, STA):
            self.do_sta(instruction.get_address())
        elif isinstance(instruction, LDA):
            self.do_lda(instruction.get_address())
        elif isinstance(instruction, BRA):
            self.do_bra(instruction.get_address())
        elif isinstance(instruction, BRZ):
            self.do_brz(instruction.get_address())
        elif isinstance(instruction, BRP):
            self.do_brp(instruction.get_address())
        elif isinstance(instruction, INP):
            self.do_inp()
        elif isinstance(instruction, OUT):
            self.do_out()

    def do_add(self, address):
        """ Add value in memory, to the accumulator """
        value_from_memory = self.memory.get_value(address)
        value_from_accumulator = self.accumulator.get_value()
        new_accumulator_value = value_from_accumulator + value_from_memory
        self.accumulator.set_value(new_accumulator_value)

    def do_sub(self, address):
        """ Subtract value in memory, from the accumulator """
        value_from_memory = self.memory.get_value(address)
        value_from_accumulator = self.accumulator.get_value()
        new_accumulator_value = value_from_accumulator - value_from_memory
        self.accumulator.set_value(new_accumulator_value)

    def do_sta(self, address):
        """ Store the accumulator's value into memory """
        value = self.accumulator.get_value()
        self.memory.set_value(address, value)

    def do_lda(self, address):
        """ Load the accumulator's value from memory """
        value = self.memory.get_value(address)
        self.accumulator.set_value(value)

    def do_bra(self, address):
        self.program_counter.set_value(address)

    def do_brz(self, address):
        value = self.accumulator.get_value()
        if value == 0:
            self.program_counter.set_value(address)

    def do_brp(self, address):
        value = self.accumulator.get_value()
        if value >= 0:
            self.program_counter.set_value(address)

    def do_inp(self):
        """ Get value from the user, store in in the INPut Buffer, and then the accumulator """
        value = self.inp.get_value()
        self.accumulator.set_value(value)

    def do_out(self):
        value = self.accumulator.get_value()
        self.out.write_value(value)

    def get_program_counter(self):
        return self.program_counter

    def get_memory(self):
        return self.memory

    def get_accumulator(self):
        return self.accumulator

    def get_input_buffer(self):
        return self.inp

    def get_output_buffer(self):
        return self.out
