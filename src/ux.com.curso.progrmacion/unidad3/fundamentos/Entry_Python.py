
def pregunta_1():
    print(2 **3 ** 2)

def pregunta_2():
    x = 10/5
    print(type(x))
"""
 x=1 x==x print(x==x) True
"""   

def pregunta_3():
    x = 1 
    x == x 
    print(x == x)

"""
Orden de operacione sprimero evalua // y luego * 
entonces 1//2 se evalua primero y da 0, luego 0*3 da 0
"""
def pregunta_4():

    print(1//2*3)

def pregunta_5():
     y = 2+3 *5
     print(y)
    
def pregunta_6():
    b = '2'
    a = '1'
    print(a + b)
"""
Operador % devuelve el residuo de la division 
entre 11 y 3, que es 2
"""   
def pregunta_7():
    z = 11 % 3
    print(z)

def pregunta_8():
    X = 5
    Y = 2
    print(X // Y)

def pregunta_9():
    val = 10 
    val += 5*2
    print(val)
def pregunta_10():
    print(bool(""), bool(" "), bool(0), bool(0.0))

def main():
    pregunta_1()
    pregunta_2()
    pregunta_3()
    pregunta_4()
    pregunta_5()
    pregunta_6()
    pregunta_7()
    pregunta_8()
    pregunta_9()
    pregunta_10()

if __name__ == "__main__":
    main()

