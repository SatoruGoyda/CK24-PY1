# TODO решите задачу
import json
def task() -> float:
     with open('input.json', 'r') as json_file:
            data = json.load(json_file)
            total_sum = sum(item['score'] * item['weight'] for item in data)
            return round(total_sum, 3)
print(task())
