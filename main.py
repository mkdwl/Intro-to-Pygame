import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks()/1000)-start_time
    score_surf = test_font.render(f'{current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font("font\Pixeltype.ttf", 50)
game_active = True
start_time = 0

sky_surface = pygame.image.load('graphics\Sky.png').convert()
ground_surface = pygame.image.load('graphics\ground.png').convert()

# score_surf=test_font.render("My game",False,(64,64,64))
# score_rect=score_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('graphics\Fly\Fly1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load('Player\player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(bottomright=(600, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >=300:
                    player_gravity-=20
            
            if event.type ==pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE
                     


    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.display.update()
