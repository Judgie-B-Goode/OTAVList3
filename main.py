import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((1080, 1920))
    pygame.display.set_caption("OTAV PLAYLIST")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Proxima Nova', 32, bold=True)
    current_clip_header_text = font.render("CURRENT CLIP:", True, pygame.Color("black"))
    time_remaining_header_text = font.render("TIME REMAINING:", True, pygame.Color("black"))
    next_live_clip_text = font.render("NEXT LIVE CLIP IN:", True, pygame.Color("red"))
	  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("#656565")
        pygame.draw.rect(screen,"#bebebe",(5,5,520,100))#CURRENT CLIP FRAME
        pygame.draw.rect(screen,"#9E9D9D",(10,10,510,90))#CURRENT CLIP INSIDE
        pygame.draw.rect(screen,"#bebebe",(555,5,520,100))#CURRENT CLIP TIME REMAINING FRAME
        pygame.draw.rect(screen,"#9E9D9D",(560,10,510,90))#CURRENT CLIP TIME REMAINING INSIDE
        pygame.draw.rect(screen,"#F8B9C3",(5,110,1070,40))#NEXT LIVE FRAME
        pygame.draw.rect(screen,"#F49DAA",(8,113,1064,34))#NEXT LIVE FRAME
        screen.blit(current_clip_header_text, (15,15))#CURRENT CLIP
        screen.blit(time_remaining_header_text, (560,10))
        screen.blit(next_live_clip_text, (10, 110))
        for x in range (155,5000, 45):
            pygame.draw.rect(screen,"#adafae", (5,x,1070,40))
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()