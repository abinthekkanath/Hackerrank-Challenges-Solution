#!/bin/python3


# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    cnt=0
    c=s[0]
    for i in range(1,int(len(s))):
        if c != s[i]:
            c=s[i]
        else :
            cnt+=1

    return cnt

        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
