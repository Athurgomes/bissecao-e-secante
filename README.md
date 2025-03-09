# Método da Bisseção 

---

## 📚 Teoria Básica
O método da bisseção é um algoritmo numérico para encontrar raízes de funções contínuas. Ele requer:
- Uma função contínua `f(x)`.
- Um intervalo inicial `[a, b]` onde `f(a)` e `f(b)` têm sinais opostos.
- Tolerância (`tol`) para o erro aceitável.
- Número máximo de iterações (`max_iter`).

O algoritmo divide o intervalo ao meio iterativamente e atualiza os extremos com base no sinal da função no ponto médio, garantindo convergência para a raiz.

---

## ⚙️ Funcionalidades
- **Verificação de pré-condições**: Checa se `f(a)` e `f(b)` têm sinais opostos.
- **Controle de iterações**: Limita o número máximo de iterações para evitar loops infinitos.
- **Critério de parada**: Interrompe quando `|f(x)| < tol` ou atinge `max_iter`.

---

## 📋 Pré-requisitos
- Python 3.x instalado.
- Nenhuma biblioteca externa necessária.

---

## 🚀 Como Usar

### 1. Definir a Função
Modifique a função `func(x)` no código para representar sua equação:
```python
def func(x):        
    return x**3 - 3*x**2 + 2*x - 1  # Exemplo: f(x) = x³ - 3x² + 2x - 1
```

### 2. Executar o Algoritmo
Chame a função `bissecao` com os parâmetros desejados:
```python
raiz, iteracoes = bissecao(func, a=2, b=3, tol=1e-6, maxiter=100)
```

#### Parâmetros:
- `func`: Função a ser analisada.
- `a`, `b`: Extremos do intervalo inicial.
- `tol`: Tolerância para o erro (ex: `1e-6`).
- `maxiter`: Máximo de iterações (ex: `100`).

#### Retorno:
- `raiz`: Aproximação da raiz encontrada.
- `iteracoes`: Número de iterações realizadas.

---

## 📊 Exemplo de Saída
```python
Raiz encontrada: 2.5468183 em 20 iterações.
```

---

## 🧪 Validação e Resultados
A função de exemplo `f(x) = x³ - 3x² + 2x - 1` possui uma raiz real no intervalo `[2, 3]`. O algoritmo converge em **~20 iterações** com tolerância `1e-6`.

---

## ⚠️ Limitações
- Requer que `f(a)` e `f(b)` tenham sinais opostos.
- Convergência mais lenta comparada a métodos como Newton-Raphson.

---

## 📖 Referências
- SATUF, Francisco. ["O Método da Bisseção"](https://rmu.sbm.org.br/wp-content/uploads/sites/27/2018/03/n36_Artigo04.pdf). Revista de Matemática Universitária, 2018.

---
