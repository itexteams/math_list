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


def bt_dang28_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Hàm hỗ trợ tạo bảng dữ liệu thô (2 dòng, 15 cột)
                def create_raw_table(data):
                    row1 = " & ".join(map(str, data[:15]))
                    row2 = " & ".join(map(str, data[15:]))
                    latex_str = "\\begin{center}\n\\begin{tabular}{|" + "c|"*15 + "}\n\\hline\n"
                    latex_str += row1 + " \\\\\n\\hline\n"
                    latex_str += row2 + " \\\\\n\\hline\n"
                    latex_str += "\\end{tabular}\n\\end{center}"
                    return latex_str

                # Hàm hỗ trợ lập bảng tần số
                def create_freq_table(data):
                    counts = {}
                    for val in data:
                        counts[val] = counts.get(val, 0) + 1
                    sorted_keys = sorted(counts.keys())

                    num_cols = len(sorted_keys)
                    cols_format = "|" + "c|" * num_cols

                    header = "Giá trị & " + " & ".join(str(k) for k in sorted_keys) + " \\\\"
                    row_freq = "Tần số & " + " & ".join(str(counts[k]) for k in sorted_keys) + " \\\\"

                    # Dùng tabularx hoặc resizebox thường cần package ngoài, ta dùng tabular chuẩn. 
                    # Bảng có thể dài nên dùng font nhỏ hoặc cứ để nguyên cấu trúc chuẩn.
                    latex_str = "\\begin{center}\n"
                    latex_str += "\\begin{tabular}{|c" + cols_format + "}\n\\hline\n"
                    latex_str += header + "\n\\hline\n"
                    latex_str += row_freq + "\n\\hline\n"
                    latex_str += "\\end{tabular}\n\\end{center}"
                    return latex_str

                # Random 30 giá trị cho con đường A và B
                data_A = [random.randint(60, 90) for _ in range(30)]
                data_B = [random.randint(55, 85) for _ in range(30)]

                # Tính trung bình và làm tròn 1 chữ số thập phân
                mean_A = sum(data_A) / 30.0
                mean_B = sum(data_B) / 30.0

                mean_A_rounded = round(mean_A, 1)
                mean_B_rounded = round(mean_B, 1)

                str_A = f"{mean_A_rounded:.1f}".replace('.', ',')
                str_B = f"{mean_B_rounded:.1f}".replace('.', ',')

                # Đáp án đúng
                da = f"\\overline{{x}}_A \\approx {str_A}; \\overline{{x}}_B \\approx {str_B}."

                # Tạo đáp án nhiễu
                s_vals = []
                # Nhiễu 1: Đảo ngược A và B
                if mean_A_rounded != mean_B_rounded:
                    s_vals.append(f"\\overline{{x}}_A \\approx {str_B}; \\overline{{x}}_B \\approx {str_A}.")

                # Sinh các nhiễu khác bằng cách cộng trừ ngẫu nhiên
                while len(s_vals) < 3:
                    off_A = round(random.choice([-1.1, -0.1, 0.1, 1.1]), 1)
                    off_B = round(random.choice([-1.2, -0.2, 0.2, 1.2]), 1)

                    cand_A = round(mean_A_rounded + off_A, 1)
                    cand_B = round(mean_B_rounded + off_B, 1)

                    str_cand_A = f"{cand_A:.1f}".replace('.', ',')
                    str_cand_B = f"{cand_B:.1f}".replace('.', ',')
                    cand_str = f"\\overline{{x}}_A \\approx {str_cand_A}; \\overline{{x}}_B \\approx {str_cand_B}."

                    if cand_str not in s_vals and cand_str != da:
                        s_vals.append(cand_str)

                das1 = s_vals[0]
                das2 = s_vals[1]
                das3 = s_vals[2]

                # Tạo bảng đề bài
                table_A_raw = create_raw_table(data_A)
                table_B_raw = create_raw_table(data_B)

                # Nội dung câu hỏi
                noidungcauhoi = f'''Trên $2$ con đường $A$ và $B$, trạm kiểm soát đã ghi lại tốc độ (km/h) của $30$ chiếc xe ô tô trên mỗi con đường như sau:
            Con đường $A$:
            {table_A_raw}
            Con đường $B$:
            {table_B_raw}
            Số trung bình $\\overline{{x}}_A; \\overline{{x}}_B$ của mẫu số liệu con đường $A$ và con đường $B$ (chính xác đến hàng phần chục) là'''

                # Các đáp án
                da_d = ('\\True $' + str(da) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$' 
                da_s3 = '$' + str(das3) + '$' 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tạo bảng tần số cho lời giải
                table_A_freq = create_freq_table(data_A)
                table_B_freq = create_freq_table(data_B)

                # Nội dung lời giải
                loigiai = f'''* \\textbf{{Con đường $A$}}:
            Sắp xếp các số liệu theo thứ tự không giảm
            {table_A_freq}
            Số trung bình của mẫu số liệu: $\\overline{{x}}_A \\approx {str_A}$.\\\\
            * \\textbf{{Con đường $B$}}:
            Sắp xếp các số liệu theo thứ tự không giảm
            {table_B_freq}
            Số trung bình của mẫu số liệu: $\\overline{{x}}_B \\approx {str_B}$.'''

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

