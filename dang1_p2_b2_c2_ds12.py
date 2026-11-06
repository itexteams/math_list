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


def bt_dang1_p2_b2_c2_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='4':
                # Khai báo biến
                lisv=[30,35,40,45,50,55,60]
                v=random.choice(lisv)
                while True:
                    xe1 = randint(1, 10)
                    xe2 = randint(1, 10)
                    xe3 = randint(1, 10)
                    xe4 = randint(1, 10)
                    xe5 = randint(1, 10)
                    tong = xe1 + xe2 + xe3 + xe4 + xe5
                    tong1=(tong-1)/2

                    # Kiểm tra nếu tổng là số lẻ và tổng1 chẵn thì thoát vòng lặp
                    if tong % 2 != 0 and tong1 % 2 ==0:
                        break 

                lisk=[2,4,6,8,10]
                k=random.choice(lisk)

                # Tạo danh sách số liệu gốc
                data = []
                data.extend([v] * xe1)
                data.extend([v + k] * xe2)
                data.extend([v + 2 * k] * xe3)
                data.extend([v + 3 * k] * xe4)
                data.extend([v + 4 * k] * xe5)

                # Sắp xếp danh sách số liệu
                data.sort()

                # Tính toán vị trí Q1
                n = len(data)
                Q1_index = (n + 1) / 4  # Vị trí lý thuyết của Q1

                # Nếu chỉ số Q1 không phải số nguyên, lấy nội suy
                if Q1_index.is_integer():
                    Q1_index = int(Q1_index) - 1  # Đánh chỉ số từ 0
                    Q1 = data[Q1_index]
                else:
                    lower_index = int(Q1_index) - 1
                    upper_index = lower_index + 1
                    Q1 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q3
                Q3_index = 3 * (n + 1) / 4  # Vị trí lý thuyết của Q3

                # Nếu chỉ số Q3 không phải số nguyên, lấy nội suy
                if Q3_index.is_integer():
                    Q3_index = int(Q3_index) - 1  # Đánh chỉ số từ 0
                    Q3 = data[Q3_index]
                else:
                    lower_index = int(Q3_index) - 1
                    upper_index = lower_index + 1
                    Q3 = (data[lower_index] + data[upper_index]) / 2

                # Tạo danh sách các khoảng và tần số tương ứng
                intervals = [(v, v + k), (v + k, v + 2 * k), (v + 2 * k, v + 3 * k), (v + 3 * k, v + 4 * k), (v + 4 * k, v + 5 * k)]
                frequencies = [xe1, xe2, xe3, xe4, xe5]

                # Tìm khoảng chứa Q1 và Q3
                Q1_interval = None
                Q3_interval = None
                Q1_interval_index = None
                Q3_interval_index = None

                for i, (start, end) in enumerate(intervals):
                    if start <= Q1 < end:
                        Q1_interval = (start, end)
                        Q1_interval_index = i
                    if start <= Q3 < end:
                        Q3_interval = (start, end)
                        Q3_interval_index = i

                # Tính tổng tần số đến trước khoảng chứa Q1 và Q3
                total_freq_before_Q1 = sum(frequencies[:Q1_interval_index]) if Q1_interval_index is not None else 0
                total_freq_before_Q3 = sum(frequencies[:Q3_interval_index]) if Q3_interval_index is not None else 0

                # Tìm tần số tương ứng với khoảng chứa Q1 và Q3
                Q1_interval_frequency = frequencies[Q1_interval_index] if Q1_interval_index is not None else 0
                Q3_interval_frequency = frequencies[Q3_interval_index] if Q3_interval_index is not None else 0

                #kqQ1=Q1_interval[0]+((1*n/4-total_freq_before_Q1)/Q1_interval_frequency)*(Q1_interval[1]-Q1_interval[0])
                kqQ1=Q1_interval[0]+Rational(1*n/4-total_freq_before_Q1,Q1_interval_frequency)*(Q1_interval[1]-Q1_interval[0])
                #kqQ3=Q3_interval[0]+((3*n/4-total_freq_before_Q3)/Q3_interval_frequency)*(Q3_interval[1]-Q3_interval[0])
                kqQ3=Q3_interval[0]+Rational(3*n/4-total_freq_before_Q3,Q3_interval_frequency)*(Q3_interval[1]-Q3_interval[0])
                kq=kqQ3-kqQ1

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)
                phuong_sai=Rational(xe1*x1**2+xe2*x2**2+xe3*x3**2+xe4*x4**2+xe5*x5**2,tong)-xtb**2
                do_lech=sqrt(phuong_sai)

                du = ['\\True Tổng số liệu của mẫu số liệu là $%s$'%(latex(tong)),
                    '\\True Tứ phân vị thứ nhất là $Q_1=%s$'%(latex(kqQ1)),
                    '\\True Tứ phân vị thứ ba là $Q_3=%s$'%(latex(kqQ3)),
                    '\\True Khoảng biến thiên là $R=%s$'%(latex(5*k)),
                    '\\True Khoảng tứ phân vị là $\\Delta_Q=%s$'%(latex(kqQ3-kqQ1)),
                    '\\True Giá trị đại diện của nhóm $3$ là $x_3=%s$'%(latex(x3)),
                    '\\True Số trung bình của mẫu số liệu là $\\bar{x}=%s$'%(latex(xtb)),
                    '\\True Phương sai là $s^2=%s$'%(latex(phuong_sai)),
                    '\\True Độ lệch chuẩn là $s=%s$'%(latex(do_lech)),
                    ]

                da1= random.choice(du)
                du.remove(da1)
                da2= random.choice(du)
                du.remove(da2)
                da3= random.choice(du)
                du.remove(da3)
                da4= random.choice(du)
                s = ['Tổng số liệu của mẫu số liệu là $%s$'%(latex(tong+1)),
                    'Tứ phân vị thứ nhất là $Q_1=%s$'%(latex(kqQ1+1)),
                    'Tứ phân vị thứ ba là $Q_3=%s$'%(latex(kqQ3+1)),
                    'Khoảng biến thiên là $R=%s$'%(latex(5*k+1)),
                    'Khoảng tứ phân vị là $\\Delta_Q=%s$'%(latex(kqQ3-kqQ1+1)),
                    'Giá trị đại diện của nhóm $3$ là $x_3=%s$'%(latex(x3+1)),
                    'Số trung bình của mẫu số liệu là $\\bar{x}=%s$'%(latex(xtb+1)),
                    'Phương sai là $s^2=%s$'%(latex(phuong_sai+1)),
                    'Độ lệch chuẩn là $s=%s$'%(latex(do_lech+1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                s.remove(das3)
                das4 = random.choice(s)
                list_dapan = [da1,da2,da3,da4,das1,das2,das3,das4]
                # Câu hỏi
                noidungcauhoi = ('Thời gian chạy bộ thể dục (phút) của một người trong các ngày được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Thời gian (phút) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số ngày & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5)
                                ))
                # Các đáp án
                da_d = random.choice(list_dapan)
                list_dapan.remove(da_d)
                da_s1 = random.choice(list_dapan)
                list_dapan.remove(da_s1)
                da_s2 = random.choice(list_dapan) 
                list_dapan.remove(da_s2)
                da_s3 = random.choice(list_dapan)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tổng số liệu là $n=%s+%s+%s+%s+%s=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là các giá trị tương ứng của $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự tăng dần. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ ba là \\\\ \n'
                        '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Khoảng tứ phân vị của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\Delta_Q=Q_3-Q_1=%s-%s=%s$.\\\\ \n'

                        'Giá trị đại diện của các nhóm số liệu là \\\\ \n'
                        '\\hspace*{1cm} $x_1=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_2=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_3=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_4=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_5=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{1}{%s}\\left( %s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s \\right)=%s$. \\\\ \n'
                        'Phương sai của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $s^2=\\dfrac{1}{%s}\\left( %s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2 \\right)-\\left(%s\\right)^2=%s$. \\\\ \n'
                        'Độ lệch chuẩn của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $s=\\sqrt{s^2}=%s$. \\\\ \n'

                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),latex(tong),latex(tong),
                        latex(n),latex(n/4-1/4),latex(n/4-1/4+1),latex(Q1_interval[0]),latex(Q1_interval[1]),
                        latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),
                        latex(n),latex(3*n/4+1/4),latex(3*n/4+1/4+1),latex(Q3_interval[0]),latex(Q3_interval[1]),
                        latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),
                        latex(kqQ3),latex(kqQ1),latex(kq),

                            latex(v),latex(v+k),latex(x1),
                            latex(v+k),latex(v+2*k),latex(x2),
                            latex(v+2*k),latex(v+3*k),latex(xe3),
                            latex(v+3*k),latex(v+4*k),latex(x4),
                            latex(v+4*k),latex(v+5*k),latex(x5),
                            latex(tong),latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(xtb),
                            latex(tong),latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(xtb),latex(phuong_sai),
                            latex(do_lech),
                        ))
            if dang=='3':
                # Khai báo biến
                lisv=[30,35,40,45,50,55,60]
                v=random.choice(lisv)
                while True:
                    xe1 = randint(1, 10)
                    xe2 = randint(1, 10)
                    xe3 = randint(1, 10)
                    xe4 = randint(1, 10)
                    xe5 = randint(1, 10)
                    tong = xe1 + xe2 + xe3 + xe4 + xe5
                    tong1=(tong-1)/2

                    # Kiểm tra nếu tổng là số lẻ và tổng1 lẻ thì thoát vòng lặp
                    if tong % 2 != 0 and tong1 % 2 !=0:
                        break 

                lisk=[2,4,6,8,10]
                k=random.choice(lisk)

                # Tạo danh sách số liệu gốc
                data = []
                data.extend([v] * xe1)
                data.extend([v + k] * xe2)
                data.extend([v + 2 * k] * xe3)
                data.extend([v + 3 * k] * xe4)
                data.extend([v + 4 * k] * xe5)

                # Sắp xếp danh sách số liệu
                data.sort()

                # Tính toán vị trí Q1
                n = len(data)
                Q1_index = (n + 1) / 4  # Vị trí lý thuyết của Q1

                # Nếu chỉ số Q1 không phải số nguyên, lấy nội suy
                if Q1_index.is_integer():
                    Q1_index = int(Q1_index) - 1  # Đánh chỉ số từ 0
                    Q1 = data[Q1_index]
                else:
                    lower_index = int(Q1_index) - 1
                    upper_index = lower_index + 1
                    Q1 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q3
                Q3_index = 3 * (n + 1) / 4  # Vị trí lý thuyết của Q3

                # Nếu chỉ số Q3 không phải số nguyên, lấy nội suy
                if Q3_index.is_integer():
                    Q3_index = int(Q3_index) - 1  # Đánh chỉ số từ 0
                    Q3 = data[Q3_index]
                else:
                    lower_index = int(Q3_index) - 1
                    upper_index = lower_index + 1
                    Q3 = (data[lower_index] + data[upper_index]) / 2

                # Tạo danh sách các khoảng và tần số tương ứng
                intervals = [(v, v + k), (v + k, v + 2 * k), (v + 2 * k, v + 3 * k), (v + 3 * k, v + 4 * k), (v + 4 * k, v + 5 * k)]
                frequencies = [xe1, xe2, xe3, xe4, xe5]

                # Tìm khoảng chứa Q1 và Q3
                Q1_interval = None
                Q3_interval = None
                Q1_interval_index = None
                Q3_interval_index = None

                for i, (start, end) in enumerate(intervals):
                    if start <= Q1 < end:
                        Q1_interval = (start, end)
                        Q1_interval_index = i
                    if start <= Q3 < end:
                        Q3_interval = (start, end)
                        Q3_interval_index = i

                # Tính tổng tần số đến trước khoảng chứa Q1 và Q3
                total_freq_before_Q1 = sum(frequencies[:Q1_interval_index]) if Q1_interval_index is not None else 0
                total_freq_before_Q3 = sum(frequencies[:Q3_interval_index]) if Q3_interval_index is not None else 0

                # Tìm tần số tương ứng với khoảng chứa Q1 và Q3
                Q1_interval_frequency = frequencies[Q1_interval_index] if Q1_interval_index is not None else 0
                Q3_interval_frequency = frequencies[Q3_interval_index] if Q3_interval_index is not None else 0

                #kqQ1=Q1_interval[0]+((1*n/4-total_freq_before_Q1)/Q1_interval_frequency)*(Q1_interval[1]-Q1_interval[0])
                kqQ1=Q1_interval[0]+Rational(1*n/4-total_freq_before_Q1,Q1_interval_frequency)*(Q1_interval[1]-Q1_interval[0])
                #kqQ3=Q3_interval[0]+((3*n/4-total_freq_before_Q3)/Q3_interval_frequency)*(Q3_interval[1]-Q3_interval[0])
                kqQ3=Q3_interval[0]+Rational(3*n/4-total_freq_before_Q3,Q3_interval_frequency)*(Q3_interval[1]-Q3_interval[0])
                kq=kqQ3-kqQ1

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)
                phuong_sai=Rational(xe1*x1**2+xe2*x2**2+xe3*x3**2+xe4*x4**2+xe5*x5**2,tong)-xtb**2
                do_lech=sqrt(phuong_sai)

                du = ['\\True Tổng số liệu của mẫu số liệu là $%s$'%(latex(tong)),
                    '\\True Tứ phân vị thứ nhất là $Q_1=%s$'%(latex(kqQ1)),
                    '\\True Tứ phân vị thứ ba là $Q_3=%s$'%(latex(kqQ3)),
                    '\\True Khoảng biến thiên là $R=%s$'%(latex(5*k)),
                    '\\True Khoảng tứ phân vị là $\\Delta_Q=%s$'%(latex(kqQ3-kqQ1)),
                    '\\True Giá trị đại diện của nhóm $3$ là $x_3=%s$'%(latex(x3)),
                    '\\True Số trung bình của mẫu số liệu là $\\bar{x}=%s$'%(latex(xtb)),
                    '\\True Phương sai là $s^2=%s$'%(latex(phuong_sai)),
                    '\\True Độ lệch chuẩn là $s=%s$'%(latex(do_lech)),
                    ]

                da1= random.choice(du)
                du.remove(da1)
                da2= random.choice(du)
                du.remove(da2)
                da3= random.choice(du)
                du.remove(da3)
                da4= random.choice(du)
                s = ['Tổng số liệu của mẫu số liệu là $%s$'%(latex(tong+1)),
                    'Tứ phân vị thứ nhất là $Q_1=%s$'%(latex(kqQ1+1)),
                    'Tứ phân vị thứ ba là $Q_3=%s$'%(latex(kqQ3+1)),
                    'Khoảng biến thiên là $R=%s$'%(latex(5*k+1)),
                    'Khoảng tứ phân vị là $\\Delta_Q=%s$'%(latex(kqQ3-kqQ1+1)),
                    'Giá trị đại diện của nhóm $3$ là $x_3=%s$'%(latex(x3+1)),
                    'Số trung bình của mẫu số liệu là $\\bar{x}=%s$'%(latex(xtb+1)),
                    'Phương sai là $s^2=%s$'%(latex(phuong_sai+1)),
                    'Độ lệch chuẩn là $s=%s$'%(latex(do_lech+1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                s.remove(das3)
                das4 = random.choice(s)
                list_dapan = [da1,da2,da3,da4,das1,das2,das3,das4]
                # Câu hỏi
                noidungcauhoi = ('Thời gian chạy bộ thể dục (phút) của một người trong các ngày được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Thời gian (phút) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số ngày & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5)
                                ))
                # Các đáp án
                da_d = random.choice(list_dapan)
                list_dapan.remove(da_d)
                da_s1 = random.choice(list_dapan)
                list_dapan.remove(da_s1)
                da_s2 = random.choice(list_dapan) 
                list_dapan.remove(da_s2)
                da_s3 = random.choice(list_dapan)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tổng số liệu là $n=%s+%s+%s+%s+%s=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là các giá trị tương ứng của $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự tăng dần. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ ba là \\\\ \n'
                        '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Khoảng tứ phân vị của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\Delta_Q=Q_3-Q_1=%s-%s=%s$. \\\\ \n'

                        'Giá trị đại diện của các nhóm số liệu là \\\\ \n'
                        '\\hspace*{1cm} $x_1=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_2=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_3=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_4=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_5=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{1}{%s}\\left( %s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s \\right)=%s$. \\\\ \n'
                        'Phương sai của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $s^2=\\dfrac{1}{%s}\\left( %s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2 \\right)-\\left(%s\\right)^2=%s$. \\\\ \n'
                        'Độ lệch chuẩn của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $s=\\sqrt{s^2}=%s$. \\\\ \n'

                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),latex(tong),latex(tong),
                        latex(n),latex(n/4+1/4),latex(Q1_interval[0]),latex(Q1_interval[1]),
                        latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),
                        latex(n),latex(3*n/4+3/4),latex(Q3_interval[0]),latex(Q3_interval[1]),
                        latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),
                        latex(kqQ3),latex(kqQ1),latex(kq),

                            latex(v),latex(v+k),latex(x1),
                            latex(v+k),latex(v+2*k),latex(x2),
                            latex(v+2*k),latex(v+3*k),latex(xe3),
                            latex(v+3*k),latex(v+4*k),latex(x4),
                            latex(v+4*k),latex(v+5*k),latex(x5),
                            latex(tong),latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(xtb),
                            latex(tong),latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(xtb),latex(phuong_sai),
                            latex(do_lech),
                        ))
            if dang=='2':
                # Khai báo biến
                lisv=[30,35,40,45,50,55,60]
                v=random.choice(lisv)
                while True:
                    xe1 = randint(1, 10)
                    xe2 = randint(1, 10)
                    xe3 = randint(1, 10)
                    xe4 = randint(1, 10)
                    xe5 = randint(1, 10)
                    tong = xe1 + xe2 + xe3 + xe4 + xe5
                    tong1=tong/2

                    # Kiểm tra nếu tổng là số chẵn và toongr1 chẵn thì thoát vòng lặp
                    if tong % 2 == 0 and tong1 % 2 ==0:
                        break 

                lisk=[2,4,6,8,10]
                k=random.choice(lisk)

                # Tạo danh sách số liệu gốc
                data = []
                data.extend([v] * xe1)
                data.extend([v + k] * xe2)
                data.extend([v + 2 * k] * xe3)
                data.extend([v + 3 * k] * xe4)
                data.extend([v + 4 * k] * xe5)

                # Sắp xếp danh sách số liệu
                data.sort()

                # Tính toán vị trí Q1
                n = len(data)
                Q1_index = (n + 1) / 4  # Vị trí lý thuyết của Q1

                # Nếu chỉ số Q1 không phải số nguyên, lấy nội suy
                if Q1_index.is_integer():
                    Q1_index = int(Q1_index) - 1  # Đánh chỉ số từ 0
                    Q1 = data[Q1_index]
                else:
                    lower_index = int(Q1_index) - 1
                    upper_index = lower_index + 1
                    Q1 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q3
                Q3_index = 3 * (n + 1) / 4  # Vị trí lý thuyết của Q3

                # Nếu chỉ số Q3 không phải số nguyên, lấy nội suy
                if Q3_index.is_integer():
                    Q3_index = int(Q3_index) - 1  # Đánh chỉ số từ 0
                    Q3 = data[Q3_index]
                else:
                    lower_index = int(Q3_index) - 1
                    upper_index = lower_index + 1
                    Q3 = (data[lower_index] + data[upper_index]) / 2

                # Tạo danh sách các khoảng và tần số tương ứng
                intervals = [(v, v + k), (v + k, v + 2 * k), (v + 2 * k, v + 3 * k), (v + 3 * k, v + 4 * k), (v + 4 * k, v + 5 * k)]
                frequencies = [xe1, xe2, xe3, xe4, xe5]

                # Tìm khoảng chứa Q1 và Q3
                Q1_interval = None
                Q3_interval = None
                Q1_interval_index = None
                Q3_interval_index = None

                for i, (start, end) in enumerate(intervals):
                    if start <= Q1 < end:
                        Q1_interval = (start, end)
                        Q1_interval_index = i
                    if start <= Q3 < end:
                        Q3_interval = (start, end)
                        Q3_interval_index = i

                # Tính tổng tần số đến trước khoảng chứa Q1 và Q3
                total_freq_before_Q1 = sum(frequencies[:Q1_interval_index]) if Q1_interval_index is not None else 0
                total_freq_before_Q3 = sum(frequencies[:Q3_interval_index]) if Q3_interval_index is not None else 0

                # Tìm tần số tương ứng với khoảng chứa Q1 và Q3
                Q1_interval_frequency = frequencies[Q1_interval_index] if Q1_interval_index is not None else 0
                Q3_interval_frequency = frequencies[Q3_interval_index] if Q3_interval_index is not None else 0

                #kqQ1=Q1_interval[0]+((1*n/4-total_freq_before_Q1)/Q1_interval_frequency)*(Q1_interval[1]-Q1_interval[0])
                kqQ1=Q1_interval[0]+Rational(1*n/4-total_freq_before_Q1,Q1_interval_frequency)*(Q1_interval[1]-Q1_interval[0])
                #kqQ3=Q3_interval[0]+((3*n/4-total_freq_before_Q3)/Q3_interval_frequency)*(Q3_interval[1]-Q3_interval[0])
                kqQ3=Q3_interval[0]+Rational(3*n/4-total_freq_before_Q3,Q3_interval_frequency)*(Q3_interval[1]-Q3_interval[0])
                kq=kqQ3-kqQ1

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)
                phuong_sai=Rational(xe1*x1**2+xe2*x2**2+xe3*x3**2+xe4*x4**2+xe5*x5**2,tong)-xtb**2
                do_lech=sqrt(phuong_sai)

                du = ['\\True Tổng số liệu của mẫu số liệu là $%s$'%(latex(tong)),
                    '\\True Tứ phân vị thứ nhất là $Q_1=%s$'%(latex(kqQ1)),
                    '\\True Tứ phân vị thứ ba là $Q_3=%s$'%(latex(kqQ3)),
                    '\\True Khoảng biến thiên là $R=%s$'%(latex(5*k)),
                    '\\True Khoảng tứ phân vị là $\\Delta_Q=%s$'%(latex(kqQ3-kqQ1)),
                    '\\True Giá trị đại diện của nhóm $3$ là $x_3=%s$'%(latex(x3)),
                    '\\True Số trung bình của mẫu số liệu là $\\bar{x}=%s$'%(latex(xtb)),
                    '\\True Phương sai là $s^2=%s$'%(latex(phuong_sai)),
                    '\\True Độ lệch chuẩn là $s=%s$'%(latex(do_lech)),
                    ]

                da1= random.choice(du)
                du.remove(da1)
                da2= random.choice(du)
                du.remove(da2)
                da3= random.choice(du)
                du.remove(da3)
                da4= random.choice(du)
                s = ['Tổng số liệu của mẫu số liệu là $%s$'%(latex(tong+1)),
                    'Tứ phân vị thứ nhất là $Q_1=%s$'%(latex(kqQ1+1)),
                    'Tứ phân vị thứ ba là $Q_3=%s$'%(latex(kqQ3+1)),
                    'Khoảng biến thiên là $R=%s$'%(latex(5*k+1)),
                    'Khoảng tứ phân vị là $\\Delta_Q=%s$'%(latex(kqQ3-kqQ1+1)),
                    'Giá trị đại diện của nhóm $3$ là $x_3=%s$'%(latex(x3+1)),
                    'Số trung bình của mẫu số liệu là $\\bar{x}=%s$'%(latex(xtb+1)),
                    'Phương sai là $s^2=%s$'%(latex(phuong_sai+1)),
                    'Độ lệch chuẩn là $s=%s$'%(latex(do_lech+1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                s.remove(das3)
                das4 = random.choice(s)
                list_dapan = [da1,da2,da3,da4,das1,das2,das3,das4]
                # Câu hỏi
                noidungcauhoi = ('Thời gian chạy bộ thể dục (phút) của một người trong các ngày được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Thời gian (phút) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số ngày & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5)
                                ))
                # Các đáp án
                da_d = random.choice(list_dapan)
                list_dapan.remove(da_d)
                da_s1 = random.choice(list_dapan)
                list_dapan.remove(da_s1)
                da_s2 = random.choice(list_dapan) 
                list_dapan.remove(da_s2)
                da_s3 = random.choice(list_dapan)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tổng số liệu là $n=%s+%s+%s+%s+%s=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là các giá trị tương ứng của $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự tăng dần. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ ba là \\\\ \n'
                        '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Khoảng tứ phân vị của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\Delta_Q=Q_3-Q_1=%s-%s=%s$. \\\\ \n'

                        'Giá trị đại diện của các nhóm số liệu là \\\\ \n'
                        '\\hspace*{1cm} $x_1=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_2=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_3=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_4=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_5=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{1}{%s}\\left( %s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s \\right)=%s$. \\\\ \n'
                        'Phương sai của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $s^2=\\dfrac{1}{%s}\\left( %s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2 \\right)-\\left(%s\\right)^2=%s$. \\\\ \n'
                        'Độ lệch chuẩn của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $s=\\sqrt{s^2}=%s$. \\\\ \n'

                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),latex(tong),latex(tong),
                        latex(n),latex(n/4+1/2-1/2),latex(n/4+1/2+1/2),latex(Q1_interval[0]),latex(Q1_interval[1]),
                        latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),
                        latex(n),latex(n/2+n/4+1/2-1/2),latex(n/2+n/4+1/2+1/2),latex(Q3_interval[0]),latex(Q3_interval[1]),
                        latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),
                        latex(kqQ3),latex(kqQ1),latex(kq),

                            latex(v),latex(v+k),latex(x1),
                            latex(v+k),latex(v+2*k),latex(x2),
                            latex(v+2*k),latex(v+3*k),latex(xe3),
                            latex(v+3*k),latex(v+4*k),latex(x4),
                            latex(v+4*k),latex(v+5*k),latex(x5),
                            latex(tong),latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(xtb),
                            latex(tong),latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(xtb),latex(phuong_sai),
                            latex(do_lech),
                        ))
            if dang=='1':
                # Khai báo biến
                lisv=[30,35,40,45,50,55,60]
                v=random.choice(lisv)
                while True:
                    xe1 = randint(1, 10)
                    xe2 = randint(1, 10)
                    xe3 = randint(1, 10)
                    xe4 = randint(1, 10)
                    xe5 = randint(1, 10)
                    tong = xe1 + xe2 + xe3 + xe4 + xe5
                    tong1=tong/2

                    # Kiểm tra nếu tổng là số chẵn và toongr1 lẻ thì thoát vòng lặp
                    if tong % 2 == 0 and tong1 % 2 !=0:
                        break 

                lisk=[2,4,6,8,10]
                k=random.choice(lisk)

                # Tạo danh sách số liệu gốc
                data = []
                data.extend([v] * xe1)
                data.extend([v + k] * xe2)
                data.extend([v + 2 * k] * xe3)
                data.extend([v + 3 * k] * xe4)
                data.extend([v + 4 * k] * xe5)

                # Sắp xếp danh sách số liệu
                data.sort()

                # Tính toán vị trí Q1
                n = len(data)
                Q1_index = (n + 1) / 4  # Vị trí lý thuyết của Q1

                # Nếu chỉ số Q1 không phải số nguyên, lấy nội suy
                if Q1_index.is_integer():
                    Q1_index = int(Q1_index) - 1  # Đánh chỉ số từ 0
                    Q1 = data[Q1_index]
                else:
                    lower_index = int(Q1_index) - 1
                    upper_index = lower_index + 1
                    Q1 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q3
                Q3_index = 3 * (n + 1) / 4  # Vị trí lý thuyết của Q3

                # Nếu chỉ số Q3 không phải số nguyên, lấy nội suy
                if Q3_index.is_integer():
                    Q3_index = int(Q3_index) - 1  # Đánh chỉ số từ 0
                    Q3 = data[Q3_index]
                else:
                    lower_index = int(Q3_index) - 1
                    upper_index = lower_index + 1
                    Q3 = (data[lower_index] + data[upper_index]) / 2

                # Tạo danh sách các khoảng và tần số tương ứng
                intervals = [(v, v + k), (v + k, v + 2 * k), (v + 2 * k, v + 3 * k), (v + 3 * k, v + 4 * k), (v + 4 * k, v + 5 * k)]
                frequencies = [xe1, xe2, xe3, xe4, xe5]

                # Tìm khoảng chứa Q1 và Q3
                Q1_interval = None
                Q3_interval = None
                Q1_interval_index = None
                Q3_interval_index = None

                for i, (start, end) in enumerate(intervals):
                    if start <= Q1 < end:
                        Q1_interval = (start, end)
                        Q1_interval_index = i
                    if start <= Q3 < end:
                        Q3_interval = (start, end)
                        Q3_interval_index = i

                # Tính tổng tần số đến trước khoảng chứa Q1 và Q3
                total_freq_before_Q1 = sum(frequencies[:Q1_interval_index]) if Q1_interval_index is not None else 0
                total_freq_before_Q3 = sum(frequencies[:Q3_interval_index]) if Q3_interval_index is not None else 0

                # Tìm tần số tương ứng với khoảng chứa Q1 và Q3
                Q1_interval_frequency = frequencies[Q1_interval_index] if Q1_interval_index is not None else 0
                Q3_interval_frequency = frequencies[Q3_interval_index] if Q3_interval_index is not None else 0

                #kqQ1=Q1_interval[0]+((1*n/4-total_freq_before_Q1)/Q1_interval_frequency)*(Q1_interval[1]-Q1_interval[0])
                kqQ1=Q1_interval[0]+Rational(1*n/4-total_freq_before_Q1,Q1_interval_frequency)*(Q1_interval[1]-Q1_interval[0])
                #kqQ3=Q3_interval[0]+((3*n/4-total_freq_before_Q3)/Q3_interval_frequency)*(Q3_interval[1]-Q3_interval[0])
                kqQ3=Q3_interval[0]+Rational(3*n/4-total_freq_before_Q3,Q3_interval_frequency)*(Q3_interval[1]-Q3_interval[0])
                kq=kqQ3-kqQ1

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)
                phuong_sai=Rational(xe1*x1**2+xe2*x2**2+xe3*x3**2+xe4*x4**2+xe5*x5**2,tong)-xtb**2
                do_lech=sqrt(phuong_sai)

                du = ['\\True Tổng số liệu của mẫu số liệu là $%s$'%(latex(tong)),
                    '\\True Tứ phân vị thứ nhất là $Q_1=%s$'%(latex(kqQ1)),
                    '\\True Tứ phân vị thứ ba là $Q_3=%s$'%(latex(kqQ3)),
                    '\\True Khoảng biến thiên là $R=%s$'%(latex(5*k)),
                    '\\True Khoảng tứ phân vị là $\\Delta_Q=%s$'%(latex(kqQ3-kqQ1)),
                    '\\True Giá trị đại diện của nhóm $3$ là $x_3=%s$'%(latex(x3)),
                    '\\True Số trung bình của mẫu số liệu là $\\bar{x}=%s$'%(latex(xtb)),
                    '\\True Phương sai là $s^2=%s$'%(latex(phuong_sai)),
                    '\\True Độ lệch chuẩn là $s=%s$'%(latex(do_lech)),
                    ]

                da1= random.choice(du)
                du.remove(da1)
                da2= random.choice(du)
                du.remove(da2)
                da3= random.choice(du)
                du.remove(da3)
                da4= random.choice(du)
                s = ['Tổng số liệu của mẫu số liệu là $%s$'%(latex(tong+1)),
                    'Tứ phân vị thứ nhất là $Q_1=%s$'%(latex(kqQ1+1)),
                    'Tứ phân vị thứ ba là $Q_3=%s$'%(latex(kqQ3+1)),
                    'Khoảng biến thiên là $R=%s$'%(latex(5*k+1)),
                    'Khoảng tứ phân vị là $\\Delta_Q=%s$'%(latex(kqQ3-kqQ1+1)),
                    'Giá trị đại diện của nhóm $3$ là $x_3=%s$'%(latex(x3+1)),
                    'Số trung bình của mẫu số liệu là $\\bar{x}=%s$'%(latex(xtb+1)),
                    'Phương sai là $s^2=%s$'%(latex(phuong_sai+1)),
                    'Độ lệch chuẩn là $s=%s$'%(latex(do_lech+1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                s.remove(das3)
                das4 = random.choice(s)
                list_dapan = [da1,da2,da3,da4,das1,das2,das3,das4]
                # Câu hỏi
                noidungcauhoi = ('Thời gian chạy bộ thể dục (phút) của một người trong các ngày được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Thời gian (phút) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số ngày & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5)
                                ))
                # Các đáp án
                da_d = random.choice(list_dapan)
                list_dapan.remove(da_d)
                da_s1 = random.choice(list_dapan)
                list_dapan.remove(da_s1)
                da_s2 = random.choice(list_dapan) 
                list_dapan.remove(da_s2)
                da_s3 = random.choice(list_dapan)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tổng số liệu là $n=%s+%s+%s+%s+%s=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là các giá trị tương ứng của $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự tăng dần. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ ba là \\\\ \n'
                        '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Khoảng tứ phân vị của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\Delta_Q=Q_3-Q_1=%s-%s=%s$.\\\\ \n'

                        'Giá trị đại diện của các nhóm số liệu là \\\\ \n'
                        '\\hspace*{1cm} $x_1=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_2=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_3=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_4=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_5=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{1}{%s}\\left( %s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s \\right)=%s$. \\\\ \n'
                        'Phương sai của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $s^2=\\dfrac{1}{%s}\\left( %s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2 \\right)-\\left(%s\\right)^2=%s$. \\\\ \n'
                        'Độ lệch chuẩn của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $s=\\sqrt{s^2}=%s$.'

                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),latex(tong),latex(tong),
                        latex(n),latex(n/4+1/2),latex(Q1_interval[0]),latex(Q1_interval[1]),
                        latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),
                        latex(n),latex(n/2+n/4+1/2),latex(Q3_interval[0]),latex(Q3_interval[1]),
                        latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),
                        latex(kqQ3),latex(kqQ1),latex(kq),

                            latex(v),latex(v+k),latex(x1),
                            latex(v+k),latex(v+2*k),latex(x2),
                            latex(v+2*k),latex(v+3*k),latex(xe3),
                            latex(v+3*k),latex(v+4*k),latex(x4),
                            latex(v+4*k),latex(v+5*k),latex(x5),
                            latex(tong),latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(xtb),
                            latex(tong),latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(xtb),latex(phuong_sai),
                            latex(do_lech),
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.0', '')
            return content

