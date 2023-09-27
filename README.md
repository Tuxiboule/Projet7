# Investment Brute-Force

**Investment Brute-Force** is a Python program that solves an investment optimization problem. It explores all possible combinations of actions to determine the best investment strategy while adhering to budget constraints.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributions](#contributions)
- [License](#license)

## Overview

In the world of finance, investment is often a complex matter of strategic choices. This program aims to explore all possibilities to maximize profit within specific constraints. It can be useful for making informed investment decisions.

## Features

- Search for the best combination of actions to maximize profit.
- Adherence to budget constraints.
- Ability to specify a CSV file containing action data.
- Brute-force algorithm to explore all possible combinations.

## Installation

1. Ensure you have Python installed on your system.
2. Download the source code from the GitHub repository:
```
bash git clone https://github.com/your-username/investment-bruteforce.git
```
3. Install dependencies if necessary
```
pip install -r requirements.txt
```

## Usage

- Make sure you have a CSV file containing action data. The file should have the following format :
```
Action #, Cost per Action (in euros), Profit (after 2 years)
1,20,5
2,30,10
...
```
- Run the program using the following command :
```
python bruteforce.py
```

