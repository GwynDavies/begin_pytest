class TestDataOpcodes:

    @staticmethod
    def opcodes_subtract():
        program_opcodes = [
            901,  # INP
            308,  # STA
            901,  # INP
            309,  # STA
            508,  # LDA
            209,  # SUB
            902,  # OUT
            000,  # HLT
            000,  # DAT 0
            000   # DAT 0
        ]
        return program_opcodes
