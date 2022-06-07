import random

from PySide6.QtCharts import QChart, QSplineSeries, QValueAxis,QAreaSeries,QLineSeries
from PySide6.QtCore import Qt, QTimer, Slot, QPointF, QRect
from PySide6.QtGui import QPen, QPainter,QLinearGradient,QGradient,QColor

class Chart(QChart):
    def __init__(self, parent=None):
        super().__init__(QChart.ChartTypeCartesian, parent, Qt.WindowFlags())
        self._timer = QTimer()
        self._series = QLineSeries(self)
        self._titles = []
        self._axisX = QValueAxis()
        self._axisY = QValueAxis()
        self._step = 0
        self._x = 5
        self._y = 1
        self._count = 0
        self._timer.timeout.connect(self.handleTimeout)
        self._timer.setInterval(200)
        
        self.series_area_0 = QLineSeries()
        self.series_area_1 = QLineSeries()
        # self.series_area_0.replace()
        self.series_area_0.append(QPointF(0, 10))
        self.series_area_0.append(QPointF(15, 10))
        self.series_area_1.append(QPointF(0, -5))
        self.series_area_1.append(QPointF(15, -5))
        self.area_series = QAreaSeries(self.series_area_0, self.series_area_1)
        # Color on the block
        gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 1))
        gradient.setColorAt(0.0, QColor(0,0,255,50))
        gradient.setColorAt(0.5, QColor(0,0,255,255))
        gradient.setColorAt(1, QColor(0,0,255,50))
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        self.area_series.setBrush(gradient)
        block_pen = QPen(Qt.transparent)
        self.area_series.setPen(block_pen)

        green = QPen(0xFFFF55)
        green.setWidth(1.5)
        self._series.setPen(green)
        self._series.append(self._x, self._y)
        self._axisY.setGridLineVisible(False)
        self._axisX.setGridLineVisible(False)
        self._axisX.setLabelsVisible(False)

        self.addSeries(self.area_series)
        self.addSeries(self._series)
        self.addAxis(self._axisX, Qt.AlignBottom)
        self.addAxis(self._axisY, Qt.AlignLeft)
        self.setBackgroundBrush(Qt.black)
        self.area_series.attachAxis(self._axisX)
        self.area_series.attachAxis(self._axisY)
        self._series.attachAxis(self._axisX)
        self._series.attachAxis(self._axisY)
        self._axisX.setTickCount(200)
        self._axisX.setRange(0, 200)
        self._axisY.setRange(-5, 10)
        self._timer.start()

    @Slot()
    def handleTimeout(self):
        x = self.plotArea().width() / self._axisX.tickCount()
        y = (self._axisX.max() - self._axisX.min()) / self._axisX.tickCount()
        self._x += y
        if(self._x >= 15):
            self.series_area_0.replace([QPointF(self._x-15, 10),QPointF(self._x+3, 10)])
            self.series_area_1.replace([QPointF(self._x-15, -5),QPointF(self._x+3, -5)])
        self._y = random.uniform(0, 10) - 2.5
        self._series.append(self._x, self._y)
        self._count += 1
        if(self._count > 160):
            self._axisX.setRange(max(0, int(self._x) - 160), self._x+40)
        if self._x == 10000:
            self._timer.stop()