#!/usr/bin/env python

import os, pygame

fullscreen_mode=(pygame.HWSURFACE | pygame.FULLSCREEN | pygame.NOFRAME | pygame.DOUBLEBUF)
resizable_mode=(pygame.RESIZABLE | pygame.DOUBLEBUF)

def main():
    pygame.init()
    pygame.display.set_caption('screen test')
    screen=pygame.display.set_mode((640, 480), resizable_mode)

    background=pygame.Surface((256,192))
    background.convert()
    background.fill((255, 255, 255))

    font=pygame.font.Font(None, 36)
    text=font.render('this is a test', 1, (10, 10, 10))
    
    background.blit(text, (10,10))

    #    screen.blit(background, (0,0))
    pygame.transform.scale(background, screen.get_size(), screen)
    pygame.display.flip()

    frame_counter=0
    
    while True:
        frame_counter += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('shutting down...')
                pygame.quit()
                return 0
            if event.type == pygame.VIDEORESIZE:
                print('new screen size: %d, %d' % (event.w, event.h))
                screen=pygame.display.set_mode((event.w, event.h), resizable_mode)

        background.fill((255, 255, 255))
        text=font.render('frame count is %05d' % (frame_counter), True, (10, 10, 10))
        background.blit(text, (10,10))
        pygame.transform.scale(background, screen.get_size(), screen)
        pygame.display.flip()
    

    

if __name__ == '__main__':
    main()
