# Read from the file file.txt and print its transposed content to stdout.
# xargs（英文全拼： eXtended ARGuments）是给命令传递参数的一个过滤器，也是组合多个命令的一个工具。
# xargs 可以将管道或标准输入（stdin）数据转换成命令行参数，也能够从文件的输出中读取数据。
# xargs 也可以将单行或多行文本输入转换为其他格式，例如多行变单行，单行变多行。
# xargs 默认的命令是 echo，这意味着通过管道传递给 xargs 的输入将会包含换行和空白，不过通过 xargs 的处理，换行和空白将被空格取代。
# xargs 是一个强有力的命令，它能够捕获一个命令的输出，然后传递给另外一个命令。
# 之所以能用到这个命令，关键是由于很多命令不支持|管道来传递参数，而日常工作中有有这个必要，所以就有了 xargs 命令

# head 命令可用于查看文件的开头部分的内容，有一个常用的参数 -n 用于显示行数，默认为 10，即显示 10 行的内容。

# Linux wc命令用于计算字数。

# 利用wc指令我们可以计算文件的Byte数、字数、或是列数，若不指定文件名称、或是所给予的文件名为"-"，则wc指令会从标准输入设备读取数据。
# -c或--bytes或--chars 只显示Bytes数。
# -l或--lines 显示行数。
# -w或--words 只显示字数。
# --help 在线帮助。
# --version 显示版本信息。

# seq
# 用法：seq [选项]... 尾数
# 　或：seq [选项]... 首数 尾数
# 　或：seq [选项]... 首数 增量 尾数
# 以指定增量从首数开始打印数字到尾数。

columns=$(cat file.txt | head -n 1 | wc -w)
for i in $(seq 1 $columns)
do
# $i前后的'有一个或者三个都可以，主要是为了分离出$i给bash处理，而''内是给awk处理的字符串，可以理解为字符串拼接，只不过不能用加号而已
awk '{print $'$i'}' file.txt | xargs
done
