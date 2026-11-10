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


def bt_dang42_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hai điểm A, B sao cho OA, OB có độ dài hữu tỉ đẹp[cite: 21]
    # Ở đề gốc: A(2; 2; 1) => OA = 3; B(-8/3; 4/3; 8/3) => OB = 4[cite: 21]
    # Chân đường phân giác trong góc AOB: D = (OB * A + OA * B) / (OA + OB) = (4A + 3B) / 7[cite: 21]
    while True:
        # Chọn A từ bộ ba số Pythagore mở rộng: u^2 + v^2 + w^2 = OA^2 (OA = 3)
        coords_a = [2, 2, 1]
        signs_a = [
            random.choice([-1, 1]),
            random.choice([-1, 1]),
            random.choice([-1, 1]),
        ]
        xa = coords_a[0] * signs_a[0]
        ya = coords_a[1] * signs_a[1]
        za = coords_a[2] * signs_a[2]
        oa_len = 3
    
        # Chọn B có dạng (xb_num/3; yb_num/3; zb_num/3) sao cho OB = 4[cite: 21]
        # (xb_num)^2 + (yb_num)^2 + (zb_num)^2 = 12^2 = 144
        # 8^2 + 4^2 + 8^2 = 64 + 16 + 64 = 144
        coords_b = [8, 4, 8]
        random.shuffle(coords_b)
        signs_b = [
            random.choice([-1, 1]),
            random.choice([-1, 1]),
            random.choice([-1, 1]),
        ]
    
        xb_num = coords_b[0] * signs_b[0]
        yb_num = coords_b[1] * signs_b[1]
        zb_num = coords_b[2] * signs_b[2]
        ob_len = 4
    
        xb_val = Rational(xb_num, 3)
        yb_val = Rational(yb_num, 3)
        zb_val = Rational(zb_num, 3)
    
        # Tích vô hướng OA . OB để xét tính nhọn/tù/vuông[cite: 21]
        dot_oa_ob = xa * xb_val + ya * yb_val + za * zb_val
    
        # Tính AB^2
        ab_vec_x = xb_val - xa
        ab_vec_y = yb_val - ya
        ab_vec_z = zb_val - za
        ab_sq = ab_vec_x**2 + ab_vec_y**2 + ab_vec_z**2
    
        # Tọa độ chân phân giác trong góc AOB là D:
        # Theo tính chất đường phân giác trong: DA / DB = OA / OB = 3 / 4[cite: 21]
        # => vecto DA = -3/4 vecto DB <=> 4 DA + 3 DB = 0 <=> D = (4A + 3B) / 7[cite: 21]
        # x_D = (4*xa + 3*xb_val) / 7 = (4*xa + xb_num) / 7
        xd_num = 4 * xa + xb_num
        yd_num = 4 * ya + yb_num
        zd_num = 4 * za + zb_num
    
        xd_val = Rational(xd_num, 7)
        yd_val = Rational(yd_num, 7)
        zd_val = Rational(zd_num, 7)
    
        # Đảm bảo ba điểm O, A, B không thẳng hàng và ít nhất 1 tọa độ của D bằng 0 tạo sự đặc biệt đẹp[cite: 21]
        if (
            (xa * yb_val - ya * xb_val != 0 or ya * zb_val - za * yb_val != 0)
            and (xd_num == 0 or yd_num == 0 or zd_num == 0)
            and dot_oa_ob != 0
        ):
            break
    
    str_xb = format_fraction_latex(xb_num, 3)
    str_yb = format_fraction_latex(yb_num, 3)
    str_zb = format_fraction_latex(zb_num, 3)
    
    # 1. Khẳng định a: Độ dài đoạn thẳng AB = sqrt(ab_sq)[cite: 21]
    str_ab_true = latex(sp.sqrt(ab_sq))
    str_ab_false = "\\sqrt{5}" if str_ab_true != "\\sqrt{5}" else "\\sqrt{7}"
    
    # 2. Khẳng định b: Tam giác OAB là tam giác nhọn/tù/vuông[cite: 21]
    # dot_oa_ob > 0 => góc AOB nhọn, dot_oa_ob < 0 => góc AOB tù[cite: 21]
    # Kiểm tra các góc còn lại của tam giác OAB:
    # BA . BO = (A - B) . (-B) = B^2 - A.B = 16 - dot_oa_ob
    # AB . AO = (B - A) . (-A) = A^2 - A.B = 9 - dot_oa_ob
    is_acute_triangle = dot_oa_ob > 0 and (9 - dot_oa_ob) > 0 and (16 - dot_oa_ob) > 0
    
    # 3. Khẳng định c: Chân đường phân giác trong góc AOB là D[cite: 21]
    str_xd = format_fraction_latex(xd_val.p, xd_val.q)
    str_yd = format_fraction_latex(yd_val.p, yd_val.q)
    str_zd = format_fraction_latex(zd_val.p, zd_val.q)
    
    # Tọa độ sai của D (nhầm dấu hoặc nhầm tỉ lệ phân giác ngoài)[cite: 21]
    str_yd_false = format_fraction_latex(yd_val.p + 2, yd_val.q)
    
    # 4. Khẳng định d: Diện tích tam giác OAB
    # [OA, OB]
    cp_x = ya * zb_val - za * yb_val
    cp_y = za * xb_val - xa * zb_val
    cp_z = xa * yb_val - ya * xb_val
    cp_sq = cp_x**2 + cp_y**2 + cp_z**2
    s_oab = Rational(1, 2) * sp.sqrt(cp_sq)
    str_s_oab_true = latex(s_oab)
    str_s_oab_false = latex(s_oab + 1)
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$ cho hai điểm $A(%s;%s;%s), B\\left(%s;%s;%s\\right)$."""
        % (xa, ya, za, str_xb, str_yb, str_zb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Độ dài đoạn thẳng AB[cite: 21]
    nb_da_1_d = "\\True Độ dài đoạn thẳng $AB = %s$" % (str_ab_true)
    nb_da_1_s = "Độ dài đoạn thẳng $AB = %s$" % (str_ab_false)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ vectơ $\\vec{AB}$ là: \\\\ $\\vec{AB} = \\left(x_B - x_A; y_B - y_A; z_B - z_A\\right) = \\left(%s - (%s); %s - (%s); %s - (%s)\\right) = \\left(%s;%s;%s\\right)$. \\\\ Khi đó độ dài đoạn thẳng $AB$ là: \\\\ $AB = \\sqrt{\\left(%s\\right)^2 + \\left(%s\\right)^2 + \\left(%s\\right)^2} = %s$."""
        % (
            str_xb,
            xa,
            str_yb,
            ya,
            str_zb,
            za,
            format_fraction_latex(ab_vec_x.p, ab_vec_x.q),
            format_fraction_latex(ab_vec_y.p, ab_vec_y.q),
            format_fraction_latex(ab_vec_z.p, ab_vec_z.q),
            format_fraction_latex(ab_vec_x.p, ab_vec_x.q),
            format_fraction_latex(ab_vec_y.p, ab_vec_y.q),
            format_fraction_latex(ab_vec_z.p, ab_vec_z.q),
            str_ab_true,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Tam giác OAB là tam giác nhọn/tù[cite: 21]
    if is_acute_triangle:
        th_da_1_d = "\\True Tam giác $OAB$ là tam giác nhọn"
        th_da_1_s = "Tam giác $OAB$ là tam giác tù"
    else:
        th_da_1_d = "\\True Tam giác $OAB$ là tam giác tù"
        th_da_1_s = "Tam giác $OAB$ là tam giác nhọn"
    
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có tọa độ các vectơ $\\vec{OA} = (%s;%s;%s)$ và $\\vec{OB} = \\left(%s;%s;%s\\right)$. \\\\ Xét tích vô hướng của hai vectơ: \\\\ $\\vec{OA} \\cdot \\vec{OB} = (%s) \\cdot \\left(%s\\right) + (%s) \\cdot \\left(%s\\right) + (%s) \\cdot \\left(%s\\right) = %s$. \\\\ Vì $\\vec{OA} \\cdot \\vec{OB} %s 0$ nên $\\cos\\widehat{AOB} %s 0$, do đó góc $\\widehat{AOB}$ là góc %s. \\\\ Vậy tam giác $OAB$ là tam giác %s."""
        % (
            xa,
            ya,
            za,
            str_xb,
            str_yb,
            str_zb,
            xa,
            str_xb,
            ya,
            str_yb,
            za,
            str_zb,
            format_fraction_latex(dot_oa_ob.p, dot_oa_ob.q),
            ">" if dot_oa_ob > 0 else "<",
            ">" if dot_oa_ob > 0 else "<",
            "nhọn" if dot_oa_ob > 0 else "tù",
            "nhọn" if is_acute_triangle else "tù",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Chân đường phân giác trong góc AOB là D[cite: 21]
    vd_da_1_d = (
        "\\True Chân đường phân giác trong góc $\\widehat{AOB}$ là $D\\left(%s;%s;%s\\right)$"
        % (str_xd, str_yd, str_zd)
    )
    vd_da_1_s = (
        "Chân đường phân giác trong góc $\\widehat{AOB}$ là $D\\left(%s;%s;%s\\right)$"
        % (str_xd, str_yd_false, str_zd)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có độ dài các cạnh: \\\\ $OA = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = %s$. \\\\ $OB = \\sqrt{\\left(%s\\right)^2 + \\left(%s\\right)^2 + \\left(%s\\right)^2} = %s$. \\\\ Theo tính chất đường phân giác trong góc $\\widehat{AOB}$ của tam giác $OAB$, ta có: \\\\ $\\frac{DA}{DB} = \\frac{OA}{OB} = \\frac{%s}{%s}$. \\\\ Vì điểm $D$ thuộc đoạn thẳng $AB$ nên hai vectơ $\\vec{DA}$ và $\\vec{DB}$ ngược hướng, suy ra: \\\\ $\\vec{DA} = -\\frac{%s}{%s}\\vec{DB} \\Leftrightarrow %s\\vec{DA} + %s\\vec{DB} = \\vec{0} \\Leftrightarrow %s(A - D) + %s(B - D) = \\vec{0} \\Leftrightarrow %s D = %s A + %s B \\Leftrightarrow D = \\frac{%s A + %s B}{%s}$. \\\\ Tọa độ của điểm $D$ là: \\\\ $\\begin{cases} x_D = \\frac{%s \\cdot (%s) + %s \\cdot \\left(%s\\right)}{%s} = %s \\\\ y_D = \\frac{%s \\cdot (%s) + %s \\cdot \\left(%s\\right)}{%s} = %s \\\\ z_D = \\frac{%s \\cdot (%s) + %s \\cdot \\left(%s\\right)}{%s} = %s \\end{cases} \\Rightarrow D\\left(%s;%s;%s\\right)$."""
        % (
            xa,
            ya,
            za,
            oa_len,
            str_xb,
            str_yb,
            str_zb,
            ob_len,
            oa_len,
            ob_len,
            oa_len,
            ob_len,
            ob_len,
            oa_len,
            ob_len,
            oa_len,
            ob_len + oa_len,
            ob_len,
            oa_len,
            ob_len,
            oa_len,
            ob_len + oa_len,
            ob_len,
            xa,
            oa_len,
            str_xb,
            ob_len + oa_len,
            str_xd,
            ob_len,
            ya,
            oa_len,
            str_yb,
            ob_len + oa_len,
            str_yd,
            ob_len,
            za,
            oa_len,
            str_zb,
            ob_len + oa_len,
            str_zd,
            str_xd,
            str_yd,
            str_zd,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Diện tích tam giác OAB
    vdc_da_1_d = "\\True Diện tích tam giác $OAB$ là $S_{OAB} = %s$" % (
        str_s_oab_true
    )
    vdc_da_1_s = "Diện tích tam giác $OAB$ là $S_{OAB} = %s$" % (
        str_s_oab_false
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta có tích có hướng của hai vectơ $\\vec{OA}$ và $\\vec{OB}$: \\\\ $[\\vec{OA}, \\vec{OB}] = \\left( \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix} \\right) = \\left(%s;%s;%s\\right)$. \\\\ Khi đó diện tích tam giác $OAB$ là: \\\\ $S_{OAB} = \\frac{1}{2} \\left|[\\vec{OA}, \\vec{OB}]\\right| = \\frac{1}{2} \\sqrt{\\left(%s\\right)^2 + \\left(%s\\right)^2 + \\left(%s\\right)^2} = %s$."""
        % (
            ya,
            za,
            str_yb,
            str_zb,
            za,
            xa,
            str_zb,
            str_xb,
            xa,
            ya,
            str_xb,
            str_yb,
            format_fraction_latex(cp_x.p, cp_x.q),
            format_fraction_latex(cp_y.p, cp_y.q),
            format_fraction_latex(cp_z.p, cp_z.q),
            format_fraction_latex(cp_x.p, cp_x.q),
            format_fraction_latex(cp_y.p, cp_y.q),
            format_fraction_latex(cp_z.p, cp_z.q),
            str_s_oab_true,
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
    