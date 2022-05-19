#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

EPS = 1e-10


if __name__ == '__main__':
    x = float(input("Введите x (0 <= x <= 2): "))
    if not 0 <= x <= 2:
        print("Ошибка", file=sys.stderr)
        exit(1)

    a = (-1) * (x-1)
    S, k = a, 1

    while math.fabs(a) > EPS:
        a *= (-1) * (x-1) / k
        S += a
        k += 1

    print(f"f(x) = {S}")