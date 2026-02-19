def rev_keep_space(s):
    ch = list(s)
    left = 0
    right = len(s) -1

    while left < right:
        if ch[left] == ' ':
            left +=1
        elif ch[right] == ' ':
            right -=1
        else:
            ch[left], ch[right] = ch[right],ch[left]
            left +=1
            right-=1
    return ''.join(ch)

print(rev_keep_space("i am good"))

def reverse_preserve_symbols(s):
    chars = list(s)
    left = 0
    right = len(chars) -1
    
    while left < right:
        if not chars[left].isalpha():
            left +=1
        elif not chars[right].isalpha():
            right -=1
        else:
            chars[left],chars[right] = chars[right], chars[left]
            left +=1
            right -=1

    return ''.join(chars)