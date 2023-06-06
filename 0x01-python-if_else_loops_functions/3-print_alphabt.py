#!/usr/bin/python3
for i in range(97, 122):
    if (i == ord('e')) or (i == ord('q')):
        continue
    print(f"{chr(i)}", end="")
