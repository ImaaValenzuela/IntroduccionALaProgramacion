# Python

Empezaremos viendo lo basico de Python. Para crear un archivo python en VSC tenemos la abreviacion ".py"

- Primer Hola Mundo
Para imprimir nuestra primer cadena de caracteres, usaremos print("").

- Como funciona una variable?
Las variables se forman a traves del espacio que hay en el sistema. Una variable se puede interpretar como una caja que guarda datos, puede guardar numeros, cadenas de caracteres, etc. Este valor debe de ser de un solo tipo. Podemos modificarlas cuando queramos. No obstante tambien existen las variables que no cambian, llamadas constantes, siguiendo el ejemplo de la caja, una vez almavenamos este dato, la caja se cierra, en palabras tecnicas, no se podra modificar durante la ejecucion del programa.

- Imprimir datos
Para declarar una variable tenemos que darle un nombre a la misma, agregar el simbolo igual "=" y poner el valor deseado.
El "+" nos permite unir dos variables o mas, se lo llama concatenacion.

- Lectura de datos
Vamos a tomar datos que ingrese el usuario. Normalmente el usuario es el que se encarga de hacer que el programa funcione. 
Input () se encarga de leer y estos datos.

- Operadores Aritmeticos
Los operadores aritmeticos se usan para calcular el valor de dos o mas numeros. Estos son parte esencial de la programacion.
Para leer datos de operadores aritmeticos hay que agregar "int", esto da a entender al programa que son numeros enteros.

- Operadores de Comparacion
Los operadores de comparacion vienen siempre acompañados de los operadores de condicion, mejor conocidos como sentencias. Estos son if...else, = (asignacion), ==(igual), > (mayor que), >= (mayor o igual que), <(menor que), < (menor o igual que).

- Casting
Es muy importante saber con que tipo de dato trabajamos(strings, booleans, num). Al momento que nosotros le pedimos al usuario que ingrese un valor por medio de input, estamos esperando a que el usuario lo ingrese desde el teclado, a esto lo reconoce como una cadena de caracteres, entonces si usaremos un numero para nuestro programa, debemos convertir nuestros strings en numeros. A esta conversion se la conoce como casteo o casting.
int() convierte a enteros, str() convierte a cadena de texto, float() recibe decimales.

- Arreglos
Los arreglos estan formados por una coleccion de datos, sean numeros o cadenas de caracteres, pero solo de un tipo. 
Para declarar un arreglo usaremos "[]". Cada valor sera distinguido por una ",".
La ubicacion de los arreglos empiezan desde el 0.

- Como trabaja una funcion?
Las funciones estan definidas por un conjunto de lineas de codigo, las cuales realizan una accion especifica. Las funciones nos permiten descomponer los problemas que tengamos en tareas pequeñas, las cuales podemos ir resolviendo una a una.


- Declaracion de funciones
Para declarar una funcion usaremos "def". 
Siempre hay que mandar a llamar a una funcion para que se ejecute.

- Argumento de funciones
Return es una palabra reservada para retornar valores.
".format" da formato a nuestra salida.

- Como trabaja un ciclo?
Los ciclos estan pensados para realizar una o varias acciones cierto numero de veces mientras una condicion se cumple. Existen diferentes formas de realizar un ciclo.

- Ciclo While
El ciclo while permite repetir un bloque de codigo mientras se cumpla una condicion, o que la instruccion siempre sea verdadera. 
La palabra reservada para definir es "while".
Si una condicion siempre se cumple se entra en un bucle infinito llamado "ciclado".

- Ciclo For
El ciclo for nos permite repetir un bloque de instrucciones un determinado numero de veces. 