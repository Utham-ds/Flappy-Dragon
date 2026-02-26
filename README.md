# Flappy Dragon Game

A Python/Pygame implementation of a Flappy Bird–style side‑scrolling game, featuring a flying dragon character. Developed as a personal project to practise real‑time game loops, collision detection and basic game state management.

## Objectives

- Practise structuring a small game project in Python.
- Implement a real‑time game loop, collision detection, and basic state management (start, playing, game over).
- Experiment with difficulty scaling through multiple levels (pipe speed and spawn frequency).

## Game Features

- **Core mechanics**  
  - Single‑key control (SPACE) to make the dragon “flap” upwards against gravity.  
  - Continuous side‑scrolling environment with randomly generated pipe gaps.  
  - Ground and pipe collision detection leading to a game‑over state.

- **Game states and levels**  
  - Start screen, active play, and game‑over screen with restart behaviour.  
  - Multiple levels with configurable pipe speeds and spawn intervals to increase difficulty over time.

- **UI elements**  
  - On‑screen score that increments as the player successfully passes pipes.  
  - Current level indicator displayed during gameplay.  
  - Simple text prompts for “Press SPACE to Start” and “Game Over – Press SPACE to Restart”.


## Tech Stack

- Python 3
- Pygame
- Basic object‑oriented and event‑driven programming concepts

## Project Structure

```text
flappy-dragon/
├─ flappy.py          # Main game script (Pygame loop, logic, rendering)
└─ assets/            # Image assets used in the game
   ├─ dragon.png
   ├─ Background.jpg
   └─ Pipe.png


## How to Play

1. Install dependencies:
   ```bash
   pip install pygame
2. Run the main file:
   ```bash
   python flappy.py
3. Press SPACE to start the game and to make the dragon flap.
4. Fly through the gaps between pipes without hitting them or the ground.
5. Your score increases each time you successfully pass a set of pipes.

## Author

Utham Kumar Mohanlal
