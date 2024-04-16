#코드트리 고대문명유적탐사
import sys
import copy
from collections import deque 
input = lambda : sys.stdin.readline().strip()

k, m = map(int,input().split())
Map = []
for _ in range(5):
    Map.append(list( map(int,input().split())))

new = list(map(int,input().split()))


def rotate(tmp):
    rotated = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            rotated[j][2 - i] = tmp[i][j]
    return rotated

def move(startX, startY):
    tmp = [row[startY:startY+3] for row in newMap[startX:startX+3]]
    rotated = rotate(tmp)
    for i in range(startX,startX+3):
        for j in range(startY,startY+3):
            newMap[i][j] = rotated[i - startX][j - startY]
    
    return newMap

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(i,j,num,visited):
    changelist = []
    queue = deque()
    queue.append((i,j))
    changelist.append([i,j])
    visited[i][j] = 1
    cnt = 1
    while queue :
        x,y = queue.popleft()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < 5 and 0<= ny < 5 and visited[nx][ny] == 0 and newMap[nx][ny] == num:
                queue.append((nx,ny))
                changelist.append([nx,ny])
                visited[nx][ny] = 1
                cnt += 1
    if len(changelist) >=3 :
        return changelist
    return []

def getting(newMap, values,angle,nextangle):
    global nextMap
    gett = []
    visited = [[0]*5 for _ in range(5)]
    for a in range(5):
        for b in range(5):
            if not visited[a][b] :
                changelist = BFS(a,b,newMap[a][b],visited)
                
                if len(changelist) >= 3 :
                    gett += changelist

    if len(gett) > len(values) :
        values = gett
        nextMap = copy.deepcopy(newMap)
        nextI,nextJ,nextangle = i,j,angle
    elif len(gett) == len(values) :
        if nextangle > angle :
            values = gett
            nextMap = copy.deepcopy(newMap)
            nextI,nextJ,nextangle = i,j,angle
    
    return nextMap,values



for K in range(k):
    # print(K,"번째 실행 ing ----")
    ans = 0
    nextangle = 360
    values = []
    # print("1. beginning Map ")
    # for q in range(5):
    #     print(Map[q])

    for i in range(3):
        for j in range(3):
            newMap = copy.deepcopy(Map)
            for angle in range(90,271,90): # 회전 각도
                
                # print("now i,j, angle :",i,j,angle)
                # print("1. move before")
                # for q in range(5):
                #     print(newMap[q])

                newMap = move(i, j)

                # print("2. move after")
                # for q in range(5):
                #     print(newMap[q])

                nextMap, values = getting(newMap,values,angle,nextangle)


    # print("3. get relics")
    # for q in range(5):
    #     print(nextMap[q])

    values.sort(key= lambda x : (x[1],-x[0]))
    if len(values) == 0:
        sys.exit()
    ans += len(values)

    for i,j in values :
        nextMap[i][j] = new[0]
        del new[0]
    # print("left new relics: ",new)

    # print("5. change relics")
    # for q in range(5):
    #     print(nextMap[q])


    while len(values) >= 3 :    
        newMap = copy.deepcopy(nextMap)
        values = []
        nextMap, values = getting(newMap,values,angle,nextangle)
        values.sort(key= lambda x : (x[1],-x[0]))
        ans += len(values)
        # print("now values :", values)
        
        for i,j in values :
            # if len(new) == 0 :
            #     sys.exit()
            nextMap[i][j] = new[0]
            del new[0]
        # print("6. repeat getting relics")
        # for q in range(5):
        #     print(nextMap[q])

    # print("left new relics: ",new)
    # for q in range(5):
    #     print(nextMap[q])
    Map = copy.deepcopy(nextMap)

    print(ans,end =' ')