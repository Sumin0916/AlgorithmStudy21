"""
음료수 얼려 먹기

새로운 방법으로 구현해야만 한다.
"""

ice_tray = []

class PacMan():
    def __init__(self, array):
        self.y = 0
        self.x = 0
        self.max_row = len(array) - 1
        self.max_col = len(array[0]) - 1
        self.short_term_mem = [None, None]
        self.array = array
        self.direc_point = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ] 
    
    def navi_perimeter(self): # 주변을 탐색한 결과를 리스트 형식으로 반환 
        r = self.y
        c = self.x
        peri_lst = [None * 4]
        search_point = [(r+1,c),(r,c+1),(r-1,c),(r,c-1)] # 아래 오른쪽 위 왼쪽
    
        for i in range(4):
            t_col = search_point[i][0]
            t_row = search_point[i][1]
            if 0 <= t_col <= self.max_row and 0 <= t_row <= self.max_col:
                if self.array[t_row][t_col] == 1:
                    peri_lst[i] = 1
                
                else:
                    peri_lst[i] = 0

        return peri_lst
    def set_start(self, row, col):
        self.y = row
        self.x = col

    def move(self): # 지점에서 한 칸 움직이기
        num_move = 0
        col = self.x
        row = self.y
        self.array[row][col] = 0
        peri_lst = self.navi_perimeter()
        
        for i in range(4):
            if peri_lst[i] == 1:
                self.y += self.direc_point[i][0]
                self.x += self.direc_point[i][1]
                num_move = 1
                return 1
        
        if num_move == 0:
            self.set_start(self.short_term_mem[0],self.short_term_mem[1])
            num_move = self.move() # 뒤로 돌아가기

            if num_move == 0: # 뒤로가서도 움직임 횟수가 0이면 0반환
                return 0

    def record_loc(self):
        self.short_term_mem = [self.y, self.x]


n, m = map(int, input().split())

for _ in range(n):
    ice_tray.append(list(map(int, input())))

pacman = PacMan(ice_tray)

for i in range(n):
    for j in range(m):
        if ice_tray[i][j] == 1:
            pacman.set_start(i, j)
            pacman.move()
            