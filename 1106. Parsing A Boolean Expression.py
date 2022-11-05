class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # 建立一个列表来表示栈
        stk = []
        # 遍历表达式中的每一个字符
        for c in expression:
            # 如果是逗号，无实际意义，用来分隔变量的，继续读就好
            if c == ',':
                continue
            # 如果不是右括号，添加到栈中，只有右括号不添加，因为右括号出现时要进行运算了，要出栈，注意，入栈后是不做任何操作的，直接进行下一循环的
            if c != ')':
                stk.append(c)
                continue

            # 到这说明一定是遇到了右括号，要开始处理了
            
            # 初始化t，f的个数为零，也就是true和false的个数为零
            t = f = 0
            # 当栈中倒数第一个字符不是左括号时，也就是当前段处理未结束，需要运算
            # 注意这里判断用的是索引，不是出栈
            while stk[-1] != '(':
                # 如果出栈是t，那么t的个数加1
                if stk.pop() == 't':
                    t += 1
                # 否则，f的个数加1
                else:
                    f += 1
            # 只有当栈中最后一个是左括号时才会到这里，那么左括号出栈
            stk.pop()
            # 记录左括号前的操作符
            op = stk.pop()
            # 如果是非
            if op == '!':
                # 如果f是1，取反操作也就是将t入栈，如果不是将f入栈
                stk.append('t' if f == 1 else 'f')
            # 操作为与，如果f是0，那么就是t，但凡f不是0个，就是f
            elif op == '&':
                stk.append('t' if f == 0 else 'f')
            # 操作为或，只要t不是0，就是t了
            elif op == '|':
                stk.append('t' if t else 'f')
        # 最后看栈尾是不是t，是t就是true，不是就是false
        return stk[-1] == 't'
