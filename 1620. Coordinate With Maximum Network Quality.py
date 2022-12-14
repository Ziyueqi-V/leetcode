class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        # 确定最大的范围，分别找x的最大和y的最大
        x_max = max(t[0] for t in towers)
        y_max = max(t[1] for t in towers)
        # 初始化最大信号强度为0，信号最大点的坐标为(0,0)
        cx = cy = max_quality = 0
        # 遍历最大x范围内的每个整数的x坐标
        for x in range(x_max + 1):
            # 遍历最大y范围内的每个整数y坐标
            for y in range(y_max + 1):
                # 当前点信号强度置为0
                quality = 0
                # 遍历每个信号塔信息
                for tx, ty, q in towers:
                    # 范围内的整数点到该信号塔的距离的平方（不做开方处理便于比较，其实就是距离的代表）
                    d = (x - tx) ** 2 + (y - ty) ** 2
                    # 如果当前位置到该信号塔的距离没有超出信号能到达的最远距离（距离相等也能覆盖到）
                    if d <= radius ** 2:
                        # 当前位置的信号强度就累加上该信号塔相应的信号强度
                        quality += int(q / (1 + d ** 0.5))
                # 如果该点信号强度大于已记录的最大信号强度
                if quality > max_quality:
                    # 刷新记录：记录较大的信号强度和位置信息
                    cx, cy, max_quality = x, y, quality
        # 遍历完所有的可能位置，返回结果
        return [cx, cy]
