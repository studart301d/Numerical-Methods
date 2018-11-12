import numpy as np

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


    def sistemaLinearTriangular(matrizA,vectorb,tipo):
    
    if type(matrizA) != np.ndarray:
            matrizA = np.array(matrizA)
            
    #Verificar se a Matriz A é triangular inferior

    b = len(vectorb)  # size da Matriz A

    vectorX = []    #Vetor x
    
    if tipo == 'inf':
    
        for i in range(b):
            vectorX.append((vectorb[i] - sum(vectorX[0:i]*matrizA[i][0:i]))/matrizA[i][i])
            
    elif tipo == 'sup':
        
        #[::-1] Inverte o vetor [x,y][::-1] = [y,x]
        matrizA = matrizA[::-1]
        vectorb = vectorb[::-1]
        
        for i in range(b):
            vectorX.append((vectorb[i] - sum(vectorX[0:i][::-1]*matrizA[i][b-i:b]))/matrizA[i][b - 1 -i])
            
        vectorX = vectorX[::-1]

    return vectorX
    
    def substituicoes_retroativas(A, b):
    '''Executa o método das substituições retroativas para resolver o sistema 
       linear triangular superior Ax=b.
       Parâmetros de entrada: A é uma matriz triangular superior e b é o vetor constante. 
    '''
    ## n é a ordem da matriz A
    n = len(A)
    
    ## inicializa o vetor x com tamanho n e elementos iguais a 0
    x = n * [0] 
    
    # escreva o seu código aqui
    A = A[::-1]
    b = b[::-1]
    
    for i in range(n):
        x[i] = (b[i] - sum([elem1*elem2 for elem1,elem2 in zip(x[0:i][::-1],A[i][n-i:n])]))/A[i][n - 1 -i]
         
    return x[::-1]

    def escolhe_pivo(k, A, b):
    '''Escolhe o pivô de maior valor absoluto na coluna k a partir da linha k 
       da matriz A. Se o pivô estiver numa linha diferente de k, as linhas da
       matriz A e do vetor b são trocadas.
       Saída: booleano (True se houve troca)
    '''
    ## n é a ordem da matriz A
    n = len(A)
    
    ## inicializa flag para controlar se houve troca de linha com false
    houve_troca = False
    ## identifica o elemento de maior valor absoluto e a linha onde ele está
    pivo = A[k][k]
    for i in range(k,n):
        auxPivo = abs(A[i][k])
        if auxPivo > pivo :
            
            houve_troca = True
            troca = i
            
    
    ## se k for diferente da linha onde está o pivô, troca a linha k
    ## pela linha do pivô em A e b e atribui o valor True à flag

    if houve_troca == True:
            
        aux = A[k]
        A[k] = A[troca]
        A[troca] = aux
            
        pivo = auxPivo
            
        aux = b[k]
        b[k] = b[troca]
        b[troca] = aux
    
    ## retorna a flag
    return houve_troca

    def gauss_pivot_det(A, b):
    '''Executa o método da eliminação de Gauss com pivotação para resolver o sistema  linear Ax=b 
    transformando o sistema em um sistema triangular superior equivalente.
    Parâmetros de entrada: A é uma matriz quadrada de ordem n e b é o vetor constante.
    Saída: vetor x
    '''
    ## n é a ordem da matriz A
    n = len(A)
    P = 0
    
    ## Para cada etapa k
    for j in range(n-1):
        
        ## Escolhe o pivô
        houve_troca = escolhe_pivo(j,A,b)
        if houve_troca == True:
            P = P + 1
            
        ## Para cada linha i
        for i in range(j+1,n):
            
            ## Calcula o fator m
            m = -A[i][j]/A[j][j]
            
            ## Atualiza a linha i da matriz, percorrendo todas as colunas j
            A[i] = [elem1 + elem2 for elem1,elem2 in zip(A[i],list(map(lambda x: x*m,A[j])))]
            
            # Atualiza o vetor b na linha i
            b[i] = b[i] + m*b[j]
            
            ## Zera o elemento Aik
            A[i][j] = 0 #Na minha opinião não precisa, não entendi porque precisa
    
    ## faz o cálculo do determinante antes de chamar as substituições retroativas

        
    det = 1
    for i in range(n):
        det = det*A[i][i]
    det = ((-1)**P)*det
    x = substituicoes_retroativas(A, b)
    
    return (x, det)

    def gauss_jordan(A, b = None ,onlyInv = False):
    
    '''
    Executa o método de Gauss-Jordan para resolver o sistema linear Ax=b 
    transformando a matriz A na matriz identidade.
    Parâmetros de entrada: A é uma matriz quadrada de ordem n e b é o vetor constante.
    Saída: vetor solução x
    '''
    n = len(A)
    
    
        
    if type(A) != np.ndarray:
            A = np.array(A)
    if type(b) != np.ndarray:
            b = np.array(b).astype(float)
            
    if b.all() == None:
        b = n*[1] #só pra pode fazer operações e não mudar o muito o codigo,se pedi só a matriz inversa
    
    # escreva o código aqui
    matrizA = np.concatenate((A,np.eye(n)),axis = 1).astype(float)
    
    for j in range(n):
        
        b[j] = b[j]/matrizA[j][j]
        matrizA[j] = matrizA[j]/matrizA[j][j]
        
        for i in range(n):

            if i != j :
                m = -matrizA[i][j]/matrizA[j][j]
                ## Atualiza a linha i da matriz, percorrendo todas as colunas j
                matrizA[i] = matrizA[j]*m+ matrizA[i]
                #matrizA[i] = [elem1 + elem2 for elem1,elem2 in zip(matrizA[i],list(map(lambda x: x*m,matrizA[j])))] 
                #Sem ser com numpy
                
                # Atualiza o vetor b na linha i
                b[i] = b[i] + m*b[j]
                
                 ## Zera o elereturn matrizA[:3,3:]mento Aik
                matrizA[i][j] = 0 
                
    if onlyInv:
        return matrizA[:3,3:]
    else:
        return (b,matrizA[:3,3:])


    def substituicoes_sucessivas(matrizA, vectorb):
    '''Executa o método das substituições sucessivas para resolver o sistema 
       linear triangular inferior Ax=b.
       Parâmetros de entrada: A é uma matriz triangular inferior e b é o vetor constante. 
       Saída: vetor x
    '''
    if type(matrizA) != np.ndarray:
        matrizA = np.array(matrizA)
            
    #Verificar se a Matriz A é triangular inferior

    b = len(vectorb)  # size da Matriz A

    vectorX = []    #Vetor x
    
    for i in range(b):
        vectorX.append((vectorb[i] - sum(vectorX[0:i]*matrizA[i][0:i]))/matrizA[i][i])
    return vectorX

    def lu(A):
    '''
    Decompõe a matriz A no produto de duas matrizes L e U. Onde L é uma matriz 
    triangular inferior unitária e U é uma matriz triangular superior.
    Parâmetros de entrada: A é uma matriz quadrada de ordem n.
    Saída: (L,U) tupla com as matrizes L e U
    '''
    n = len(A)
    
    ## Inicializa a matriz L com a matriz identidade
    #L = identidade(n)
    L = np.eye(n)
    
    # Escreva o seu código aqui
    for j in range(n-1):
        
        ## Escolhe o pivô
        #houve_troca = escolhe_pivo(j,A,b) #Não sei se precisa
        
        ## Para cada linha i
        for i in range(j+1,n):        
            
            ## Calcula o fator m
            m = -A[i][j]/A[j][j]
            
            ## Atualiza a linha i da matriz, percorrendo todas as colunas j
            A[i] = [elem1 + elem2 for elem1,elem2 in zip(A[i],list(map(lambda x: x*m,A[j])))]
            
            ## Zera o elemento Aik
            A[i][j] = 0 #Na minha opinião não precisa, não entendi porque precisa
            
            L[i][j] = -m
    
    return (L, np.array(A))

    def resolve_lu(A,b):
    '''
    Executa o método LU para resolver o sistema  linear Ax=b.
    Esse método inicialmente decompõe a matriz em L e U e depois resolve os 
    dois sistemas lineares triangulares.
    Parâmetros de entrada: A é uma matriz quadrada de ordem n e b é o vetor constante.
    Saída: vetor x solução do sistema.
    '''
    
    # Escreva o seu código aqui
    (L,U)= lu(A)
    
    y = substituicoes_sucessivas(L,b)
    x = substituicoes_retroativas(U,y)
    
    return x

    def norma(v,x):
    """Calcula a norma entre dois vetores v e x.
    """
    n = len(v)
    if type(v) != np.ndarray:
        v = np.array(v)
    if type(x) != np.ndarray:
        x = np.array(x)
        
    maxDif = max(abs(v-x))
    maxV = max(abs(v))
    
    norma = maxDif/maxV 
    
    return norma

    def jacobi(A, b, epsilon, iterMax=50):
    """Resolve o sistema linear Ax=b usando o método iterativo Gauss-Jacobi.
    O critério de parada utiliza a norma-infinito.
    Saída é o vetor x.
    
    """
    if type(A) != np.ndarray:
        A = np.array(A).astype(float)
    if type(b) != np.ndarray:
        b = np.array(b).astype(float)
        
    n = len(A)
    #x = n * [0]
    x = np.zeros(n)
    #v = n * [0]
    v = np.zeros(n)
    
    for i in range(n):
        
        b[i] = b[i]/A[i][i]
        A[i] = -A[i]/A[i][i]      
        
        x[i] = b[i]
        
        A[i][i] = 0
        
    for k  in range(iterMax):
        for i in range(n):
            v[i] = b[i] + sum((A*x)[i]) #Podia ser np.dot(A,x)[i]
            
        if norma(v,x) <= epsilon :
            return v
        x = np.copy(v)
        
    print("Passou do limite de iterações")
    return v

    def seidel(A, b, epsilon, iterMax=50):
    """Resolve o sistema linear Ax=b usando o método iterativo Gauss-Jacobi.
    O critério de parada utiliza a norma-infinito.
    Saída é o vetor x.
    
    """
    if type(A) != np.ndarray:
        A = np.array(A).astype(float)
    if type(b) != np.ndarray:
        b = np.array(b).astype(float)
        
    n = len(A)
    #x = n * [0]
    x = np.zeros(n)
    #v = n * [0]
    v = np.zeros(n)
    
    for i in range(n):
        
        b[i] = b[i]/A[i][i]
        A[i] = -A[i]/A[i][i]      
        
        A[i][i] = 0
        
    for k  in range(iterMax):
        
        x = np.copy(v)
        for i in range(n):
            
            
            v[i] = b[i] + sum((A*v)[i]) #Podia ser np.dot(A,x)[i]
            
            
        if norma(v,x) < epsilon :
            return v
        
    print("Passou do limite de iterações")
    return v