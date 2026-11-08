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


def bt_dang8_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên toạ độ các đỉnh tam giác sao cho độ dài BA và BC có tỉ số hữu tỉ đẹp
    while True:
        # Chọn toạ độ đỉnh B
        xb = random.randint(-3, 3)
        yb = random.randint(-3, 3)
        zb = random.randint(-3, 3)
    
        # Chọn vector BA có 3 thành phần có độ lớn đôi một khác nhau (để khi hoán vị tạo ra vector không cùng phương)
        magnitudes = random.sample([1, 2, 3, 4], 3)
        signs_ba = [random.choice([-1, 1]) for _ in range(3)]
        ba_x = magnitudes[0] * signs_ba[0]
        ba_y = magnitudes[1] * signs_ba[1]
        ba_z = magnitudes[2] * signs_ba[2]
    
        # Đỉnh A = B + vector(BA)
        xa = xb + ba_x
        ya = yb + ba_y
        za = zb + ba_z
    
        # Vector BC được tạo từ hoán vị các thành phần độ lớn của BA nhân với tỉ số k (k = 2)
        # để độ dài BC = 2 * BA, giúp chân đường phân giác D có toạ độ là số hữu tỉ rất đẹp
        k_ratio = 2
        perm_mag = [magnitudes[1], magnitudes[2], magnitudes[0]]
        signs_bc = [random.choice([-1, 1]) for _ in range(3)]
        bc_x = k_ratio * perm_mag[0] * signs_bc[0]
        bc_y = k_ratio * perm_mag[1] * signs_bc[1]
        bc_z = k_ratio * perm_mag[2] * signs_bc[2]
    
        # Kiểm tra hai vectơ BA và BC không cùng phương (tích có hướng khác vectơ 0)
        cp_x = ba_y * bc_z - ba_z * bc_y
        cp_y = ba_z * bc_x - ba_x * bc_z
        cp_z = ba_x * bc_y - ba_y * bc_x
    
        if cp_x != 0 or cp_y != 0 or cp_z != 0:
            # Đỉnh C = B + vector(BC)
            xc = xb + bc_x
            yc = yb + bc_y
            zc = zb + bc_z
            break
    
    # 1. Vectơ AB = - vectơ BA
    ab_x = -ba_x
    ab_y = -ba_y
    ab_z = -ba_z
    
    # 2. Vectơ AC = C - A
    ac_x = xc - xa
    ac_y = yc - ya
    ac_z = zc - za
    
    # Vectơ x = 2*AB + AC
    vec_x_x = 2 * ab_x + ac_x
    vec_x_y = 2 * ab_y + ac_y
    vec_x_z = 2 * ab_z + ac_z
    
    # 3. Cho u thoả mãn: 2*u - AB + BC = AC <=> 2*u = AB + AC - BC = AB + AB = 2*AB <=> u = AB
    # Toạ độ u đúng chính là toạ độ của AB
    u_x = ab_x
    u_y = ab_y
    u_z = ab_z
    
    # 4. Chân đường phân giác góc ABC của tam giác ABC:
    # Ta có BA/BC = 1/2 => DA/DC = 1/2 => vecto(DA) = - 1/2 * vecto(DC) => D = (2*A + C) / 3
    d_x_num = 2 * xa + xc
    d_y_num = 2 * ya + yc
    d_z_num = 2 * za + zc
    
    str_xd = format_fraction_latex(d_x_num, 3)
    str_yd = format_fraction_latex(d_y_num, 3)
    str_zd = format_fraction_latex(d_z_num, 3)
    
    # Bình phương độ dài AB và BC để trình bày lời giải chi tiết
    len_ba_sq = ba_x**2 + ba_y**2 + ba_z**2
    len_bc_sq = bc_x**2 + bc_y**2 + bc_z**2
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$ cho tam giác $ABC$ có $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Phát biểu a: Toạ độ của vectơ AB
    nb_da_1_d = "\\True Toạ độ của vectơ $\\vec{AB}$ là $(%s;%s;%s)$" % (
        ab_x,
        ab_y,
        ab_z,
    )
    nb_da_1_s = "Toạ độ của vectơ $\\vec{AB}$ là $(%s;%s;%s)$" % (
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
    # Phát biểu b: Toạ độ của vectơ x = 2*AB + AC
    vec_x_z_sai = vec_x_z + random.choice([-2, 2, -12, 12])
    th_da_1_d = (
        "\\True Toạ độ của vectơ $\\vec{x} = 2\\vec{AB} + \\vec{AC}$ là $(%s;%s;%s)$"
        % (vec_x_x, vec_x_y, vec_x_z)
    )
    th_da_1_s = (
        "Toạ độ của vectơ $\\vec{x} = 2\\vec{AB} + \\vec{AC}$ là $(%s;%s;%s)$"
        % (vec_x_x, vec_x_y, vec_x_z_sai)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có $\\vec{AB} = (%s;%s;%s) \\Rightarrow 2\\vec{AB} = (%s;%s;%s)$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s;%s;%s)$. \\\\ Suy ra $\\vec{x} = 2\\vec{AB} + \\vec{AC} = (%s + (%s); %s + (%s); %s + (%s)) = (%s;%s;%s)$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            2 * ab_x,
            2 * ab_y,
            2 * ab_z,
            ac_x,
            ac_y,
            ac_z,
            2 * ab_x,
            ac_x,
            2 * ab_y,
            ac_y,
            2 * ab_z,
            ac_z,
            vec_x_x,
            vec_x_y,
            vec_x_z,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Phát biểu c: Cho u thoả mãn 2*u - AB + BC = AC. Toạ độ của u là ...
    vd_da_1_d = (
        "\\True Cho $\\vec{u}$ thoả mãn $2\\vec{u} - \\vec{AB} + \\vec{BC} = \\vec{AC}$. Toạ độ của $\\vec{u}$ là $(%s;%s;%s)$"
        % (u_x, u_y, u_z)
    )
    vd_da_1_s = (
        "Cho $\\vec{u}$ thoả mãn $2\\vec{u} - \\vec{AB} + \\vec{BC} = \\vec{AC}$. Toạ độ của $\\vec{u}$ là $(%s;%s;%s)$"
        % (2 * u_x, 2 * u_y, 2 * u_z)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Từ giả thiết ta có: \\\\ $2\\vec{u} - \\vec{AB} + \\vec{BC} = \\vec{AC} \\Leftrightarrow 2\\vec{u} = \\vec{AB} + \\vec{AC} - \\vec{BC}$ \\\\ $\\Leftrightarrow 2\\vec{u} = \\vec{AB} + (\\vec{AC} + \\vec{CB}) \\Leftrightarrow 2\\vec{u} = \\vec{AB} + \\vec{AB} = 2\\vec{AB} \\Leftrightarrow \\vec{u} = \\vec{AB}$. \\\\ Do đó toạ độ của $\\vec{u}$ là $(%s;%s;%s)$."""
        % (u_x, u_y, u_z)
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Phát biểu d: Gọi D là chân đường phân giác góc ABC của tam giác ABC. Toạ độ điểm D là ...
    vdc_da_1_d = (
        "\\True Gọi $D$ là chân đường phân giác góc $\\widehat{ABC}$ của tam giác $ABC$. Toạ độ điểm $D$ là $\\left(%s;%s;%s\\right)$"
        % (str_xd, str_yd, str_zd)
    )
    
    # Tạo toạ độ sai bằng cách lấy trung điểm AC hoặc hoán vị
    str_xd_s = format_fraction_latex(xa + xc, 2)
    str_yd_s = format_fraction_latex(ya + yc, 2)
    str_zd_s = format_fraction_latex(za + zc, 2)
    vdc_da_1_s = (
        "Gọi $D$ là chân đường phân giác góc $\\widehat{ABC}$ của tam giác $ABC$. Toạ độ điểm $D$ là $\\left(%s;%s;%s\\right)$"
        % (str_xd_s, str_yd_s, str_zd_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta có $\\vec{BA} = (%s;%s;%s) \\Rightarrow BA = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $\\vec{BC} = (%s;%s;%s) \\Rightarrow BC = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = 2\\sqrt{%s}$. \\\\ Do $D$ là chân đường phân giác trong của góc $\\widehat{ABC}$ nên theo tính chất đường phân giác trong của tam giác, ta có: \\\\ $\\frac{DA}{DC} = \\frac{BA}{BC} = \\frac{\\sqrt{%s}}{2\\sqrt{%s}} = \\frac{1}{2} \\Rightarrow \\vec{DA} = -\\frac{1}{2}\\vec{DC} \\Leftrightarrow 2\\vec{DA} + \\vec{DC} = \\vec{0}$. \\\\ Do đó toạ độ điểm $D$ thoả mãn: \\\\ $\\begin{cases} x_D = \\frac{2x_A + x_C}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\\\ y_D = \\frac{2y_A + y_C}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\\\ z_D = \\frac{2z_A + z_C}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\end{cases}$ \\\\ Vậy tọa độ điểm $D$ là $\\left(%s;%s;%s\\right)$."""
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
            len_ba_sq,
            len_ba_sq,
            len_ba_sq,
            xa,
            xc,
            str_xd,
            ya,
            yc,
            str_yd,
            za,
            zc,
            str_zd,
            str_xd,
            str_yd,
            str_zd,
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
    