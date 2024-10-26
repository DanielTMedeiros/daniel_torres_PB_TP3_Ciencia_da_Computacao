class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)

    def pre_ordem(self):
        return self._pre_ordem_recursivo(self.raiz, [])

    def _pre_ordem_recursivo(self, no, percurso):
        if no:
            percurso.append(no.valor)
            self._pre_ordem_recursivo(no.esquerda, percurso)
            self._pre_ordem_recursivo(no.direita, percurso)
        return percurso

    def em_ordem(self):
        return self._em_ordem_recursivo(self.raiz, [])

    def _em_ordem_recursivo(self, no, percurso):
        if no:
            self._em_ordem_recursivo(no.esquerda, percurso)
            percurso.append(no.valor)
            self._em_ordem_recursivo(no.direita, percurso)
        return percurso

    def pos_ordem(self):
        return self._pos_ordem_recursivo(self.raiz, [])

    def _pos_ordem_recursivo(self, no, percurso):
        if no:
            self._pos_ordem_recursivo(no.esquerda, percurso)
            self._pos_ordem_recursivo(no.direita, percurso)
            percurso.append(no.valor)
        return percurso

    def altura(self):
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, no):
        if no is None:
            return -1
        altura_esquerda = self._altura_recursiva(no.esquerda)
        altura_direita = self._altura_recursiva(no.direita)
        return 1 + max(altura_esquerda, altura_direita)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        elif valor < no.valor:
            return self._buscar_recursivo(no.esquerda, valor)
        else:
            return self._buscar_recursivo(no.direita, valor)

arvore = ArvoreBinaria()
valores_desordenados = [45, 10, 50, 20, 55, 15, 5]

for valor in valores_desordenados:
    arvore.inserir(valor)

print("Pré-Ordem:", arvore.pre_ordem()) 
print("Em-Ordem:", arvore.em_ordem())     
print("Pós-Ordem:", arvore.pos_ordem())   
