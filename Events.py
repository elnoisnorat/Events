
# ------------------------------------------------------------
# Events.py
# ------------------------------------------------------------

# Import parser to start execution
from EventsYacc import parser

def main():
    while True:
        try:
            s = raw_input('Events > ')
        except EOFError:
            break
        if s == 'quit': break
        if not s: continue
        result = parser.parse(s)

if __name__ == '__main__':
    main()