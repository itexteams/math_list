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


def bt_dang6_p3_b1_c3_ds10(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8','9']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                b=randint(1,11)
                c=1
                a=b**2+c
                d=randint(-10,9)
                e=randint(2,7)
                h=randint(1,9)
                g=h/1000
                x0=(d+sqrt(a))/e
                while d==0:
                    b=randint(1,21)
                    c=random.choice([8,7,6,5,4,3,2,1])
                    a=b**2+c
                    d=randint(-10,9)
                    e=randint(2,50)
                    h=randint(1,9)
                    g=h/1000
                    x0=(d+sqrt(a))/e

                number = Decimal(float(x0))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                number2 = Decimal(float(x0+0.01))  # Số cần làm tròn
                kq2 = number2.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                number3 = Decimal(float(x0-0.01))  # Số cần làm tròn
                kq3 = number3.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                number4 = Decimal(float(x0+0.02))  # Số cần làm tròn
                kq4 = number4.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                number5 = Decimal(float(x0-0.02))  # Số cần làm tròn
                kq5 = number5.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


                kq8 = number.quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)


                du = ['$%s$'%(latex(kq1)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq2)),
                    '$%s$'%(latex(kq3)),
                    '$%s$'%(latex(kq4)),
                    '$%s$'%(latex(kq5)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\overline{b}=\\dfrac{%s+\\sqrt{%s}}{%s}=%s$zz$$zz$$zz$$$zz$ Số quy tròn của $\\overline{b}$ với độ chính xác $d=%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'

                                %(latex(d),latex(a),latex(e),latex(kq8),
                                latex(g),
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Độ chính xác hàng phần ngìn $(d=%s)$ nên số quy tròn của \\\\ \n'
                        '$\\overline{b}=\\dfrac{%s+\\sqrt{%s}}{%s}=%s$zz$$zz$$zz$$ theo quy tắc làm tròn đến hàng phần trăm là $%s$$zz$'
                        %(latex(g),latex(d),latex(a),latex(e),latex(kq8),latex(kq1))
                        )
                dapan='\\shortans[0]{$%s$}\n'%(kq1)

            if dang=='2':
                # Khai báo biến
                b=randint(1,11)
                c=1
                a=b**2+c
                d=randint(-10,9)
                e=randint(2,7)
                h=randint(1,9)
                g=h/100
                x0=(d+sqrt(a))/e
                while d==0:
                    b=randint(1,21)
                    c=random.choice([8,7,6,5,4,3,2,1])
                    a=b**2+c
                    d=randint(-10,9)
                    e=randint(2,50)
                    h=randint(1,9)
                    g=h/100
                    x0=(d+sqrt(a))/e

                number = Decimal(float(x0))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                number2 = Decimal(float(x0+0.1))  # Số cần làm tròn
                kq2 = number2.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                number3 = Decimal(float(x0-0.1))  # Số cần làm tròn
                kq3 = number3.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                number4 = Decimal(float(x0+0.2))  # Số cần làm tròn
                kq4 = number4.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                number5 = Decimal(float(x0-0.2))  # Số cần làm tròn
                kq5 = number5.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)


                kq8 = number.quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)


                du = ['$%s$'%(latex(kq1)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq2)),
                    '$%s$'%(latex(kq3)),
                    '$%s$'%(latex(kq4)),
                    '$%s$'%(latex(kq5)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\overline{b}=\\dfrac{%s+\\sqrt{%s}}{%s}=%s\\cdots$$zz$ Số quy tròn của $\\overline{b}$ với độ chính xác $d=%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'

                                %(latex(d),latex(a),latex(e),latex(kq8),
                                latex(g),
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Độ chính xác hàng phần trăm $(d=%s)$ nên số quy tròn của \\\\ \n'
                        '$\\overline{b}=\\dfrac{%s+\\sqrt{%s}}{%s}=%s\\cdots$ theo quy tắc làm tròn đến hàng phần chục là $%s$$zz$'
                        %(latex(g),latex(d),latex(a),latex(e),latex(kq8),latex(kq1))
                        )
                dapan='\\shortans[0]{$%s$}\n'%(kq1)

            if dang=='3':
                # Khai báo biến
                b=randint(1,11)
                c=1
                a=b**2+c
                d=randint(-10,9)
                e=randint(2,7)
                h=randint(1,9)
                g=h/10000
                x0=(d+sqrt(a))/e
                while d==0:
                    b=randint(1,21)
                    c=1
                    a=b**2+c
                    d=randint(-10,9)
                    e=randint(2,50)
                    h=randint(1,9)
                    g=h/100
                    x0=(d+sqrt(a))/e

                number = Decimal(float(x0))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

                number2 = Decimal(float(x0+0.001))  # Số cần làm tròn
                kq2 = number2.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

                number3 = Decimal(float(x0-0.001))  # Số cần làm tròn
                kq3 = number3.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

                number4 = Decimal(float(x0+0.002))  # Số cần làm tròn
                kq4 = number4.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

                number5 = Decimal(float(x0-0.002))  # Số cần làm tròn
                kq5 = number5.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)


                kq8 = number.quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP)


                du = ['$%s$'%(latex(kq1)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq2)),
                    '$%s$'%(latex(kq3)),
                    '$%s$'%(latex(kq4)),
                    '$%s$'%(latex(kq5)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\overline{b}=\\dfrac{%s+\\sqrt{%s}}{%s}=%s\\cdots$$zz$ Số quy tròn của $\\overline{b}$ với độ chính xác $d=%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'

                                %(latex(d),latex(a),latex(e),latex(kq8),
                                latex(g),
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Độ chính xác hàng phần chục nghìn $(d=%s)$ nên số quy tròn của \\\\ \n'
                        '$\\overline{b}=\\dfrac{%s+\\sqrt{%s}}{%s}=%s\\cdots$ theo quy tắc làm tròn đến hàng phần nghìn là $%s$$zz$'
                        %(latex(g),latex(d),latex(a),latex(e),latex(kq8),latex(kq1))
                        )
                dapan='\\shortans[0]{$%s$}\n'%(kq1)

            if dang=='4':
                # Khai báo biến
                b=randint(2,21)
                c=1
                a=b**2+c
                d=randint(1,9)
                e=d/100

                x0=sqrt(a)
                number = Decimal(float(x0))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                number2 = Decimal(float(x0+0.1))  # Số cần làm tròn
                kq2 = number2.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                number3 = Decimal(float(x0-0.1))  # Số cần làm tròn
                kq3 = number3.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                number4 = Decimal(float(x0+0.2))  # Số cần làm tròn
                kq4 = number4.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                number5 = Decimal(float(x0-0.2))  # Số cần làm tròn
                kq5 = number5.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)



                kq8 = number.quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)
                du = ['$%s$'%(latex(kq1)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq2)),
                    '$%s$'%(latex(kq3)),
                    '$%s$'%(latex(kq4)),
                    '$%s$'%(latex(kq5)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Biết $\\sqrt{%s}=%s\\ldots$ \n'
                                'Số quy tròn của $\\sqrt{%s}$ với độ chính xác $d=%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'
                                %(latex(a),latex(kq8),
                                latex(a),latex(e),
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có độ chính xác hàng phần trăm $(d=%s)$ nên số quy tròn của $\\sqrt{%s}$ theo quy tắc quy tròn đến hàng phần chục là $%s$$zz$'%(latex(e),latex(a),latex(kq1))
                        )
                dapan='\\shortans[0]{$%s$}\n'%(kq1)

            if dang=='5':
                # Khai báo biến
                b=randint(5,50)
                c=random.choice([-2,-3,-4,-5,-6,-7,-8,8,7,6,5,4,3,2])
                a=b**2+c
                d=randint(1,9)
                e=d/1000

                x0=sqrt(a)
                number = Decimal(float(x0))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                number2 = Decimal(float(x0+0.01))  # Số cần làm tròn
                kq2 = number2.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                number3 = Decimal(float(x0-0.01))  # Số cần làm tròn
                kq3 = number3.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                number4 = Decimal(float(x0+0.02))  # Số cần làm tròn
                kq4 = number4.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                number5 = Decimal(float(x0-0.02))  # Số cần làm tròn
                kq5 = number5.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


                kq8 = number.quantize(Decimal('0.0000001'), rounding=ROUND_HALF_UP)


                du = ['$%s$'%(latex(kq1)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq2)),
                    '$%s$'%(latex(kq3)),
                    '$%s$'%(latex(kq4)),
                    '$%s$'%(latex(kq5)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Biết $\\sqrt{%s}=%s\\ldots$ \n'
                                'Số quy tròn của $\\sqrt{%s}$ với độ chính xác $d=%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'
                                %(latex(a),latex(kq8),
                                latex(a),latex(e),
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có độ chính xác hàng phần nghìn $(d=%s)$ nên số quy tròn của $\\sqrt{%s}$ theo quy tắc quy tròn đến hàng phần trăm là $%s$$zz$'%(latex(e),latex(a),latex(kq1))
                        )
                dapan='\\shortans[0]{$%s$}\n'%(kq1)

            if dang=='6':
                # Khai báo biến
                b=randint(5,50)
                c=random.choice([-2,-3,-4,-5,-6,-7,-8,8,7,6,5,4,3,2])
                a=b**2+c
                d=randint(1,9)
                e=d/10000

                x0=sqrt(a)
                number = Decimal(float(x0))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

                number2 = Decimal(float(x0+0.001))  # Số cần làm tròn
                kq2 = number2.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

                number3 = Decimal(float(x0-0.001))  # Số cần làm tròn
                kq3 = number3.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

                number4 = Decimal(float(x0+0.002))  # Số cần làm tròn
                kq4 = number4.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

                number5 = Decimal(float(x0-0.002))  # Số cần làm tròn
                kq5 = number5.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)


                kq8 = number.quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP)


                du = ['$%s$'%(latex(kq1)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq2)),
                    '$%s$'%(latex(kq3)),
                    '$%s$'%(latex(kq4)),
                    '$%s$'%(latex(kq5)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Biết $\\sqrt{%s}=%s\\ldots$ \n'
                                'Số quy tròn của $\\sqrt{%s}$ với độ chính xác $d=%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'
                                %(latex(a),latex(kq8),
                                latex(a),latex(e),
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có độ chính xác hàng phần chục nghìn $(d=%s)$ nên số quy tròn của $\\sqrt{%s}$ theo quy tắc quy tròn đến hàng phần nghìn là $%s$$zz$'%(latex(e),latex(a),latex(kq1))
                        )
                dapan='\\shortans[0]{$%s$}\n'%(kq1)

            if dang=='7':
                # Khai báo biến
                b=randint(2,50)
                d=randint(1,9)
                e=d/10000

                a=b*math.pi

                x0=b*math.pi

                number = Decimal(float(x0))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

                number2 = Decimal(float(x0+0.001))  # Số cần làm tròn
                kq2 = number2.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

                number3 = Decimal(float(x0-0.001))  # Số cần làm tròn
                kq3 = number3.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

                number4 = Decimal(float(x0+0.002))  # Số cần làm tròn
                kq4 = number4.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

                number5 = Decimal(float(x0-0.002))  # Số cần làm tròn
                kq5 = number5.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)


                kq8 = number.quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)


                du = ['$%s$'%(latex(kq1)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq2)),
                    '$%s$'%(latex(kq3)),
                    '$%s$'%(latex(kq4)),
                    '$%s$'%(latex(kq5)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Biết $%s\\pi=%s\\ldots$ \n'
                                'Số quy tròn của $%s\\pi$ với độ chính xác $d=%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'
                                %(latex(b),latex(kq8),
                                latex(b),latex(e),
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có độ chính xác hàng phần chục nghìn $(d=%s)$ nên số quy tròn của $%s\\pi$ theo quy tắc quy tròn đến hàng phần nghìn là $%s$$zz$'%(latex(e),latex(b),latex(kq1))
                        )
                dapan='\\shortans[0]{$%s$}\n'%(kq1)

            if dang=='8':
                # Khai báo biến
                b=randint(2,50)
                d=randint(1,9)
                e=d/1000
                a=b*math.pi

                x0=b*math.pi

                number = Decimal(float(x0))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                number2 = Decimal(float(x0+0.01))  # Số cần làm tròn
                kq2 = number2.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                number3 = Decimal(float(x0-0.01))  # Số cần làm tròn
                kq3 = number3.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                number4 = Decimal(float(x0+0.02))  # Số cần làm tròn
                kq4 = number4.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                number5 = Decimal(float(x0-0.02))  # Số cần làm tròn
                kq5 = number5.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


                kq8 = number.quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)
                du = ['$%s$'%(latex(kq1)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq2)),
                    '$%s$'%(latex(kq3)),
                    '$%s$'%(latex(kq4)),
                    '$%s$'%(latex(kq5)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Biết $%s\\pi=%s\\ldots$ \n'
                                'Số quy tròn của $%s\\pi$ với độ chính xác $d=%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'
                                %(latex(b),latex(kq8),
                                latex(b),latex(e),
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có độ chính xác hàng phần nghìn $(d=%s)$ nên số quy tròn của $%s\\pi$ theo quy tắc quy tròn đến hàng phần trăm là $%s$$zz$'%(latex(e),latex(b),latex(kq1))
                        )
                dapan='\\shortans[0]{$%s$}\n'%(kq1)

            if dang=='9':
                # Khai báo biến
                b=randint(2,50)
                d=randint(1,9)
                e=d/100
                a=b*math.pi

                x0=b*math.pi

                number = Decimal(float(x0))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                number2 = Decimal(float(x0+0.1))  # Số cần làm tròn
                kq2 = number2.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                number3 = Decimal(float(x0-0.1))  # Số cần làm tròn
                kq3 = number3.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                number4 = Decimal(float(x0+0.2))  # Số cần làm tròn
                kq4 = number4.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                number5 = Decimal(float(x0-0.2))  # Số cần làm tròn
                kq5 = number5.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                kq8 = number.quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)
                du = ['$%s$'%(latex(kq1)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq2)),
                    '$%s$'%(latex(kq3)),
                    '$%s$'%(latex(kq4)),
                    '$%s$'%(latex(kq5)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Biết $%s\\pi=%s\\ldots$ \n'
                                'Số quy tròn $%s\\pi$ với độ chính xác $d=%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'
                                %(latex(b),latex(kq8),
                                latex(b),latex(e),
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có độ chính xác hàng phần trăm $(d=%s)$ nên số quy tròn của $%s\\pi$ theo quy tắc quy tròn đến hàng phần chục là $%s$$zz$'%(latex(e),latex(b),latex(kq1))
                        )
                dapan='\\shortans[0]{$%s$}\n'%(kq1)


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content


