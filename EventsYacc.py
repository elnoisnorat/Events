# ------------------------------------------------------------
# EventsYacc.py
# ------------------------------------------------------------
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from EventsLex import tokens

# Import intermediate code module here
import EventsTools

# Primary reduce statement
def p_statement(p):
    '''statement : statement_add
                 | statement_remove
                 | statement_edit
                 | statement_mark
                 | statement_view'''
    p[0] = p[1]
    pass

# Requisites:
#   When invoking add(), make sure to pass down arguments
#   in the correct order of event, date, time.
def p_statement_add(p):
    '''statement_add : statement_add_edt
                           | statement_add_ed
                           | statement_add_e
                           | ADD'''
    p[0] = p[1]
    if(p[1] == 'add'):
        res = EventsTools.add(None, None, None)
        print(res)
    pass
#add an event with date and time
def p_statement_add_edt(p):
    'statement_add_edt : ADD EVENT DATE TIME'
    p[0] = p[1] + p[2] + p[3] + p[4]
    res = EventsTools.add(p[2], p[3], p[4])
    print(res)
#add an event with date
def p_statement_add_ed(p):
    'statement_add_ed : ADD EVENT DATE'
    p[0] = p[1] + p[2] + p[3]
    res = EventsTools.add(p[2], p[3], None)
    print(res)
#just add an event
def p_statement_add_e(p):
    'statement_add_e : ADD EVENT'
    p[0] = p[1] + p[2]
    res = EventsTools.add(p[2], None, None)
    print(res)
#remove an event
def p_statement_remove(p):
    'statement_remove : REMOVE EVENT'
    p[0] = p[1] + p[2]           # evento
    res = EventsTools.remove(p[2])
    print(res)

# Requisites:
#   When invoking edit(), make sure to pass down arguments
#   in the correct order of event, date, time.
def p_statement_edit(p):
    '''statement_edit : statement_edit_edt
                           | statement_edit_ed
                           | statement_edit_et
                           | EDIT'''
    p[0] = p[1]
    if(p[1] == 'edit'):
        res = EventsTools.edit(None, None, None)
        print(res)
    pass
#edit date and time of an event
def p_statement_edit_edt(p):
    'statement_edit_edt : EDIT EVENT DATE TIME'
    p[0] = p[1] + p[2] + p[3] + p[4]
    res = EventsTools.edit(p[2], p[3], p[4])
    print(res)
#edit date of an event
def p_statement_edit_ed(p):
    'statement_edit_ed : EDIT EVENT DATE'
    p[0] = p[1] + p[2] + p[3]
    res = EventsTools.edit(p[2], p[3], None)
    print(res)
#edit time of an event
def p_statement_edit_et(p):
    'statement_edit_et : EDIT EVENT TIME'
    p[0] = p[1] + p[2] + p[3]
    res = EventsTools.edit(p[2], None, p[3])
    print(res)

def p_statement_mark(p):
    'statement_mark : MARK EVENT STATUS'
    p[0] = p[1] + p[2] + p[3]           # evento estado
    res = EventsTools.mark(p[2], p[3])
    print(res)

# Requisites:
#   When invoking view(), make sure to pass down arguments
#   in the correct order of event, date, time.
def p_statement_view(p):
    '''statement_view : statement_view_edt
                           | statement_view_ed
                           | statement_view_et
                           | statement_view_dt
                           | statement_view_e
                           | statement_view_d
                           | statement_view_t
                           | VIEW'''
    p[0] = p[1]
    if(p[1] == 'view'):
        res = EventsTools.available(None, None, None)
        print(res)
    pass

def p_statement_view_edt(p):
    'statement_view_edt : VIEW EVENT DATE TIME'
    p[0] = p[1] + p[2] + p[3] + p[4]
    res = EventsTools.available(p[2], p[3], p[4])
    print(res)

def p_statement_view_ed(p):
    'statement_view_ed : VIEW EVENT DATE'
    p[0] = p[1] + p[2] + p[3]
    res = EventsTools.available(p[2], p[3], None)
    print(res)

def p_statement_view_et(p):
    'statement_view_et : VIEW EVENT TIME'
    p[0] = p[1] + p[2] + p[3]
    res = EventsTools.available(p[2], None, p[3])
    print(res)

def p_statement_view_dt(p):
    'statement_view_dt : VIEW DATE TIME'
    p[0] = p[1] + p[2] + p[3]
    res = EventsTools.available(None, p[2], p[3])
    print(res)

def p_statement_view_e(p):
    'statement_view_e : VIEW EVENT'
    p[0] = p[1] + p[2]
    res = EventsTools.available(p[2], None, None)
    print(res)

def p_statement_view_d(p):
    'statement_view_d : VIEW DATE'
    p[0] = p[1] + p[2]
    res = EventsTools.available(None, p[2], None)
    print(res)

def p_statement_view_t(p):
    'statement_view_t : VIEW TIME'
    p[0] = p[1] + p[2]
    res = EventsTools.available(None, None, p[2])
    print(res)

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

