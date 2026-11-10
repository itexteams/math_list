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


def bt_dang66_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hai vectơ a và b(m)[cite: 25]
    # a = (a1; a2; a3)[cite: 25]
    # b = (m; b2; m + k_b)[cite: 25]
    # a . b = a1*m + a2*b2 + a3*(m + k_b) = (a1 + a3)*m + (a2*b2 + a3*k_b)[cite: 25]
    # Đặt alpha = a1 + a3, beta = a2*b2 + a3*k_b[cite: 25]
    # Góc giữa a và b tù <=> a . b < 0 <=> alpha * m + beta < 0 <=> m < -beta / alpha (khi alpha > 0)[cite: 25]
    while True:
        a1 = random.randint(4, 7)
        a2 = random.choice([2, 3, 4])
        a3 = random.choice([-3, -2, -1])
    
        len_a_sq = a1**2 + a2**2 + a3**2
    
        b2 = random.choice([-2, -1, 1, 2])
        k_b = random.choice([2, 3, 4, 5])
    
        alpha = a1 + a3
        beta = a2 * b2 + a3 * k_b
    
        # Chọn sao cho m_bound = -beta / alpha là số nguyên dương đẹp (từ 2 đến 5)[cite: 25]
        if alpha > 0 and (-beta) % alpha == 0:
            m_bound = (-beta) // alpha
            if 2 <= m_bound <= 5:
                # Giá trị nhỏ nhất của |b|:
                # |b|^2 = m^2 + b2^2 + (m + k_b)^2 = 2m^2 + 2*k_b*m + (b2^2 + k_b^2)[cite: 25]
                #        = 2*(m + k_b/2)^2 + b2^2 + k_b^2 / 2 >= b2^2 + k_b^2 / 2[cite: 25]
                min_len_b_sq = Rational(2 * (b2**2) + k_b**2, 2)
                min_len_b_sym = sp.sqrt(min_len_b_sq)
                break
    
    # 1. Khẳng định a: |a| = sqrt(len_a_sq)[cite: 25]
    str_len_a_true = latex(sp.sqrt(len_a_sq))
    str_len_a_false = latex(sp.sqrt(len_a_sq + random.choice([-3, -2, 2, 3])))
    if str_len_a_false == str_len_a_true:
        str_len_a_false = "\\sqrt{38}"[cite: 25]
    
    # 2. Khẳng định b: Nếu a = OA thì điểm A cách mặt phẳng (Oyz) một khoảng lớn hơn / nhỏ hơn bound_x[cite: 25]
    dist_a_oyz = abs(a1)
    bound_x = a1 - random.choice([1, 2])
    is_dist_gt_bound = dist_a_oyz > bound_x
    
    # 3. Khẳng định c: |b| >= min_len_b_sym, với mọi m[cite: 25]
    str_min_b_true = latex(min_len_b_sym)
    # Tạo giá trị sai cho bất đẳng thức của |b|[cite: 25]
    str_min_b_false = latex(sp.sqrt(min_len_b_sq + random.choice([3, 5, 7])))
    if str_min_b_false == str_min_b_true:
        str_min_b_false = "\\frac{13\\sqrt{2}}{2}"[cite: 25]
    
    # 4. Khẳng định d: Số lượng số nguyên dương của m để góc giữa a và b là góc tù[cite: 25]
    # m nguyên dương và m < m_bound => m in {1, 2, ..., m_bound - 1}[cite: 25]
    num_positive_m_true = m_bound - 1
    num_positive_m_false = (
        num_positive_m_true + 1 if num_positive_m_true < 4 else num_positive_m_true - 1
    )
    
    str_kb = "+ %s" % (k_b) if k_b > 0 else "- %s" % (-k_b)
    
    # Nội dung câu hỏi[cite: 25]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho các vectơ $\\vec{a} = (%s;%s;%s)$ và $\\vec{b} = (m;%s;m %s)$."""
        % (a1, a2, a3, b2, str_kb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: |a|[cite: 25]
    nb_da_1_d = "\\True $|\\vec{a}| = %s$" % (str_len_a_true)
    nb_da_1_s = "$|\\vec{a}| = %s$" % (str_len_a_false)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Độ dài của vectơ $\\vec{a}$ được tính theo công thức: \\\\ $|\\vec{a}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$."""
        % (
            a1,
            a2,
            a3,
            len_a_sq,
            str_len_a_true,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Nếu a = OA thì điểm A cách mặt phẳng (Oyz) một khoảng lớn hơn bound_x[cite: 25]
    if is_dist_gt_bound:
        th_da_1_d = (
            "\\True Nếu $\\vec{a} = \\vec{OA}$ thì điểm $A$ cách mặt phẳng $(Oyz)$ một khoảng lớn hơn $%s$"
            % (bound_x)
        )
        th_da_1_s = (
            "Nếu $\\vec{a} = \\vec{OA}$ thì điểm $A$ cách mặt phẳng $(Oyz)$ một khoảng nhỏ hơn $%s$"
            % (bound_x)
        )
    else:
        th_da_1_d = (
            "\\True Nếu $\\vec{a} = \\vec{OA}$ thì điểm $A$ cách mặt phẳng $(Oyz)$ một khoảng nhỏ hơn $%s$"
            % (bound_x)
        )
        th_da_1_s = (
            "Nếu $\\vec{a} = \\vec{OA}$ thì điểm $A$ cách mặt phẳng $(Oyz)$ một khoảng lớn hơn $%s$"
            % (bound_x)
        )
    
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì $\\vec{a} = \\vec{OA} = (%s;%s;%s)$ nên tọa độ của điểm $A$ là $A(%s;%s;%s)$. \\\\ Mặt phẳng tọa độ $(Oyz)$ có phương trình là $x = 0$. \\\\ Khoảng cách từ điểm $A$ đến mặt phẳng $(Oyz)$ là: \\\\ $d(A, (Oyz)) = |x_A| = |%s| = %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            a1,
            a2,
            a3,
            a1,
            a2,
            a3,
            a1,
            dist_a_oyz,
            dist_a_oyz,
            ">" if is_dist_gt_bound else "<",
            bound_x,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: |b| >= min_b, với mọi m[cite: 25]
    vd_da_1_d = "\\True $|\\vec{b}| \\ge %s, \\forall m$" % (str_min_b_true)
    vd_da_1_s = "$|\\vec{b}| \\ge %s, \\forall m$" % (str_min_b_false)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    str_half_k = format_fraction_latex(k_b, 2)
    str_rem_k = format_fraction_latex(min_len_b_sq.p, min_len_b_sq.q)
    
    loigiai_vd_1 = (
        """Độ dài của vectơ $\\vec{b}$ là: \\\\ $|\\vec{b}| = \\sqrt{m^2 + (%s)^2 + (m %s)^2} = \\sqrt{m^2 + %s + m^2 + %sm + %s} = \\sqrt{2m^2 + %sm + %s}$. \\\\ Ta biến đổi biểu thức trong căn: \\\\ $2m^2 + %sm + %s = 2\\left(m + %s\\right)^2 + %s \\ge %s, \\forall m$. \\\\ Do đó $|\\vec{b}| \\ge \\sqrt{%s} = %s, \\forall m$. \\\\ Vì vậy mệnh đề là %s."""
        % (
            b2,
            str_kb,
            b2**2,
            2 * k_b,
            k_b**2,
            2 * k_b,
            b2**2 + k_b**2,
            2 * k_b,
            b2**2 + k_b**2,
            str_half_k,
            str_rem_k,
            str_rem_k,
            str_rem_k,
            str_min_b_true,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Số giá trị nguyên dương của m để góc giữa a và b là góc tù[cite: 25]
    vdc_da_1_d = (
        "\\True Có đúng $%s$ số nguyên dương của $m$ để góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ là góc tù"
        % (num_positive_m_true)
    )
    vdc_da_1_s = (
        "Có đúng $%s$ số nguyên dương của $m$ để góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ là góc tù"
        % (num_positive_m_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_set_m = ", ".join(str(i) for i in range(1, m_bound))
    
    loigiai_vdc_1 = (
        """Góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ là góc tù khi và chỉ khi: \\\\ $\\begin{cases} \\vec{a} \\cdot \\vec{b} < 0 \\\\ \\vec{a}, \\vec{b} \\text{ không cùng phương} \\end{cases}$. \\\\ Ta có tích vô hướng của hai vectơ là: \\\\ $\\vec{a} \\cdot \\vec{b} = (%s) \\cdot m + (%s) \\cdot (%s) + (%s) \\cdot (m %s) = %sm + (%s) + (%sm + (%s)) = %sm + (%s)$. \\\\ Bất phương trình: \\\\ $\\vec{a} \\cdot \\vec{b} < 0 \\Leftrightarrow %sm + (%s) < 0 \\Leftrightarrow %sm < %s \\Leftrightarrow m < %s$. \\\\ Vì $m$ là số nguyên dương nên $m \\in \\{%s\\}$ (gồm $%s$ giá trị). \\\\ Với các giá trị này, hai vectơ $\\vec{a}$ và $\\vec{b}$ không cùng phương. \\\\ Vậy có đúng $%s$ số nguyên dương của $m$ thỏa mãn. Do đó khẳng định là %s."""
        % (
            a1,
            a2,
            b2,
            a3,
            str_kb,
            a1,
            a2 * b2,
            a3,
            a3 * k_b,
            alpha,
            beta,
            alpha,
            beta,
            alpha,
            -beta,
            m_bound,
            str_set_m,
            num_positive_m_true,
            num_positive_m_true,
            "đúng" if "\\True" in vdc_da_1 else "sai",
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
    