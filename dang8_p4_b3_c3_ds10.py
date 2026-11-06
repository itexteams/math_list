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


def bt_dang8_p4_b3_c3_ds10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='2':
                # Khai báo biến
                x1=randint(1,20)
                x2=randint(1,20)
                x3=randint(1,20)
                x4=randint(1,20)
                x5=randint(1,20)
                x6=randint(1,20)
                x7=randint(1,20)
                x8=randint(1,20)
                x9=randint(1,20)
                x10=randint(1,20)
                x11=randint(1,3)
                x12=randint(1,20)
                x13=randint(1,20)
                x14=randint(20,50)
                x15=randint(25,35)
                x16=randint(1,20)
                x17=randint(1,3)
                x18=randint(1,3)

                xtb = Decimal(float((x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12+x13+x14+x15+x16+x17+x18)/18)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Đưa các số vào danh sách
                numbers = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10,x11,x12,x13,x14,x15,x16,x17,x18]

                # Sắp xếp danh sách theo thứ tự tăng dần
                numbers.sort()

                # Tìm hai số đứng giữa
                x_9 = numbers[8]
                x_10 = numbers[9]
                me=(x_9+x_10)/2

                x_5 = numbers[4]
                q1=x_5 

                x_14 = numbers[13]
                q3=x_14
                delta_q=q3-q1

                gtnn=q1-1.5*delta_q
                gtln=q3+1.5*delta_q

                #Điếm giá trị bất thường
                outliers = [x for x in numbers if x < gtnn or x > gtln]
                count_outliers = len(outliers)  # Số lượng giá trị nằm ngoài khoảng

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho mẫu số liệu \n'
                                '$$%s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s$$'
                                'Tìm số giá trị bất thường của mẫu số liệu$zz$'

                                %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),latex(x6),latex(x7),latex(x8),latex(x9),latex(x10),latex(x11),latex(x12),latex(x13),latex(x14),latex(x15),latex(x16),latex(x17),latex(x18)
                                ))

                # Nội dung lời giải
                loigiai=('Xắp xếp dãy số theo thứ tự tăng dần ta được \\\\ \n'
                        '$$%s$$ \n'
                        'Tổng của mẫu số liệu là $n=10$ nên \\\\ \n'
                        '\\hspace*{1cm} Trung vị của mẫu số liệu là $M_e=\\dfrac{x_5+x_6}{2}=\\dfrac{%s+%s}{2}=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=x_3=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Tứ phân vị thứ nhất của mẫu số liệu là $Q_3=x_8=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Khoảng tứ phân vị là $\\Delta_Q=Q_3-Q_1=%s-%s=%s$$zz$ \\\\ \n'
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $Q_1-1,5\\Delta_Q=%s$ và $Q_3+1,5\\Delta_Q=%s$$zz$ \\\\ \n'
                        'Vậy trong dãy số liệu có $%s$ giá trị được xem là bất thường$zz$'
                        %(latex(numbers),
                        latex(x_9),latex(x_10),latex(me),
                        latex(q1),latex(q3),
                        latex(q3),latex(q1),latex(q3-q1),
                        latex(q1-1.5*(q3-q1)),latex(q3+1.5*(q3-q1)),
                        latex(count_outliers)
                        ))

            if dang=='1':
                # Khai báo biến
                x1=randint(1,20)
                x2=randint(1,20)
                x3=randint(1,20)
                x4=randint(1,20)
                x5=randint(1,20)
                x6=randint(1,20)
                x7=randint(1,20)
                x8=randint(1,20)
                x9=randint(1,20)
                x10=randint(1,20)

                xtb = Decimal(float((x1+x2+x3+x4+x5+x6+x7+x8+x9+x10)/10)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Đưa các số vào danh sách
                numbers = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]

                # Sắp xếp danh sách theo thứ tự tăng dần
                numbers.sort()

                # Tìm hai số đứng giữa
                x_5 = numbers[4]
                x_6 = numbers[5]
                me=(x_5+x_6)/2

                x_3 = numbers[2]
                q1=x_3 

                x_8 = numbers[7]
                q3=x_8 
                delta_q=q3-q1

                gtnn=q1-1.5*delta_q
                gtln=q3+1.5*delta_q

                #Điếm giá trị bất thường
                outliers = [x for x in numbers if x < gtnn or x > gtln]
                count_outliers = len(outliers)  # Số lượng giá trị nằm ngoài khoảng

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho mẫu số liệu \n'
                                '$$%s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s$$'
                                'Tìm số giá trị bất thường của mẫu số liệu$zz$'

                                %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),latex(x6),latex(x7),latex(x8),latex(x9),latex(x10)
                                ))

                # Nội dung lời giải
                loigiai=('Xắp xếp dãy số theo thứ tự tăng dần ta được \\\\ \n'
                        '$$%s$$ \n'
                        'Tổng của mẫu số liệu là $n=10$ nên \\\\ \n'
                        '\\hspace*{1cm} Trung vị của mẫu số liệu là $M_e=\\dfrac{x_5+x_6}{2}=\\dfrac{%s+%s}{2}=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=x_3=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Tứ phân vị thứ nhất của mẫu số liệu là $Q_3=x_8=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Khoảng tứ phân vị là $\\Delta_Q=Q_3-Q_1=%s-%s=%s$$zz$ \\\\ \n'
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $Q_1-1,5\\Delta_Q=%s$ và $Q_3+1,5\\Delta_Q=%s$$zz$ \\\\ \n'
                        'Vậy trong dãy số liệu có $%s$ giá trị được xem là bất thường$zz$'
                        %(latex(numbers),
                        latex(x_5),latex(x_6),latex(me),
                        latex(q1),latex(q3),
                        latex(q3),latex(q1),latex(q3-q1),
                        latex(q1-1.5*(q3-q1)),latex(q3+1.5*(q3-q1)),
                        latex(count_outliers)
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace('\\left[', '').replace('\\right]', '').replace(',0$', '$').replace(', \\', '\\hspace*{0.5cm}')
            return content

