import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()

n,m,k = map(int,input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int,input().split())))


parti = []
cnt = 11
for _ in range(m):
    x,y = map(int,input().split())
    parti.append([x-1,y-1,cnt])
    maze[x-1][y-1] = cnt
    cnt +=1 

exitX, exitY = map(int,input().split())
exitX, exitY = exitX-1, exitY-1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

maze[exitX][exitY] = -1
ans = 0
def distance(x1,y1,x2,y2):
    return abs(x1-x2)+ abs(y1-y2)

def movedir(maze,parti,exitX,exitY):
    global ans
    removes =[]
    m = len(parti)
    a = 0
    for i in range(m):
        x,y,cnt = parti[i]
        #동남
        if x > exitX and y > exitY : 
            if maze[x-1][y] == 0 or maze[x-1][y] > 10:
                maze[x-1][y] += cnt
                maze[x][y] = 0
                parti[i] = [x-1,y,cnt]
                a +=1
                continue
            elif maze[x][y-1] == 0 or maze[x][y-1] > 10 :
                maze[x][y-1] += cnt
                maze[x][y] = 0
                parti[i] = [x,y-1,cnt]
                a +=1
        #정남
        elif x > exitX and y == exitY :
            if maze[x-1][y] == -1 :
                maze[x][y] = 0
                removes.append([x,y,cnt])
                a +=1
                continue
            elif maze[x-1][y] == 0 or maze[x-1][y] > 10:
                maze[x-1][y] += cnt
                maze[x][y] = 0
                parti[i] = [x-1,y,cnt]
                a +=1
        #서남
        elif x> exitX and y < exitY:
            if maze[x-1][y] == 0 or maze[x-1][y] > 10:
                maze[x-1][y] += cnt
                maze[x][y] = 0
                parti[i] = [x-1,y,cnt]
                a +=1
                continue
            elif maze[x][y+1] == 0 or maze[x][y+1] > 10:
                maze[x][y+1] += cnt
                maze[x][y] = 0
                parti[i] = [x,y+1,cnt]
                a +=1
        #정동
        elif x == exitX and y > exitY :
            if maze[x][y-1] == -1 :
                maze[x][y] = 0
                removes.append([x,y,cnt])
                a +=1
                continue
            elif maze[x][y-1] == 0 or maze[x][y-1] > 10:
                maze[x][y-1] += cnt
                maze[x][y] = 0
                parti[i] = [x,y-1,cnt]
                a +=1
        #정서
        elif x == exitX and y < exitY :
            if maze[x][y+1] == -1 :
                maze[x][y] = 0
                removes.append([x,y,cnt])
                a +=1
                continue
            elif maze[x][y+1] == 0 or maze[x][y+1] > 10 :
                maze[x][y+1] += cnt
                maze[x][y] = 0
                parti[i] = [x,y+1,cnt]
                a +=1
        #동북
        if x < exitX and y > exitY : 
            if maze[x+1][y] == 0 or maze[x+1][y] > 10 :
                maze[x+1][y] += cnt
                maze[x][y] = 0
                a +=1
                parti[i] = [x+1,y,cnt]
                continue
            elif maze[x][y-1] == 0 or maze[x][y-1] > 10:
                maze[x][y-1] += cnt
                maze[x][y] = 0
                parti[i] = [x,y-1,cnt]
                a +=1
        #정북
        elif x < exitX and y == exitY :
            if maze[x-1][y] == -1 :
                maze[x][y] = 0
                remove.append([x,y,cnt])
                a +=1
                continue
            elif maze[x+1][y] == 0 or  maze[x+1][y] > 10:
                maze[x+1][y] += cnt
                maze[x][y] = 0
                parti[i] = [x+1,y,cnt]
                a +=1
        #서북
        elif x < exitX and y < exitY:
            if maze[x+1][y] == 0 or maze[x+1][y] > 10:
                maze[x+1][y] += cnt
                maze[x][y] = 0
                parti[i] = [x+1,y,cnt]
                a +=1
                continue
            elif maze[x][y+1] == 0 or maze[x][y+1] > 10:
                maze[x][y+1] += cnt
                maze[x][y] = 0
                parti[i] = [x,y+1,cnt]
                a +=1
    if len(removes) > 0 :
        for aa,bb,cc in removes :
            parti.remove([aa,bb,cc])
    ans += a
    return parti,maze

def square(parti,exitX,exitY):
    global leftX, leftY
    dist = int(n+1)
    for i,j,cnt in parti :
        tmp = distance(i,j,exitX,exitY)
        if tmp < dist :
            dist = tmp
            if exitY == j:
                leftX = min(i,exitX)
                if exitY - dist + 1  > 0 :
                    leftY = exitY - dist 
                leftY = 0
            else :
                leftY = min(j,exitY)
                if exitX - dist + 1 > 0 :
                    leftX = exitX - dist 
                leftX = 0
        if tmp == dist:
            if leftX > i or leftY > j :
                if exitY == j:
                    leftX = min(i,exitX)
                    if exitY - dist + 1  > 0 :
                        leftY = exitY - dist 
                    leftY = 0
                else :
                    leftY = min(j,exitY)
                    if exitX - dist + 1 > 0 :
                        leftX = exitX - dist 
                    leftX = 0
    return dist+1, leftX, leftY

def rotation(parti,dist, leftX, leftY):
    global exitX,exitY
    tmp = [[0]*dist for _ in range(dist)]
    for i in range(leftX,dist+leftX):
        for j in range(leftY,dist+leftY):
            tmp[i-leftX][j-leftY] = maze[dist+leftX+leftY-j-1][i-leftX+leftY]
            if 0< tmp[i-leftX][j-leftY] < 10 :
                tmp[i-leftX][j-leftY] -= 1 
    for i in range(leftX,dist+leftX):
        for j in range(leftY,dist+leftY):
            maze[i][j] = tmp[i-leftX][j-leftY]
            if maze[i][j] == -1 :
                exitX,exitY = i,j
    return maze,exitX,exitY
                

for q in range(8):
    if len(parti) == 0 :
        break
    #1. 참가자 탈출구 쪽으로 이동
    parti,maze= movedir(maze,parti,exitX,exitY)
    # print("after move")
    # print(parti)
    # print(maze)
    # print('-----')
    #2. 회전
    dist, leftX, leftY = square(parti,exitX,exitY)
    # print("회전 좌상단 :",leftX, leftY)
    maze,exitX,exitY = rotation(parti,dist,leftX, leftY)
    parti = []
    for i in range(n):
        for j in range(n):
            if maze[i][j] > 10 :
                parti.append([i,j,maze[i][j]])
    # print("after rotation")
    # print(parti)
    # print(maze)
print(ans)
print(exitX+1,exitY+1)