from pathlib import Path
import json


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
    if number in sequence:
        for index, i in enumerate(sequence):
            if number > sequence[len(sequence)/2]:

            elif number < sequence[len(sequence)/2]:


            else:
                return sequence[len(sequence)/2]

    else:
        return None
def main():
    vystup = read_data("sequential.json", "unordered_numbers")
    vyhledani = linear_search(vystup, 9)
    return vystup,vyhledani




if __name__ == "__main__":
    print(main())
