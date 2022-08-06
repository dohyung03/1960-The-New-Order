from function import *

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pressed = True

        elif event.type == pygame.MOUSEBUTTONUP: # 마우스를 땠다면
            mx, my = pygame.mouse.get_pos()
            Return_check = mouse_target(StartButton_X, StartButton_Y, (StartButton_W, StartButton_H), (mx, my))
            if Return_check == True:
                print("체크")
            

    SCREEN.blit(img_StartButton, [StartButton_X, StartButton_Y])
    SCREEN.blit(start_text,(start_text_X,start_text_Y))

    pygame.display.update()