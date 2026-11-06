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


def bt_dang7_p3_b1_c2_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    def format_vn(num):
        """Hàm định dạng số thực sang chuẩn Việt Nam (dấu phẩy)"""
        num = round(num, 4)
        if num == int(num):
            return str(int(num))
        return str(num).replace('.', ',')

    if dang=='1':
        # 1. Sinh ngẫu nhiên số liệu
        h = random.randint(2, 4) # Độ dài khoảng
        a1 = random.choice([5, 6, 8, 10]) # Giá trị bắt đầu
        a = [a1 + i*h for i in range(6)] # Các mốc của khoảng

        # Random tần số
        f = [random.randint(3, 8) for _ in range(5)]
        n = sum(f)

        # 2. Xử lý các phép toán thống kê
        cf = [0]
        for x in f:
            cf.append(cf[-1] + x)

        # Tìm nhóm chứa Q1
        for i in range(1, 6):
            if cf[i-1] < n/4 <= cf[i]:
                g1 = i
                break

        # Tìm nhóm chứa Q3
        for i in range(1, 6):
            if cf[i-1] < 3*n/4 <= cf[i]:
                g3 = i
                break

        # Tìm vị trí tứ phân vị mẫu số liệu gốc (bắt chính xác theo luật trung vị)
        mid = n // 2
        if mid % 2 != 0:
            q1_pos = (mid + 1) // 2
            q1_goc_str = f"x_{{{q1_pos}}}"
        else:
            q1_goc_str = f"\\frac{{1}}{{2}}(x_{{{mid // 2}}} + x_{{{mid // 2 + 1}}})"

        upper_start = mid + 2 if n % 2 != 0 else mid + 1

        if mid % 2 != 0:
            q3_pos = upper_start - 1 + (mid + 1) // 2
            q3_goc_str = f"x_{{{q3_pos}}}"
        else:
            p3, p4 = upper_start - 1 + mid // 2, upper_start - 1 + mid // 2 + 1
            q3_goc_str = f"\\frac{{1}}{{2}}(x_{{{p3}}} + x_{{{p4}}})"

        # Tính giá trị Q1, Q3
        q1_val = a[g1-1] + (n/4 - cf[g1-1]) / f[g1-1] * h
        q3_val = a[g3-1] + (3*n/4 - cf[g3-1]) / f[g3-1] * h
        delta_q = q3_val - q1_val

        # 3. Định dạng chuỗi hiển thị
        # Chuỗi hiển thị các đoạn x_i thuộc khoảng
        ta_co_arr = []
        for i in range(5):
            start = cf[i] + 1
            end = cf[i+1]
            if start == end:
                ta_co_arr.append(f"x_{{{start}}} \\in [{a[i]};{a[i+1]})")
            else:
                ta_co_arr.append(f"x_{{{start}}};...;x_{{{end}}} \\in [{a[i]};{a[i+1]})")
        ta_co_str = "; ".join(ta_co_arr)

        # Chuỗi tổng tần số hiển thị trong công thức
        def get_sum_f_str(group_idx):
            if group_idx == 1:
                return "0"
            elif group_idx == 2:
                return str(f[0])
            else:
                return "(" + "+".join(map(str, f[:group_idx-1])) + ")"

        sum_q1_str = get_sum_f_str(g1)
        c_q1_str = "" if sum_q1_str == "0" else f"- {sum_q1_str}"

        sum_q3_str = get_sum_f_str(g3)
        c_q3_str = "" if sum_q3_str == "0" else f"- {sum_q3_str}"

        bang = f'''\\begin{{center}}
    \\begin{{tabular}}{{|c|c|c|c|c|c|}}
    \\hline
    \\begin{{tabular}}{{c}} Thời gian giải \\\\ rubik (giây) \\end{{tabular}} & $[{a[0]};{a[1]})$ & $[{a[1]};{a[2]})$ & $[{a[2]};{a[3]})$ & $[{a[3]};{a[4]})$ & $[{a[4]};{a[5]})$ \\\\
    \\hline
    Số lần & ${f[0]}$ & ${f[1]}$ & ${f[2]}$ & ${f[3]}$ & ${f[4]}$ \\\\
    \\hline
    \\end{{tabular}}
    \\end{{center}}'''
        # Đề bài
        noidungcauhoi = f'''Dũng là học sinh rất giỏi chơi rubik, bạn có thể giải nhiều loại khối rubik khác nhau. Trong một lần tập luyện giải khối rubik $3 \\times 3$, bạn Dũng đã tự thống kê lại thời gian giải rubik trong ${n}$ lần giải liên tiếp ở bảng sau:
    {bang}
    Khoảng tứ phân vị của mẫu số liệu ghép nhóm bằng bao nhiêu (kết quả làm tròn đến hàng phần chục)'''

        # Nội dung lời giải
        loigiai = f'''Cỡ mẫu $n = {n}$
    Gọi $x_1; x_2; ...; x_{{{n}}}$ là mẫu số liệu gốc về thời gian giải rubik trong ${n}$ lần của bạn Dũng được xếp theo thứ tự không giảm.
    Ta có: ${ta_co_str}$
    Tứ phân vị thứ nhất của mẫu số liệu gốc là ${q1_goc_str} \\in [{a[g1-1]}; {a[g1]})$. Do đó, tứ phân vị thứ nhất của mẫu số liệu ghép nhóm là: 
    $$Q_1 = {a[g1-1]} + \\frac{{\\frac{{{n}}}{{4}} {c_q1_str}}}{{{f[g1-1]}}}({a[g1]} - {a[g1-1]}) = {format_vn(round(q1_val, 1))}$$
    Tứ phân vị thứ ba của mẫu số liệu gốc là ${q3_goc_str} \\in [{a[g3-1]}; {a[g3]})$. Do đó, tứ phân vị thứ ba của mẫu số liệu ghép nhóm là: 
    $$Q_3 = {a[g3-1]} + \\frac{{\\frac{{3 \\cdot {n}}}{{4}} {c_q3_str}}}{{{f[g3-1]}}}({a[g3]} - {a[g3-1]}) = {format_vn(round(q3_val, 1))}$$
    Khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_Q = Q_3 - Q_1 = {format_vn(round(delta_q, 1))}$'''

        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(latex(format_vn(round(delta_q, 1))))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

