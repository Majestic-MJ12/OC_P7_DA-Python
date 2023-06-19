import sys
import csv
import time
import sys
from tqdm import tqdm
from itertools import combinations

start_time = time.time()

try:
    maximum = float(sys.argv[1])
except IndexError:
    maximum = 500


def main():
    share_listing = csv()

    print(f"\nProcess {len(share_listing)} shares for {maximum}€ :")

    best_combination = set_combination(share_listing)
    get_results(best_combination)


def csv():
    with open("data/shares.csv") as csvfile:
        shares_file = csv.reader(csvfile, delimiter=',')

        csv_list = []
        for row in shares_file:
            csv_list.append(
                (row[0], float(row[1]), float(row[2]))
            )

        return csv_list


def set_combination(csv_list):
    income = 0
    best_combination = []

    for f in tqdm(range(len(csv_list))):
        one_combination = all_combinations(csv_list, f + 1)

        for combination in one_combination:
            total_investment = calc_investment(combination)

            if total_investment <= maximum:
                total_income = calc_income(combination)

                if total_income > income:
                    income = total_income
                    best_combination = combination

    return best_combination
