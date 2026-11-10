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


def bt_dang48_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu 4 điểm A, B, C, D không đồng phẳng
    while True:
        xa = random.randint(-2, 2)
        ya = random.randint(-1, 2)
        za = random.randint(-1, 2)
    
        xb = random.randint(-3, 2)
        yb = random.randint(-2, 2)
        zb = random.randint(0, 3)
    
        xc = random.randint(-3, 2)
        yc = random.randint(-1, 3)
        zc = random.randint(-2, 2)
    
        xd = random.randint(1, 3)
        yd = random.randint(0, 3)
        zd = random.randint(-3, 1)
    
        # AB, AC, AD
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        ad_x = xd - xa
        ad_y = yd - ya
        ad_z = zd - za
    
        # Tích có hướng [AB, AC]
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        cp_sq = cp_x**2 + cp_y**2 + cp_z**2
    
        # Tích hỗn tạp [AB, AC] . AD để tính thể tích
        mix_prod = cp_x * ad_x + cp_y * ad_y + cp_z * ad_z
    
        if cp_sq > 0 and mix_prod != 0:
            # Rút gọn vectơ pháp tuyến cơ bản của mặt phẳng (ABC)
            gcd_val = math.gcd(math.gcd(abs(cp_x), abs(cp_y)), abs(cp_z))
            u0_x = cp_x // gcd_val
            u0_y = cp_y // gcd_val
            u0_z = cp_z // gcd_val
    
            # Chuẩn hóa dấu để u0_x > 0 nếu có thể
            if u0_x < 0:
                u0_x, u0_y, u0_z = -u0_x, -u0_y, -u0_z
    
            v_val = Rational(abs(mix_prod), 6)
            # Chiều cao h_D = (3 * V_ABCD) / S_ABC = |mix_prod| / sqrt(cp_sq)
            h_d_sq = Rational(mix_prod**2, cp_sq)
            h_d_sym = sp.sqrt(h_d_sq)
    
            break
    
    # 1. Tọa độ vectơ AB
    ab_x_s = ab_x
    ab_y_s = -ab_y if ab_y != 0 else 1
    ab_z_s = ab_z
    
    # 2. Vectơ u = k(u0_x; u0_y; u0_z) cùng vuông góc với AB và AC
    # Vectơ sai (đổi dấu một tọa độ)
    u0_x_s, u0_y_s, u0_z_s = u0_x, -u0_y if u0_y != 0 else u0_y + 1, u0_z
    
    # 3. Thể tích khối tứ diện V_ABCD
    str_v_true = format_fraction_latex(v_val.p, v_val.q)
    bound_v_val = Rational(v_val.p - 1 if v_val.p > 1 else v_val.p + 1, v_val.q)
    str_bound_v = format_fraction_latex(bound_v_val.p, bound_v_val.q)
    is_v_gt = v_val > bound_v_val
    
    # 4. Chiều cao hạ từ đỉnh D: h_D
    str_hd_true = latex(h_d_sym)
    h_d_sym_s = sp.sqrt(Rational(mix_prod**2 + 2, cp_sq))
    str_hd_false = latex(h_d_sym_s)
    if str_hd_false == str_hd_true:
        str_hd_false = "\\frac{2\\sqrt{6}}{3}"
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho bốn điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$ và điểm $D(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc, xd, yd, zd)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Vectơ AB
    nb_da_1_d = "\\True $\\vec{AB} = (%s;%s;%s)$" % (ab_x, ab_y, ab_z)
    nb_da_1_s = "$\\vec{AB} = (%s;%s;%s)$" % (ab_x_s, ab_y_s, ab_z_s)
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
    # Mệnh đề b: Vectơ u vuông góc với cả hai vectơ AB, AC
    th_da_1_d = (
        "\\True Vectơ $\\vec{u} = k(%s;%s;%s)$ vuông góc với cả hai vectơ $\\vec{AB}, \\vec{AC}$"
        % (u0_x, u0_y, u0_z)
    )
    th_da_1_s = (
        "Vectơ $\\vec{u} = k(%s;%s;%s)$ vuông góc với cả hai vectơ $\\vec{AB}, \\vec{AC}$"
        % (u0_x_s, u0_y_s, u0_z_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (%s;%s;%s)$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Tích có hướng của hai vectơ $\\vec{AB}$ và $\\vec{AC}$ là: \\\\ $[\\vec{AB}, \\vec{AC}] = \\left( \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix} \\right) = (%s;%s;%s)$. \\\\ Vectơ cùng vuông góc với cả hai vectơ $\\vec{AB}$ và $\\vec{AC}$ cùng phương với tích có hướng $[\\vec{AB}, \\vec{AC}]$, do đó có dạng: \\\\ $\\vec{u} = k(%s;%s;%s)$ (với $k \\in \\mathbb{R}$)."""
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
            u0_x,
            u0_y,
            u0_z,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Thể tích V_ABCD
    if is_v_gt:
        vd_da_1_d = (
            "\\True $V_{ABCD} > %s$ (đơn vị thể tích)" % (str_bound_v)
        )
        vd_da_1_s = (
            "$V_{ABCD} < %s$ (đơn vị thể tích)" % (str_bound_v)
        )
    else:
        vd_da_1_d = (
            "\\True $V_{ABCD} < %s$ (đơn vị thể tích)" % (str_bound_v)
        )
        vd_da_1_s = (
            "$V_{ABCD} > %s$ (đơn vị thể tích)" % (str_bound_v)
        )
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có tọa độ vectơ $\\vec{AD}$ là: \\\\ $\\vec{AD} = (x_D - x_A; y_D - y_A; z_D - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Tích vô hướng của tích có hướng $[\\vec{AB}, \\vec{AC}]$ với $\\vec{AD}$ là: \\\\ $[\\vec{AB}, \\vec{AC}] \\cdot \\vec{AD} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Khi đó thể tích khối tứ diện $ABCD$ là: \\\\ $V_{ABCD} = \\frac{1}{6} \\left|[\\vec{AB}, \\vec{AC}] \\cdot \\vec{AD}\\right| = \\frac{1}{6} \\cdot |%s| = %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            xd,
            xa,
            yd,
            ya,
            zd,
            za,
            ad_x,
            ad_y,
            ad_z,
            cp_x,
            ad_x,
            cp_y,
            ad_y,
            cp_z,
            ad_z,
            mix_prod,
            mix_prod,
            str_v_true,
            str_v_true,
            ">" if is_v_gt else "<",
            str_bound_v,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Tứ diện ABCD có chiều cao hạ từ đỉnh D là h_D
    vdc_da_1_d = (
        "\\True Tứ diện $ABCD$ có chiều cao hạ từ đỉnh $D$ là $h_D = %s$"
        % (str_hd_true)
    )
    vdc_da_1_s = (
        "Tứ diện $ABCD$ có chiều cao hạ từ đỉnh $D$ là $h_D = %s$"
        % (str_hd_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Diện tích tam giác $ABC$ là: \\\\ $S_{ABC} = \\frac{1}{2} \\left|[\\vec{AB}, \\vec{AC}]\\right| = \\frac{1}{2} \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\frac{\\sqrt{%s}}{2}$. \\\\ Thể tích khối tứ diện $ABCD$ liên hệ với chiều cao $h_D$ và diện tích đáy $S_{ABC}$ theo công thức: \\\\ $V_{ABCD} = \\frac{1}{3} S_{ABC} \\cdot h_D \\Rightarrow h_D = \\frac{3 V_{ABCD}}{S_{ABC}}$. \\\\ Thay số vào, ta được: \\\\ $h_D = \\frac{3 \\cdot %s}{\\frac{\\sqrt{%s}}{2}} = \\frac{|%s|}{\\sqrt{%s}} = %s$."""
        % (
            cp_x,
            cp_y,
            cp_z,
            cp_sq,
            str_v_true,
            cp_sq,
            abs(mix_prod),
            cp_sq,
            str_hd_true,
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
    