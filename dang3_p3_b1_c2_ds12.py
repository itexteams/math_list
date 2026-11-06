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


def bt_dang3_p3_b1_c2_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    def format_num(val):
        # Hàm hỗ trợ định dạng số thập phân, thay dấu chấm bằng dấu phẩy theo chuẩn Toán VN
        s = f"{round(val, 1):g}"
        return s.replace('.', ',')

    if dang=='1':
        # B3 - Random bài toán: 
        # Random độ dài khoảng h (thường là 5, 10, 20 phút)
        h = random.choice([5, 10, 20])
        a1, a2, a3, a4, a5 = 0, h, 2*h, 3*h, 4*h

        # Thiết lập tần số m1, m2, m3, m4 sao cho Q1 rơi vào nhóm 2 và Q3 rơi vào nhóm 3 giống bài mẫu
        # Cố ý chọn n không chia hết cho 4 (vd: 38, 42, 46) để vị trí Q1, Q3 là số nguyên sau khi làm tròn lên
        n_target = random.choice([38, 42, 46, 54, 58])
        m1 = random.randint(3, 7)
        m2 = random.randint(12, 16)
        m3 = random.randint(12, 16)
        m4 = n_target - (m1 + m2 + m3)
        if m4 < 3: 
            m4 = random.randint(5, 10) # Đảm bảo m4 không bị âm hoặc quá nhỏ

        n = m1 + m2 + m3 + m4

        # Tính toán Q1
        q1_val_exact = n / 4
        q1_idx = math.ceil(q1_val_exact) # Vị trí x_{q1_idx}

        cf1 = m1
        cf2 = m1 + m2
        cf3 = m1 + m2 + m3

        # Xác định nhóm chứa Q1 (Theo cấu trúc random, chắc chắn rơi vào nhóm 2)
        L1 = a2
        cf_prev1 = m1
        f_q1 = m2
        Q1 = L1 + (q1_val_exact - cf_prev1) / f_q1 * h

        # Tính toán Q3
        q3_val_exact = 3 * n / 4
        q3_idx = math.ceil(q3_val_exact) # Vị trí x_{q3_idx}

        # Xác định nhóm chứa Q3 (Theo cấu trúc random, chắc chắn rơi vào nhóm 3)
        L3 = a3
        cf_prev3 = cf2
        f_q3 = m3
        Q3 = L3 + (q3_val_exact - cf_prev3) / f_q3 * h

        # Khoảng tứ phân vị
        delta_Q = Q3 - Q1

        noidungcauhoi = f"""Thời gian chờ khám bệnh của các bệnh nhân tại phòng khám $X$ được cho trong bảng sau:
    \\begin{{center}}
    \\begin{{tabular}}{{|c|c|c|c|c|}}
    \\hline
    Thời gian (phút) & $[{a1};{a2})$ & $[{a2};{a3})$ & $[{a3};{a4})$ & $[{a4};{a5})$ \\\\
    \\hline
    Số bệnh nhân & ${m1}$ & ${m2}$ & ${m3}$ & ${m4}$ \\\\
    \\hline
    \\end{{tabular}}
    \\end{{center}}
    Khoảng tứ phân vị của mẫu số liệu ghép nhóm này bằng bao nhiêu? (kết quả làm tròn đến hàng phần mười)."""

        # Quyết định dấu = hay \approx cho hiển thị
        sign_q1 = "=" if abs(Q1 - round(Q1, 2)) < 1e-9 else "\\approx"
        sign_q3 = "=" if abs(Q3 - round(Q3, 2)) < 1e-9 else "\\approx"

        # Nội dung lời giải
        loigiai = f"""Cỡ mẫu là $n = {m1} + {m2} + {m3} + {m4} = {n}$. Gọi $x_1, \\dots, x_{{{n}}}$ là thời gian chờ khám bệnh của ${n}$ bệnh nhân này và giả sử rằng dãy số liệu gốc này đã được sắp xếp theo thứ tự tăng dần. Tứ phân vị thứ nhất của mẫu số liệu gốc là $x_{{{q1_idx}}}$ nên nhóm chứa tứ phân vị thứ nhất là nhóm $[{L1};{L1+h})$ và ta có:
    $$Q_1 = {L1} + \\left[ \\frac{{\\frac{{{n}}}{{4}} - {cf_prev1}}}{{{f_q1}}} \\right] .{h} {sign_q1} {format_num(Q1)}.$$

    Tứ phân vị thứ ba của mẫu số liệu gốc là $x_{{{q3_idx}}}$ nên nhóm chứa tứ phân vị thứ ba là nhóm $[{L3};{L3+h})$ và ta có:
    $$Q_3 = {L3} + \\left[ \\frac{{\\frac{{3 \\cdot {n}}}{{4}} - {cf_prev3}}}{{{f_q3}}} \\right] .{h} {sign_q3} {format_num(Q3)}.$$

    Vậy khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_Q = Q_3 - Q_1 \\approx {format_num(Q3)} - {format_num(Q1)} = {format_num(delta_Q)}.$"""

        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(format_num(delta_Q))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

