import time
import sys
import pandas as pd
from tqdm import tqdm
from itertools import combinations

begin_time = time.time()

try:
    maximum = float(sys.argv[1])
except IndexError:
    maximum = 500


def main():
    share_listing = read_csv()

    print(f"\nProcessing {len(share_listing)} shares for {maximum} euros:")

    best_combination = set_combination(share_listing)
    display(best_combination)


def read_csv():
    df = pd.read_csv("csv/shares.csv", names=['Shares', 'Prices', 'Return'])

    csv_list = []
    for index, row in df.iterrows():
        csv_list.append(
            (row['Shares'], float(row['Prices']), float(row['Return']))
        )

    return csv_list


def set_combination(csv_list):
    income = 0
    best_combination = []

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


def calc_investment(combination):
    prices = []
    for el in combination:
        prices.append(el[1])

    return sum(prices)


def calc_income(combination):
    all_income = []
    for el in combination:
        all_income.append(el[1] * el[2] / 100)

    return sum(all_income)


def display(best_combination):
    print(f"\n\033[34mMost profitable investment ({len(best_combination)} in shares) :\033[0m\n")

    for item in best_combination:
        print(f"{item[0]} | {item[1]} euros | +{item[2]} %")

    print("\n\033[34mThe total cost : \033[0m", calc_investment(best_combination), "euros")
    print("\033[34mProfit after 2 years : +\033[0m", calc_income(best_combination), "euros")
    print("\n\033[34mTime elapsed : \033[0m", time.time() - begin_time, "s")


if __name__ == "__main__":
    main()
