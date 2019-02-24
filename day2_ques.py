#hackerrnk basic question
#https://www.hackerrank.com/challenges/30-conditional-statements/problem


#my_solution

if __name__ == '__main__':
    N = int(input())
    if N%2!=0:
        print('Weird')
    else:
        if N>=2 and N<=5:
            print('Not Weird')
        elif N>=6 and N<=20:
            print('Weird')
        elif N>20:
            print("Not Weird")

