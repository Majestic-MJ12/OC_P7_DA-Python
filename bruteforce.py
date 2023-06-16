import csv

maximum = 500


def main():
    share_listing = read_the_csv()

    print(f"\nProcess {len(share_listing)} shares for {maximum}€ :")

    best_combination = set_combination(share_listing)
    get_results(best_combination)


def csv():

    with open("data/shares.csv") as csvfile:
        shares_file = csv.reader(csvfile, delimiter=',')

        shares_list = []
        for row in shares_file:
            shares_list.append(
                (row[0], float(row[1]), float(row[2]))
            )

        return shares_list