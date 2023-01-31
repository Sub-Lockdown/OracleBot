#!/usr/bin/env python3

# We are an import and import company
import sys
import random
import os

if os.path.isdir('images') is False:
    os.makedirs('images')

class Deck:
    def __init__(self) -> None:
        """Auto runs through the cards in deck, mapping values."""
        self.deck = []
        self.buildDeck()

    def buildDeck(self):
        """Creates the dictionary of the deck."""
        mypath = '.\\images\\'
        images = []
        for (filenames) in os.walk(mypath):
            images.extend(filenames)
        for paths in images[2]:
            card = mypath + paths
            self.deck.append(card)
        self.shuffleDeck()
    
    def shuffleDeck(self):
        """Shuffles the order of the deck."""
        random.shuffle(self.deck)
    
    def drawCard(self):
        """Removes and returns the first card in deck"""
        return self.deck[0]

class Hand:
    def __init__(self, name) -> None:
        """Sets the name of this hand, and an empty hand."""
        self.name =  name
        self.hand = []
    
    def drawCard(self, deck):
        """Draws a card from a deck."""
        self.hand.append(deck.drawCard())
        return self

    def showCard(self):
        return self.hand.pop()

if __name__ == "__main__":
    print('This file contains basic oracle deck functions.')
    sys.exit()
