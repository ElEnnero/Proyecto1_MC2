# Manual de Usuario
Este programa permite al usuario interactuar con grafos realizando búsquedas con profundidad y anchura, presentando de manera gráfica, descriptiva e intuitiva las posiciones en las cuales se deben ingresar los datos y mostrando sobre el grafo la búsqueda realizada.

#### Objetivo General
1. Permitir al usuario comprender de mejor manera el funcionamiento del programa que implementa los métodos de búsqueda por profundidad y anchura.

#### Objetivos Especificos
1. Mostrar paso a paso el funcionamiento del programa creado a partir de Python.
2. Permitir una mejor comprensión de los métodos de búsqueda por medio de la gráfica.
3. Demostrar cómo se pueden implementar los métodos de búsqueda dentro de los lenguajes de programación.

### Flujo de las funcionalidades del programa
1. ![](/images/u1.png)
   Se abre el ejecutable que se encuentra dentro de la carpeta *dist* en el archivo descargado en [github](https://github.com/ElEnnero/Proyecto1_MC2.git) 
2. ![](/images/u2.png)
    Se mostrará la siguiente ventana, la cual presentará las siguiente opciones:
    - Agregar vértices
    - Agregar arístias
    - Búsqueda en anchura
    - Búsqueda en profundidad
3. ![](/images/u3.png)
    Dentro de la primera entrada (la que se encuentra arriba del primer botón), se podrá ingresar una **letra** que identifique el nodo a ingresar
4. ![](/images/u4.png)
   Se ingresan todo los nodos que se deseen para grafo respetando siempre el tipo de **letra**, siendo en este caso **minúsculas**, por lo que deben ser minúsculas para evitar problemas dentro del programa. Adicionalmente, se podrá percatar de que cada vez que se genera un nuevo nodo, todas las posiciones se actualizan; esto sucede debido a la naturaleza de los grafos, los cuales son simples representaciones de camino o redes, los cuales no tienen posiciciones fijas.
5. ![](/images/u5.png)
    Una vez que se ingresan todos los nodos deseados, se cran las conexiones entre estos. La conexiones se realizan mediante los otras dos entradas en las que se podrán ingresar las **etiquetas** de dos nodos para que se cree una arista entre estos que los conecte.
6. ![](/images/u6.png)
    Se ingresan todas las conexiones que se desee que tenga el grafo. Como curiosidad, es posible generar un lazo colocando el mismo nodo en ambas entradas.
7. ![](/images/u7.png)
   Una vez con el grafo deseado generado, se ingresa en la entrada que se usó para ingresar los nodos para escoger el nodo de inicio y se preciona el tipo de búsqueda que se desea realizar, que en este caso será la búsqueda en anchura
8. ![](/images/u8.png)
    Se pudo observar que se marcan en la gráfica las vértices que se usan para realizar la búsqueda en anchura y, en la parte inferior, se indica que se realizó este proceso. Ahora si se desea cambiar de tipo de búsqueda simplemente se presiona el otro botón, en este caso el de búsqueda en profundidad.
9. ![](/images/u9.png)
    Una vez realizado esto, es posible seguir utilizando el programa agregando más vertices y aristas y cambiando entre los tipos de búsqueda que se desee.
10. ![](/images/u2.png)
    Finalmente, si se deseea borrar todo, basta con cerrar y volver a abrir el programa, el cual se iniciará con todos los datos en 0.

Para más información acerca de la teoría de grafos y el funcionamiento del programa y su código, se puede visualizar el siguiente [video de youtuve](https://youtu.be/nkzDdbQEhLQ?si=Q_IHvOQjbO2OCVUC)