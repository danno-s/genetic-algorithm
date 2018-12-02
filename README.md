## Tarea 2 - CC5114
# Algoritmo Genético

### Daniel Soto

La implementación básica del algoritmo genético implementada está centrada en la clase población, la que, para funcionar correctamente para algún problema dado, necesita recibir implementaciones de:

* Una clase de individuos, la que soporte una función reproduce.
* Una función (sin argumentos) que genere un nuevo individuo.
* Una función que defina el fitness utililzado en el problema.
* Una función que implemente el filtro aplicado a la población entre iteraciones (top 25%, random, torneo, etc)

## Ejecución

El código fuente está escrito en Python 3 sin librerías externas. En este repositorio están implementados dos problemas, el de adivinar bits y el de N-Reinas (El informe sólo analiza a las N-Reinas). Estos se encuentran implementados en ```bit_guesser.py``` y ```nqueen_guesser.py``` respectivamente. Para ejecutar el archivo ```[ARCHIVO]```, se debe correr en la terminal:

```
$ python3 [ARCHIVO] 
```

Este pedirá un input apropiado para el problema, y luego intentará resolverlo, retornando estadísticas básicas sobre la ejecución, y el resultado obtenido.
