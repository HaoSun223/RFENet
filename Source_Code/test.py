import csv

def extract_allergies(text):
    allergies = []
    allergy_index = text.find('过敏')
    while allergy_index != -1:
        separators = ['，', '。', ',', '.', ';', '；', ':', '：', '？', '?']
        separator_index = -1
        for separator in separators:
            separator_index = max(separator_index, text.rfind(separator, 0, allergy_index))

        if separator_index == -1:
            substr = text[:allergy_index]
        else:
            substr = text[separator_index + 1: allergy_index]

        if '否认' not in substr:
            allergies.append(substr.strip() + '过敏')

        text = text[allergy_index + 2:]
        allergy_index = text.find('过敏')

    return ';'.join(allergies)

def process_csv(input_file, output_file):
    rows = []
    keywords = ['对', '存在', '患', '有', '患者', '的']
    with open(input_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            allergies = []
            for item in row:
                if '过敏' in item and '过敏反应不详' not in item:
                    for keyword in keywords:
                        item = item.replace(keyword, '')
                    if '不存在' not in item and '没有' not in item:
                        allergies.append(extract_allergies(item))
            if not allergies:
                allergies.append('无过敏')
            current_row = {'过敏信息': ';'.join(allergies)}
            rows.append(current_row)

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['过敏信息']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


input_file = 'input.csv'
output_file = 'output.csv'
process_csv(input_file, output_file)
