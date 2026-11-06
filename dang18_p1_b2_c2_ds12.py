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


def bt_dang18_p1_b2_c2_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random dữ liệu ngữ cảnh
                names = ["An", "Bình", "Cường", "Dũng", "Hoa", "Lan", "Mai", "Hùng"]
                name = random.choice(names)
                activities = ["nhảy hiện đại", "chơi thể thao", "tự học", "đọc sách", "chơi đàn piano"]
                activity = random.choice(activities)

                # Random các khoảng số liệu [a; a+h)
                h = random.choice([5, 10])
                a = random.choice([10, 15, 20, 25])

                # Tạo 5 khoảng và tính giá trị đại diện c_i
                intervals = [(a + i*h, a + (i+1)*h) for i in range(5)]
                c = [(iv[0] + iv[1])/2 for iv in intervals]

                # Random tần số (số ngày)
                n = [random.randint(2, 8) for _ in range(5)]
                N = sum(n)

                # Hàm định dạng số bỏ .0 và chuyển dấu chấm thành phẩy
                def format_num(val):
                    if val == int(val):
                        return str(int(val))
                    return str(val).replace('.', ',')

                c_str = [format_num(val) for val in c]

                # Tính toán chính xác bằng phân số (Fraction) để tránh sai số thập phân khi hiển thị LaTeX
                mean_val_exact = frac(0)
                for i in range(5):
                    mean_val_exact += frac(int(c[i]*10), 10) * n[i]
                mean_val_exact = mean_val_exact / N

                var_val_exact = frac(0)
                for i in range(5):
                    var_val_exact += n[i] * (frac(int(c[i]*10), 10) - mean_val_exact)**2
                var_val_exact = var_val_exact / N

                # Chuyển đổi sang dạng Rational của Sympy để dùng lệnh latex() xuất phân số
                mean_frac = Rational(mean_val_exact.numerator, mean_val_exact.denominator)
                var_frac = Rational(var_val_exact.numerator, var_val_exact.denominator)

                # Tính phương sai và độ lệch chuẩn bằng số thực
                variance = float(var_val_exact)
                std_dev = math.sqrt(variance)

                # Làm tròn chuẩn xác bằng Decimal
                ans_true_val = Decimal(str(std_dev)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                ans_true_str = str(ans_true_val).replace('.', ',')

                var_val_d1 = Decimal(str(variance)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                var_val_d2 = Decimal(str(variance + 0.01)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Tạo các đáp án gây nhiễu
                set_options = {str(var_val_d1).replace('.', ','), str(var_val_d2).replace('.', ',')}
                fake_val = float(ans_true_val) - 0.2

                # Đảm bảo đủ 3 phương án sai và không trùng với đáp án đúng
                while len(set_options) < 3 or ans_true_str in set_options:
                    fake_val += 0.1
                    fake_str = str(Decimal(str(fake_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    if fake_str != ans_true_str:
                        set_options.add(fake_str)

                list_options = list(set_options)[:3]

                # Gán các đáp án
                da_d = '\\True $' + ans_true_str + '$'
                da_s1 = '$' + list_options[0] + '$'
                da_s2 = '$' + list_options[1] + '$'
                da_s3 = '$' + list_options[2] + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xây dựng nội dung câu hỏi
                noidungcauhoi = ('''Bạn %s rất thích %s. Thời gian tập luyện mỗi ngày của bạn %s được thống kê lại ở bảng sau:
            \\begin{center}
            \\begin{tabular}{|c|c|c|c|c|c|}
            \\hline
            \\textbf{Thời gian (phút)} & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\
            \\hline
            \\textbf{Số ngày} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
            \\hline
            \\end{tabular}
            \\end{center}
            Độ lệch chuẩn của mẫu số liệu ghép nhóm có giá trị gần nhất với giá trị nào dưới đây?''' % (
                    name, activity, name,
                    intervals[0][0], intervals[0][1],
                    intervals[1][0], intervals[1][1],
                    intervals[2][0], intervals[2][1],
                    intervals[3][0], intervals[3][1],
                    intervals[4][0], intervals[4][1],
                    n[0], n[1], n[2], n[3], n[4]
                ))

                # Xây dựng nội dung lời giải
                loigiai = ('''Giá trị trung bình của mẫu số liệu ghép nhóm là $\\overline{x} = \\frac{%s \\cdot %s + %s \\cdot %s + ... + %s \\cdot %s}{%s} = %s$.\\\\
            Độ lệch chuẩn mẫu số liệu ghép nhóm là
            $$s = \\sqrt{s^2} = \\sqrt{\\frac{(%s - \\overline{x})^2 \\cdot %s + (%s - \\overline{x})^2 \\cdot %s + ... + (%s - \\overline{x})^2 \\cdot %s}{%s}} = \\sqrt{%s} \\approx %s$$\\\\
            Độ lệch chuẩn của mẫu số liệu ghép nhóm có giá trị gần nhất với $%s$.''' % (
                    c_str[0], n[0], c_str[1], n[1], c_str[-1], n[-1], N, latex(mean_frac).replace('.', ','),
                    c_str[0], n[0], c_str[1], n[1], c_str[-1], n[-1], N, latex(var_frac).replace('.', ','), ans_true_str,
                    ans_true_str
                ))

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

