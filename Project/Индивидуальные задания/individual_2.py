#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))

    if a >= b >= c:
        print(f"По возрастанию: {c}, {b}, {a}\n"
              f"По убыванию: {a}, {b}, {c}")
    elif a >= c >= b:
        print(f"По возрастанию: {b}, {c}, {a}\n"
              f"По убыванию: {a}, {c}, {b}")
    elif c >= a >= b:
        print(f"По возрастанию: {b}, {a}, {c}\n"
              f"По убыванию: {c}, {a}, {b}")
    elif c >= b >= a:
        print(f"По возрастанию: {a}, {b}, {c}\n"
              f"По убыванию: {c}, {b}, {a}")
    elif b >= a >= c:
        print(f"По возрастанию: {c}, {a}, {b}\n"
              f"По убыванию: {b}, {a}, {c}")
    else:
        print(f"По возрастанию: {a}, {c}, {b}\n"
              f"По убыванию: {b}, {c}, {a}")