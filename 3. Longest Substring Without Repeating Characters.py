class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 先判断特殊形况，给的字符串本来为空，那么直接返回长度为0
        if not s:return 0
        # 初始化剩余字符串在原字符串中的起始索引为0
        left = 0
        # 建立一个空集合为查重集合
        lookup = set()
        # 原字符串长度为n
        n = len(s)
        # 初始化最大子串（子字符串）长度为零
        max_len = 0
        # 初始化当前找到的字串长度为零
        cur_len = 0
        # 遍历原字符串长度内的所有数，作为下标，其实就是遍历原字符串中的每个字符
        for i in range(n):
            # 开始判断新字符串了，那么就增加一个长度，如果不符合，再减去
            cur_len += 1
            # 如果当前字符在查重集合中，那么进入循环
            # 刚开始第一个字符肯定不会在查重集合中，也就是不会是重复出现的
            while s[i] in lookup:
                # 从查找集合中删除剩余子串的首字符
                # 只要重复字符没被删去，就会不断循环，left不断右移
                lookup.remove(s[left])
                # 剩余子串的开端右移一位（索引加1）
                left += 1
                # 当前字符重复了，不能计入长度增加，所以当前字符串长度减1
                cur_len -= 1
            # 如果当前长度比最大长度还要大，那么就将当前长度记录为最大长度
            if cur_len > max_len:max_len = cur_len
            # 将当前字符串加入查重集合中
            # 下面这句不在循环中，那就是原字符串中每个字符都会被添加到查重集合中，不过一旦有重复，先出现的就被删除了
            lookup.add(s[i])
        return max_len

作者：qing-shan-si-ma
链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters/solution/zhu-shi-by-qing-shan-si-ma-phsq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
