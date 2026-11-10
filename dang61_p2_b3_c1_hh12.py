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


def bt_dang61_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    while True:
        xa = random.randint(1, 4)
        ya = random.randint(3, 6)
        za = random.randint(0, 3)
    
        xc = xa + random.choice([-2, -1, 1, 2])
        yc = ya + random.choice([-4, -3, -2, 2, 3])
        zc = za + random.choice([-3, -2, 2, 3])
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        xb = random.randint(-4, 0)
        yb = random.randint(-7, -3)
        zb = random.randint(1, 4)
    
        # Đặt K sao cho BK = 2*AC <=> K = B - 2*AC[cite: 20]
        # MB - 2*AC = (xB - m - 2*ac_x; yB - m - 2*ac_y; zB - m - 2*ac_z) = (xk - m; yk - m; zk - m)[cite: 20]
        xk = xb - 2 * ac_x
        yk = yb - 2 * ac_y
        zk = zb - 2 * ac_z
    
        sum_k = xk + yk + zk
        sum_b = xb + yb + zb
    
        if sum_k % 3 == 0 and sum_b != 0 and yb != 0:
            m_opt = sum_k // 3
            # Giá trị nhỏ nhất bình phương: (m_opt - xk)^2 + (m_opt - yk)^2 + (m_opt - zk)^2[cite: 20]
            f_min_sq = (m_opt - xk) ** 2 + (m_opt - yk) ** 2 + (m_opt - zk) ** 2
            if f_min_sq > 0:
                break
    
    # 1. Khẳng định a: Tọa độ vectơ AC[cite: 20]
    ac_x_true, ac_y_true, ac_z_true = ac_x, ac_y, ac_z
    ac_x_false = ac_x_true
    ac_y_false = -ac_y_true if ac_y_true != 0 else 2
    ac_z_false = ac_z_true
    
    # 2. Khẳng định b: Điểm B cách mặt phẳng (Oxz) một khoảng bằng |yB|[cite: 20]
    dist_b_oxz = abs(yb)
    dist_b_oxz_s = dist_b_oxz + random.choice([-1, 1])
    if dist_b_oxz_s <= 0:
        dist_b_oxz_s = dist_b_oxz + 2
    
    # 3. Khẳng định c: MB = sqrt(3m^2 + b_m*m + c_m)[cite: 20]
    # MB^2 = (m - xb)^2 + (m - yb)^2 + (m - zb)^2 = 3m^2 - 2(xb + yb + zb)m + (xb^2 + yb^2 + zb^2)[cite: 20]
    coef_b_m = -2 * sum_b
    const_c_m = xb**2 + yb**2 + zb**2
    
    str_sign_b_m = (
        "+ %sm" % (coef_b_m) if coef_b_m >= 0 else "- %sm" % (-coef_b_m)
    )
    str_mb_expr_true = "\\sqrt{3m^2 %s + %s}" % (str_sign_b_m, const_c_m)
    
    coef_b_m_false = coef_b_m + random.choice([-4, -2, 2, 4])
    str_sign_b_m_false = (
        "+ %sm" % (coef_b_m_false)
        if coef_b_m_false >= 0
        else "- %sm" % (-coef_b_m_false)
    )
    str_mb_expr_false = "\\sqrt{3m^2 %s + %s}" % (str_sign_b_m_false, const_c_m)
    
    # 4. Khẳng định d: Biểu thức |MB - 2*AC| đạt giá trị nhỏ nhất bằng min_val[cite: 20]
    min_val_sym = sp.sqrt(f_min_sq)
    str_min_val_true = latex(min_val_sym)
    
    min_val_sym_false = sp.sqrt(f_min_sq + random.choice([-4, -2, 2, 4]))
    str_min_val_false = latex(min_val_sym_false)
    if str_min_val_false == str_min_val_true:
        str_min_val_false = "2\\sqrt{5}"[cite: 20]
    
    # Hệ số khai triển biểu thức trong căn của |MB - 2*AC|^2:
    # f(m) = 3m^2 - 2(xk + yk + zk)m + (xk^2 + yk^2 + zk^2)[cite: 20]
    coef_m_d = -2 * sum_k
    const_d = xk**2 + yk**2 + zk**2
    str_sign_m_d = "+ %sm" % (coef_m_d) if coef_m_d >= 0 else "- %sm" % (-coef_m_d)
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Trong không gian tọa độ $Oxyz$ cho ba điểm $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s)$ và điểm $M(m;m;m)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Tọa độ vectơ AC[cite: 20]
    nb_da_1_d = "\\True $\\vec{AC} = (%s;%s;%s)$" % (
        ac_x_true,
        ac_y_true,
        ac_z_true,
    )
    nb_da_1_s = "$\\vec{AC} = (%s;%s;%s)$" % (
        ac_x_false,
        ac_y_false,
        ac_z_false,
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Tọa độ của vectơ $\\vec{AC}$ là: \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (
            xc,
            xa,
            yc,
            ya,
            zc,
            za,
            ac_x_true,
            ac_y_true,
            ac_z_true,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Điểm B cách mặt phẳng (Oxz) một khoảng bằng dist_b_oxz[cite: 20]
    th_da_1_d = (
        "\\True Điểm $B$ cách mặt phẳng $(Oxz)$ một khoảng bằng $%s$" % (dist_b_oxz)
    )
    th_da_1_s = (
        "Điểm $B$ cách mặt phẳng $(Oxz)$ một khoảng bằng $%s$" % (dist_b_oxz_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Mặt phẳng tọa độ $(Oxz)$ có phương trình là $y = 0$. \\\\ Khoảng cách từ điểm $B(%s;%s;%s)$ đến mặt phẳng $(Oxz)$ là: \\\\ $d(B, (Oxz)) = |y_B| = |%s| = %s$."""
        % (
            xb,
            yb,
            zb,
            yb,
            dist_b_oxz,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: MB = sqrt(3m^2 + b_m*m + c_m)[cite: 20]
    vd_da_1_d = "\\True $MB = %s$" % (str_mb_expr_true)
    vd_da_1_s = "$MB = %s$" % (str_mb_expr_false)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Tọa độ vectơ $\\vec{BM}$ là: \\\\ $\\vec{BM} = (x_M - x_B; y_M - y_B; z_M - z_B) = (m - (%s); m - (%s); m - (%s))$. \\\\ Khi đó độ dài đoạn thẳng $MB$ là: \\\\ $MB = \\sqrt{(m - (%s))^2 + (m - (%s))^2 + (m - (%s))^2}$ \\\\ $= \\sqrt{(m^2 - 2 \\cdot (%s) m + (%s)^2) + (m^2 - 2 \\cdot (%s) m + (%s)^2) + (m^2 - 2 \\cdot (%s) m + (%s)^2)}$ \\\\ $= %s$."""
        % (
            xb,
            yb,
            zb,
            xb,
            yb,
            zb,
            xb,
            xb,
            yb,
            yb,
            zb,
            zb,
            str_mb_expr_true,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Biểu thức |MB - 2*AC| đạt giá trị nhỏ nhất bằng min_val[cite: 20]
    vdc_da_1_d = (
        "\\True Biểu thức $\\left|\\vec{MB} - 2\\vec{AC}\\right|$ đạt giá trị nhỏ nhất bằng $%s$"
        % (str_min_val_true)
    )
    vdc_da_1_s = (
        "Biểu thức $\\left|\\vec{MB} - 2\\vec{AC}\\right|$ đạt giá trị nhỏ nhất bằng $%s$"
        % (str_min_val_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta có tọa độ vectơ $\\vec{MB}$ là: \\\\ $\\vec{MB} = (x_B - m; y_B - m; z_B - m) = (%s - m; %s - m; %s - m)$. \\\\ Tọa độ vectơ $2\\vec{AC}$ là: \\\\ $2\\vec{AC} = 2(%s; %s; %s) = (%s; %s; %s)$. \\\\ Suy ra tọa độ của vectơ $\\vec{MB} - 2\\vec{AC}$ là: \\\\ $\\vec{u} = \\vec{MB} - 2\\vec{AC} = (%s - m - (%s); %s - m - (%s); %s - m - (%s)) = (%s - m; %s - m; %s - m)$. \\\\ Độ dài của vectơ $\\vec{MB} - 2\\vec{AC}$ là: \\\\ $\\left|\\vec{MB} - 2\\vec{AC}\\right| = \\sqrt{(%s - m)^2 + (%s - m)^2 + (%s - m)^2}$ \\\\ $= \\sqrt{3m^2 %s + %s} = \\sqrt{3\\left(m - %s\\right)^2 + %s} \\ge \\sqrt{%s} = %s$. \\\\ Dấu đẳng thức xảy ra khi và chỉ khi $m = %s$. \\\\ Vậy giá trị nhỏ nhất của biểu thức là $%s$."""
        % (
            xb,
            yb,
            zb,
            ac_x,
            ac_y,
            ac_z,
            2 * ac_x,
            2 * ac_y,
            2 * ac_z,
            xb,
            2 * ac_x,
            yb,
            2 * ac_y,
            zb,
            2 * ac_z,
            xk,
            yk,
            zk,
            xk,
            yk,
            zk,
            str_sign_m_d,
            const_d,
            m_opt,
            f_min_sq,
            f_min_sq,
            str_min_val_true,
            m_opt,
            str_min_val_true,
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
    