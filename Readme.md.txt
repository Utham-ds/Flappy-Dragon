# Flappy Dragon – Pygame Project

This repository contains a simple 2D side‑scrolling game inspired by Flappy Bird, implemented in Python using the Pygame library. The player controls a dragon character that must navigate through gaps between moving pipes without colliding with them.

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

## Project Structure

```text
flappy-dragon/
├─ flappy.py          # Main game script (Pygame loop, logic, rendering)
└─ assets/            # Image assets used in the game
   ├─ dragon.png
   ├─ Background.jpg
   └─ Pipe.png
