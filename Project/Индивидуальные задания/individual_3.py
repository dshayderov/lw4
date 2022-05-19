#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    n = int(input("Введите кол-во часов: "))
    if n < 0:
        print("Ошибка", file=sys.stderr)

    count = n//3
    a = 1
    for k in range(1, count + 1):
        a *= 2

    print(f"Кол-во клеток через {n} часов: {a}")
