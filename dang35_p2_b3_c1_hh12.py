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


def bt_dang35_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A, B, C không thẳng hàng
    while True:
        xa = random.randint(-2, 2)
        ya = random.randint(-1, 2)
        za = random.choice([2, 3, 4])
    
        xb = random.randint(1, 4)
        yb = random.randint(-4, -1)
        zb = random.choice([-3, -2, -1, 1, 2])
    
        xc = random.randint(-3, 0)
        yc = random.randint(1, 4)
        zc = random.randint(-1, 2)
    
        # Vectơ AB, AC
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        # Tích có hướng [AB, AC] để đảm bảo ba điểm không thẳng hàng
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        len_ac_sq = ac_x**2 + ac_y**2 + ac_z**2
        dot_ab_ac = ab_x * ac_x + ab_y * ac_y + ab_z * ac_z
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and len_ac_sq > 0
            and dot_ab_ac != 0
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
        ):
            break
    
    # 1. Tích vô hướng AB . AC[cite: 21]
    dot_ab_ac_true = dot_ab_ac
    dot_ab_ac_false = dot_ab_ac + random.choice([-5, -3, 3, 5])
    
    # 2. Điểm M(a;b;c) thỏa mãn MA + MB - 3MC = 0 <=> M = 3C - A - B[cite: 21]
    # OM = (OA + OB - 3OC) / (1 + 1 - 3) = 3OC - OA - OB[cite: 21]
    ma_val = 3 * xc - xa - xb
    mb_val = 3 * yc - ya - yb
    mc_val = 3 * zc - za - zb
    sum_abc_m = ma_val + mb_val + mc_val
    sum_abc_m_s = sum_abc_m + random.choice([-2, -1, 1, 2])
    
    # 3. Chân đường cao H(m;n;p) kẻ từ B của tam giác ABC lên đường thẳng AC[cite: 21]
    # H = A + t * AC với t = (AB . AC) / |AC|^2[cite: 21]
    t_h = Rational(dot_ab_ac, len_ac_sq)
    h_m = xa + t_h * ac_x
    h_n = ya + t_h * ac_y
    h_p = za + t_h * ac_z
    
    expr_h = h_m + 2 * h_n + h_p
    str_expr_h_true = format_fraction_latex(expr_h.p, expr_h.q)
    target_expr_h_s = expr_h.p // expr_h.q + random.choice([1, 2])
    
    # 4. Giá trị nhỏ nhất của P = MA^2 + MB^2 - MC^2 với M in (Oxy)[cite: 21]
    # Gọi I là điểm thỏa mãn IA + IB - IC = 0 <=> I = A + B - C[cite: 21]
    xi = xa + xb - xc
    yi = ya + yb - yc
    zi = za + zb - zc
    
    # P = MI^2 + IA^2 + IB^2 - IC^2[cite: 21]
    ia_sq = (xa - xi) ** 2 + (ya - yi) ** 2 + (za - zi) ** 2
    ib_sq = (xb - xi) ** 2 + (yb - yi) ** 2 + (zb - zi) ** 2
    ic_sq = (xc - xi) ** 2 + (yc - yi) ** 2 + (zc - zi) ** 2
    const_k = ia_sq + ib_sq - ic_sq
    
    # Vì M in (Oxy) nên M(x; y; 0), MI^2 = (x - xI)^2 + (y - yI)^2 + zI^2 >= zI^2[cite: 21]
    # min P = zI^2 + const_k khi M(xI; yI; 0)[cite: 21]
    min_p = zi**2 + const_k
    min_p_s = min_p + random.choice([15, 20, 25, -15])
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Trong không gian với hệ toạ độ $Oxyz$ cho $3$ điểm $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: AB . AC = dot_ab_ac[cite: 21]
    nb_da_1_d = "\\True $\\vec{AB} \\cdot \\vec{AC} = %s$" % (dot_ab_ac_true)
    nb_da_1_s = "$\\vec{AB} \\cdot \\vec{AC} = %s$" % (dot_ab_ac_false)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Tích vô hướng của hai vectơ là: \\\\ $\\vec{AB} \\cdot \\vec{AC} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$."""
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
            xc,
            xa,
            yc,
            ya,
            zc,
            za,
            ac_x,
            ac_y,
            ac_z,
            ab_x,
            ac_x,
            ab_y,
            ac_y,
            ab_z,
            ac_z,
            dot_ab_ac_true,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Điểm M thỏa mãn MA + MB - 3MC = 0 thì a + b + c[cite: 21]
    th_da_1_d = (
        "\\True Gọi $M(a;b;c)$ là điểm thoả mãn $\\vec{MA} + \\vec{MB} - 3\\vec{MC} = \\vec{0}$. Khi đó $a + b + c = %s$"
        % (sum_abc_m)
    )
    th_da_1_s = (
        "Gọi $M(a;b;c)$ là điểm thoả mãn $\\vec{MA} + \\vec{MB} - 3\\vec{MC} = \\vec{0}$. Khi đó $a + b + c = %s$"
        % (sum_abc_m_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có hệ thức: \\\\ $\\vec{MA} + \\vec{MB} - 3\\vec{MC} = \\vec{0} \\Leftrightarrow (\\vec{OA} - \\vec{OM}) + (\\vec{OB} - \\vec{OM}) - 3(\\vec{OC} - \\vec{OM}) = \\vec{0}$ \\\\ $\\Leftrightarrow \\vec{OM} = 3\\vec{OC} - \\vec{OA} - \\vec{OB}$. \\\\ Suy ra tọa độ của điểm $M(a;b;c)$ là: \\\\ $\\begin{cases} a = 3x_C - x_A - x_B = 3 \\cdot (%s) - (%s) - (%s) = %s \\\\ b = 3y_C - y_A - y_B = 3 \\cdot (%s) - (%s) - (%s) = %s \\\\ c = 3z_C - z_A - z_B = 3 \\cdot (%s) - (%s) - (%s) = %s \\end{cases} \\Rightarrow M(%s;%s;%s)$. \\\\ Khi đó: $a + b + c = %s + (%s) + (%s) = %s$."""
        % (
            xc,
            xa,
            xb,
            ma_val,
            yc,
            ya,
            yb,
            mb_val,
            zc,
            za,
            zb,
            mc_val,
            ma_val,
            mb_val,
            mc_val,
            ma_val,
            mb_val,
            mc_val,
            sum_abc_m,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Chân đường cao H(m;n;p) kẻ từ B thì m + 2n + p[cite: 21]
    vd_da_1_d = (
        "\\True Gọi $H(m;n;p)$ là chân đường cao kẻ từ $B$ của tam giác $ABC$. Khi đó $m + 2n + p = %s$"
        % (str_expr_h_true)
    )
    vd_da_1_s = (
        "Gọi $H(m;n;p)$ là chân đường cao kẻ từ $B$ của tam giác $ABC$. Khi đó $m + 2n + p = %s$"
        % (target_expr_h_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    str_th = format_fraction_latex(t_h.p, t_h.q)
    str_hm = format_fraction_latex(h_m.p, h_m.q)
    str_hn = format_fraction_latex(h_n.p, h_n.q)
    str_hp = format_fraction_latex(h_p.p, h_p.q)
    
    loigiai_vd_1 = (
        """Đường thẳng $AC$ đi qua điểm $A(%s;%s;%s)$ và nhận vectơ $\\vec{AC} = (%s;%s;%s)$ làm vectơ chỉ phương. \\\\ Vì $H$ thuộc đường thẳng $AC$ nên tọa độ của điểm $H$ có dạng: \\\\ $H(%s + (%s)t; %s + (%s)t; %s + (%s)t)$. \\\\ Khi đó: $\\vec{BH} = (%s + (%s)t; %s + (%s)t; %s + (%s)t)$. \\\\ Vì $H$ là chân đường cao kẻ từ $B$ của tam giác $ABC$ nên $BH \\perp AC \\Leftrightarrow \\vec{BH} \\cdot \\vec{AC} = 0$: \\\\ $(%s) \\cdot [%s + (%s)t] + (%s) \\cdot [%s + (%s)t] + (%s) \\cdot [%s + (%s)t] = 0$ \\\\ $\\Leftrightarrow %st + (%s) = 0 \\Leftrightarrow t = %s$. \\\\ Suy ra tọa độ điểm $H$ là $H\\left(%s;%s;%s\\right)$. \\\\ Khi đó: $m + 2n + p = %s + 2 \\cdot \\left(%s\\right) + %s = %s$."""
        % (
            xa,
            ya,
            za,
            ac_x,
            ac_y,
            ac_z,
            xa,
            ac_x,
            ya,
            ac_y,
            za,
            ac_z,
            xa - xb,
            ac_x,
            ya - yb,
            ac_y,
            za - zb,
            ac_z,
            ac_x,
            xa - xb,
            ac_x,
            ac_y,
            ya - yb,
            ac_y,
            ac_z,
            za - zb,
            ac_z,
            len_ac_sq,
            -dot_ab_ac,
            str_th,
            str_hm,
            str_hn,
            str_hp,
            str_hm,
            str_hn,
            str_hp,
            str_expr_h_true,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Giá trị nhỏ nhất của P = MA^2 + MB^2 - MC^2[cite: 21]
    vdc_da_1_d = (
        "\\True Với $M(x;y;z)$ là điểm tuỳ ý thuộc mặt phẳng $(Oxy)$. Giá trị nhỏ nhất của biểu thức $P = MA^2 + MB^2 - MC^2$ bằng $%s$"
        % (min_p)
    )
    vdc_da_1_s = (
        "Với $M(x;y;z)$ là điểm tuỳ ý thuộc mặt phẳng $(Oxy)$. Giá trị nhỏ nhất của biểu thức $P = MA^2 + MB^2 - MC^2$ bằng $%s$"
        % (min_p_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Gọi điểm $I$ thỏa mãn hệ thức vectơ $\\vec{IA} + \\vec{IB} - \\vec{IC} = \\vec{0} \\Leftrightarrow \\vec{OI} = \\vec{OA} + \\vec{OB} - \\vec{OC}$. \\\\ Tọa độ điểm $I$ là: \\\\ $\\begin{cases} x_I = x_A + x_B - x_C = %s + (%s) - (%s) = %s \\\\ y_I = y_A + y_B - y_C = %s + (%s) - (%s) = %s \\\\ z_I = z_A + z_B - z_C = %s + (%s) - (%s) = %s \\end{cases} \\Rightarrow I(%s;%s;%s)$. \\\\ Khi đó ta có: \\\\ $P = (\\vec{MI} + \\vec{IA})^2 + (\\vec{MI} + \\vec{IB})^2 - (\\vec{MI} + \\vec{IC})^2$ \\\\ $= MI^2 + 2\\vec{MI} \\cdot (\\vec{IA} + \\vec{IB} - \\vec{IC}) + IA^2 + IB^2 - IC^2 = MI^2 + IA^2 + IB^2 - IC^2$. \\\\ Tính độ dài các đoạn thẳng: \\\\ $IA^2 = (%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2 = %s$. \\\\ $IB^2 = (%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2 = %s$. \\\\ $IC^2 = (%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2 = %s$. \\\\ Suy ra $IA^2 + IB^2 - IC^2 = %s + %s - %s = %s$. \\\\ Vì $M \\in (Oxy)$ nên $M$ có tọa độ dạng $M(x;y;0)$, do đó: \\\\ $MI^2 = (x - %s)^2 + (y - (%s))^2 + (0 - %s)^2 = (x - %s)^2 + (y - (%s))^2 + %s \\ge %s$. \\\\ Đẳng thức xảy ra khi $x = %s, y = %s$. \\\\ Khi đó giá trị nhỏ nhất của $P$ là: \\\\ $P_{\\min} = %s + (%s) = %s$."""
        % (
            xa,
            xb,
            xc,
            xi,
            ya,
            yb,
            yc,
            yi,
            za,
            zb,
            zc,
            zi,
            xi,
            yi,
            zi,
            xa,
            xi,
            ya,
            yi,
            za,
            zi,
            ia_sq,
            xb,
            xi,
            yb,
            yi,
            zb,
            zi,
            ib_sq,
            xc,
            xi,
            yc,
            yi,
            zc,
            zi,
            ic_sq,
            ia_sq,
            ib_sq,
            ic_sq,
            const_k,
            xi,
            yi,
            zi,
            xi,
            yi,
            zi**2,
            zi**2,
            xi,
            yi,
            zi**2,
            const_k,
            min_p,
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
    