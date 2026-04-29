def reverse(s):
    s =list(s)
    l,r = 0, len(s)-1

    vowels = set(["a","e","i","o","u","A","E","I","O","U"])

    while l<r:
        if s[l] not in vowels :
            l+=1
        elif s[r] not in vowels:
            r-=1
        else:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
    return ''.join(s)

if __name__ == "__main__" :
    s = "hello"
    print(reverse(s))             
