

class DisjointSet:

    def __init__(self, numElems):
        self.vals = [-1] * numElems

    def find(self, elem):
        if self.vals[elem] < 0:
            return elem
        self.vals[elem] = self.find(self.vals[elem])
        return self.vals[elem]

    def size(self, elem):
        return -self.vals[self.find(elem)]

    def setUnion(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.vals[a] <= self.vals[b]:
                self.vals[a] += self.vals[b]
                self.vals[b] = a
            else:
                self.vals[b] += self.vals[a]
                self.vals[a] = b
            # return True
        # return False

    def getList(self):
        return self.vals
