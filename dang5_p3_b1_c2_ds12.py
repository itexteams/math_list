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


def bt_dang5_p3_b1_c2_ds12(self):
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
        h = random.choice([5, 10]) # Độ dài khoảng
        a1 = random.choice([140, 150, 160]) # Giá trị bắt đầu
        a = [a1 + i*h for i in range(7)] # Các mốc của khoảng (6 nhóm)

        # Random tần số
        # Cố gắng tạo tổng n chẵn để giống form mẫu
        f = [random.randint(15, 30), random.randint(25, 40), random.randint(30, 45), 
             random.randint(40, 55), random.randint(35, 50), random.randint(25, 40)]
        n = sum(f)
        if n % 2 != 0:
            f[0] += 1
            n += 1

        # 2. Xử lý các phép toán thống kê
        cf = [0]
        for x in f:
            cf.append(cf[-1] + x)

        # Tìm nhóm chứa Q1
        for i in range(1, 7):
            if cf[i-1] < n/4 <= cf[i]:
                g1 = i
                break

        # Tìm nhóm chứa Q3
        for i in range(1, 7):
            if cf[i-1] < 3*n/4 <= cf[i]:
                g3 = i
                break

        # Tìm vị trí tứ phân vị mẫu số liệu gốc
        mid = n // 2
        q1_pos_1 = (mid + 1) // 2
        q1_pos_2 = q1_pos_1 + 1 if mid % 2 == 0 else q1_pos_1

        if q1_pos_1 == q1_pos_2:
            q1_goc_str = f"x_{{{q1_pos_1}}}"
            q1_thuoc_nhom_str = f"Do $x_{{{q1_pos_1}}}$ thuộc nhóm $[{a[g1-1]};{a[g1]})$ nên nhóm này chứa $Q_1$."
        else:
            q1_goc_str = f"\\frac{{x_{{{q1_pos_1}}} + x_{{{q1_pos_2}}}}}{{2}}"
            q1_thuoc_nhom_str = f"Do $x_{{{q1_pos_1}}}, x_{{{q1_pos_2}}}$ đều thuộc nhóm $[{a[g1-1]};{a[g1]})$ nên nhóm này chứa $Q_1$."

        upper_start = mid + 1
        q3_pos_1 = upper_start - 1 + (mid + 1) // 2
        q3_pos_2 = q3_pos_1 + 1 if mid % 2 == 0 else q3_pos_1

        if q3_pos_1 == q3_pos_2:
            q3_goc_str = f"x_{{{q3_pos_1}}}"
            q3_thuoc_nhom_str = f"Do $x_{{{q3_pos_1}}}$ thuộc nhóm $[{a[g3-1]};{a[g3]})$ nên nhóm này chứa $Q_3$."
        else:
            q3_goc_str = f"\\frac{{x_{{{q3_pos_1}}} + x_{{{q3_pos_2}}}}}{{2}}"
            q3_thuoc_nhom_str = f"Do $x_{{{q3_pos_1}}}, x_{{{q3_pos_2}}}$ đều thuộc nhóm $[{a[g3-1]};{a[g3]})$ nên nhóm này chứa $Q_3$."

        # Tính giá trị Q1, Q3
        q1_val = a[g1-1] + (n/4 - cf[g1-1]) / f[g1-1] * h
        q3_val = a[g3-1] + (3*n/4 - cf[g3-1]) / f[g3-1] * h
        delta_q = q3_val - q1_val

        # 3. Định dạng chuỗi hiển thị
        def get_sum_f_str_detail(group_idx):
            if group_idx == 1:
                return "0", "0"
            m_list = [f"m_{i}" for i in range(1, group_idx)]
            f_list_str = " + ".join(map(str, f[:group_idx-1]))
            return " + ".join(m_list), f"{f_list_str} = {cf[group_idx-1]}"

        m_str_q1, val_str_q1 = get_sum_f_str_detail(g1)
        if g1 > 1:
            sum_q1_text = f"{m_str_q1} = {val_str_q1}"
        else:
            sum_q1_text = ""

        m_str_q3, val_str_q3 = get_sum_f_str_detail(g3)
        if g3 > 1:
            sum_q3_text = f"{m_str_q3} = {val_str_q3}"
        else:
            sum_q3_text = ""

        c_q1_str = "" if cf[g1-1] == 0 else f"- {cf[g1-1]}"
        c_q3_str = "" if cf[g3-1] == 0 else f"- {cf[g3-1]}"

        bang = f'''\\begin{{center}}
    \\begin{{tabular}}{{|c|c|}}
    \\hline
    \\textbf{{Tốc độ $v$ (km/h)}} & \\textbf{{Số lần}} \\\\
    \\hline
    ${a[0]} \\le v < {a[1]}$ & ${f[0]}$ \\\\
    \\hline
    ${a[1]} \\le v < {a[2]}$ & ${f[1]}$ \\\\
    \\hline
    ${a[2]} \\le v < {a[3]}$ & ${f[2]}$ \\\\
    \\hline
    ${a[3]} \\le v < {a[4]}$ & ${f[3]}$ \\\\
    \\hline
    ${a[4]} \\le v < {a[5]}$ & ${f[4]}$ \\\\
    \\hline
    ${a[5]} \\le v < {a[6]}$ & ${f[5]}$ \\\\
    \\hline
    \\end{{tabular}}
    \\end{{center}}'''

        # Đề bài
        noidungcauhoi = f'''Ghi lại tốc độ bóng trong ${n}$ lần giao bóng của một vận động viên môn quần vợt cho kết quả như bảng bên.
    {bang}
    Khoảng tứ phân vị của mẫu số liệu ghép nhóm bằng bao  nhiêu? (kết quả làm tròn đến hàng phần chục)'''

        # Nội dung lời giải
        loigiai = f'''Cỡ mẫu là $n = {n}$.
    Tứ phân vị thứ nhất $Q_1$ là ${q1_goc_str}$. {q1_thuoc_nhom_str}
    Do đó, $p = {g1}; a_{{{g1}}} = {a[g1-1]}; m_{{{g1}}} = {f[g1-1]}; {sum_q1_text}; a_{{{g1+1}}} - a_{{{g1}}} = {a[g1]} - {a[g1-1]} = {h}$ và ta có
    $$Q_1 = {a[g1-1]} + \\frac{{\\frac{{{n}}}{{4}} {c_q1_str}}}{{{f[g1-1]}}} \\cdot {h} \\approx {format_vn(round(q1_val, 2))}$$
    Tứ phân vị thứ ba $Q_3$ là ${q3_goc_str}$. {q3_thuoc_nhom_str}
    Do đó, $p = {g3}; a_{{{g3}}} = {a[g3-1]}; m_{{{g3}}} = {f[g3-1]}; {sum_q3_text}; a_{{{g3+1}}} - a_{{{g3}}} = {a[g3]} - {a[g3-1]} = {h}$ và ta có
    $$Q_3 = {a[g3-1]} + \\frac{{\\frac{{3 \\cdot {n}}}{{4}} {c_q3_str}}}{{{f[g3-1]}}} \\cdot {h} \\approx {format_vn(round(q3_val, 2))}$$
    Khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_Q = Q_3 - Q_1 \\approx {format_vn(round(delta_q, 1))}$'''

        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(latex(format_vn(round(delta_q, 1))))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

