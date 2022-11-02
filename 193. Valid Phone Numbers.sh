# Read from the file file.txt and output all valid phone numbers to stdout.
# 这个题解挺厉害的，写的挺清晰：https://leetcode.cn/problems/valid-phone-numbers/solution/zheng-ze-biao-da-shi-zhong-xian-ding-fu-yu-ding-we/

# -P 可以让grep使用perl的正则表达式语法，因为perl的正则更加多元化，能实现更加复杂的场景。
grep -P '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt
