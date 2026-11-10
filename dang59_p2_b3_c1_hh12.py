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


def bt_dang59_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A, B, C không thẳng hàng[cite: 23]
    while True:
        xa = random.randint(-2, 3)
        ya = random.randint(-4, 0)
        za = random.randint(4, 8)
    
        # AB có độ dài đẹp hoặc các tọa độ là số chẵn/nguyên[cite: 23]
        ab_x = random.choice([2, 4, -4, 6])
        ab_y = random.choice([4, 6, 8, -6])
        ab_z = random.choice([-4, -2, 2, 4])
    
        xb = xa + ab_x
        yb = ya + ab_y
        zb = za + ab_z
    
        # AC không cùng phương với AB[cite: 23]
        ac_x = random.choice([-5, -4, -3, 3, 5])
        ac_y = random.choice([5, 7, 9, -5])
        ac_z = random.choice([1, 2, 3, -3])
    
        xc = xa + ac_x
        yc = ya + ac_y
        zc = za + ac_z
    
        # BC = AC - AB[cite: 23]
        bc_x = xc - xb
        bc_y = yc - yb
        bc_z = zc - zb
    
        # Tích có hướng [AB, AC] để tính diện tích và kiểm tra tính không thẳng hàng[cite: 23]
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        cp_sq = cp_x**2 + cp_y**2 + cp_z**2
    
        # Độ dài các cạnh
        len_ab_sq = ab_x**2 + ab_y**2 + ab_z**2
        len_ac_sq = ac_x**2 + ac_y**2 + ac_z**2
        len_bc_sq = bc_x**2 + bc_y**2 + bc_z**2
    
        len_ab = math.sqrt(len_ab_sq)
        len_ac = math.sqrt(len_ac_sq)
        len_bc = math.sqrt(len_bc_sq)
        p_perimeter = len_ab + len_ac + len_bc
    
        # Diện tích S_ABC = 1/2 * sqrt(cp_sq)[cite: 23]
        s_abc = Rational(1, 2) * sp.sqrt(cp_sq)
        str_s_true = latex(s_abc)
    
        if (
            cp_sq > 0
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
            and (xb, yb, zb) != (xc, yc, zc)
        ):
            break
    
    # 1. Khẳng định a: Tọa độ vectơ AB[cite: 23]
    ab_false_x = ab_x
    ab_false_y = ab_y + random.choice([-2, 2])
    ab_false_z = ab_z
    
    # 2. Khẳng định b: Ba điểm A, B, C không thẳng hàng (luôn đúng do [AB, AC] != 0)[cite: 23]
    
    # 3. Khẳng định c: Chu vi tam giác ABC là một số lớn hơn / nhỏ hơn bound_p[cite: 23]
    bound_p = round(p_perimeter)
    if bound_p == round(p_perimeter, 2):
        bound_p = math.floor(p_perimeter)
    is_p_gt = p_perimeter > bound_p
    
    # 4. Khẳng định d: S_ABC = ...[cite: 23]
    str_s_false = latex(Rational(1, 2) * sp.sqrt(cp_sq + random.choice([-20, -10, 10, 20])))
    if str_s_false == str_s_true:
        str_s_false = "2\\sqrt{590}"[cite: 23]
    
    # Nội dung câu hỏi[cite: 23]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho ba điểm $A(%s;%s;%s); B(%s;%s;%s); C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Tọa độ vectơ AB[cite: 23]
    nb_da_1_d = "\\True $\\vec{AB} = (%s;%s;%s)$" % (ab_x, ab_y, ab_z)
    nb_da_1_s = "$\\vec{AB} = (%s;%s;%s)$" % (ab_false_x, ab_false_y, ab_false_z)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ của vectơ $\\vec{AB}$ là: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (xb, xa, yb, ya, zb, za, ab_x, ab_y, ab_z)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Ba điểm A, B, C không thẳng hàng[cite: 23]
    th_da_1_d = "\\True Ba điểm $A, B, C$ không thẳng hàng"
    th_da_1_s = "Ba điểm $A, B, C$ thẳng hàng"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (%s;%s;%s)$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Vì $\\frac{%s}{%s} \\neq \\frac{%s}{%s}$ nên hai vectơ $\\vec{AB}$ và $\\vec{AC}$ không cùng phương. \\\\ Do đó ba điểm $A, B, C$ không thẳng hàng."""
        % (
            ab_x,
            ab_y,
            ab_z,
            xc,
            xa,
            yc,
            ya,
            zc,
            za,
            ac_x,
            ac_y,
            ac_z,
            ab_x,
            ac_x,
            ab_y,
            ac_y,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Chu vi tam giác ABC là một số lớn hơn / nhỏ hơn bound_p[cite: 23]
    if is_p_gt:
        vd_da_1_d = (
            "\\True Chu vi của tam giác $ABC$ là một số lớn hơn $%s$ (đơn vị độ dài)"
            % (bound_p)
        )
        vd_da_1_s = (
            "Chu vi của tam giác $ABC$ là một số nhỏ hơn $%s$ (đơn vị độ dài)"
            % (bound_p)
        )
    else:
        vd_da_1_d = (
            "\\True Chu vi của tam giác $ABC$ là một số nhỏ hơn $%s$ (đơn vị độ dài)"
            % (bound_p)
        )
        vd_da_1_s = (
            "Chu vi của tam giác $ABC$ là một số lớn hơn $%s$ (đơn vị độ dài)"
            % (bound_p)
        )
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Độ dài các cạnh của tam giác $ABC$ là: \\\\ $AB = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} \\approx %s$. \\\\ $AC = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} \\approx %s$. \\\\ $BC = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = \\sqrt{%s} \\approx %s$. \\\\ Khi đó chu vi tam giác $ABC$ là: \\\\ $P_{ABC} = AB + AC + BC \\approx %s + %s + %s = %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            ab_x,
            ab_y,
            ab_z,
            len_ab_sq,
            str(round(len_ab, 2)).replace(".", ","),
            ac_x,
            ac_y,
            ac_z,
            len_ac_sq,
            str(round(len_ac, 2)).replace(".", ","),
            xc,
            xb,
            yc,
            yb,
            zc,
            zb,
            len_bc_sq,
            str(round(len_bc, 2)).replace(".", ","),
            str(round(len_ab, 2)).replace(".", ","),
            str(round(len_ac, 2)).replace(".", ","),
            str(round(len_bc, 2)).replace(".", ","),
            str(round(p_perimeter, 2)).replace(".", ","),
            str(round(p_perimeter, 2)).replace(".", ","),
            ">" if is_p_gt else "<",
            bound_p,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: S_ABC = ...[cite: 23]
    vdc_da_1_d = "\\True $S_{ABC} = %s$" % (str_s_true)
    vdc_da_1_s = "$S_{ABC} = %s$" % (str_s_false)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta có tích có hướng của hai vectơ $\\vec{AB}$ và $\\vec{AC}$ là: \\\\ $[\\vec{AB}, \\vec{AC}] = \\left( \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix} \\right) = (%s; %s; %s)$. \\\\ Độ dài của vectơ tích có hướng: \\\\ $\\left|[\\vec{AB}, \\vec{AC}]\\right| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Diện tích tam giác $ABC$ là: \\\\ $S_{ABC} = \\frac{1}{2} \\left|[\\vec{AB}, \\vec{AC}]\\right| = \\frac{1}{2} \\sqrt{%s} = %s$."""
        % (
            ab_y,
            ab_z,
            ac_y,
            ac_z,
            ab_z,
            ab_x,
            ac_z,
            ac_x,
            ab_x,
            ab_y,
            ac_x,
            ac_y,
            cp_x,
            cp_y,
            cp_z,
            cp_x,
            cp_y,
            cp_z,
            cp_sq,
            cp_sq,
            str_s_true,
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
    