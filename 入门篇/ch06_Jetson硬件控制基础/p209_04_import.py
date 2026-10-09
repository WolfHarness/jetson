# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第6章 Jetson硬件控制基础 · 印刷第209页 (PDF第219页)
# 上下文: 使用 GPIO。参考如下代码，将stderr 重定向到/dev/null 以屏蔽警告信息。 ／ 如果硬件可以正常工作，并且确定不需要修复该警告，则可以选择忽略该

import sys
import os

# 将stderr重定向到/dev/null以屏蔽警告
sys.stderr = open(os.devnull, 'w')

import Jetson.GPIO
