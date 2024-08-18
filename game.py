from data_structures.referential_array import ArrayR
from data_structures.stack_adt import ArrayStack
from data_structures.queue_adt import CircularQueue
from player import Player
from card import CardColor, CardLabel, Card
from random_gen import RandomGen
from constants import Constants


class Game:
    """
    Game class to play the game
    """

    def __init__(self) -> None:
        self.players = CircularQueue(Constants.MAX_PLAYERS)
        self.draw_pile = ArrayStack(Constants.DECK_SIZE)
        self.discard_pile = ArrayStack(Constants.DECK_SIZE)
        self.current_player = None
        self.current_color = None
        self.current_label = None
        """
        Constructor for the Game class

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        return None

    def generate_cards(self) -> ArrayR[Card]:
        """
        Method to generate the cards for the game

        Args:
            None

        Returns:
            ArrayR[Card]: The array of Card objects generated

        Complexity:
            Best Case Complexity: O(N) - Where N is the number of cards in the deck
            Worst Case Complexity: O(N) - Where N is the number of cards in the deck
        """
        list_of_cards: ArrayR[Card] = ArrayR(Constants.DECK_SIZE)
        idx: int = 0

        for color in CardColor:
            if color != CardColor.CRAZY:
                # Generate 4 sets of cards from 0 to 9 for each color
                for i in range(10):
                    list_of_cards[idx] = Card(color, CardLabel(i))
                    idx += 1
                    list_of_cards[idx] = Card(color, CardLabel(i))
                    idx += 1

                # Generate 2 of each special card for each color
                for i in range(2):
                    list_of_cards[idx] = Card(color, CardLabel.SKIP)
                    idx += 1
                    list_of_cards[idx] = Card(color, CardLabel.REVERSE)
                    idx += 1
                    list_of_cards[idx] = Card(color, CardLabel.DRAW_TWO)
                    idx += 1
            else:
                # Generate the crazy and crazy draw 4 cards
                for i in range(4):
                    list_of_cards[idx] = Card(CardColor.CRAZY, CardLabel.CRAZY)
                    idx += 1
                    list_of_cards[idx] = Card(CardColor.CRAZY, CardLabel.DRAW_FOUR)
                    idx += 1

                # Randomly shuffle the cards
                RandomGen.random_shuffle(list_of_cards)

                return list_of_cards

    def initialise_game(self, players: ArrayR[Player]) -> None:
        for player in players:
            self.players.append(player)
        cards = self.generate_cards()
        idx = 0
        for i in range(Constants.NUM_CARDS_AT_INIT):
            for player in players:
                player.add_card(cards[idx])
                idx += 1
        while idx < len(cards):
            self.draw_pile.push(cards[idx])
            idx += 1
        while True:
            top_card = self.draw_pile.pop()
            self.discard_pile.push(top_card)
            if (
                top_card.label is not CardLabel.SKIP
                and top_card.label is not CardLabel.REVERSE
                and top_card.label is not CardLabel.DRAW_TWO
                and top_card.label is not CardLabel.CRAZY
                and top_card.label is not CardLabel.DRAW_FOUR
            ):
                break
        self.current_color = top_card.color
        self.current_label = top_card.label

        """
        Method to initialise the game

        Args:
            players (ArrayR[Player]): The array of players

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """

    def crazy_play(self, card: Card) -> None:
        """
        Method to play a crazy card

        Args:
            card (Card): The card to be played

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.current_color = CardColor(RandomGen.randint(0, 3))
        if card.label == CardLabel.DRAW_FOUR:
            self.next_player()
            for i in range(4):
                self.draw_card(self.next_player(), False)

        return None

    def play_reverse(self) -> None:
        """
        Method to play a reverse card

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        reverse_stack = ArrayStack(len(self.players))
        while not self.players.is_empty():
            reverse_stack.push(self.players.serve())
        while not reverse_stack.is_empty():
            self.players.append(reverse_stack.pop())
        return None

    def play_skip(self) -> None:
        """
        Method to play a skip card

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        skip = self.players.serve()
        self.players.append(skip)
        return None

    def draw_card(self, player: Player, playing: bool) -> Card | None:
        """
        Method to draw a card from the deck

        Args:
            player (Player): The player who is drawing the card
            playing (bool): A boolean indicating if the player is able to play the card

        Returns:
            Card - When drawing a playable card, other return None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        drawn_card = self.draw_pile.pop()

        if playing == True and (
            drawn_card.color == self.current_color
            or drawn_card.label == self.current_label
            or drawn_card.label == CardLabel.CRAZY
            or drawn_card.label == CardLabel.DRAW_FOUR
        ):
            return drawn_card

        player.add_card(drawn_card)
        return None

    def next_player(self) -> Player:
        """
        Method to get the next player

        Args:
            None

        Returns:
            Player: The next player

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        next_player = self.players.peek()
        return next_player

    def play_game(self) -> Player:
        """
        Method to play the game

        Args:
            None

        Returns:
            Player: The winner of the game

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        winner = False
        while winner == False:


def test_case():
    players: ArrayR[Player] = ArrayR(4)
    players[0] = Player("Alice", 0)
    players[1] = Player("Bob", 1)
    players[2] = Player("Charlie", 2)
    players[3] = Player("David", 3)
    g: Game = Game()
    g.initialise_game(players)
    winner: Player = g.play_game()
    print(f"Winner is {winner.name}")


if __name__ == '__main__':
    test_case()
