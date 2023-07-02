import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk
import list_logic as ll
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk


LARGEFONT = ("Verdana", 25)

this_array = []
weight, height, tree, edges, leaf_nodos, \
    inorder_array, postorder_array, \
    preorder_array, int_array = (None, None, None, None, None, None, None, None, None)
def convert_to_int(entry_object, window):
    get_information = entry_object.get()
    this_list = get_information.split(',')
    prov_list = []

    try:
        for i in this_list:
            prov_list.append(i)
        global int_array, edges, tree, weight, height, leaf_nodos, inorder_array, postorder_array, preorder_array
        this_array = prov_list
        int_array = [int(x) for x in this_array]
        tree = ll.create_tree(int_array)

        inorder_array = ll.get_inorder(tree)
        postorder_array = ll.get_postorder(tree)
        preorder_array = ll.get_preorder(tree)

        weight = ll.get_weight(tree)
        height = ll.get_height(tree)
        leaf_nodos = ll.get_hojas(tree)

        edges = ll.create_tuple_list(tree)
    except ValueError:
        print('Error')


    window.destroy()


class IngresarValores:

    def __init__(self):
        self.root = tk.Tk()
        entry_ingress = tk.Entry(self.root)
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (self.width, self.height))
        label_indications = tk.Label(self.root, text="Ingrese los numeros separados por comas, sin espacios", font=LARGEFONT)
        label_indications.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        button_enviar = tk.Button(self.root, text="Enviar", command=lambda: convert_to_int(entry_ingress, self.root))
        entry_ingress.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        button_enviar.place(relx=0.5,rely=0.8,anchor=tk.CENTER)
        self.root.mainloop()

IngresarValores()

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.estructura_arbol = None
        self.insertar_nodo = None
        self.eliminar_nodo = None
        self.nodos_interiores = None
        self.indicar_peso = None
        self.mostrar_orden = None
        self.indicar_altura = None
        self.indicar_hojas = None
        self.buscar_nodo = None
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}


        for F in (Menu, EstructuraArbol, IndicarPeso, MostrarOrden,
                  IndicarAltura, IndicarHojas, InsertarNodo, EliminarNodo, BuscarNodo, ImprimirNodosInteriores):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu)

    def show_frame(self, cont):
        frame = self.frames[cont]


        if cont == EstructuraArbol:
            if self.estructura_arbol is not None:
                self.estructura_arbol.draw_graph(arr=int_array,edg=edges)
            else:
                self.estructura_arbol = frame

        if cont == InsertarNodo:
            if self.insertar_nodo is not None:
                self.insertar_nodo.draw_graph(arr=int_array, edg=edges)
            else:
                self.insertar_nodo = frame
        if cont == EliminarNodo:
            if self.eliminar_nodo is not None:
                self.eliminar_nodo.draw_graph(arr=int_array, edg=edges)
            else:
                self.eliminar_nodo = frame
        if cont == ImprimirNodosInteriores:
            if self.nodos_interiores is not None:
                self.nodos_interiores.main_label.destroy()
                self.nodos_interiores.imprimir_nodos(tree)
            else:

                self.nodos_interiores = frame
        if cont == IndicarPeso:
            if self.indicar_peso is not None:
                self.indicar_peso.main_label.destroy()
                self.indicar_peso.indicar_peso()
            else:
                self.indicar_peso = frame
        if cont == IndicarAltura:
            if self.indicar_altura is not None:
                self.indicar_altura.main_label.destroy()
                self.indicar_altura.indicar_altura()
            else:
                self.indicar_altura = frame
        if cont == IndicarHojas:
            if self.indicar_hojas is not None:
                self.indicar_hojas.main_label.destroy()
                self.indicar_hojas.indicar_hojas()
            else:
                self.indicar_hojas = frame
        if cont == MostrarOrden:
            if self.mostrar_orden is not None:
                self.mostrar_orden.label_inorder.destroy()
                self.mostrar_orden.label_postorder.destroy()
                self.mostrar_orden.label_preorder.destroy()
                self.mostrar_orden.mostrar_ordenes()
            else:
                self.mostrar_orden = frame
        if cont == BuscarNodo:
            if self.buscar_nodo is not None:
                self.buscar_nodo.label_found.destroy()

        frame.tkraise()





