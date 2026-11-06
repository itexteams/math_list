import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang3_p4_b5_c2_hh10(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x1=randint(-10,10)
                y1=randint(-10,10)
                x2=randint(-10,10)
                y2=randint(-10,10)
                x3=randint(-10,10)
                y3=randint(-10,10)
                while (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)==0:
                    x1=randint(-10,10)
                    y1=randint(-10,10)
                    x2=randint(-10,10)
                    y2=randint(-10,10)
                    x3=randint(-10,10)
                    y3=randint(-10,10)
                dab=nsimplify(sqrt((x2-x1)**2+(y2-y1)**2))
                dac=nsimplify(sqrt((x3-x1)**2+(y3-y1)**2))
                dbc=nsimplify(sqrt((x3-x2)**2+(y3-y2)**2))
                tvh1=(x2-x1)*(x3-x2)+(y2-y1)*(y3-y2)
                tvh2=(x3-x1)*(x3-x2)+(y3-y1)*(y3-y2)
                tvh3=(x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)
                tb=(x1-x2)*(x3-x2)+(y1-y2)*(y3-y2)
                tc=(x1-x3)*(x2-x3)+(y1-y3)*(y2-y3)
                cosa=nsimplify(tvh3/(dab*dac))
                cosb=nsimplify(tb/(dab*dbc))
                cosc=nsimplify(tc/(dbc*dac))


                number = Decimal(float(cosa))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ với ba điểm $A(%s;%s)$, $B(%s;%s)$ và  $C(%s;%s)$$zz$ Tính $\\cos \\widehat{BAC}$$zz$ (Kết quả làm tròn đến hàng phần chục)$zz$ \n'%(latex(x1),latex(y1),latex(x2),latex(y2),latex(x3),latex(y3))
                                )

                # Nội dung lời giải
                loigiai = ('Dễ thấy $\\widehat{BAC}=\\left(\\vec{AB},\\vec{AC}\\right)$$zz$\\\\ \n'
                                'Ta có $\\vec{AB}=(%s;%s)$ và $\\vec{AC}=(%s;%s)$$zz$\\\\ \n'
                                '\\hspace*{1cm} $\\abs{\\vec{AB}}=\\sqrt{(%s)^2+(%s)^2}=%s$zz$$\\\\ \n'
                                '\\hspace*{1cm} $\\abs{\\vec{AC}}=\\sqrt{(%s)^2+(%s)^2}=%s$zz$$\\\\ \n'
                                '\\hspace*{1cm} $\\vec{AB}\\cdot\\vec{AC}=%s\\cdot(%s)+%s\\cdot(%s)=%s$$zz$\\\\ \n'
                                'Suy ra\\\\ \n'
                                '\\hspace*{1cm} $\\cos \\widehat{BAC}=\\cos \\left(\\vec{AB},\\vec{AC}\\right)=\\dfrac{\\vec{AB}\\cdot \\vec{AC}}{\\abs{\\vec{AB}}\\cdot \\abs{\\vec{AC}}}=\\dfrac{%s}{%s\\cdot %s}=%s\\approx %s$$zz$'
                                %(latex(x2-x1),latex(y2-y1),latex(x3-x1),latex(y3-y1),
                                latex(x2-x1),latex(y2-y1),latex(dab),latex(x3-x1),latex(y3-y1),latex(dac),
                                latex(x2-x1),latex(x3-x1),latex(y2-y1),latex(y3-y1),latex(tvh3),
                                latex(tvh3),latex(dab),latex(dac),latex(cosa),latex(kq)
                                )
                            )

            if dang=='2':
                # Khai báo biến
                x1=randint(-10,10)
                y1=randint(-10,10)
                x2=randint(-10,10)
                y2=randint(-10,10)
                x3=randint(-10,10)
                y3=randint(-10,10)
                while (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)==0:
                    x1=randint(-10,10)
                    y1=randint(-10,10)
                    x2=randint(-10,10)
                    y2=randint(-10,10)
                    x3=randint(-10,10)
                    y3=randint(-10,10)
                dab=nsimplify(sqrt((x2-x1)**2+(y2-y1)**2))
                dac=nsimplify(sqrt((x3-x1)**2+(y3-y1)**2))
                dbc=nsimplify(sqrt((x3-x2)**2+(y3-y2)**2))
                tvh1=(x2-x1)*(x3-x2)+(y2-y1)*(y3-y2)
                tvh2=(x3-x1)*(x3-x2)+(y3-y1)*(y3-y2)
                tvh3=(x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)
                tb=(x1-x2)*(x3-x2)+(y1-y2)*(y3-y2)
                tc=(x1-x3)*(x2-x3)+(y1-y3)*(y2-y3)
                cosa=nsimplify(tvh3/(dab*dac))
                cosb=nsimplify(tb/(dab*dbc))
                cosc=nsimplify(tc/(dbc*dac))


                number = Decimal(float(cosb))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ với ba điểm $A(%s;%s)$, $B(%s;%s)$ và  $C(%s;%s)$$zz$ Tính $\\cos \\widehat{ABC}$$zz$ (Kết quả làm tròn đến hàng phần chục)$zz$ \n'%(latex(x1),latex(y1),latex(x2),latex(y2),latex(x3),latex(y3))
                                )

                # Nội dung lời giải
                loigiai = ('Dễ thấy $\\widehat{ABC}=\\left(\\vec{BA},\\vec{BC}\\right)$$zz$\\\\ \n'
                                'Ta có $\\vec{BA}=(%s;%s)$ và $\\vec{BC}=(%s;%s)$$zz$\\\\ \n'
                                '\\hspace*{1cm} $\\abs{\\vec{BA}}=\\sqrt{(%s)^2+(%s)^2}=%s$zz$$\\\\ \n'
                                '\\hspace*{1cm} $\\abs{\\vec{BC}}=\\sqrt{(%s)^2+(%s)^2}=%s$zz$$\\\\ \n'
                                '\\hspace*{1cm} $\\vec{BA}\\cdot\\vec{BC}=%s\\cdot(%s)+%s\\cdot(%s)=%s$$zz$\\\\ \n'
                                'Suy ra\\\\ \n'
                                '\\hspace*{1cm} $\\cos \\widehat{ABC}=\\cos \\left(\\vec{BA},\\vec{BC}\\right)=\\dfrac{\\vec{BA}\\cdot \\vec{BC}}{\\abs{\\vec{BA}}\\cdot \\abs{\\vec{BC}}}=\\dfrac{%s}{%s\\cdot %s}=%s\\approx %s$$zz$'
                                %(latex(x1-x2),latex(y1-y2),latex(x3-x2),latex(y3-y2),
                                latex(x1-x2),latex(y1-y2),latex(dab),latex(x3-x2),latex(y3-y2),latex(dbc),
                                latex(x1-x2),latex(x3-x2),latex(y1-y2),latex(y3-y2),latex(tb),
                                latex(tb),latex(dab),latex(dbc),latex(cosb),latex(kq)
                                )
                            )

            if dang=='3':
                # Khai báo biến
                x1=randint(-10,10)
                y1=randint(-10,10)
                x2=randint(-10,10)
                y2=randint(-10,10)
                x3=randint(-10,10)
                y3=randint(-10,10)
                while (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)==0:
                    x1=randint(-10,10)
                    y1=randint(-10,10)
                    x2=randint(-10,10)
                    y2=randint(-10,10)
                    x3=randint(-10,10)
                    y3=randint(-10,10)
                dab=nsimplify(sqrt((x2-x1)**2+(y2-y1)**2))
                dac=nsimplify(sqrt((x3-x1)**2+(y3-y1)**2))
                dbc=nsimplify(sqrt((x3-x2)**2+(y3-y2)**2))
                tvh1=(x2-x1)*(x3-x2)+(y2-y1)*(y3-y2)
                tvh2=(x3-x1)*(x3-x2)+(y3-y1)*(y3-y2)
                tvh3=(x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)
                tb=(x1-x2)*(x3-x2)+(y1-y2)*(y3-y2)
                tc=(x1-x3)*(x2-x3)+(y1-y3)*(y2-y3)
                cosa=nsimplify(tvh3/(dab*dac))
                cosb=nsimplify(tb/(dab*dbc))
                cosc=nsimplify(tc/(dbc*dac))


                number = Decimal(float(cosc))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ với ba điểm $A(%s;%s)$, $B(%s;%s)$ và  $C(%s;%s)$$zz$ Tính $\\cos \\widehat{ACB}$$zz$ (Kết quả làm tròn đến hàng phần chục)$zz$ \n'%(latex(x1),latex(y1),latex(x2),latex(y2),latex(x3),latex(y3))
                                )

                # Nội dung lời giải
                loigiai = ('Dễ thấy $\\widehat{ACB}=\\left(\\vec{CA},\\vec{CB}\\right)$$zz$\\\\ \n'
                                'Ta có $\\vec{CA}=(%s;%s)$ và $\\vec{CB}=(%s;%s)$$zz$\\\\ \n'
                                '\\hspace*{1cm} $\\abs{\\vec{CA}}=\\sqrt{(%s)^2+(%s)^2}=%s$zz$$\\\\ \n'
                                '\\hspace*{1cm} $\\abs{\\vec{CB}}=\\sqrt{(%s)^2+(%s)^2}=%s$zz$$\\\\ \n'
                                '\\hspace*{1cm} $\\vec{CA}\\cdot\\vec{CB}=%s\\cdot(%s)+%s\\cdot(%s)=%s$$zz$\\\\ \n'
                                'Suy ra\\\\ \n'
                                '\\hspace*{1cm} $\\cos \\widehat{ACB}=\\cos \\left(\\vec{CA},\\vec{CB}\\right)=\\dfrac{\\vec{CA}\\cdot \\vec{CB}}{\\abs{\\vec{CA}}\\cdot \\abs{\\vec{CB}}}=\\dfrac{%s}{%s\\cdot %s}=%s\\approx %s$$zz$'
                                %(latex(x1-x3),latex(y1-y3),latex(x2-x3),latex(y2-y3),
                                latex(x1-x3),latex(y1-y3),latex(dac),latex(x2-x3),latex(y2-y3),latex(dbc),
                                latex(x1-x3),latex(x2-x3),latex(y1-y3),latex(y2-y3),latex(tc),
                                latex(tc),latex(dac),latex(dbc),latex(cosc),latex(kq)
                                )
                            )


            if dang=='4':
                # Khai báo biến
                x1=randint(-10,10)
                y1=randint(-10,10)
                x2=randint(-10,10)
                y2=randint(-10,10)
                x3=randint(-10,10)
                y3=randint(-10,10)
                while (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)==0:
                    x1=randint(-10,10)
                    y1=randint(-10,10)
                    x2=randint(-10,10)
                    y2=randint(-10,10)
                    x3=randint(-10,10)
                    y3=randint(-10,10)
                dab=nsimplify(sqrt((x2-x1)**2+(y2-y1)**2))
                dac=nsimplify(sqrt((x3-x1)**2+(y3-y1)**2))
                dbc=nsimplify(sqrt((x3-x2)**2+(y3-y2)**2))
                tvh1=(x2-x1)*(x3-x2)+(y2-y1)*(y3-y2)
                tvh2=(x3-x1)*(x3-x2)+(y3-y1)*(y3-y2)
                tvh3=(x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)
                tb=(x1-x2)*(x3-x2)+(y1-y2)*(y3-y2)
                tc=(x1-x3)*(x2-x3)+(y1-y3)*(y2-y3)
                cosa=nsimplify(tvh3/(dab*dac))
                cosb=nsimplify(tb/(dab*dbc))
                cosc=nsimplify(tc/(dbc*dac))
                sda=math.degrees(math.acos(cosa))


                number = Decimal(float(sda))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ với ba điểm $A(%s;%s)$, $B(%s;%s)$ và  $C(%s;%s)$$zz$ Tính số đo góc $\\widehat{BAC}$$zz$ (Kết quả làm tròn đến hàng đơn vị)$zz$ \n'%(latex(x1),latex(y1),latex(x2),latex(y2),latex(x3),latex(y3))
                                )

                # Nội dung lời giải
                loigiai = ('Dễ thấy $\\widehat{BAC}=\\left(\\vec{AB},\\vec{AC}\\right)$$zz$\\\\ \n'
                                'Ta có $\\vec{AB}=(%s;%s)$ và $\\vec{AC}=(%s;%s)$$zz$\\\\ \n'
                                '\\hspace*{1cm} $\\abs{\\vec{AB}}=\\sqrt{(%s)^2+(%s)^2}=%s$zz$$\\\\ \n'
                                '\\hspace*{1cm} $\\abs{\\vec{AC}}=\\sqrt{(%s)^2+(%s)^2}=%s$zz$$\\\\ \n'
                                '\\hspace*{1cm} $\\vec{AB}\\cdot\\vec{AC}=%s\\cdot(%s)+%s\\cdot(%s)=%s$$zz$\\\\ \n'
                                'Suy ra\\\\ \n'
                                '\\hspace*{1cm} $\\cos \\widehat{BAC}=\\cos \\left(\\vec{AB},\\vec{AC}\\right)=\\dfrac{\\vec{AB}\\cdot \\vec{AC}}{\\abs{\\vec{AB}}\\cdot \\abs{\\vec{AC}}}=\\dfrac{%s}{%s\\cdot %s}=%s$$zz$\\\\ \n'
                                'Vậy số đo góc $\\widehat{BAC} \\approx %s ^{\\circ}$zz$$'
                                %(latex(x2-x1),latex(y2-y1),latex(x3-x1),latex(y3-y1),
                                latex(x2-x1),latex(y2-y1),latex(dab),latex(x3-x1),latex(y3-y1),latex(dac),
                                latex(x2-x1),latex(x3-x1),latex(y2-y1),latex(y3-y1),latex(tvh3),
                                latex(tvh3),latex(dab),latex(dac),latex(cosa),latex(kq)
                                )
                            )

            if dang=='5':
                # Khai báo biến
                x1=randint(-10,10)
                y1=randint(-10,10)
                x2=randint(-10,10)
                y2=randint(-10,10)
                x3=randint(-10,10)
                y3=randint(-10,10)
                while (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)==0:
                    x1=randint(-10,10)
                    y1=randint(-10,10)
                    x2=randint(-10,10)
                    y2=randint(-10,10)
                    x3=randint(-10,10)
                    y3=randint(-10,10)
                dab=nsimplify(sqrt((x2-x1)**2+(y2-y1)**2))
                dac=nsimplify(sqrt((x3-x1)**2+(y3-y1)**2))
                dbc=nsimplify(sqrt((x3-x2)**2+(y3-y2)**2))
                tvh1=(x2-x1)*(x3-x2)+(y2-y1)*(y3-y2)
                tvh2=(x3-x1)*(x3-x2)+(y3-y1)*(y3-y2)
                tvh3=(x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)
                tb=(x1-x2)*(x3-x2)+(y1-y2)*(y3-y2)
                tc=(x1-x3)*(x2-x3)+(y1-y3)*(y2-y3)
                cosa=nsimplify(tvh3/(dab*dac))
                cosb=nsimplify(tb/(dab*dbc))
                cosc=nsimplify(tc/(dbc*dac))
                sdb=math.degrees(math.acos(cosb))

                number = Decimal(float(sdb))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ với ba điểm $A(%s;%s)$, $B(%s;%s)$ và  $C(%s;%s)$$zz$ Tính số đo góc $\\widehat{ABC}$$zz$ (Kết quả làm tròn đến hàng đơn vị)$zz$ \n'%(latex(x1),latex(y1),latex(x2),latex(y2),latex(x3),latex(y3))
                                )

                # Nội dung lời giải
                loigiai = ('Dễ thấy $\\widehat{ABC}=\\left(\\vec{BA},\\vec{BC}\\right)$$zz$\\\\ \n'
                                'Ta có $\\vec{BA}=(%s;%s)$ và $\\vec{BC}=(%s;%s)$$zz$\\\\ \n'
                                '\\hspace*{1cm} $\\abs{\\vec{BA}}=\\sqrt{(%s)^2+(%s)^2}=%s$zz$$\\\\ \n'
                                '\\hspace*{1cm} $\\abs{\\vec{BC}}=\\sqrt{(%s)^2+(%s)^2}=%s$zz$$\\\\ \n'
                                '\\hspace*{1cm} $\\vec{BA}\\cdot\\vec{BC}=%s\\cdot(%s)+%s\\cdot(%s)=%s$$zz$\\\\ \n'
                                'Suy ra\\\\ \n'
                                '\\hspace*{1cm} $\\cos \\widehat{ABC}=\\cos \\left(\\vec{BA},\\vec{BC}\\right)=\\dfrac{\\vec{BA}\\cdot \\vec{BC}}{\\abs{\\vec{BA}}\\cdot \\abs{\\vec{BC}}}=\\dfrac{%s}{%s\\cdot %s}=%s$$zz$\\\\ \n'
                                'Vậy số đo góc $\\widehat{ABC}\\approx %s ^{\\circ}$zz$$'
                                %(latex(x1-x2),latex(y1-y2),latex(x3-x2),latex(y3-y2),
                                latex(x1-x2),latex(y1-y2),latex(dab),latex(x3-x2),latex(y3-y2),latex(dbc),
                                latex(x1-x2),latex(x3-x2),latex(y1-y2),latex(y3-y2),latex(tb),
                                latex(tb),latex(dab),latex(dbc),latex(cosb),latex(kq)
                                )
                            )

            if dang=='6':
                # Khai báo biến
                x1=randint(-10,10)
                y1=randint(-10,10)
                x2=randint(-10,10)
                y2=randint(-10,10)
                x3=randint(-10,10)
                y3=randint(-10,10)
                while (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)==0:
                    x1=randint(-10,10)
                    y1=randint(-10,10)
                    x2=randint(-10,10)
                    y2=randint(-10,10)
                    x3=randint(-10,10)
                    y3=randint(-10,10)
                dab=nsimplify(sqrt((x2-x1)**2+(y2-y1)**2))
                dac=nsimplify(sqrt((x3-x1)**2+(y3-y1)**2))
                dbc=nsimplify(sqrt((x3-x2)**2+(y3-y2)**2))
                tvh1=(x2-x1)*(x3-x2)+(y2-y1)*(y3-y2)
                tvh2=(x3-x1)*(x3-x2)+(y3-y1)*(y3-y2)
                tvh3=(x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)
                tb=(x1-x2)*(x3-x2)+(y1-y2)*(y3-y2)
                tc=(x1-x3)*(x2-x3)+(y1-y3)*(y2-y3)
                cosa=nsimplify(tvh3/(dab*dac))
                cosb=nsimplify(tb/(dab*dbc))
                cosc=nsimplify(tc/(dbc*dac))
                sdc=math.degrees(math.acos(cosc))

                number = Decimal(float(sdc))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ với ba điểm $A(%s;%s)$, $B(%s;%s)$ và  $C(%s;%s)$$zz$ Tính số đo góc $\\widehat{ACB}$$zz$ (Kết quả làm tròn đến hàng đơn vị) \n'%(latex(x1),latex(y1),latex(x2),latex(y2),latex(x3),latex(y3))
                                )

                # Nội dung lời giải
                loigiai = ('Dễ thấy $\\widehat{ACB}=\\left(\\vec{CA},\\vec{CB}\\right)$$zz$\\\\ \n'
                                'Ta có $\\vec{CA}=(%s;%s)$ và $\\vec{CB}=(%s;%s)$$zz$\\\\ \n'
                                '\\hspace*{1cm} $\\abs{\\vec{CA}}=\\sqrt{(%s)^2+(%s)^2}=%s$zz$$\\\\ \n'
                                '\\hspace*{1cm} $\\abs{\\vec{CB}}=\\sqrt{(%s)^2+(%s)^2}=%s$zz$$\\\\ \n'
                                '\\hspace*{1cm} $\\vec{CA}\\cdot\\vec{CB}=%s\\cdot(%s)+%s\\cdot(%s)=%s$$zz$\\\\ \n'
                                'Suy ra\\\\ \n'
                                '\\hspace*{1cm} $\\cos \\widehat{ACB}=\\cos \\left(\\vec{CA},\\vec{CB}\\right)=\\dfrac{\\vec{CA}\\cdot \\vec{CB}}{\\abs{\\vec{CA}}\\cdot \\abs{\\vec{CB}}}=\\dfrac{%s}{%s\\cdot %s}=%s$$zz$\\\\ \n'
                                'Vậy số đo góc $\\widehat{ACB}\\approx %s ^{\\circ}$zz$$'
                                %(latex(x1-x3),latex(y1-y3),latex(x2-x3),latex(y2-y3),
                                latex(x1-x3),latex(y1-y3),latex(dac),latex(x2-x3),latex(y2-y3),latex(dbc),
                                latex(x1-x3),latex(x2-x3),latex(y1-y3),latex(y2-y3),latex(tc),
                                latex(tc),latex(dac),latex(dbc),latex(cosc),latex(kq)
                                )
                            )



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace('--', '+').replace('+-', '-')
            return content 

