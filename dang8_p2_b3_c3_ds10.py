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


def bt_dang8_p2_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo hàm đếm số đáp án đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Định dạng số thập phân dùng dấu phẩy của Việt Nam
            def format_num(num):
                res = f"{round(num, 4):g}"
                return res.replace('.', ',')

            ######################################################################## Xử lý Data Random ########################

            # Sinh ngẫu nhiên dữ liệu 8 loại rượu (Giá từ 1.00 đến 3.00)
            data = sorted([round(random.randint(100, 300) / 100.0, 2) for _ in range(8)])

            # Thêm xác suất 30% tạo ra một giá trị bất thường (outlier) ở cuối để câu (d) có sự đa dạng
            if random.random() < 0.3:
                data[-1] = round(data[-2] + random.randint(150, 250) / 100.0, 2)

            # Tính toán các đại lượng thống kê
            min_val = data[0]
            max_val = data[-1]
            R = max_val - min_val

            Q1 = (data[1] + data[2]) / 2.0
            Q2 = (data[3] + data[4]) / 2.0
            Q3 = (data[5] + data[6]) / 2.0
            delta_Q = Q3 - Q1

            lower_bound = Q1 - 1.5 * delta_Q
            upper_bound = Q3 + 1.5 * delta_Q

            # Xác định giá trị bất thường
            outliers = [x for x in data if x < lower_bound or x > upper_bound]

            # Format chuỗi
            data_str = " \\quad ".join(map(format_num, data))
            data_left_str = " \\quad ".join(map(format_num, data[:4]))
            data_right_str = " \\quad ".join(map(format_num, data[4:]))

            # Nội dung câu hỏi
            noidungcauhoi = f"Mẫu số liệu sau là giá tiền (triệu đồng) của 8 loại rượu ngoại được nhập về tại một cửa hàng rượu: ${data_str}$."

            ######################################################################## Nhận biết ############################################

            R_fake = R + random.choice([-0.2, -0.15, 0.1, 0.25])
            if R_fake <= 0: R_fake = R + 0.3

            # Các đáp án
            nb_da_1_d = f'\\True Khoảng biến thiên của mẫu là: $R = {format_num(R)}$'
            nb_da_1_s = f'Khoảng biến thiên của mẫu là: $R = {format_num(R_fake)}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Nội dung lời giải
            loigiai_nb_1 = (f"Giá trị lớn nhất và nhỏ nhất trong mẫu số liệu là: $x_{{max}} = {format_num(max_val)}; x_{{min}} = {format_num(min_val)}$.\\\\"
                            f"Khoảng biến thiên của mẫu là: $R = x_{{max}} - x_{{min}} = {format_num(max_val)} - {format_num(min_val)} = {format_num(R)}$.")
            list_nb_2 = [loigiai_nb_1]

            ######################################################################## Thông hiểu ############################################

            delta_Q_fake = delta_Q + random.choice([-0.1, 0.15, 0.05, -0.05])
            if delta_Q_fake <= 0: delta_Q_fake = delta_Q + 0.1

            # Các đáp án
            th_da_1_d = f'\\True Khoảng tứ phân vị là: $\\Delta_Q = {format_num(delta_Q)}$'
            th_da_1_s = f'Khoảng tứ phân vị là: $\\Delta_Q = {format_num(delta_Q_fake)}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Nội dung lời giải
            loigiai_th_1 = (f"Xét mẫu số liệu: ${data_str}$.\\\\"
                            f"Tứ phân vị thứ hai cũng là trung vị của mẫu: $Q_2 = \\frac{{{format_num(data[3])} + {format_num(data[4])}}}{{2}} = {format_num(Q2)}$.\\\\"
                            f"Xét nửa mẫu bên trái: ${data_left_str}$.\\\\"
                            f"Tứ phân vị thứ nhất là trung vị nửa mẫu này: $Q_1 = \\frac{{{format_num(data[1])} + {format_num(data[2])}}}{{2}} = {format_num(Q1)}$.\\\\"
                            f"Xét nửa mẫu bên phải: ${data_right_str}$.\\\\"
                            f"Tứ phân vị thứ ba là trung vị nửa mẫu này: $Q_3 = \\frac{{{format_num(data[5])} + {format_num(data[6])}}}{{2}} = {format_num(Q3)}$.\\\\"
                            f"Khoảng tứ phân vị là: $\\Delta_Q = Q_3 - Q_1 = {format_num(Q3)} - {format_num(Q1)} = {format_num(delta_Q)}$.")
            list_th_2 = [loigiai_th_1]

            ######################################################################## Vận dụng ############################################

            lower_fake = lower_bound + random.choice([-0.25, 0.15, 0.35, -0.1])

            vd_da_1_d = f'\\True $Q_1 - 1,5\\Delta_Q = {format_num(lower_bound)}$'
            vd_da_1_s = f'$Q_1 - 1,5\\Delta_Q = {format_num(lower_fake)}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Nội dung lời giải (Chỉnh sửa lỗi đánh máy Q2 thành Q3 cho chuẩn Toán so với ảnh gốc)
            loigiai_vd_1 = (f"Ta có: $Q_1 - 1,5\\Delta_Q = {format_num(lower_bound)} ; Q_3 + 1,5\\Delta_Q = {format_num(upper_bound)}$.")
            list_vd_2 = [loigiai_vd_1]

            ######################################################################## Vận dụng cao ########################################

            if len(outliers) == 0:
                vdc_da_1_d = '\\True Mẫu số liệu không có giá trị nào là bất thường'
                vdc_da_1_s = 'Mẫu số liệu có giá trị bất thường'

                loigiai_vdc_1 = (f"Ta thấy trong mẫu số liệu không có giá trị nào nhỏ hơn ${format_num(lower_bound)}$, "
                                 f"cũng không có giá trị nào lớn hơn ${format_num(upper_bound)}$.\\\\"
                                 f"Vậy mẫu số liệu không có giá trị nào là bất thường.")
            else:
                outlier_str_display = ", ".join(map(format_num, outliers))
                vdc_da_1_d = f'\\True Mẫu số liệu có giá trị bất thường là ${outlier_str_display}$'
                vdc_da_1_s = 'Mẫu số liệu không có giá trị nào là bất thường'

                loigiai_vdc_1 = (f"Ta thấy trong mẫu số liệu có giá trị ${outlier_str_display}$ "
                                 f"nằm ngoài khoảng $[{format_num(lower_bound)}; {format_num(upper_bound)}]$.\\\\"
                                 f"Vậy mẫu số liệu có giá trị bất thường là ${outlier_str_display}$.")

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            list_vdc_2 = [loigiai_vdc_1]

            ######################################################################## Xáo trộn và in kết quả ###############################

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n'
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
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

