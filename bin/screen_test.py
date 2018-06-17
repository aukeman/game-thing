#!/usr/bin/env python

import os, pygame, gc

fullscreen_mode=(pygame.HWSURFACE | pygame.FULLSCREEN | pygame.NOFRAME | pygame.DOUBLEBUF)
resizable_mode=(pygame.HWSURFACE | pygame.RESIZABLE | pygame.DOUBLEBUF)

screen_mode=fullscreen_mode

resolution=(256, 192)
#resolution=(640, 480)

def main():
    gc.disable()
    pygame.init()
    pygame.display.set_caption('screen test')
    screen=pygame.display.set_mode((640, 480), screen_mode)

    background=pygame.Surface(resolution)
    background.convert()
    background.fill((255, 255, 255))

    font=pygame.font.Font(None, 36)

    scroller=font.render('this is a test', True, (10, 10, 10))
    speed_pps=40.0
    position=float(resolution[0])
    
    #    screen.blit(background, (0,0))
    pygame.transform.scale(background, screen.get_size(), screen)
    pygame.display.flip()

    clock=pygame.time.Clock()
    
    while True:
        clock.tick_busy_loop(60.0)
        top_of_frame=pygame.time.get_ticks()

        if 17 < clock.get_time():
            print('last frame took %d ms at %d' % (clock.get_time(), pygame.time.get_ticks()))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('shutting down...')
                pygame.quit()
                return 0
            elif event.type == pygame.VIDEORESIZE:
                print('new screen size: %d, %d' % (event.w, event.h))
                screen=pygame.display.set_mode((event.w, event.h), screen_mode)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and bool(event.mod & pygame.KMOD_ALT):
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        background.fill((255, 255, 255))
        text=font.render('Frame Rate is %4.1f' % (clock.get_fps()), True, (10, 10, 10))
#        text=font.render('Frame Time is %3.2f ms' % (clock.get_rawtime()), True, (10, 10, 10))
        background.blit(text, (10,10))

        position = position-(speed_pps*clock.get_time()/1000.0)
        if position < -scroller.get_width():
            position = float(resolution[0])
        background.blit(scroller, (int(position),100))
        
        pygame.transform.scale(background, screen.get_size(), screen)
        pygame.display.flip()
    
        gc.collect()

        # sleep up until near the end of the frame,
        # then let the busy loop take over until the end of the frame.
        # this way the process doesn't spend most of its time in a busy loop
        frame_time_elapsed=pygame.time.get_ticks() - top_of_frame
        if ( frame_time_elapsed < 14):
            pygame.time.wait( (14-frame_time_elapsed) )
        
if __name__ == '__main__':
    main()
