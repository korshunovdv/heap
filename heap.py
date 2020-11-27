class Heap():

    def __init__(self):
        self.data = []

    def heapyfu(self):
        for i in range(len(self.data) - 1, -1, -1):
            self.sift_down(i)

    def heappush(self, x):
        self.data.append(x)
        self.sift_up(len(self.data) - 1)

    def heappop(self, i=0):
        self.data[i], self.data[-1] = self.data[-1], self.data[i]
        res = self.data.pop()
        self.sift_up(i)
        self.sift_down(i)
        return res

    def sift_up(self, i):
        if i == 0:
            return
        parent = (i - 1) // 2
        if self.data[parent] > self.data[i]:
            self.data[parent], self.data[i] = self.data[i], self.data[parent]
            self.sift_up(parent)

    def sift_down(self, i):
        child1 = i * 2 + 1
        child2 = i * 2 + 2
        if child1 >= len(self.data):
            return
        if child2 >= len(self.data):
            child_min = child1
        else:
            child_min = (
                child1 if self.data[child1] < self.data[child2] else child2
            )
        if self.data[child_min] < self.data[i]:
            self.data[child_min], self.data[i] = (
                self.data[i], self.data[child_min]
            )
            self.sift_down(child_min)


if __name__ == '__main__':
    arr = [4, 6, 7, 8, 9, 1, 10, 3, 5, 2]
    heap = Heap()
    heap.data = arr
    heap.heapyfu()
    for i in range(len(heap.data)):
        print(heap.heappop())


