import sys
sys.path.append(r'C:\Users\USUARIO\Desktop\SIA\aima-python')

from search import Problem, astar_search, breadth_first_graph_search

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
                if a != b:

                    # resta
                    acciones.append((a, '-', b)) 
                if a != 1 and b != 1:

                    # multiplicación
                    acciones.append((a, '*', b))  
                if b > 1 and a % b == 0:

                    #división
                    acciones.append((a, '/', b))

        return sorted(acciones) # lista de acciones generada

    '''
    Precondiciones: el estado tiene que estar bien formado, lista de 6 números y un objetivo
                    tiene que ser una opción válida para el estado
                    la resta no puede dar resultado negativo
    '''

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


    # -> Definir el mejor algoritmo de búsqueda

    # Para que el árbol sea finito hay que asegurarse de que no se repitan estados

    # importar mi objeto y llamar al árbol
    # breadth_first_search