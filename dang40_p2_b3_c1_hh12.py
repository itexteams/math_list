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


def bt_dang40_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hai điểm A, B cùng phía đối với (Oxy): zA > 0, zB > 0
    # Đảm bảo bài toán tìm GTNN của MA + MB trên (Oxy) bằng điểm đối xứng A' qua (Oxy) cho kết quả đẹp
    while True:
        za = random.choice([2, 3, 4])
        zb = random.choice([1, 2])
    
        # Tọa độ B
        xb = random.choice([1, 2, -1, -2])
        yb = 0  # Cho yb = 0 như đề gốc để NB trên trục Oy đơn giản, đẹp
        # B cách Oy một khoảng d(B, Oy) = sqrt(xb^2 + zb^2)
    
        # Chọn điểm A sao cho zA + zB chia hết cho 1 hoặc phân số tối giản đẹp
        xa = random.randint(3, 5) if xb > 0 else random.randint(-5, -3)
        ya = random.choice([-4, -3, 3, 4])
    
        # Trung điểm I của AB có cao độ (za + zb)/2
        zi_val = Rational(za + zb, 2)
    
        # Điểm đối xứng của A qua (Oxy) là A'(xa; ya; -za)
        # Giao điểm của A'B với (Oxy) là M(x; y; 0):
        # Vectơ A'B = (xb - xa; yb - ya; zb + za)
        # Đường thẳng A'B: (x - xb) / (xa - xb) = (y - yb) / (ya - yb) = (z - zb) / (-za - zb)
        # z = 0 => t = -zb / (-za - zb) = zb / (za + zb)
        # xM = xb + t * (xa - xb) = (za * xb + zb * xa) / (za + zb)
        # yM = yb + t * (ya - yb) = (za * yb + zb * ya) / (za + zb) = (zb * ya) / (za + zb)
        xm_val = Rational(za * xb + zb * xa, za + zb)
        ym_val = Rational(zb * ya, za + zb)
    
        val_expr_d = xm_val**2 - ym_val**2
        if (
            (xa, ya, za) != (xb, yb, zb)
            and (xb**2 + zb**2) > 0
            and val_expr_d.q <= 4
        ):
            break
    
    # 1. Vectơ AB = (xb - xa; yb - ya; zb - za)
    ab_x = xb - xa
    ab_y = yb - ya
    ab_z = zb - za
    
    ab_x_s = ab_x
    ab_y_s = -ab_y if ab_y != 0 else 2
    ab_z_s = ab_z
    
    # 2. Trung điểm AB có cao độ bằng zi_val
    str_zi_true = format_fraction_latex(za + zb, 2)
    # Tạo giá trị sai (nhầm thành cao độ của B hoặc số nguyên khác)
    zi_false = zb if zi_val != zb else zb + 1
    str_zi_false = str(zi_false)
    
    # 3. Với N bất kỳ thuộc trục tung (Oy): N(0; y; 0)
    # NB^2 = (0 - xb)^2 + (y - yb)^2 + (0 - zb)^2 = xb^2 + zb^2 + y^2 >= xb^2 + zb^2
    # NB >= sqrt(xb^2 + zb^2)
    min_nb_sq = xb**2 + zb**2
    str_min_nb = latex(sp.sqrt(min_nb_sq))
    
    # 4. Tồn tại điểm M(x; y; 0) để MA + MB min thì x^2 - y^2 = val_expr_d
    str_val_d_true = format_fraction_latex(val_expr_d.p, val_expr_d.q)
    target_int_d = int(val_expr_d)
    if target_int_d == val_expr_d:
        target_int_d_s = target_int_d + random.choice([-2, -1, 1, 2])
    else:
        target_int_d_s = target_int_d + 1
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$ cho các điểm $A(%s;%s;%s), B(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Vectơ AB
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
    # Khẳng định b: Trung điểm đoạn thẳng AB có cao độ bằng zi_val
    th_da_1_d = (
        "\\True Trung điểm đoạn thẳng $AB$ có cao độ bằng $%s$" % (str_zi_true)
    )
    th_da_1_s = (
        "Trung điểm đoạn thẳng $AB$ có cao độ bằng $%s$" % (str_zi_false)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Gọi $I$ là trung điểm của đoạn thẳng $AB$. Khi đó cao độ của điểm $I$ là: \\\\ $z_I = \\frac{z_A + z_B}{2} = \\frac{%s + (%s)}{2} = %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            za,
            zb,
            str_zi_true,
            str_zi_true,
            "=" if "\\True" in th_da_1 else "\\neq",
            str_zi_true if "\\True" in th_da_1 else str_zi_false,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Với điểm N bất kỳ thuộc trục tung thì NB >= str_min_nb
    vd_da_1_d = (
        "\\True Với điểm $N$ bất kỳ thuộc trục tung thì $NB \\ge %s$" % (str_min_nb)
    )
    vd_da_1_s = (
        "Với điểm $N$ bất kỳ thuộc trục tung thì $NB \\le %s$" % (str_min_nb)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì điểm $N$ thuộc trục tung $Oy$ nên tọa độ của điểm $N$ có dạng $N(0;y;0)$. \\\\ Khi đó khoảng cách giữa hai điểm $N$ và $B(%s;%s;%s)$ là: \\\\ $NB = \\sqrt{(0 - (%s))^2 + (y - (%s))^2 + (0 - (%s))^2} = \\sqrt{(%s)^2 + (%s)^2 + (y - (%s))^2} = \\sqrt{%s + (y - (%s))^2}$. \\\\ Do $(y - (%s))^2 \\ge 0$ với mọi $y \\in \\mathbb{R}$ nên ta có: \\\\ $NB \\ge \\sqrt{%s} = %s$. \\\\ Đẳng thức xảy ra khi $y = %s$, tức là khi $N(0;%s;0)$ là hình chiếu vuông góc của $B$ lên trục $Oy$."""
        % (
            xb,
            yb,
            zb,
            xb,
            yb,
            zb,
            xb,
            zb,
            yb,
            min_nb_sq,
            yb,
            yb,
            min_nb_sq,
            str_min_nb,
            yb,
            yb,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Tồn tại M(x; y; 0) sao cho MA + MB đạt GTNN thì x^2 - y^2 = ...
    vdc_da_1_d = (
        "\\True Tồn tại điểm $M(x;y;0)$ sao cho $MA + MB$ đạt giá trị nhỏ nhất thì $x^2 - y^2 = %s$"
        % (str_val_d_true)
    )
    vdc_da_1_s = (
        "Tồn tại điểm $M(x;y;0)$ sao cho $MA + MB$ đạt giá trị nhỏ nhất thì $x^2 - y^2 = %s$"
        % (target_int_d_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_xm = format_fraction_latex(xm_val.p, xm_val.q)
    str_ym = format_fraction_latex(ym_val.p, ym_val.q)
    
    loigiai_vdc_1 = (
        """Ta thấy $z_A = %s > 0$ và $z_B = %s > 0$ nên hai điểm $A, B$ nằm cùng phía đối với mặt phẳng tọa độ $(Oxy)$. \\\\ Gọi $A'$ là điểm đối xứng với điểm $A(%s;%s;%s)$ qua mặt phẳng $(Oxy)$, suy ra $A'(%s;%s;%s)$. \\\\ Với mọi điểm $M \\in (Oxy)$, ta có $MA = MA'$. \\\\ Khi đó: $MA + MB = MA' + MB \\ge A'B$. \\\\ Đẳng thức xảy ra khi và chỉ khi điểm $M$ là giao điểm của đoạn thẳng $A'B$ với mặt phẳng $(Oxy)$. \\\\ Ta có $\\vec{A'B} = (x_B - x_{A'}; y_B - y_{A'}; z_B - z_{A'}) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Phương trình tham số của đường thẳng $A'B$ là: \\\\ $\\begin{cases} x = %s + (%s)t \\\\ y = %s + (%s)t \\\\ z = %s + (%s)t \\end{cases}$. \\\\ Điểm $M(x;y;0) \\in (Oxy)$ tương ứng với $z = 0$: \\\\ $%s + (%s)t = 0 \\Leftrightarrow t = %s$. \\\\ Thay giá trị của $t$ vào, ta được tọa độ điểm $M$: \\\\ $\\begin{cases} x = %s + (%s) \\cdot \\left(%s\\right) = %s \\\\ y = %s + (%s) \\cdot \\left(%s\\right) = %s \\end{cases} \\Rightarrow M\\left(%s;%s;0\\right)$. \\\\ Khi đó: $x^2 - y^2 = \\left(%s\\right)^2 - \\left(%s\\right)^2 = %s$. \\\\ Do đó khẳng định là %s."""
        % (
            za,
            zb,
            xa,
            ya,
            za,
            xa,
            ya,
            -za,
            xb,
            xa,
            yb,
            ya,
            zb,
            -za,
            xb - xa,
            yb - ya,
            zb + za,
            xa,
            xb - xa,
            ya,
            yb - ya,
            -za,
            zb + za,
            -za,
            zb + za,
            format_fraction_latex(za, zb + za),
            xa,
            xb - xa,
            format_fraction_latex(za, zb + za),
            str_xm,
            ya,
            yb - ya,
            format_fraction_latex(za, zb + za),
            str_ym,
            str_xm,
            str_ym,
            str_xm,
            str_ym,
            str_val_d_true,
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
    