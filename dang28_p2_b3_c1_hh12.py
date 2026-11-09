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


def bt_dang28_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba vectơ a, b, c
    # a có độ dài nguyên đẹp (ví dụ bộ ba Pythagore mở rộng: 1, 2, 2 hoặc 2, 3, 6)
    # b nằm trong mặt phẳng (Oxz) để vuông góc với c (trên trục Oy)
    while True:
        # Vectơ a
        a1 = random.choice([1, 2, -1, -2])
        a2 = random.choice([-2, 2, -3, 3])
        a3 = random.choice([2, -2, 6, -6])
    
        len_a_sq = a1**2 + a2**2 + a3**2
        len_a = int(math.isqrt(len_a_sq))
        if len_a * len_a != len_a_sq:
            continue
    
        # Vectơ c nằm trên trục Oy: c = (0, c2, 0)
        c2 = random.choice([-3, -2, 2, 3])
        c1, c3 = 0, 0
    
        # Vectơ b nằm trong mặt phẳng (Oxz): b = (b1, 0, b3)
        # Chọn b1 và b3 sao cho -b3 chia hết cho b1 để nghiệm a của u nguyên
        b1 = random.choice([-2, -1, 1, 2])
        mult = random.choice([-3, -2, 2, 3])
        b3 = -b1 * mult
        b2 = 0
    
        len_b_sq = b1**2 + b2**2 + b3**2
        # Nghiệm a: b1*a + b3*1 = 0 => a = -b3/b1 = mult
        sol_a = -b3 // b1
        # Nghiệm b: a1*sol_a + a2*b + a3 = 0 => a2*b = -(a1*sol_a + a3)
        rem_b = -(a1 * sol_a + a3)
        if rem_b % a2 != 0:
            continue
        sol_b = rem_b // a2
    
        # Tích vô hướng b . c = 0 (b vuông góc c)
        dot_bc = b1 * c1 + b2 * c2 + b3 * c3
    
        # cos(a, c) = (a . c) / (|a| * |c|)
        dot_ac = a1 * c1 + a2 * c2 + a3 * c3
        len_c = abs(c2)
    
        cos_ac_sym = Rational(dot_ac, len_a * len_c)
        str_cos_ac_true = format_fraction_latex(cos_ac_sym.p, cos_ac_sym.q)
        # Khẳng định sai cho cos(a, c) (nhầm dấu giá trị dương như bài gốc)
        str_cos_ac_false = format_fraction_latex(abs(cos_ac_sym.p), cos_ac_sym.q)
    
        if (
            len_b_sq > 0
            and dot_bc == 0
            and str_cos_ac_true != str_cos_ac_false
        ):
            break
    
    # 1. Độ dài |b| = \sqrt{len_b_sq}[cite: 25]
    str_len_b_true = latex(sp.sqrt(len_b_sq))
    # Khẳng định sai: quên căn bậc hai, ví dụ |b| = len_b_sq[cite: 25]
    str_len_b_false = str(len_b_sq)
    
    # 2. b vuông góc với c[cite: 25]
    
    # 3. cos(a, c)[cite: 25]
    
    # 4. Tồn tại vectơ u = (a; b; 1) vuông góc với cả a và b:
    # Vì luôn tồn tại duy nhất u = (sol_a; sol_b; 1) nên khẳng định "Không tồn tại" là SAI[cite: 25]
    
    # Nội dung câu hỏi[cite: 25]
    noidungcauhoi = (
        """Trong không gian $Oxyz$, cho $\\vec{a}=(%s;%s;%s)$, $\\vec{b}=(%s;%s;%s)$, $\\vec{c}=(%s;%s;%s)$."""
        % (a1, a2, a3, b1, b2, b3, c1, c2, c3)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Độ dài vectơ b[cite: 25]
    nb_da_1_d = "\\True $|\\vec{b}| = %s$" % (str_len_b_true)
    nb_da_1_s = "$|\\vec{b}| = %s$" % (str_len_b_false)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Độ dài của vectơ $\\vec{b}$ là: \\\\ $|\\vec{b}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$."""
        % (
            b1,
            b2,
            b3,
            len_b_sq,
            str_len_b_true,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: b vuông góc với c[cite: 25]
    th_da_1_d = "\\True $\\vec{b}$ vuông góc với $\\vec{c}$"
    th_da_1_s = "$\\vec{b}$ không vuông góc với $\\vec{c}$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta xét tích vô hướng của hai vectơ $\\vec{b}$ và $\\vec{c}$: \\\\ $\\vec{b} \\cdot \\vec{c} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = 0$. \\\\ Vì tích vô hướng bằng $0$ nên hai vectơ $\\vec{b}$ và $\\vec{c}$ vuông góc với nhau."""
        % (
            b1,
            c1,
            b2,
            c2,
            b3,
            c3,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: cos(a, c)[cite: 25]
    vd_da_1_d = "\\True $\\cos(\\vec{a},\\vec{c}) = %s$" % (str_cos_ac_true)
    vd_da_1_s = "$\\cos(\\vec{a},\\vec{c}) = %s$" % (str_cos_ac_false)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có: \\\\ $|\\vec{a}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$. \\\\ $|\\vec{c}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = %s$. \\\\ Tích vô hướng: \\\\ $\\vec{a} \\cdot \\vec{c} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Do đó: \\\\ $\\cos(\\vec{a},\\vec{c}) = \\frac{\\vec{a} \\cdot \\vec{c}}{|\\vec{a}| \\cdot |\\vec{c}|} = \\frac{%s}{%s \\cdot %s} = %s$."""
        % (
            a1,
            a2,
            a3,
            len_a_sq,
            len_a,
            c1,
            c2,
            c3,
            len_c,
            a1,
            c1,
            a2,
            c2,
            a3,
            c3,
            dot_ac,
            dot_ac,
            len_a,
            len_c,
            str_cos_ac_true,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Tồn tại/Không tồn tại vectơ u = (a; b; 1) vuông góc với cả hai vectơ a và b[cite: 25]
    vdc_da_1_d = (
        "\\True Tồn tại vectơ $\\vec{u} = (a;b;1)$ vuông góc với cả hai vectơ $\\vec{a}(%s;%s;%s)$, $\\vec{b}(%s;%s;%s)$"
        % (a1, a2, a3, b1, b2, b3)
    )
    vdc_da_1_s = (
        "Không tồn tại vectơ $\\vec{u} = (a;b;1)$ vuông góc với cả hai vectơ $\\vec{a}(%s;%s;%s)$, $\\vec{b}(%s;%s;%s)$"
        % (a1, a2, a3, b1, b2, b3)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vectơ $\\vec{u} = (a;b;1)$ vuông góc với cả hai vectơ $\\vec{a}$ và $\\vec{b}$ khi và chỉ khi: \\\\ $\\begin{cases} \\vec{u} \\cdot \\vec{b} = 0 \\\\ \\vec{u} \\cdot \\vec{a} = 0 \\end{cases} \\Leftrightarrow \\begin{cases} (%s) \\cdot a + (%s) \\cdot b + (%s) \\cdot 1 = 0 \\\\ (%s) \\cdot a + (%s) \\cdot b + (%s) \\cdot 1 = 0 \\end{cases}$ \\\\ $\\Leftrightarrow \\begin{cases} %sa + %s = 0 \\\\ %sa + %sb + (%s) = 0 \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$ \\\\ Như vậy tồn tại duy nhất vectơ $\\vec{u} = (%s;%s;1)$ thỏa mãn yêu cầu bài toán."""
        % (
            b1,
            b2,
            b3,
            a1,
            a2,
            a3,
            b1,
            b3,
            a1,
            a2,
            a3,
            sol_a,
            sol_b,
            sol_a,
            sol_b,
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
        "\\end{ex}\n \\end{minipage}\n\n" )
    return content
    