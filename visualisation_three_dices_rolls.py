from dice import Diсe
from plotly.graph_objs import Bar, Layout    # импортируем класс самой столбцовой диаграммы и макета диаграммы
from plotly import offline    # импортируем функцию постороения диаграммы

die_0 = Diсe()
die_1 = Diсe()
die_2 = Diсe()

results = []
for roll_num in range(1000):
    result = die_0.roll() + die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
for v in range(1, die_0.num_sides + die_1.num_sides + die_2.num_sides + 1):
    frequency = results.count(v)
    frequencies.append(frequency)

# Визуализация
x_values = list(range(1, die_0.num_sides + die_1.num_sides + die_2.num_sides + 1))    # список результатов
data = [Bar(x=x_values, y=frequencies)]    # столбцовая диаграмма

# заголовки осей
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of result'}

# задаем макет диаграммы
my_layout = Layout(title='Result of rolling three D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

# вызываем функцию построения диаграммы
offline.plot({'data': data, 'layout': my_layout}, filename='../d6.html')




