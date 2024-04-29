#las librerías
from matplotlib.figure import Figure
import networkx as nx #Para trabajar con los grafos
import tkinter as tk #Crea la interfaz gráfica
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #Es la libería para graficar todo 

#Crea una gráfica que almacenará los nodos y las vertices
G = nx.Graph()
root = tk.Tk()#crea la la ventana y le pone el título
root.configure(bg="white")
root.title("ALGORTIMOS DE BÚSQUEDA")


# Función para agregar un vértice
def add_vertex():
    G.add_node(vertex_entry.get())
    draw_graph()#la dibuja

# Función para agregar una arista
def add_edge():
    G.add_edge(edge_entry_1.get(), edge_entry_2.get())
    draw_graph()#la dibuja


# Función para dibujar el gráfico
def draw_graph(bfs_edges=None, dfs_edges=None):
    ax.clear()
    pos = nx.spring_layout(G)
    nx.draw(G, pos=pos, ax=ax, with_labels=True)
    if bfs_edges:
        nx.draw_networkx_edges(G, pos=pos, edgelist=bfs_edges, edge_color='r', ax=ax)
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[vertex_entry.get()]+[v for u, v in bfs_edges], node_color='r', ax=ax)
    if dfs_edges:
        nx.draw_networkx_edges(G, pos=pos, edgelist=dfs_edges, edge_color='b', ax=ax)
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[vertex_entry.get()]+[v for u, v in dfs_edges], node_color='b', ax=ax)
    canvas.draw()

# Función para realizar la búsqueda en anchura
def show_bfs():
    bfs_edges = list(nx.bfs_edges(G, source=vertex_entry.get()))
    draw_graph(bfs_edges=bfs_edges)
    Label3.config(text="SE REALIZÓ UNA BÚSQUEDA EN ANCHURA")
    Label3.config(bg="white", font=("Helvetica",16), fg="red")


# Función para realizar la búsqueda en profundidad
def show_dfs():
    dfs_edges = list(nx.dfs_edges(G, source=vertex_entry.get()))
    draw_graph(dfs_edges=dfs_edges)
    Label3.config(text="SE REALIZÓ UNA BÚSQUEDA EN PROFUNDIDAD")
    Label3.config(bg="white", font=("Helvetica",16), fg="blue")

# Creación de la interfaz gráfica

Label1=tk.Label(root,text="Ingrese el nodo a crear")
Label1.pack()
Label1.config(bg="white", font=("Helvetica",14))

vertex_entry = tk.Entry(root)
vertex_entry.pack()
add_vertex_button = tk.Button(root, text="Agregar vértice", command=add_vertex)
add_vertex_button.pack()
add_vertex_button.config(background="white")

Label2=tk.Label(root, text="Ingrese los nodos a conectar")
Label2.pack()
Label2.config(bg="white", font=("Helvetica",14))

frame2=tk.Frame(root, background="white")
frame2.pack()

edge_entry_1 = tk.Entry(frame2)
edge_entry_1.pack(side="left")
edge_entry_2 = tk.Entry(frame2)
edge_entry_2.pack(side="left")
add_edge_button = tk.Button(root, text="Agregar arista", command=add_edge)
add_edge_button.pack()
add_edge_button.config(background="white")

figure = Figure(figsize=(7, 4))
ax = figure.add_subplot(111)
canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().pack()

frame=tk.Frame(root)
frame.pack()
frame.config(background="white")

bfs_button = tk.Button(frame, text="Búsqueda en anchura", command=show_bfs)
bfs_button.pack(side="left")
bfs_button.config(background="white", highlightbackground="red")

dfs_button = tk.Button(frame, text="Búsqueda en profundidad", command=show_dfs)
dfs_button.pack(side="left")
dfs_button.config(background="white", highlightbackground="blue")

Label3= tk.Label(root, text="")
Label3.pack()
Label3.config(background="white")

root.mainloop()
