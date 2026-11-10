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


def bt_dang47_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A, B, C không thẳng hàng
    while True:
        xa = random.randint(1, 3)
        ya = random.randint(-3, -1)
        za = random.randint(1, 3)
    
        xb = random.randint(-1, 2)
        yb = random.randint(1, 4)
        zb = random.randint(-2, 1)
    
        xc = random.randint(1, 4)
        yc = random.randint(-4, -1)
        zc = random.randint(1, 3)
    
        # AB, AC
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        # Tích có hướng [AB, AC] để tính diện tích
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        cp_sq = cp_x**2 + cp_y**2 + cp_z**2
    
        # Biểu thức T = MA^2 - MB^2 + MC^2 nhỏ nhất:
        # Gọi I là điểm thỏa mãn IA - IB + IC = 0 <=> I = A - B + C
        # Khi đó T = MI^2 + IA^2 - IB^2 + IC^2
        # Biểu thức T nhỏ nhất khi M trùng I
        xi = xa - xb + xc
        yi = ya - yb + yc
        zi = za - zb + zc
    
        # Giá trị biểu thức: x_M^2 - 3*y_M^2 + z_M^2 tại M = I
        val_expr_d = xi**2 - 3 * (yi**2) + zi**2
    
        if (
            cp_sq > 0
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
            and (xb, yb, zb) != (xc, yc, zc)
        ):
            break
    
    # 1. Khoảng cách từ điểm C đến mặt phẳng (Oyz): d(C, (Oyz)) = |xC|
    dist_c_oyz = abs(xc)
    dist_c_oyz_s = dist_c_oyz + random.choice([-1, 1])
    
    # 2. Điểm M thỏa mãn MA + MB = 2MI (với I là trung điểm AB)
    # Hệ thức MA + MB = 2MI luôn đúng với MỌI điểm M trong không gian,
    # do đó M không nhất thiết phải nằm trên một cạnh của tam giác ABC
    
    # 3. Diện tích tam giác ABC: S_ABC = 1/2 * sqrt(cp_sq)
    # Chọn một mốc so sánh sqrt(k_bound)/2
    s_abc_float = 0.5 * math.sqrt(cp_sq)
    bound_sq = cp_sq - random.choice([2, 3, 4]) if cp_sq > 5 else cp_sq + 3
    bound_float = 0.5 * math.sqrt(bound_sq)
    is_s_gt = s_abc_float > bound_float
    
    str_s_bound = "\\frac{\\sqrt{%s}}{2}" % (bound_sq)
    str_s_true = (
        "\\frac{\\sqrt{%s}}{2}" % (cp_sq)
        if sp.sqrt(cp_sq) != int(math.isqrt(cp_sq))
        else str(int(math.isqrt(cp_sq)) // 2)
    )
    
    # 4. Giá trị biểu thức x_M^2 - 3*y_M^2 + z_M^2
    val_expr_d_s = val_expr_d + random.choice([-15, -10, 10, 15])
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Điểm C cách mặt phẳng (Oyz) một khoảng bằng dist_c_oyz
    nb_da_1_d = (
        "\\True Điểm $C(%s;%s;%s)$ cách mặt phẳng $(Oyz)$ một khoảng bằng $%s$"
        % (xc, yc, zc, dist_c_oyz)
    )
    nb_da_1_s = (
        "Điểm $C(%s;%s;%s)$ cách mặt phẳng $(Oyz)$ một khoảng bằng $%s$"
        % (xc, yc, zc, dist_c_oyz_s)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Mặt phẳng tọa độ $(Oyz)$ có phương trình là $x = 0$. \\\\ Khoảng cách từ điểm $C(%s;%s;%s)$ đến mặt phẳng $(Oyz)$ là: \\\\ $d(C, (Oyz)) = |x_C| = |%s| = %s$."""
        % (
            xc,
            yc,
            zc,
            xc,
            dist_c_oyz,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Điểm M thỏa mãn MA + MB = 2MI thì M nằm trên một cạnh của tam giác ABC
    th_da_1_d = (
        "\\True Điểm $M$ thỏa mãn $\\vec{MA} + \\vec{MB} = 2\\vec{MI}$ (với $I$ là trung điểm của $AB$) luôn đúng với mọi điểm $M$ trong không gian"
    )
    th_da_1_s = (
        "Điểm $M$ thỏa mãn $\\vec{MA} + \\vec{MB} = 2\\vec{MI}$ (với $I$ là trung điểm của $AB$) thì $M$ nằm trên một cạnh của tam giác $ABC$"
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Với $I$ là trung điểm của đoạn thẳng $AB$, ta có $\\vec{IA} + \\vec{IB} = \\vec{0}$. \\\\ Khi đó với mọi điểm $M$ bất kỳ trong không gian, ta luôn có: \\\\ $\\vec{MA} + \\vec{MB} = (\\vec{MI} + \\vec{IA}) + (\\vec{MI} + \\vec{IB}) = 2\\vec{MI} + (\\vec{IA} + \\vec{IB}) = 2\\vec{MI}$. \\\\ Đẳng thức này là một đồng nhất thức đúng với mọi điểm $M$, do đó điểm $M$ không nhất thiết phải nằm trên một cạnh của tam giác $ABC$."""
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: S_ABC > \frac{\sqrt{bound_sq}}{2}
    if is_s_gt:
        vd_da_1_d = "\\True $S_{ABC} > %s$" % (str_s_bound)
        vd_da_1_s = "$S_{ABC} < %s$" % (str_s_bound)
    else:
        vd_da_1_d = "\\True $S_{ABC} < %s$" % (str_s_bound)
        vd_da_1_s = "$S_{ABC} > %s$" % (str_s_bound)
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Tích có hướng của hai vectơ $\\vec{AB}$ và $\\vec{AC}$ là: \\\\ $[\\vec{AB}, \\vec{AC}] = \\left( \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix} \\right) = (%s;%s;%s)$. \\\\ Độ dài của vectơ tích có hướng là: \\\\ $\\left|[\\vec{AB}, \\vec{AC}]\\right| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Diện tích tam giác $ABC$ là: \\\\ $S_{ABC} = \\frac{1}{2} \\left|[\\vec{AB}, \\vec{AC}]\\right| = \\frac{\\sqrt{%s}}{2}$. \\\\ Vì $%s %s %s$ nên $\\frac{\\sqrt{%s}}{2} %s %s$, do đó mệnh đề là %s."""
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
            cp_x,
            cp_y,
            cp_z,
            cp_sq,
            cp_sq,
            cp_sq,
            ">" if is_s_gt else "<",
            bound_sq,
            cp_sq,
            ">" if is_s_gt else "<",
            str_s_bound,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Điểm M thỏa mãn T = MA^2 - MB^2 + MC^2 nhỏ nhất thì x_M^2 - 3*y_M^2 + z_M^2 = val_expr_d
    vdc_da_1_d = (
        "\\True Điểm $M$ thỏa mãn $T = MA^2 - MB^2 + MC^2$ nhỏ nhất thì $x_M^2 - 3y_M^2 + z_M^2 = %s$"
        % (val_expr_d)
    )
    vdc_da_1_s = (
        "Điểm $M$ thỏa mãn $T = MA^2 - MB^2 + MC^2$ nhỏ nhất thì $x_M^2 - 3y_M^2 + z_M^2 = %s$"
        % (val_expr_d_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Gọi điểm $I$ thỏa mãn hệ thức vectơ $\\vec{IA} - \\vec{IB} + \\vec{IC} = \\vec{0} \\Leftrightarrow \\vec{OI} = \\vec{OA} - \\vec{OB} + \\vec{OC}$. \\\\ Tọa độ của điểm $I$ là: \\\\ $\\begin{cases} x_I = x_A - x_B + x_C = %s - (%s) + (%s) = %s \\\\ y_I = y_A - y_B + y_C = %s - (%s) + (%s) = %s \\\\ z_I = z_A - z_B + z_C = %s - (%s) + (%s) = %s \\end{cases} \\Rightarrow I(%s;%s;%s)$. \\\\ Biến đổi biểu thức $T$: \\\\ $T = (\\vec{MI} + \\vec{IA})^2 - (\\vec{MI} + \\vec{IB})^2 + (\\vec{MI} + \\vec{IC})^2$ \\\\ $= MI^2 + 2\\vec{MI} \\cdot (\\vec{IA} - \\vec{IB} + \\vec{IC}) + IA^2 - IB^2 + IC^2 = MI^2 + IA^2 - IB^2 + IC^2$. \\\\ Do $IA^2 - IB^2 + IC^2$ không đổi nên biểu thức $T$ đạt giá trị nhỏ nhất khi và chỉ khi $MI = 0 \\Leftrightarrow M \\equiv I(%s;%s;%s)$. \\\\ Khi đó tọa độ của điểm $M$ là $x_M = %s, y_M = %s, z_M = %s$. \\\\ Giá trị của biểu thức là: \\\\ $x_M^2 - 3y_M^2 + z_M^2 = (%s)^2 - 3 \\cdot (%s)^2 + (%s)^2 = %s - 3 \\cdot (%s) + %s = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            xa,
            xb,
            xc,
            xi,
            ya,
            yb,
            yc,
            yi,
            za,
            zb,
            zc,
            zi,
            xi,
            yi,
            zi,
            xi,
            yi,
            zi,
            xi,
            yi,
            zi,
            xi,
            yi,
            zi,
            xi**2,
            yi**2,
            zi**2,
            val_expr_d,
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
    