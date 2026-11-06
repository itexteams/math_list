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


def bt_dang19_p1_b1_c2_ds12(self):
            # Khai báo biến
            lisdang=['3']
            dang=random.choice(lisdang)
            if dang=='4':
                # Khai báo biến
                lisv=[1,2,3,4,5,6]
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

                lisk=[1,2,3,4,5,6]
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

                du = ['$\\Delta_Q=%s$'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$\\Delta_Q=%s$'%(latex(kq+1)),
                    '$\\Delta_Q=%s$'%(latex(kq+2)),
                    '$\\Delta_Q=%s$'%(latex(kq+3)),
                    '$\\Delta_Q=%s$'%(latex(kq-1)),
                    '$\\Delta_Q=%s$'%(latex(kq-2)),
                    '$\\Delta_Q=%s$'%(latex(kq-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Kiểm tra điện lượng (nghìn mAh) của $%s$ viên pin tiểu do một hãng sản xuất được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Điện lượng (nghìn mAh) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số viên pin & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Khoảng tứ phân vị của mẫu số liệu là'
                                %(latex(tong),
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5)
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
                loigiai=('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là điện lượng của $%s$ viên pin tiểu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự tăng dần. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ ba là \\\\ \n'
                        '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Vậy khoảng tứ phân vị của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\Delta_Q=Q_3-Q_1=%s-%s=%s$.'

                        %(latex(tong),latex(tong),latex(tong),
                        latex(n),latex(n/4-1/4),latex(n/4-1/4+1),latex(Q1_interval[0]),latex(Q1_interval[1]),
                        latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),
                        latex(n),latex(3*n/4+1/4),latex(3*n/4+1/4+1),latex(Q3_interval[0]),latex(Q3_interval[1]),
                        latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),
                        latex(kqQ3),latex(kqQ1),latex(kq)
                        ))
            if dang=='3':
                # Khai báo biến
                lisv=[1,2,3,4,5,6]
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

                lisk=[1,2,3,4,5,6]
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

                du = ['$\\Delta_Q=%s$'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$\\Delta_Q=%s$'%(latex(kq+1)),
                    '$\\Delta_Q=%s$'%(latex(kq+2)),
                    '$\\Delta_Q=%s$'%(latex(kq+3)),
                    '$\\Delta_Q=%s$'%(latex(kq-1)),
                    '$\\Delta_Q=%s$'%(latex(kq-2)),
                    '$\\Delta_Q=%s$'%(latex(kq-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Kiểm tra điện lượng (nghìn mAh) của $%s$ viên pin tiểu do một hãng sản xuất được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Điện lượng (nghìn mAh) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số viên pin & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Khoảng tứ phân vị của mẫu số liệu là'
                                %(latex(tong),
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5)
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
                loigiai=('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là điện lượng của $%s$ viên pin tiểu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự tăng dần. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ ba là \\\\ \n'
                        '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Vậy khoảng tứ phân vị của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\Delta_Q=Q_3-Q_1=%s-%s=%s$.'

                        %(latex(tong),latex(tong),latex(tong),
                        latex(n),latex(n/4+1/4),latex(Q1_interval[0]),latex(Q1_interval[1]),
                        latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),
                        latex(n),latex(3*n/4+3/4),latex(Q3_interval[0]),latex(Q3_interval[1]),
                        latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),
                        latex(kqQ3),latex(kqQ1),latex(kq)
                        ))
            if dang=='2':
                # Khai báo biến
                lisv=[1,2,3,4,5,6]
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

                lisk=[1,2,3,4,5,6]
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

                du = ['$\\Delta_Q=%s$'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$\\Delta_Q=%s$'%(latex(kq+1)),
                    '$\\Delta_Q=%s$'%(latex(kq+2)),
                    '$\\Delta_Q=%s$'%(latex(kq+3)),
                    '$\\Delta_Q=%s$'%(latex(kq-1)),
                    '$\\Delta_Q=%s$'%(latex(kq-2)),
                    '$\\Delta_Q=%s$'%(latex(kq-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Kiểm tra điện lượng (nghìn mAh) của $%s$ viên pin tiểu do một hãng sản xuất được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Điện lượng (nghìn mAh) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số viên pin & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Khoảng tứ phân vị của mẫu số liệu là'
                                %(latex(tong),
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5)
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
                loigiai=('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là điện lượng của $%s$ viên pin tiểu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự tăng dần. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ ba là \\\\ \n'
                        '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Vậy khoảng tứ phân vị của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\Delta_Q=Q_3-Q_1=%s-%s=%s$.'

                        %(latex(tong),latex(tong),latex(tong),
                        latex(n),latex(n/4+1/2-1/2),latex(n/4+1/2+1/2),latex(Q1_interval[0]),latex(Q1_interval[1]),
                        latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),
                        latex(n),latex(n/2+n/4+1/2-1/2),latex(n/2+n/4+1/2+1/2),latex(Q3_interval[0]),latex(Q3_interval[1]),
                        latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),
                        latex(kqQ3),latex(kqQ1),latex(kq)
                        ))
            if dang=='1':
                # Khai báo biến
                lisv=[1,2,3,4,5,6]
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

                lisk=[1,2,3,4,5,6]
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

                du = ['$\\Delta_Q=%s$'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$\\Delta_Q=%s$'%(latex(kq+1)),
                    '$\\Delta_Q=%s$'%(latex(kq+2)),
                    '$\\Delta_Q=%s$'%(latex(kq+3)),
                    '$\\Delta_Q=%s$'%(latex(kq-1)),
                    '$\\Delta_Q=%s$'%(latex(kq-2)),
                    '$\\Delta_Q=%s$'%(latex(kq-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Kiểm tra điện lượng (nghìn mAh) của $%s$ viên pin tiểu do một hãng sản xuất được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Điện lượng (nghìn mAh) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số viên pin & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Khoảng tứ phân vị của mẫu số liệu là'
                                %(latex(tong),
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5)
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
                loigiai=('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là điện lượng của $%s$ viên pin tiểu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự tăng dần. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ ba là \\\\ \n'
                        '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$. \\\\ \n'
                        'Vậy khoảng tứ phân vị của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\Delta_Q=Q_3-Q_1=%s-%s=%s$.'

                        %(latex(tong),latex(tong),latex(tong),
                        latex(n),latex(n/4+1/2),latex(Q1_interval[0]),latex(Q1_interval[1]),
                        latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),
                        latex(n),latex(n/2+n/4+1/2),latex(Q3_interval[0]),latex(Q3_interval[1]),
                        latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),
                        latex(kqQ3),latex(kqQ1),latex(kq)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.0', '')
            return content

