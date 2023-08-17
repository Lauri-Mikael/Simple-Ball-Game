import pygame
import time
import math
import os

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 1280
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Goal Scorer Game")

# Total played times
times = 0

# Load the images
assets_folder = "assets"
start_screen_image = pygame.image.load(os.path.join(assets_folder, "start.png"))
main_screen_image = pygame.image.load(os.path.join(assets_folder, "game_field.png"))
winner_screen_image = pygame.image.load(os.path.join(assets_folder, "winner.png"))
ball_image = pygame.image.load(os.path.join(assets_folder, "ball.gif"))
trave1_image = pygame.image.load(os.path.join(assets_folder, "trave1.gif"))
trave2_image = pygame.image.load(os.path.join(assets_folder, "trave2.gif"))
leftchar_image = pygame.image.load(os.path.join(assets_folder, "LeftChar.gif"))
leftchar_kick1_image = pygame.image.load(os.path.join(assets_folder, "LeftChar_kick1.gif"))
leftchar_kick2_image = pygame.image.load(os.path.join(assets_folder, "LeftChar_kick2.gif"))
rightchar_image = pygame.image.load(os.path.join(assets_folder, "RightChar.gif"))
rightchar_kick1_image = pygame.image.load(os.path.join(assets_folder, "RightChar_kick1.gif"))
rightchar_kick2_image = pygame.image.load(os.path.join(assets_folder, "RightChar_kick2.gif"))


# Define screen durations in seconds
start_screen_duration = 3
main_screen_duration = 10
winner_screen_duration = 5
action_duration = 2600

# Define colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
winnercolor = (255, 170, 0)
team2color = (255, 70, 0)
purple = (128, 0, 128)
timecolor = (200, 20, 20)
green = (0, 255, 0)

# Define font
fontsize = 108
fontpath = "assets/arialbd.ttf"

# Define initial scores and timer
team1_score = 0
team2_score = 0
team1_current_score = 0
team2_current_score = 0
started_time = 0

# Initial values
leftchar_position = (180, 600)
rightchar_position = (1050, 600)
curve_height = 400  # Adjust the curve height as needed

# Define states as initial ones
statelist = [0, 0, [230, 650], [1030, 650]]

# Function to display the main screen
def display(_statelist, times):
    display_main_screen(times)
    display_moving_objects(_statelist)
    pygame.display.flip() 

