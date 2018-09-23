def busca_incremental(f,a,b,delta):
    
    if a > b :
        print("Por definição o a é o inf do intervalo, portanto menor do que o b")
        return []
    else:
        
        Fa = f(a)
        b_fake = a + delta
        Fbf = f(b_fake)

        lista_raiz = []

        interv = abs(b - a)

        while interv >= delta :
            if Fa*Fbf < 0:
                lista_raiz.append([a,b_fake])
                
            a = b_fake
            b_fake = a + delta
            Fa = f(a)
            Fbf = f(b_fake)

            interv = abs(b - a)

        return lista_raiz

def bissecao(f, a, b, epsilon, maxIter = 50):
    
    """Executa o método da bisseção para achar o zero de f no intervalo 
       [a,b] com precisão epsilon. O método executa no máximo maxIter
       iterações.
       Retorna uma tupla (houveErro, raiz), onde houveErro é booleano.
    """
    ## Inicializar as variáveis Fa e Fb
    Fa = f(a)
    Fb = f(b)
    
    ## Teste para saber se a função muda de sinal. Se não mudar, mostrar
    ## mensagem de erro
    if (Fa*Fb) > 0 :#and (diff(Fa)*diff(Fb) >0):
        ## Mostrar mensagem
        print("Erro! A função não muda de sinal.")
        return (True, None)
    
    ## Mostra na tela cabeçalho da tabela
    print("k\t  a\t\t  fa\t\t  b\t\t  fb\t\t  x\t\t  fx\t\tintervX")
    
    ## Inicializa tamanho do intervalo intervX usando a função abs, x e Fx
    intervX = abs( b - a)
    x = (a + b)/2
    Fx = f(x)
    
    ## Mostra dados de inicialização
    print("-\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (a, Fa, b, Fb, x, Fx, intervX))
    
    ## Teste se intervalo já é do tamanho da precisão e retorna a raiz sem erros
    # escreva o seu código aqui 
    if intervX < epsilon:
        return (False, x)
    
    
    ## Iniciliza o k
    k = 1
    
    ## laço
    while k <= maxIter:
        ## Testes para saber se a raiz está entre a e x ou entre x e b e atualiza
        ## as variáveis apropriadamente
        
        if Fa*Fx > 0 and Fx != 0:
            a = x
            Fa = f(a)
        else:
            b = x
            Fb = f(b)
        
        ## Atualiza intervX, x, e Fx
        intervX = abs( b - a)
        x = (a + b)/2
        Fx = f(x)
        
        
        ## Mostra valores na tela
        print("%d\t%e\t%e\t%e\t%e\t%e\t%e\t%e"%(k, a, Fa, b, Fb, x, Fx, intervX))
        
        ## Teste do critério de parada (usando apenas o tamanho do intervalo)
        if intervX < epsilon :
            return(False, x)
        
        ## Atualiza o k
        k = k+1
    ## Se chegar aqui é porque o número máximo de iterações foi atingido
    ## Mostrar uma mensagem de erro e retorna que houve erro e a última raiz encontrada
    print("ERRO! número máximo de iterações atingido.")
    return (True, x)


def false_pos(f, a, b, epsilon, maxIter = 50):
    
    """Executa o método da Posição Falsa para achar o zero de f no intervalo 
       [a,b] com precisão epsilon. O método executa no máximo maxIter
       iterações.
       Retorna uma tupla (houveErro, raiz), onde houveErro é booleano.
    """
    ## Inicializar as variáveis Fa e Fb
    Fa = f(a)
    Fb = f(b)
    
    ## Teste para saber se a função muda de sinal. Se não mudar, mostrar
    ## mensagem de erro
    if Fa*Fb > 0 :
        print("Erro! A função não muda de sinal.")
        return (True, None)
    
    ## Inicializa o tamanho do intervalo intervX usando a função abs
    intervX = abs(b - a)
    
    ## Teste se intervalo já é do tamanho da precisão e retorna a raiz sem erros
    if intervX < epsilon:
        x = (a*f(b) - b*f(a))/(f(b) - f(a))
        return (False,x)
    
    ## Testes se raiz está nos extremos dos intervalos
    
    ## Teste se a é raiz, se for, retorna o próprio a sem erros
    if Fa == 0:
        return (False,a)
    
    ## Teste se b é raiz, se for, retorna o próprio b sem erros
    if Fb == 0:
        return (False,b)
    
    ## Mostra na tela cabeçalho da tabela
    print("k\t  a\t\t  Fa\t\t  b\t\t  Fb\t\t  x\t\t  Fx\t\tintervX")
    
    ## Iniciliza o k, dessa vez usaremos um for
    for k in range(1, maxIter+1):
        ## Calcula x, Fx
        x = (a*f(b) - b*f(a))/(f(b) - f(a))
        Fx = f(x)
        
        ## Mostra valores na tela
        print("%d\t%e\t%e\t%e\t%e\t%e\t%e\t%e"%(k,a, Fa, b, Fb, x, Fx, intervX))
        
        ## Teste do critério de parada módulo da função
        if abs(Fx) < epsilon:
            return(False,x)
        
        ## Testes para saber se a raiz está entre a e x ou entre x e b e atualiza
        ## as variáveis apropriadamente
        
        if Fa * Fx > 0 :
            a = x
            Fa = Fx
        else:
            b = x
            Fb = Fx
        
        ## Atualiza intervX e checa o outro critério de parada: tamanho do intervalo
        intervX = abs(b - a)
        if intervX < epsilon:
            return(False,x)
       
    ## Mostrar uma mensagem de erro e retorna que houve erro e a última raiz encontrada
    print("ERRO! número máximo de iterações atingido.")
    
    return (True, x)



def MPF(f, fi,x0, epsilson, iterMax=50):
   
    ## Teste se x0 já é logo a raiz
    if f(x0) == 0:
        return (False,x0)

    ## Escreva o cabeçalho da tabela e o valor da aproximação inicial
    print("k\t  x\t\t  f(x1)\t")
    
    ## Inicie as iterações (pode ser um for)
    for i in range(iterMax):
        ## Em cada iteração: 
        ##    Calcule x1 a partir de x0
        x = fi(x0)
        Fx = f(x)
        ##    Escreva os valores de k, x1, f(x1)
        print("%d\t%e\t%e"%(i, x, Fx))

        ##    Teste para o critério de parada usando módulo da função
        if abs(Fx) < epsilson:
              return (False,x)
        ##    Atualize o valor de x0
        x0 = x
          
    ## Se atingir o número máximo de iterações mostra mensagem de erro e retorna
    ## a última raiz encontrada
    print("ERRO! número máximo de iterações atingido.")
    return (True, x)

def newton(f, flin, x0, epsilson, iterMax=50):
    """Executa o método de Newton-Raphson para ac8har o zero de f  
       a partir da derivada de f flin, aproximação inicial x0 
       e tolerância epsilon.
       Retorna uma tupla (houveErro, raiz), onde houveErro é booleano.
    """   
    ## Teste se x0 já é logo a raiz
    if f(x0) == 0:
        return (False,x0)

    ## Escreva o cabeçalho da tabela e o valor da aproximação inicial
    print("k\t  x\t\t  f(x1)\t")
    
    ## Inicie as iterações (pode ser um for)
    for i in range(iterMax):
        ## Em cada iteração: 
        ##    Calcule x1 a partir de x0
        x = x0 - f(x0)/flin(x0)
        Fx = f(x)
        ##    Escreva os valores de k, x1, f(x1)
        print("%d\t%e\t%e"%(i, x, Fx))

        ##    Teste para o critério de parada usando módulo da função
        if abs(Fx) < epsilson:
              return (False,x)
        ##    Atualize o valor de x0
        x0 = x
          
    ## Se atingir o número máximo de iterações mostra mensagem de erro e retorna
    ## a última raiz encontrada
    print("ERRO! número máximo de iterações atingido.")
    return (True, x)


def secante(f, x0, x1, epsilson, iterMax=50):
    """Executa o método da Secante para achar o zero de f  
       a partir das aproximações x0 e x1, e da tolerância 
       epsilon.
       Retorna uma tupla (houveErro, raiz), onde houveErro é booleano.
    """
    ## Teste se x0 e x1 já são raízes
    if f(x0) == 0:
        return (False,x0)
    
    if f(x1) == 0:
        return (False,x1)
    
    ## Escreva o cabeçalho da tabela e as linhas para x0 e x1
    print("k\t  x\t\t  f(x2)\t\t")
    print("-\t%e\t%e"%(x0, f(x0)))
    print("-\t%e\t%e"%(x1, f(x1)))
    
    ## Inicie as iterações (pode ser um for)
    for i in range(iterMax):
        ## Em cada iteração: 
        ##Calcule x2 a partir de x0 e x1
        x2 = (x0*f(x1) - x1*f(x0))/(f(x1) - f(x0))
        Fx = f(x2)
        ##    Escreva os valores de k, x2, f(x2)
        print("%d\t%e\t%e"%(i, x2, Fx))

        ##    Teste para o critério de parada usando módulo da função
        if abs(Fx) < epsilson:
              return (False,x2)
        ##    Atualize o valor de x0 e x1
        x0 = x1
        x1 = x2
          
    ## Se atingir o número máximo de iterações mostra mensagem de erro e retorna
    ## a última raiz encontrada
    print("ERRO! número máximo de iterações atingido.")
    return (True, x2)