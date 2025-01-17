"""
Othello Project
Group: 3A1
Team: Băcăoanu Adriana-Bianca, Chiperi Andrei, Coța Ștefan-Octavian, Pătrașcu Deny
"""

import pygame
import os
import board
import time


def run_game(delay=None):
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.init()

    surface = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Othello')

    table = board.Board()
    running = True
    player = -1

    positions = None  # valid positions for the human player
    last_position = None  # position of red dot

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not table.is_final():
                if player == -1:
                    # The turn of the human player
                    positions = table.generate_possible_moves(player, None, False)
                    if len(positions) is not None:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos_x, pos_y = pygame.mouse.get_pos()
                            pos_x -= 100
                            pos_x //= 75
                            pos_y -= 100
                            pos_y //= 75
                            if (pos_y, pos_x) in positions:
                                table.set_move(pos_y, pos_x, player)
                                player = 1
                                last_position = (pos_y, pos_x)
                                positions.clear()
                                if delay is not None and delay != 0:
                                    surface.fill((255, 255, 255))
                                    board.draw_table(surface)
                                    table.draw(surface, last_position)
                                    pygame.display.flip()
                                    pygame.time.wait(delay)
                    else:
                        time.sleep(0.1)
                else:
                    # The turn of the computer
                    # last_position = table.random_strategy()
                    # last_position = table.local_maximization_strategy()
                    # last_position = table.maximization_strategy()
                    # last_position = table.mini_max_strategy()
                    last_position = table.alpha_beta_strategy()
                    if last_position == None:
                    # last_position = table.negamax_strategy()
                        player = -1
            else:
                running = False

            surface.fill((255, 255, 255))
            board.draw_table(surface)
            table.draw(surface, last_position)

            if len(positions) > 0:
                board.draw_possible_moves(surface, positions)

            pygame.display.flip()


if __name__ == '__main__':
    run_game(delay=500)