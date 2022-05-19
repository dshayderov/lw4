#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    n = int(input("Введите свой возраст: "))
    if n <= 0 or n >= 100:
        print("Ошибка", file=sys.stderr)
        exit(1)

    a = n % 10
    if a == 1 and not 10 < n < 20:
        print(f"Мне {n} год")
    elif 1 < a < 5 and not 10 < n < 20:
        print(f"Мне {n} года")
    else:
        print(f"Мне {n} лет")