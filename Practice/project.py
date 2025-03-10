import csv
import os
import time
from tabulate import tabulate


class PriceMachine:
    
    def __init__(self):
        self.data = []
        # self.result = ''
        # self.name_length = 0
    
    def load_prices(self, file_path=''):
        """
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт

            Допустимые названия для столбца с ценой:
                розница
                цена

            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        """
        files = [
            file for file in os.listdir(file_path)
            if os.path.isfile(os.path.join(file_path, file)) and 'price' in file
        ]
        for file in files:
            self._process_file(os.path.join(file_path, file), file)

    def _process_file(self, path, file):
        # with open(path, newline='') as f:
        #     reader = csv.reader(f)
        #     file_data = list(reader)
        file_data = []
        with open(path, 'r') as f:
            for line in f.readlines():
                linelist = line.strip().split(',')
                file_data.append(linelist)

        columns = self._search_product_price_weight(file_data[0])
        for row_index in range(1, len(file_data)):
            name = file_data[row_index][columns[0]]
            full_weigth = int(file_data[row_index][columns[1]])
            quantity = int(file_data[row_index][columns[2]])
            piece_weigth = round(full_weigth / quantity, 2)
            self.data.append([name, full_weigth, quantity, file, piece_weigth])

    def _search_product_price_weight(self, headers):
        """
            Возвращает номера столбцов
        """
        columns_names = [
            ["название", "продукт", "товар", "наименование"],
            ["цена", "розница"],
            ["фасовка", "масса", "вес"]
        ]
        columns_indexes = []
        for column_names in columns_names:
            for header in headers:
                if header in column_names:
                    columns_indexes.append(headers.index(header))
                    break
        return columns_indexes

    def export_to_html(self, fname='output.html'):
        result = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Номер</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Фасовка</th>
                    <th>Файл</th>
                    <th>Цена за кг.</th>
                </tr>
        '''
        for number, item in enumerate(self.data, start=1):
            name, price, weigth, file, unit_price = item
            result += '\n<tr>'
            result += f'<td>{number}</td>'
            result += f'<td>{name}</td>'
            result += f'<td>{price}</td>'
            result += f'<td>{weigth}</td>'
            result += f'<td>{file}</td>'
            result += f'<td>{unit_price}</td>'
            result += '</tr>'
        result += '\n</table></body>'
        with open(fname, 'w') as f:
            f.write(result)
        return 'Запись в файл завершена'

    def find_text(self, text):
        data_selected =sorted(filter(lambda x: text.lower() in x[0].lower(), self.data), key = lambda y: y[4])
        return [[index, *data] for index, data in enumerate(data_selected, start=1)]

    
pm = PriceMachine()
start = time.time()
pm.load_prices('data')
end = time.time()
print(f'Обработка файлов завершена за {end - start} секунд')

print('Начало цикла поиска')
while True:
    search_str = input('\nВведите строку для поиска. Выход-"exit" или "выход":')
    if search_str in ['exit', 'выход']:
        break
    data_printed = pm.find_text(search_str)
    print(tabulate(data_printed, headers=['№', 'Наименование', 'Цена', 'Вес', 'Файл', 'Цена за кг.'], floatfmt=".2f"))

print('Конец цикла поиска')
print(pm.export_to_html())
