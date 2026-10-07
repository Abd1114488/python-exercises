# The Clean Water Quest

A text game I made in Python. You play it in the terminal by typing commands.

## Story

The well in your village is dirty and people are getting sick. You walk around the village, pick up or buy items, and try to bring clean water back.

## Objective

Your goal is to fix the well. You win when you are in the village and carry both items of one of three ways:

- Engineer way: filter part + pipes
- Community way: gloves + trash bag
- Nature way: seedling + spring water

So there are three different routes from the start to the end of the game.

## Clean water goal

The game is about clean water (Sustainable Development Goal 6, Clean Water and Sanitation). Each way to win is a way to protect water: using technology, people working together, or protecting nature. There is no violence, so anyone can play it.

## How to start

Open a terminal in the project1 folder and type:

```
python ROLLA.py
```

The game asks for your name and age. You must be 12 or older to play. If you saved the game before, it asks if you want to continue.

## Actions in the game

You type one command at a time and press Enter:

- look: shows the room you are in, the item in it and where you can go
- move: go to another room. The game asks where, then you type a room name like shop
- collect: pick up the item in the room
- buy: buy the item in the shop (costs gold)
- talk: talk to the shopkeeper (only in the shop)
- gold: shows how much gold you have (you start with 42)
- inventory: shows what you carry and the total weight
- fix: try to fix the well (only in the village). If you have the right items you win, if not the game gives hints
- save: saves your game to a file
- help: shows the instructions again
- lopeta: quits the game ("lopeta" is Finnish for "stop")

## Map

- The village connects to the shop, the forest, the workshop and the school.
- The forest connects to the village, the river and the spring.
- The other rooms only connect back to where you came from.

## Where to find the items

- filter part: shop (20 gold)
- pipes: workshop
- gloves: school
- trash bag: river (go through the forest)
- seedling: forest
- spring water: spring (go through the forest)

## Project structure

```
project1/
  ROLLA.py            the main file, starts the game and runs the menu
  readme.md           this file
  game/
    __init__.py       empty file, makes game a package
    item.py           class Item (name, weight, price)
    room.py           class Room (name, description, item, exits)
    player.py         class Player (name, age, gold, items, current room)
    world.py          makes all the rooms and items, and stores the three ways to win
    actions.py        one function for each command in the menu
    storage.py        reads the text files, saves and loads the game
  data/
    intro.txt         the story shown at the start
    instructions.txt  how to play
    savegame.txt      made when you save
```

## How it works

- ROLLA.py asks for your name and age, then runs a loop that reads your command and calls the right function from actions.py.
- The game uses three classes: Item, Room and Player. Rooms are connected to each other with a dictionary of exits.
- world.py builds the rooms and items when the game starts.
- The intro and the instructions are read from text files in the data folder.
- When you save, your name, age, gold, room and items are written to savegame.txt. When you start again, the game can load them.

## What I did

I built the game step by step. First the menu with name, age and an inventory. Then the classes Item, Room and Player so I could move between rooms. After that I split the code into different files, added the text files and the saving, and then the goal and the three ways to win.