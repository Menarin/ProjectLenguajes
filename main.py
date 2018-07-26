import Parser
import MiTokens
from ply.lex import lex
from ply.yacc import yacc
from tkinter import *
from tkinter import scrolledtext


lexer = lex(module=MiTokens)
parser = yacc(module=Parser)

x = "d = lambda d,Y=\"5aas\": (X * 5)"
# x2= "B = lambda X: X*2"
# x3= "B = lambda X,Y,Z=1: X + X"
# x4 = "B = map(lambda X : X + 3, [0,1,4,6]"
x5 = 'B = filter(lambda X: int if X > 4 else "menor",[0,1,4,6])'
x6 = 'B = map(lambda Z: str if Z == "verde" else "falso",["verde", "rojo"])'
x7 = 'B = filter(lambda X: X - 2 >= 5, [0,10,14,6])'
x8 = 'b=reduce(lambda X, Y: X + Y, Nums)'
x9 = 'B = filter(lambda X: X  >= 8, [0,10,14,6])'
x10 = 'b = map(lambda Y: Y *6, Items) '

window = Tk()

window.title("Python expr checker")

lbl = Label(window, text="Your expression: ")

lbl.grid(column=0, row=1)

txt = Entry(window, width=40)

txt.grid(column=0, row=0)

txt2 = scrolledtext.ScrolledText(window, state=DISABLED, width=30, height=10)

txt2.grid(column=0, row=3, sticky=W)

txt.focus()


def clicked():
    txt2.configure(state=NORMAL)
    txt2.delete(1.0, END)
    txt2.configure(state=DISABLED)
    res = "Your expression:  " + txt.get()
    lbl.configure(text=res)
    lexer.input(txt.get())
    for i in lexer:
        s = str(i.value)
        txt2.configure(state=NORMAL)
        txt2.insert(INSERT, i.type + ' : ' + s + '\n')
        txt2.configure(state=DISABLED)
    parser.parse(txt.get(), lexer,False,True)


btn = Button(window, text="Check", command=clicked)

btn.grid(column=2, row=0)

window.mainloop()

# tok = lexer.token()

# while tok is not None:
#    print(tok.type + ': ', tok.value)
#    tok = lexer.token()






