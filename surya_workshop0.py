# -*- coding: utf-8 -*-
"""Surya_workshop0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lN_XZia5aI2iv78MSFxgEwjv5LrbDdRO

Surya Bahadur Shrestha  1.task 1 , 2 and 3:
"""

temperatures = [8.2, 17.4, 14.1, 7.9, 18.0, 13.5, 9.0, 17.8, 13.0, 8.5,
                16.5, 12.9, 7.7, 17.2, 13.3, 8.4, 16.7, 14.0, 9.5, 18.3,
                13.4, 8.1, 17.9, 14.2, 7.6, 17.0, 12.8, 8.0, 16.8, 13.7,
                7.8, 17.5, 13.6, 8.7, 17.1, 13.8, 9.2, 18.1, 13.9, 8.3,
                16.4, 12.7, 8.9, 18.2, 13.1, 7.8, 16.6, 12.5]

cold = []
mild = []
comfortable = []
fahrenheit = []

def classify_temperatures():
    """Classify temperatures into cold, mild, and comfortable categories based on their values."""
    for temp in temperatures:
        if temp < 10:
            cold.append(temp)
        elif 10 <= temp <= 15:
            mild.append(temp)
        else:
            comfortable.append(temp)

    print("Cold temperatures:", cold)
    print("Mild temperatures:", mild)
    print("Comfortable temperatures:", comfortable)

def display_category_counts():
    """Display the count of temperatures in each category."""
    print(f"Number of cold days: {len(cold)}")
    print(f"Number of mild days: {len(mild)}")
    print(f"Number of comfortable days: {len(comfortable)}")

def convert_to_fahrenheit():
    """Convert the list of temperatures from Celsius to Fahrenheit."""
    for temp in temperatures:
        converted_temp = (temp * 9/5) + 32
        fahrenheit.append(round(converted_temp, 2))
    print("Temperatures in Fahrenheit:", fahrenheit)

print("------------------------- Task 1: Classification -------------------------")
classify_temperatures()

print("------------------------- Task 2: Counts -------------------------")
display_category_counts()

print("------------------------- Task 3: Conversion -------------------------")
convert_to_fahrenheit()

"""1.task4:"""

import matplotlib.pyplot as plt


temperatures = [8.2, 17.4, 14.1, 7.9, 18.0, 13.5, 9.0, 17.8, 13.0, 8.5,
                16.5, 12.9, 7.7, 17.2, 13.3, 8.4, 16.7, 14.0, 9.5, 18.3,
                13.4, 8.1, 17.9, 14.2, 7.6, 17.0, 12.8, 8.0, 16.8, 13.7,
                7.8, 17.5, 13.6, 8.7, 17.1, 13.8, 9.2, 18.1, 13.9, 8.3,
                16.4, 12.7, 8.9, 18.2, 13.1, 7.8, 16.6, 12.5]

night = []
evening = []
day = []

def categorize_temperatures():
    """
    Assign temperatures to 'night', 'day', and 'evening' lists based on their position in the dataset.
    """
    for i, temp in enumerate(temperatures):
        if i % 24 < 8:
            night.append(temp)
        elif i % 24 < 16:
            day.append(temp)
        else:
            evening.append(temp)

    print("Day temperatures:", day)
    print("Night temperatures:", night)
    print("Evening temperatures:", evening)

def calculate_average_day_temperature():
    """
    Calculate and display the average temperature during the day.
    """
    average = sum(day) / len(day)
    print(f"The average temperature during the day is: {average:.2f}°C")

def plot_day_temperatures():
    """
    Plot the day temperatures over time with a line graph.
    """
    plt.figure(figsize=(10, 6))
    days = range(1, len(day) + 1)  # X-axis: Day numbers
    plt.plot(days, day, marker='o', label='Day Temperature', color='blue')
    plt.title("Day Temperatures Over Time")
    plt.xlabel("Day")
    plt.ylabel("Temperature (°C)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()


categorize_temperatures()
calculate_average_day_temperature()
plot_day_temperatures()

"""recursion
task1
"""

`nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]

def sum_nested_list(nested_list):
    """
    Calculate the sum of all numbers in a nested list.
    This function takes a list that may contain integers and other nested lists.
    It recursively traverses the list and sums all the integers, no matter how deeply
    nested they are.
    Args:
    nested_list (list): A list that may contain integers or other lists of integers.
    Returns:

    18

    5CS037 Worksheet - 0 Siman Giri

    int: The total sum of all integers in the nested list, including those in sublists
    .
    Example:
    >>> sum_nested_list([1, [2, [3, 4], 5], 6, [7, 8]])
    36
    >>> sum_nested_list([1, [2, 3], [4, [5]]])
    15
    """
    total = 0
    for element in nested_list:
        if isinstance(element, list): # Check if the element is a list
            total += sum_nested_list(element) # Recursively sum the nested list
        else:
            total += element # Add the number to the total
    return total


sum_nested_list(nested_list)

"""2.task 2"""

def generate_permutations(s):
    """function to Takes a string s as input and returns a list of all unique permutations. """
    if len(s) <= 1:
        return [s]

    permutations = []
    for i, char in enumerate(s):
        rest = s[:i] + s[i+1:]
        for perm in generate_permutations(rest):
            permutations.append(char + perm)


    return list(set(permutations))

print(generate_permutations("abc"))

"""2.task3"""

directory_structure = {
"file1.txt": 200,
"file2.txt": 300,
"subdir1": {
"file3.txt": 400,
"file4.txt": 100
},
"subdir2": {
"subsubdir1": {
"file5.txt": 250
},
"file6.txt": 150
}
}

def calculate_directory_size(directory):
    """Return the total size of the directory."""
    total_size = 0

    for name, value in directory.items():
        if isinstance(value, dict):
            total_size += calculate_directory_size(value)
        else:
            total_size += value

    return total_size
total_size= calculate_directory_size(directory_structure)
print(f"total directory size : {total_size}")

"""3.task1"""

def min_coins(coins, amount):
    """
     Finds the minimum number of coins needed to make up a given amount using dynamic
  programming.
  This function solves the coin change problem by determining the fewest number of
  coins from a given set of coin denominations that sum up to a target amount. The
  solution uses dynamic programming(tabulation) to iteratively build up the minimum
  number of coins required for each amount.
  Parameters:
  coins (list of int): A list of coin denominations available for making change. Each
  coin denomination is a positive integer.
  amount (int): The target amount for which we need to find the minimum number of coins
  . It must be a non-negative integer.
  Returns:
  int: The minimum number of coins required to make the given amount.
  If it is not possible to make the amount with the given coins, returns -1.
  Example:
  >>> min_coins([1, 2, 5], 11)
  3
  >>> min_coins([2], 3)
  -1
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Test with the given example
coins = [1, 2, 5]
amount = 11
result = min_coins(coins, amount)
print(f"Minimum coins required to make {amount} using coins {coins}: {result}")

"""3.task 2"""

def longest_common_subsequence(s1, s2):
    """function to uses DP to find the length of the LCS of two strings s1 and s2."""
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

s1 = "abcde"
s2 = "ace"
result = longest_common_subsequence(s1, s2)
print(f"Length of LCS for '{s1}' and '{s2}': {result}")

"""3.task 3"""

def knapsack(weights, values, capacity):
    """function to  Uses DP to determine the maximum value that can be achieved within the given weight capacity."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]


    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
result = knapsack(weights, values, capacity)
print(f"Maximum value for weights {weights}, values {values}, and capacity {capacity}: {result}")