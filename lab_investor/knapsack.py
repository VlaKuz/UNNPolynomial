def additonal_new_item(investor_data, item):
    if investor_data["money"] - get_amount(item) >= 0:
        investor_data["items"].append(item)
        investor_data["money"] -= get_amount(item)

def get_amount(obligation):
    return (int(10. * obligation["price"] * obligation["amount"])) #10. = NOMINAL_OBLIGATION / 100.

def get_reward(days, obligation):
    NOMINAL_OBLIGATION = 1000
    MONTH = 30
    return (NOMINAL_OBLIGATION * obligation["amount"] + (days - obligation["day"] + MONTH) * obligation["amount"]
            - get_amount(obligation))

def knapsack_solver(investors_data, obligations):
    if len(obligations) == 0:
        raise ValueError('Empty obligation list. Check your obligation list')

    full_money = investors_data["money"]
    list_reward = []
    for i in range(len(obligations) + 1):
        list_reward.append([0] * (full_money + 1))

    for idx, obligation in enumerate(obligations, 1):
        reward = get_reward(investors_data["days"], obligation)
        cost_item = get_amount(obligation)

        for money in range(full_money + 1):
            if money < cost_item:
                list_reward[idx][money] = list_reward[idx - 1][money]
            else:
                list_reward[idx][money] = max(list_reward[idx - 1][money],list_reward[idx - 1][money - cost_item] + reward)

    current_money = full_money
    range_obligate = range(1, len(obligations) + 1)
    reverse_range_obligate = reversed(range_obligate)

    for obligation_count in reverse_range_obligate:
        if list_reward[obligation_count][current_money] != list_reward[obligation_count - 1][current_money]:
            additonal_new_item(investors_data, (obligations[obligation_count - 1]))
            current_money -= get_amount(obligations[obligation_count - 1])

    investors_data["items"].reverse()
    investors_data["total_reward"] = list_reward[len(obligations)][full_money]
    return investors_data, obligations