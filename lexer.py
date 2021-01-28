def split(word): 
    return [char for char in word]

def removeEmptyStrings(lst):
    while "" in lst: 
        lst.remove("") 

ints = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
tokenList = []

class Token:

    def __init__(self, token, value):
        self.token = token
        self.value = value
    
    def display(self):
        if self.token == 'ERROR':
            error = Error('UnknownError', 'cannot identify character', str(self.value), 1, r'C:\Users\tanne\My_Codes\Python\ease_language\SAMPLE.py')
            print(error.display())
        else:
            if self.token == 'STRING' or self.token == 'INT':
                pair = f'{self.token}: {self.value}'
            else:
                pair = f'{self.token}'
            return pair
    
    def addToList(self):
        tokenList.append(self.display())


class Lexer:

    def __init__(self, items):
        self.items = split(items)
        self.index = 0
        self.item = ''
        self.stringOn = False
        self.stringList = ''
        self.intOn = False

    def identify(self):
        ints = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        tok = ''
        val = self.item

        if '"' == self.item or "'" == self.item:
            if self.stringOn:
                self.stringOn = False
                tok = 'STRING'
                val = self.getString()
            else:
                self.stringOn = True
        elif self.stringOn:
            self.addToString()
        elif self.item in ' \n':
            pass
        elif '+' == self.item:
            tok = 'PLUS'
        elif '-' == self.item:
            tok = 'MINUS'
        elif '*' == self.item:
            tok = 'MUL'
        elif '/' == self.item:
            tok = 'DIV'
        elif '(' == self.item:
            tok = 'LPAREN'
        elif ')' == self.item:
            tok = 'RPAREN'
        else:
            if self.item in ints:
                tok = 'INT'
            else:
                tok = 'ERROR'
        
        token = Token(tok, val)
        return token.addToList()
    
    def advance(self):
        self.item = self.items[self.index]
        self.index += 1
    
    def displayAll(self):
        removeEmptyStrings(tokenList)
        return tokenList
    
    def addToString(self):
        self.stringList += self.item
    
    def getString(self):
        temp = self.stringList
        self.stringList = ''
        return temp


class Error:

    def __init__(self, error, detail, code, line, fileName):
        self.error = error
        self.detail = detail
        self.code = code
        self.line = line
        self.file = fileName
    
    def display(self):
        return f'File "{self.file}", line {str(self.line)}\n   {self.code}\n{self.error}: {self.detail}'


def run(text):
    wordList = split(text)
    l1 = Lexer(text)

    for word in wordList:
        l1.advance()
        l1.identify()
    
    print(l1.displayAll())
    tokenList.clear()