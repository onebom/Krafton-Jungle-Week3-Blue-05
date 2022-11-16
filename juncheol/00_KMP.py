def kmp_match(txt: str, pat: str) -> int:
    # kmp 법으로 문자열 검색
    pt = 1 # txt를 따라가는 커서
    pp = 0 # pat을 따라가는 커서
    skip = [0] * (len(pat) + 1) # 건너뛰기 표

    # 건너뛰기 표 만들기
    print('건너뛰기 표를 만듭니다.')
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            print('일치합니다. ',pt,pp)
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            print('첫번째')
            pt += 1
            skip[pt] = pp
        else:
            print('일치하지 않습니다.')
            pp = skip[pp]

    print('skip = ', skip)

    # 문자열 검색하기
    print('문자열을 검색합니다.')
    pt = pp = 0
    count = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0 :
            pt += 1
        else:
            pp = skip[pp]
            count += 1
    print('count =', count)
    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요 :') # 텍스트용 문자열
    s2 = input('패턴을 입력하세요 :') # 패턴용 문자열

    idx = kmp_match(s1, s2) # 문자열 s1 ~ s2까지를 KMP 법을 검색

    if idx == -1 :
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{idx + 1}번쨰 문자가 일치합니다.')


    