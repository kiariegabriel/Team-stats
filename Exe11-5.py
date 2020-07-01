d=dict()
for i in range(5):
	l=list()
	team=input('Enter team: ')
	l.append(eval(input('Enter winning: ')))
	l.append(eval(input('Enter losses: ')))
	d[team]=l
print(d)t=input(',Enter a team name: ')
x=sum(d[t])
p=(d[t][0])*100/x
print(p,'% winning rate',sep='')
wins=[c[0] for c in d.values()]
print(wins)
w_r=[c[0] for c in d.items() if c[1][0]>=60]
print(w_r)