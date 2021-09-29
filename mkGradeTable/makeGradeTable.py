### # 가상의 성적표.csv 만들기
#### - 이름 리스트 만들기

# 아래의 사이트 에서 가장 흔한 보통 남자아이의 이름을 복사해옮
# https://www.ef.com/wwen/english-resources/english-names/

names = '''1	Oliver	Jake	Noah	James
2	Jack	Connor	Liam	John
3	Harry	Callum	Mason	Robert
4	Jacob	Jacob	Jacob	Michael
5	Charlie	Kyle	William	William
6	Thomas	Joe	Ethan	David
7	George	Reece	Michael	Richard
8	Oscar	Rhys	Alexander	Joseph
9	James	Charlie	James	Charles
10	William	Damian	Daniel	Thomas'''

print(names)

toList = names.replace('\n', '\t').split('\t')

for name in toList:
    if name.isdigit():
        toList.remove(name)

toList = tuple(set(toList))

print( toList, len( toList ) )

#### - 랜덤으로 성적표 리스트 만들기

# 위에서 구한 names tuple 를 이용한 무작위 성적 List 만들기 
import random

table = []
line = []
studentsCount = 20
for count, name in zip(range( studentsCount ), toList):
    line = []
    line.append( name )
    for grade in range(5):
        line.append(str(random.randint( 70, 101 )))
    table.append( line )

print( table )

#### - 성적표 csv 파일 형식의 데이터로 만들기

csvFormat = 'name,math,science,korean,english,history\n'
for line in table:
    csvFormat += (','.join(line) + '\n')

print( csvFormat )

#### - 만든 데이터 csv 파일로 저장하고 확인해보기

f = open( 'gradeTable.csv', 'w')
f.write(csvFormat)
f.close()

f = open('gradeTable.csv')
print( f.read() )
f.close()