# Function to display the start screen
def display_start_screen(team1, team2):
    scaled_image = pygame.transform.scale(start_screen_image, (window_width, window_height))
    window.blit(scaled_image, (0, 0))

    # Display Team 1 Name
    font = pygame.font.Font(fontpath, fontsize)
    text = font.render(str(team1), True, blue)
    window.blit(text, (window_width // 4 - text.get_width() // 2, (window_height - fontsize) // 2))

    # Display Team 2 Name
    font = pygame.font.Font(fontpath, fontsize)
    text = font.render(str(team2), True, red)
    window.blit(text, (window_width // 4 * 3 - text.get_width() // 2, (window_height - fontsize)  // 2))

    pygame.display.flip()
    time.sleep(start_screen_duration)

# Function to display moving objects
def display_moving_objects(statelist):

    # Draw Characters
    if statelist[0] == 0:
        window.blit(leftchar_image, leftchar_position)
    elif statelist[0] == 1:
        window.blit(leftchar_kick1_image, leftchar_position)
    elif statelist[0] == 2:
        window.blit(leftchar_kick2_image, leftchar_position)

    if statelist[1] == 0:
        window.blit(rightchar_image, rightchar_position)
    elif statelist[1] == 1:
        window.blit(rightchar_kick1_image, rightchar_position)
    elif statelist[1] == 2:
        window.blit(rightchar_kick2_image, rightchar_position)

    # Draw Balls
    ballleft_x = statelist[2][0]
    ballleft_y = statelist[2][1]
    window.blit(ball_image, (ballleft_x, ballleft_y))

    ballright_x = statelist[3][0]
    ballright_y = statelist[3][1]
    window.blit(ball_image, (ballright_x, ballright_y))

# Function to display the main screen
def display_main_screen(times):

    # Draw background image
    scaled_image = pygame.transform.scale(main_screen_image, (window_width, window_height))
    window.blit(scaled_image, (0, 0))

    # Draw Traves
    window.blit(trave1_image, (20, 500))
    window.blit(trave2_image, (1150, 500))

    # Display Team 1 Name
    font = pygame.font.Font(fontpath, 36)
    text1 = font.render("TEAM 1 SCORE", True, purple)
    window.blit(text1, (100, 20))

    # Display Team 1 Score
    font = pygame.font.Font(fontpath, 36)
    text = font.render(str(team1_score), True, purple)
    window.blit(text, (90 + text1.get_width() // 2, 70))

    # Display Team 1 Current Score
    font = pygame.font.Font(fontpath, 36)
    text = font.render("+" + str(team1_current_score), True, green)
    window.blit(text, (80 + text1.get_width() // 2, 120))

    # Display Team 2 Name
    font = pygame.font.Font(fontpath, 36)
    text2 = font.render("TEAM 2 SCORE", True, team2color)
    window.blit(text2, (880, 20))

    # Display Team 2 Score
    font = pygame.font.Font(fontpath, 36)
    text = font.render(str(team2_score), True, team2color)
    window.blit(text, (1150 - text2.get_width() // 2, 70))

    # Display Team 2 Current Score
    font = pygame.font.Font(fontpath, 36)
    text = font.render("+" + str(team2_current_score), True, green)
    window.blit(text, (1140 - text2.get_width() // 2, 120))

    # Display Timer
    font = pygame.font.Font(fontpath, 36)
    text = font.render("TIME", True, timecolor)
    window.blit(text, (window_width // 2 - text.get_width() // 2, 20))

    # Display Timer Value
    font = pygame.font.Font(fontpath, 36)
    time = main_screen_duration + start_screen_duration + times * (start_screen_duration + main_screen_duration + winner_screen_duration) - (pygame.time.get_ticks() - started_time) // 1000
    text = font.render(str(time), True, timecolor)
    window.blit(text, (window_width // 2 - text.get_width() // 2, 70))

# Function to display the winner screen
def display_winner_screen(winner):
    scaled_image = pygame.transform.scale(winner_screen_image, (window_width, window_height))
    window.blit(scaled_image, (0, 0))

    # Display Winner Name
    font = pygame.font.Font(fontpath, fontsize)
    text = font.render(str(winner), True, winnercolor)
    window.blit(text, (window_width // 2 - text.get_width() // 2, (window_height - fontsize) // 2))

    pygame.display.flip()
    time.sleep(winner_screen_duration)

# Function to update the score
def update_score(team, score):
    if team == 1:
        global team1_score
        team1_score = score
    elif team == 2:
        global team2_score
        team2_score = score

    # Redraw the score text
    display_main_screen(times)

def update_current_score(team, score):
    if team == 1:
        global team1_current_score
        team1_current_score = score
    elif team == 2:
        global team2_current_score
        team2_current_score = score

    # Redraw the score text
    display_main_screen(times)

# Define custom events for keydowns
CUSTOM_EVENT1 = pygame.USEREVENT + 1
CUSTOM_EVENT5 = pygame.USEREVENT + 5
CUSTOM_EVENT10 = pygame.USEREVENT + 10
CUSTOM_EVENT11 = pygame.USEREVENT + 11
CUSTOM_EVENT51 = pygame.USEREVENT + 51
CUSTOM_EVENT101 = pygame.USEREVENT + 101
  
# Main game loop
def game_loop():
    while True:

        # Initialize values
        global times
        started_time = pygame.time.get_ticks()
        statelist = [0, 0, [230, 650], [1030, 650]]


        # Display start screen
        display_start_screen("Team 1", "Team 2")

        # Game loop
        running = True
        left_event_time = -1
        right_event_time = -1
        update_score_triggeredl = True
        update_score_triggeredr = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Keydown actions
                if event.type == pygame.KEYDOWN:   
                    if event.key ==  pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d:
                        if not update_score_triggeredl:
                                break
                        left_event_time = pygame.time.get_ticks()
                        if event.key == pygame.K_a:
                            pygame.time.set_timer(CUSTOM_EVENT1, action_duration)
                        elif event.key == pygame.K_s:
                            pygame.time.set_timer(CUSTOM_EVENT5, action_duration)
                        elif event.key == pygame.K_d:
                            pygame.time.set_timer(CUSTOM_EVENT10, action_duration)

                        update_score_triggeredl = False

                    if event.key ==  pygame.K_l or event.key == pygame.K_k or event.key == pygame.K_j:
                        if not update_score_triggeredr:
                                break
                        right_event_time = pygame.time.get_ticks()
                        if event.key == pygame.K_l:
                            pygame.time.set_timer(CUSTOM_EVENT11, action_duration)
                        elif event.key == pygame.K_k:
                            pygame.time.set_timer(CUSTOM_EVENT51, action_duration)
                        elif event.key == pygame.K_j:
                            pygame.time.set_timer(CUSTOM_EVENT101, action_duration)
                        
                        update_score_triggeredr = False

                if not update_score_triggeredl:
                    if pygame.time.get_ticks() - left_event_time >= action_duration:
                        if event.type == CUSTOM_EVENT1:
                            update_score(1, team1_score + 1)
                            update_current_score(1, 1)
                        if event.type == CUSTOM_EVENT5:
                            update_score(1, team1_score + 5)
                            update_current_score(1, 5)
                        if event.type == CUSTOM_EVENT10:
                            update_score(1, team1_score + 10)
                            update_current_score(1, 10)
                        update_score_triggeredl = True

                if not update_score_triggeredr:
                    if pygame.time.get_ticks() - right_event_time >= action_duration:
                        if event.type == CUSTOM_EVENT11:
                            update_score(2, team2_score + 1)
                            update_current_score(2, 1)
                        if event.type == CUSTOM_EVENT51:
                            update_score(2, team2_score + 5)
                            update_current_score(2, 5)
                        if event.type == CUSTOM_EVENT101:
                            update_score(2, team2_score + 10)
                            update_current_score(2, 10)
                        update_score_triggeredr = True

            # Set statelist
            if left_event_time == -1:
                statelist[0] = 0
            elif pygame.time.get_ticks() - left_event_time < 200:
                statelist[0] = 0
            elif pygame.time.get_ticks() - left_event_time < 400:
                statelist[0] = 1
            elif pygame.time.get_ticks() - left_event_time < 600:
                statelist[0] = 2
            elif pygame.time.get_ticks() - left_event_time < action_duration:
                statelist[0] = 0

                # Set ball position
                ball_rect = ball_image.get_rect()
                ball_rect.center = (230, 650)

                start_pos = pygame.Vector2(230, 650)
                end_pos = pygame.Vector2(1180, 650)
                motion_time = 2.6

                distance = end_pos.x - start_pos.x

                t = (pygame.time.get_ticks() - left_event_time) / 1000 - 0.6  # Calculate elapsed time in seconds
                if t <= motion_time - 0.6:
                    x = start_pos.x + distance / (motion_time - 0.6) * t
                    y = start_pos.y - curve_height * math.sin((x - start_pos.x) * (math.pi / distance))
                statelist[2] = [x, y]

            else:
                x = 230
                y = 650
                statelist[2] = [x, y]
               
            if right_event_time == -1:
                statelist[1] = 0
            elif pygame.time.get_ticks() - right_event_time < 200:
                statelist[1] = 0
            elif pygame.time.get_ticks() - right_event_time < 400:
                statelist[1] = 1
            elif pygame.time.get_ticks() - right_event_time < 600:
                statelist[1] = 2
            elif pygame.time.get_ticks() - right_event_time < action_duration:
                statelist[1] = 0

                # Set ball position
                ball_rect = ball_image.get_rect()
                ball_rect.center = (1030, 650)

                start_pos = pygame.Vector2(1030, 650)
                end_pos = pygame.Vector2(80, 650)
                motion_time = 2.6

                distance = start_pos.x - end_pos.x

                t = (pygame.time.get_ticks() - right_event_time) / 1000 - 0.6  # Calculate elapsed time in seconds
                if t <= motion_time - 0.6:
                    x = start_pos.x - distance / (motion_time - 0.6) * t
                    y = start_pos.y + curve_height * math.sin((x - start_pos.x) * (math.pi / distance))
                statelist[3] = [x, y]
                
            else:
                x = 1030
                y = 650
                statelist[3] = [x, y]
                

            # Display current state
            display(statelist, times)

            # Check if the timer has reached 0
            if main_screen_duration + start_screen_duration - (pygame.time.get_ticks() - started_time) // 1000 == 0:
                running = False

            pygame.time.Clock().tick(100)

        # Display winner screen
        if team1_score > team2_score:
            display_winner_screen("Winner: Team 1")
        elif team2_score > team1_score:
            display_winner_screen("Winner: Team 2")
        else:
            display_winner_screen("It's a tie")

        update_score(1, 0)
        update_score(2, 0)
        update_current_score(1, 0)
        update_current_score(2, 0)
        times = times + 1

# Start the game loop
game_loop()