class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Menu", font=LARGEFONT)
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        button1 = ttk.Button(self, text="Estructura Arbol",
                             command=lambda: controller.show_frame(EstructuraArbol))

        button2 = ttk.Button(self, text="Indicar Peso",
                             command= lambda : controller.show_frame(IndicarPeso))

        button3 = ttk.Button(self, text="Mostrar Orden",
                             command= lambda : controller.show_frame(MostrarOrden))
        button4 = ttk.Button(self, text="Indicar Altura",
                             command=lambda: controller.show_frame(IndicarAltura))

        button5 = ttk.Button(self, text="Indicar Hojas",
                             command= lambda : controller.show_frame(IndicarHojas))
        button6 = ttk.Button(self, text="Insertar",
                             command= lambda : controller.show_frame(InsertarNodo))

        button7 = ttk.Button(self, text="Eliminar", command=lambda : controller.show_frame(EliminarNodo))

        button8 = ttk.Button(self, text="Buscar Nodo", command=lambda: controller.show_frame(BuscarNodo))

        button9 = ttk.Button(self, text="Imprimir Nodos Interiores", command=lambda: controller.show_frame(ImprimirNodosInteriores))

        button1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        button2.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
        button3.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        button4.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
        button5.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        button6.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        button7.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        button8.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        button9.place(relx=0.5, rely=0.6, anchor=tk.CENTER)



