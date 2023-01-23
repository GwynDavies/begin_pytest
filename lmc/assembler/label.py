from lmc.hardware.instruction import Id


class Label:
    @staticmethod
    def is_label(token):
        """
        If the token is not a mnemonic, then we are considering it a label
        """
        return not Id.from_mnemonic(token)
