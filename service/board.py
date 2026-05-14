from typing import List, Dict

def create_empty_table(row_num : int, col_num : int) -> List[List[Dict[str, str]]]:
    table = []
    for i in range(row_num):
        colm = []
        for j in range(col_num):
            colm.append({'type': " "})
        table.append(colm)
    return table

def get_represent_table(table : List[List[Dict[str,str]]]) -> List[List[str | None]]:
    row = []
    for row_index in table:
        col = []
        for col_index in row_index:
            col.append(col_index['type'])
        row.append(col)
    return row

def print_table(table : List[List[Dict[str,str]]]) -> None:
    new_table = get_represent_table(table)
    print(f'Choose a number from (0 - {len(table[0]) -1})')
    for row in new_table:
        print('| ' + ' | '.join(row) + ' |')
