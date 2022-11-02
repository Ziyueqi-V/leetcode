# Read from the file file.txt and output the tenth line to stdout.

# tail 命令可用于查看文件的内容，有一个常用的参数 -f 常用于查阅正在改变的日志文件。
# tail -f filename 会把 filename 文件里的最尾部的内容显示在屏幕上，并且不断刷新，只要 filename 更新就可以看到最新的文件内容。
# -n<行数> 显示文件的尾部 n 行内容

# 注意：tail -n +10 与 tail -n 10 不一样，-n +10 表示从第 10 行开始显示，若文件不足 10 行则什么也不会输出；-n 10 表示显示最后的 10 行。

# 举例：
# head -20 install.log
# 通过上面命令你可以查看install.log这个文件前面20行的内容

# 从十行开始输出，第二步查看输入内容的前面部分的一行，两者结合，就是第10行了
tail -n +10 file.txt | head -1
