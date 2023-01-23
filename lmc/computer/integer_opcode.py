from lmc.hardware.instruction import ADD, SUB, HLT, STA, LDA, BRA, BRZ, BRP, INP, OUT, DAT, Instruction


class IntegerOpcode:

    def convert_to_instruction(self, opcode: int) -> Instruction:
        """
        For decoding an integer opcode, into a computer instruction
        """
        # 000	HLT
        if opcode == 000:
            instruction = HLT()
        # 1xx	ADD
        elif 100 <= opcode < 200:
            instruction = ADD(opcode-100)
        # 2xx	SUB
        elif 200 <= opcode < 300:
            instruction = SUB(opcode-200)
        # 3xx	STA
        elif 300 <= opcode < 400:
            instruction = STA(opcode-300)
        # 5xx    LDA
        elif 500 <= opcode < 600:
            instruction = LDA(opcode-500)
        # 6xx	BRA
        elif 600 <= opcode < 700:
            instruction = BRA(opcode-600)
        # 7xx	BRZ
        elif 700 <= opcode < 800:
            instruction = BRZ(opcode-700)
        # 8xx	BRP
        elif 800 <= opcode < 900:
            instruction = BRP(opcode-800)
        # 901	INP
        elif opcode == 901:
            instruction = INP()
        # 902	OUT
        elif opcode == 902:
            instruction = OUT()
        # Anything else consider a DAT
        else:
            instruction = DAT()

        return instruction
