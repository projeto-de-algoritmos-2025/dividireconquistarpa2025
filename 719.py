class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        def _contar_pares_menores_que(distancia_max: int) -> int:

        nums.sort()
        
        dist_minima, dist_maxima = 0, nums[-1] - nums[0]
        
        while dist_minima < dist_maxima:
            distancia_teste = (dist_minima + dist_maxima) // 2
            
            if _contar_pares_menores_que(distancia_teste) < k:
                dist_minima = distancia_teste + 1
            else:
                dist_maxima = distancia_teste

        return dist_minima