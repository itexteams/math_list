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


def bt_dang71_p1_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp đảm bảo sinh số liệu hợp lệ và 4 đáp án hoàn toàn phân biệt
                while True:
                    # 1. Sinh ngẫu nhiên hệ số và số mũ cho f'(x) và g'(x)
                    a = randint(1, 5)
                    n = randint(1, 4)
                    b = randint(1, 5)
                    m = randint(1, 4)

                    # Đảm bảo 2 số mũ khác nhau để biểu thức không bị rút gọn thành 1 số hạng duy nhất
                    if n == m:
                        continue

                    f_prime = a * x**n
                    g_prime = b * x**m

                    # 2. Chọn ngẫu nhiên yêu cầu đề bài: Tính (f(x) + g(x))' hoặc (f(x) - g(x))'
                    op = random.choice(['+', '-'])

                    if op == '+':
                        ans_correct = f_prime + g_prime
                        ans_w2 = f_prime - g_prime
                        req_func = "f(x) + g(x)"
                        loigiai_op = "+"
                    else:
                        ans_correct = f_prime - g_prime
                        ans_w2 = f_prime + g_prime
                        req_func = "f(x) - g(x)"
                        loigiai_op = "-"

                    # 3. Tạo các đáp án nhiễu
                    # Nhiễu 1: Học sinh đạo hàm biểu thức thêm 1 lần nữa (tính đạo hàm cấp 2)
                    ans_w1 = diff(ans_correct, x)

                    # Nhiễu 3: Học sinh nhầm sang quy tắc nhân 2 đạo hàm
                    ans_w3 = f_prime * g_prime

                    # Kiểm tra đảm bảo 4 đáp án không bị trùng lặp
                    options = {ans_correct, ans_w1, ans_w2, ans_w3}
                    if len(options) == 4:
                        break

                # 4. Chuyển đổi sang chuỗi hiển thị LaTeX (SymPy tự động chuẩn hóa dấu + -)
                da = f"${latex(ans_correct)}$"
                das1 = f"${latex(ans_w1)}$"
                das2 = f"${latex(ans_w2)}$"
                das3 = f"${latex(ans_w3)}$"

                # Câu hỏi
                noidungcauhoi = (
                    f"Cho các hàm số $y=f(x)$ và $y=g(x)$ có đạo hàm trên tập số thực $\\mathbb{{R}}$ thỏa mãn $f'(x)={latex(f_prime)}$ và $g'(x)={latex(g_prime)}$. "
                    f"Đạo hàm của hàm số $y={req_func}$ là"
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
                    f"Sử dụng quy tắc đạo hàm của tổng/hiệu hai hàm số, ta có:\\\\ \n"
                    f"$\\left( {req_func} \\right)' = f'(x) {loigiai_op} g'(x)$.\\\\ \n"
                    f"Thay $f'(x) = {latex(f_prime)}$ và $g'(x) = {latex(g_prime)}$ vào biểu thức trên, ta được:\\\\ \n"
                    f"$y' = {latex(ans_correct)}$.\\\\ \n"
                    f"Vậy đạo hàm của hàm số đã cho là $y' = {latex(ans_correct)}$."
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

