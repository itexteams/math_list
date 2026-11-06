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


def bt_dang21_p1_b2_c2_ds10(self):
            # Định nghĩa hàm
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp đảm bảo sinh số liệu và tìm được các đáp án hợp lệ
                while True:
                    # 1. Sinh ngẫu nhiên hệ số cho 2 bất phương trình
                    a1, b1, c1 = randint(-2, 2), randint(-2, 2), randint(-5, 5)
                    a2, b2, c2 = randint(-2, 2), randint(-2, 2), randint(-5, 5)

                    # Đảm bảo hệ số ẩn không đồng thời bằng 0 để giữ dạng BPT bậc nhất 2 ẩn
                    if (a1 == 0 and b1 == 0) or (a2 == 0 and b2 == 0):
                        continue

                    # Chọn ngẫu nhiên hoàn toàn dấu bất đẳng thức cho cả 2 BPT
                    sign1 = random.choice(['<', '>', '<=', '>='])
                    sign2 = random.choice(['<', '>', '<=', '>='])

                    # Tạo biểu thức vế trái bằng SymPy (Tự động chuẩn hóa dấu, loại bỏ + -)
                    expr1 = a1*x + b1*y + c1
                    expr2 = a2*x + b2*y + c2

                    # 2. Tìm một điểm ngẫu nhiên (x0, y0) thỏa mãn hệ để làm đáp án ĐÚNG
                    found_true = False
                    x0, y0 = 0, 0

                    # Quét nhanh ngẫu nhiên trong miền số nguyên nhỏ
                    for _ in range(150):
                        test_x = randint(-3, 3)
                        test_y = randint(-3, 3)

                        val1 = expr1.subs({x: test_x, y: test_y})
                        val2 = expr2.subs({x: test_x, y: test_y})

                        # Kiểm tra tính đúng đắn với dấu sign1 ngẫu nhiên
                        cond1 = False
                        if sign1 == '<' and val1 < 0: cond1 = True
                        elif sign1 == '>' and val1 > 0: cond1 = True
                        elif sign1 == '<=' and val1 <= 0: cond1 = True
                        elif sign1 == '>=' and val1 >= 0: cond1 = True

                        # Kiểm tra tính đúng đắn với dấu sign2 ngẫu nhiên
                        cond2 = False
                        if sign2 == '<' and val2 < 0: cond2 = True
                        elif sign2 == '>' and val2 > 0: cond2 = True
                        elif sign2 == '<=' and val2 <= 0: cond2 = True
                        elif sign2 == '>=' and val2 >= 0: cond2 = True

                        if cond1 and cond2:
                            x0, y0 = test_x, test_y
                            found_true = True
                            break

                    if not found_true:
                        continue # Nếu hệ dấu + hệ số này vô nghiệm trong miền quét thì tạo lại hệ mới

                    # 3. Tìm 3 tọa độ ngẫu nhiên không thỏa mãn hệ để làm đáp án SAI
                    wrong_points = set()
                    attempts = 0
                    while len(wrong_points) < 3 and attempts < 200:
                        attempts += 1
                        wx = randint(-4, 4)
                        wy = randint(-4, 4)
                        if (wx == x0 and wy == y0):
                            continue

                        w_val1 = expr1.subs({x: wx, y: wy})
                        w_val2 = expr2.subs({x: wx, y: wy})

                        w_cond1 = False
                        if sign1 == '<' and w_val1 < 0: w_cond1 = True
                        elif sign1 == '>' and w_val1 > 0: w_cond1 = True
                        elif sign1 == '<=' and w_val1 <= 0: w_cond1 = True
                        elif sign1 == '>=' and w_val1 >= 0: w_cond1 = True

                        w_cond2 = False
                        if sign2 == '<' and w_val2 < 0: w_cond2 = True
                        elif sign2 == '>' and w_val2 > 0: w_cond2 = True
                        elif sign2 == '<=' and w_val2 <= 0: w_cond2 = True
                        elif sign2 == '>=' and w_val2 >= 0: w_cond2 = True

                        # Điểm sai là điểm vi phạm ít nhất một trong hai điều kiện của hệ
                        if not (w_cond1 and w_cond2):
                            wrong_points.add((wx, wy))

                    if len(wrong_points) < 3:
                        continue

                    break

                # Format hiển thị tọa độ các cặp số đáp án
                da = f"$({x0}; {y0})$"

                list_wrong = list(wrong_points)
                das1 = f"$({list_wrong[0][0]}; {list_wrong[0][1]})$"
                das2 = f"$({list_wrong[1][0]}; {list_wrong[1][1]})$"
                das3 = f"$({list_wrong[2][0]}; {list_wrong[2][1]})$"

                # Định dạng chuỗi LaTeX cho hệ bất phương trình
                str_expr1 = latex(expr1)
                str_expr2 = latex(expr2)

                # Biến đổi các ký tự dấu sang chuẩn mã hiển thị LaTeX
                sign1_latex = '\\le' if sign1 == '<=' else ('\\ge' if sign1 == '>=' else sign1)
                sign2_latex = '\\le' if sign2 == '<=' else ('\\ge' if sign2 == '>=' else sign2)

                # Câu hỏi
                noidungcauhoi = (
                    f"Cặp số nào sau đây là nghiệm của hệ bất phương trình "
                    f"$\\begin{{cases}} {str_expr1} {sign1_latex} 0 \\\\ {str_expr2} {sign2_latex} 0 \\end{{cases}}$?"
                )

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tính toán giá trị số cụ thể sau khi thay điểm đúng để hiển thị trong lời giải
                v1_true = expr1.subs({x: x0, y: y0})
                v2_true = expr2.subs({x: x0, y: y0})

                loigiai = (
                    f"Thay tọa độ của các cặp số đã cho vào hệ bất phương trình để thử lại:\\\\ \n"
                    f"Thay cặp số {da} vào hệ ta được:\\\\ \n"
                    f"$\\begin{{cases}} {v1_true} {sign1_latex} 0 \\\\ {v2_true} {sign2_latex} 0 \\end{{cases}}$ (luôn đúng).\\\\ \n"
                    f"Do đó, cặp số {da} là một nghiệm của hệ bất phương trình đã cho."
                )

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

