#!/usr/bin/env python3
# File: bigdigits.py
# Func: 输出指定整数的大个字符样式
# Note: 每一位的0-9数字字符样式已经预先设定好的，只需要将所有字符按行输出。
#       在原代码的基础上将数字字符样式改为等宽度。

# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import sys #从命令行中读取参数列表

Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One =  ["   *   ", 
        "  **   ", 
	    "   *   ", 
	    "   *   ", 
	    "   *   ", 
	    "   *   ", 
	    "  ***  "]
Two =  ["  ***  ", 
        " *   * ", 
	    " *  *  ", 
	    "   *   ", 
	    "  *    ", 
	    " *     ", 
	    " ***** "]
Three =["  ***  ", 
        " *   * ", 
		"     * ", 
		"   **  ", 
		"     * ", 
		" *   * ", 
		"  ***  "]
Four = ["    *  ", 
        "   **  ", 
		"  * *  ", 
		" *  *  ", 
		"*******", 
		"    *  ",
        "    *  "]
Five = [" ***** ", 
        " *     ", 
		" *     ", 
		"  ***  ", 
		"     * ", 
		" *   * ", 
		"  ***  "]
Six =  ["  ***  ", 
        " *     ", 
		" *     ", 
		" ****  ", 
		" *   * ", 
		" *   * ", 
		"  ***  "]
Seven =[" ***** ", 
        "     * ", 
		"    *  ", 
		"   *   ", 
		"  *    ", 
		" *     ", 
		" *     "]
Eight =["  ***  ", 
        " *   * ", 
		" *   * ", 
		"  ***  ", 
		" *   * ", 
		" *   * ", 
		"  ***  "]
Nine = ["  **** ", 
        " *   * ", 
		" *   * ", 
		"  **** ", 
		"     * ", 
		"     * ", 
		"     * "]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1] #读取命令行第二个参数
    row = 0 #从第0行开始输出结果
    while row < 7:
        line = "" #初始化待输出的一行字符串为空
        column = 0
        while column < len(digits):     #按列输出参数字符串中的每一个字符
            number = int(digits[column])#将参数中第column个字符转换为整数
            digit = Digits[number]      #读取该数字的字符串样式列表
            line += digit[row] + "  "   #将该数字字符串样式列表的第row行追加到line并添加2个空格作为数字之间的分隔
            column += 1                 #读取参数中下一列字符
        print(line)
        row += 1
except IndexError:#如果不存在第二个参数，则提示用法错误！
    print("usage: bigdigits.py <number>")
except ValueError as err:#如果参数中有字符不能转换为数字，则出现异常！
    print(err, "in", digits)
