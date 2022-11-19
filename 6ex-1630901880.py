class struc:
    def __init__(self):
        self.x = [[" "," "],[" "," "]]
    def hobb(self,Node_name):    
        if self.x[0][-1] != " ":
            self.x[0].append(" ")
            nin = False
        else:
            nin = True
        ck = 0
        if self.x[0][0] == " ":
            self.x[0][0] = "-"
        for i in range (len(self.x[0])):
            if i == len(self.x[0])- 1 and not nin:
                self.x.append([])
            while len(self.x[i]) < len(self.x[i-1]):
                self.x[i].append("0")
                if self.x[i][0] == "0":
                    self.x[i][0] = " "
        for i in range (len(self.x)):
            if self.x[0][i] == " " and ck == 0:
                    self.x[0][i] = Node_name
                    ck = 1
        for x in range (len(self.x[0])):
            if self.x[x][0] == " " and ck == 1:
                self.x[x][0] = Node_name
                self.x[x][1] = "0"
                ck = 0
    def matrix(self):
        print(len(self.x) * "")
        for i in range(len(self.x)):
            print(self.x[i])
    def conn(self,numm1,numm):
        if numm1 in self.x[0]  :
            node,nodenum = 0,0
            for i in range(len(self.x)):
                if numm1 == self.x[0][i]:
                    node = i
                elif numm == self.x[0][i]:
                    nodenum = i
                self.x[node][node] = "1"
                self.x[node][node] = "1"
       
num=struc()
num.matrix()
num.hobb('A')
num.hobb('B')
num.hobb('C')
num.hobb('D')
num.hobb('E')
num.hobb('F')

num.conn('A','B')
num.conn('A','C')
num.conn('C','D')
num.conn('C','F')
num.conn('E','F')
