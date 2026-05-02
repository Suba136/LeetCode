def ReverseString(s):
    words = s.split()
    ans = ''

    for word in words[::-1]:
        ans+= word + ' '
    return ans.strip()

if __name__ == "__main__":
    s="The sky is blue"   
    print(ReverseString(s))