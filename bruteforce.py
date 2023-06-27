# Import necessary libraries
import time
import sys
import pandas as pd
from tqdm import tqdm
from itertools import combinations

# Store the start time of the program
begin_time = time.time()

# Set the floating point format for pandas dataframes
pd.set_option('float_format', '{:.2f}'.format)

# Try to read the maximum investment amount from the command line arguments, and if it fails, set it to 500
try:
    maximum = float(sys.argv[1])
except IndexError:
    maximum = 500


# The main function reads the CSV file, finds the best combination of shares, and displays the results.
def main():
    share_listing = read_csv()

    # Print a message indicating the number of shares being processed and the maximum investment amount
    print(f"\nProcessing {len(share_listing)} shares for {maximum} euros:")

    # Find the best combination of shares and display the results
    best_combination = set_combination(share_listing)
    display(best_combination)


# The read_csv function reads the CSV file and returns a list of tuples containing the share name, price, and return.
def read_csv():
    # Read the CSV file using pandas and assign column names
    df = pd.read_csv("csv/shares.csv", names=['Shares', 'Prices', 'Return'])

    # Convert the dataframe to a list of tuples
    csv_list = []
    for index, row in df.iterrows():
        csv_list.append(
            (row['Shares'], float(row['Prices']), float(row['Return']))
        )

    return csv_list


# The set_combination function finds the best combination of shares that
# maximizes the income while keeping the total investment below the maximum investment amount.
def set_combination(csv_list):
    income = 0
    best_combination = []

    # Use tqdm to display a progress bar while iterating over all possible combinations of shares.
    for f in tqdm(range(len(csv_list)), desc="\033[34mFinding the best combination among all\033[0m",
                  bar_format="{l_bar}{bar:10}{r_bar}{bar:-10b}", ncols=100, colour='green'):
        one_combination = combinations(csv_list, f + 1)

        for combination in one_combination:
            total_investment = calc_investment(combination)

            if total_investment <= maximum:
                total_income = calc_income(combination)

                if total_income > income:
                    income = total_income
                    best_combination = combination

    return best_combination


# The calc_investment function calculates the total investment required for a given combination of shares.
def calc_investment(combination):
    prices = []
    for el in combination:
        prices.append(el[1])

    return sum(prices)


# The calc_income function calculates the total income for a given combination of shares.
def calc_income(combination):
    all_income = []
    for el in combination:
        all_income.append(el[1] * el[2] / 100)

    return sum(all_income)


# The display function displays the best combination of shares and the corresponding investment and income.
def display(best_combination):
    # Print a message indicating the number of shares in the best combination
    print(f"\n\033[34mMost profitable investment ({len(best_combination)} shares) :\033[0m\n")

    # Print the details of each share in the best combination
    for item in best_combination:
        print(f"{item[0]} | {item[1]} euros | +{item[2]} %")

    # Print the total cost and profit of the best combination
    print("\n\033[34mThe total cost : \033[0m", calc_investment(best_combination), "euros")
    print("\033[34mProfit after 2 years :\033[0m +", round(calc_income(best_combination), 2), "euros")

    # Print the time elapsed since the start of the program
    print("\n\033[34mTime elapsed : \033[0m", round(time.time() - begin_time, 2), "s")


# Call the main function if the script is run directly.
if __name__ == "__main__":
    main()
