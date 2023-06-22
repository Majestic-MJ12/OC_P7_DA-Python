import time
import sys
import pandas as pd
from tqdm import tqdm

begin_time = time.time()

try:
    maximum = float(sys.argv[2])
except IndexError:
    maximum = 500


def main():
    """Check for filename input"""
    try:
        file = "csv/" + sys.argv[1] + ".csv"
    except IndexError:
        print("\nNo file found. Please try again.\n")
        time.sleep(1)
        sys.exit()

    share_listing = read_csv(file)

    print(f"\nProcessing '{sys.argv[1]}' ({len(share_listing)} shares) for {maximum}euros:")

    display(kp(share_listing))


def read_csv(file):
    try:
        with open(file) as csvfile:
            share_file = csv.reader(csvfile, delimiter=',')

            if file != "csv/shares.csv":
                next(csvfile)

            share_listing = []

            for i in share_file:
                if float(i[1]) <= 0 or float(i[2]) <= 0:
                    pass
                else:
                    shares = (
                    i[0],
                        int(float(i[1])*100),
                        float(float(i[1]) * float(i[2]) / 100)
                    )
                    share_listing.append(shares)

            return share_listing

    except FileNotFoundError:
        print(f"\nFile '{file}' doesn't exist. Try again.\n")
        time.sleep(1)
        sys.exit()


def kp(share_listing):
    pass


def display(best_combination):
    pass


if __name__ == "__main__":
    main()
