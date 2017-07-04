# ------------------------------------------------------------
# EventsLex.py
# ------------------------------------------------------------
import ply.lex as lex

# Reserved words
reserved = {
   'add' : 'ADD',
   'remove' : 'REMOVE',
   'edit' : 'EDIT',
   'mark' : 'MARK',
   'view' : 'VIEW'
}

# List of token names. This is always required
tokens = [
    'EVENT',
    'DATE',
    'TIME',
    'STATUS'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_EVENT = r'[a-zA-Z_]'
t_STATUS = r'[a-zA-Z_]'
t_DATE = r'[0-9]{2}'+r'/'+r'[0-9]{2}'+r'/'+r'[0-9]{2}'
t_TIME = r'[0-9]{2}'+r':'+r'[0-9]{2}'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()