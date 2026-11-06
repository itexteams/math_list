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


def bt_dang35_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Cố định số phần tử của mẫu số liệu là 16
                n = 16

                # Sinh ngẫu nhiên 16 giá trị sản lượng chè (ví dụ từ 105 đến 135 kg)
                list_num = [random.randint(105, 135) for _ in range(n)]

                # Sắp xếp mảng số liệu theo thứ tự không giảm
                sorted_num = sorted(list_num)

                # --- TẠO BẢNG LATEX CHO ĐỀ BÀI (Chưa sắp xếp) ---
                row1_orig = " & ".join(map(str, list_num[:8]))
                row2_orig = " & ".join(map(str, list_num[8:]))
                table_orig = (
                    "\\begin{center}\n"
                    "\\begin{tabular}{|c|c|c|c|c|c|c|c|}\n"
                    "\\hline\n"
                    f"{row1_orig} \\\\\n"
                    "\\hline\n"
                    f"{row2_orig} \\\\\n"
                    "\\hline\n"
                    "\\end{tabular}\n"
                    "\\end{center}"
                )

                # --- TẠO BẢNG LATEX CHO LỜI GIẢI (Đã sắp xếp) ---
                row1_sort = " & ".join(map(str, sorted_num[:8]))
                row2_sort = " & ".join(map(str, sorted_num[8:]))
                table_sort = (
                    "\\begin{center}\n"
                    "\\begin{tabular}{|c|c|c|c|c|c|c|c|}\n"
                    "\\hline\n"
                    f"{row1_sort} \\\\\n"
                    "\\hline\n"
                    f"{row2_sort} \\\\\n"
                    "\\hline\n"
                    "\\end{tabular}\n"
                    "\\end{center}"
                )

                # --- TÍNH TOÁN CÁC TỨ PHÂN VỊ CHO n=16 ---
                # Q2 là trung bình cộng của phần tử thứ 8 và thứ 9 (chỉ số 7 và 8)
                val2_1 = sorted_num[7]
                val2_2 = sorted_num[8]
                q2 = (val2_1 + val2_2) / 2
                q2_str = str(int(q2)) if q2.is_integer() else str(q2).replace('.', ',')

                # Q1 là trung bình cộng 2 phần tử chính giữa nửa trái (chỉ số 3 và 4)
                val1_1 = sorted_num[3]
                val1_2 = sorted_num[4]
                q1 = (val1_1 + val1_2) / 2
                q1_str = str(int(q1)) if q1.is_integer() else str(q1).replace('.', ',')

                # Q3 là trung bình cộng 2 phần tử chính giữa nửa phải (chỉ số 11 và 12)
                val3_1 = sorted_num[11]
                val3_2 = sorted_num[12]
                q3 = (val3_1 + val3_2) / 2
                q3_str = str(int(q3)) if q3.is_integer() else str(q3).replace('.', ',')

                # Chuỗi đáp án đúng
                da_str = f"Q_1 = {q1_str}, Q_2 = {q2_str}, Q_3 = {q3_str}"

                # --- TẠO CÁC ĐÁP ÁN NHIỄU ---
                options = set()
                while len(options) < 3:
                    # Tạo nhiễu bằng cách biến động nhẹ
                    f_q1_val = q1 + random.choice([-2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2])
                    f_q2_val = q2 + random.choice([-2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2])
                    f_q3_val = q3 + random.choice([-2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2])

                    f_q1_str = str(int(f_q1_val)) if f_q1_val.is_integer() else str(f_q1_val).replace('.', ',')
                    f_q2_str = str(int(f_q2_val)) if f_q2_val.is_integer() else str(f_q2_val).replace('.', ',')
                    f_q3_str = str(int(f_q3_val)) if f_q3_val.is_integer() else str(f_q3_val).replace('.', ',')

                    # Đảo vị trí nhiễu hoặc đổi giá trị
                    distractors = [
                        f"Q_1 = {f_q1_str}, Q_2 = {f_q2_str}, Q_3 = {f_q3_str}",
                        f"Q_1 = {f_q2_str}, Q_2 = {f_q1_str}, Q_3 = {f_q3_str}", # Cố tình đảo Q1, Q2 để đánh lừa
                        f"Q_1 = {q1_str}, Q_2 = {f_q2_str}, Q_3 = {f_q3_str}" 
                    ]

                    opt = random.choice(distractors)
                    if opt != da_str and opt not in options:
                        options.add(opt)

                options_list = list(options)
                random.shuffle(options_list)

                das1 = options_list[0]
                das2 = options_list[1]
                das3 = options_list[2]

                # Câu hỏi
                noidungcauhoi = f"Bảng số liệu sau đây cho biết sản lượng chè thu được trong 1 năm (kg/sào) của 16 hộ gia đình: \n{table_orig}\nCác tứ phân vị của mẫu số liệu đã cho là"

                # Định dạng đáp án
                da_d = '\\True $' + da_str + '$'
                da_s1 = '$' + das1 + '$'
                da_s2 = '$' + das2 + '$'
                da_s3 = '$' + das3 + '$'

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (f"Sắp xếp các giá trị theo thứ tự không giảm ta được: \n"
                           f"{table_sort}\n"
                           f"Ta có: \n"
                           f"$$Q_2 = \\frac{{{val2_1} + {val2_2}}}{{2}} = {q2_str}$$ \n"
                           f"$$Q_1 = \\frac{{{val1_1} + {val1_2}}}{{2}} = {q1_str}$$ \n"
                           f"$$Q_3 = \\frac{{{val3_1} + {val3_2}}}{{2}} = {q3_str}$$")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

