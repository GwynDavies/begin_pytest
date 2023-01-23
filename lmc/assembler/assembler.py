from lmc.application.error_fatal import ErrorFatal
from lmc.assembler.pass_one import PassOne
from lmc.assembler.pass_two import PassTwo
from lmc.assembler.symbol_table import SymbolTable
from lmc.computer.memory_image import MemoryImage
from lmc.io.file.executable_program.executable_program_file import ExecutableProgramFile
from lmc.io.file.source_pprogram.source_program import SourceProgram
from lmc.io.file.source_pprogram.source_program_file import SourceProgramFile


class Assembler:
    """
    Two pass assembler for "Little man Computer" assembly language:

    https://en.wikipedia.org/wiki/Little_man_computer

    Converts a file containing a source program, into first an internal program that
    could be executed.

    It does this in 2 passes.

    The first pass converts the source program file into a source program, and a symbol table.

    The second pass converts the source program into an internal program, using the symbol
    table to do this.

    It then saves the internal program as an executable program file - which can be
    executed later.
    """

    def run(self, source_program_file_name):
        """
        Run the assembler to convert the source program file, into an internal program.

        This internal program then gets saved as an executable program file.
        """

        # Load source program file
        source_program_file = SourceProgramFile(source_program_file_name)

        # Exit if the file does not exist or is empty
        if not source_program_file.exists():
            ErrorFatal.exit_file_not_found(source_program_file_name)

        if source_program_file.is_empty():
            ErrorFatal.exit_file_is_empty(source_program_file_name)

        # Do assembler stage - 'pass 1' to get the source instructions and the symbol table
        source_instructions, symbol_table = self._run_pass_one(
            source_program_file)

        # Do assembler stage - 'pass 2' to get the binary program which the computer can execute
        pass_two = PassTwo()
        internal_program = pass_two.assemble_source_instructions(
            symbol_table, source_instructions)

        # Save the internal program, as an executable program file. This can be
        # loaded later back as an internal program and run
        execuatble_program_file_name = source_program_file_name.replace(
            'lmcs', 'lmcb')
        executable_program_file = ExecutableProgramFile(
            execuatble_program_file_name)
        executable_program_file.write(internal_program)

        # Print source program and assembled program as a listing
        self._print_(source_program_file, internal_program, symbol_table)

    def _run_pass_one(self, source_program_file: str) -> (SourceProgram, SymbolTable):
        """
        Perform assembler stage - pass 1

        Convert a source program file, into a source program, and a symbol table
        """

        pass_one = PassOne()

        # Load source program from the file
        source_program_file.read()

        # Decode each of the source instruction file lines, in the file
        pass_one.decode_source_program_file(source_program_file)

        # Get the decoded source program
        source_program = pass_one.get_source_program()

        # Exit if there are errors in the source program, giving the errors to the user
        if source_program.has_errors():
            ErrorFatal.exit_fatal_errors(source_program.get_list_errors())

        # As the source program is valid, we can now also get the symbol table for the source program
        symbol_table = pass_one.get_symbol_table()

        return source_program, symbol_table

    def _print_(self, source_program_file: SourceProgramFile, binary_program: MemoryImage,
                symbol_table: SymbolTable) -> None:
        """
        Print the source program file, and the resulting executable program file
        """
        print("\n\n\n")
        source_sz = len(source_program_file)
        program_sz = len(binary_program)
        assert source_sz == program_sz

        print('          Index                  Source instruction                      Binary opcode')
        for index in range(0, source_sz):
            source_instruction = source_program_file[index].rstrip()
            opcode = binary_program[index]
            print(
                f'          {index:03}                    {source_instruction:20}                    {opcode:03}')

        # Print symbol table
        print("")
        print('Symbol table\n')
        print(symbol_table)
