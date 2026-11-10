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


def bt_dang54_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    while True:
        xa = random.randint(1, 3)
        ya = random.randint(1, 4)
        za = random.randint(1, 4)
    
        # Chọn vectơ AB và AC sao cho góc giữa hai đường thẳng đẹp (ví dụ 60 độ: cos = 1/2)
        # Ta chọn độ dài AB = sqrt(6), AC = sqrt(6), |AB . AC| = 3 => cos = 3/6 = 1/2 => góc 60 độ
        # Hoặc 1, 2, 1; 1, 1, 2 v.v.
        # Thử các cặp vectơ mẫu có góc đặc biệt:
        angle_candidates = [
            # (u, v, angle_deg)
            ((1, -1, 2), (1, 2, -1), 60),    # dot = 1 - 2 - 2 = -3, |dot| = 3, len1=sqrt(6), len2=sqrt(6), cos = 3/6 = 1/2 => 60 độ
            ((1, 0, 1), (0, 1, 1), 60),      # dot = 1, len1=sqrt(2), len2=sqrt(2), cos = 1/2 => 60 độ
            ((1, 1, 0), (1, 0, 1), 60),      # dot = 1, len1=sqrt(2), len2=sqrt(2), cos = 1/2 => 60 độ
            ((2, -1, 1), (1, 1, 2), 60),     # dot = 2 - 1 + 2 = 3, len1=sqrt(6), len2=sqrt(6), cos = 1/2 => 60 độ
            ((1, 1, 0), (0, 1, 1), 60),      # cos = 1/2 => 60 độ
            ((1, 0, 0), (1, 1, 0), 45),      # dot = 1, len1=1, len2=sqrt(2), cos = 1/sqrt(2) => 45 độ
            ((0, 1, 1), (0, 0, 1), 45),      # cos = 1/sqrt(2) => 45 độ
            ((1, 2, 2), (2, 1, -2), 90),     # dot = 2 + 2 - 4 = 0 => 90 độ
        ]
        u_vec, v_vec, target_angle = random.choice(angle_candidates)
    
        xb = xa + u_vec[0]
        yb = ya + u_vec[1]
        zb = za + u_vec[2]
    
        xc = xa + v_vec[0]
        yc = ya + v_vec[1]
        zc = za + v_vec[2]
    
        # Kiểm tra K = (3B - C)/2 có xK và zK nguyên để tính toán đẹp
        xk_num = 3 * xb - xc
        yk_num = 3 * yb - yc
        zk_num = 3 * zb - zc
    
        if xk_num % 2 == 0 and zk_num % 2 == 0:
            xk_val = xk_num // 2
            yk_val = Rational(yk_num, 2)
            zk_val = zk_num // 2
    
            # Điểm I thuộc (Oxz) => b = 0, a = xk_val, c = zk_val
            val_expr_d = xk_val - 2 * 0 + 2 * zk_val
            break
    
    # 1. Tọa độ trung điểm của AB[cite: 23]
    xm_ab_num = xa + xb
    ym_ab_num = ya + yb
    zm_ab_num = za + zb
    
    str_xm_ab = format_fraction_latex(xm_ab_num, 2)
    str_ym_ab = format_fraction_latex(ym_ab_num, 2)
    str_zm_ab = format_fraction_latex(zm_ab_num, 2)
    
    # Tọa độ trung điểm sai
    str_ym_ab_false = format_fraction_latex(ym_ab_num + 2, 2)
    
    # 2. Tổng vectơ OA + OB + OC = (xa + xb + xc; ya + yb + yc; za + zb + zc)[cite: 23]
    sum_x = xa + xb + xc
    sum_y = ya + yb + yc
    sum_z = za + zb + zc
    
    sum_x_false = sum_x + random.choice([-1, 1])
    sum_y_false = sum_y
    sum_z_false = sum_z
    
    # 3. Góc giữa hai đường thẳng AB và AC[cite: 23]
    angle_true = target_angle
    angle_false = 30 if target_angle != 30 else 45
    
    # 4. Giá trị biểu thức a - 2b + 2c[cite: 23]
    val_expr_d_true = val_expr_d
    val_expr_d_false = val_expr_d + random.choice([-3, -2, 2, 3])
    
    # Nội dung câu hỏi[cite: 23]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho ba điểm $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Tọa độ trung điểm của AB[cite: 23]
    nb_da_1_d = (
        "\\True Tọa độ trung điểm của $AB$ là $\\left(%s;%s;%s\\right)$"
        % (str_xm_ab, str_ym_ab, str_zm_ab)
    )
    nb_da_1_s = (
        "Tọa độ trung điểm của $AB$ là $\\left(%s;%s;%s\\right)$"
        % (str_xm_ab, str_ym_ab_false, str_zm_ab)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Gọi $M$ là trung điểm của đoạn thẳng $AB$. Tọa độ của điểm $M$ là: \\\\ $\\begin{cases} x_M = \\frac{x_A + x_B}{2} = \\frac{%s + (%s)}{2} = %s \\\\ y_M = \\frac{y_A + y_B}{2} = \\frac{%s + (%s)}{2} = %s \\\\ z_M = \\frac{z_A + z_B}{2} = \\frac{%s + (%s)}{2} = %s \\end{cases} \\Rightarrow M\\left(%s;%s;%s\\right)$."""
        % (
            xa,
            xb,
            str_xm_ab,
            ya,
            yb,
            str_ym_ab,
            za,
            zb,
            str_zm_ab,
            str_xm_ab,
            str_ym_ab,
            str_zm_ab,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: OA + OB + OC[cite: 23]
    th_da_1_d = "\\True $\\vec{OA} + \\vec{OB} + \\vec{OC} = (%s;%s;%s)$" % (
        sum_x,
        sum_y,
        sum_z,
    )
    th_da_1_s = "$\\vec{OA} + \\vec{OB} + \\vec{OC} = (%s;%s;%s)$" % (
        sum_x_false,
        sum_y_false,
        sum_z_false,
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{OA} = (%s;%s;%s)$, $\\vec{OB} = (%s;%s;%s)$, $\\vec{OC} = (%s;%s;%s)$. \\\\ Suy ra: \\\\ $\\vec{OA} + \\vec{OB} + \\vec{OC} = (%s + (%s) + (%s); %s + (%s) + (%s); %s + (%s) + (%s)) = (%s;%s;%s)$."""
        % (
            xa,
            ya,
            za,
            xb,
            yb,
            zb,
            xc,
            yc,
            zc,
            xa,
            xb,
            xc,
            ya,
            yb,
            yc,
            za,
            zb,
            zc,
            sum_x,
            sum_y,
            sum_z,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Góc giữa hai đường thẳng AB và AC[cite: 23]
    vd_da_1_d = "\\True Góc giữa hai đường thẳng $AB$ và $AC$ bằng $%s^\\circ$" % (
        angle_true
    )
    vd_da_1_s = "Góc giữa hai đường thẳng $AB$ và $AC$ bằng $%s^\\circ$" % (
        angle_false
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    ab_x = xb - xa
    ab_y = yb - ya
    ab_z = zb - za
    len_ab_sq = ab_x**2 + ab_y**2 + ab_z**2
    
    ac_x = xc - xa
    ac_y = yc - ya
    ac_z = zc - za
    len_ac_sq = ac_x**2 + ac_y**2 + ac_z**2
    
    dot_ab_ac = ab_x * ac_x + ab_y * ac_y + ab_z * ac_z
    abs_dot = abs(dot_ab_ac)
    
    loigiai_vd_1 = (
        """Ta có tọa độ các vectơ chỉ phương: \\\\ $\\vec{AB} = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ $\\vec{AC} = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Độ dài của các vectơ là: \\\\ $|\\vec{AB}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $|\\vec{AC}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Tích vô hướng: $\\vec{AB} \\cdot \\vec{AC} = (%s)(%s) + (%s)(%s) + (%s)(%s) = %s$. \\\\ Góc giữa hai đường thẳng $AB$ và $AC$ thỏa mãn: \\\\ $\\cos(AB, AC) = \\frac{|\\vec{AB} \\cdot \\vec{AC}|}{|\\vec{AB}| \\cdot |\\vec{AC}|} = \\frac{|%s|}{\\sqrt{%s} \\cdot \\sqrt{%s}} = \\frac{%s}{\\sqrt{%s}} = %s$. \\\\ Suy ra góc giữa hai đường thẳng $AB$ và $AC$ bằng $%s^\\circ$."""
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
            ab_y,
            ab_z,
            len_ab_sq,
            ac_x,
            ac_y,
            ac_z,
            len_ac_sq,
            ab_x,
            ac_x,
            ab_y,
            ac_y,
            ab_z,
            ac_z,
            dot_ab_ac,
            dot_ab_ac,
            len_ab_sq,
            len_ac_sq,
            abs_dot,
            len_ab_sq * len_ac_sq,
            latex(Rational(abs_dot, 1) / (sp.sqrt(len_ab_sq) * sp.sqrt(len_ac_sq))),
            angle_true,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Điểm I(a;b;c) thuộc (Oxz) để T = |3*IB - IC| đạt GTNN thì a - 2b + 2c[cite: 23]
    vdc_da_1_d = (
        "\\True Điểm $I(a;b;c)$ nằm trên mặt phẳng $(Oxz)$ thỏa mãn $T = \\left|3\\vec{IB} - \\vec{IC}\\right|$ đạt giá trị nhỏ nhất. Khi đó $a - 2b + 2c = %s$"
        % (val_expr_d_true)
    )
    vdc_da_1_s = (
        "Điểm $I(a;b;c)$ nằm trên mặt phẳng $(Oxz)$ thỏa mãn $T = \\left|3\\vec{IB} - \\vec{IC}\\right|$ đạt giá trị nhỏ nhất. Khi đó $a - 2b + 2c = %s$"
        % (val_expr_d_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_yk = format_fraction_latex(yk_val.p, yk_val.q)
    
    loigiai_vdc_1 = (
        """Gọi điểm $K$ là điểm thỏa mãn hệ thức vectơ: \\\\ $3\\vec{KB} - \\vec{KC} = \\vec{0} \\Leftrightarrow 3(\\vec{OB} - \\vec{OK}) - (\\vec{OC} - \\vec{OK}) = \\vec{0} \\Leftrightarrow 2\\vec{OK} = 3\\vec{OB} - \\vec{OC} \\Leftrightarrow \\vec{OK} = \\frac{3\\vec{OB} - \\vec{OC}}{2}$. \\\\ Tọa độ điểm $K$ là: \\\\ $\\begin{cases} x_K = \\frac{3x_B - x_C}{2} = \\frac{3 \\cdot (%s) - (%s)}{2} = %s \\\\ y_K = \\frac{3y_B - y_C}{2} = \\frac{3 \\cdot (%s) - (%s)}{2} = %s \\\\ z_K = \\frac{3z_B - z_C}{2} = \\frac{3 \\cdot (%s) - (%s)}{2} = %s \\end{cases} \\Rightarrow K\\left(%s;%s;%s\\right)$. \\\\ Khi đó ta có: \\\\ $3\\vec{IB} - \\vec{IC} = 3(\\vec{IK} + \\vec{KB}) - (\\vec{IK} + \\vec{KC}) = 2\\vec{IK} + (3\\vec{KB} - \\vec{KC}) = 2\\vec{IK}$. \\\\ Suy ra biểu thức $T = \\left|3\\vec{IB} - \\vec{IC}\\right| = \\left|2\\vec{IK}\\right| = 2 IK$. \\\\ Biểu thức $T$ đạt giá trị nhỏ nhất khi và chỉ khi đoạn thẳng $IK$ ngắn nhất. \\\\ Vì điểm $I$ nằm trên mặt phẳng tọa độ $(Oxz)$ nên $I$ là hình chiếu vuông góc của điểm $K$ lên mặt phẳng $(Oxz)$. \\\\ Do đó tọa độ điểm $I(a;b;c)$ là $I(%s;0;%s) \\Rightarrow a = %s, b = 0, c = %s$. \\\\ Khi đó giá trị của biểu thức là: \\\\ $a - 2b + 2c = %s - 2 \\cdot 0 + 2 \\cdot (%s) = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            xb,
            xc,
            xk_val,
            yb,
            yc,
            str_yk,
            zb,
            zc,
            zk_val,
            xk_val,
            str_yk,
            zk_val,
            xk_val,
            zk_val,
            xk_val,
            zk_val,
            xk_val,
            zk_val,
            val_expr_d_true,
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
    