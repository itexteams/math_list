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


def bt_dang19_p4_b1_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1', '2', '3', '4', '5', '6']
            dang=random.choice(lisdang)

            if dang=='1':
                # Dạng 1: Hàng nghìn, Tính P = a * b
                num = random.randint(110000, 189499)
                rounded_num = round(num, -3)
                str_rounded = str(rounded_num)
                a_val = int(str_rounded[1])
                b_val = int(str_rounded[2])
                kq = a_val * b_val
                noidungcauhoi = ('''Quy tròn số $\\overline{b} = %s$ đến hàng nghìn ta được kết quả dạng $\\overline{1ab000}$ với $a;b$ là các số tự nhiên. Tính giá trị $P = a.b$.''' %(num))
                loigiai=('''Số quy tròn của số $\\overline{b} = %s$ đến hàng nghìn là $ %s $. \\\\
                         Khi đó $\\begin{cases} a = %s \\\\ b = %s \\end{cases} \\rightarrow P = a.b = %s$.'''
                         %(num, rounded_num, a_val, b_val, kq))

            elif dang=='2':
                # Dạng 2: Hàng nghìn, Tính P = a + b
                num = random.randint(110000, 189499)
                rounded_num = round(num, -3)
                str_rounded = str(rounded_num)
                a_val = int(str_rounded[1])
                b_val = int(str_rounded[2])
                kq = a_val + b_val
                noidungcauhoi = ('''Quy tròn số $\\overline{b} = %s$ đến hàng nghìn ta được kết quả dạng $\\overline{1ab000}$ với $a;b$ là các số tự nhiên. Tính giá trị $P = a + b$.''' %(num))
                loigiai=('''Số quy tròn của số $\\overline{b} = %s$ đến hàng nghìn là $ %s $. \\\\
                         Khi đó $\\begin{cases} a = %s \\\\ b = %s \\end{cases} \\rightarrow P = a + b = %s$.'''
                         %(num, rounded_num, a_val, b_val, kq))

            elif dang=='3':
                # Dạng 3: Hàng nghìn, Tính P = a^2 - b
                num = random.randint(110000, 189499)
                rounded_num = round(num, -3)
                str_rounded = str(rounded_num)
                a_val = int(str_rounded[1])
                b_val = int(str_rounded[2])
                kq = (a_val**2) - b_val
                noidungcauhoi = ('''Quy tròn số $\\overline{b} = %s$ đến hàng nghìn ta được kết quả dạng $\\overline{1ab000}$ với $a;b$ là các số tự nhiên. Tính giá trị $P = a^2 - b$.''' %(num))
                loigiai=('''Số quy tròn của số $\\overline{b} = %s$ đến hàng nghìn là $ %s $. \\\\
                         Khi đó $\\begin{cases} a = %s \\\\ b = %s \\end{cases} \\rightarrow P = a^2 - b = %s^2 - %s = %s$.'''
                         %(num, rounded_num, a_val, b_val, a_val, b_val, kq))

            elif dang=='4':
                # Dạng 4: Hàng trăm, Tính P = a * b
                num = random.randint(11000, 18949) # Số 5 chữ số
                rounded_num = round(num, -2) # Làm tròn 2 số cuối (hàng trăm)
                str_rounded = str(rounded_num)
                a_val = int(str_rounded[1])
                b_val = int(str_rounded[2])
                kq = a_val * b_val
                noidungcauhoi = ('''Quy tròn số $\\overline{b} = %s$ đến hàng trăm ta được kết quả dạng $\\overline{1ab00}$ với $a;b$ là các số tự nhiên. Tính giá trị $P = a.b$.''' %(num))
                loigiai=('''Số quy tròn của số $\\overline{b} = %s$ đến hàng trăm là $ %s $. \\\\
                         Khi đó $\\begin{cases} a = %s \\\\ b = %s \\end{cases} \\rightarrow P = a.b = %s$.'''
                         %(num, rounded_num, a_val, b_val, kq))

            elif dang=='5':
                # Dạng 5: Hàng chục, Tính P = a + b
                num = random.randint(1100, 1894) # Số 4 chữ số
                rounded_num = round(num, -1) # Làm tròn 1 số cuối (hàng chục)
                str_rounded = str(rounded_num)
                a_val = int(str_rounded[1])
                b_val = int(str_rounded[2])
                kq = a_val + b_val
                noidungcauhoi = ('''Quy tròn số $\\overline{b} = %s$ đến hàng chục ta được kết quả dạng $\\overline{1ab0}$ với $a;b$ là các số tự nhiên. Tính giá trị $P = a + b$.''' %(num))
                loigiai=('''Số quy tròn của số $\\overline{b} = %s$ đến hàng chục là $ %s $. \\\\
                         Khi đó $\\begin{cases} a = %s \\\\ b = %s \\end{cases} \\rightarrow P = a + b = %s$.'''
                         %(num, rounded_num, a_val, b_val, kq))

            elif dang=='6':
                # Dạng 6: Hàng chục nghìn, Tính P = a - b
                num = random.randint(1100000, 1894999) # Số 7 chữ số
                rounded_num = round(num, -4) # Làm tròn 4 số cuối (hàng chục nghìn)
                str_rounded = str(rounded_num)
                a_val = int(str_rounded[1])
                b_val = int(str_rounded[2])
                kq = a_val - b_val
                noidungcauhoi = ('''Quy tròn số $\\overline{b} = %s$ đến hàng chục nghìn ta được kết quả dạng $\\overline{1ab0000}$ với $a;b$ là các số tự nhiên. Tính giá trị $P = a - b$.''' %(num))
                loigiai=('''Số quy tròn của số $\\overline{b} = %s$ đến hàng chục nghìn là $ %s $. \\\\
                         Khi đó $\\begin{cases} a = %s \\\\ b = %s \\end{cases} \\rightarrow P = a - b = %s - %s = %s$.'''
                         %(num, rounded_num, a_val, b_val, a_val, b_val, kq))

            # Xử lý sinh đáp án nhiễu chung cho tất cả các dạng
            du = ['$%s$'%(kq)]
            da = random.choice(du)

            s = [
                 '$%s$'%(kq + random.randint(1, 3)),
                 '$%s$'%(kq - random.randint(1, 3)),
                 '$%s$'%(abs(a_val - b_val) if kq != abs(a_val - b_val) else kq + 4),
                 '$%s$'%(a_val + b_val if kq != (a_val + b_val) else kq - 4),
                 '$%s$'%(a_val * b_val if kq != (a_val * b_val) else kq + 5)
                ]

            # Loại bỏ trùng lặp và loại bỏ đáp án đúng ra khỏi list nhiễu
            s = list(set(s))
            if da in s:
                s.remove(da)

            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Xử lý hiển thị dấu: + - thành - và - - thành +
            noidungcauhoi = noidungcauhoi.replace('+ -', '-').replace('- -', '+')
            loigiai = loigiai.replace('+ -', '-').replace('- -', '+')

            # Các đáp án
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

