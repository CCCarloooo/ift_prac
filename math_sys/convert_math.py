import json_lines
import json
import torch

def convert(data_idx, data_case):

    gpt_str = item['answer']
    human_str = item['question']
    conversation = {
        'id': f'conv_{data_idx}',
        'conversations': [
            {
                'from': 'human',
                'value': human_str,
            },
            {
                'from': 'gpt',
                'value': gpt_str
            }
        ]
    }
    return conversation

if __name__ == '__main__':

    dataset = []
    with open('/home/mengxiangdi/grade-school-math/grade_school_math/data/train.jsonl', 'rb') as f: 
        for item in json_lines.reader(f):
            dataset.append(item)

    dataset = [
        convert(i, x) for i, x in enumerate(dataset)
    ]
    json.dump(dataset, open('math_train.json', 'w'))