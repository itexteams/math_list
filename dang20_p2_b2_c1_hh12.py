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


def bt_dang20_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A, B, C sao cho hình thang cân ABCD có đỉnh D tọa độ nguyên đẹp
    while True:
        ux = random.choice([-2, 2])
        uy = random.choice([-1, 1])
        uz = random.choice([-2, 2])
    
        ab_x = 2 * ux
        ab_y = 2 * uy
        ab_z = 2 * uz
    
        xa = random.randint(-3, 3)
        ya = random.randint(-3, 3)
        za = random.randint(-3, 3)
    
        xb = xa + ab_x
        yb = ya + ab_y
        zb = za + ab_z
    
        vx = random.choice([-5, -3, -2, 2, 3, 5])
        vy = random.choice([-3, -2, 0, 1, 2, 3])
        vz = random.choice([-4, -3, 3, 4])
    
        # Kiểm tra vectơ BC = v không cùng phương với AB
        cp1 = ab_y * vz - ab_z * vy
        cp2 = ab_z * vx - ab_x * vz
        cp3 = ab_x * vy - ab_y * vx
        if cp1 == 0 and cp2 == 0 and cp3 == 0:
            continue
    
        xc = xb + vx
        yc = yb + vy
        zc = zb + vz
    
        len_ab_sq = ab_x**2 + ab_y**2 + ab_z**2
        dot_ab_bc = ab_x * vx + ab_y * vy + ab_z * vz
    
        # Điều kiện để D có tọa độ nguyên và ABCD là hình thang cân (k khác 1)
        if (2 * dot_ab_bc) % len_ab_sq != 0:
            continue
    
        k_val = 1 + (2 * dot_ab_bc) // len_ab_sq
        if k_val <= 0 or k_val == 1:
            continue
    
        # Tọa độ đỉnh D: CD = k_val * AB => D = C - k_val * AB
        xd = xc - k_val * ab_x
        yd = yc - k_val * ab_y
        zd = zc - k_val * ab_z
    
        break
    
    # 1. Vectơ AB = (ab_x; ab_y; ab_z)
    # 2. Trọng tâm G của tam giác ABC
    sum_xg = xa + xb + xc
    sum_yg = ya + yb + yc
    sum_zg = za + zb + zc
    
    str_xg = format_fraction_latex(sum_xg, 3)
    str_yg = format_fraction_latex(sum_yg, 3)
    str_zg = format_fraction_latex(sum_zg, 3)
    
    str_xg_s = format_fraction_latex(sum_xg + random.choice([-1, 1]), 3)
    
    # 3. Điểm E để ABCE là hình bình hành
    # Tứ giác ABCE là hình bình hành <=> vecto AB = vecto EC <=> E = C - AB = C + A - B
    xe = xc - ab_x
    ye = yc - ab_y
    ze = zc - ab_z
    
    # Tọa độ điểm E sai (nhầm sang E = C + AB hoặc E = B + C - A)
    xe_s = xc + ab_x
    ye_s = yc + ab_y
    ze_s = zc + ab_z
    
    # 4. Khi ABCD là hình thang cân với hai đáy AB, CD:
    # D(a; b; c) = (xd; yd; zd)
    # Biểu thức a + b + c
    sum_d = xd + yd + zd
    sum_d_s = sum_d + random.choice([-4, -2, 2, 4])
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Tọa độ vectơ AB
    nb_da_1_d = "\\True Tọa độ vectơ $\\vec{AB} = (%s;%s;%s)$" % (
        ab_x,
        ab_y,
        ab_z,
    )
    nb_da_1_s = "Tọa độ vectơ $\\vec{AB} = (%s;%s;%s)$" % (
        -ab_x,
        -ab_y,
        -ab_z,
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (xb, xa, yb, ya, zb, za, ab_x, ab_y, ab_z)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Tọa độ trọng tâm tam giác ABC
    th_da_1_d = (
        "\\True Tọa độ trọng tâm của tam giác $ABC$ là $\\left(%s;%s;%s\\right)$"
        % (str_xg, str_yg, str_zg)
    )
    th_da_1_s = (
        "Tọa độ trọng tâm của tam giác $ABC$ là $\\left(%s;%s;%s\\right)$"
        % (str_xg_s, str_yg, str_zg)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Gọi $G$ là trọng tâm của tam giác $ABC$. Khi đó ta có: \\\\ $\\begin{cases} x_G = \\frac{x_A + x_B + x_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ y_G = \\frac{y_A + y_B + y_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\end{cases}$ \\\\ Vậy tọa độ trọng tâm của tam giác $ABC$ là $\\left(%s;%s;%s\\right)$."""
        % (
            xa,
            xb,
            xc,
            str_xg,
            ya,
            yb,
            yc,
            str_yg,
            za,
            zb,
            zc,
            str_zg,
            str_xg,
            str_yg,
            str_zg,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Khi điểm E có tọa độ ... thì ABCE là hình bình hành
    vd_da_1_d = (
        "\\True Khi điểm $E$ có tọa độ $(%s;%s;%s)$ thì $ABCE$ là hình bình hành"
        % (xe, ye, ze)
    )
    vd_da_1_s = (
        "Khi điểm $E$ có tọa độ $(%s;%s;%s)$ thì $ABCE$ là hình bình hành"
        % (xe_s, ye_s, ze_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Gọi $E(x_E; y_E; z_E)$. Tứ giác $ABCE$ là hình bình hành khi và chỉ khi: \\\\ $\\vec{EC} = \\vec{AB} \\Leftrightarrow \\begin{cases} x_C - x_E = x_B - x_A \\\\ y_C - y_E = y_B - y_A \\\\ z_C - z_E = z_B - z_A \\end{cases} \\Leftrightarrow \\begin{cases} x_E = x_C - (x_B - x_A) = %s - (%s) = %s \\\\ y_E = y_C - (y_B - y_A) = %s - (%s) = %s \\\\ z_E = z_C - (z_B - z_A) = %s - (%s) = %s \\end{cases}$ \\\\ Do đó $E(%s;%s;%s)$ thì $ABCE$ là hình bình hành."""
        % (
            xc,
            ab_x,
            xe,
            yc,
            ab_y,
            ye,
            zc,
            ab_z,
            ze,
            xe,
            ye,
            ze,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Khi ABCD là hình thang cân có các đáy lần lượt là AB, CD. Khi đó a + b + c = sum_d
    vdc_da_1_d = (
        "\\True Khi $ABCD$ là hình thang cân có các đáy lần lượt là $AB, CD$. Biết điểm $D(a;b;c)$ với $a, b, c \\in \\mathbb{R}$. Khi đó $a + b + c = %s$"
        % (sum_d)
    )
    vdc_da_1_s = (
        "Khi $ABCD$ là hình thang cân có các đáy lần lượt là $AB, CD$. Biết điểm $D(a;b;c)$ với $a, b, c \\in \\mathbb{R}$. Khi đó $a + b + c = %s$"
        % (sum_d_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    len_bc_sq = vx**2 + vy**2 + vz**2
    
    loigiai_vdc_1 = (
        """Vì $ABCD$ là hình thang có hai đáy là $AB, CD$ nên đường thẳng $CD // AB$, suy ra tồn tại số thực $k \\neq 0$ sao cho $\\vec{CD} = k\\vec{AB} = (%sk; %sk; %sk)$. \\\\ Từ đó ta có tọa độ điểm $D$: \\\\ $\\begin{cases} a = x_C + %sk = %s + %sk \\\\ b = y_C + %sk = %s + %sk \\\\ c = z_C + %sk = %s + %sk \\end{cases}$ \\\\ Do $ABCD$ là hình thang cân nên hai cạnh bên có độ dài bằng nhau: $AD = BC \\Leftrightarrow AD^2 = BC^2$. \\\\ Ta có: $BC^2 = (%s)^2 + (%s)^2 + (%s)^2 = %s$. \\\\ $AD^2 = (a - x_A)^2 + (b - y_A)^2 + (c - z_A)^2$. \\\\ Thay tọa độ $D$ vào và giải phương trình bậc hai theo $k$, ta loại nghiệm $k = -1$ (ứng với $ABCD$ là hình bình hành), thu được $k = %s$. \\\\ Khi đó tọa độ điểm $D$ là $D(%s;%s;%s)$, tức $a = %s, b = %s, c = %s$. \\\\ Vậy $a + b + c = (%s) + (%s) + (%s) = %s$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            ab_x,
            xc,
            ab_x,
            ab_y,
            yc,
            ab_y,
            ab_z,
            zc,
            ab_z,
            vx,
            vy,
            vz,
            len_bc_sq,
            -k_val,
            xd,
            yd,
            zd,
            xd,
            yd,
            zd,
            xd,
            yd,
            zd,
            sum_d,
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
        "\\end{ex}\n \\end{minipage}\n\n")
    return content
    