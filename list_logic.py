import networkx as nx
import random

class TreeNode():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def delete(self, value):
        if value < self.value:
            if self.left is not None:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right is not None:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                successor = self.right.find_min()
                self.value = successor.value
                self.right = self.right.delete(successor.value)
        return self

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current



def get_weight(root):
    if root is None:
        return 0
    else:
        left_weight = get_weight(root.left)
        right_weight = get_weight(root.right)
        return 1 + left_weight + right_weight



def create_tree(list):

    tree = TreeNode(list[0])

    length = int(len(list))

    for i in range(1, length):
        tree.insert(list[i])
    return tree

def get_inorder(root):

    inorder_l = []
    def inorder(tree):
        if tree is not None:

            inorder(tree.left)
            inorder_l.append(tree.value)
            inorder(tree.right)

    inorder(root)
    return inorder_l

def buscar_nodo(raiz, valor):
    if raiz is None or raiz.value == valor:
        return raiz

    if valor < raiz.value:
        return buscar_nodo(raiz.left, valor)
    else:
        return buscar_nodo(raiz.right, valor)

def buscar_nodo_padre(raiz, valor):
    if raiz is None or raiz.value == valor:
        return None

    if (raiz.left is not None and raiz.left.value == valor) or (raiz.right is not None and raiz.right.value == valor):
        return raiz

    if valor < raiz.value:
        return buscar_nodo_padre(raiz.left, valor)
    else:
        return buscar_nodo_padre(raiz.right, valor)



def get_preorder(root):
    preorder_l = []

    def preorder(tree):

        if tree is not None:
            preorder_l.append(tree.value)
            preorder(tree.left)
            preorder(tree.right)

    preorder(root)
    return preorder_l


def get_postorder(root):
    postorder_l = []

    def postorder(tree):
        if tree is not None:
            postorder(tree.left)
            postorder(tree.right)
            postorder_l.append(tree.value)

    postorder(root)
    return postorder_l


def get_height(root):
    if root is None:
        return 0

    left_height = get_height(root.left)
    right_height = get_height(root.right)
    return max(left_height, right_height) + 1


def get_hojas(root):
    leaf_nodes = []

    def traverse(node):
        if node is None:
            return
        if node.left is None and node.right is None:
            leaf_nodes.append(node.value)

        traverse(node.left)
        traverse(node.right)

    traverse(root)

    return leaf_nodes

def get_interior_nodes(root):
    interior_nodes = []

    def traverse(node):
        if node is None:
            return
        if node.left is not None or node.right is not None:
            interior_nodes.append(node.value)

        traverse(node.left)
        traverse(node.right)

    traverse(root)

    return interior_nodes


def create_tuple_list(root):

    tuple_list = []

    def create_tuple(current_node):
        if current_node is None:
            return

        if current_node.left is not None and (current_node.value != current_node.left.value):
            tuple_left = (current_node.value, current_node.left.value)
            tuple_list.append(tuple_left)
            create_tuple(current_node.left)


        if current_node.right is not None and (current_node.value != current_node.right.value):
            tuple_right = (current_node.value, current_node.right.value)
            tuple_list.append(tuple_right)
            create_tuple(current_node.right)


    create_tuple(root)


    return tuple_list


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    '''

    Si el grafo es un arbol entonces esta función retornará las posiciones jerárquicas como diseño

    G: grafo (Debe de ser un arbol)

    root: el nodo raiz de la actual rama
    - si el arbol es directo y esto (la raiz) no es dada, entonces se encontrará la raíz de forma automática y esta misma será usada
    - si el arbol es directo y la raiz se da, entonces las posiciones se ajustarán como los descendientes directos de este nodo
    - si el arbol no es directo y la raiz no se da, entonces se escoge la raiz de forma aleatora

    width: espacio alocado para esta rama. Evita sobreposiciones

    vert_gap: Espacio entre los niveles de la jerarquía

    vert_loc: posición vertical de la raíz

    xcenter: Posición horizontal de la raíz
    '''
    if not nx.is_tree(G):
        raise TypeError('No se puede usar la función en un grafo que no sea arbol')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0.0, xcenter=0.5, pos=None, parent=None):
        '''
        (Ver la descripción de la función hierarchy_pos para la mayoría de los argumentos)

        pos: un diccionario que indica la ubicación de todos los nodos si se les ha asignado.

        parent: padre de esta rama. - solo afecta si es no dirigido.
        '''

        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc = (vert_loc - vert_gap), xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)