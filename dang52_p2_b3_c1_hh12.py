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


def bt_dang52_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu bốn điểm A, B, C, D[cite: 21]
    # Đảm bảo:
    # 1. |AB| là số nguyên đẹp (ví dụ |AB| = 3 từ bộ 2^2 + 2^2 + 1^2 = 9)[cite: 21]
    # 2. Tam giác ABC vuông hoặc không vuông tại A[cite: 21]
    # 3. cos(AB, CD) có giá trị phân số tối giản đẹp[cite: 21]
    while True:
        xa = random.randint(-2, 2)
        ya = random.randint(-2, 2)
        za = random.randint(-1, 3)
    
        # Chọn AB có độ dài bằng 3 từ hoán vị và dấu của (2, 2, 1)[cite: 21]
        ab_components = [2, 2, 1]
        random.shuffle(ab_components)
        s_ab = [random.choice([-1, 1]), random.choice([-1, 1]), random.choice([-1, 1])]
        ab_x = ab_components[0] * s_ab[0]
        ab_y = ab_components[1] * s_ab[1]
        ab_z = ab_components[2] * s_ab[2]
    
        xb = xa + ab_x
        yb = ya + ab_y
        zb = za + ab_z
    
        len_ab_sq = ab_x**2 + ab_y**2 + ab_z**2
        len_ab = int(math.isqrt(len_ab_sq))
    
        # Chọn điểm C[cite: 21]
        xc = random.randint(-2, 3)
        yc = random.randint(-1, 4)
        zc = random.randint(-1, 3)
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
        len_ac_sq = ac_x**2 + ac_y**2 + ac_z**2
    
        # Tích vô hướng AB . AC (kiểm tra tính vuông góc của tam giác ABC tại A)[cite: 21]
        dot_ab_ac = ab_x * ac_x + ab_y * ac_y + ab_z * ac_z
    
        # Chọn điểm D sao cho CD có độ dài nguyên đẹp hoặc tính cos(AB, CD) hữu tỉ đẹp[cite: 21]
        # Ví dụ CD có các thành phần từ (2, 2, 1) để |CD| = 3[cite: 21]
        cd_components = [2, 2, 1]
        random.shuffle(cd_components)
        s_cd = [random.choice([-1, 1]), random.choice([-1, 1]), random.choice([-1, 1])]
        cd_x = cd_components[0] * s_cd[0]
        cd_y = cd_components[1] * s_cd[1]
        cd_z = cd_components[2] * s_cd[2]
    
        xd = xc + cd_x
        yd = yc + cd_y
        zd = zc + cd_z
    
        len_cd_sq = cd_x**2 + cd_y**2 + cd_z**2
        len_cd = int(math.isqrt(len_cd_sq))
    
        # Tích vô hướng AB . CD[cite: 21]
        dot_ab_cd = ab_x * cd_x + ab_y * cd_y + ab_z * cd_z
    
        if (
            len_ac_sq > 0
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
            and (xc, yc, zc) != (xd, yd, zd)
            and dot_ab_cd != 0
        ):
            break
    
    # 1. Khẳng định a: |AB| = len_ab[cite: 21]
    len_ab_s = len_ab + random.choice([-1, 1])
    
    # 2. Khẳng định b: Tích vô hướng AB . CD[cite: 21]
    dot_ab_cd_true = dot_ab_cd
    dot_ab_cd_false = dot_ab_cd + random.choice([-2, -1, 1, 2])
    
    # 3. Khẳng định c: Tam giác ABC vuông tại A[cite: 21]
    is_right_at_a = dot_ab_ac == 0
    
    # 4. Khẳng định d: cos(AB, CD)[cite: 21]
    # cos(AB, CD) = (AB . CD) / (|AB| * |CD|)[cite: 21]
    cos_val = Rational(dot_ab_cd, len_ab * len_cd)
    str_cos_true = format_fraction_latex(cos_val.p, cos_val.q)
    cos_val_false = Rational(dot_ab_cd + 1, len_ab * len_cd)
    str_cos_false = format_fraction_latex(cos_val_false.p, cos_val_false.q)
    if str_cos_false == str_cos_true:
        str_cos_false = "\\frac{2}{9}"
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s), D(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc, xd, yd, zd)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: |AB|[cite: 21]
    nb_da_1_d = "\\True $|\\vec{AB}| = %s$" % (len_ab)
    nb_da_1_s = "$|\\vec{AB}| = %s$" % (len_ab_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ vectơ $\\vec{AB}$ là: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Khi đó độ dài của vectơ $\\vec{AB}$ là: \\\\ $|\\vec{AB}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$."""
        % (
            xb,
            xa,
            yb,
            ya,
            zb,
            za,
            ab_x,
            ab_y,
            ab_z,
            ab_x,
            ab_y,
            ab_z,
            len_ab_sq,
            len_ab,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: AB . CD[cite: 21]
    th_da_1_d = "\\True $\\vec{AB} \\cdot \\vec{CD} = %s$" % (dot_ab_cd_true)
    th_da_1_s = "$\\vec{AB} \\cdot \\vec{CD} = %s$" % (dot_ab_cd_false)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có tọa độ vectơ $\\vec{CD}$ là: \\\\ $\\vec{CD} = (x_D - x_C; y_D - y_C; z_D - z_C) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Kết hợp với $\\vec{AB} = (%s;%s;%s)$, ta có tích vô hướng: \\\\ $\\vec{AB} \\cdot \\vec{CD} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$."""
        % (
            xd,
            xc,
            yd,
            yc,
            zd,
            zc,
            cd_x,
            cd_y,
            cd_z,
            ab_x,
            ab_y,
            ab_z,
            ab_x,
            cd_x,
            ab_y,
            cd_y,
            ab_z,
            cd_z,
            dot_ab_cd_true,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Tam giác ABC vuông tại A[cite: 21]
    if is_right_at_a:
        vd_da_1_d = "\\True Tam giác $ABC$ vuông góc tại $A$"
        vd_da_1_s = "Tam giác $ABC$ không vuông góc tại $A$"
    else:
        vd_da_1_d = "\\True Tam giác $ABC$ không vuông góc tại $A$"
        vd_da_1_s = "Tam giác $ABC$ vuông góc tại $A$"
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (%s;%s;%s)$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Tích vô hướng của hai vectơ $\\vec{AB}$ và $\\vec{AC}$ là: \\\\ $\\vec{AB} \\cdot \\vec{AC} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Vì $\\vec{AB} \\cdot \\vec{AC} = %s %s 0$ nên hai vectơ $\\vec{AB}$ và $\\vec{AC}$ %s. \\\\ Do đó tam giác $ABC$ %s."""
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
            ab_z,
            ac_z,
            dot_ab_ac,
            dot_ab_ac,
            "=" if is_right_at_a else "\\neq",
            "vuông góc với nhau" if is_right_at_a else "không vuông góc với nhau",
            "vuông góc tại $A$" if is_right_at_a else "không vuông góc tại $A$",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: cos(AB, CD)[cite: 21]
    vdc_da_1_d = (
        "\\True $\\cos(\\vec{AB}, \\vec{CD}) = %s$" % (str_cos_true)
    )
    vdc_da_1_s = (
        "$\\cos(\\vec{AB}, \\vec{CD}) = %s$" % (str_cos_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta có độ dài của các vectơ là: \\\\ $|\\vec{AB}| = %s$. \\\\ $|\\vec{CD}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$. \\\\ Tích vô hướng của hai vectơ: $\\vec{AB} \\cdot \\vec{CD} = %s$. \\\\ Khi đó côsin của góc giữa hai vectơ $\\vec{AB}$ và $\\vec{CD}$ là: \\\\ $\\cos(\\vec{AB}, \\vec{CD}) = \\frac{\\vec{AB} \\cdot \\vec{CD}}{|\\vec{AB}| \\cdot |\\vec{CD}|} = \\frac{%s}{%s \\cdot %s} = %s$."""
        % (
            len_ab,
            cd_x,
            cd_y,
            cd_z,
            len_cd_sq,
            len_cd,
            dot_ab_cd_true,
            dot_ab_cd_true,
            len_ab,
            len_cd,
            str_cos_true,
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
    