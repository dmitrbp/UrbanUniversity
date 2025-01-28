import os
import json
import csv

class PriceMachine():
    
    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0
    
    def load_prices(self, file_path=''):
        '''
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
        '''
        files = [
            file for file in os.listdir(file_path)
            if os.path.isfile(os.path.join(file_path, file)) and 'price' in file
        ]
        for file in files:
            file_data = []
            with open(os.path.join(file_path, file), newline='') as f:
                reader = csv.reader(f)
                file_data = list(reader)
            columns = self._search_product_price_weight(file_data[0])
            for row_index in range(1, len(file_data)):
                self.data.append([
                    file_data[row_index][columns[0]],
                    int(file_data[row_index][columns[1]]),
                    int(file_data[row_index][columns[2]]),
                    file,
                    int(file_data[row_index][columns[1]]) / int(file_data[row_index][columns[2]])
                ])
        
    def _search_product_price_weight(self, headers):
        '''
            Возвращает номера столбцов
        '''
        names = [
            ["название", "продукт", "товар", "наименование"],
            ["цена", "розница"],
            ["фасовка", "масса", "вес"]
        ]
        columns = []
        for name_set in names:
            for header in headers:
                if header in name_set:
                    columns.append(headers.index(header))
        return columns

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
        pass
    
    def find_text(self, text):
        pass

    
pm = PriceMachine()
print(pm.load_prices('data'))

'''
    Логика работы программы
'''
print(sorted(pm.data, key=lambda x: x[4]))
print('the end')
# print(pm.export_to_html())
