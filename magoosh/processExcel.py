import xlrd


def save_object(obj, fn):
    import json
    with open(fn, 'w', encoding='utf-8') as outfile:
        json.dump(obj, outfile, indent=2, sort_keys=True, ensure_ascii = False)


current_row = 0
sheet_num = 0
input_total = 0
output_total = 0

# path to the file you want to extract data from
src = 'magoosh.xlsx'

book = xlrd.open_workbook(src)

# select the sheet that the data resids in
work_sheet = book.sheet_by_index(sheet_num)

# get the total number of rows
num_rows = work_sheet.nrows - 1

word_list = []
while current_row < num_rows:
    word = work_sheet.cell_value(current_row, 0)
    definition = work_sheet.cell_value(current_row, 1)
    definition = definition.splitlines(keepends=False)
    example = work_sheet.cell_value(current_row, 2)
    example = example.splitlines(keepends=False)
    word_list.append({
        'word': word,
        'definition': definition,
        'example': example,
    })

    current_row += 1

# print(word_list)
save_object(word_list, 'word-list.json')