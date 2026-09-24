import operator

print("""
==========================================
            CONSOLE CALCULATOR
==========================================
      """)

def calculator(valor_1,operador,valor_2):
    
    operators = {
        'division': '/',
        'multiplicacion': '*',
        'potencia': '**',
        'floor': '//',
        'module': '%',
        'resta': '-',
        'suma': '+'
    }
    
    # VALIDACION DEL OPERADOR
    if operador not in operators.values():
        return print('Operador inválido')
    
    # OPERACIONES
    if operador == operators['resta']:
        operation = operator.sub(valor_1,valor_2)
        print(operation)
    if operador == operators['suma']:
        operation = operator.add(valor_1,valor_2)
        print(operation)
    if operador == operators['division']:
        operation = operator.truediv(valor_1,valor_2)
        print(operation)
    if operador == operators['multiplicacion']:
        operation = operator.mul(valor_1,valor_2)
        print(operation)
    if operador == operators['potencia']:
        operation = operator.pow(valor_1,valor_2)
        print(operation)
    if operador == operators['floor']:
        operation = operator.floordiv(valor_1,valor_2)
        print(operation)
    if operador == operators['module']:
        operation = operator.mod(valor_1,valor_2)
        print(operation)
    return 

try:
    valor_1 = float(input('Ingrese un valor: '))
    operador = input('Ingrese el operador (/,*,-,+,**,//,%): ')
    valor_2 = float(input('Ingrese un valor: '))
    results = calculator(valor_1, operador,valor_2)
except ValueError:  
    print('El valor debe ser un número')

