from lmc.computer.memory_image import MemoryImage
import pytest


class TestMemoryImage:
    def test_get_max_size(self):
        # When I ask for the maximum size of a memory image

        # Then I get maximum size of 100, this is the maximum size of memory
        assert MemoryImage.get_max_size() == 100

    def test_empty_binary_program_gives_error_on_trying_to_access(self):
        # Given an empty memory image

        memory_image = MemoryImage()
        assert len(memory_image) == 0

        # When I try to access an element of the image

        # Then I get an exception

        error_message = 'list index out of range'
        with pytest.raises(IndexError, match=error_message):
            _ = memory_image[0]

    def test_appending_gives_the_correct_size(self):
        # Given an empty memory image

        memory_image = MemoryImage()

        # When I append opcodes

        # Then I get the new correct binary program size

        memory_image.append(201)
        assert len(memory_image) == 1

        memory_image.append(202)
        assert len(memory_image) == 2

    def test_appending_more_than_max_size_gives_exception(self):
        # Given an empty memory image

        memory_image = MemoryImage()

        # When I try to append more opcodes than the maximum size

        # Then I get an exception

        error_message = 'Program exceeds max size of 100 opcodes'
        with pytest.raises(Exception, match=error_message):
            for _ in range(0, MemoryImage.get_max_size() + 2):
                memory_image.append(201)

    def test_python_setitem_and_getitem_methods(self):
        # When the image has an opcode
        memory_image = MemoryImage()
        memory_image.append(201)
        assert len(memory_image) == 1

        # Then I can use the python setitem and getitem methods for that opcode

        memory_image[0] = 202  # setitem
        assert memory_image[0] == 202  # getitem

    def test_python_str_method(self):
        # Given an empty memory image
        memory_image = MemoryImage()

        # When the program has no binary instructions, one or more binary instructions

        # Then I can call the python str method

        assert str(memory_image) == ''  # Empty

        memory_image.append(201)  # One opcode
        assert str(memory_image) == "201\n"

        memory_image.append(202)  # Two opcodes
        assert str(memory_image) == "201\n202\n"
