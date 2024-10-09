from tkinter import *
from tkinter import messagebox

class No:
    def __init__(self, key, dir=None, esq=None):
        self.item = key
        self.dir = dir
        self.esq = esq
        self.altura = 1  # Nova propriedade para armazenar a altura do nó

class AVLTree:
    def __init__(self):
        self.root = None

    def inserir(self, root, key):
        if not root:
            return No(key)
        elif key < root.item:
            root.esq = self.inserir(root.esq, key)
        else:
            root.dir = self.inserir(root.dir, key)

        root.altura = 1 + max(self.get_altura(root.esq), self.get_altura(root.dir))
        balance = self.get_balance(root)

        if balance > 1 and key < root.esq.item:
            return self.rotate_right(root)
        if balance < -1 and key > root.dir.item:
            return self.rotate_left(root)
        if balance > 1 and key > root.esq.item:
            root.esq = self.rotate_left(root.esq)
            return self.rotate_right(root)
        if balance < -1 and key < root.dir.item:
            root.dir = self.rotate_right(root.dir)
            return self.rotate_left(root)

        return root

    def get_altura(self, root):
        if not root:
            return 0
        return root.altura

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_altura(root.esq) - self.get_altura(root.dir)

    def rotate_left(self, z):
        y = z.dir
        T2 = y.esq
        y.esq = z
        z.dir = T2
        z.altura = 1 + max(self.get_altura(z.esq), self.get_altura(z.dir))
        y.altura = 1 + max(self.get_altura(y.esq), self.get_altura(y.dir))
        return y

    def rotate_right(self, z):
        y = z.esq
        T3 = y.dir
        y.dir = z
        z.esq = T3
        z.altura = 1 + max(self.get_altura(z.esq), self.get_altura(z.dir))
        y.altura = 1 + max(self.get_altura(y.esq), self.get_altura(y.dir))
        return y

    def buscar(self, chave, root):
        if not root or root.item == chave:
            return root
        if chave < root.item:
            return self.buscar(chave, root.esq)
        return self.buscar(chave, root.dir)

    def minn(self, root):
        if root is None or root.esq is None:
            return root
        return self.minn(root.esq)

    def maxx(self, root):
        if root is None or root.dir is None:
            return root
        return self.maxx(root.dir)

    def remover(self, root, key):
        if not root:
            return root
        elif key < root.item:
            root.esq = self.remover(root.esq, key)
        elif key > root.item:
            root.dir = self.remover(root.dir, key)
        else:
            if root.esq is None:
                return root.dir
            elif root.dir is None:
                return root.esq
            temp = self.minn(root.dir)
            root.item = temp.item
            root.dir = self.remover(root.dir, temp.item)
        if root is None:
            return root

        root.altura = 1 + max(self.get_altura(root.esq), self.get_altura(root.dir))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.esq) >= 0:
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.dir) <= 0:
            return self.rotate_left(root)
        if balance > 1 and self.get_balance(root.esq) < 0:
            root.esq = self.rotate_left(root.esq)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.dir) > 0:
            root.dir = self.rotate_right(root.dir)
            return self.rotate_left(root)

        return root

    def inOrder(self, root):
        if root:
            self.inOrder(root.esq)
            print(root.item, end=" ")
            self.inOrder(root.dir)

    def preOrder(self, root):
        if root:
            print(root.item, end=" ")
            self.preOrder(root.esq)
            self.preOrder(root.dir)

    def posOrder(self, root):
        if root:
            self.posOrder(root.esq)
            self.posOrder(root.dir)
            print(root.item, end=" ")

    def imprimir_indentado(self, root, nivel=0):
        if root is not None:
            self.imprimir_indentado(root.dir, nivel + 1)
            print(' ' * 4 * nivel + '.', root.item)
            self.imprimir_indentado(root.esq, nivel + 1)

def inserir():
    valor = int(entry_valor.get())
    arv.root = arv.inserir(arv.root, valor)
    messagebox.showinfo("Inserir", f"Valor {valor} inserido na árvore.")

def excluir():
    valor = int(entry_valor.get())
    arv.root = arv.remover(arv.root, valor)
    messagebox.showinfo("Excluir", f"Valor {valor} removido da árvore.")

def pesquisar():
    valor = int(entry_valor.get())
    if arv.buscar(valor, arv.root):
        messagebox.showinfo("Pesquisar", f"Valor {valor} encontrado na árvore.")
    else:
        messagebox.showwarning("Pesquisar", f"Valor {valor} não encontrado na árvore.")

def exibir():
    print("\nCaminhando na árvore:")
    arv.inOrder(arv.root)

def exibir_indentado():
    print("\nÁrvore com indentação:")
    arv.imprimir_indentado(arv.root)

arv = AVLTree()

root = Tk()
root.title("Árvore AVL")

frame = Frame(root)
frame.pack(pady=20)

label_valor = Label(frame, text="Valor:")
label_valor.grid(row=0, column=0, padx=10, pady=10)
entry_valor = Entry(frame)
entry_valor.grid(row=0, column=1, padx=10, pady=10)

btn_inserir = Button(frame, text="Inserir", command=inserir)
btn_inserir.grid(row=1, column=0, padx=10, pady=10)
btn_excluir = Button(frame, text="Excluir", command=excluir)
btn_excluir.grid(row=1, column=1, padx=10, pady=10)
btn_pesquisar = Button(frame, text="Pesquisar", command=pesquisar)
btn_pesquisar.grid(row=2, column=0, padx=10, pady=10)
btn_exibir = Button(frame, text="Exibir", command=exibir)
btn_exibir.grid(row=2, column=1, padx=10, pady=10)
btn_exibir_indentado = Button(frame, text="Exibir Indentado", command=exibir_indentado)
btn_exibir_indentado.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
