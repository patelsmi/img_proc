import pygame, sys
from PIL import Image

pygame.init()

def displayImage( screen, px, topleft):
     screen.blit(px, px.get_rect())
     if topleft:
         pygame.draw.rect( screen, (128,128,128), pygame.Rect(topleft[0], topleft[1], pygame.mouse.get_pos()[0] - topleft[0], pygame.mouse.get_pos()[1] - topleft[1]))
     pygame.display.flip()

def setup(path):
     px = pygame.image.load(path)
     screen = pygame.display.set_mode( px.get_rect()[2:] )
     screen.blit(px, px.get_rect())
     pygame.display.flip()
     return screen, px

def mainLoop(screen, px):
     topleft = None
     bottomright = None
     n=0
     while n!=1:
         for event in pygame.event.get():
             if event.type == pygame.MOUSEBUTTONUP:
                 if not topleft:
                     topleft = event.pos
                 else:
                     bottomright = event.pos
                     n=1
         displayImage(screen, px, topleft)
     return ( topleft + bottomright )

def img_calibrate(input_loc):
     screen, px = setup(input_loc)
     left, upper, right, lower = mainLoop(screen, px)
     im = Image.open(input_loc)
     im = im.crop(( left, upper, right, lower))
     pygame.display.quit()
     pix = im.load()
     im_w,im_h = im.size

     avg_r = 0
     avg_g = 0
     avg_b = 0
     for h in xrange(im_h):
         for w in xrange(im_w):
             r,g,b = pix[w,h]
             avg_r += r
             avg_g += g
             avg_b += b
     cnt = im_h * im_w
     avg_r = avg_r/cnt
     avg_g = avg_g/cnt
     avg_b = avg_b/cnt
     #print "R=%s\nG=%s\nB=%s" % (str(avg_r), str(avg_g), str(avg_b))
     return (avg_r,avg_g,avg_b)


