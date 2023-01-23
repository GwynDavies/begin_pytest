from lmc.assembler.pass_one import PassOne
import pytest


class TestSymbolTable:
    """Test the symbol table can hold the values for corresponding source language instructions"""

    @pytest.fixture
    def fixture_symbol_table(self):
        # Perform assembler Pass One operation
        pass_one = PassOne()
        pass_one.decode_source_line('Label0 INP')  # Address 0
        pass_one.decode_source_line('STA Label2')
        pass_one.decode_source_line('LDA Label3')
        pass_one.decode_source_line('Label1 OUT')  # Address 3
        pass_one.decode_source_line('Label2 DAT')  # Address 4
        pass_one.decode_source_line('Label3 DAT')  # Address 5

        # Get the corresponding symbol table for the source instructions processed by "pass one"
        return pass_one.get_symbol_table()

    def test_get_values_from_symbol_table(self, fixture_symbol_table):
        """Test I can get the value from a symbol table"""

        # Given a symbol table which has values
        symbol_table = fixture_symbol_table

        # Then the symbol table gives the correct number of values its contains
        assert len(symbol_table) == 4

        # And the symbol table returns the correct values in order
        assert symbol_table['Label0'] == 0
        assert symbol_table['Label1'] == 3
        assert symbol_table['Label2'] == 4
        assert symbol_table['Label3'] == 5

    def test_get_the_symbol_table_as_a_string(self, fixture_symbol_table):
        """Test I can get the symbol table as a string"""

        # Given a symbol table which has values
        symbol_table = fixture_symbol_table

        # Then I can get a string representation of the symbol table and its values
        expected_string_value_of_symbol_table = "Label0               :   0\n" + \
            "Label1               :   3\n" + \
            "Label2               :   4\n" + \
            "Label3               :   5\n"
        assert expected_string_value_of_symbol_table == str(symbol_table)
