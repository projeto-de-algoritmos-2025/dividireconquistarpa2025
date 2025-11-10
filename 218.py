from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        return self._resolver_recursivamente(buildings)

    def _resolver_recursivamente(self, predios_atuais: List[List[int]]) -> List[List[int]]:
        
        num_predios = len(predios_atuais)
        
        # caso 1 = sem predios, skyline vazio
        if num_predios == 0:
            return []
        
        # caso 2 = somente 1 predio
        # retorna dois pontos: [inicio, altura], [fim, 0]
        if num_predios == 1:
            l, r, h = predios_atuais[0]
            return [[l, h], [r, 0]]
        
        # divisao: encontra o meio e divide a lista de predios
        ponto_medio = num_predios // 2
        
        # chama para a  esquerda
        skyline_esquerdo = self._resolver_recursivamente(predios_atuais[:ponto_medio])
        
        # chama para a direita
        skyline_direito = self._resolver_recursivamente(predios_atuais[ponto_medio:])
        
        # conquista: mescla os dois resultados
        return self._mesclar_skylines(skyline_esquerdo, skyline_direito)

        pass

    def _mesclar_skylines(self, esq: List[List[int]], dir: List[List[int]]) -> List[List[int]]:
        
        #conquistar

        pass