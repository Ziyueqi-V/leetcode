# Read from the file words.txt and output the word frequency list to stdout.


# |
# 管道符号，是unix一个很强大的功能,符号为一条竖线:"|"。
# 用法: command 1 | command 2 他的功能是把第一个命令command 1执行的结果作为command 2的输入传给command 2

# cat（英文全拼：concatenate）命令用于连接文件并打印到标准输出设备上。

# tr（translate缩写）主要用于删除文件中的控制字符，或进行字符转换。
# 语法：tr [–c/d/s/t] [SET1] [SET2]
# SET1: 字符集1
# SET2：字符集2
# -c:complement，用SET2替换SET1中没有包含的字符
# -d:delete，删除SET1中所有的字符，不转换
# -s: squeeze-repeats，压缩SET1中重复的字符
# -t: truncate-set1，将SET1用SET2转换， 一般缺省为-t

# Linux sort 命令用于将文本文件内容加以排序。
# sort 可针对文本文件的内容，以行为单位来排序。
# -b 忽略每行前面开始出的空格字符。
# -c 检查文件是否已经按照顺序排序。
# -d 排序时，处理英文字母、数字及空格字符外，忽略其他的字符。
# -f 排序时，将小写字母视为大写字母。
# -i 排序时，除了040至176之间的ASCII字符外，忽略其他的字符。
# -m 将几个排序好的文件进行合并。
# -M 将前面3个字母依照月份的缩写进行排序。
# -n 依照数值的大小排序。
# -u 意味着是唯一的(unique)，输出的结果是去完重了的。
# -o<输出文件> 将排序后的结果存入指定的文件。
# -r 以相反的顺序来排序。
# -t<分隔字符> 指定排序时所用的栏位分隔字符。
# +<起始栏位>-<结束栏位> 以指定的栏位来排序，范围由起始栏位到结束栏位的前一栏位。
# --help 显示帮助。
# --version 显示版本信息。
# [-k field1[,field2]] 按指定的列进行排序。
# sort 命令将以默认的方式将文本文件的第一列以 ASCII 码的次序排列，并将结果输出到标准输出。

# Linux uniq 命令用于检查及删除文本文件中重复出现的行列，一般与 sort 命令结合使用。
# uniq 可检查文本文件中重复出现的行列。
# -c或--count 在每列旁边显示该行重复出现的次数。

# AWK 是一种处理文本文件的语言，是一个强大的文本分析工具。
# 之所以叫 AWK 是因为其取了三位创始人 Alfred Aho，Peter Weinberger, 和 Brian Kernighan 的 Family Name 的首字符。
# 关于 awk 脚本，我们需要注意两个关键词 BEGIN 和 END。
# BEGIN{ 这里面放的是执行前的语句 }
# END {这里面放的是处理完所有的行后要执行的语句 }
# {这里面放的是处理每一行时要执行的语句}
# 每行按空格或TAB分割，输出文本中的1、4项
# $ awk '{print $1,$4}' log.txt


cat words.txt | tr -s ' ' '\n'|sort|uniq -c|sort -nr|awk '{print $2" "$1}'
