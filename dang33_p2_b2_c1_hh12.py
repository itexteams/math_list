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


def bt_dang33_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hình hộp ABCD.A'B'C'D'
    # A(0; 0; 0), B(b; 0; 0) thuộc Ox, D(0; d; 0) thuộc Oy, D'(0; d; h)
    while True:
        xa, ya, za = 0, 0, 0
    
        xb = random.choice([2, 3, 4, 5])
        yb, zb = 0, 0
    
        yd = random.choice([2, 3, 4, 5])
        xd, zd = 0, 0
    
        # Cao độ h của D' (chọn âm như đề bài gốc để có dấu trừ đẹp)
        h_val = random.choice([-5, -4, -3, -2])
        xd_p = 0
        yd_p = yd
        zd_p = h_val
    
        # Đáy ABCD là hình chữ nhật: C = B + D - A = (xb; yd; 0)
        xc = xb
        yc = yd
        zc = 0
    
        # Vectơ cạnh bên DD' = (0; 0; h_val)
        # A' = A + DD' = (0; 0; h_val)
        # B' = B + DD' = (xb; 0; h_val)
        xa_p, ya_p, za_p = 0, 0, h_val
        xb_p, yb_p, zb_p = xb, 0, h_val
    
        # Trọng tâm G của tam giác A'B'C:
        # xG = (0 + xb + xc) / 3 = 2*xb / 3
        # yG = (0 + 0 + yc) / 3 = yd / 3
        # zG = (h_val + h_val + 0) / 3 = 2*h_val / 3
        # Để trọng tâm đẹp hoặc nguyên, ta kiểm tra điều kiện chia hết cho 3
        if (2 * xb) % 3 == 0 or yd % 3 == 0:
            break
    
    # 1. Tọa độ trung điểm I của BD':
    # I = (B + D') / 2 = (xb/2; yd/2; h_val/2)
    str_xi = format_fraction_latex(xb, 2)
    str_yi = format_fraction_latex(yd, 2)
    str_zi = format_fraction_latex(h_val, 2)
    
    # Tọa độ sai của trung điểm (ví dụ nhầm x = 0 như đề gốc)
    str_xi_s = "0"
    str_yi_s = "1"
    
    # 2. Tọa độ điểm C để ABCD là hình bình hành: C(xc; yc; 0)
    # Tọa độ C sai
    xc_s = xc + random.choice([-1, 1])
    yc_s = yc
    zc_s = zc
    
    # 3. Điểm M trên trục Oy cách đều hai điểm B, C:
    # M thuộc Oy => M(0; y; 0)
    # MB^2 = MC^2 <=> (0 - xb)^2 + y^2 = (0 - xc)^2 + (y - yc)^2
    # <=> xb^2 + y^2 = xc^2 + y^2 - 2*yc*y + yc^2
    # Vì xc = xb nên: 0 = -2*yc*y + yc^2 <=> 2*yc*y = yc^2 <=> y = yc / 2 (do yc != 0)
    ym_num = yd
    str_ym = format_fraction_latex(ym_num, 2)
    str_ym_s = format_fraction_latex(1, 2) if str_ym != "\\frac{1}{2}" else "1"
    
    # 4. Tọa độ trọng tâm G của tam giác A'B'C:
    xg_num = 2 * xb
    yg_num = yd
    zg_num = 2 * h_val
    
    str_xg = format_fraction_latex(xg_num, 3)
    str_yg = format_fraction_latex(yg_num, 3)
    str_zg = format_fraction_latex(zg_num, 3)
    
    str_xg_s = format_fraction_latex(xg_num + random.choice([-1, 1]), 3)
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho hình hộp $ABCD.A'B'C'D'$ có các đỉnh $A(%s;%s;%s)$, $B(%s;%s;%s)$, $D(%s;%s;%s)$, $D'(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xd, yd, zd, xd_p, yd_p, zd_p)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Tọa độ trung điểm của BD'
    nb_da_1_d = (
        "\\True Tọa độ trung điểm của $BD'$ là $\\left(%s;%s;%s\\right)$"
        % (str_xi, str_yi, str_zi)
    )
    nb_da_1_s = (
        "Tọa độ trung điểm của $BD'$ là $\\left(%s;%s;%s\\right)$"
        % (str_xi_s, str_yi_s, str_zi)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Gọi $I$ là trung điểm của đoạn thẳng $BD'$. Khi đó ta có: \\\\ $\\begin{cases} x_I = \\frac{x_B + x_{D'}}{2} = \\frac{%s + %s}{2} = %s \\\\ y_I = \\frac{y_B + y_{D'}}{2} = \\frac{%s + %s}{2} = %s \\\\ z_I = \\frac{z_B + z_{D'}}{2} = \\frac{%s + (%s)}{2} = %s \\end{cases}$ \\\\ Vậy tọa độ trung điểm của $BD'$ là $\\left(%s;%s;%s\\right)$."""
        % (
            xb,
            xd_p,
            str_xi,
            yb,
            yd_p,
            str_yi,
            zb,
            zd_p,
            str_zi,
            str_xi,
            str_yi,
            str_zi,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Tọa độ điểm C để ABCD là hình bình hành
    th_da_1_d = (
        "\\True Tọa độ điểm $C$ để $ABCD$ là hình bình hành là $(%s;%s;%s)$"
        % (xc, yc, zc)
    )
    th_da_1_s = (
        "Tọa độ điểm $C$ để $ABCD$ là hình bình hành là $(%s;%s;%s)$"
        % (xc_s, yc_s, zc_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì tứ giác $ABCD$ là hình bình hành nên theo quy tắc hình bình hành ta có: \\\\ $\\vec{AC} = \\vec{AB} + \\vec{AD} \\Leftrightarrow C - A = (B - A) + (D - A) \\Leftrightarrow C = B + D - A$. \\\\ Tọa độ điểm $C$ là: \\\\ $\\begin{cases} x_C = x_B + x_D - x_A = %s + %s - %s = %s \\\\ y_C = y_B + y_D - y_A = %s + %s - %s = %s \\\\ z_C = z_B + z_D - z_A = %s + %s - %s = %s \\end{cases} \\Rightarrow C(%s;%s;%s)$."""
        % (
            xb,
            xd,
            xa,
            xc,
            yb,
            yd,
            ya,
            yc,
            zb,
            zd,
            za,
            zc,
            xc,
            yc,
            zc,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Tọa độ điểm M trên trục Oy cách đều hai điểm B, C
    vd_da_1_d = (
        "\\True Tọa độ điểm $M$ trên trục $Oy$ cách đều hai điểm $B, C$ là $\\left(0;%s;0\\right)$"
        % (str_ym)
    )
    vd_da_1_s = (
        "Tọa độ điểm $M$ trên trục $Oy$ cách đều hai điểm $B, C$ là $\\left(0;%s;0\\right)$"
        % (str_ym_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì điểm $M$ thuộc trục $Oy$ nên tọa độ của $M$ có dạng $M(0;y;0)$. \\\\ Điểm $M$ cách đều hai điểm $B(%s;0;0)$ và $C(%s;%s;0)$ khi và chỉ khi: \\\\ $MB = MC \\Leftrightarrow MB^2 = MC^2$ \\\\ $\\Leftrightarrow (0 - %s)^2 + (y - 0)^2 + (0 - 0)^2 = (0 - %s)^2 + (y - %s)^2 + (0 - 0)^2$ \\\\ $\\Leftrightarrow %s + y^2 = %s + y^2 - %sy + %s$ \\\\ $\\Leftrightarrow %sy = %s \\Leftrightarrow y = %s$. \\\\ Vậy tọa độ điểm $M$ là $\\left(0;%s;0\\right)$."""
        % (
            xb,
            xc,
            yc,
            xb,
            xc,
            yc,
            xb**2,
            xc**2,
            2 * yc,
            yc**2,
            2 * yc,
            yc**2,
            str_ym,
            str_ym,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Tọa độ trọng tâm tam giác A'B'C
    vdc_da_1_d = (
        "\\True Tọa độ trọng tâm tam giác $A'B'C$ là $\\left(%s;%s;%s\\right)$"
        % (str_xg, str_yg, str_zg)
    )
    vdc_da_1_s = (
        "Tọa độ trọng tâm tam giác $A'B'C$ là $\\left(%s;%s;%s\\right)$"
        % (str_xg_s, str_yg, str_zg)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì $ABCD.A'B'C'D'$ là hình hộp nên ta có: \\\\ $\\vec{AA'} = \\vec{DD'} = (0 - 0; %s - %s; %s - 0) = (0;0;%s) \\Rightarrow A'(0;0;%s)$. \\\\ $\\vec{BB'} = \\vec{DD'} = (0;0;%s) \\Rightarrow B'(%s;0;%s)$. \\\\ Gọi $G$ là trọng tâm của tam giác $A'B'C$, ta có: \\\\ $\\begin{cases} x_G = \\frac{x_{A'} + x_{B'} + x_C}{3} = \\frac{0 + %s + %s}{3} = %s \\\\ y_G = \\frac{y_{A'} + y_{B'} + y_C}{3} = \\frac{0 + 0 + %s}{3} = %s \\\\ z_G = \\frac{z_{A'} + z_{B'} + z_C}{3} = \\frac{%s + (%s) + 0}{3} = %s \\end{cases}$ \\\\ Vậy tọa độ trọng tâm tam giác $A'B'C$ là $\\left(%s;%s;%s\\right)$."""
        % (
            yd,
            yd,
            h_val,
            h_val,
            h_val,
            h_val,
            xb,
            h_val,
            xb,
            xc,
            str_xg,
            yc,
            str_yg,
            h_val,
            h_val,
            str_zg,
            str_xg,
            str_yg,
            str_zg,
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
    