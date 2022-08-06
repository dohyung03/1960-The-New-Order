from variable import *

def check_point_in_rect(x,y, rect): # 사각형 체크
    if rect.top < y and rect.bottom > y:
        if rect.left < x and rect.right > x:
            return True
    return False

def mouse_target(x, y, size, pos): # 마우스 충돌감지
    global StartButton_W, StartButton_H

    Rect = pygame.Rect(x, y, size[0], size[1]) #감지할 사각형 만들기

    print(pos[0],pos[1])
    
    if check_point_in_rect(pos[0],pos[1], Rect):
            return True

    return -1