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


def bt_dang11_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên tọa độ các điểm A, B, C không thẳng hàng
    while True:
        xa, ya, za = (
            random.randint(-3, 3),
            random.randint(-3, 3),
            random.randint(-3, 3),
        )
        xb, yb, zb = (
            random.randint(-3, 3),
            random.randint(-3, 3),
            random.randint(-3, 3),
        )
        xc, yc, zc = (
            random.randint(-3, 3),
            random.randint(-3, 3),
            random.randint(-3, 3),
        )
    
        # Đảm bảo B không nằm trên trục Oy để đoạn BB' có độ dài > 0
        if xb == 0 and zb == 0:
            continue
    
        # Vectơ BC và BA
        bc_x, bc_y, bc_z = xc - xb, yc - yb, zc - zb
        ba_x, ba_y, ba_z = xa - xb, ya - yb, za - zb
    
        # Tích có hướng [BA, BC] để kiểm tra ba điểm không thẳng hàng
        cp_x = ba_y * bc_z - ba_z * bc_y
        cp_y = ba_z * bc_x - ba_x * bc_z
        cp_z = ba_x * bc_y - ba_y * bc_x
    
        bc_sq = bc_x**2 + bc_y**2 + bc_z**2
        dot_ba_bc = ba_x * bc_x + ba_y * bc_y + ba_z * bc_z
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and bc_sq != 0
            and dot_ba_bc != 0
            and dot_ba_bc != bc_sq
        ):
            break
    
    # 1. Hình chiếu của A lên trục Ox: A'(xa; 0; 0)
    xa_prime, ya_prime, za_prime = xa, 0, 0
    
    # 2. Điểm đối xứng B' của B qua trục Oy: B'(-xb; yb; -zb)
    # BB' = 2 * sqrt(xb^2 + zb^2)
    bb_prime_inner = xb**2 + zb**2
    bb_prime_val = sp.sqrt(bb_prime_inner)
    
    if bb_prime_inner in [1, 4, 9, 16, 25]:
        len_bb_prime_str = str(2 * int(math.isqrt(bb_prime_inner)))
        len_bb_prime_str_s = str(2 * int(math.isqrt(bb_prime_inner)) + 2)
    else:
        len_bb_prime_str = "2\\sqrt{%s}" % bb_prime_inner
        len_bb_prime_str_s = "2\\sqrt{%s}" % (bb_prime_inner + 2)
    
    # 3. Điểm đối xứng C' của C qua mặt phẳng (Oxy): C'(xc; yc; -zc) => tung độ bằng yc
    tung_do_c_prime = yc
    tung_do_c_prime_s = -yc if yc != 0 else 2
    
    # 4. Chân đường cao H kẻ từ A của tam giác ABC lên cạnh BC
    # H thuộc đường thẳng BC: H = B + t*BC
    # t = (BA . BC) / (BC . BC)
    t_val = Rational(dot_ba_bc, bc_sq)
    xh_val = xb + t_val * bc_x
    yh_val = yb + t_val * bc_y
    zh_val = zb + t_val * bc_z
    
    str_xh = format_fraction_latex(xh_val.p, xh_val.q)
    str_yh = format_fraction_latex(yh_val.p, yh_val.q)
    str_zh = format_fraction_latex(zh_val.p, zh_val.q)
    
    # Tọa độ sai của H (đổi dấu hoành độ hoặc sai phân số)
    str_xh_s = (
        format_fraction_latex(-xh_val.p, xh_val.q)
        if xh_val != 0
        else format_fraction_latex(xh_val.p + 1, xh_val.q)
    )
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ toạ độ $Oxyz$, cho tam giác $ABC$ với $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Phát biểu a: Hình chiếu của A lên trục Ox
    nb_da_1_d = (
        "\\True Gọi $A'$ là hình chiếu của $A$ lên trục $Ox$ thì $A'(%s;%s;%s)$"
        % (xa_prime, ya_prime, za_prime)
    )
    nb_da_1_s = (
        "Gọi $A'$ là hình chiếu của $A$ lên trục $Ox$ thì $A'(%s;%s;%s)$"
        % (0, ya, za)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Hình chiếu vuông góc của điểm $A(%s;%s;%s)$ lên trục $Ox$ giữ nguyên hoành độ, tung độ và cao độ bằng $0$. \\\\ Do đó ta được $A'(%s;0;0)$."""
        % (xa, ya, za, xa)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Phát biểu b: Điểm B' đối xứng với B qua trục Oy
    th_da_1_d = (
        "\\True Gọi $B'$ là điểm đối xứng với $B$ qua trục $Oy$ thì độ dài $BB'$ là $%s$"
        % (len_bb_prime_str)
    )
    th_da_1_s = (
        "Gọi $B'$ là điểm đối xứng với $B$ qua trục $Oy$ thì độ dài $BB'$ là $%s$"
        % (len_bb_prime_str_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Điểm $B'$ đối xứng với điểm $B(%s;%s;%s)$ qua trục $Oy$ có toạ độ là $B'(%s;%s;%s)$. \\\\ Ta có $\\vec{BB'} = (%s - %s; %s - %s; %s - %s) = (%s;0;%s)$. \\\\ Do đó độ dài đoạn thẳng $BB' = \\sqrt{(%s)^2 + 0^2 + (%s)^2} = %s$."""
        % (
            xb,
            yb,
            zb,
            -xb,
            yb,
            -zb,
            -xb,
            xb,
            yb,
            yb,
            -zb,
            zb,
            -2 * xb,
            -2 * zb,
            -2 * xb,
            -2 * zb,
            len_bb_prime_str,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Phát biểu c: C' đối xứng với C qua mặt phẳng (Oxy)
    vd_da_1_d = (
        "\\True Gọi $C'$ là điểm đối xứng với $C$ qua mặt phẳng $(Oxy)$ thì $C'$ có tung độ bằng $%s$"
        % (tung_do_c_prime)
    )
    vd_da_1_s = (
        "Gọi $C'$ là điểm đối xứng với $C$ qua mặt phẳng $(Oxy)$ thì $C'$ có tung độ bằng $%s$"
        % (tung_do_c_prime_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Điểm $C'$ đối xứng với điểm $C(%s;%s;%s)$ qua mặt phẳng toạ độ $(Oxy)$ giữ nguyên hoành độ và tung độ, đổi dấu cao độ. \\\\ Do đó $C'(%s;%s;%s)$, suy ra tung độ của điểm $C'$ bằng $%s$."""
        % (xc, yc, zc, xc, yc, -zc, yc)
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Phát biểu d: Tọa độ chân đường cao H kẻ từ A của tam giác ABC
    vdc_da_1_d = (
        "\\True Gọi $H$ là chân đường cao kẻ từ $A$ của tam giác $ABC$. Toạ độ của điểm $H$ là $H\\left(%s;%s;%s\\right)$"
        % (str_xh, str_yh, str_zh)
    )
    vdc_da_1_s = (
        "Gọi $H$ là chân đường cao kẻ từ $A$ của tam giác $ABC$. Toạ độ của điểm $H$ là $H\\left(%s;%s;%s\\right)$"
        % (str_xh_s, str_yh, str_zh)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_t_frac = format_fraction_latex(t_val.p, t_val.q)
    
    loigiai_vdc_1 = (
        """Ta có $\\vec{BC} = (x_C - x_B; y_C - y_B; z_C - z_B) = (%s;%s;%s)$. \\\\ Vì điểm $H$ thuộc đường thẳng $BC$ nên ta có $\\vec{BH} = t\\vec{BC} = (%st; %st; %st)$ với $t \\in \\mathbb{R}$. \\\\ Suy ra tọa độ điểm $H$ có dạng: $H(%s + %st; %s + %st; %s + %st)$. \\\\ Khi đó: $\\vec{AH} = (x_H - x_A; y_H - y_A; z_H - z_A) = (%s + %st; %s + %st; %s + %st)$. \\\\ Do $AH \\perp BC$ nên $\\vec{AH} \\cdot \\vec{BC} = 0$: \\\\ $\\Leftrightarrow (%s)(%s + %st) + (%s)(%s + %st) + (%s)(%s + %st) = 0$ \\\\ $\\Leftrightarrow %st - (%s) = 0 \\Leftrightarrow t = %s$. \\\\ Thay $t = %s$ vào tọa độ điểm $H$, ta được $H\\left(%s;%s;%s\\right)$."""
        % (
            bc_x,
            bc_y,
            bc_z,
            bc_x,
            bc_y,
            bc_z,
            xb,
            bc_x,
            yb,
            bc_y,
            zb,
            bc_z,
            xb - xa,
            bc_x,
            yb - ya,
            bc_y,
            zb - za,
            bc_z,
            bc_x,
            xb - xa,
            bc_x,
            bc_y,
            yb - ya,
            bc_y,
            bc_z,
            zb - za,
            bc_z,
            bc_sq,
            dot_ba_bc,
            str_t_frac,
            str_t_frac,
            str_xh,
            str_yh,
            str_zh,
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
    