from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        def _combinar_contando(sub_esq: List[int], sub_dir: List[int]) -> (int, List[int]):
            num_inversoes = 0
            resultado_mesclado = []
            i_esq, i_dir = 0, 0
            tam_esq, tam_dir = len(sub_esq), len(sub_dir)

            while i_esq < tam_esq and i_dir < tam_dir:
                if sub_esq[i_esq] <= sub_dir[i_dir]:
                    resultado_mesclado.append(sub_esq[i_esq])
                    i_esq += 1
                else:
                    resultado_mesclado.append(sub_dir[i_dir])
                    i_dir += 1
                    num_inversoes += tam_esq - i_esq

            resultado_mesclado.extend(sub_esq[i_esq:])
            resultado_mesclado.extend(sub_dir[i_dir:])
            return num_inversoes, resultado_mesclado

        def _ordenar_recursivo(lista_parcial: List[int]) -> (int, List[int]):
            if len(lista_parcial) <= 1:
                return 0, lista_parcial

            meio = len(lista_parcial) // 2
            inversoes_esq, ordenada_esq = _ordenar_recursivo(lista_parcial[:meio])
            inversoes_dir, ordenada_dir = _ordenar_recursivo(lista_parcial[meio:])
            inversoes_mescla, lista_final = _combinar_contando(ordenada_esq, ordenada_dir)

            return inversoes_esq + inversoes_dir + inversoes_mescla, lista_final

        def _contar_pares_menores_que(distancia_max: int) -> int:
            contagem = 0
            ponteiro_esq = 0
            
            for ponteiro_dir in range(len(nums)):
                while nums[ponteiro_dir] - nums[ponteiro_esq] > distancia_max:
                    ponteiro_esq += 1
                contagem += ponteiro_dir - ponteiro_esq
            return contagem

        nums.sort()

        dist_minima, dist_maxima = 0, nums[-1] - nums[0]
        
        while dist_minima < dist_maxima:
            distancia_teste = (dist_minima + dist_maxima) // 2
            
            if _contar_pares_menores_que(distancia_teste) < k:
                dist_minima = distancia_teste + 1
            else:
                dist_maxima = distancia_teste

        return dist_minima