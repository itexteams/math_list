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


def bt_dang53_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hai vectơ a và b không cùng phương[cite: 22]
    while True:
        a1 = random.choice([-2, -1, 1, 2])
        a2 = random.choice([-3, -2, 1, 2, 3])
        a3 = random.choice([1, 2, 3, -1, -2])
    
        b1 = random.choice([-3, -2, -1, 1, 2])
        b2 = random.choice([-2, -1, 1, 2])
        b3 = random.choice([1, 2, 3, -1, -2])
    
        # Tích có hướng [a, b] xác định phương của vectơ c[cite: 22]
        # c cùng phương với [a, b] = (u1, u2, u3)[cite: 22]
        u1 = a2 * b3 - a3 * b2
        u2 = a3 * b1 - a1 * b3
        u3 = a1 * b2 - a2 * b1
    
        # Tích vô hướng a . b[cite: 22]
        dot_a_b = a1 * b1 + a2 * b2 + a3 * b3
        len_a_sq = a1**2 + a2**2 + a3**2
        len_b_sq = b1**2 + b2**2 + b3**2
    
        # a . (a - b) = |a|^2 - a . b[cite: 22]
        val_a_amb = len_a_sq - dot_a_b
    
        # Rút gọn vectơ (u1, u2, u3) bằng GCD[cite: 22]
        g = math.gcd(math.gcd(abs(u1), abs(u2)), abs(u3))
    
        if (u1 != 0 or u2 != 0 or u3 != 0) and dot_a_b != 0 and g > 0:
            c_dir1 = u1 // g
            c_dir2 = u2 // g
            c_dir3 = u3 // g
    
            # Đảm bảo c_dir1 > 0 để đồng bộ dấu nếu có thể
            if c_dir1 < 0:
                c_dir1, c_dir2, c_dir3 = -c_dir1, -c_dir2, -c_dir3
    
            # Tìm mối quan hệ giữa x và z (mệnh đề d): x / c_dir1 = z / c_dir3 <=> c_dir3 * x - c_dir1 * z = 0[cite: 22]
            # Đặt A_d * x + B_d * z = 0 với A_d = c_dir3, B_d = -c_dir1
            if c_dir1 != 0 and c_dir3 != 0:
                coef_x = c_dir3
                coef_z = -c_dir1
                # Rút gọn hệ số
                g_xz = math.gcd(abs(coef_x), abs(coef_z))
                coef_x //= g_xz
                coef_z //= g_xz
                if coef_x < 0:
                    coef_x, coef_z = -coef_x, -coef_z
                break
    
    # 1. Tích vô hướng a . (a - b)[cite: 22]
    val_a_amb_true = val_a_amb
    val_a_amb_false = val_a_amb + random.choice([-2, -1, 1, 2])
    
    # 2. Góc giữa hai vectơ a và b[cite: 22]
    # dot_a_b < 0 <=> góc tù; dot_a_b > 0 <=> góc nhọn[cite: 22]
    is_angle_obtuse = dot_a_b < 0
    
    # 3. Mệnh đề c: c vuông góc với 2a - b thì ...[cite: 22]
    # Vì c vuông góc với cả a và b nên c vuông góc với mọi tổ hợp tuyến tính k*a + m*b[cite: 22]
    # Do đó c vuông góc với 2a - b luôn luôn đúng với mọi vectơ c thỏa mãn giả thiết đề bài![cite: 22]
    # Trong khi đó hệ thức 3x + 4y = 0 chỉ đúng khi tỉ số tương ứng thỏa mãn (thường sai với c tổng quát)[cite: 22]
    # Ta kiểm tra xem hệ thức c_dir3 * x - c_dir1 * y = 0 có thỏa mãn không:
    is_rel_xy_true = (3 * c_dir1 + 4 * c_dir2 == 0)
    
    # 4. Mệnh đề d: coef_x * x + coef_z * z = 0[cite: 22]
    str_sign_z = "+ %sz" % (coef_z) if coef_z > 0 else "- %sz" % (-coef_z)
    str_eq_d_true = "%sx %s = 0" % (coef_x, str_sign_z)
    # Hệ thức sai cho d
    coef_z_false = coef_z + random.choice([-1, 1])
    if coef_z_false == 0:
        coef_z_false = 2
    str_sign_z_false = (
        "+ %sz" % (coef_z_false) if coef_z_false > 0 else "- %sz" % (-coef_z_false)
    )
    str_eq_d_false = "%sx %s = 0" % (coef_x, str_sign_z_false)
    
    # Nội dung câu hỏi[cite: 22]
    noidungcauhoi = (
        """Trong không gian $Oxyz$, cho vectơ $\\vec{c} = (x;y;z)$ khác $\\vec{0}$ và vuông góc với cả hai vectơ $\\vec{a} = (%s;%s;%s)$ và $\\vec{b} = (%s;%s;%s)$."""
        % (a1, a2, a3, b1, b2, b3)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: a . (a - b) = val_a_amb[cite: 22]
    nb_da_1_d = "\\True $\\vec{a} \\cdot (\\vec{a} - \\vec{b}) = %s$" % (val_a_amb_true)
    nb_da_1_s = "$\\vec{a} \\cdot (\\vec{a} - \\vec{b}) = %s$" % (val_a_amb_false)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ vectơ $\\vec{a} - \\vec{b}$ là: \\\\ $\\vec{a} - \\vec{b} = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Khi đó tích vô hướng: \\\\ $\\vec{a} \\cdot (\\vec{a} - \\vec{b}) = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$."""
        % (
            a1,
            b1,
            a2,
            b2,
            a3,
            b3,
            a1 - b1,
            a2 - b2,
            a3 - b3,
            a1,
            a1 - b1,
            a2,
            a2 - b2,
            a3,
            a3 - b3,
            val_a_amb_true,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Góc giữa hai vectơ a và b là góc tù/nhọn[cite: 22]
    if is_angle_obtuse:
        th_da_1_d = "\\True Góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ là góc tù"
        th_da_1_s = "Góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ là góc nhọn"
    else:
        th_da_1_d = "\\True Góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ là góc nhọn"
        th_da_1_s = "Góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ là góc tù"
    
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có tích vô hướng của hai vectơ $\\vec{a}$ và $\\vec{b}$ là: \\\\ $\\vec{a} \\cdot \\vec{b} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Vì $|\\vec{a}| > 0$ và $|\\vec{b}| > 0$ nên dấu của $\\cos(\\vec{a}, \\vec{b})$ phụ thuộc vào dấu của tích vô hướng: \\\\ $\\cos(\\vec{a}, \\vec{b}) = \\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{a}| \\cdot |\\vec{b}|} %s 0$. \\\\ Do đó góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ là góc %s."""
        % (
            a1,
            b1,
            a2,
            b2,
            a3,
            b3,
            dot_a_b,
            "<" if is_angle_obtuse else ">",
            "tù" if is_angle_obtuse else "nhọn",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: c vuông góc với (2a - b) thì 3x + 4y = 0[cite: 22]
    if is_rel_xy_true:
        vd_da_1_d = "\\True $\\vec{c} \\perp (2\\vec{a} - \\vec{b})$ thì $3x + 4y = 0$"
        vd_da_1_s = "$\\vec{c} \\perp (2\\vec{a} - \\vec{b})$ thì $3x + 4y \\neq 0$"
    else:
        vd_da_1_d = "\\True $\\vec{c} \\perp (2\\vec{a} - \\vec{b})$ luôn đúng với mọi vectơ $\\vec{c}$ vuông góc với $\\vec{a}$ và $\\vec{b}$"
        vd_da_1_s = "$\\vec{c} \\perp (2\\vec{a} - \\vec{b})$ thì $3x + 4y = 0$"
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì vectơ $\\vec{c}$ vuông góc với cả hai vectơ $\\vec{a}$ và $\\vec{b}$ nên ta có: \\\\ $\\begin{cases} \\vec{c} \\cdot \\vec{a} = 0 \\\\ \\vec{c} \\cdot \\vec{b} = 0 \\end{cases}$. \\\\ Xét tích vô hướng của $\\vec{c}$ với $(2\\vec{a} - \\vec{b})$: \\\\ $\\vec{c} \\cdot (2\\vec{a} - \\vec{b}) = 2(\\vec{c} \\cdot \\vec{a}) - (\\vec{c} \\cdot \\vec{b}) = 2 \\cdot 0 - 0 = 0$. \\\\ Như vậy $\\vec{c} \\perp (2\\vec{a} - \\vec{b})$ là một tính chất luôn đúng với mọi vectơ $\\vec{c}$ vuông góc với cả $\\vec{a}$ và $\\vec{b}$. \\\\ Do đó điều kiện $\\vec{c} \\perp (2\\vec{a} - \\vec{b})$ không suy ra đẳng thức $3x + 4y = 0$. Khẳng định này là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: coef_x * x + coef_z * z = 0[cite: 22]
    vdc_da_1_d = "\\True $%s$" % (str_eq_d_true)
    vdc_da_1_s = "$%s$" % (str_eq_d_false)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì $\\vec{c} = (x;y;z) \\neq \\vec{0}$ vuông góc với cả hai vectơ $\\vec{a}$ và $\\vec{b}$ nên $\\vec{c}$ cùng phương với tích có hướng $[\\vec{a}, \\vec{b}]$: \\\\ $[\\vec{a}, \\vec{b}] = \\left( \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix} \\right) = (%s; %s; %s)$. \\\\ Rút gọn vectơ chỉ phương, ta có $\\vec{c}$ cùng phương với vectơ $(%s; %s; %s)$. \\\\ Do đó tồn tại số thực $k \\neq 0$ sao cho: \\\\ $\\begin{cases} x = %s k \\\\ y = %s k \\\\ z = %s k \\end{cases}$. \\\\ Xét mối quan hệ giữa $x$ và $z$: \\\\ Từ $x = %s k \\Rightarrow k = \\frac{x}{%s}$ và $z = %s k \\Rightarrow k = \\frac{z}{%s}$. \\\\ Đồng nhất giá trị $k$, ta được: \\\\ $\\frac{x}{%s} = \\frac{z}{%s} \\Leftrightarrow %sx %s = 0$. \\\\ Do đó mệnh đề là %s."""
        % (
            a2,
            a3,
            b2,
            b3,
            a3,
            a1,
            b3,
            b1,
            a1,
            a2,
            b1,
            b2,
            u1,
            u2,
            u3,
            c_dir1,
            c_dir2,
            c_dir3,
            c_dir1,
            c_dir2,
            c_dir3,
            c_dir1,
            c_dir1,
            c_dir3,
            c_dir3,
            c_dir1,
            c_dir3,
            coef_x,
            str_sign_z,
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
    