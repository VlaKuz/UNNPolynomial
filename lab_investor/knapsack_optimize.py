import numpy as np
from numba import njit
NOMINAL_OBLIGATION = 1000
MONTH = 30
@njit(cache=True)
def knapsack_solver_optimize(investors_data, obligations, names):

    full_money = investors_data[2]
    list_reward = []
    items_list = []
    res_name = []
    for i in range(len(obligations) + 1):
        list_reward.append([0] * (full_money + 1))

    for idx, obligation in enumerate(obligations, 1):
        reward = NOMINAL_OBLIGATION * obligation[2] + (investors_data[0] - obligation[0] + MONTH) * obligation[2]\
                 - (int(10. * obligation[1] * obligation[2]))
        cost_item = int(10. * obligation[1] * obligation[2])

        for money in range(full_money + 1):
            if money < cost_item:
                list_reward[idx][money] = list_reward[idx - 1][money]
            else:
                list_reward[idx][money] = max(list_reward[idx - 1][money],list_reward[idx - 1][money - cost_item] + reward)

    current_money = full_money
    range_obligate = np.arange(1, len(obligations) + 1)
    reverse_range_obligate = np.flip(range_obligate)

    for obligation_count in reverse_range_obligate:
        if list_reward[obligation_count][current_money] != list_reward[obligation_count - 1][current_money]:
            if investors_data[2] - (int(10. * obligations[obligation_count - 1][1] * obligations[obligation_count - 1][2])) >= 0:
                items_list.append(obligations[obligation_count - 1])
                res_name.append(names[obligation_count - 1])
                investors_data[2] -= (int(10. * obligations[obligation_count - 1][1] * obligations[obligation_count - 1][2]))
            current_money -= (int(10. * obligations[obligation_count - 1][1] * obligations[obligation_count - 1][2]))

    items_list.reverse()
    total_reward = list_reward[len(obligations)][full_money]
    return investors_data, obligations, items_list, total_reward, res_name