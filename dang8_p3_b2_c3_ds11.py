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


def bt_dang8_p3_b2_c3_ds11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Thiết lập số liệu sao cho các giá trị nguyên, đẹp và thỏa mãn điều kiện mốt thuộc [10;15)
        # Tổng N = n1 + n2 + x + y + n5 + n6
        # Giữ nguyên cấu trúc các nhóm [0;5), [5;10), [10;15), [15;20), [20;25), [25;30) với độ dài h = 5
        n1 = randint(15, 25)
        n2 = randint(30, 40)
        n5 = randint(35, 45)
        n6 = randint(10, 20)

        # Chọn x, y sao cho x > n2 và x > y để nhóm chứa mốt là [10; 15)
        # M_o = 10 + ((x - n2) / ((x - n2) + (x - y))) * 5
        # Chọn ngẫu nhiên x và y
        while True:
            x_val = randint(45, 65)
            y_val = randint(30, x_val - 1)
            if x_val > n2 and x_val > y_val:
                d1 = x_val - n2
                d2 = x_val - y_val
                # Mo = 10 + 5 * d1 / (d1 + d2)
                Mo_val = Rational(10) + Rational(5 * d1, d1 + d2)
                # Tổng N
                N_val = n1 + n2 + x_val + y_val + n5 + n6
                if N_val % 2 == 0:
                    break

        # Tính vị trí trung vị Me: N/2
        # Cần xác định nhóm chứa trung vị
        # Tần số tích lũy:
        # cf1 = n1
        # cf2 = n1 + n2
        # cf3 = n1 + n2 + x_val
        cf1 = n1
        cf2 = n1 + n2
        cf3 = n1 + n2 + x_val
        cf4 = cf3 + y_val

        # Tính Me
        half_N = Rational(N_val, 2)
        if half_N <= cf2:
            # Nhóm [5; 10)
            u_m = 5
            n_m = n2
            C_prev = cf1
        elif half_N <= cf3:
            # Nhóm [10; 15)
            u_m = 10
            n_m = x_val
            C_prev = cf2
        else:
            # Nhóm [15; 20)
            u_m = 15
            n_m = y_val
            C_prev = cf3

        Me_val = Rational(u_m) + Rational(half_N - C_prev, n_m) * 5

        # Hệ số cho biểu thức P = a_p * Me + b_p * x - c_p * y sao cho P là số nguyên hoặc phân số gọn
        # Chọn hệ số a_p là mẫu số của Me_val để P nguyên
        a_p = Me_val.q
        b_p = 1
        c_p = 2
        P_val = a_p * Me_val + b_p * x_val - c_p * y_val

        kq = int(P_val)
        kq_str = str(kq)

        # Biểu diễn LaTeX của Mo
        Mo_latex = latex(Mo_val)
        Me_latex = latex(Me_val)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một trung tâm dữ liệu đo đạc thời gian xử lý (đơn vị: giây) của $N = %s$ yêu cầu tính toán từ các thiết bị IoT trong giờ cao điểm. Dữ liệu thu được được tổng hợp thành bảng tần số ghép nhóm dưới đây, trong đó số lượng yêu cầu ở hai nhóm $[10;15)$ và $[15;20)$ chưa được ghi nhận đầy đủ và được ký hiệu lần lượt là $x$ và $y$ ($x, y \\in \\mathbb{N}^*$).
    \\begin{center}
    \\begin{tabular}{|c|c|c|c|c|c|c|}
    \\hline
    \\textbf{Thời gian (giây)} & $[0;5)$ & $[5;10)$ & $[10;15)$ & $[15;20)$ & $[20;25)$ & $[25;30)$ \\\\
    \\hline
    \\textbf{Số yêu cầu} & $%s$ & $%s$ & $x$ & $y$ & $%s$ & $%s$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}
    Biết rằng mốt của mẫu số liệu ghép nhóm thuộc nhóm $[10;15)$ và có giá trị bằng $M_o = %s$ giây. Gọi $M_e$ là trung vị của mẫu số liệu ghép nhóm trên. Giá trị của biểu thức $P = %s M_e + x - 2y$ bằng bao nhiêu?'''
                         % (str(N_val),
                            str(n1), str(n2), str(n5), str(n6),
                            Mo_latex,
                            str(a_p)
                            ))

        # Nội dung lời giải
        d1_val = x_val - n2
        d2_val = x_val - y_val
        loigiai = ('''Tổng số yêu cầu là $N = %s$, do đó ta có: \\\\
    $%s + %s + x + y + %s + %s = %s \\Leftrightarrow x + y = %s$. (1) \\\\
    Nhóm chứa mốt là nhóm $[10;15)$, có tần số $x$. Nhóm trước đó là $[5;10)$ có tần số là $%s$, nhóm tiếp sau là $[15;20)$ có tần số là $y$. \\\\
    Độ dài của mỗi nhóm là $h = 15 - 10 = 5$. \\\\
    Công thức tính mốt của mẫu số liệu ghép nhóm là: \\\\
    $M_o = 10 + \\frac{x - %s}{(x - %s) + (x - y)} \\cdot 5$. \\\\
    Theo giả thiết, ta có: \\\\
    $10 + \\frac{x - %s}{2x - y - %s} \\cdot 5 = %s \\Leftrightarrow \\frac{x - %s}{2x - y - %s} \\cdot 5 = %s - 10 = %s$ \\\\
    $\\Leftrightarrow %s(x - %s) = %s(2x - y - %s)$. (2) \\\\
    Từ (1) và (2), giải hệ phương trình ta tìm được: \\\\
    $\\begin{cases} x = %s \\\\ y = %s \\end{cases}$ \\\\
    Ta tìm trung vị $M_e$: \\\\
    Cỡ mẫu $N = %s$, do đó $\\frac{N}{2} = %s$. \\\\
    Tần số tích lũy của các nhóm: \\\\
    - Nhóm $[0;5)$: $%s$ \\\\
    - Nhóm $[5;10)$: $%s + %s = %s$ \\\\
    - Nhóm $[10;15)$: $%s + %s = %s$ \\\\
    Do $%s < %s \\le %s$ nên trung vị $M_e$ thuộc nhóm $[10;15)$. \\\\
    Ta có: \\\\
    $M_e = 10 + \\frac{%s - %s}{%s} \\cdot 5 = %s$. \\\\
    Thay vào biểu thức $P$, ta được: \\\\
    $P = %s \\cdot \\left(%s\\right) + %s - 2 \\cdot %s = %s$.'''
                   % (str(N_val),
                      str(n1), str(n2), str(n5), str(n6), str(N_val), str(x_val + y_val),
                      str(n2),
                      str(n2), str(n2),
                      str(n2), str(n2), Mo_latex, str(n2), str(n2), Mo_latex, latex(Mo_val - 10),
                      str((Mo_val - 10).q * 5), str(n2), str((Mo_val - 10).p), str(n2),
                      str(x_val), str(y_val),
                      str(N_val), str(half_N),
                      str(n1),
                      str(n1), str(n2), str(cf2),
                      str(cf2), str(x_val), str(cf3),
                      str(cf2), str(half_N), str(cf3),
                      str(half_N), str(cf2), str(x_val), Me_latex,
                      str(a_p), Me_latex, str(x_val), str(y_val), str(kq_str)
                      ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

