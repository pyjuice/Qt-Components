from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot
from PyQt5.QtQuick import QQuickPaintedItem, QQuickItem
from PyQt5.QtGui import QPainter
from PyQt5 import QtCore
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DialType():
    FullDial = 0
    MinToMax = 1
    NoDial = 2

class RadialBar(QQuickPaintedItem):

    sizeChanged = pyqtSignal()
    startAngleChanged = pyqtSignal()
    spanAngleChanged = pyqtSignal()
    minValueChanged = pyqtSignal()
    maxValueChanged = pyqtSignal()
    valueChanged = pyqtSignal()
    dialWidthChanged = pyqtSignal()
    backgroundColorChanged = pyqtSignal()
    foregroundColorChanged = pyqtSignal()
    progressColorChanged = pyqtSignal()
    textColorChanged = pyqtSignal()
    suffixTextChanged = pyqtSignal()
    showTextChanged = pyqtSignal()
    penStyleChanged = pyqtSignal()
    dialTypeChanged = pyqtSignal()
    textFontChanged = pyqtSignal()


    def __init__(self, parent=None):
        super(RadialBar, self).__init__(parent)

        self.setWidth(200)
        self.setHeight(200)
        self.setSmooth(True)
        self.setAntialiasing(True)

        self._Size = 200
        self._StartAngle = 40
        self._SpanAngle = 280
        self._MinValue = 0
        self._MaxValue = 100
        self._Value = 50
        self._DialWidth = 15
        self._BackgroundColor = Qt.transparent
        self._DialColor = QColor(80,80,80)
        self._ProgressColor = QColor(135,26,5)
        self._TextColor = QColor(0, 0, 0)
        self._SuffixText = ""
        self._ShowText = True
        self._PenStyle = Qt.FlatCap
        self._DialType = DialType.MinToMax
        self._TextFont = QFont()

    def paint(self, painter):
        painter.save()

        size = min(self.width(), self.height())       
        self.setWidth(size)
        self.setHeight(size)
        rect = QRectF(0, 0, self.width(), self.height()) #self.boundingRect()
        painter.setRenderHint(QPainter.Antialiasing)
        pen = painter.pen()
        pen.setCapStyle(self._PenStyle)

        startAngle = -90 - self._StartAngle
        if DialType.FullDial != self._DialType:
            spanAngle = 0 - self._SpanAngle
        else:
            spanAngle = -360

        #Draw outer dial
        painter.save()
        pen.setWidth(self._DialWidth)
        pen.setColor(self._DialColor)
        painter.setPen(pen)
        offset = self._DialWidth / 2
        if self._DialType == DialType.MinToMax:
            painter.drawArc(rect.adjusted(offset, offset, -offset, -offset), startAngle * 16, spanAngle * 16)
        elif self._DialType == DialType.FullDial:
            painter.drawArc(rect.adjusted(offset, offset, -offset, -offset), -90 * 16, -360 * 16)
        else:
            pass
            #do not draw dial
        
        painter.restore()

        #Draw background
        painter.save()
        painter.setBrush(self._BackgroundColor)
        painter.setPen(self._BackgroundColor)
        inner = offset * 2
        painter.drawEllipse(rect.adjusted(inner, inner, -inner, -inner))
        painter.restore()

        #Draw progress text with suffix
        painter.save()
        painter.setFont(self._TextFont)
        pen.setColor(self._TextColor)
        painter.setPen(pen)
        if self._ShowText:
            painter.drawText(rect.adjusted(offset, offset, -offset, -offset), Qt.AlignCenter,str(self._Value) + self._SuffixText)
        else:
            painter.drawText(rect.adjusted(offset, offset, -offset, -offset), Qt.AlignCenter, self._SuffixText)
        painter.restore()

        #Draw progress bar
        painter.save()
        pen.setWidth(self._DialWidth)
        pen.setColor(self._ProgressColor)
        valueAngle = float(float(self._Value - self._MinValue)/float(self._MaxValue - self._MinValue)) * float(spanAngle)  #Map value to angle range
        painter.setPen(pen)
        painter.drawArc(rect.adjusted(offset, offset, -offset, -offset), startAngle * 16, valueAngle * 16)
        painter.restore()


    @QtCore.pyqtProperty(str, notify=sizeChanged)
    def size(self):
        return self._Size

    @size.setter
    def size(self, size):
        if self._Size == size:
            return
        self._Size = size
        self.sizeChanged.emit()

    @QtCore.pyqtProperty(int, notify=startAngleChanged)
    def startAngle(self):
        return self._StartAngle

    @startAngle.setter
    def startAngle(self, angle):
        if self._StartAngle == angle:
            return
        self._StartAngle = angle
        self.startAngleChanged.emit()

    @QtCore.pyqtProperty(int, notify=spanAngleChanged)
    def spanAngle(self):
        return self._SpanAngle

    @spanAngle.setter
    def spanAngle(self, angle):
        if self._SpanAngle == angle:
            return
        self._SpanAngle = angle
        self.spanAngleChanged.emit()

    @QtCore.pyqtProperty(int, notify=minValueChanged)
    def minValue(self):
        return self._MinValue

    @minValue.setter
    def minValue(self, value):
        if self._MinValue == value:
            return
        self._MinValue = value
        self.minValueChanged.emit()

    @QtCore.pyqtProperty(int, notify=maxValueChanged)
    def maxValue(self):
        return self._MaxValue

    @maxValue.setter
    def maxValue(self, value):
        if self._MaxValue == value:
            return
        self._MaxValue = value
        self.maxValueChanged.emit()

    @QtCore.pyqtProperty(float, notify=valueChanged)
    def value(self):
        return self._Value

    @value.setter
    def value(self, value):
        if self._Value == value:
            return
        self._Value = value
        self.valueChanged.emit()

    @QtCore.pyqtProperty(int, notify=dialWidthChanged)
    def dialWidth(self):
        return self._DialWidth


    @dialWidth.setter
    def dialWidth(self, width):
        if self._DialWidth == width:
            return
        self._DialWidth = width
        self.dialWidthChanged.emit()

    @QtCore.pyqtProperty(QColor, notify=backgroundColorChanged)
    def backgroundColor(self):
        return self._BackgroundColor

    @backgroundColor.setter
    def backgroundColor(self, color):
        if self._BackgroundColor == color:
            return
        self._BackgroundColor = color
        self.backgroundColorChanged.emit()

    @QtCore.pyqtProperty(QColor, notify=foregroundColorChanged)
    def foregroundColor(self):
        return self._ForegrounColor

    @foregroundColor.setter
    def foregroundColor(self, color):
        if self._DialColor == color:
            return
        self._DialColor = color
        self.foregroundColorChanged.emit()

    @QtCore.pyqtProperty(QColor, notify=progressColorChanged)
    def progressColor(self):
        return self._ProgressColor

    @progressColor.setter
    def progressColor(self, color):
        if self._ProgressColor == color:
            return
        self._ProgressColor = color
        self.progressColorChanged.emit()

    @QtCore.pyqtProperty(QColor, notify=textColorChanged)
    def textColor(self):
        return self._TextColor

    @textColor.setter
    def textColor(self, color):
        if self._TextColor == color:
            return
        self._TextColor = color
        self.textColorChanged.emit()  

    @QtCore.pyqtProperty(str, notify=suffixTextChanged)
    def suffixText(self):
        return self._SuffixText

    @suffixText.setter
    def suffixText(self, text):
        if self._SuffixText == text:
            return
        self._SuffixText = text
        self.suffixTextChanged.emit()

    @QtCore.pyqtProperty(str, notify=showTextChanged)
    def showText(self):
        return self._ShowText

    @showText.setter
    def showText(self, show):
        if self._ShowText == show:
            return
        self._ShowText = show

    @QtCore.pyqtProperty(Qt.PenCapStyle, notify=penStyleChanged)
    def penStyle(self):
        return self._PenStyle

    @penStyle.setter
    def penStyle(self, style):
        if self._PenStyle == style:
            return
        self._PenStyle = style
        self.penStyleChanged.emit()

    @QtCore.pyqtProperty(str, notify=dialTypeChanged)
    def dialType(self):
        return self._DialType

    @dialType.setter
    def dialType(self, type):
        if self._DialType == type:
            return
        self._DialType = type
        self.dialTypeChanged.emit()

    @QtCore.pyqtProperty(QFont, notify=textFontChanged)
    def textFont(self):
        return self._TextFont

    @textFont.setter
    def textFont(self, font):
        if self._TextFont == font:
            return
        self._TextFont = font
        self.textFontChanged.emit()
