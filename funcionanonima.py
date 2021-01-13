from funcionprimernivel import sumatodos

triple = lambda x: x*3

print(sumatodos(3,lambda x: x*2))
print(sumatodos(100,triple))

#las funciones anonimas se usan cuando no se quieren volver a usar
