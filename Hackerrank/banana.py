def minion_game(string):
    s = string
    ss = 0
    ks = 0
    ls = []
    lk = []
    sw = ''
    kw = ''
    v = 'AEIOU'
    for i in range(0, len(s)):
        if s[i] in v:
            for j in range(i, len(s)):
                for k in range(i, j+1):
                    kw += s[k]
                ks += s.count(kw) if kw not in lk else 0
                lk.append(kw)
                kw = ''
        else:
            for j in range(i, len(s)):
                for k in range(i, j+1):
                    sw += s[k]
                ss += s.count(sw) if sw not in ls else 0
                ls.append(sw)
                sw = ''
    if ss>ks:
        print(f'Stuart {ss} {ks}')
    elif ks>ss:
        print(f'Kevin {ks} {ss}')
    else:
        print('Draw')

if __name__ == '__main__':
    s = 'BANANANAAAS'
    minion_game(s)