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


def bt_dang7_p4_b1_c3_ds10(self):
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(21,199)
                b=randint(21,199)
                c=randint(21,199)
                e=randint(1,9)


                x0=a*b*c
                number = Decimal(float(x0))  # Số cần làm tròn
                number1 = Decimal(float(x0+10))  # Số cần làm tròn
                number2 = Decimal(float(x0-20))  # Số cần làm tròn
                number3 = Decimal(float(x0+20))  # Số cần làm tròn
                number4 = Decimal(float(x0-10))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)
                kq2 = number1.quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)
                kq3 = number2.quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)
                kq4 = number3.quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)
                kq5 = number4.quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)


                du = ['$%s$'%(latex(int(kq1))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(int(kq2))),
                    '$%s$'%(latex(int(kq3))),
                    '$%s$'%(latex(int(kq4))),
                    '$%s$'%(latex(int(kq5))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Số quy tròn của số $a$ với độ chính xác $d$ được viết như sau đây $\\overline{a} = %s\\pm %s$, tìm số quy tròn đó.'
                                %(latex(x0),latex(e),
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
                loigiai=('Độ chính xác hàng đơn vị $(d=%s)$ nên số quy tròn của $%s$ theo quy tắc làm tròn đến hàng chục là $%s$ $zz$'%(latex(e),latex(x0),latex(int(kq1)))
                        )

            if dang=='2':
                # Khai báo biến
                a=randint(21,199)
                b=randint(21,199)
                c=randint(21,199)
                e=randint(11,90)


                x0=a*b*c
                number = Decimal(float(x0))  # Số cần làm tròn
                number1 = Decimal(float(x0+100))  # Số cần làm tròn
                number2 = Decimal(float(x0-200))  # Số cần làm tròn
                number3 = Decimal(float(x0+200))  # Số cần làm tròn
                number4 = Decimal(float(x0-100))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('1E2'), rounding=ROUND_HALF_UP)
                kq2 = number1.quantize(Decimal('1E2'), rounding=ROUND_HALF_UP)
                kq3 = number2.quantize(Decimal('1E2'), rounding=ROUND_HALF_UP)
                kq4 = number3.quantize(Decimal('1E2'), rounding=ROUND_HALF_UP)
                kq5 = number4.quantize(Decimal('1E2'), rounding=ROUND_HALF_UP)


                du = ['$%s$'%(latex(int(kq1))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(int(kq2))),
                    '$%s$'%(latex(int(kq3))),
                    '$%s$'%(latex(int(kq4))),
                    '$%s$'%(latex(int(kq5))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Số quy tròn của số $a$ với độ chính xác $d$ được viết như sau đây $\\overline{a} = %s\\pm %s$, tìm số quy tròn đó.'
                                %(latex(x0),latex(e),
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
                loigiai=('Độ chính xác hàng chục $(d=%s)$ nên số quy tròn của $%s$ theo quy tắc làm tròn đến hàng trăm là $%s$ $zz$'%(latex(e),latex(x0),latex(int(kq1)))
                        )

            if dang=='3':
                # Khai báo biến
                a=randint(51,199)
                b=randint(51,199)
                c=randint(31,199)
                e=randint(101,800)


                x0=a*b*c
                number = Decimal(float(x0))  # Số cần làm tròn
                number1 = Decimal(float(x0+1000))  # Số cần làm tròn
                number2 = Decimal(float(x0-2000))  # Số cần làm tròn
                number3 = Decimal(float(x0+2000))  # Số cần làm tròn
                number4 = Decimal(float(x0-1000))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('1E3'), rounding=ROUND_HALF_UP)
                kq2 = number1.quantize(Decimal('1E3'), rounding=ROUND_HALF_UP)
                kq3 = number2.quantize(Decimal('1E3'), rounding=ROUND_HALF_UP)
                kq4 = number3.quantize(Decimal('1E3'), rounding=ROUND_HALF_UP)
                kq5 = number4.quantize(Decimal('1E3'), rounding=ROUND_HALF_UP)


                du = ['$%s$'%(latex(int(kq1))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(int(kq2))),
                    '$%s$'%(latex(int(kq3))),
                    '$%s$'%(latex(int(kq4))),
                    '$%s$'%(latex(int(kq5))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Số quy tròn của số $a$ với độ chính xác $d$ được viết như sau đây $\\overline{a} = %s\\pm %s$, tìm số quy tròn đó.'
                                %(latex(x0),latex(e),
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
                loigiai=('Độ chính xác hàng trăm $(d=%s)$ nên số quy tròn của $%s$ theo quy tắc làm tròn đến hàng nghìn là $%s$ $zz$'%(latex(e),latex(x0),latex(int(kq1)))
                        )


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace('\\text{-', '\\text{$-$')
            return content

