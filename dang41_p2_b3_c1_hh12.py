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


def bt_dang41_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hai điểm A, B[cite: 20]:
    # A(xa; ya; 0) nằm trên (Oxy), B(xb; 0; zb) nằm trên (Oxz)[cite: 20]
    # xa + xb = 0 để trung điểm AB có hoành độ bằng 0[cite: 20]
    # Tìm M(m; 0; 0) thuộc tia Ox (m > 0) để tam giác ABM vuông tại M:
    # MA = (xa - m; ya; 0), MB = (xb - m; 0; zb)
    # MA . MB = 0 <=> (m - xa)(m - xb) + 0 + 0 = 0
    # <=> m^2 - (xa + xb)m + xa*xb = 0. Do xb = -xa nên m^2 - xa^2 = 0 <=> m = |xa|
    while True:
        xa_val = random.choice([1, 2, 3])
        ya_val = random.choice([2, 3, 4])
        za_val = 0
    
        xb_val = -xa_val
        yb_val = 0
        zb_val = random.choice([2, 3, 4])
    
        # Tích có hướng [OA, OB] để tìm phương của vectơ u[cite: 20]
        # OA = (xa, ya, 0), OB = (xb, 0, zb)
        cp_x = ya_val * zb_val
        cp_y = -xa_val * zb_val
        cp_z = -ya_val * xb_val  # = ya_val * xa_val > 0
    
        # u cùng phương với [OA, OB] => u = k * (cp_x, cp_y, cp_z)
        # Vectơ v = 2i - 3j + 4k[cite: 20]
        v_i, v_j, v_k = 2, -3, 4
        dot_base = cp_x * v_i + cp_y * v_j + cp_z * v_k
    
        if dot_base != 0 and (xa_val, ya_val, za_val) != (xb_val, yb_val, zb_val):
            # Chọn hệ số k_scale nguyên để phép tính vectơ u đẹp
            k_scale = random.choice([1, 2])
            dot_target = dot_base * k_scale
    
            u_x = cp_x * k_scale
            u_y = cp_y * k_scale
            u_z = cp_z * k_scale
    
            len_u_sq = u_x**2 + u_y**2 + u_z**2
            len_u = math.sqrt(len_u_sq)
            break
    
    # 1. Khoảng cách từ A đến mặt phẳng (Oxz): d(A, (Oxz)) = |yA|[cite: 20]
    dist_a_oxz = abs(ya_val)
    dist_a_oxz_s = dist_a_oxz + random.choice([-1, 1])
    
    # 2. Hoành độ trung điểm của đoạn thẳng AB: x_I = (xa + xb)/2 = 0[cite: 20]
    xi_true = (xa_val + xb_val) // 2
    xi_false = xi_true + random.choice([1, 2])
    
    # 3. Độ dài vectơ u và so sánh với bound_u[cite: 20]
    bound_u = int(len_u)
    is_len_u_gt = len_u > bound_u
    str_len_u = latex(sp.sqrt(len_u_sq))
    
    # 4. Tồn tại điểm M thuộc tia Ox sao cho tam giác ABM vuông tại M thì OM = |xa_val|[cite: 20]
    # m = xa_val (vì M thuộc tia Ox nên m > 0) => OM = xa_val[cite: 20]
    om_val = xa_val
    bound_om_sq = om_val**2 - 1 if om_val**2 > 1 else 2
    is_om_gt = om_val**2 > bound_om_sq
    str_bound_om = latex(sp.sqrt(bound_om_sq))
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho $A(%s;%s;%s); B(%s;%s;%s)$."""
        % (xa_val, ya_val, za_val, xb_val, yb_val, zb_val)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Điểm A cách mặt phẳng (Oxz) một khoảng bằng dist_a_oxz[cite: 20]
    nb_da_1_d = "\\True Điểm $A(%s;%s;%s)$ cách mặt phẳng $(Oxz)$ một khoảng bằng $%s$" % (
        xa_val,
        ya_val,
        za_val,
        dist_a_oxz,
    )
    nb_da_1_s = "Điểm $A(%s;%s;%s)$ cách mặt phẳng $(Oxz)$ một khoảng bằng $%s$" % (
        xa_val,
        ya_val,
        za_val,
        dist_a_oxz_s,
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Mặt phẳng $(Oxz)$ có phương trình là $y = 0$. \\\\ Khoảng cách từ điểm $A(%s;%s;%s)$ đến mặt phẳng $(Oxz)$ là: \\\\ $d(A, (Oxz)) = |y_A| = |%s| = %s$."""
        % (
            xa_val,
            ya_val,
            za_val,
            ya_val,
            dist_a_oxz,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Trung điểm của đoạn thẳng AB có hoành độ bằng xi_true[cite: 20]
    th_da_1_d = "\\True Trung điểm của đoạn thẳng $AB$ có hoành độ bằng $%s$" % (
        xi_true
    )
    th_da_1_s = "Trung điểm của đoạn thẳng $AB$ có hoành độ bằng $%s$" % (
        xi_false
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Gọi $I$ là trung điểm của đoạn thẳng $AB$. Khi đó hoành độ của điểm $I$ là: \\\\ $x_I = \\frac{x_A + x_B}{2} = \\frac{%s + (%s)}{2} = %s$. \\\\ Do đó trung điểm của đoạn thẳng $AB$ có hoành độ bằng $%s$."""
        % (
            xa_val,
            xb_val,
            xi_true,
            xi_true,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Vectơ u thỏa mãn u perp OA, u perp OB và tích vô hướng[cite: 20]
    if is_len_u_gt:
        vd_da_1_d = (
            "\\True Nếu vectơ $\\vec{u}$ thỏa mãn $\\vec{u} \\perp \\vec{OA}, \\vec{u} \\perp \\vec{OB}, \\vec{u} \\cdot (2\\vec{i} - 3\\vec{j} + 4\\vec{k}) = %s$ thì $|\\vec{u}| > %s$"
            % (dot_target, bound_u)
        )
        vd_da_1_s = (
            "Nếu vectơ $\\vec{u}$ thỏa mãn $\\vec{u} \\perp \\vec{OA}, \\vec{u} \\perp \\vec{OB}, \\vec{u} \\cdot (2\\vec{i} - 3\\vec{j} + 4\\vec{k}) = %s$ thì $|\\vec{u}| < %s$"
            % (dot_target, bound_u)
        )
    else:
        vd_da_1_d = (
            "\\True Nếu vectơ $\\vec{u}$ thỏa mãn $\\vec{u} \\perp \\vec{OA}, \\vec{u} \\perp \\vec{OB}, \\vec{u} \\cdot (2\\vec{i} - 3\\vec{j} + 4\\vec{k}) = %s$ thì $|\\vec{u}| < %s$"
            % (dot_target, bound_u)
        )
        vd_da_1_s = (
            "Nếu vectơ $\\vec{u}$ thỏa mãn $\\vec{u} \\perp \\vec{OA}, \\vec{u} \\perp \\vec{OB}, \\vec{u} \\cdot (2\\vec{i} - 3\\vec{j} + 4\\vec{k}) = %s$ thì $|\\vec{u}| > %s$"
            % (dot_target, bound_u)
        )
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có $\\vec{OA} = (%s;%s;%s)$ và $\\vec{OB} = (%s;%s;%s)$. \\\\ Vectơ cùng vuông góc với cả hai vectơ $\\vec{OA}, \\vec{OB}$ cùng phương với tích có hướng $[\\vec{OA}, \\vec{OB}]$: \\\\ $[\\vec{OA}, \\vec{OB}] = \\left( \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix} \\right) = (%s;%s;%s)$. \\\\ Do đó đặt $\\vec{u} = k(%s;%s;%s) = (%sk;%sk;%sk)$. \\\\ Mặt khác, vectơ $\\vec{v} = 2\\vec{i} - 3\\vec{j} + 4\\vec{k} = (2;-3;4)$. \\\\ Theo giả thiết: \\\\ $\\vec{u} \\cdot \\vec{v} = %s \\Leftrightarrow (%sk) \\cdot 2 + (%sk) \\cdot (-3) + (%sk) \\cdot 4 = %s \\Leftrightarrow %sk = %s \\Leftrightarrow k = %s$. \\\\ Suy ra $\\vec{u} = (%s;%s;%s) \\Rightarrow |\\vec{u}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = %s \\approx %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            xa_val,
            ya_val,
            za_val,
            xb_val,
            yb_val,
            zb_val,
            ya_val,
            za_val,
            yb_val,
            zb_val,
            za_val,
            xa_val,
            zb_val,
            xb_val,
            xa_val,
            ya_val,
            xb_val,
            yb_val,
            cp_x,
            cp_y,
            cp_z,
            cp_x,
            cp_y,
            cp_z,
            cp_x,
            cp_y,
            cp_z,
            dot_target,
            cp_x,
            cp_y,
            cp_z,
            dot_target,
            dot_base,
            dot_target,
            k_scale,
            u_x,
            u_y,
            u_z,
            u_x,
            u_y,
            u_z,
            str_len_u,
            str(round(len_u, 2)).replace(".", ","),
            str(round(len_u, 2)).replace(".", ","),
            ">" if is_len_u_gt else "<",
            bound_u,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Tồn tại M thuộc tia Ox sao cho tam giác ABM vuông tại M thì OM > sqrt(bound_om_sq)[cite: 20]
    if is_om_gt:
        vdc_da_1_d = (
            "\\True Tồn tại điểm $M$ thuộc tia $Ox$ sao cho tam giác $ABM$ vuông tại $M$ thì $OM > %s$"
            % (str_bound_om)
        )
        vdc_da_1_s = (
            "Tồn tại điểm $M$ thuộc tia $Ox$ sao cho tam giác $ABM$ vuông tại $M$ thì $OM < %s$"
            % (str_bound_om)
        )
    else:
        vdc_da_1_d = (
            "\\True Tồn tại điểm $M$ thuộc tia $Ox$ sao cho tam giác $ABM$ vuông tại $M$ thì $OM < %s$"
            % (str_bound_om)
        )
        vdc_da_1_s = (
            "Tồn tại điểm $M$ thuộc tia $Ox$ sao cho tam giác $ABM$ vuông tại $M$ thì $OM > %s$"
            % (str_bound_om)
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì điểm $M$ thuộc tia $Ox$ nên tọa độ của điểm $M$ có dạng $M(m;0;0)$ với $m > 0$. \\\\ Khi đó ta có tọa độ các vectơ: \\\\ $\\vec{MA} = (x_A - m; y_A - 0; z_A - 0) = (%s - m; %s; 0)$. \\\\ $\\vec{MB} = (x_B - m; y_B - 0; z_B - 0) = (%s - m; 0; %s)$. \\\\ Tam giác $ABM$ vuông tại $M$ khi và chỉ khi: \\\\ $\\vec{MA} \\cdot \\vec{MB} = 0 \\Leftrightarrow (%s - m)(%s - m) + %s \\cdot 0 + 0 \\cdot %s = 0$ \\\\ $\\Leftrightarrow m^2 - (%s + (%s))m + (%s) \\cdot (%s) = 0$ \\\\ $\\Leftrightarrow m^2 - %s = 0 \\Leftrightarrow m = %s$ (vì $m > 0$). \\\\ Suy ra tọa độ điểm $M$ là $M(%s;0;0)$. \\\\ Khi đó khoảng cách $OM = |m| = %s = \\sqrt{%s}$. \\\\ So sánh với $%s = \\sqrt{%s}$, vì $%s %s %s$ nên khẳng định là %s."""
        % (
            xa_val,
            ya_val,
            xb_val,
            zb_val,
            xa_val,
            xb_val,
            ya_val,
            zb_val,
            xa_val,
            xb_val,
            xa_val,
            xb_val,
            om_val**2,
            om_val,
            om_val,
            om_val,
            om_val**2,
            str_bound_om,
            bound_om_sq,
            om_val**2,
            ">" if is_om_gt else "<",
            bound_om_sq,
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
    