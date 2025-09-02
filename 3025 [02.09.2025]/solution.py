class Solution(object):

    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        length = len(points)

        for i in range(length):
            for j in range(length):
                # Пропускаем, если точки одинаковые
                if i == j:
                    continue

                x1, y1 = points[i] # точка A
                x2, y2 = points[j] # точка B

                # Первое условие: A находится в верхнем левом квадранте B.
                if x1 <= x2 and y1 >= y2:

                    # Второе условие: в прямоугольнике между ними нет других точек.
                    is_valid = True
                    for k in range(length):
                        # Пропускаем точки, которые являются A или B
                        if k == i or k == j:
                            continue

                        x3, y3 = points[k]

                        # Проверяем, находится ли точка k внутри прямоугольника (включая границы).
                        if (x1 <= x3 <= x2) and (y2 <= y3 <= y1):
                            is_valid = False
                            break

                    if is_valid:
                        count += 1

        return count