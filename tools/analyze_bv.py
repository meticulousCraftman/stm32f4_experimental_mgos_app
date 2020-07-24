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

def gen_name_value(data):
    vars_name = []
    vars_value = []
    
    for x in data:
        tmp = x.split("=")
        if len(tmp) == 2:
            vars_name.append(tmp[0].strip())
            vars_value.append(truncate(tmp[1].strip()))
        else:
            vars_name.append(tmp[0].strip())
            vars_value.append("None")
        
    return vars_name, vars_value

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

    file1_build_vars_name, file1_build_vars_value = gen_name_value(file1_raw)
    file2_build_vars_name, file2_build_vars_value = gen_name_value(file2_raw)

    file1_build_vars_name, file2_build_vars_name = compare_elems_in_list(file1_build_vars_name, file2_build_vars_name)


    print("\n\n")
    table = list(zip_longest(file1_build_vars_name, file1_build_vars_value, file2_build_vars_name, file2_build_vars_value, fillvalue="N/A"))
    table_header = [f"{file1} Names ({len(file1_build_vars_name)})", f"{file1} Values", f"{file2} Names ({len(file2_build_vars_name)})", f"{file2} Values"]
    print(tabulate(table, headers=table_header))

    f = open("output_bv.html","w")
    f.write(tabulate(table, headers=table_header, tablefmt="unsafehtml"))
    f.close()

