import random

# 초기화
memory = []
root = None
nameAry = ['콘말차', '삿포로 맥주', '아카페라 벤티 헤이즐넛', '레어치즈푸딩',
           '척오리지널 메가 사워', '요아정 요거트컵', '페퍼로니피자주먹밥', '널담 슈톨렌',
           '딸기마시멜로케이크', '버니공쥬 딸기뚱카롱', '고추잡채호빵', '체다 슈크림붕어스낵']
sellAry = [random.choice(nameAry) for _ in range(20)]

# TreeNode 클래스 선언
class TreeNode:
    def __init__(self):
        self.left = None  # 왼쪽 자식
        self.data = None  # 노드 데이터
        self.right = None # 오른쪽 자식

    def __str__(self):
        return f"TreeNode({self.data})"

# 전위 순회 함수
def preorder(node):
    if node is None:
        return
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)



node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
        node = TreeNode()
        node.data = name
    
current = root
while True:
    if name < current.data:  # 현재 name이 노드 안 데이터보다 작으면 왼쪽
        if current.left is None:
            current.left = node
            break  # 왼쪽에 노드를 추가한 후 종료
        else:
            current = current.left  # 왼쪽 자식으로 내려감
    else:  # 오른쪽으로 보냄
        if current.right is None:
            current.right = node
            break  # 오른쪽에 노드를 추가한 후 종료
        else:
             current = current.right  # 오른쪽 자식으로 내려감


print('# 오늘 판매된 전체 물건(중복O, 정렬X) -->', sellAry)

# 메인 코드 부분
if __name__ == '__main__':

    # 사용자 입력에 따른 처리
    while True:
        select = input('확인(D)/ 중복없이확인(V)/ 종료(Q) --->>').upper()

        if select == 'D':
            sellAry.sort()
            print('# 오늘 판매된 전체 물건(중복O, 정렬O) -->', sellAry)
        elif select == 'V':
            sellProduct = list(set(sellAry))
            print('# 오늘 판매된 물품 종류(중복X) -->', sellProduct)
            print()  # 줄바꿈
        elif select == 'Q':
            break
        else:
            print('제대로 입력하세요')

    print('프로그램 종료')
