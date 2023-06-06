#!/usr/bin/python3
def remove_char_at(str, n):
    swap_str = str
    if n >= 0 and n <= len(swap_str):
        swap_str = swap_str[:n] + swap_str[n + 1:]
    return swap_str
