class Solution(object):

    # решение которое прошло все тесты на лимит времени
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        max_result = temp_sum = float('-inf')

        def get_sum_max_range(array):
            max_sum = current_sum = sum(array)

            for i in range(len(array) - 1):
                current_sum -= array[i]
                if max_sum < current_sum:
                     max_sum = current_sum

            return max_sum

        for i in range(k):
            temp_sum = get_sum_max_range(energy[i::k])
            if temp_sum > max_result:
                max_result = temp_sum
        return max_result

    # решение которое не прошло временные лимиты
    def maximumEnergy_2(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        max_result = float('-inf')
        for i in range(len(energy)):
            max_result = max(
                max_result,
                sum(energy[i::k])
            )
        return max_result