class EstructuraArbol(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Estructura Arbol", font=LARGEFONT)

        self.draw_graph(arr=int_array, edg=edges)
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


        button1 = ttk.Button(self, text="Menu",
                             command=lambda: controller.show_frame(Menu))
        button1.place(rely=0.5, anchor=tk.W)

    def draw_graph(self, arr, edg):

        figure = plt.figure()
        graph = nx.DiGraph()
        graph.add_edges_from(edg)

        pos = ll.hierarchy_pos(graph, arr[0])
        nx.draw(graph, pos=pos, with_labels=True)

        canvas = FigureCanvasTkAgg(figure=figure, master=self)
        canvas.draw()

        canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class IndicarPeso(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        label = ttk.Label(self, text="PESO DEL ARBOL: ", font=LARGEFONT)
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        self.main_label = ttk.Label(self, text="", font=("Verdana", 15))
        self.indicar_peso()

        button1 = ttk.Button(self, text="Menu",
                             command=lambda: controller.show_frame(Menu))
        button1.place(rely=0.5, anchor=tk.W)

    def indicar_peso(self):
        global weight
        weight = ll.get_weight(tree)
        self.main_label = ttk.Label(self, text=f"{weight}", font=("sans-serif", 50))
        self.main_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

class IndicarAltura(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Indicar Altura", font=LARGEFONT)
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        self.main_label = ttk.Label(self, text="", font=("Verdana", 15))

        self.indicar_altura()


        button1 = ttk.Button(self, text="Menu",
                             command=lambda: controller.show_frame(Menu))
        button1.place(rely=0.5, anchor=tk.W)

    def indicar_altura(self):
        global height
        height = ll.get_height(tree)
        self.main_label = ttk.Label(self, text=f"{height}", font=("Verdana", 15))
        self.main_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

class IndicarHojas(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global int_array, edges, tree, weight, height, leaf_nodos, inorder_array, postorder_array, preorder_array
        label = ttk.Label(self, text="Indicar Nodos Hojas", font=LARGEFONT)
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.main_label = ttk.Label(self, text="", font=("Verdana", 12))
        self.indicar_hojas()
        button1 = ttk.Button(self, text="Menu",
                             command=lambda: controller.show_frame(Menu))
        button1.place(rely=0.5, anchor=tk.W)

    def indicar_hojas(self):
        global leaf_nodos
        leaf_nodos = ll.get_hojas(tree)
        self.main_label= ttk.Label(self, text=f"{leaf_nodos}", font=LARGEFONT)
        self.main_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

class MostrarOrden(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Mostrar Ordenes", font=LARGEFONT)
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.label_inorder = ttk.Label(self, text="", font=("Verdana", 12))
        self.label_postorder = ttk.Label(self, text="", font=("Verdana", 12))
        self.label_preorder = ttk.Label(self, text="", font=("Verdana", 12))
        self.mostrar_ordenes()
        button1 = ttk.Button(self, text="Menu",
                             command=lambda: controller.show_frame(Menu))
        button1.place(rely=0.5, anchor=tk.W)

    def mostrar_ordenes(self):
        in_o = ll.get_inorder(tree)
        post_o = ll.get_postorder(tree)
        pre_o = ll.get_preorder(tree)
        self.label_inorder = ttk.Label(self, text=f"Inorden: {in_o}", font=("Verdana", 12))
        self.label_postorder = ttk.Label(self, text=f"Postorden: {post_o}", font=("Verdana", 12))
        self.label_preorder = ttk.Label(self, text=f"Preorden: {pre_o}", font=("Verdana", 12))

        self.label_inorder.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.label_postorder.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.label_preorder.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

class InsertarNodo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global int_array, edges, tree, weight, height, leaf_nodos, inorder_array, postorder_array, preorder_array
        label = ttk.Label(self, text="Insertar Nodo", font=("Verdana", 12))
        label.place(relx=0.2, rely=0.1, anchor=tk.W)
        self.draw_graph(arr=int_array, edg=edges)

        label_insertar = ttk.Label(self, text="Indique el nodo a insertar", font=("Verdana", 12))
        label_insertar.place(relx=0.2, rely=0.2, anchor=tk.W)
        entry_insert = ttk.Entry(self)
        entry_insert.place(relx=0.2, rely=0.3, anchor=tk.W)

        button_get = ttk.Button(self, text="Enviar", command=lambda : self.comando_insertar(entry_object=entry_insert))
        button_get.place(relx=0.2,rely=0.4)

        button1 = ttk.Button(self, text="Menu",
                             command=lambda: controller.show_frame(Menu))
        button1.place(rely=0.5, anchor=tk.W)

    def draw_graph(self,arr,edg):


        figure = plt.figure()
        graph = nx.DiGraph()
        graph.add_edges_from(edg)

        pos = ll.hierarchy_pos(graph, arr[0])
        nx.draw(graph, pos=pos, with_labels=True)

        canvas = FigureCanvasTkAgg(figure=figure, master=self)
        canvas.draw()

        canvas.get_tk_widget().place(relx=0.6, rely=0.4, anchor=tk.CENTER)


    def retornar_valor(self, value):
        get_nodo_ultimo = ll.buscar_nodo(tree, valor=value)
        return get_nodo_ultimo.value

    def get_padre(self, valor):
        obtener_padre = ll.buscar_nodo_padre(tree, valor=valor)
        return obtener_padre.value

    def comando_insertar(self, entry_object):
        value = int(entry_object.get())
        global tree, edges, int_array
        tree.insert(value)
        int_array.append(value)
        edges = ll.create_tuple_list(tree)
        #valor = self.retornar_valor(value)
        #padre = self.get_padre(valor)
        #tupla_meter = (padre, valor)
        self.draw_graph(int_array,edges)


class EliminarNodo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global int_array, edges, tree, weight, height, leaf_nodos, inorder_array, postorder_array, preorder_array
        self.draw_graph(int_array,edges)
        label = ttk.Label(self, text="Eliminar Nodo", font=("Verdana", 12))

        label.place(relx=0.2, rely=0.1, anchor=tk.W)


        label_eliminar = ttk.Label(self, text="Indique el nodo a eliminar", font=("Verdana", 12))
        label_eliminar.place(relx=0.2, rely=0.2, anchor=tk.W)
        entry_insert = ttk.Entry(self)
        entry_insert.place(relx=0.2, rely=0.3, anchor=tk.W)

        button_get = ttk.Button(self, text="Eliminar", command=lambda : self.comando_eliminar(entry_object=entry_insert))
        button_get.place(relx=0.2,rely=0.4)

        button1 = ttk.Button(self, text="Menu",
                             command=lambda: controller.show_frame(Menu))
        button1.place(rely=0.5, anchor=tk.W)

    def draw_graph(self, arr, edg):


        figure = plt.figure()
        graph = nx.DiGraph()
        graph.add_edges_from(edg)

        pos = ll.hierarchy_pos(graph, arr[0])
        nx.draw(graph, pos=pos, with_labels=True)

        canvas = FigureCanvasTkAgg(figure=figure, master=self)
        canvas.draw()

        canvas.get_tk_widget().place(relx=0.6, rely=0.4, anchor=tk.CENTER)

    def comando_eliminar(self, entry_object):
        value_eliminate = int(entry_object.get())

        global int_array, tree, edges

        tree.delete(value_eliminate)

        if value_eliminate in int_array:
            if value_eliminate == int_array[0]:
                int_array.remove(value_eliminate)
                tree = ll.create_tree(int_array)
            else:
                int_array.remove(value_eliminate)


        edges = ll.create_tuple_list(tree)
        self.draw_graph(int_array,edges)


class BuscarNodo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global int_array, edges, tree, weight, height, leaf_nodos, inorder_array, postorder_array, preorder_array
        label = ttk.Label(self, text="Buscar Nodo", font=("Verdana", 15))
        label.place(relx=0.3, rely=0.1, anchor=tk.CENTER)

        self.label_found = ttk.Label(self, text=f"", font=("Verdana", 12))

        label_two = ttk.Label(self, text="Ingrese el nodo a buscar", font=("Verdana", 15))
        label_two.place(relx=0.3, rely=0.2, anchor=tk.CENTER)
        entry_ingress = ttk.Entry(self)
        entry_ingress.place(relx=0.3, rely=0.3, anchor=tk.CENTER)

        button_getinfo = ttk.Button(self, text="Buscar valor", command=lambda: self.buscar(entry_ingress))

        button_getinfo.place(relx=0.3, rely=0.4, anchor=tk.CENTER)
        button1 = ttk.Button(self, text="Menu",
                             command=lambda: controller.show_frame(Menu))
        button1.place(rely=0.5, anchor=tk.W)

    def buscar(self, entry_object):
        value = int(entry_object.get())
        global tree
        encontrar = ll.buscar_nodo(tree, value)

        self.encontrado(encontrar)
    def encontrado(self, found):
        if found:
            self.label_found = ttk.Label(self, text=f"El nodo ha sido encontrado y es {found.value}", font=("Verdana", 15))
            self.label_found.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        else:

            self.label_found = ttk.Label(self, text=f"No ha sido encontrado", font=("Verdana", 15))
            self.label_found.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



class ImprimirNodosInteriores(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.main_label = ttk.Label(self, text="", font=("Verdana", 15))
        self.imprimir_nodos(tree)

        label = ttk.Label(self, text="Imprimir Nodos Interiores", font=LARGEFONT)
        label.place(relx=0.3, rely=0.2, anchor=tk.CENTER)


        button1 = ttk.Button(self, text="Menu",
                             command=lambda: controller.show_frame(Menu))
        button1.place(rely=0.5, anchor=tk.W)
    def imprimir_nodos(self, tree):
        interior_nodes = ll.get_interior_nodes(tree)
        del interior_nodes[0]
        self.main_label = ttk.Label(self, text=f"Nodos interiores: {interior_nodes}", font=("Verdana", 15))
        self.main_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

app = Application()

width = app.winfo_screenwidth()
height_w = app.winfo_screenheight()
app.geometry("%dx%d" % (width, height_w))
app.mainloop()