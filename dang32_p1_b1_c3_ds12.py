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


def bt_dang32_p1_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Hàm hỗ trợ dọn dẹp mã LaTeX cho đẹp (bỏ các dấu ngoặc thừa ở hàm lượng giác)
                def clean_latex(expr):
                    return latex(expr).replace('\\left(x \\right)', 'x')

                # 1. Chọn ngẫu nhiên hàm F(x) (kết quả nguyên hàm của f(x)) và các dạng lỗi sai tương ứng
                # Cấu trúc: (Hàm đúng, [Nhiễu 1 (sai dấu), Nhiễu 2 (nhầm sang đạo hàm), Nhiễu 3 (đạo hàm + sai dấu)])
                funcs = [
                    (sp.sin(x), [-sp.sin(x), sp.cos(x), -sp.cos(x)]),
                    (sp.cos(x), [-sp.cos(x), sp.sin(x), -sp.sin(x)]),
                    (sp.exp(x), [-sp.exp(x), x*sp.exp(x-1), -x*sp.exp(x-1)]), # Nhiễu đạo hàm hàm mũ nhầm thành hạ bậc
                    (x**2, [-x**2, 2*x, -2*x]),
                    (x**3, [-x**3, 3*x**2, -3*x**2])
                ]
                F_expr, F_distractors = random.choice(funcs)

                # 2. Random hệ số A và dấu của phép toán
                A = randint(2, 9)
                sign_val = random.choice([1, -1])

                # 3. Tạo biểu thức tính toán
                if sign_val == 1:
                    question_expr = f"{A} + f(x)"
                    correct_ans = A*x + F_expr
                    w1 = A*x + F_distractors[0]
                    w2 = A*x + F_distractors[1]
                    w3 = A*x + F_distractors[2]
                    op_str = "+"
                else:
                    question_expr = f"{A} - f(x)"
                    correct_ans = A*x - F_expr
                    w1 = A*x - F_distractors[0]
                    w2 = A*x - F_distractors[1]
                    w3 = A*x - F_distractors[2]
                    op_str = "-"

                # Định dạng các đáp án (hiển thị trọn vẹn phương trình như hình gốc)
                da = f"$\\int \\left[ {question_expr} \\right] \\mathrm{{d}}x = {clean_latex(correct_ans)} + C$"
                das1 = f"$\\int \\left[ {question_expr} \\right] \\mathrm{{d}}x = {clean_latex(w1)} + C$"
                das2 = f"$\\int \\left[ {question_expr} \\right] \\mathrm{{d}}x = {clean_latex(w2)} + C$"
                das3 = f"$\\int \\left[ {question_expr} \\right] \\mathrm{{d}}x = {clean_latex(w3)} + C$"

                # Câu hỏi
                noidungcauhoi = (
                    f"Cho $\\int f(x) \\mathrm{{d}}x = {clean_latex(F_expr)} + C$. Phát biểu nào sau đây là đúng?"
                )

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (
                    f"Áp dụng tính chất của nguyên hàm (nguyên hàm của một tổng/hiệu), ta có:\\\\ \n"
                    f"$\\int \\left[ {question_expr} \\right] \\mathrm{{d}}x = \\int {A} \\mathrm{{d}}x {op_str} \\int f(x) \\mathrm{{d}}x$.\\\\ \n"
                    f"Biết rằng $\\int {A} \\mathrm{{d}}x = {A}x + C_1$ và theo giả thiết $\\int f(x) \\mathrm{{d}}x = {clean_latex(F_expr)} + C_2$.\\\\ \n"
                    f"Suy ra $\\int \\left[ {question_expr} \\right] \\mathrm{{d}}x = {A}x {op_str} {clean_latex(F_expr)} + C$.\\\\ \n"
                    f"Vậy đáp án đúng là $\\int \\left[ {question_expr} \\right] \\mathrm{{d}}x = {clean_latex(correct_ans)} + C.$"
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

