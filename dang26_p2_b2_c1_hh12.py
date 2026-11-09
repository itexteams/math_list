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


def bt_dang26_p2_b2_c1_hh12(self):
    # Hàm biểu diễn vectơ theo hệ ba vectơ đơn vị i, j, k
    def format_ijk(c1, c2, c3):
        res = ""
        # Thành phần i
        if c1 == 1:
            res += "\\vec{i}"
        elif c1 == -1:
            res += "-\\vec{i}"
        elif c1 != 0:
            res += "%s\\vec{i}" % c1
    
        # Thành phần j
        if c2 == 1:
            res += "+\\vec{j}" if res else "\\vec{j}"
        elif c2 == -1:
            res += "-\\vec{j}"
        elif c2 > 0:
            res += "+%s\\vec{j}" % c2 if res else "%s\\vec{j}" % c2
        elif c2 < 0:
            res += "%s\\vec{j}" % c2
    
        # Thành phần k
        if c3 == 1:
            res += "+\\vec{k}" if res else "\\vec{k}"
        elif c3 == -1:
            res += "-\\vec{k}"
        elif c3 > 0:
            res += "+%s\\vec{k}" % c3 if res else "%s\\vec{k}" % c3
        elif c3 < 0:
            res += "%s\\vec{k}" % c3
    
        return res
    
    
    # Hàm biểu diễn biểu thức tuyến tính dạng ax + by
    def format_linear_xy(a_coef, b_coef):
        terms = []
        if a_coef == 1:
            terms.append("x")
        elif a_coef == -1:
            terms.append("-x")
        elif a_coef != 0:
            terms.append("%sx" % a_coef)
    
        if b_coef == 1:
            terms.append("+ y" if terms else "y")
        elif b_coef == -1:
            terms.append("- y" if terms else "-y")
        elif b_coef > 0:
            terms.append("+ %sy" % b_coef if terms else "%sy" % b_coef)
        elif b_coef < 0:
            terms.append("- %sy" % (-b_coef) if terms else "-%sy" % (-b_coef))
    
        return " ".join(terms)
    
    
    # Sinh ngẫu nhiên dữ liệu bài toán
    while True:
        # Chọn trước nghiệm x0, y0 nguyên đẹp cho hệ phương trình ở khẳng định c
        x0 = random.randint(1, 3)
        y0 = random.randint(-2, 2)
    
        # Chọn các hệ số ma trận của hệ: c11*x + c12*y = a1, c21*x + c22*y = a2
        c11 = random.choice([2, 3])
        c12 = random.choice([-2, -1, 1])
        c21 = random.choice([1, 2])
        c22 = random.choice([-4, -3, 3, 4])
    
        # Định thức hệ số
        det_c = c11 * c22 - c12 * c21
        if det_c == 0:
            continue
    
        # Tọa độ của vectơ a
        a1 = c11 * x0 + c12 * y0
        a2 = c21 * x0 + c22 * y0
        a3 = random.choice([-5, -4, -3, 3, 4, 5])
    
        # Điểm A(xa, ya, za)
        xa = random.randint(-3, 3)
        ya = random.randint(-3, 3)
        za = random.randint(-3, 3)
    
        if a1 != 0 and a2 != 0:
            break
    
    # Chuỗi biểu diễn vectơ a theo i, j, k
    str_vec_a = format_ijk(a1, a2, a3)
    
    # Biểu thức tọa độ thứ nhất và thứ hai của vectơ b
    expr_b1 = format_linear_xy(c11, c12)
    expr_b2 = format_linear_xy(c21, c22)
    
    # Tổng x + y
    sum_xy = x0 + y0
    sum_xy_s = sum_xy + random.choice([-2, -1, 1, 2])
    
    # Điểm B khi AB = a <=> B = A + a
    xb = xa + a1
    yb = ya + a2
    zb = za + a3
    
    # Tọa độ sai của B (nhầm sang B = A - a hoặc nhầm dấu)
    xb_s = xa - a1
    yb_s = ya - a2
    zb_s = za - a3
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian $Oxyz$, cho vectơ $\\vec{a} = %s$."""
        % (str_vec_a)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Tọa độ của vectơ a là a = (a1; a2; a3)[cite: 22]
    nb_da_1_d = "\\True Tọa độ của vectơ $\\vec{a}$ là $\\vec{a} = (%s;%s;%s)$" % (
        a1,
        a2,
        a3,
    )
    nb_da_1_s = "Tọa độ của vectơ $\\vec{a}$ là $\\vec{a} = (%s;%s;%s)$" % (
        a2,
        a1,
        a3,
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Theo định nghĩa tọa độ của vectơ trong không gian đối với hệ trục toạ độ $Oxyz$, nếu $\\vec{a} = %s\\vec{i} + (%s)\\vec{j} + (%s)\\vec{k}$ thì tọa độ của vectơ $\\vec{a}$ là $\\vec{a} = (%s;%s;%s)$."""
        % (a1, a2, a3, a1, a2, a3)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Nếu vectơ OA = a thì điểm A có tọa độ là A(a1; a2; a3)[cite: 22]
    th_da_1_d = (
        "\\True Nếu vectơ $\\vec{OA} = \\vec{a}$ thì điểm $A$ có tọa độ là $A(%s;%s;%s)$"
        % (a1, a2, a3)
    )
    th_da_1_s = (
        "Nếu vectơ $\\vec{OA} = \\vec{a}$ thì điểm $A$ có tọa độ là $A(%s;%s;%s)$"
        % (-a1, -a2, -a3)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Theo định nghĩa tọa độ điểm trong không gian: Tọa độ của điểm $A$ chính là tọa độ của vectơ $\\vec{OA}$. \\\\ Vì $\\vec{OA} = \\vec{a} = (%s;%s;%s)$ nên tọa độ của điểm $A$ là $A(%s;%s;%s)$."""
        % (a1, a2, a3, a1, a2, a3)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Biết a = b và b = (c11*x + c12*y; c21*x + c22*y; a3). Khi đó x + y = sum_xy[cite: 22]
    vd_da_1_d = (
        "\\True Biết $\\vec{a} = \\vec{b}$ và $\\vec{b} = (%s; %s; %s)$. Khi đó $x + y = %s$"
        % (expr_b1, expr_b2, a3, sum_xy)
    )
    vd_da_1_s = (
        "Biết $\\vec{a} = \\vec{b}$ và $\\vec{b} = (%s; %s; %s)$. Khi đó $x + y = %s$"
        % (expr_b1, expr_b2, a3, sum_xy_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Hai vectơ bằng nhau khi và chỉ khi các tọa độ tương ứng bằng nhau, do đó: \\\\ $\\vec{a} = \\vec{b} \\Leftrightarrow \\begin{cases} %s = %s \\\\ %s = %s \\\\ %s = %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$ \\\\ Suy ra $x + y = %s + (%s) = %s$."""
        % (
            expr_b1,
            a1,
            expr_b2,
            a2,
            a3,
            a3,
            x0,
            y0,
            x0,
            y0,
            sum_xy,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Biết AB = a và A(xa; ya; za) thì điểm B có tọa độ là B(xb; yb; zb)[cite: 22]
    vdc_da_1_d = (
        "\\True Biết $\\vec{AB} = \\vec{a}$ và $A(%s;%s;%s)$ thì điểm $B$ có tọa độ là $B(%s;%s;%s)$"
        % (xa, ya, za, xb, yb, zb)
    )
    vdc_da_1_s = (
        "Biết $\\vec{AB} = \\vec{a}$ và $A(%s;%s;%s)$ thì điểm $B$ có tọa độ là $B(%s;%s;%s)$"
        % (xa, ya, za, xb_s, yb_s, zb_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Gọi tọa độ điểm $B$ là $B(x_B; y_B; z_B)$. \\\\ Ta có $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (x_B - (%s); y_B - (%s); z_B - (%s))$. \\\\ Vì $\\vec{AB} = \\vec{a} = (%s;%s;%s)$ nên ta có hệ phương trình: \\\\ $\\begin{cases} x_B - (%s) = %s \\\\ y_B - (%s) = %s \\\\ z_B - (%s) = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_B = %s + (%s) = %s \\\\ y_B = %s + (%s) = %s \\\\ z_B = %s + (%s) = %s \\end{cases}$ \\\\ Vậy điểm $B$ có tọa độ là $B(%s;%s;%s)$."""
        % (
            xa,
            ya,
            za,
            a1,
            a2,
            a3,
            xa,
            a1,
            ya,
            a2,
            za,
            a3,
            xa,
            a1,
            xb,
            ya,
            a2,
            yb,
            za,
            a3,
            zb,
            xb,
            yb,
            zb,
        )
    )
    
    list_vdc_2 = [loigiai_vdc_1]
    
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    
    def count_true_answers(answers):
        return sum("\\True" in ans for ans in answers)
    
    
    # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
    
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
    
        if 1 <= true_count <= 3:
            break
    
    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = (
        "\\begin{minipage}{\\textwidth} \n"
        "\\begin{ex}\n"
        + str(noidungcauhoi)
        + "\n"
        "\\choiceTFn \n"
        "{" + str(shuffled_answers_nb[0]) + "}\n"
        "{" + str(shuffled_answers_th[0]) + "}\n"
        "{" + str(shuffled_answers_vd[0]) + "}\n"
        "{" + str(shuffled_answers_vdc[0]) + "}\n"
        "\\loigiai{ \n"
        "\\begin{enumEX}[a)]{1} \n"
        "\\item " + str(shuffled_solutions_nb[0]) + "\n"
        "\\item " + str(shuffled_solutions_th[0]) + "\n"
        "\\item " + str(shuffled_solutions_vd[0]) + "\n"
        "\\item " + str(shuffled_solutions_vdc[0]) + "\n"
        "\\end{enumEX}} \n"
        "\\end{ex}\n \\end{minipage}\n\n")
    return content
    