import sys
from tabulate import tabulate
from itertools import zip_longest

from colorama import init
from colorama import Fore, Style

init(autoreset=True)

file1 = sys.argv[1]
file2 = sys.argv[2]

print(f"Opening {file1} and {file2}")

def clean(file_obj):
    file_raw = file_obj.read()
    file_raw = file_raw.strip()
    file_raw = file_raw.split(" -")
    file_raw = "\n-".join(file_raw)
    file_raw = file_raw.split("\n")
    return file_raw

def truncate(data, length=50):
    if len(data) > length:
        return data[:length]+"...(truncated)"
    else:
        return data

def compare_elems_in_list(l1, l2):
    new_l1 = []
    new_l2 = []

    # For L1
    for x in l1:
        if not x in l2:
            new_l1.append(f"<span style='color:red'><b>{x}</b></span>")
        else:
            new_l1.append(x)
    
    # For L1
    for x in l2:
        if not x in l1:
            new_l2.append(f"<span style='color:red'><b>{x}</b></span>")
        else:
            new_l2.append(x)
    
    return new_l1, new_l2

with open(file1, "r") as file1_obj, open(file2, "r") as file2_obj:
    file1_raw = clean(file1_obj)
    file2_raw = clean(file2_obj)

    file1_data, file2_data = compare_elems_in_list(file1_raw, file2_raw)


    print("\n\n")
    table = list(zip_longest(file1_data, file2_data, fillvalue="N/A"))
    table_header = [f"{file1} Includes ({len(file1_raw)})", f"{file2} Includes ({len(file2_raw)})"]
    print(tabulate(table, headers=table_header))

    f = open("output_ipath.html","w")
    f.write(tabulate(table, headers=table_header, tablefmt="unsafehtml"))
    f.close()

