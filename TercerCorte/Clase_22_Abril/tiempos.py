# Programa para automatizart las ejecuciones de cython, python y c
# posteriormente lleverlo a un archivo csv

from timeit import repeat
from subprocess import check_output


def tiempos(arg, niter, nombre, modulo):
    stmt = "%s(%s)" % (nombre, arg)
    setup = "from %s import %s" % (modulo, nombre)
    tiempo = min(repeat(stmt=stmt, setup=setup, number=niter))/float(niter)*1e9
    return tiempo

# Ejecución para fib(0) con N repeticiones
N= 10
py_tiempo_0 = tiempos(0, N, nombre = 'fib', modulo = 'fib') 
cy_tiempo_0 = tiempos(0, N, nombre = 'fib', modulo = 'cyfib') 
ctiempo__0 = float(check_output(('./cfib.x 0 %d' % N).split()))

print("tiempo en Python {} \n". format(py_tiempo_0))
print("tiempo en Cython {} \n". format(py_tiempo_0))
print("tiempo en C {} \n". format(py_tiempo_0))
