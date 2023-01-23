import io


class SymbolTable():
    def __init__(self):
        self.symbol_table = {}

    def __len__(self):
        return len(self.symbol_table)

    def __getitem__(self, key):
        return self.symbol_table[key]

    def __setitem__(self, symbol, address):
        self.symbol_table[symbol] = address

    def __str__(self):
        output = io.StringIO()

        for key, value in sorted(self.symbol_table.items()):
            print(f'{key:20} : {value:3}', file=output)

        contents = output.getvalue()
        output.close()
        return contents
