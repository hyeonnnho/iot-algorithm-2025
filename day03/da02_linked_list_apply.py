memory = [] 
head, prev, curr = None, None, None
dataArray = [['지민', '010-1111-1111'], ['정국', '010-2222-2222'], ['뷔', '010-3333-3333'], ['슈가', '010-4444-4444'], ['진', '010-5555-5555']]


class Node:
    def __init__(self):
        self.data = data
        self.link = None
    
    # def setLink(self, link):
    #     self.__link = link

    # def getData(self):
    #     return self.__data
    
    # def getLink(self):
    #     return self.__link

    
def printNode(start):
    curr = start
    if curr == None: return
    print(curr.data, end='->')
    while curr.link != None: # 현재 링크의 다음링크가 있는 동안
        curr = curr.link # 다음 노드를 가리킴
        if curr.link == None:
            print(curr.data, end=' ')
        else:
            print(curr.data, end='->')

    print() # 한 줄 내림

def makeSimpleLinkedList(namePhone):
    global memory, head, curr, prev
    printNode(head)
    node = Node()
    node.data = namePhone
    memory.append(node)
    if head == None:
        head = node
        return
    
    if head.data[0] > namePhone[0]:
        node.link = head
        head = node
        return
    
    curr = head
    while curr.link != None:
        prev = curr
        curr = curr.link
        if curr.data[0] > namePhone[0]:
            prev.link = node
            node.link = curr
            return
    
    curr.link = node

if __name__ == '__main__':
    for data in dataArray:
        makeSimpleLinkedList(data)
    printNode(head)