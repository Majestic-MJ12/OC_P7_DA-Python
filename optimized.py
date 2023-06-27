# Import necessary libraries
import csv
import time
import sys
from tqdm import tqdm

# Record the start time of the program
begin_time = time.time()

# Try to get the maximum investment amount from the command line arguments, default to 500 if not provided
try:
    maximum = float(sys.argv[2])
except IndexError:
    maximum = 500


# Define the main function
def main():
    try:
        # Try to get the filename from the command line arguments
        file = "csv/" + sys.argv[1] + ".csv"
    except IndexError:
        # If no filename is provided, print an error message and exit the program
        print("\n\x1b[34mNo file found. Try again.\x1b[0m\n")
        time.sleep(1)
        sys.exit()

    # Read the CSV file and create a list of shares
    share_listing = read_csv(file)

    # Print a message indicating the start of processing
    print(f"\n\x1b[34mProcessing '{sys.argv[1]}' ({len(share_listing)} shares) for {maximum} euros:\x1b[0m")

    # Find the best combination of shares to invest in
    best_combination = kp(share_listing)

    # Display the best combination of shares and the total cost and profit
    display(best_combination)


# Define a function to read a CSV file and return a list of shares
def read_csv(file):
    try:
        with open(file) as csvfile:
            shares_file = csv.reader(csvfile, delimiter=',')

            # Skip the first row in both datasets
            if file != "csv/shares.csv":
                next(csvfile)

            share_listing = []

            # Create a tuple for each share and add it to the list if it meets the criteria
            for i in shares_file:
                if float(i[1]) <= 0 or float(i[2]) <= 0:
                    pass
                else:
                    share = (
                        i[0],
                        int(float(i[1])*100),
                        float(float(i[1]) * float(i[2]) / 100)
                    )
                    share_listing.append(share)

            return share_listing

    except FileNotFoundError:
        # If the file is not found, print an error message and exit the program
        print(f"\n\x1b[34mFile '{file}' does not exist. Please try again.\x1b[0m\n")
        time.sleep(1)
        sys.exit()


# Define a function to find the best combination of shares to invest in
def kp(share_listing):
    max_investment = int(maximum * 100)
    share_total = len(share_listing)
    investment = []
    income = []

    # Create lists of investments and incomes for each share
    for cut in share_listing:
        investment.append(cut[1])
        income.append(cut[2])

    # Create a 2D list to store the optimal profit for each combination of shares and investment amount
    kps = [[0 for x in range(max_investment + 1)] for x in range(share_total + 1)]

    # Use tqdm to display a progress bar while processing
    with tqdm(total=share_total, bar_format="\x1b[32m{l_bar}{bar:30}{r_bar}\x1b[0m") as pbar:
        for i in range(1, share_total + 1):
            pbar.update(1)

            for t in range(1, max_investment + 1):
                if investment[i-1] <= t:
                    kps[i][t] = max(income[i-1] + kps[i-1][t-investment[i-1]], kps[i-1][t])
                else:
                    kps[i][t] = kps[i-1][t]

    # Retrieve combination of shares from optimal profit
    best_combination = []

    while max_investment >= 0 and share_total >= 0:

        if kps[share_total][max_investment] == \
                kps[share_total-1][max_investment - investment[share_total-1]] + income[share_total-1]:

            best_combination.append(share_listing[share_total-1])
            max_investment -= investment[share_total-1]

        share_total -= 1

    return best_combination


# Define a function to display the best combination of shares and the total cost and profit
def display(best_combination):
    print(f"\n\x1b[34mThe most profitable investment ({len(best_combination)} shares):\x1b[0m\n")

    investment = []
    income = []

    # Print information for each share in the best combination
    for item in best_combination:
        print(f"\x1b[34m{item[0]} | {round(item[1] / 100, 2)} euros | +{round(item[2], 2)} euros\x1b[0m")
        investment.append(round(item[1] / 100, 2))
        income.append(round(item[2], 2))

    # Print the total cost and profit
    print("\n\x1b[34mThe total cost : ", round(sum(investment), 2), "euros")
    print("Profit after 2 years : +", round(sum(income), 2), "euros")
    print("\nTime elapsed : ", round(time.time() - begin_time, 2), "s\n")


# Call the main function if this file is being run as the main program
if __name__ == "__main__":
    main()
