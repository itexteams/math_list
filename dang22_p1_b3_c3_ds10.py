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


def bt_dang22_p1_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            # Hàm hỗ trợ định dạng số
            def format_num(num):
                if num == int(num):
                    return str(int(num))
                return str(num).replace('.', ',')

            if dang=='1':
                # Số lượng ngày khảo sát
                n = 10

                # B3: Thuật toán tạo số liệu luôn có giá trị bất thường
                # Tạo 8 giá trị "bình thường" ở giữa
                core_data = [random.randint(10, 20) for _ in range(8)]
                core_data.sort()

                # Tạm tính Q1, Q3 của thân để ước lượng ngưỡng
                # Với n=10, khi ghép thêm 2 đầu, Q1 sẽ là phần tử thứ 3 (index 2), Q3 là phần tử thứ 8 (index 7) của mảng full
                # Tương ứng với index 1 và 6 của core_data
                temp_q1 = core_data[1]
                temp_q3 = core_data[6]
                temp_iqr = temp_q3 - temp_q1

                lower_bound_est = temp_q1 - 1.5 * temp_iqr
                upper_bound_est = temp_q3 + 1.5 * temp_iqr

                # Tạo 2 giá trị bất thường nằm ngoài các ngưỡng ước lượng
                outlier_min = math.floor(lower_bound_est) - random.randint(1, 4)
                # Đảm bảo số ghế không âm
                if outlier_min < 0:
                    outlier_min = 0

                outlier_max = math.ceil(upper_bound_est) + random.randint(1, 4)

                # Ghép thành mẫu số liệu hoàn chỉnh
                full_data = [outlier_min] + core_data + [outlier_max]

                # Xáo trộn mẫu số liệu để tạo đề bài ngẫu nhiên
                random.shuffle(full_data)
                data_str_de = " \\hspace{0.5cm} ".join(map(str, full_data))

                # B2: Tính toán chính xác các tham số cho mảng đã sort
                sorted_data = sorted(full_data)
                sorted_data_str = " \\hspace{0.5cm} ".join(map(str, sorted_data))

                # Tính Q1, Q2, Q3
                q2_val = (sorted_data[4] + sorted_data[5]) / 2
                q1_val = sorted_data[2]
                q3_val = sorted_data[7]
                iqr_val = q3_val - q1_val

                lower_limit = q1_val - 1.5 * iqr_val
                upper_limit = q3_val + 1.5 * iqr_val

                # Tìm thực tế các giá trị bất thường dựa trên limit chuẩn
                outliers = []
                for val in sorted_data:
                    if val < lower_limit or val > upper_limit:
                        outliers.append(val)

                # Xử lý chuỗi đáp án đúng
                if len(outliers) == 2:
                    ans_correct_str = f"{outliers[0]} và {outliers[1]}"
                elif len(outliers) == 1:
                    ans_correct_str = f"{outliers[0]}"
                else:
                    ans_correct_str = "Không có giá trị nào"

                du = [ans_correct_str]
                da = random.choice(du)

                # Sinh đáp án nhiễu
                distractors = []
                if len(outliers) == 2:
                    distractors.append(str(outliers[0]))
                    distractors.append(str(outliers[1]))
                elif len(outliers) == 1:
                    distractors.append(str(sorted_data[0]) if outliers[0] != sorted_data[0] else str(sorted_data[-1]))
                    distractors.append(f"{sorted_data[0]} và {sorted_data[-1]}")

                # Thêm nhiễu ngẫu nhiên
                distractors.append(str(q1_val))
                distractors.append(str(q3_val))
                distractors.append(f"{q1_val} và {q3_val}")

                s = distractors
                s = list(set(s) - set(du))
                random.shuffle(s)

                das1 = str(s[0])
                das2 = str(s[1])
                das3 = str(s[2])

                # Câu hỏi
                noidungcauhoi = ('''Mẫu số liệu sau cho biết số ghế trống tại một rạp chiếu phim trong mười ngày:
            \\begin{center}
            %s
            \\end{center}
            Các giá trị bất thường của mẫu số liệu trên bằng cách sử dụng biểu đồ hộp là''' 
                                 % (data_str_de))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Trích xuất để viết lời giải
                # Xử lý text giải thích phần outliers
                outlier_explanation = ""
                for val in outliers:
                    if val < lower_limit:
                        outlier_explanation += f" ${val}$ ghế (nhỏ hơn ${format_num(lower_limit)}$ ghế) và "
                    elif val > upper_limit:
                        outlier_explanation += f" ${val}$ ghế (lớn hơn ${format_num(upper_limit)}$ ghế) và "

                # Bỏ chữ " và " ở cuối chuỗi
                if outlier_explanation.endswith(" và "):
                    outlier_explanation = outlier_explanation[:-4]

                num_outliers = len(outliers)
                if num_outliers == 0:
                    conclusion_str = "mẫu số liệu không có giá trị bất thường."
                else:
                    conclusion_str = f"mẫu số liệu có {num_outliers} giá trị được xem là bất thường là {outlier_explanation}."

                # Nội dung lời giải
                loigiai = ('''Sắp xếp mẫu số liệu trên theo thứ tự không giảm ta được:\\\\
            %s\\\\
            Từ mẫu số liệu ta tính được $Q_2 = \\frac{%s+%s}{2} = %s, Q_1 = %s$ và $Q_3 = %s$.\\\\
            Do đó khoảng tứ phân vị là: $\\Delta_Q = %s - %s = %s$.\\\\
            Ta có $Q_1 - 1,5\\Delta_Q = %s - 1,5 \\cdot %s = %s$ và $Q_3 + 1,5\\Delta_Q = %s + 1,5 \\cdot %s = %s$ nên %s'''
                           % (sorted_data_str, 
                              sorted_data[4], sorted_data[5], format_num(q2_val), q1_val, q3_val,
                              q3_val, q1_val, iqr_val,
                              q1_val, iqr_val, format_num(lower_limit), q3_val, iqr_val, format_num(upper_limit), conclusion_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

