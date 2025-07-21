min_num = None
while True:
    try:
        x = float(input())
        if x <= 0:
            break
        if min_num is None or x < min_num:
            min_num = x
    except:
        break

if min_num is not None:
    print(min_num)