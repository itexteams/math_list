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


def bt_dang70_p2_b3_c1_hh12(self):
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
        xa = 0  # Giữ cấu trúc hoành độ bằng 0 như đề gốc[cite: 23]
        ya = random.randint(1, 4)
        za = random.randint(1, 3)
    
        xb = random.choice([2, 4, 6])
        yb = 0  # Giữ tung độ bằng 0 như đề gốc[cite: 23]
        zb = random.choice([1, 2, 3])
    
        xc = random.randint(1, 3)
        yc = random.randint(2, 5)
        zc = random.randint(-3, -1)
    
        # Kiểm tra 3 điểm không thẳng hàng[cite: 23]
        ab_x, ab_y, ab_z = xb - xa, yb - ya, zb - za
        ac_x, ac_y, ac_z = xc - xa, yc - ya, zc - za
    
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        if cp_x != 0 or cp_y != 0 or cp_z != 0:
            # Độ dài các cạnh AB, BC, CA[cite: 23]
            ab_sq = ab_x**2 + ab_y**2 + ab_z**2
            bc_sq = (xc - xb) ** 2 + (yc - yb) ** 2 + (zc - zb) ** 2
            ca_sq = ac_x**2 + ac_y**2 + ac_z**2
    
            # Điểm M thỏa mãn MA + 3*MB = 0 <=> M = (A + 3*B)/4[cite: 23]
            xm_num = xa + 3 * xb
            ym_num = ya + 3 * yb
            zm_num = za + 3 * zb
    
            # Trung điểm của BC: I_bc = (B + C)/2[cite: 23]
            x_ibc_num = xb + xc
            y_ibc_num = yb + yc
            z_ibc_num = zb + zc
    
            break
    
    # 1. Khẳng định a: Tọa độ trung điểm của BC[cite: 23]
    str_x_ibc = format_fraction_latex(x_ibc_num, 2)
    str_y_ibc = format_fraction_latex(y_ibc_num, 2)
    str_z_ibc = format_fraction_latex(z_ibc_num, 2)
    
    # Tạo phương án sai cho trung điểm BC (ví dụ nhầm tung độ thành 0 như mẫu gốc)[cite: 23]
    str_y_ibc_false = "0" if str_y_ibc != "0" else "1"
    
    # 2. Khẳng định b: Hình chiếu của A lên trục Oy là điểm I(0; ya; 0)[cite: 23]
    ya_false = ya + random.choice([-1, 1])
    
    # 3. Khẳng định c: MA + 3*MB = 0 thì tọa độ điểm M là ((xa+3xb)/4; (ya+3yb)/4; (za+3zb)/4)[cite: 23]
    str_xm = format_fraction_latex(xm_num, 4)
    str_ym = format_fraction_latex(ym_num, 4)
    str_zm = format_fraction_latex(zm_num, 4)
    
    # Tạo phương án sai (ví dụ chia nhầm mẫu cho 3 thay vì 4 như đề gốc)[cite: 23]
    str_zm_false = format_fraction_latex(zm_num, 3)
    
    # 4. Khẳng định d: Chu vi tam giác ABC bằng AB + BC + CA[cite: 23]
    len_ab_sym = sp.sqrt(ab_sq)
    len_bc_sym = sp.sqrt(bc_sq)
    len_ca_sym = sp.sqrt(ca_sq)
    
    str_p_true = "%s + %s + %s" % (
        latex(len_bc_sym),
        latex(len_ca_sym),
        latex(len_ab_sym),
    )
    # Tạo giá trị sai cho chu vi tam giác ABC[cite: 23]
    str_p_false = "%s + %s + %s" % (
        latex(sp.sqrt(bc_sq + 2)),
        latex(len_ca_sym),
        latex(len_ab_sym),
    )
    if str_p_false == str_p_true:
        str_p_false = "\\sqrt{29} + \\sqrt{17} + 3\\sqrt{2}"[cite: 23]
    
    # Nội dung câu hỏi[cite: 23]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho tam giác $ABC$ có $A(%s;%s;%s), B(%s;%s;%s)$ và $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Tọa độ trung điểm của BC[cite: 23]
    nb_da_1_d = (
        "\\True Tọa độ trung điểm của $BC$ là $\\left(%s;%s;%s\\right)$"
        % (str_x_ibc, str_y_ibc, str_z_ibc)
    )
    nb_da_1_s = (
        "Tọa độ trung điểm của $BC$ là $\\left(%s;%s;%s\\right)$"
        % (str_x_ibc, str_y_ibc_false, str_z_ibc)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Gọi $N$ là trung điểm của đoạn thẳng $BC$. \\\\ Tọa độ điểm $N$ được tính theo công thức: \\\\ $\\begin{cases} x_N = \\frac{x_B + x_C}{2} = \\frac{%s + (%s)}{2} = %s \\\\ y_N = \\frac{y_B + y_C}{2} = \\frac{%s + (%s)}{2} = %s \\\\ z_N = \\frac{z_B + z_C}{2} = \\frac{%s + (%s)}{2} = %s \\end{cases} \\Rightarrow N\\left(%s;%s;%s\\right)$. \\\\ Do đó khẳng định là %s."""
        % (
            xb,
            xc,
            str_x_ibc,
            yb,
            yc,
            str_y_ibc,
            zb,
            zc,
            str_z_ibc,
            str_x_ibc,
            str_y_ibc,
            str_z_ibc,
            "đúng" if "\\True" in nb_da_1 else "sai",
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Hình chiếu của điểm A lên trục Oy[cite: 23]
    th_da_1_d = (
        "\\True Hình chiếu của điểm $A$ lên trục $Oy$ là $I(0;%s;0)$" % (ya)
    )
    th_da_1_s = (
        "Hình chiếu của điểm $A$ lên trục $Oy$ là $I(0;%s;0)$" % (ya_false)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Hình chiếu vuông góc của điểm $A(x_A; y_A; z_A) = (%s;%s;%s)$ lên trục tung $Oy$ giữ nguyên tung độ và có hoành độ, cao độ bằng $0$. \\\\ Suy ra tọa độ hình chiếu là điểm $I(0;%s;0)$. \\\\ Do đó mệnh đề là %s."""
        % (
            xa,
            ya,
            za,
            ya,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: MA + 3*MB = 0 thì tọa độ điểm M[cite: 23]
    vd_da_1_d = (
        "\\True $\\vec{MA} + 3\\vec{MB} = \\vec{0}$ thì tọa độ điểm $M\\left(%s;%s;%s\\right)$"
        % (str_xm, str_ym, str_zm)
    )
    vd_da_1_s = (
        "$\\vec{MA} + 3\\vec{MB} = \\vec{0}$ thì tọa độ điểm $M\\left(%s;%s;%s\\right)$"
        % (str_xm, str_ym, str_zm_false)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có hệ thức vectơ: \\\\ $\\vec{MA} + 3\\vec{MB} = \\vec{0} \\Leftrightarrow (\\vec{OA} - \\vec{OM}) + 3(\\vec{OB} - \\vec{OM}) = \\vec{0}$ \\\\ $\\Leftrightarrow 4\\vec{OM} = \\vec{OA} + 3\\vec{OB} \\Leftrightarrow \\vec{OM} = \\frac{\\vec{OA} + 3\\vec{OB}}{4}$. \\\\ Tọa độ điểm $M$ thỏa mãn: \\\\ $\\begin{cases} x_M = \\frac{x_A + 3x_B}{4} = \\frac{%s + 3 \\cdot (%s)}{4} = %s \\\\ y_M = \\frac{y_A + 3y_B}{4} = \\frac{%s + 3 \\cdot (%s)}{4} = %s \\\\ z_M = \\frac{z_A + 3z_B}{4} = \\frac{%s + 3 \\cdot (%s)}{4} = %s \\end{cases} \\Rightarrow M\\left(%s;%s;%s\\right)$. \\\\ Do đó mệnh đề là %s."""
        % (
            xa,
            xb,
            str_xm,
            ya,
            yb,
            str_ym,
            za,
            zb,
            str_zm,
            str_xm,
            str_ym,
            str_zm,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Chu vi tam giác ABC bằng str_p_true[cite: 23]
    vdc_da_1_d = "\\True Chu vi tam giác $ABC$ bằng $%s$" % (str_p_true)
    vdc_da_1_s = "Chu vi tam giác $ABC$ bằng $%s$" % (str_p_false)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Độ dài các cạnh của tam giác $ABC$ là: \\\\ $AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$. \\\\ $BC = \\sqrt{(x_C - x_B)^2 + (y_C - y_B)^2 + (z_C - z_B)^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$. \\\\ $CA = \\sqrt{(x_A - x_C)^2 + (y_A - y_C)^2 + (z_A - z_C)^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$. \\\\ Khi đó chu vi tam giác $ABC$ là: \\\\ $P = AB + BC + CA = %s + %s + %s = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            ab_x,
            ab_y,
            ab_z,
            ab_sq,
            latex(len_ab_sym),
            xc - xb,
            yc - yb,
            zc - zb,
            bc_sq,
            latex(len_bc_sym),
            xa - xc,
            ya - yc,
            za - zc,
            ca_sq,
            latex(len_ca_sym),
            latex(len_ab_sym),
            latex(len_bc_sym),
            latex(len_ca_sym),
            str_p_true,
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
    