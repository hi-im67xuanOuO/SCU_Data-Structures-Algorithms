from collections import defaultdict 
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w])  #將新增的邊加入list中，這裡的u是起點，v是終點，w是該邊的權重
    def minDistance(self, distance, past): #取出距離最小的邊
        min = float("inf") #先初始化都為inf（最大）
        i = 0 
        for v in range(self.V):  #使用for迴圈判斷所有節點，v代表節點
            if distance[v] < min and past[v] == False: #如果distance比目前最小值短而且該點尚未被納入最短路徑中
                min = distance[v] #把最短路徑更新
                i = v #將 i 指定為最短邊的節點為何
        return i 
    def Dijkstra(self, s): 
        distance = { i:float("inf") for i in range(self.V) } #初始化所有的距離為inf（最大）
        past = { i:False for i in range(self.V) } #這個dict用來判斷是否被走訪過
        ans = { str(i):0 for i in range(self.V) } #這個dict用來儲存我們的答案
        distance[s] = 0 #起點到起點的距離為0
        i = self.V # i 是總共有多少個節點
        while i-1>=0: #因為 i 個點，最後要選出 i-1 個邊，所以當還沒選完 i-1 個邊，就要持續執行
            current = self.minDistance(distance,past) #跑出最新的最短邊
            past[current] = True #將該點納入最短路徑中
            i = i-1 #待尋找的邊數少一個
            v = 0 #v拿來儲存從起點到該點總共的路徑長
            while v<=self.V-1:  #使用while迴圈判斷目前各個節點的到起點的路徑長
                if self.graph[current][v]>0 and past[v]==False and distance[v]>distance[current]+self.graph[current][v]: #當該節點未被走過而且路徑長比原本未納入新節點時的路徑長還大
                    distance[v]=distance[current]+self.graph[current][v] 
                    ans[str(v)] = distance[v] #更新新的路徑長到答案中
                v+=1 #繼續計算下一個節點更新後的路徑長
        return ans
    def find(self,parent,i): #尋找該節點的parent為何
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])
    def union(self,parent,x,y): #將x與y節點的parent變成同一個（代表進入相同cycle中）
        parent[self.find(parent,x)] = parent[self.find(parent,y)] = self.find(parent,x)  
    def create(self,parent): #準備好要儲存parent的list
        node = 0
        while self.V>0: #這裡將parent先準備好，self.V為節點個數
            parent.append(node) #依序將節點append進入parent的list中
            node+=1
            self.V-=1
        return parent
    def Kruskal(self):
        i = 0
        ans = {}
        count = self.V #需要執行的次數為count-1
        self.graph = sorted(self.graph, key=lambda weight: weight[2]) #先將Adjacency List依照權重weight進行排序
        #因為weight是在我們addEdge時的第三個值，所以是在weight[2]的位子
        parent = []
        parent=self.create(parent)      
        while count>1: #count為尚須尋找的個數
            start,end,weight = self.graph[i] 
            i+=1
            x = self.find(parent,start) #找到start節點的parent為何
            y = self.find(parent,end) #找到end節點的parent為何 
            if x!= y: #如果兩者的parent不同（代表在不同cycle裡）
                ans[str("%d-%d" % (start,end))] = weight #將該邊加入ans中
                count-=1 #尚須尋找的個數減一
                self.union(parent,x,y) #將x與y兩點的parent變成同一個，代表他們已被納入同一個cycle中 
        return ans
