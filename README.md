# Investment Optimisation

![](icon.png)
## About
A Python script that solves an investment optimization problem. It explores all possible combinations of actions to determine the best investment strategy while adhering to budget constraints.

## Features

- Search for the best combination of actions to maximize profit.
- Adherence to budget constraints.
- Ability to specify a CSV file containing action data.
- Brute-force algorithm to explore all possible combinations.
- Optimized algorithm to go way faster

## Usage

1. Ensure you have Python installed on your system.
2. Download the source code from the GitHub repository:
```
bash git clone https://github.com/Tuxiboule/Projet7.git
```
3. Install dependencies if necessary
```
pip install -r requirements.txt
```

- Make sure you have a CSV file containing action data. The file should have the following format :
```
Action #, Cost per Action (in euros), Profit (after 2 years)
1,20,5
2,30,10
```
- Run the program using the following command :

> python bruteforce.py
or 
> python optimized.py


## Context - Use Python to resolve problem with algorithm

- I really enjoyed this project about optimization. 
- The brute-force solution quickly became apparent to me. However, I had to research the optimized solution, which allowed me to learn more about linear optimization problems.

## Skills

- Bruteforce
  - CSV Reading
  - Itertools library
  - Optimisation algorithms

- Optimized
  - Using PuLP (Linear Programming)
  - Modeling Optimization Problems

## Credits
[Tuxiboule](https://github.com/Tuxiboule)
