import pygame
from constants import *
import player
import asteroid
import astroidfield
import shot
def main():
    pygame.init()
    #Draw the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))  
    dt = 0 
    clock = pygame.time.Clock() 
    #imported from constants.py
    player_start_x = SCREEN_WIDTH / 2
    player_start_y = SCREEN_HEIGHT / 2
    #Create the pygame groups and add the groups to a containers class variable on the Player class.
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroid.Asteroid.containers = (updateable,drawable,astroids)
    player.Player.containers = (updateable,drawable)
    astroidfield.AsteroidField.containers = (updateable)
    shot.shot.containers = (shots,drawable,updateable)
    player1 = player.Player(player_start_x,player_start_y)
    astroidfld = astroidfield.AsteroidField()
    print("Starting asteroids!")
    print(f"""
          Screen width: {SCREEN_WIDTH}
          Screen height: {SCREEN_HEIGHT} """)
    #Game loop.
    while True:
        #Handle user hitting the x button (exiting the game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Fill in the background on frame refresh with a black screen.
        screen.fill("black")

        for object in updateable:
            object.update(dt)
        
        for object in astroids:
            if object.collision(player1):
                print("Game over!")
                return
        for object in astroids:
            for bullet in shots:
                if object.collision(bullet):
                    object.split()
                    bullet.kill()
        
        for object in drawable:
            object.draw(screen)
            
        #Frame update.
        pygame.display.flip()
        #Set FPS to 60. DT is the detla time (time since last refresh) in seconds.
        dt = clock.tick(60) / 1000
    
        
    
if __name__ == "__main__":
    main()