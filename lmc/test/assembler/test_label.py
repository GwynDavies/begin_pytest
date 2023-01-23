from lmc.assembler.label import Label
import pytest


class TestLabel:
    """Test a source language token can be identified as a 'label'"""

    parameterized_test_values = [
        # Is a label as this is not a source language instruction mnemonic
        ("LABEL", True),
        ("ADD", False),  # Is a source language instruction mnemonic
    ]

    @pytest.mark.parametrize("source_file_token, expected_result", parameterized_test_values)
    def test_is_label(self, source_file_token, expected_result):
        # Given a parameter for a test token

        # When I call the is_label method

        # Then I should get true if the source language instruction mnemonic
        assert Label.is_label(source_file_token) is expected_result
