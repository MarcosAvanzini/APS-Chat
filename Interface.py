from cgitb import text
import imp
from operator import truediv
import socket
from sre_parse import State
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

host = '127.0.0.1' #Localhost
porta = 24546 #Porta

class Client:

    def __init__(self, host, port):
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tkinter.Tk()
        msg.withdraw()
        
        self.apelido = simpledialog.askstring("Nick", "Defina seu Nick aqui!!", parent=msg)

        self.gui_done = False


        self.running = True

        gui_thread = threading.Thread(target=gui_loop)
        receber_thread = threading.Thread(target=receber)

        gui_thread.start()
        receber_thread.start()

def gui_loop(self):
    
    self.win = tkinter.Tk()
    self.win.configure(bg="#5865F2")
    
    self.chat_label = tkinter.Label(self.win, text="Chat:", bg="#5865F2")
    self.chat_label.config(font=("Arial", 12))
    self.chat_label.pack(padx=20, pady=5)

    self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
    self.text_area.pack(padx=20, pady=5)
    self.text_area.config(state='disabled')

    self.msg_label = tkinter.Label(self.win, text="Mensagem: ", bg="#5865F2")
    self.msg_label.config(font=("Arial", 12))
    self.msg_label.pack(padx=20, pady=5)

    self.input_area = tkinter.Text(self.win, height=3)
    self.input_area.pack(padx=20, pady=5)

    self.botao_enviar = tkinter.Button(self.win, text="Enviar", command=self.write)
    self.botao_enviar.config(font=("Arial", 12))
    self.botao_enviar.pack(padx=20, pady=5)

    self.gui_done = True

    self.win.protocol("WM_DELETE_WINDOW", self.parar)
    
    self.win.mainloop()

def escrever(self):
    mensagem = f"{self.apelido}: {self.input_area.get('1.0', 'end')}"
    self.sock.send(mensagem.encode('utf-8'))
    self.input_area.delete('1.0', 'end')



def parar(self):
    self.running = False
    self.win.destroy()
    self.sock.close()
    exit(0)


def receber(self):
    while self.running:
        try:
            mensagem = self.sock.recv(1024)
            if mensagem == 'NICK':
                self.sock.send(self.apelido.encode('utf-8'))
            else:
                if self.gui_done:
                    self.text_area.config(state='normal')
                    self.text_area.insert('end', mensagem)
                    self.text_area.yview('end')
                    self.text_area.config(state='disabled')

        except ConnectionAbortedError:
            break
        except:
            print("Ocorreu um Erro")
            self.sock.close()
            break

interface = Client(host, porta)

    
    
        