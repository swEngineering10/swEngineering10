import os
import random
import sys

import pygame
from deck import Deck
from game_board import GameBoard
from game_logic import GameLogic
from player import Player
from timer import Timer
from uno_button import UnoButton


class SinglePlayerGame:
    def __init__(self):
        # Initialize Pygame and the game window
        pygame.init()
        pygame.display.set_caption("UNO Game")
        self.screen = pygame.display.set_mode((800, 600))
        # Set the game clock and game state
        self.clock = pygame.time.Clock()
        # Create the game board, timer, and UNO button
        self.game_board = GameBoard()
        self.game_logic = GameLogic()
        self.timer = Timer()
        self.uno_button = UnoButton()
        # Create the player and computer player
        self.player = Player("Player 1")
        self.computer = Player("Computer")
        # Create the deck and deal cards to the player and computer player
        self.deck = Deck()
        self.init_game()
        self.shuffle_deck()
        self.deal_cards()
        # initialize the game logic and set the initial turn
        self.game_logic.init_game(self.player, self.computer, self.deck)
        self.game_logic.set_initial_turn()

    def start_game(self):
        # Reset the game state and game board
        self.game_logic.reset_game()
        self.game_board.reset_game()
        # Loop until the game ends or the player quits:
        while not self.game_logic.is_winner():
            # Handle events such as key presses and mouse clicks
            self.handle_events()
        # Update the game board, timer, and UNO button
            self.update_game()
        # Handle the player's turn and computer player's turn
            self.handle_turns()
        # Check for a winner or a draw
            self.check_for_winner()
        # Update the game state
            self.update_game_state()
        # Show the game over screen and wait for user input
            self.show_game_over_screen()

    def end_game(self):
        # shows the game over screen:
        # Stop the game clock and show the game over text
        self.timer.stop()
        self.game_board.show_game_over_text()
        # Show the player's and computer player's scores and cards
        self.game_board.show_player_score(self.player)
        self.game_board.show_computer_score(self.computer)
        # Wait for user input to return to the main menu
        self.wait_for_user_input()

    def update(self):
        # Update the game board, timer, and UNO button
        self.game_board.update()
        self.timer.update()
        self.uno_button.update()
        # Update the player and computer player's cards and scores
        self.game_board.show_player_cards(self.player)
        self.game_board.show_computer_cards(self.computer)

    def handle_events(self):
        # Handle key presses, mouse clicks, and window events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end_game()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_presses(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_clicks(event)

        # Handle events specific to the UNO button
        if self.uno_button.is_clicked():
            self.game_logic.handle_uno_button_click()

    def handle_key_presses(self, event):
        # Handle key presses
        if event.key == pygame.K_ESCAPE:
            self.end_game()

    def handle_mouse_clicks(self, event):
        # Handle mouse clicks
        if event.button == 1:
            self.handle_left_mouse_click()

    def handle_player_turn(self):
        # Handle the player's card selection and play
        if self.game_logic.is_player_turn():
            self.game_logic.handle_player_turn()
        # Handle the player's UNO call and draw card
        if self.game_logic.is_player_turn():
            self.game_logic.handle_player_uno_call()
            self.game_logic.handle_player_draw_card()

    def handle_computer_turn(self):
        # Handle the computer player's card selection and play
        if self.game_logic.is_computer_turn():
            self.game_logic.handle_computer_turn()
        # Handle the computer player's UNO call and draw card
        if self.game_logic.is_computer_turn():
            self.game_logic.handle_computer_uno_call()
            self.game_logic.handle_computer_draw_card()
    # Define the main function that initializes and starts the single player game:

    def main():
        # Create an instance of the SinglePlayerGame class and start the game loop if the player doesn't quit.
        game = SinglePlayerGame()
        game.start_game()
