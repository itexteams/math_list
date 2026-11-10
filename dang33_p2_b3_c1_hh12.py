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


def bt_dang33_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu tam giác ABC vuông tại A[cite: 22]
    # Tọa độ A, B, C nguyên, AB có độ dài nguyên đẹp
    while True:
        xa = random.randint(-3, 3)
        ya = random.randint(-3, 3)
        za = random.randint(-3, 3)
    
        # Chọn vectơ AB có độ dài là số nguyên đẹp (ví dụ bộ ba Pythagore hoặc các số quen thuộc)[cite: 22]
        ab_triplets = [
            (2, 2, 1),
            (1, 2, 2),
            (2, 1, 2),
            (0, 3, 4),
            (3, 0, 4),
            (4, 3, 0),
            (0, 0, 3),
            (0, 4, 0),
        ]
        u1, u2, u3 = random.choice(ab_triplets)
        s1 = random.choice([-1, 1])
        s2 = random.choice([-1, 1])
        s3 = random.choice([-1, 1])
        ab_x, ab_y, ab_z = u1 * s1, u2 * s2, u3 * s3
    
        xb = xa + ab_x
        yb = ya + ab_y
        zb = za + ab_z
    
        len_ab_sq = ab_x**2 + ab_y**2 + ab_z**2
        len_ab = int(math.isqrt(len_ab_sq))
    
        # Tìm vectơ AC vuông góc với AB: ab_x * ac_x + ab_y * ac_y + ab_z * ac_z = 0[cite: 22]
        # Chọn ac_x, ac_y ngẫu nhiên rồi giải tìm ac_z (nếu chia hết)
        candidates_ac = []
        for cx in range(-3, 4):
            for cy in range(-3, 4):
                rem = -(ab_x * cx + ab_y * cy)
                if ab_z != 0 and rem % ab_z == 0:
                    cz = rem // ab_z
                    if -4 <= cz <= 4 and (cx != 0 or cy != 0 or cz != 0):
                        candidates_ac.append((cx, cy, cz))
                elif ab_z == 0 and rem == 0:
                    for cz in [-2, -1, 1, 2]:
                        if cx != 0 or cy != 0 or cz != 0:
                            candidates_ac.append((cx, cy, cz))
    
        if not candidates_ac:
            continue
    
        ac_x, ac_y, ac_z = random.choice(candidates_ac)
        xc = xa + ac_x
        yc = ya + ac_y
        zc = za + ac_z
    
        len_ac_sq = ac_x**2 + ac_y**2 + ac_z**2
    
        # Vectơ BC[cite: 22]
        bc_x = xc - xb
        bc_y = yc - yb
        bc_z = zc - zb
        len_bc_sq = bc_x**2 + bc_y**2 + bc_z**2
    
        # Đảm bảo tam giác không suy biến và các cạnh khác nhau[cite: 22]
        if (
            len_ac_sq > 0
            and len_ab_sq > 0
            and len_ab_sq + len_ac_sq == len_bc_sq
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
        ):
            break
    
    # 1. Độ dài đoạn thẳng AB = len_ab[cite: 22]
    len_ab_s = len_ab + random.choice([-2, -1, 1, 2])
    
    # 2. Tam giác ABC vuông tại A[cite: 22]
    
    # 3. Điểm N thuộc đoạn BC sao cho S_ABN = 2 * S_ACN[cite: 22]
    # Vì hai tam giác ABN và ACN chung đường cao hạ từ đỉnh A xuống BC nên:
    # S_ABN = 2 * S_ACN <=> BN = 2 * CN <=> vecto BN = 2 * vecto NC[cite: 22]
    # <=> N - B = 2(C - N) <=> 3N = B + 2C <=> N = (B + 2C) / 3[cite: 22]
    xn_num = xb + 2 * xc
    yn_num = yb + 2 * yc
    zn_num = zb + 2 * zc
    
    str_xn = format_fraction_latex(xn_num, 3)
    str_yn = format_fraction_latex(yn_num, 3)
    str_zn = format_fraction_latex(zn_num, 3)
    
    # Tọa độ N sai (nhầm mẫu hoặc nhầm dấu)[cite: 22]
    str_zn_s = format_fraction_latex(zn_num + random.choice([-2, -1, 1, 2]), 3)
    
    # 4. Tứ giác ABDC là hình chữ nhật (do tam giác ABC vuông tại A)[cite: 22]
    # <=> vecto AD = vecto AB + vecto AC <=> D = B + C - A
    xd = xb + xc - xa
    yd = yb + yc - ya
    zd = zb + zc - za
    
    xd_s = xd
    yd_s = yd + random.choice([-2, -1, 1, 2])
    zd_s = zd
    
    # Nội dung câu hỏi[cite: 22]
    noidungcauhoi = (
        """Trong không gian với hệ toạ độ $Oxyz$ cho các điểm $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Độ dài đoạn thẳng AB[cite: 22]
    nb_da_1_d = "\\True Độ dài đoạn thẳng $AB = %s$" % (len_ab)
    nb_da_1_s = "Độ dài đoạn thẳng $AB = %s$" % (len_ab_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ của vectơ $\\vec{AB}$ là: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Khi đó độ dài đoạn thẳng $AB$ là: \\\\ $AB = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$."""
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
    # Khẳng định b: Tam giác ABC là tam giác vuông[cite: 22]
    th_da_1_d = "\\True Tam giác $ABC$ là tam giác vuông"
    th_da_1_s = "Tam giác $ABC$ không phải là tam giác vuông"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (%s;%s;%s) \\Rightarrow AB^2 = (%s)^2 + (%s)^2 + (%s)^2 = %s$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s) \\Rightarrow AC^2 = (%s)^2 + (%s)^2 + (%s)^2 = %s$. \\\\ $\\vec{BC} = (x_C - x_B; y_C - y_B; z_C - z_B) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s) \\Rightarrow BC^2 = (%s)^2 + (%s)^2 + (%s)^2 = %s$. \\\\ Nhận thấy $AB^2 + AC^2 = %s + %s = %s = BC^2$. \\\\ Theo định lí Pythagore đảo, tam giác $ABC$ vuông tại $A$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            ab_x,
            ab_y,
            ab_z,
            len_ab_sq,
            xc,
            xa,
            yc,
            ya,
            zc,
            za,
            ac_x,
            ac_y,
            ac_z,
            ac_x,
            ac_y,
            ac_z,
            len_ac_sq,
            xc,
            xb,
            yc,
            yb,
            zc,
            zb,
            bc_x,
            bc_y,
            bc_z,
            bc_x,
            bc_y,
            bc_z,
            len_bc_sq,
            len_ab_sq,
            len_ac_sq,
            len_bc_sq,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Điểm N thuộc đoạn BC sao cho S_ABN = 2 S_ACN[cite: 22]
    vd_da_1_d = (
        "\\True Điểm $N$ thuộc đoạn $BC$ sao cho $S_{\\Delta ABN} = 2S_{\\Delta ACN}$. Tọa độ điểm $N$ là $N\\left(%s;%s;%s\\right)$"
        % (str_xn, str_yn, str_zn)
    )
    vd_da_1_s = (
        "Điểm $N$ thuộc đoạn $BC$ sao cho $S_{\\Delta ABN} = 2S_{\\Delta ACN}$. Tọa độ điểm $N$ là $N\\left(%s;%s;%s\\right)$"
        % (str_xn, str_yn, str_zn_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Hai tam giác $ABN$ và $ACN$ có chung đường cao kẻ từ đỉnh $A$ xuống cạnh $BC$. \\\\ Do đó ta có tỉ số diện tích: \\\\ $\\frac{S_{\\Delta ABN}}{S_{\\Delta ACN}} = \\frac{BN}{CN} = 2 \\Rightarrow BN = 2 CN$. \\\\ Vì điểm $N$ thuộc đoạn thẳng $BC$ nên hai vectơ $\\vec{BN}$ và $\\vec{NC}$ cùng hướng, suy ra: \\\\ $\\vec{BN} = 2\\vec{NC} \\Leftrightarrow N - B = 2(C - N) \\Leftrightarrow 3N = B + 2C \\Leftrightarrow N = \\frac{B + 2C}{3}$. \\\\ Tọa độ của điểm $N$ là: \\\\ $\\begin{cases} x_N = \\frac{x_B + 2x_C}{3} = \\frac{%s + 2 \\cdot (%s)}{3} = %s \\\\ y_N = \\frac{y_B + 2y_C}{3} = \\frac{%s + 2 \\cdot (%s)}{3} = %s \\\\ z_N = \\frac{z_B + 2z_C}{3} = \\frac{%s + 2 \\cdot (%s)}{3} = %s \\end{cases} \\Rightarrow N\\left(%s;%s;%s\\right)$."""
        % (
            xb,
            xc,
            str_xn,
            yb,
            yc,
            str_yn,
            zb,
            zc,
            str_zn,
            str_xn,
            str_yn,
            str_zn,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Tọa độ điểm D để tứ giác ABDC là hình chữ nhật
    vdc_da_1_d = (
        "\\True Tọa độ điểm $D$ để tứ giác $ABDC$ là hình chữ nhật là $D(%s;%s;%s)$"
        % (xd, yd, zd)
    )
    vdc_da_1_s = (
        "Tọa độ điểm $D$ để tứ giác $ABDC$ là hình chữ nhật là $D(%s;%s;%s)$"
        % (xd_s, yd_s, zd_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì tam giác $ABC$ vuông tại $A$ nên tứ giác $ABDC$ là hình chữ nhật khi và chỉ khi $ABDC$ là hình bình hành. \\\\ Điều này tương đương với: \\\\ $\\vec{AD} = \\vec{AB} + \\vec{AC} \\Leftrightarrow \\begin{cases} x_D - x_A = (x_B - x_A) + (x_C - x_A) \\\\ y_D - y_A = (y_B - y_A) + (y_C - y_A) \\\\ z_D - z_A = (z_B - z_A) + (z_C - z_A) \\end{cases}$ \\\\ $\\Leftrightarrow \\begin{cases} x_D = x_B + x_C - x_A = %s + (%s) - (%s) = %s \\\\ y_D = y_B + y_C - y_A = %s + (%s) - (%s) = %s \\\\ z_D = z_B + z_C - z_A = %s + (%s) - (%s) = %s \\end{cases} \\Rightarrow D(%s;%s;%s)$."""
        % (
            xb,
            xc,
            xa,
            xd,
            yb,
            yc,
            ya,
            yd,
            zb,
            zc,
            za,
            zd,
            xd,
            yd,
            zd,
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
    