# Basic arcade shooter game

# Import libraries
import arcade
import random
import os, sys

# Constants
global SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCALING
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade Space Shooter"
SCALING = 0.1

global SpaceShooter
class SpaceShooter(arcade.Window):
    """Space Shooter side scroller game.
    Player starts on the left, enemies appear on the right.
    Player can move anywhere, but not off screen.
    Enemies fly to the left at variable speed.
    Collisions or player hitting the quit button end the game.
    Keys to move the jet: Upward arrow, Downward arrow, Left arrow and Right arrow. """
    global self, width, height, title
    def __init__(self, width, height, title):
        """Initialize the game"""
        

        super().__init__(width, height, title)

        # Set up the empty sprite lists
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

    
    
    def setup(self):
        """Get the game ready to play"""
        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Set up the player
        self.player = arcade.Sprite("C:/img_retro_crusade_bg/imgjetrev.png", SCALING)
        self.player.center_y = self.height / 2
        self.player.left = 10
        self.all_sprites.append(self.player)


        # Spawn a new enemy every 0.25 seconds
        arcade.schedule(self.add_enemy, 0.5)

        # Spawn a new cloud every second
        arcade.schedule(self.add_cloud, 2.0)


    global delta_time, sprite, enemies_list
    def on_update(self, delta_time):
        """Update the positions and statuses of all game objects
           If paused, do nothing

           Arguments:
           delta_time {float} -- Time since the last update"""

        
         # Did you hit anything? If so, end the game
        if self.player.collides_with_list(self.enemies_list):
             arcade.close_window()

         # Update everything
        
        for sprite in self.all_sprites:
                 sprite.center_x = int( sprite.center_x + sprite.change_x * delta_time )
                 sprite.center_y = int( sprite.center_y + sprite.change_y * delta_time )

        # Remove if off the screen
        if sprite.right < 0:
                 sprite.remove_from_sprite_lists()


        self.all_sprites.update()


         # Keep the player on screen
        if self.player.top > self.height:
             self.player.top = self.height
        if self.player.right > self.width:
             self.player.right = self.width
        if self.player.bottom < 0:
             self.player.bottom = 0
        if self.player.left < 0:
             self.player.left = 0





    global symbol, modifiers
    def on_key_press(self, symbol: int, modifiers: int):
        """Handle user keyboard input
           Q: Quit the game
           P: Pause/Unpause the game
           I/J/K/L: Move Up, Left, Down, Right
           Arrows: Move Up, Left, Down, Right

           Arguments:
                   symbol {int} -- Which key was pressed
                   modifiers {int} -- Which modifiers were pressed"""

        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        #if symbol == arcade.key.P:
            #self.paused = not self.paused
            

        if symbol == arcade.key.I or symbol == arcade.key.UP:
            self.player.change_y = 5

        if symbol == arcade.key.K or symbol == arcade.key.DOWN:
            self.player.change_y = -5

        if symbol == arcade.key.J or symbol == arcade.key.LEFT:
            self.player.change_x = -5

        if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
            self.player.change_x = 5



    def on_draw(self):
        """Draw all game objects"""
        arcade.start_render()
        self.all_sprites.draw()



    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

           Arguments:
           symbol {int} -- Which key was pressed
           modifiers {int} -- Which modifiers were pressed
        """
        if (
            symbol == arcade.key.I
            or symbol == arcade.key.K
            or symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0

        if (
            symbol == arcade.key.J
            or symbol == arcade.key.L
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0



    def add_cloud(self, delta_time: float):
            """Adds a new cloud to the screen. Arguments: Delta_time{float} -- How much time has passed since the last call"""

            # First, create the new cloud sprite
            cloud= FlyingSprite("C:/img_retro_crusade_bg/imgcloud.png", 0.5)

            # Set its position to a random height and off screen right
            cloud.left = random.randint(self.width, self.width + 80 )
            cloud.top = random.randint(10, self.height - 10)

            # Set its speed to a random speed heading left
            cloud.velocity = (random.randint(-5, -2),0)

            # Add it to the enemies list
            self.clouds_list.append(cloud)
            self.all_sprites.append(cloud)



    def add_enemy(self, delta_time: float):
            """Adds a new enemy to the screen. Arguments: delta_time {float} -- How much time has passed since the last call"""

            # First, create the new enemy sprite
            enemy = FlyingSprite("C:/img_retro_crusade_bg/imgmissile.png", 0.08)

            # Set its position to a random height and off screen right
            enemy.left = random.randint(self.width, self.width + 80)
            enemy.top = random.randint(10, self.height - 10)

            # Set its speed to a random speed heading left
            enemy.velocity = (random.randint(-20, -5), 0)

            # Add it to the enemies list
            self.enemies_list.append(enemy)
            self.all_sprites.append(enemy)

            self.on_update(delta_time)





global FlyingSprite    

class FlyingSprite(arcade.Sprite):
        """Base class for all flying sprites. Flying sprites include enemies and clouds"""

        def update(self):

            
            # Move the sprite
            super().update()

            # Remove if off the screen
            if self.right < 0:
                  self.remove_from_sprite_lists()


        



    
def main():
    """MAIN METHOD"""
    global game, arcade
    game= SpaceShooter(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    
    main()

    
