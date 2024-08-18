from card import Card
from data_structures.array_sorted_list import ArraySortedList
from constants import Constants


class Player:
    """
    Player class to store the player details
    """
    def __init__(self, name: str, position: int) -> None:
        self.name = name
        self.position = position
        self.hand = ArraySortedList(1)
        return None
        """
        Constructor for the Player class

        Args:
            name (str): The name of the player
            position (int): The position of the player

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        

    def add_card(self, card: Card) -> None:
       self.hand.add(card)
       return None
       """
        Method to add a card to the player's hand

        Args:
            card (Card): The card to be added to the player's hand

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """                                                                                                                         
        

    def play_card(self, index: int) -> Card:
        return self.hand.delete_at_index(index)
        """
        Method to play a card from the player's hand

        Args:
            index (int): The index of the card to be played

        Returns:
            Card: The card at the given index from the player's hand

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
   

    def __len__(self) -> int:
        return len(self.hand)
        """
        Method to get the number of cards in the player's hand

        Args:
            None

        Returns:
            int: The number of cards in the player's hand

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        
    def __getitem__(self, index: int) -> Card:
        return self.hand[index]
        """
        Method to get the card at the given index from the player's hand

        Args:
            index (int): The index of the card to be fetched

        Returns:
            Card: The card at the given index from the player's hand

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        
