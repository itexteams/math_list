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


def bt_dang2_p2_b1_c2_ds12(self):
            # Khai báo biến
            lisdang=['3']
            dang=random.choice(lisdang)
            if dang=='4':
                # Khai báo biến
                lisv=[1,2,3,4,5,6,7,8,9,10]
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

                lisk=[1,2,3,4,5]
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


                # Nội dung câu hỏi
                noidungcauhoi = ('Cho bảng số liệu ghép nhóm sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Giá trị & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5)
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Cỡ mẫu là $n=%s$' %(latex(tong))
                nb_da_1_s = 'Cỡ mẫu là $n=%s$' %(latex(tong+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$.' 
                                %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong)
                            ))

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(kqQ1))
                th_da_1_s = 'Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(kqQ1+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ giá trị và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự tăng dần. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$.'

                        %(latex(tong),latex(tong),latex(tong),
                        latex(n),latex(n/4-1/4),latex(n/4-1/4+1),latex(Q1_interval[0]),latex(Q1_interval[1]),
                        latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),

                        ))

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(kqQ3))
                vd_da_1_s = 'Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(kqQ3-1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = (
                        'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ ba là \\\\ \n'
                        '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$.'

                        %(
                        latex(n),latex(3*n/4+1/4),latex(3*n/4+1/4+1),latex(Q3_interval[0]),latex(Q3_interval[1]),
                        latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),
                        ))

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q=%s$'%(latex(kq))
                vdc_da_1_s = 'Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q=%s$'%(latex(kq+1))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = (
                        'Khoảng tứ phân vị của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\Delta_Q=Q_3-Q_1=%s-%s=%s$.'

                        %(
                        latex(kqQ3),latex(kqQ1),latex(kq)
                        ))
                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='3':
                # Khai báo biến
                lisv=[1,2,3,4,5,6,7,8,9,10]
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

                lisk=[1,2,3,4,5]
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


                # Nội dung câu hỏi
                noidungcauhoi = ('Cho bảng số liệu ghép nhóm sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Giá trị & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5)
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Cỡ mẫu là $n=%s$' %(latex(tong))
                nb_da_1_s = 'Cỡ mẫu là $n=%s$' %(latex(tong+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$.' 
                                %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong)
                            ))

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(kqQ1))
                th_da_1_s = 'Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(kqQ1+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ giá trị và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự tăng dần. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$.'

                        %(latex(tong),latex(tong),latex(tong),
                        latex(n),latex(n/4+1/4),latex(Q1_interval[0]),latex(Q1_interval[1]),
                        latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),

                        ))

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(kqQ3))
                vd_da_1_s = 'Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(kqQ3-1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = (
                        'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$.\\\\ \n'
                        'Do đó, tứ phân vị thứ ba là \\\\ \n'
                        '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$.'

                        %(
                        latex(n),latex(3*n/4+3/4),latex(Q3_interval[0]),latex(Q3_interval[1]),
                        latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),
                        ))

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q=%s$'%(latex(kq))
                vdc_da_1_s = 'Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q=%s$'%(latex(kq+1))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = (
                        'Khoảng tứ phân vị của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\Delta_Q=Q_3-Q_1=%s-%s=%s$.'

                        %(
                        latex(kqQ3),latex(kqQ1),latex(kq)
                        ))
                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='2':
                # Khai báo biến
                lisv=[1,2,3,4,5,6,7,8,9,10]
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

                lisk=[1,2,3,4,5]
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


                # Nội dung câu hỏi
                noidungcauhoi = ('Cho bảng số liệu ghép nhóm sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Giá trị & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5)
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Cỡ mẫu là $n=%s$' %(latex(tong))
                nb_da_1_s = 'Cỡ mẫu là $n=%s$' %(latex(tong+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$.' 
                                %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong)
                            ))

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(kqQ1))
                th_da_1_s = 'Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(kqQ1+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ giá trị và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự tăng dần. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$.'

                        %(latex(tong),latex(tong),latex(tong),
                        latex(n),latex(n/4+1/2-1/2),latex(n/4+1/2+1/2),latex(Q1_interval[0]),latex(Q1_interval[1]),
                        latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),

                        ))

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(kqQ3))
                vd_da_1_s = 'Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(kqQ3-1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = (
                        'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ ba là \\\\ \n'
                        '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$.'

                        %(
                        latex(n),latex(n/2+n/4+1/2-1/2),latex(n/2+n/4+1/2+1/2),latex(Q3_interval[0]),latex(Q3_interval[1]),
                        latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),
                        ))

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q=%s$'%(latex(kq))
                vdc_da_1_s = 'Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q=%s$'%(latex(kq+1))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = (
                        'Khoảng tứ phân vị của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\Delta_Q=Q_3-Q_1=%s-%s=%s$.'

                        %(
                        latex(kqQ3),latex(kqQ1),latex(kq)
                        ))
                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='1':
                lisv=[1,2,3,4,5,6,7,8,9,10]
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

                lisk=[1,2,3,4,5]
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


                # Nội dung câu hỏi
                noidungcauhoi = ('Cho bảng số liệu ghép nhóm sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Giá trị & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5)
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Cỡ mẫu là $n=%s$' %(latex(tong))
                nb_da_1_s = 'Cỡ mẫu là $n=%s$' %(latex(tong+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$.' 
                                %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong)
                            ))

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(kqQ1))
                th_da_1_s = 'Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(kqQ1+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ giá trị và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự tăng dần.\\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$.\\\\ \n'
                        'Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$.'

                        %(latex(tong),latex(tong),latex(tong),
                        latex(n),latex(n/4+1/2),latex(Q1_interval[0]),latex(Q1_interval[1]),
                        latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),

                        ))

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(kqQ3))
                vd_da_1_s = 'Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(kqQ3-1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = (
                        'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        'Do đó, tứ phân vị thứ ba là \\\\ \n'
                        '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$.'

                        %(
                        latex(n),latex(n/2+n/4+1/2),latex(Q3_interval[0]),latex(Q3_interval[1]),
                        latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),
                        ))

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q=%s$'%(latex(kq))
                vdc_da_1_s = 'Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q=%s$'%(latex(kq+1))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = (
                        'Khoảng tứ phân vị của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\Delta_Q=Q_3-Q_1=%s-%s=%s$.'

                        %(
                        latex(kqQ3),latex(kqQ1),latex(kq)
                        ))
                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

