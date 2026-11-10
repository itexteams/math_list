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


def bt_dang55_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba vectơ a, b, c(m)[cite: 24]
    # a = (a1; a2; a3), b = (b1; b2; b3) sao cho a . b = 0 (góc giữa a và b bằng 90 độ)[cite: 24]
    # c = (m; c2; m + k_c)[cite: 24]
    # a . c = a1*m + a2*c2 + a3*(m + k_c) = (a1 + a3)*m + (a2*c2 + a3*k_c)[cite: 24]
    while True:
        # Chọn a1, a2, a3 sao cho a1 + a3 > 0
        a1 = random.choice([4, 5, 6])
        a2 = random.choice([2, 3, 4])
        a3 = random.choice([-3, -2, -1])
        len_a_sq = a1**2 + a2**2 + a3**2
    
        # Tìm b sao cho a1*b1 + a2*b2 + a3*b3 = 0[cite: 24]
        found_b = False
        for b1 in range(-3, 3):
            if b1 == 0:
                continue
            for b2 in range(1, 5):
                rem = -(a1 * b1 + a2 * b2)
                if rem % a3 == 0:
                    b3 = rem // a3
                    if -5 <= b3 <= 5 and (b1, b2, b3) != (0, 0, 0):
                        found_b = True
                        break
            if found_b:
                break
    
        if not found_b:
            continue
    
        # Tham số cho vectơ c: c = (m; c2; m + k_c)[cite: 24]
        c2 = random.choice([-2, -1, 1])
        k_c = random.choice([2, 3, 4])
    
        alpha = a1 + a3  # Hệ số của m trong a . c[cite: 24]
        beta = a2 * c2 + a3 * k_c  # Hằng số tự do trong a . c[cite: 24]
    
        # Để a . c < 0 tương đương alpha * m + beta < 0 <=> m < -beta / alpha (do alpha > 0)[cite: 24]
        # Ta chọn sao cho -beta / alpha là số nguyên m_bound >= 2 để có m_bound - 1 nghiệm nguyên dương[cite: 24]
        if alpha > 0 and (-beta) % alpha == 0:
            m_bound = (-beta) // alpha
            if 2 <= m_bound <= 4:
                count_positive_m = m_bound - 1
                break
    
    # 1. Khẳng định a: Góc giữa hai vectơ a và b bằng 90 độ (do a . b = 0)[cite: 24]
    dot_a_b = a1 * b1 + a2 * b2 + a3 * b3
    
    # 2. Khẳng định b: Khi m = 0, côsin góc giữa hai vectơ a và c[cite: 24]
    # c(0) = (0; c2; k_c)[cite: 24]
    c_m0 = (0, c2, k_c)
    len_c_m0_sq = c2**2 + k_c**2
    dot_a_c_m0 = a2 * c2 + a3 * k_c  # = beta[cite: 24]
    prod_len_m0_sq = len_a_sq * len_c_m0_sq
    
    # cos(a, c) = beta / sqrt(prod_len_m0_sq)[cite: 24]
    str_cos_m0_true = format_fraction_latex(dot_a_c_m0, 1) + "/\\sqrt{%s}" % (
        prod_len_m0_sq
    ) if dot_a_c_m0 >= 0 else "-\\frac{%s}{\\sqrt{%s}}" % (
        -dot_a_c_m0,
        prod_len_m0_sq,
    )
    
    # Giá trị sai (nhầm mất dấu trừ nếu dot_a_c_m0 < 0 như đề gốc)[cite: 24]
    str_cos_m0_false = "\\frac{%s}{\\sqrt{%s}}" % (abs(dot_a_c_m0), prod_len_m0_sq)
    is_b_true = (str_cos_m0_true == str_cos_m0_false)
    
    # 3. Khẳng định c: Với m = 1, hai vectơ a + b và c vuông góc[cite: 24]
    # a + b = (a1 + b1; a2 + b2; a3 + b3)[cite: 24]
    apb_x = a1 + b1
    apb_y = a2 + b2
    apb_z = a3 + b3
    
    # Với m = 1, c = (1; c2; 1 + k_c)[cite: 24]
    c_m1_x = 1
    c_m1_y = c2
    c_m1_z = 1 + k_c
    
    dot_apb_c = apb_x * c_m1_x + apb_y * c_m1_y + apb_z * c_m1_z
    is_apb_c_orthogonal = dot_apb_c == 0
    
    # 4. Khẳng định d: Số giá trị nguyên dương của m để góc giữa a và c là góc tù[cite: 24]
    count_d_true = count_positive_m
    count_d_false = count_d_true + random.choice([-1, 1])
    if count_d_false == 0:
        count_d_false = count_d_true + 2
    
    # Chuỗi hiển thị cho vectơ c[cite: 24]
    str_c2 = str(c2)
    str_c3 = "m + %s" % (k_c) if k_c > 0 else "m - %s" % (-k_c)
    
    # Nội dung câu hỏi[cite: 24]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho các vectơ $\\vec{a} = (%s;%s;%s); \\vec{b} = (%s;%s;%s)$ và $\\vec{c} = (m;%s;%s)$."""
        % (a1, a2, a3, b1, b2, b3, str_c2, str_c3)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Góc giữa hai vectơ a và b bằng 90 độ[cite: 24]
    nb_da_1_d = "\\True Góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ bằng $90^\\circ$"
    nb_da_1_s = "Góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ bằng $60^\\circ$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Tích vô hướng của hai vectơ $\\vec{a}$ và $\\vec{b}$ là: \\\\ $\\vec{a} \\cdot \\vec{b} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s + (%s) + (%s) = 0$. \\\\ Vì $\\vec{a} \\cdot \\vec{b} = 0$ và $\\vec{a} \\neq \\vec{0}, \\vec{b} \\neq \\vec{0}$ nên hai vectơ $\\vec{a}$ và $\\vec{b}$ vuông góc với nhau. \\\\ Do đó góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ bằng $90^\\circ$."""
        % (
            a1,
            b1,
            a2,
            b2,
            a3,
            b3,
            a1 * b1,
            a2 * b2,
            a3 * b3,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Khi m = 0 thì côsin góc giữa hai vectơ a và c bằng ...[cite: 24]
    th_da_1_d = (
        "\\True Khi $m = 0$ thì côsin góc giữa hai vectơ $\\vec{a}$ và $\\vec{c}$ bằng $%s$"
        % (str_cos_m0_true)
    )
    th_da_1_s = (
        "Khi $m = 0$ thì côsin góc giữa hai vectơ $\\vec{a}$ và $\\vec{c}$ bằng $%s$"
        % (str_cos_m0_false)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Khi $m = 0$, ta có $\\vec{c} = (0;%s;%s)$. \\\\ Độ dài của các vectơ là: \\\\ $|\\vec{a}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $|\\vec{c}| = \\sqrt{0^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Tích vô hướng của $\\vec{a}$ và $\\vec{c}$: \\\\ $\\vec{a} \\cdot \\vec{c} = (%s) \\cdot 0 + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Khi đó côsin góc giữa hai vectơ là: \\\\ $\\cos(\\vec{a}, \\vec{c}) = \\frac{\\vec{a} \\cdot \\vec{c}}{|\\vec{a}| \\cdot |\\vec{c}|} = \\frac{%s}{\\sqrt{%s} \\cdot \\sqrt{%s}} = %s$."""
        % (
            c2,
            k_c,
            a1,
            a2,
            a3,
            len_a_sq,
            c2,
            k_c,
            len_c_m0_sq,
            a1,
            a2,
            c2,
            a3,
            k_c,
            dot_a_c_m0,
            dot_a_c_m0,
            len_a_sq,
            len_c_m0_sq,
            str_cos_m0_true,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Với m = 1 thì hai vectơ a + b và c vuông góc[cite: 24]
    if is_apb_c_orthogonal:
        vd_da_1_d = "\\True Với $m = 1$ thì hai vectơ $\\vec{a} + \\vec{b}$ và $\\vec{c}$ vuông góc"
        vd_da_1_s = "Với $m = 1$ thì hai vectơ $\\vec{a} + \\vec{b}$ và $\\vec{c}$ không vuông góc"
    else:
        vd_da_1_d = "\\True Với $m = 1$ thì hai vectơ $\\vec{a} + \\vec{b}$ và $\\vec{c}$ không vuông góc"
        vd_da_1_s = "Với $m = 1$ thì hai vectơ $\\vec{a} + \\vec{b}$ và $\\vec{c}$ vuông góc"
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có tọa độ của vectơ $\\vec{a} + \\vec{b}$ là: \\\\ $\\vec{a} + \\vec{b} = (%s + (%s); %s + (%s); %s + (%s)) = (%s;%s;%s)$. \\\\ Với $m = 1$, vectơ $\\vec{c}$ có tọa độ là: \\\\ $\\vec{c} = (1;%s;1 + %s) = (%s;%s;%s)$. \\\\ Xét tích vô hướng: \\\\ $(\\vec{a} + \\vec{b}) \\cdot \\vec{c} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Vì $(\\vec{a} + \\vec{b}) \\cdot \\vec{c} = %s %s 0$ nên hai vectơ $\\vec{a} + \\vec{b}$ và $\\vec{c}$ %s."""
        % (
            a1,
            b1,
            a2,
            b2,
            a3,
            b3,
            apb_x,
            apb_y,
            apb_z,
            c2,
            k_c,
            c_m1_x,
            c_m1_y,
            c_m1_z,
            apb_x,
            c_m1_x,
            apb_y,
            c_m1_y,
            apb_z,
            c_m1_z,
            dot_apb_c,
            dot_apb_c,
            "=" if is_apb_c_orthogonal else "\\neq",
            "vuông góc với nhau" if is_apb_c_orthogonal else "không vuông góc với nhau",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Số giá trị nguyên dương của m để góc giữa a và c là góc tù[cite: 24]
    vdc_da_1_d = (
        "\\True Có $%s$ giá trị nguyên dương của $m$ để góc giữa hai vectơ $\\vec{a}$ và $\\vec{c}$ là góc tù"
        % (count_d_true)
    )
    vdc_da_1_s = (
        "Có $%s$ giá trị nguyên dương của $m$ để góc giữa hai vectơ $\\vec{a}$ và $\\vec{c}$ là góc tù"
        % (count_d_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_m_vals = ", ".join(str(i) for i in range(1, m_bound))
    
    loigiai_vdc_1 = (
        """Góc giữa hai vectơ $\\vec{a}$ và $\\vec{c}$ là góc tù khi và chỉ khi: \\\\ $\\begin{cases} \\vec{a} \\cdot \\vec{c} < 0 \\\\ \\vec{a}, \\vec{c} \\text{ không cùng phương} \\end{cases}$. \\\\ Ta có: \\\\ $\\vec{a} \\cdot \\vec{c} = (%s) \\cdot m + (%s) \\cdot (%s) + (%s) \\cdot (m + %s)$ \\\\ $= %sm + (%s) + (%sm + (%s)) = %sm + (%s)$. \\\\ Bất phương trình: \\\\ $\\vec{a} \\cdot \\vec{c} < 0 \\Leftrightarrow %sm + (%s) < 0 \\Leftrightarrow %sm < %s \\Leftrightarrow m < %s$. \\\\ Vì $m$ là số nguyên dương ($m \\in \\mathbb{Z}^+$) nên $m \\in \\{%s\\}$. \\\\ Với các giá trị $m \\in \\{%s\\}$, ta kiểm tra thấy hai vectơ $\\vec{a}$ và $\\vec{c}$ không cùng phương. \\\\ Vậy có đúng $%s$ giá trị nguyên dương của $m$ thỏa mãn yêu cầu bài toán."""
        % (
            a1,
            a2,
            c2,
            a3,
            k_c,
            a1,
            a2 * c2,
            a3,
            a3 * k_c,
            alpha,
            beta,
            alpha,
            beta,
            alpha,
            -beta,
            m_bound,
            str_m_vals,
            str_m_vals,
            count_d_true,
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
    