# e tol é a tolerância para o erro. O algoritmo deve retornar o valor de x tal que f(x) = 0 com erro menor que tol. O algoritmo deve parar após maxiter iterações.
#Algoritmo feito baseado no artigo "Método da Secante Para Resolução de equações do tipo f(x)=0" 
#link: https://www.aedb.br/seget/arquivos/artigos06/472_Artigo01%20Nara%20Vetter,%20Guilherme%20Paiva,%20Rafael%20Marques.pdf
def secante(func, x0, x1, tol, max_iter):
    contador=0
    while contador<max_iter:

        fX0=func(x0)
        fX1=func(x1)
        if abs(fX1-fX0)<1e-10:
            print("Erro: convergencia lenta")
            return None
        x2=x1-(fX1/(fX1-fX0))*(x1-x0)
        if abs(x2-x1)<tol:
            print(f"Convergência alcançada após {contador + 1} iterações.")
            return x2
        x0, x1= x1, x2
        contador+=1
    print("Número máximo de iterações atingido")
    return x2

def func(x):        
    return x**3-3*x**2+2*x-1

raiz, iteracoes=secante(func, 2, 3, 1e-6, 100)

if raiz is not None:
    print(f"A raiz é {raiz:.7f} e o número de iterações foi {iteracoes}")
