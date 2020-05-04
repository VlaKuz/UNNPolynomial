import os
import time

import knapsack
import knapsack_optimize
import mem_use_win32
import pprint
import numpy as np
from argparse import  ArgumentParser

def parse_data_classic(file_path):
    with open(file_path) as f:
        days, items, money = f.readline().split()
        investor_data = {"days": int(days),"items": int(items),"money": int(money),"items": [], "total_reward": None }
        obligations = []
        for l in f:
            day, name, price, amount = l.split()
            obligations.append({"day": int(day),"name": str(name),"price": float(price),"amount": int(amount)})
    return investor_data, obligations

def parse_data_optimize(file_path):
    with open(file_path) as f:
        days, items, money = f.readline().split()
        investor_data = np.array([int(days), int(items), int(money)])
        obligations = []
        names = []
        for l in f:
            day, name, price, amount = l.split()
            obligations.append([int(day), float(price), int(amount)])
            names.append(str(name))
        obligations = np.array(obligations)
    return investor_data, obligations, names

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-a', '--algorithm', default='base', help='Base or Opt alg.', required=True)
    parser.add_argument('-i', '--input_file', default='input.txt', help='Input File', required=True)
    parser.add_argument('-o', '--output_file', default='output.txt', help='Output File', required=True)
    args = parser.parse_args()
    in_algorithm = args.algorithm
    in_input_file = args.input_file
    in_output_file = args.output_file

    test = os.path.join(in_input_file)

    investors_data, obligations = parse_data_classic(test)
    investors_data_opt, obligations_opt, names = parse_data_optimize(test)

    if in_algorithm == 'base':
        print('--------------------------------------')
        print('MEMORY INFO BEFORE ALG:')
        pprint.pprint(mem_use_win32.get_memory_info())
        print('--------------------------------------')
        first_v_time = time.time()
        knapsack.knapsack_solver(investors_data, obligations)
        first_v_time = time.time() - first_v_time
        print('--------------------------------------')
        print('MEMORY INFO AFTER ALG:')
        pprint.pprint(mem_use_win32.get_memory_info())
        print('--------------------------------------')
        print('Standart Algorithm without optimization:')
        print('Time: {:.4f} ms'.format(first_v_time * 1000))
        print('--------------------------------------')
        print(investors_data["total_reward"])
        for obligation in investors_data["items"]:
            print(str(obligation["day"]) + ' ' + str(obligation["name"]) + ' ' + str(obligation["price"]) + ' ' + str(
                obligation["amount"]))
        print('--------------------------------------')
        f = open("output.txt", "w")
        f.write(str(investors_data["total_reward"]) + '\n')
        for obligation in investors_data["items"]:
            f.write(str(obligation["day"]) + ' ' + str(obligation["name"]) + ' ' + str(obligation["price"]) + ' ' + str(
                obligation["amount"]) + '\n')
        f.close()
    elif in_algorithm == 'opt':
        print('--------------------------------------')
        print('MEMORY INFO BEFORE ALG:')
        pprint.pprint(mem_use_win32.get_memory_info())
        print('--------------------------------------')
        second_v_time = time.time()
        investors_data_opt_res, obligations_opt_res, item_list_res, total_reward_res, names_res = \
            knapsack_optimize.knapsack_solver_optimize(investors_data_opt, obligations_opt, names)
        second_v_time = time.time() - second_v_time
        print('--------------------------------------')
        print('MEMORY INFO AFTER ALG:')
        pprint.pprint(mem_use_win32.get_memory_info())
        print('--------------------------------------')
        print('Numpy Algorithm with Numba optimization:')
        print('Time: {:.4f} ms'.format(second_v_time * 1000))
        print('--------------------------------------')
        print(total_reward_res)
        for index in range(len(item_list_res)):
            print(str(int(item_list_res[index][0])) + ' ' + names_res[index] + ' ' + str(item_list_res[index][1]) + ' ' + str(int(item_list_res[index][2])))
        print('--------------------------------------')
        f = open("output.txt", "w")
        f.write(str(total_reward_res) + '\n')
        for index in range(len(item_list_res)):
            f.write(str(int(item_list_res[index][0])) + ' ' + names_res[index] + ' ' + str(item_list_res[index][1]) + ' ' + str(int(item_list_res[index][2])) + '\n')
        f.close()

