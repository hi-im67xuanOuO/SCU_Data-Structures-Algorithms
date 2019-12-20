from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list)       
    def addEdge(self,u,v): 
        self.graph[u].append(v)   
    def started(self,s,total,past):
        total.append(s) #先將起點加入queue中
        past.append(s) #先將起點加入past中
        return total,past 
    def existed(self,current,nodes,past,total):
        for w in nodes: #使用for迴圈開始走訪
            if w not in past: #如果未曾走訪過該點
                total.append(w) #將該點加入queue跟past中（以作為之後走訪的順序）
                past.append(w)
        return total,past
    def BFS(self, s): 
        graph = self.graph #先導入我們指定的圖
        total=[]#total要存放所有的節點 
        past = [] # past要存放已經走訪過的點
        ans =[] #這裏存放走訪的順序
        total,past=self.started(s,past,total)
        times = len(set(self.graph))#程式碼總共需要執行的次數，也就是總共多少個節點
        for i in range(times):
            if total:
                current = total.pop(0) #BFS是從第一個queue中的最前面開始跑
                nodes = graph[current] #從graph中找出所有該點會連結到的點
                total,past=self.existed(current,nodes,past,total)
                if current is not None: 
                    ans.append(current) #將目前走訪的點加入ans中
        return ans
    def DFS(self, s): 
        graph = self.graph
        total=[]#total要存放所有的節點 
        past = [] # past要存放已經走訪過的點
        ans =[] #這裏存放走訪的順序
        total,past=self.started(s,past,total)
        times = len(set(self.graph)) #程式碼總共需要執行的次數，也就是總共多少個節點
        for i in range(times):
            if total:
                current = total.pop() # DFS是從stack中的最後一個開始跑
                nodes = graph[current] #從graph中找出所有該點會連結到的點
                total,past=self.existed(current,nodes,past,total)
                if current is not None: 
                    ans.append(current) #最後將目前走訪的點加入ans中
        return ans
