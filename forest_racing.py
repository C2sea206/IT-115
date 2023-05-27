import random


stage = codebug_tether.CodeBug()

# Green background with the walls disabled to allow objects to leave the screen for the game
stage.set_background_color("green")
stage.disable_all_walls()

# Create the road where the objects will be placed
road = codesters.Rectangle(0, 0, 400, 500, "grey")

# Put the speed up and score text
speed_text = codesters.Text("Press up to speed up!", 0, 0, "pink")
score_text = codesters.Text("Score: 0", 150, 220, "pink")

# Create player object the car
player = codesters.Sprite("car2", 0, -200)
player.set_size(0.5)

# Created two empty arrays
trees = []
obstacles = []

# Integer variables score and speed
score = 0
speed = -5

# Boolean variable which checks the game state of the program
game_over = False

# Function for random trees
def create_scenery():
    # Iterates 10 times
    for row in range(10):
        # Pick a random number
        tree_num = random.randint(1, 7)
        # Make a choice left or right side of the edge
        side = random.choice([-1, 1])

        # Creation of the tree object and size of the tree
        tree = codesters.Sprite("pinetree{}".format(tree_num), 230 * side, 250 - row * 50)
        tree.set_size(0.3)
        # Adds it to the empty array list
        trees.append(tree)

    # Iterate through the populated list
    for tree in trees:
        tree.set_y_speed(speed)

# Call the function above
create_scenery()

# Function to increase speed
def speed_up():
    # With global speed, we can make the car speed up
    global speed

    # Increase the speed with the logic test
    if speed > -15:
        speed -= 1

    # Once reached a certain speed, the text will clear
    if speed < -8:
        speed_text.hide()

stage.event_key("up", speed_up)

# Function for the brake
def brake():
    global speed
    # Slow down
    if speed < -4:
        speed += 1
    # Hide the label when slowing down enough
    if speed >= -8:
        speed_text.show()

stage.event_key("down", brake)

# Add event to move object left by defining the function
def left():
    player.move_left(10)

stage.event_key("left", left)

# Move player object to right
def right():
    player.move_right(10)

stage.event_key("right", right)

# Creating obstacles for the player to dodge
def create_obstacle():
    # Randomly choose between the options in image
    image = random.choice(["car1", "pollution"])

    # Place obstacle on set x and y axis
    sprite = codesters.Sprite(image, random.randint(-180, 180), 350)
    sprite.set_size(0.5)

    # Another car as obstacle appears on the screen
    if image == "car1":
        sprite.set_rotation(180)
        sprite.set_y_speed(-5 + speed)
    else:
        # Pollution
        sprite.set_y_speed(speed)
    obstacles.append(sprite)


# When collision occurs, change the game state to game over
def collision(player, hit_sprite):
    # Created the game over boolean and set it to false above line 29
    global speed, game_over

    # Show text game over when collision occurs and set speed to 0
    if hit_sprite in obstacles or hit_sprite in trees:
        speed = 0
        game_over = True  # Change the game state
        speed_text.show()
        speed_text.set_text("Game Over!")

        # Make the player car spin out on collision
        player.set_y_speed(-5)
        player.turn_left(1000)

player.event_collision(collision)

# Updating the score value on the screen
def update():
    global score
    # Calculate the score using absolute value
    if speed < -8:
        score += abs(speed + 7)
        score_text.set_text("Score: {}".format(score))

    # Set the speed of the trees the same as the player speed
    for tree in trees:
        tree.set_y_speed(speed)

        # Nested if condition
        if tree.get_y() < -300:
            tree.set_y(300)

    # Make the obstacles speed up according to player speed
    for obs in obstacles:
        # Speed up car1 or pollution
        if obs.get_image_name() == "car1":
            obs.set_y_speed(-5 + speed)
        else:
            obs.set_y_speed(speed)

        if obs.get_y() < -300:
            obstacles.remove(obs)

stage.event_interval(update, 0.1)


def main():
    # While loop checking the game state. While is not equal to True
    # If the game state is not overt, run the function to create the obstacles.
    while not game_over:
        create_obstacle()
        stage.wait(random.uniform(0.1, 1.5))


main()