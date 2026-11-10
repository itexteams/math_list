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


def bt_dang51_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba vectơ a, b, c
    while True:
        # Vectơ a
        a1 = random.choice([2, 3, 4, 5])
        a2 = random.choice([1, 2, 3, 4])
        a3 = random.choice([-3, -2, -1, 1, 2])
    
        # Vectơ b (có hoành độ bằng 0 như đề gốc hoặc số nhỏ)
        b1 = 0
        b2 = random.choice([1, 2, 3])
        b3 = random.choice([-2, -1, 1, 2])
    
        # Vectơ c
        c1 = random.choice([-4, -3, -2, 2, 3])
        c2 = random.choice([1, 2, 3])
        c3 = random.choice([1, 2, 3])
    
        # Tính độ dài vectơ a, b
        len_a_sq = a1**2 + a2**2 + a3**2
        len_b_sq = b1**2 + b2**2 + b3**2
    
        # Vectơ a + b
        ab1 = a1 + b1
        ab2 = a2 + b2
        ab3 = a3 + b3
    
        # Tích vô hướng (a + b) . c
        dot_apb_c = ab1 * c1 + ab2 * c2 + ab3 * c3
    
        # Tích vô hướng a . c (kiểm tra tính vuông góc)
        dot_a_c = a1 * c1 + a2 * c2 + a3 * c3
    
        # Tích vô hướng a . b và cosin góc giữa a và b
        dot_a_b = a1 * b1 + a2 * b2 + a3 * b3
        prod_len_sq = len_a_sq * len_b_sq
    
        if (
            len_a_sq > 0
            and len_b_sq > 0
            and dot_a_b != 0
            and (a1, a2, a3) != (b1, b2, b3)
        ):
            break
    
    # 1. Tích vô hướng (a + b) . c
    dot_apb_c_true = dot_apb_c
    dot_apb_c_false = dot_apb_c + random.choice([-3, -2, 2, 3])
    
    # 2. Độ dài hai vectơ a và b
    str_len_a = latex(sp.sqrt(len_a_sq))
    str_len_b = latex(sp.sqrt(len_b_sq))
    str_len_a_false = (
        latex(sp.sqrt(len_a_sq + 2))
        if sp.sqrt(len_a_sq) != sp.sqrt(len_a_sq + 2)
        else "\\sqrt{30}"
    )
    
    # 3. Hai vectơ a và c vuông góc nhau
    is_a_c_orthogonal = dot_a_c == 0
    
    # 4. Côsin của góc giữa hai vectơ a và b
    str_cos_ab_true = "\\frac{%s}{\\sqrt{%s}}" % (dot_a_b, prod_len_sq)
    str_cos_ab_false = "\\frac{%s}{\\sqrt{%s}}" % (
        dot_a_b + random.choice([-1, 1]),
        prod_len_sq,
    )
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho ba vectơ $\\vec{a} = (%s;%s;%s)$, $\\vec{b} = (%s;%s;%s)$, $\\vec{c} = (%s;%s;%s)$."""
        % (a1, a2, a3, b1, b2, b3, c1, c2, c3)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Tích vô hướng (a + b) . c
    nb_da_1_d = (
        "\\True Tích vô hướng $(\\vec{a} + \\vec{b}) \\cdot \\vec{c}$ bằng $%s$"
        % (dot_apb_c_true)
    )
    nb_da_1_s = (
        "Tích vô hướng $(\\vec{a} + \\vec{b}) \\cdot \\vec{c}$ bằng $%s$"
        % (dot_apb_c_false)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ của vectơ $\\vec{a} + \\vec{b}$ là: \\\\ $\\vec{a} + \\vec{b} = (%s + %s; %s + %s; %s + (%s)) = (%s;%s;%s)$. \\\\ Khi đó tích vô hướng của $(\\vec{a} + \\vec{b})$ và $\\vec{c}$ là: \\\\ $(\\vec{a} + \\vec{b}) \\cdot \\vec{c} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$."""
        % (
            a1,
            b1,
            a2,
            b2,
            a3,
            b3,
            ab1,
            ab2,
            ab3,
            ab1,
            c1,
            ab2,
            c2,
            ab3,
            c3,
            dot_apb_c_true,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Độ dài của hai vectơ a và b
    th_da_1_d = (
        "\\True Độ dài của hai vectơ $\\vec{a} = (%s;%s;%s)$, $\\vec{b} = (%s;%s;%s)$ lần lượt bằng $%s$ và $%s$"
        % (a1, a2, a3, b1, b2, b3, str_len_a, str_len_b)
    )
    th_da_1_s = (
        "Độ dài của hai vectơ $\\vec{a} = (%s;%s;%s)$, $\\vec{b} = (%s;%s;%s)$ lần lượt bằng $%s$ và $%s$"
        % (a1, a2, a3, b1, b2, b3, str_len_a_false, str_len_b)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Độ dài của vectơ $\\vec{a}$ là: \\\\ $|\\vec{a}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$. \\\\ Độ dài của vectơ $\\vec{b}$ là: \\\\ $|\\vec{b}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$."""
        % (
            a1,
            a2,
            a3,
            len_a_sq,
            str_len_a,
            b1,
            b2,
            b3,
            len_b_sq,
            str_len_b,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: a và c vuông góc nhau
    if is_a_c_orthogonal:
        vd_da_1_d = "\\True $\\vec{a}$ và $\\vec{c}$ vuông góc nhau"
        vd_da_1_s = "$\\vec{a}$ và $\\vec{c}$ không vuông góc nhau"
    else:
        vd_da_1_d = "\\True $\\vec{a}$ và $\\vec{c}$ không vuông góc nhau"
        vd_da_1_s = "$\\vec{a}$ và $\\vec{c}$ vuông góc nhau"
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Tích vô hướng của hai vectơ $\\vec{a}$ và $\\vec{c}$ là: \\\\ $\\vec{a} \\cdot \\vec{c} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Vì $\\vec{a} \\cdot \\vec{c} = %s %s 0$ nên hai vectơ $\\vec{a}$ và $\\vec{c}$ %s."""
        % (
            a1,
            c1,
            a2,
            c2,
            a3,
            c3,
            dot_a_c,
            dot_a_c,
            "=" if is_a_c_orthogonal else "\\neq",
            "vuông góc với nhau" if is_a_c_orthogonal else "không vuông góc với nhau",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Côsin của góc giữa hai vectơ a và b
    vdc_da_1_d = (
        "\\True Côsin của góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ bằng $%s$"
        % (str_cos_ab_true)
    )
    vdc_da_1_s = (
        "Côsin của góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ bằng $%s$"
        % (str_cos_ab_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Tích vô hướng của hai vectơ $\\vec{a}$ và $\\vec{b}$ là: \\\\ $\\vec{a} \\cdot \\vec{b} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Độ dài của các vectơ là: \\\\ $|\\vec{a}| = \\sqrt{%s}$ và $|\\vec{b}| = \\sqrt{%s}$. \\\\ Khi đó côsin của góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ là: \\\\ $\\cos(\\vec{a}, \\vec{b}) = \\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{a}| \\cdot |\\vec{b}|} = \\frac{%s}{\\sqrt{%s} \\cdot \\sqrt{%s}} = \\frac{%s}{\\sqrt{%s}}$."""
        % (
            a1,
            b1,
            a2,
            b2,
            a3,
            b3,
            dot_a_b,
            len_a_sq,
            len_b_sq,
            dot_a_b,
            len_a_sq,
            len_b_sq,
            dot_a_b,
            prod_len_sq,
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
    