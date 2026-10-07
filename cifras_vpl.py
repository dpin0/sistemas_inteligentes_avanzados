import sys
sys.path.append("/usr/lib/python3/dist-packages/aima-python")

from aima.search import Problem, astar_search, breadth_first_graph_search

class ProblemaCifras(Problem):
    ''' Clase que modelizar un algoritmo que solucione los problemas numéricos del programa Cifras Y Letras '''
    
    def __init__(self, estado_inicial, estado_objetivo):
        super().__init__(tuple(sorted(estado_inicial)), estado_objetivo)
        # almacenar en tuplas para que no sean eliminadas por error

    def actions(self, estado):
        acciones = []
        n = len(estado)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = estado[j], estado[i] # pareja de números -> elegir operación entre las 4 opciones

                # suma
                acciones.append((a, '+', b))
                if a >= b:

                    # resta
                    acciones.append((a, '-', b)) 
                if a != 1 and b != 1:

                    # multiplicación
                    acciones.append((a, '*', b))  
                if b > 1 and a % b == 0:

                    #división
                    acciones.append((a, '/', b))

        return sorted(acciones) # lista de acciones generada


    def result(self, estado, action):
        a, accion, b = action

        if accion == '+':
            sol = a + b
            
        elif accion == '-':
            sol = a - b

        elif accion == '*':
            sol = a * b

        else:
            sol = a // b

        nueva_lista = list(estado)

        nueva_lista.remove(a)
        nueva_lista.remove(b)
        nueva_lista.append(sol)

        return tuple(sorted(nueva_lista))


    def goal_test(self, estado):
        return self.goal in estado

def main():
    
    datos = []
    for i in sys.stdin.read().split():
        datos.append(int(i))
        
    estado_inicial = datos[:-1]
    objetivo = datos[-1]
    contador = 0
    
    problema = ProblemaCifras(estado_inicial, objetivo)
    nodo = breadth_first_graph_search(problema)
        
    if nodo:
        for a, op, b in nodo.solution():
            contador +=1
        print("Número mínimo de operaciones:", contador)
    else:
        print("Número mínimo de operaciones: 0")
    

if __name__ == "__main__":
     main()