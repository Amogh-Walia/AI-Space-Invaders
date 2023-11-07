# AI Space Invaders vs. Spaceship AI Battle


Welcome to the Space Invaders vs. Spaceship AI Battle project, a small Flask-based simulation where we pit Space Invaders, powered by Genetic AI, against a spaceship driven by Reinforcement Learning. In this exciting showdown, we observe how two different AI algorithms perform in a challenging environment.

## Overview

After running the simulation for 168 turns, we made the following observations:

- The Genetic Algorithm consistently defeats the Reinforcement Learning agent within just 3 turns, showcasing its remarkable adaptability.
- The Reinforcement Learning agent maintained its learning rate throughout episodes, whereas the Genetic Algorithm reset every episode.
- The dominance of Genetic AI is attributed to the fact that the six Invaders act like six different Q agents simultaneously.
- However, the increasing number of kills suggests that it got stuck at a local minimum and couldn't evolve past it.
- Genetic AI was able to traverse more of its sample space than Reinforcement Learning, but it often got stuck at a local optima. In contrast, Reinforcement Learning was slower to traverse but managed to increase its performance over 168 episodes.
- A potential solution may involve a hybrid variant that combines multiple Q agents navigating the environment simultaneously.

## Project Highlights

- **Simulation Results:** This project provides insights into the performance and behavior of Genetic AI and Reinforcement Learning in a gaming environment.
- **Adaptation Rate:** Genetic AI shows rapid adaptation and is capable of achieving its peak performance in a single episode, whereas Reinforcement Learning gradually improves over 168 episodes.
- **Potential for Hybrid Solution:** Considering the strengths and weaknesses of both algorithms, a hybrid approach involving multiple Q agents may offer a promising solution.

## Getting Started

Follow these steps to get started with the project:

1. Clone the repository to your local machine:
   git clone https://github.com/Amogh-Walia/AI-Space-Invaders
2.Navigate to the project directory:
   cd AI-Space-Invaders
3.Install dependencies
  pip install -r requirements.txt
4.Start the Flask app by running the following command:
  python app.py

##Observations
After running the simulation for 168 turns, the following observations were made:
● The Genetic Algorithm almost always defeats the RL each episode within 3 turns.
● This means that it is capable of adapting at a rate much faster than RL.
● The RL kept its learning common throughout the Episodes while the Genetic Algorithm reset
every Episode.
● This Genetic AI dominance is attributed to the fact that the 6 Invaders act like 6 Different Q
agents at the same time.
● However the rising number of Kills also means that it got stuck at a local minimum and
couldn't evolve past it.
● Genetic AI was able to traverse more of its Sample Space than RL could but got very easily
stuck at a local optima while RL was much slower to traverse but was able to keep increasing
its performance right up to 100% average reward per episode. However this took 168
episodes while Genetic AI would achieve its peak in a single episode and beat it.
● Hence a Hybrid variant of the two which involves multiple Q agents traversing the
Environment at the same time might be able to solve both these problems.
Both the algorithms had different issues in being able to perform efficiently at first. These were:
1. The Genetic Algorithm did not have a lot of variety in its population, causing many “similar”
invaders to spawn that behaved exactly the same way and caused it to get stuck in a local
optima.
2. The Reinforcement Learning Q agent kept getting stuck in one half of the zone since it hadn't
“explored” the other half nearly as well causing it to almost never get out of its “comfort
zone”.
Changing the different hyperparameters of both the AI algorithms have a major impact on their
performance and remedied the above effects:
1. Increasing the “Mutation chance” in Genetic Algorithm turned out to allow it to have a lot
more variety within its population allowing for faster “Traversal through the Sample Space”
and posed a bigger challenge for its RL counterpart.
2. At the same time in RL, increasing the epsilon led to the Q agent to explore more than
exploit which allowed it to avoid getting stuck in a small zone
