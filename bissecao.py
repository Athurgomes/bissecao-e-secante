#bisseção consiste em uma função e três números a, b, tol. A função é uma função contínua, a e b são números reais que definem um intervalo [a,b] 
# e tol é a tolerância para o erro. O algoritmo deve retornar o valor de x tal que f(x) = 0 com erro menor que tol. O algoritmo deve parar após maxiter iterações.
#intervalo inicial a1=a, b1=b
#calculo do ponto médio xn=(an+bn)/2
#criterio para atualização de an e bn
#se f(an)*f(xn)<0, (está entre an e x) então bn+1=x
#se f(bn)*f(xn)<0, (está entre x e bn) então an+1=x
#Algoritmo feito baseado no artigo "O Método da Bisseção" de Francisco Satuf da UFMG
#link: https://rmu.sbm.org.br/wp-content/uploads/sites/27/2018/03/n36_Artigo04.pdf

def bissecao(func, a, b, tol, max_iter):
    if func(a)*func(b)>=0:
        print("f(a) e f(b) não apresentam sinais opostos")
        return None, None
    contador=0
    while contador<max_iter:
        x=(a+b)/2
        fXn=func(x)
        if abs(fXn)<tol:
            return x, contador
        if func(a)*fXn<0:
            b=x
        else:
            a=x
        contador+=1
    print("Número máximo de iterações atingido")
    return (a+b)/2, contador

def func(x):        
    return x**3-3*x**2+2*x-1

raiz, iteracoes=bissecao(func, 2, 3, 1e-6, 100)

if raiz is not None:
    print(f"A raiz é {raiz:.7f} e o número de iterações foi {iteracoes}")
