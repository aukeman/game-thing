#!/usr/bin/env python

import os, pygame

def main():
    pygame.init()
    pygame.display.set_caption('screen test')
    screen=pygame.display.set_mode((640, 480))

    background=pygame.Surface((256,192))
    background.convert()
    background.fill((255, 255, 255))

    font=pygame.font.Font(None, 36)
    text=font.render('this is a test', 1, (10, 10, 10))
    
    background.blit(text, (10,10))

    #    screen.blit(background, (0,0))
    pygame.transform.scale(background, screen.get_size(), screen)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('shutting down...')
                pygame.quit()
                return 0

        

if __name__ == '__main__':
    main()
