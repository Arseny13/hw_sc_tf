N = int(input())
lang = [{input() for j in range(int(input()))} for i in range(N)]
all, some = set.intersection(*lang), set.union(*lang)
print(len(all), *sorted(all), sep='\n')
print(len(some), *sorted(some), sep='\n')
