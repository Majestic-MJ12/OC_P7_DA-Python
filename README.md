# OC_P7_DA-Python
Projet n°7: DA-Python OpenClassrooms (Develop a user interface for a Python web application).

The program calculates the best combination of stocks based on their profits using two approaches: bruteforce and dynamic programming (knapsack algorithm).

## Getting Started

### Prerequisites
- Python 3.11 or higher
- Git

### Installation
1. Clone the repository:
    ```
    git clone https://github.com/Majestic-MJ12/OC_P7_DA-Python.git
    ```
2. Navigate to the project directory:
    ```
    cd OC_P7_DA-Python 
    ```
3. Set up a virtual environment:
    ```
    python -m venv env
    ```
4. Activate the virtual environment:
    - On Windows:
        ```
        env\scripts\activate
        ```
    - On MacOS and Linux:
        ```
        source env/bin/activate
        ```
5. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Usage

### Bruteforce
To run the bruteforce approach, use the following command:
```
python bruteforce.py
```
By default, the investment amount is set to 500€. However, it is possible to enter a custom amount as follows:
```
python bruteforce.py 400
```
Note: The bruteforce approach only processes data from the "shares.csv" file, which contains 20 stocks. Datasets 1 and 2 would result in an extremely long execution time (What is solved with the optimized.py).

### Dynamic Programming
To run the dynamic programming approach, use the following command:
```
python optimized.py dataset1
```
Replace "dataset1" with the name of the file you want to process, without the file path or extension. By default, the investment amount is set to 500€. However, it is possible to enter a custom amount as follows:
```
python optimized.py dataset2 600
```
It is also possible to process the test file (20 stocks), with or without a custom amount:
```
python optimized.py shares

python optimized.py shares 400
```
Note: During data processing, the program displays a progress bar (thanks to "tqdm").

## Slides

Here you'll find the slides that explain the optimised solution (including the bruteforce):

[Link to PDF](pdf/Spring_Florent_3_diapositives_062023.pdf)

## Built With
- Python
- Git

## License

GNU AFFERO GENERAL PUBLIC LICENSE
