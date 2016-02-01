#!/usr/bin/env python3
# File: generate_grid.py
# Func: 创建一个随机生成的整数组成的网格
# Note: 需要用户指定网格的行数、列数以及整数的范围。

# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import random  #导入random模块

# 定义读取整数的函数，该函数可以传递一个提示消息字符串
# 通过get_int()函数可以很容易获取行数、列数以及用户需要的最小随机数值
def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print("must be >=", minimum)
            else:
                return i
        except ValueError as err:
            print(err)


rows = get_int("rows: ", 1, None)
columns = get_int("columns: ", 1, None)
minimum = get_int("minimum (or Enter for 0): ", -1000000, 0)

default = 1000 #初始化默认最大值
if default < minimum: #如果默认最大值比最小值还小，则将最大值设置为最小值的2倍
    default = 2 * minimum
# 重新要求用户设置最大值
maximum = get_int("maximum (or Enter for " + str(default) + "): ",
                  minimum, default)

row = 0
while row < rows:
    line = ""
    column = 0
    while column < columns:
        i = random.randint(minimum, maximum)
        s = str(i)
		# 对每个整数的字符串用空格进行填充，保证每个数字都使用10个字符表示
        while len(s) < 10:
            s = " " + s
        line += s
        column += 1
    print(line)
    row += 1
