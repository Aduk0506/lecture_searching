from pathlib import Path
import json
from random import choices
import time
# import matplotlib.pyplot as plt
def read_data(file_name, field):

    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

        if field not in data:
            return None
        else:
            return data[field]
def linear_search(sequence, number):
    positions = []
    for index, i in enumerate(sequence):

        if i == number:
            positions.append(index)
    y = sequence.count(number)
    dict = {

        "pozice": positions,
        "pocet": y
    }
    return dict


def binary_search(sequence, number):
    pozice = []

    left = 0
    right = len(sequence)-1
    middle = (right - left)//2
    if number in sequence:
        for index, i in enumerate(sequence):
            if number == sequence[middle]:
                return middle
            elif number > sequence[middle]:
                left += middle

            else:
                right -= middle

    else:
        return None
# def unordered_sequence(max_len=100):
#     return choices(range(-1000, 1000), k=max_len)
#
#
# sizes = [100, 500, 1000, 5000, 10000]
# times = [0.00001, 0.00003, 0.00006, 0.00031, 0.00067]
#
# plt.plot(sizes, times)
#
# plt.xlabel("Velikost vstupu")
# plt.ylabel("Čas [s]")
# plt.title("Ukázkový graf měření")
# plt.show()

def pattern_search(sekvence, vzor):
    pozice = []


    return pozice

def main():
    vystup = read_data("sequential.json", "unordered_numbers")
    vyhledani = linear_search(vystup, 9)
    return vystup,vyhledani




if __name__ == "__main__":
    print(main())
