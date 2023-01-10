# Damavis-Snake

La solución se compone de dos archivos:
- **snake.py**. Contiene el código que soluciona el problema planteado dentro de la clase SnakePathFinder.
- **test_snake.py**. Contiene los test que comprueban la validez del resultado.


Para solucionar el problema he utilizado una técnica similar al Breadth-First Search.
Básicamente he partido de la serpiente inicial y la he encolado en una lista de caminos posibles (possible_paths).
Mientras queden posibles caminos por comprobar obtengo el primero de ellos, obtengo el head del snake actual y obtengo las 4 posibles posiciones hacia las que se podría mover.

Despues compruebo si dichas posciones son validas, si es así creo un nuevo snake y lo encolo para seguir comprobando caminos. Si un snake no puede avanzar hacia ninguna posición no se encolará nada en la lista de caminos posibles.

Una vez que los caminos llegan a la profundidad adecuada los guardo en una lista de caminos acabados (finished ways).

Cuando se han terminado todos los posibles caminos a recorrer obtengo el número de caminos acabados obtenidos.


Para completar el problema he incluido un método que permite guardar los caminos acabados en un archivo y que facilita la tarea si hay que comprobar los resultados.


La solución que he planteado tiene una complejdad O(4<sup>n</sup>) en el espacio temporal ya que para cada posición tenemos que comprobar 4 posibles caminos. Esto genera que a partir de cierta profundidad de camino el rendimiento decaiga debido a la cantidad de opciones que se tienen que comprobar. 

No se me han ocurrido muchas opciones para conseguir hacer un pruning de caminos a comprobar. Quizás una opción sería buscar patrones de caminos que se repitan pero no estoy seguro de si funcionaría. De todas formas implementarlo me llevaría más de un par de días.

