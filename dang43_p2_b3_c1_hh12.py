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


def bt_dang43_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    
    while True:
        xa = random.randint(-3, 3)
        ya = random.randint(-3, 3)
        za = random.randint(1, 4)
    
        xb = random.randint(-3, 3)
        yb = random.randint(-3, 3)
        zb = random.randint(-3, 3)
    
        xc = random.randint(-3, 3)
        yc = random.randint(-3, 3)
        zc = random.randint(-4, 0)
    
        # AB, AC, BC
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        bc_x = xc - xb
        bc_y = yc - yb
        bc_z = zc - zb
    
        # Tích có hướng [AB, AC] để kiểm tra tính không thẳng hàng
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        len_ab_sq = ab_x**2 + ab_y**2 + ab_z**2
        len_ac_sq = ac_x**2 + ac_y**2 + ac_z**2
        len_bc_sq = bc_x**2 + bc_y**2 + bc_z**2
    
        dot_ab_ac = ab_x * ac_x + ab_y * ac_y + ab_z * ac_z
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and len_ab_sq > 0
            and len_ac_sq > 0
            and len_bc_sq > 0
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
        ):
            break
    
    # 1. Trọng tâm G của tam giác ABC: G = (A + B + C) / 3[cite: 22]
    xg_num = xa + xb + xc
    yg_num = ya + yb + yc
    zg_num = za + zb + zc
    
    str_xg_true = format_fraction_latex(xg_num, 3)
    str_yg_true = format_fraction_latex(yg_num, 3)
    str_zg_true = format_fraction_latex(zg_num, 3)
    
    # Tọa độ sai của G (nhầm dấu một thành phần như trong đề gốc)[cite: 22]
    str_xg_false = format_fraction_latex(-xg_num if xg_num != 0 else 1, 3)
    
    # 2. Chu vi tam giác ABC = AB + BC + CA[cite: 22]
    str_p_true = "%s + %s + %s" % (
        latex(sp.sqrt(len_ab_sq)),
        latex(sp.sqrt(len_bc_sq)),
        latex(sp.sqrt(len_ac_sq)),
    )
    str_p_false = "%s + %s + %s" % (
        latex(sp.sqrt(len_ab_sq + random.choice([2, 4]))),
        latex(sp.sqrt(len_bc_sq)),
        latex(sp.sqrt(len_ac_sq)),
    )
    
    # 3. cos A = (AB . AC) / (|AB| * |AC|)[cite: 22]
    cos_a_sym = Rational(dot_ab_ac, 1) / (sp.sqrt(len_ab_sq) * sp.sqrt(len_ac_sq))
    str_cos_a_true = latex(cos_a_sym)
    cos_a_sym_false = Rational(dot_ab_ac + 1, 1) / (sp.sqrt(len_ab_sq) * sp.sqrt(len_ac_sq))
    str_cos_a_false = latex(cos_a_sym_false)
    if str_cos_a_false == str_cos_a_true:
        str_cos_a_false = "\\frac{\\sqrt{321}}{321}"
    
    # 4. Điểm M(a;b;c) thuộc (Oxy) để S = MA.MB + 2 MB.MC + 3 MC.MA đạt GTNN[cite: 22]
    # Hệ thức vectơ: 4 IA + 3 IB + 5 IC = 0 => I = (4A + 3B + 5C) / 12
    xi_num = 4 * xa + 3 * xb + 5 * xc
    yi_num = 4 * ya + 3 * yb + 5 * yc
    zi_num = 4 * za + 3 * zb + 5 * zc
    
    xi_val = Rational(xi_num, 12)
    yi_val = Rational(yi_num, 12)
    zi_val = Rational(zi_num, 12)
    
    # M là hình chiếu của I lên (Oxy): a = xi_val, b = yi_val, c = 0[cite: 22]
    val_t = 12 * xi_val + 12 * yi_val + 0  # = xi_num + yi_num
    val_t_int = int(val_t)
    val_t_false = val_t_int + random.choice([-2, -1, 1, 2])
    
    # Nội dung câu hỏi[cite: 22]
    noidungcauhoi = (
        """Trong không gian $Oxyz$ cho tam giác $ABC$ biết: $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Điểm G là trọng tâm tam giác ABC[cite: 22]
    nb_da_1_d = (
        "\\True Điểm $G\\left(%s;%s;%s\\right)$ là trọng tâm tam giác $ABC$"
        % (str_xg_true, str_yg_true, str_zg_true)
    )
    nb_da_1_s = (
        "Điểm $G\\left(%s;%s;%s\\right)$ là trọng tâm tam giác $ABC$"
        % (str_xg_false, str_yg_true, str_zg_true)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Tọa độ trọng tâm $G$ của tam giác $ABC$ là: \\\\ $\\begin{cases} x_G = \\frac{x_A + x_B + x_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ y_G = \\frac{y_A + y_B + y_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\end{cases} \\Rightarrow G\\left(%s;%s;%s\\right)$."""
        % (
            xa,
            xb,
            xc,
            str_xg_true,
            ya,
            yb,
            yc,
            str_yg_true,
            za,
            zb,
            zc,
            str_zg_true,
            str_xg_true,
            str_yg_true,
            str_zg_true,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Chu vi tam giác ABC[cite: 22]
    th_da_1_d = "\\True Tam giác $ABC$ có chu vi bằng $%s$" % (str_p_true)
    th_da_1_s = "Tam giác $ABC$ có chu vi bằng $%s$" % (str_p_false)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có độ dài các cạnh của tam giác $ABC$ là: \\\\ $AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2} = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = %s$. \\\\ $BC = \\sqrt{(x_C - x_B)^2 + (y_C - y_B)^2 + (z_C - z_B)^2} = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = %s$. \\\\ $AC = \\sqrt{(x_C - x_A)^2 + (y_C - y_A)^2 + (z_C - z_A)^2} = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = %s$. \\\\ Chu vi tam giác $ABC$ là: \\\\ $P_{ABC} = AB + BC + AC = %s$."""
        % (
            xb,
            xa,
            yb,
            ya,
            zb,
            za,
            latex(sp.sqrt(len_ab_sq)),
            xc,
            xb,
            yc,
            yb,
            zc,
            zb,
            latex(sp.sqrt(len_bc_sq)),
            xc,
            xa,
            yc,
            ya,
            zc,
            za,
            latex(sp.sqrt(len_ac_sq)),
            str_p_true,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: cos A[cite: 22]
    vd_da_1_d = "\\True $\\cos A = %s$" % (str_cos_a_true)
    vd_da_1_s = "$\\cos A = %s$" % (str_cos_a_false)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (%s;%s;%s) \\Rightarrow |\\vec{AB}| = %s$. \\\\ $\\vec{AC} = (%s;%s;%s) \\Rightarrow |\\vec{AC}| = %s$. \\\\ Tích vô hướng của hai vectơ $\\vec{AB}$ và $\\vec{AC}$ là: \\\\ $\\vec{AB} \\cdot \\vec{AC} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Khi đó cosin của góc $A$ là: \\\\ $\\cos A = \\frac{\\vec{AB} \\cdot \\vec{AC}}{|\\vec{AB}| \\cdot |\\vec{AC}|} = \\frac{%s}{%s \\cdot %s} = %s$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            latex(sp.sqrt(len_ab_sq)),
            ac_x,
            ac_y,
            ac_z,
            latex(sp.sqrt(len_ac_sq)),
            ab_x,
            ac_x,
            ab_y,
            ac_y,
            ab_z,
            ac_z,
            dot_ab_ac,
            dot_ab_ac,
            latex(sp.sqrt(len_ab_sq)),
            latex(sp.sqrt(len_ac_sq)),
            str_cos_a_true,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: M(a;b;c) thuộc (Oxy) để S min thì T = 12a + 12b + c[cite: 22]
    vdc_da_1_d = (
        "\\True Gọi $M(a;b;c)$ là điểm thuộc mặt phẳng $(Oxy)$ sao cho biểu thức sau đạt giá trị nhỏ nhất: \\\\ $S = \\vec{MA} \\cdot \\vec{MB} + 2\\vec{MB} \\cdot \\vec{MC} + 3\\vec{MC} \\cdot \\vec{MA}$. \\\\ Khi đó $T = 12a + 12b + c = %s$"
        % (val_t_int)
    )
    vdc_da_1_s = (
        "Gọi $M(a;b;c)$ là điểm thuộc mặt phẳng $(Oxy)$ sao cho biểu thức sau đạt giá trị nhỏ nhất: \\\\ $S = \\vec{MA} \\cdot \\vec{MB} + 2\\vec{MB} \\cdot \\vec{MC} + 3\\vec{MC} \\cdot \\vec{MA}$. \\\\ Khi đó $T = 12a + 12b + c = %s$"
        % (val_t_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_xi = format_fraction_latex(xi_num, 12)
    str_yi = format_fraction_latex(yi_num, 12)
    str_zi = format_fraction_latex(zi_num, 12)
    
    loigiai_vdc_1 = (
        """Biến đổi biểu thức $S$: \\\\ $S = \\vec{MA} \\cdot \\vec{MB} + 2\\vec{MB} \\cdot \\vec{MC} + 3\\vec{MC} \\cdot \\vec{MA}$. \\\\ Gọi $I$ là điểm cố định thỏa mãn hệ thức vectơ: \\\\ $4\\vec{IA} + 3\\vec{IB} + 5\\vec{IC} = \\vec{0} \\Leftrightarrow \\vec{OI} = \\frac{4\\vec{OA} + 3\\vec{OB} + 5\\vec{OC}}{12}$. \\\\ Tọa độ của điểm $I$ là: \\\\ $\\begin{cases} x_I = \\frac{4x_A + 3x_B + 5x_C}{12} = \\frac{4 \\cdot (%s) + 3 \\cdot (%s) + 5 \\cdot (%s)}{12} = %s \\\\ y_I = \\frac{4y_A + 3y_B + 5y_C}{12} = \\frac{4 \\cdot (%s) + 3 \\cdot (%s) + 5 \\cdot (%s)}{12} = %s \\\\ z_I = \\frac{4z_A + 3z_B + 5z_C}{12} = \\frac{4 \\cdot (%s) + 3 \\cdot (%s) + 5 \\cdot (%s)}{12} = %s \\end{cases} \\Rightarrow I\\left(%s;%s;%s\\right)$. \\\\ Thay $\\vec{MA} = \\vec{MI} + \\vec{IA}$, $\\vec{MB} = \\vec{MI} + \\vec{IB}$, $\\vec{MC} = \\vec{MI} + \\vec{IC}$ vào biểu thức $S$, ta có: \\\\ $S = (\\vec{MI} + \\vec{IA})(\\vec{MI} + \\vec{IB}) + 2(\\vec{MI} + \\vec{IB})(\\vec{MI} + \\vec{IC}) + 3(\\vec{MI} + \\vec{IC})(\\vec{MI} + \\vec{IA})$ \\\\ $= 6MI^2 + \\vec{MI} \\cdot (4\\vec{IA} + 3\\vec{IB} + 5\\vec{IC}) + (\\vec{IA} \\cdot \\vec{IB} + 2\\vec{IB} \\cdot \\vec{IC} + 3\\vec{IC} \\cdot \\vec{IA})$ \\\\ $= 6MI^2 + k$ (với $k = \\vec{IA} \\cdot \\vec{IB} + 2\\vec{IB} \\cdot \\vec{IC} + 3\\vec{IC} \\cdot \\vec{IA}$ không đổi). \\\\ Do đó $S$ đạt giá trị nhỏ nhất khi và chỉ khi đoạn thẳng $MI$ ngắn nhất. \\\\ Vì $M \\in (Oxy)$ nên $M$ là hình chiếu vuông góc của điểm $I$ lên mặt phẳng $(Oxy)$. \\\\ Suy ra tọa độ của điểm $M(a;b;c)$ là: \\\\ $M\\left(%s;%s;0\\right) \\Rightarrow a = %s, b = %s, c = 0$. \\\\ Khi đó: $T = 12a + 12b + c = 12 \\cdot \\left(%s\\right) + 12 \\cdot \\left(%s\\right) + 0 = %s + (%s) = %s$."""
        % (
            xa,
            xb,
            xc,
            str_xi,
            ya,
            yb,
            yc,
            str_yi,
            za,
            zb,
            zc,
            str_zi,
            str_xi,
            str_yi,
            str_zi,
            str_xi,
            str_yi,
            str_xi,
            str_yi,
            str_xi,
            str_yi,
            xi_num,
            yi_num,
            val_t_int,
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
    