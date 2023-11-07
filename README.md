# AI Space Invaders vs. Spaceship AI Battle


Welcome to the Space Invaders vs. Spaceship AI Battle project, a small Flask-based simulation where we pit Space Invaders, powered by Genetic AI, against a spaceship driven by Reinforcement Learning. In this exciting showdown, we observe how two different AI algorithms perform in a challenging environment.



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

## Observations

After running the simulation for 168 turns, we made the following observations:

- The Genetic Algorithm consistently defeats the Reinforcement Learning agent within just 3 turns, showcasing its remarkable adaptability.
- The Reinforcement Learning agent maintained its learning rate throughout episodes, whereas the Genetic Algorithm reset every episode.
- The dominance of Genetic AI is attributed to the fact that the six Invaders act like six different Q agents simultaneously.
- However, the increasing number of kills suggests that it got stuck at a local minimum and couldn't evolve past it.
- Genetic AI was able to traverse more of its sample space than Reinforcement Learning, but it often got stuck at a local optima. In contrast, Reinforcement Learning was slower to traverse but managed to increase its performance over 168 episodes.
- A potential solution may involve a hybrid variant that combines multiple Q agents navigating the environment simultaneously.

![image](https://github.com/Amogh-Walia/AI-Space-Invaders/assets/72308844/ea0c65f6-4595-4009-bb15-731213f8257d)
