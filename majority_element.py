def main():
    nums=[3,2,3]
    count=0
    final_res=None

    for num in nums:

        if count==0:
            final_res=num

        if num!=final_res:
            count+=1
        else:
            count-=1    
    print(final_res)
    return(final_res)

if __name__ == "__main__":
    main()

