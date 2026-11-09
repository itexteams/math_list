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


def bt_dang25_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hai vectơ a và b sao cho m, n là số nguyên đẹp[cite: 22]
    while True:
        # Vectơ a có tung độ bằng 0 như đề gốc[cite: 22]
        a1 = random.choice([-3, -2, -1, 1, 2, 3])
        a2 = 0
        a3 = random.choice([-4, -3, 2, 3, 4])
    
        # Vectơ b[cite: 22]
        b1 = random.choice([-3, -2, 1, 2, 3])
        b2 = random.choice([1, 2, 3])
        b3 = random.choice([-3, -2, -1, 1, 2, 3])
    
        # Kiểm tra a và b không cùng phương[cite: 22]
        if a1 * b3 - a3 * b1 != 0:
            # Chọn trước các hệ số m0, n0 nguyên cho khẳng định d[cite: 22]
            m0 = random.randint(1, 4)
            n0 = random.randint(1, 4)
    
            # Vectơ c = m0 * a + n0 * b[cite: 22]
            c1 = m0 * a1 + n0 * b1
            c2 = m0 * a2 + n0 * b2
            c3 = m0 * a3 + n0 * b3
    
            # Đảm bảo c khác a và b
            if (c1, c2, c3) != (a1, a2, a3) and (c1, c2, c3) != (b1, b2, b3):
                break
    
    # 1. Tính tọa độ vectơ u = a - 3b[cite: 22]
    k_coef = 3
    u_x = a1 - k_coef * b1
    u_y = a2 - k_coef * b2
    u_z = a3 - k_coef * b3
    
    # Dạng tọa độ sai của u (nhầm dấu phép trừ như đề gốc)[cite: 22]
    u_x_s = -(a1 - k_coef * b1)
    u_y_s = -(a2 - k_coef * b2)
    u_z_s = a3 - k_coef * b3
    
    # 2. Độ dài vectơ |a| = \sqrt{a1^2 + a2^2 + a3^2}[cite: 22]
    len_a_sq = a1**2 + a2**2 + a3**2
    str_len_a = latex(sp.sqrt(len_a_sq))
    str_len_a_s = latex(sp.sqrt(len_a_sq + random.choice([-3, -2, 2, 3])))
    
    # 3. Tích vô hướng a . b = a1*b1 + a2*b2 + a3*b3[cite: 22]
    dot_ab = a1 * b1 + a2 * b2 + a3 * b3
    dot_ab_s = -dot_ab if dot_ab != 0 else 5
    
    # 4. Tìm m, n để c = m * a + n * b[cite: 22]
    # Vì a2 = 0 nên c2 = n * b2 => n = c2 / b2 = n0
    # Sau đó c1 = m * a1 + n * b1 => m = (c1 - n0 * b1) / a1 = m0
    sum_mn = m0 + n0
    # Chọn cận so sánh bound_mn sao cho m + n < bound_mn[cite: 22]
    bound_mn = sum_mn + random.choice([1, 2, 3])
    is_sum_mn_lt = sum_mn < bound_mn
    
    # Nội dung câu hỏi[cite: 22]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho hai vectơ $\\vec{a} = (%s;%s;%s), \\vec{b} = (%s;%s;%s)$."""
        % (a1, a2, a3, b1, b2, b3)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Tọa độ vectơ a - 3b[cite: 22]
    nb_da_1_d = "\\True $\\vec{a} - 3\\vec{b} = (%s;%s;%s)$" % (u_x, u_y, u_z)
    nb_da_1_s = "$\\vec{a} - 3\\vec{b} = (%s;%s;%s)$" % (u_x_s, u_y_s, u_z_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có $3\\vec{b} = 3 \\cdot (%s;%s;%s) = (%s;%s;%s)$. \\\\ Do đó: \\\\ $\\vec{a} - 3\\vec{b} = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (
            b1,
            b2,
            b3,
            k_coef * b1,
            k_coef * b2,
            k_coef * b3,
            a1,
            k_coef * b1,
            a2,
            k_coef * b2,
            a3,
            k_coef * b3,
            u_x,
            u_y,
            u_z,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Độ dài của vectơ a[cite: 22]
    th_da_1_d = "\\True $|\\vec{a}| = %s$" % (str_len_a)
    th_da_1_s = "$|\\vec{a}| = %s$" % (str_len_a_s)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Độ dài của vectơ $\\vec{a}$ là: \\\\ $|\\vec{a}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s + %s + %s} = %s$."""
        % (
            a1,
            a2,
            a3,
            a1**2,
            a2**2,
            a3**2,
            str_len_a,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Tích vô hướng a . b[cite: 22]
    vd_da_1_d = "\\True $\\vec{a} \\cdot \\vec{b} = %s$" % (dot_ab)
    vd_da_1_s = "$\\vec{a} \\cdot \\vec{b} = %s$" % (dot_ab_s)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Tích vô hướng của hai vectơ $\\vec{a}$ và $\\vec{b}$ là: \\\\ $\\vec{a} \\cdot \\vec{b} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s + %s + %s = %s$."""
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
            dot_ab,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Nếu c = m * a + n * b thì m + n < bound_mn[cite: 22]
    if is_sum_mn_lt:
        vdc_da_1_d = (
            "\\True Nếu $\\vec{c} = (%s;%s;%s) = m\\vec{a} + n\\vec{b}$ thì $m + n < %s$"
            % (c1, c2, c3, bound_mn)
        )
        vdc_da_1_s = (
            "Nếu $\\vec{c} = (%s;%s;%s) = m\\vec{a} + n\\vec{b}$ thì $m + n > %s$"
            % (c1, c2, c3, bound_mn)
        )
    else:
        vdc_da_1_d = (
            "\\True Nếu $\\vec{c} = (%s;%s;%s) = m\\vec{a} + n\\vec{b}$ thì $m + n > %s$"
            % (c1, c2, c3, bound_mn)
        )
        vdc_da_1_s = (
            "Nếu $\\vec{c} = (%s;%s;%s) = m\\vec{a} + n\\vec{b}$ thì $m + n < %s$"
            % (c1, c2, c3, bound_mn)
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta có $m\\vec{a} + n\\vec{b} = (m \\cdot (%s) + n \\cdot (%s); m \\cdot (%s) + n \\cdot (%s); m \\cdot (%s) + n \\cdot (%s)) = (%sm + %sn; %sn; %sm + %sn)$. \\\\ Từ $\\vec{c} = m\\vec{a} + n\\vec{b}$, ta có hệ phương trình: \\\\ $\\begin{cases} %sm + %sn = %s \\\\ %sn = %s \\\\ %sm + %sn = %s \\end{cases} \\Leftrightarrow \\begin{cases} n = %s \\\\ m = %s \\end{cases}$ \\\\ Khi đó: $m + n = %s + %s = %s$. \\\\ Vì $%s %s %s$ nên khẳng định $m + n %s %s$ là %s."""
        % (
            a1,
            b1,
            a2,
            b2,
            a3,
            b3,
            a1,
            b1,
            b2,
            a3,
            b3,
            a1,
            b1,
            c1,
            b2,
            c2,
            a3,
            b3,
            c3,
            n0,
            m0,
            m0,
            n0,
            sum_mn,
            sum_mn,
            "<" if is_sum_mn_lt else ">",
            bound_mn,
            "<" if is_sum_mn_lt else ">",
            bound_mn,
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
    