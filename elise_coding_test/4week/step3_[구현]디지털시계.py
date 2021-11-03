s, n = map(int, input().split())

for index in range(s*2+3):
    for i in str(n):
        if i == '0':
            if index == 0 or index == s*2+2:
                print(' ' + '-'*s + ' ', end=' ')
            elif index == (s*2+3) // 2:
                print(' ' * (s+2), end=' ')
            else:
                print('|' + ' ' * s + '|', end=' ')
        if i == '1':
            if index == 0 or index == (s*2+3) // 2 or index == s*2+2:
                print(' ' * (s+2), end=' ')
            else:
                print(' ' * (s+1) + '|', end=' ')
        if i == '2':
            if index == 0 or index == (s*2+3) // 2 or index == s*2+2:
                print(' ' + '-'*s + ' ', end=' ')
            elif index < (s*2+3) // 2:
                print(' ' * (s+1) + '|', end=' ')
            else:
                print('|' + ' ' * (s+1), end=' ')
        if i == '3':
            if index == 0 or index == (s*2+3) // 2 or index == s*2+2:
                print(' ' + '-'*s + ' ', end=' ')
            else:
                print(' ' * (s+1) + '|', end=' ')
        if i == '4':
            if index == 0 or index == s*2+2:
                print(' ' * (s+2), end=' ')
            elif index == (s*2+3) // 2:
                print(' ' + '-'*s + ' ', end=' ')
            elif index < (s*2+3) // 2:
                print('|' + ' ' * s + '|', end=' ')
            else:
                print(' ' * (s+1) + '|', end=' ')
        if i == '5':
            if index == 0 or index == (s*2+3) // 2 or index == s*2+2:
                print(' ' + '-'*s + ' ', end=' ')
            elif index < (s*2+3) // 2:
                print('|' + ' ' * (s+1), end=' ')
            else:
                print(' ' * (s+1) + '|', end=' ')
        if i == '6':
            if index == (s*2+3) // 2 or index == s*2+2 or index == 0:
                print(' ' + '-'*s + ' ', end=' ')
            elif index < (s*2+3) // 2:
                print('|' + ' ' * (s+1), end=' ')
            else:
                print('|' + ' ' * s + '|', end=' ')
        if i == '7':
            if index == 0:
                print(' ' + '-'*s + ' ', end=' ')
            elif index == (s*2+3) // 2 or index == s*2+2:
                print(' ' * (s+2), end=' ')
            else:
                print(' ' * (s+1) + '|', end=' ')
        if i == '8':
            if index == 0 or index == s*2+2 or index == (s*2+3) // 2:
                print(' ' + '-'*s + ' ', end=' ')
            else:
                print('|' + ' ' * s + '|', end=' ')
        if i == '9':
            if index == 0 or index == (s*2+3) // 2 or index == s*2+2:
                print(' ' + '-'*s + ' ', end=' ')
            elif index > (s*2+3) // 2:
                print(' ' * (s+1) + '|', end=' ')
            else:
                print('|' + ' ' * s + '|', end=' ')
    print()
