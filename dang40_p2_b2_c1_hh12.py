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


def bt_dang40_p2_b2_c1_hh12(self):
    # Sinh ngẫu nhiên dữ liệu tam giác ABC sao cho cos B, sin B và diện tích có dạng căn thức đẹp
    while True:
        xa = random.randint(-3, 3)
        ya = random.randint(-3, 3)
        za = random.randint(-3, 3)
    
        # Chọn vectơ BA và BC sao cho góc nhọn và độ dài đẹp
        ba_x = random.choice([-2, -1, 1, 2])
        ba_y = random.choice([-2, -1, 1, 2])
        ba_z = random.choice([-2, -1, 1, 2])
    
        bc_x = random.choice([-3, -2, 2, 3])
        bc_y = random.choice([-2, -1, 1, 2])
        bc_z = random.choice([-2, -1, 1, 2])
    
        # Tọa độ điểm B và C
        xb = xa - ba_x
        yb = ya - ba_y
        zb = za - ba_z
    
        xc = xb + bc_x
        yc = yb + bc_y
        zc = zb + bc_z
    
        # Tích vô hướng BA . BC và tích có hướng [BA, BC]
        dot_ba_bc = ba_x * bc_x + ba_y * bc_y + ba_z * bc_z
    
        cp_x = ba_y * bc_z - ba_z * bc_y
        cp_y = ba_z * bc_x - ba_x * bc_z
        cp_z = ba_x * bc_y - ba_y * bc_x
    
        len_ba_sq = ba_x**2 + ba_y**2 + ba_z**2
        len_bc_sq = bc_x**2 + bc_y**2 + bc_z**2
        cp_sq = cp_x**2 + cp_y**2 + cp_z**2
    
        # Yêu cầu góc B nhọn (dot > 0), không thẳng hàng (cp_sq > 0)
        if dot_ba_bc > 0 and cp_sq > 0:
            # Chọn tỉ số đáy k = AD / BC là số nguyên (k = 2 hoặc k = 3)
            k_val = random.choice([2, 3])
    
            # Diện tích tam giác ABC: S_ABC = 1/2 * sqrt(cp_sq)
            # Diện tích hình thang ABCD: S_ABCD = (k_val + 1) * S_ABC
            s_abc_sym = sp.Rational(1, 2) * sp.sqrt(cp_sq)
            s_abcd_sym = (k_val + 1) * s_abc_sym
            str_s_abcd = latex(s_abcd_sym)
    
            # Tính toán cos B và sin B
            cos_b_sym = sp.Rational(dot_ba_bc, 1) / (
                sp.sqrt(len_ba_sq) * sp.sqrt(len_bc_sq)
            )
            sin_b_sym = sp.sqrt(cp_sq) / (sp.sqrt(len_ba_sq) * sp.sqrt(len_bc_sq))
    
            str_cos_b = latex(cos_b_sym)
            str_sin_b = latex(sin_b_sym)
    
            # Vectơ AB = - BA
            ab_x = -ba_x
            ab_y = -ba_y
            ab_z = -ba_z
    
            # Tọa độ đỉnh D: AD = k_val * BC => D = A + k_val * BC
            xd = xa + k_val * bc_x
            yd = ya + k_val * bc_y
            zd = za + k_val * bc_z
    
            sum_d_sq = xd**2 + yd**2 + zd**2
            break
    
    # 1. Vectơ AB sai
    ab_x_s = -ab_x
    ab_y_s = ab_y
    ab_z_s = ab_z
    
    # 2. Giá trị cos B, sin B sai
    cos_b_sym_s = sp.Rational(dot_ba_bc + 1, 1) / (
        sp.sqrt(len_ba_sq) * sp.sqrt(len_bc_sq)
    )
    str_cos_b_s = latex(cos_b_sym_s)
    str_sin_b_s = latex(sin_b_sym)
    
    # 3. Mệnh đề c: Vectơ AD = k_val * BC
    k_val_s = k_val + 1 if k_val == 2 else k_val - 1
    
    # 4. Giá trị a^2 + b^2 + c^2 sai
    sum_d_sq_s = sum_d_sq + random.choice([-10, 10, -20, 20])
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho hình thang $ABCD (AD // BC)$ có diện tích bằng $%s$ và có tọa độ ba đỉnh là $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$. Gọi $H$ là hình chiếu của $A$ lên $BC$."""
        % (str_s_abcd, xa, ya, za, xb, yb, zb, xc, yc, zc)
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
    # Mệnh đề b: cos B, sin B
    th_da_1_d = "\\True $\\cos B = %s, \\sin B = %s$" % (str_cos_b, str_sin_b)
    th_da_1_s = "$\\cos B = %s, \\sin B = %s$" % (str_cos_b_s, str_sin_b_s)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có $\\vec{BA} = (%s;%s;%s) \\Rightarrow BA = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $\\vec{BC} = (x_C - x_B; y_C - y_B; z_C - z_B) = (%s;%s;%s) \\Rightarrow BC = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Tích vô hướng của hai vectơ: \\\\ $\\vec{BA} \\cdot \\vec{BC} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Do đó ta có: \\\\ $\\cos B = \\frac{\\vec{BA} \\cdot \\vec{BC}}{|\\vec{BA}| \\cdot |\\vec{BC}|} = \\frac{%s}{\\sqrt{%s} \\cdot \\sqrt{%s}} = %s$. \\\\ Vì góc $B$ của tam giác thỏa mãn $0^\\circ < B < 180^\\circ$ nên $\\sin B > 0$, suy ra: \\\\ $\\sin B = \\sqrt{1 - \\cos^2 B} = %s$."""
        % (
            ba_x,
            ba_y,
            ba_z,
            ba_x,
            ba_y,
            ba_z,
            len_ba_sq,
            bc_x,
            bc_y,
            bc_z,
            bc_x,
            bc_y,
            bc_z,
            len_bc_sq,
            ba_x,
            bc_x,
            ba_y,
            bc_y,
            ba_z,
            bc_z,
            dot_ba_bc,
            dot_ba_bc,
            len_ba_sq,
            len_bc_sq,
            str_cos_b,
            str_sin_b,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Vectơ AD = k_val * BC
    vd_da_1_d = "\\True $\\vec{AD} = %s\\vec{BC}$" % (k_val)
    vd_da_1_s = "$\\vec{AD} = %s\\vec{BC}$" % (k_val_s)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    str_s_abc = latex(s_abc_sym)
    
    loigiai_vd_1 = (
        """Diện tích tam giác $ABC$ là: \\\\ $S_{ABC} = \\frac{1}{2} BA \\cdot BC \\cdot \\sin B = \\frac{1}{2} \\cdot \\sqrt{%s} \\cdot \\sqrt{%s} \\cdot %s = %s$. \\\\ Chiều cao của hình thang $ABCD$ chính là độ dài đoạn vuông góc $AH$: \\\\ $AH = \\frac{2S_{ABC}}{BC} = \\frac{2 \\cdot %s}{\\sqrt{%s}}$. \\\\ Diện tích hình thang $ABCD$ bằng $%s$, mặt khác: \\\\ $S_{ABCD} = \\frac{(AD + BC) \\cdot AH}{2} = \\frac{AD + BC}{BC} \\cdot S_{ABC} \\Leftrightarrow %s = \\left(1 + \\frac{AD}{BC}\\right) \\cdot %s \\Leftrightarrow \\frac{AD}{BC} = %s$. \\\\ Vì $ABCD$ là hình thang với hai đáy $AD // BC$ nên hai vectơ $\\vec{AD}$ và $\\vec{BC}$ cùng hướng. \\\\ Do đó ta có đẳng thức vectơ: $\\vec{AD} = %s\\vec{BC}$."""
        % (
            len_ba_sq,
            len_bc_sq,
            str_sin_b,
            str_s_abc,
            str_s_abc,
            len_bc_sq,
            str_s_abcd,
            str_s_abcd,
            str_s_abc,
            k_val,
            k_val,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Giả sử D(a; b; c), khi đó a^2 + b^2 + c^2 = sum_d_sq
    vdc_da_1_d = (
        "\\True Giả sử $D(a;b;c)$, khi đó $a^2 + b^2 + c^2 = %s$" % (sum_d_sq)
    )
    vdc_da_1_s = "Giả sử $D(a;b;c)$, khi đó $a^2 + b^2 + c^2 = %s$" % (sum_d_sq_s)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Từ hệ thức $\\vec{AD} = %s\\vec{BC}$, với $\\vec{BC} = (%s;%s;%s)$, suy ra: \\\\ $\\vec{AD} = %s \\cdot (%s;%s;%s) = (%s;%s;%s)$. \\\\ Gọi tọa độ điểm $D$ là $D(a;b;c)$, ta có: \\\\ $\\vec{AD} = (a - x_A; b - y_A; c - z_A) = (a - (%s); b - (%s); c - (%s))$. \\\\ Do đó: \\\\ $\\begin{cases} a - (%s) = %s \\\\ b - (%s) = %s \\\\ c - (%s) = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s + (%s) = %s \\\\ b = %s + (%s) = %s \\\\ c = %s + (%s) = %s \\end{cases} \\Rightarrow D(%s;%s;%s)$. \\\\ Khi đó giá trị của biểu thức $a^2 + b^2 + c^2$ là: \\\\ $a^2 + b^2 + c^2 = (%s)^2 + (%s)^2 + (%s)^2 = %s + %s + %s = %s$."""
        % (
            k_val,
            bc_x,
            bc_y,
            bc_z,
            k_val,
            bc_x,
            bc_y,
            bc_z,
            k_val * bc_x,
            k_val * bc_y,
            k_val * bc_z,
            xa,
            ya,
            za,
            xa,
            k_val * bc_x,
            ya,
            k_val * bc_y,
            za,
            k_val * bc_z,
            xa,
            k_val * bc_x,
            xd,
            ya,
            k_val * bc_y,
            yd,
            za,
            k_val * bc_z,
            zd,
            xd,
            yd,
            zd,
            xd,
            yd,
            zd,
            xd**2,
            yd**2,
            zd**2,
            sum_d_sq,
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
    