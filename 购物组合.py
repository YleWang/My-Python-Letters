for a in range(0,51):
    for b in range(0, 51):
        for c in range(0, 51):
            if a * 15 + b * 5 + c * 2 == 100:
                print('可以买洗发水', a, '瓶，牙刷', b, '个，香皂', c, '块')