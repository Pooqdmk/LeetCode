class Spreadsheet:

    def __init__(self, rows: int):
        self.d={ chr(i+97).upper():i for i in range(26)}
        self.sheet=[[0 for j in range(26)]for i in range(rows)]


    def setCell(self, cell: str, value: int) -> None:
        col,row=cell[0],int(cell[1:])-1
        
        self.sheet[row][self.d[col]] = value

    def resetCell(self, cell: str) -> None:
        col,row=cell[0],int(cell[1:])-1
        self.sheet[row][self.d[col]]=0

    def getValue(self, formula: str) -> int:

        x,y=formula.split('+')
        x=x[1:]

        if x.isdigit():
            val1=int(x)
        else:
            col,row=x[0],int(x[1:])-1
            val1 = self.sheet[row][self.d[col]]
        
        if y.isdigit():
            val2=int(y)
        else:
            col,row=y[0],int(y[1:])-1
            val2 = self.sheet[row][self.d[col]]
        return val1+val2
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)