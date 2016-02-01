#!/usr/bin/env python3
# File: sum1.py
# Func: 求多个整数的和，并计算均值。
# Note: 注意如果此程序将数据文件重定向作为输入时会报错。

# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

print("Type integers, each followed by Enter; or just Enter to finish")

total = 0
count = 0

while True:
    line = input("integer: ") #读入一行字符串
    if line:
        try:
            number = int(line) #将字符串转换成整数
        except ValueError as err: #如果字符串不能转换为整数而发生异常
            print(err)
            continue
        total += number
        count += 1
    else: #如果读入的字符串为空，则停止读取
        break

if count:
    print("count =", count, "total =", total, "mean =", total / count)
