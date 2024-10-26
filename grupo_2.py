from concurrent.futures import ThreadPoolExecutor

class NoParalelo:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaParalela:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = NoParalelo(valor)
        else:
            with ThreadPoolExecutor() as executor:
                executor.submit(self._inserir_paralelo, self.raiz, valor)

    def _inserir_paralelo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoParalelo(valor)
            else:
                with ThreadPoolExecutor() as executor:
                    executor.submit(self._inserir_paralelo, no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = NoParalelo(valor)
            else:
                with ThreadPoolExecutor() as executor:
                    executor.submit(self._inserir_paralelo, no_atual.direita, valor)

    def percurso_pre_ordem_paralelo(self):
        return self._pre_ordem_paralelo(self.raiz, [])

    def _pre_ordem_paralelo(self, no, percurso):
        if no is None:
            return percurso
        percurso.append(no.valor)
        with ThreadPoolExecutor() as executor:
            esquerda = executor.submit(self._pre_ordem_paralelo, no.esquerda, [])
            direita = executor.submit(self._pre_ordem_paralelo, no.direita, [])
            percurso.extend(esquerda.result())
            percurso.extend(direita.result())
        return percurso

    def percurso_em_ordem_paralelo(self):
        return self._em_ordem_paralelo(self.raiz, [])

    def _em_ordem_paralelo(self, no, percurso):
        if no is None:
            return percurso
        with ThreadPoolExecutor() as executor:
            esquerda = executor.submit(self._em_ordem_paralelo, no.esquerda, [])
            percurso.extend(esquerda.result())
            percurso.append(no.valor)
            direita = executor.submit(self._em_ordem_paralelo, no.direita, [])
            percurso.extend(direita.result())
        return percurso

    def percurso_pos_ordem_paralelo(self):
        return self._pos_ordem_paralelo(self.raiz, [])

    def _pos_ordem_paralelo(self, no, percurso):
        if no is None:
            return percurso
        with ThreadPoolExecutor() as executor:
            esquerda = executor.submit(self._pos_ordem_paralelo, no.esquerda, [])
            direita = executor.submit(self._pos_ordem_paralelo, no.direita, [])
            percurso.extend(esquerda.result())
            percurso.extend(direita.result())
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

    def buscar_paralelo(self, valor):
        return self._buscar_paralelo(self.raiz, valor)

    def _buscar_paralelo(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        with ThreadPoolExecutor() as executor:
            if valor < no.valor:
                esquerda = executor.submit(self._buscar_paralelo, no.esquerda, valor)
                return esquerda.result()
            else:
                direita = executor.submit(self._buscar_paralelo, no.direita, valor)
                return direita.result()

arvore_paralela = ArvoreBinariaParalela()
valores = [20, 10, 5, 15, 30, 25, 35]

for valor in valores:
    arvore_paralela.inserir(valor)

print("Pré-Ordem (Paralelo):", arvore_paralela.percurso_pre_ordem_paralelo())
print("Em-Ordem (Paralelo):", arvore_paralela.percurso_em_ordem_paralelo())
print("Pós-Ordem (Paralelo):", arvore_paralela.percurso_pos_ordem_paralelo())
print("Altura da árvore:", arvore_paralela.altura())
print("Busca paralela pelo valor 15:", arvore_paralela.buscar_paralelo(15))
print("Busca paralela pelo valor 40:", arvore_paralela.buscar_paralelo(40))
