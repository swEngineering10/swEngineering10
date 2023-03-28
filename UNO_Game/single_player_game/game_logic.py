class GameLogic:
    def init_game(self, players, deck): #Method that initializes the game.
        self.players = players
        self.deck = deck
        self.current_player = self.players[0]
        self.current_card = self.deck.draw()
        self.direction = 1
        self.turn = 0
        self.drawn_cards = []
        self.winner = None
    def shuffle_deck(self): #Method that shuffles the deck of cards.
        self.deck.shuffle()
    def deal_cards(self): # Method that deals cards to the players.
        for player in self.players:
            player.draw_cards(self.deck)
    # def determine_start_player(self): #Method that determines the starting player.
    
    def is_winner(self): #Method that checks if there is a winner.
        return self.winner is not None
    #Define methods for playing a card, drawing a card, and skipping a turn
    def play_card(self, card):
        self.current_card = card
        self.current_player.play_card(card)
        self.turn += 1
        self.current_player = self.players[self.turn % len(self.players)]
    def draw_card(self):
        card = self.deck.draw()
        self.current_player.draw_card(card)
        self.turn += 1
        self.current_player = self.players[self.turn % len(self.players)]
    def skip_turn(self):
        self.turn += 1
        self.current_player = self.players[self.turn % len(self.players)]
    #Define methods for determining the valid plays for a player
    def is_valid_play(self, card): #Method that checks if a card is a valid play.
        if card.value == card.Value.WILD or card.value == card.Value.COLOR_CHANGE:
            return True
        if card.color == self.current_card.color:
            return True
        if card.value == self.current_card.value:
            return True
        return False

    #Define a method for handling the end of a round and updating the game state
    def end_round(self):
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                return
        self.current_card = self.deck.draw()
        self.turn = 0
        self.current_player = self.players[self.turn % len(self.players)]

    #Define a method for handling the end of the game and declaring the winner
    def end_game(self):
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                return
    
    #Define a method for simulating the computer player's turn
    def computer_turn(self):
        for card in self.current_player.hand:
            if self.is_valid_play(card):
                self.play_card(card)
                return
        self.draw_card()
        return
    
    #Define a method for updating the game status and displaying it on the screen
    def update_status(self, screen):
        screen.addstr(0, 0, "Current Card: " + str(self.current_card))
        screen.addstr(1, 0, "Current Player: " + str(self.current_player))
        screen.addstr(2, 0, "Turn: " + str(self.turn))
        screen.addstr(3, 0, "Winner: " + str(self.winner))
        screen.addstr(4, 0, "Drawn Cards: " + str(self.drawn_cards))
        screen.addstr(5, 0, "Direction: " + str(self.direction))

    #Define a method for handling user input and executing the corresponding action
    def handle_input(self, screen, key):
        if key == ord('p'):
            self.play_card(self.current_player.hand[0])
        elif key == ord('d'):
            self.draw_card()
        elif key == ord('s'):
            self.skip_turn()
        elif key == ord('q'):
            return False
        return True
    
    #Define a method for starting and running the game loop
    def run(self, screen):
        self.init_game([Player("Player 1"), Player("Computer")], Deck())
        self.shuffle_deck()
        self.deal_cards()
        while not self.is_winner():
            self.update_status(screen)
            key = screen.getch()
            if not self.handle_input(screen, key):
                return
            if self.current_player.name == "Computer":
                self.computer_turn()
        self.end_game()
        self.update_status(screen)
        screen.getch()
    
    #Define a method for handling the end of the game and returning to the start menu.
    def end_game(self):
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                return
    

    
    
    
    