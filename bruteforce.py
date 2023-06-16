maximum = 500


def main():
    share_listing = read_the_csv()

    print(f"\nProcess {len(share_listing)} shares for {maximum}€ :")

    best_combination = set_combination(share_listing)
    get_results(best_combinaison)