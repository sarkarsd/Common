from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# generate the file report.pdf
report = SimpleDocTemplate("./report.pdf")

# generating style-sheet object
styles = getSampleStyleSheet()

# getting all available styles
print(styles.list())

# generating new custom_styles object
custom_styles = styles['title']
# take attributes from styles.list()
custom_styles.fontSize = 24

report_title = Paragraph("A Complete Inventory of My Fruit", custom_styles)
print(report_title)

# generating the actual report
report.build([report_title])

# <<<<<<<<<<<<<<<<<<<< GENERATING TABLE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

fruit_report = SimpleDocTemplate("./fruit_report.pdf")

fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

fruit_table_data = []
for k, v in fruit.items():
    fruit_table_data.append([k, v])

fruit_table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]

fruit_report_title = report_title
fruit_report_table = Table(data=fruit_table_data, style=fruit_table_style)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ADDING GRAPHICS TO (fruits_report) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

fruit_report_pie = Pie()
fruit_report_pie.x = 65
fruit_report_pie.y = 15
fruit_report_pie.width = 150
fruit_report_pie.height = 150
fruit_report_pie.data = []
fruit_report_pie.labels = []
for fruit_name in sorted(fruit):
    fruit_report_pie.data.append(fruit[fruit_name])
    fruit_report_pie.labels.append(fruit_name)

fruit_report_chart = Drawing()
fruit_report_chart.add(fruit_report_pie)

fruit_report.build([fruit_report_title, fruit_report_table, fruit_report_chart])
