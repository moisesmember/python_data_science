# Importando biblioteca
import numpy as np

# Começando com os vetores sabemos que vetores podem ser linhas ou colunas, desta forma
# podemos modifica-los para que linhas -> coluna ou coluna -> linha conforme exemplificação.

# Ainda é importante lembrar que ao transposicionar um vetor, nenhuma informação é perdida 
# ou modificada. A unica coisa que acontece é a a mudança de posição da linha ou coluna.
# Transponto um vetor duas vezes, é gerado um terceiro vetor (vetor inicial) e por fim o
# vetor transporto possui o mesmo comprimento, se 3x1 -> 3x1 ou 1x3 -> 3x1.

# Todas as regras acima se aplicam também em matrizes


# Criando mais modelos de matrizes
m1 = np.array([[10,20,30],[40,50,60]])
m2 = np.array([[30,20,10],[60,50,40]])
v1 = np.array([5,4,3,2,1])
v2 = np.array([1,2,3,4,5])
e1 = np.array([2])

# Com o recurso "T" do numpy podemos transpor uma matriz
# observe a diferença das impressões na saida do console
print(m1)
print(m2)
print(m1.T)
print(m2.T)

# Podemos realizar o mesmo procedimento com escalares ou vetores
print(e1.T)

# Agora com vetores, podemos achar aque nada mudou, mas é so realizar
# a comparação com o metodo shape() para verificar a linha x coluna
print(v1.shape)
print(v1.T)
print(v1.shape)