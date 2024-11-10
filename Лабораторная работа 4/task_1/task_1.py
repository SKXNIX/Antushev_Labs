import json
# TODO решите задачу
def task() -> float:
    filename = "input.json"
    with open(filename,"r") as file:
        data = json.load(file)

    sum_ = 0
    for list_ in data:
        sum_ += list_.get("score") * list_.get("weight")

    return round(sum_,3)

print(task())
