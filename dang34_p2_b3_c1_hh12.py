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


def bt_dang34_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba vectơ a, b, c không đồng phẳng[cite: 20]
    while True:
        # a có cao độ bằng 0 như đề gốc[cite: 20]
        a1 = random.choice([1, 2, -1, -2])
        a2 = random.choice([1, 2, -1, -2])
        a3 = 0
    
        # b[cite: 20]
        b1 = random.choice([1, 2, 3, -1, -2])
        b2 = random.choice([-2, -1, 1, 2])
        b3 = random.choice([1, 2, -1, -2])
    
        # c[cite: 20]
        c1 = random.choice([-3, -2, 2, 3])
        c2 = random.choice([1, 2, -1, -2])
        c3 = random.choice([2, 3, -2, -3])
    
        # Định thức để kiểm tra ba vectơ không đồng phẳng: det([a, b, c]) != 0
        det_mat = a1 * (b2 * c3 - b3 * c2) - a2 * (b1 * c3 - b3 * c1) + a3 * (b1 * c2 - b2 * c1)
    
        if det_mat != 0:
            # Chọn trước các hệ số k0, m0, p0 nguyên đẹp cho khẳng định d[cite: 20]
            k0 = random.randint(-3, 3)
            m0 = random.randint(1, 4)
            p0 = random.randint(1, 4)
    
            if k0 == 0:
                k0 = 2
    
            # Vectơ v = k0*a + m0*b + p0*c[cite: 20]
            v1 = k0 * a1 + m0 * b1 + p0 * c1
            v2 = k0 * a2 + m0 * b2 + p0 * c2
            v3 = k0 * a3 + m0 * b3 + p0 * c3
    
            # Tính toán vectơ b - 2c cho khẳng định c[cite: 20]
            u_bc1 = b1 - 2 * c1
            u_bc2 = b2 - 2 * c2
            u_bc3 = b3 - 2 * c3
    
            dot_a_ubc = a1 * u_bc1 + a2 * u_bc2 + a3 * u_bc3
            len_a_sq = a1**2 + a2**2 + a3**2
            len_ubc_sq = u_bc1**2 + u_bc2**2 + u_bc3**2
    
            if dot_a_ubc != 0 and len_a_sq > 0 and len_ubc_sq > 0:
                break
    
    # 1. Tọa độ của vectơ a + b = (a1 + b1; a2 + b2; a3 + b3)[cite: 20]
    sum_ab1 = a1 + b1
    sum_ab2 = a2 + b2
    sum_ab3 = a3 + b3
    
    # Tọa độ sai của a + b[cite: 20]
    sum_ab1_s = sum_ab1
    sum_ab2_s = sum_ab2 + random.choice([-1, 1])
    sum_ab3_s = sum_ab3
    
    # 2. Giả sử a + x = 2b - c => x = 2b - c - a[cite: 20]
    x1 = 2 * b1 - c1 - a1
    x2 = 2 * b2 - c2 - a2
    x3 = 2 * b3 - c3 - a3
    
    # Tọa độ sai của x (nhầm dấu phép trừ như đề gốc)[cite: 20]
    x1_s = x1
    x2_s = -x2 if x2 != 0 else 3
    x3_s = x3
    
    # 3. cos \varphi với \varphi là góc giữa hai vectơ a và b - 2c[cite: 20]
    cos_phi_sym = Rational(dot_a_ubc, 1) / (sp.sqrt(len_a_sq) * sp.sqrt(len_ubc_sq))
    str_cos_phi_true = latex(cos_phi_sym)
    
    # Giá trị sai cho cos \varphi[cite: 20]
    cos_phi_sym_s = Rational(abs(dot_a_ubc) + 1, 1) / (sp.sqrt(len_a_sq) * sp.sqrt(len_ubc_sq))
    str_cos_phi_false = latex(cos_phi_sym_s)
    if str_cos_phi_false == str_cos_phi_true:
        str_cos_phi_false = "\\frac{5}{14}"
    
    # 4. v = k*a + m*b + p*c => k + m + p[cite: 20]
    sum_kmp = k0 + m0 + p0
    sum_kmp_s = sum_kmp + random.choice([-2, -1, 1, 2])
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = """Trong không gian với hệ toạ độ $Oxyz$ cho ba véc tơ $\\vec{a}(%s;%s;%s), \\vec{b}(%s;%s;%s), \\vec{c}(%s;%s;%s)$.""" % (a1, a2, a3, b1, b2, b3, c1, c2, c3)
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Toạ độ của véc tơ a + b[cite: 20]
    nb_da_1_d = "\\True Toạ độ của véc tơ $\\vec{a} + \\vec{b}$ là $(%s;%s;%s)$" % (sum_ab1, sum_ab2, sum_ab3)
    nb_da_1_s = "Toạ độ của véc tơ $\\vec{a} + \\vec{b}$ là $(%s;%s;%s)$" % (sum_ab1_s, sum_ab2_s, sum_ab3_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = """Ta có toạ độ của véc tơ $\\vec{a} + \\vec{b}$ là: \\\\ $\\vec{a} + \\vec{b} = (%s + (%s); %s + (%s); %s + (%s)) = (%s;%s;%s)$.""" % (a1, b1, a2, b2, a3, b3, sum_ab1, sum_ab2, sum_ab3)
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Giả sử a + x = 2b - c. Toạ độ của x[cite: 20]
    th_da_1_d = "\\True Giả sử $\\vec{a} + \\vec{x} = 2\\vec{b} - \\vec{c}$. Toạ độ của $\\vec{x}$ là $(%s;%s;%s)$" % (x1, x2, x3)
    th_da_1_s = "Giả sử $\\vec{a} + \\vec{x} = 2\\vec{b} - \\vec{c}$. Toạ độ của $\\vec{x}$ là $(%s;%s;%s)$" % (x1_s, x2_s, x3_s)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = """Từ giả thiết $\\vec{a} + \\vec{x} = 2\\vec{b} - \\vec{c} \\Leftrightarrow \\vec{x} = 2\\vec{b} - \\vec{c} - \\vec{a}$. \\\\ Ta có: \\\\ $2\\vec{b} = (2 \\cdot (%s); 2 \\cdot (%s); 2 \\cdot (%s)) = (%s;%s;%s)$. \\\\ Do đó toạ độ của véc tơ $\\vec{x}$ là: \\\\ $\\vec{x} = (%s - (%s) - (%s); %s - (%s) - (%s); %s - (%s) - (%s)) = (%s;%s;%s)$.""" % (
        b1, b2, b3, 2 * b1, 2 * b2, 2 * b3,
        2 * b1, c1, a1,
        2 * b2, c2, a2,
        2 * b3, c3, a3,
        x1, x2, x3
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: cos \varphi của góc giữa a và b - 2c[cite: 20]
    vd_da_1_d = "\\True Gọi $\\varphi$ là góc giữa hai véc tơ $\\vec{a}$ và $\\vec{b} - 2\\vec{c}$. Khi đó $\\cos\\varphi = %s$" % (str_cos_phi_true)
    vd_da_1_s = "Gọi $\\varphi$ là góc giữa hai véc tơ $\\vec{a}$ và $\\vec{b} - 2\\vec{c}$. Khi đó $\\cos\\varphi = %s$" % (str_cos_phi_false)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = """Ta có toạ độ của véc tơ $\\vec{b} - 2\\vec{c}$ là: \\\\ $\\vec{b} - 2\\vec{c} = (%s - 2 \\cdot (%s); %s - 2 \\cdot (%s); %s - 2 \\cdot (%s)) = (%s;%s;%s)$. \\\\ Độ dài của các véc tơ là: \\\\ $|\\vec{a}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $|\\vec{b} - 2\\vec{c}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Tích vô hướng của hai véc tơ: \\\\ $\\vec{a} \\cdot (\\vec{b} - 2\\vec{c}) = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Khi đó cosin của góc $\\varphi$ giữa hai véc tơ là: \\\\ $\\cos\\varphi = \\frac{\\vec{a} \\cdot (\\vec{b} - 2\\vec{c})}{|\\vec{a}| \\cdot |\\vec{b} - 2\\vec{c}|} = \\frac{%s}{\\sqrt{%s} \\cdot \\sqrt{%s}} = %s$.""" % (
        b1, c1, b2, c2, b3, c3, u_bc1, u_bc2, u_bc3,
        a1, a2, a3, len_a_sq,
        u_bc1, u_bc2, u_bc3, len_ubc_sq,
        a1, u_bc1, a2, u_bc2, a3, u_bc3, dot_a_ubc,
        dot_a_ubc, len_a_sq, len_ubc_sq, str_cos_phi_true
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Giả sử v = ka + mb + pc. Khi đó k + m + p[cite: 20]
    vdc_da_1_d = "\\True Giả sử $\\vec{v} = (%s;%s;%s)$ và $\\vec{v} = k\\vec{a} + m\\vec{b} + p\\vec{c}$. Khi đó $k + m + p = %s$" % (v1, v2, v3, sum_kmp)
    vdc_da_1_s = "Giả sử $\\vec{v} = (%s;%s;%s)$ và $\\vec{v} = k\\vec{a} + m\\vec{b} + p\\vec{c}$. Khi đó $k + m + p = %s$" % (v1, v2, v3, sum_kmp_s)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = """Ta có: \\\\ $k\\vec{a} + m\\vec{b} + p\\vec{c} = (k \\cdot (%s) + m \\cdot (%s) + p \\cdot (%s); k \\cdot (%s) + m \\cdot (%s) + p \\cdot (%s); k \\cdot (%s) + m \\cdot (%s) + p \\cdot (%s))$ \\\\ $= (%sk + %sm + %sp; %sk + %sm + %sp; %sm + %sp)$. \\\\ Do $\\vec{v} = k\\vec{a} + m\\vec{b} + p\\vec{c}$ nên ta có hệ phương trình: \\\\ $\\begin{cases} %sk + %sm + %sp = %s \\\\ %sk + %sm + %sp = %s \\\\ %sm + %sp = %s \\end{cases} \\Leftrightarrow \\begin{cases} k = %s \\\\ m = %s \\\\ p = %s \\end{cases}$ \\\\ Khi đó: $k + m + p = %s + %s + %s = %s$.""" % (
        a1, b1, c1, a2, b2, c2, a3, b3, c3,
        a1, b1, c1, a2, b2, c2, b3, c3,
        a1, b1, c1, v1,
        a2, b2, c2, v2,
        b3, c3, v3,
        k0, m0, p0,
        k0, m0, p0, sum_kmp
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
        "\\end{ex}\n \\end{minipage}\n\n" )
    return content
    