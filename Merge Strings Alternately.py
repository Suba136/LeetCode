def main():
    word1= "abc"
    word2= "pqr"

    i = 0
    j = 0
    res = ''

    while i< len(word1) and j<len(word2):
        res += word1[i] + word2[j]
        i+=1 
        j+=1

    while i< len(word1):
        res+= word1[i]
        i+=1
    while j< len(word2):
        res+ word2[j]
        j+=1
    print(res)
    return res

if __name__ == "__main__":
    main()    
