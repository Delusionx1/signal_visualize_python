import sys

from PySide6.QtCharts import QChart, QChartView
from PySide6.QtGui import QPainter,QLinearGradient,QColor, QGradient,QFont
from PySide6.QtWidgets import QApplication, QMainWindow,QLabel
from PySide6.QtCore import QPoint,Qt
from Chart import Chart

if __name__ == "__main__":
    a = QApplication(sys.argv)
    window = QMainWindow()
    window = QMainWindow()
    chart = Chart()
    chart.setTitle("Dynamic spline chart")

    chart.setTitleFont(QFont('Cascadia Mono',pointSize=25))
    chart.setTitleBrush(Qt.white)
    chart.legend().hide()
    chart.setAnimationOptions(QChart.AllAnimations)

    chart_view = QChartView(chart)
    chart_view.setRenderHint(QPainter.Antialiasing)
    window.setCentralWidget(chart_view)

    window.resize(1500, 600)
    window.show()
    sys.exit(a.exec())
