import statistics
num12=int(input())
str1=list(map(int,input().split()))[:num12]
print(statistics.median(str1))
