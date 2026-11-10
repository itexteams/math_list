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


def bt_dang38_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu bốn điểm A, B, C, D sao cho DA, DB, DC đôi một vuông góc (tứ diện vuông đỉnh D)
    while True:
        xd = random.randint(1, 4)
        yd = random.randint(1, 4)
        zd = random.randint(1, 4)
    
        # Chọn độ dài các cạnh DA, DB, DC là các số nguyên dương
        u = random.choice([4, 5, 6])
        v = random.choice([2, 3, 4])
        w = random.choice([2, 3, 5])
    
        xa = xd + u
        ya = yd
        za = zd
    
        xb = xd
        yb = yd + v
        zb = zd
    
        xc = xd
        yc = yd
        zc = zd + w
    
        # Thể tích khối tứ diện vuông đỉnh D: V = 1/6 * u * v * w
        v_val = Rational(u * v * w, 6)
        str_v_val = format_fraction_latex(v_val.p, v_val.q)
    
        # Khoảng cách từ O đến D: OD = sqrt(xd^2 + yd^2 + zd^2)
        od_sq = xd**2 + yd**2 + zd**2
        str_od_true = latex(sp.sqrt(od_sq))
    
        if (
            (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
            and (xb, yb, zb) != (xc, yc, zc)
        ):
            break
    
    # 1. Vectơ DA = (u; 0; 0)[cite: 24]
    da_x = u
    da_y = 0
    da_z = 0
    
    # Tọa độ sai của DA (nhầm dấu hoặc nhầm sang trục khác)[cite: 24]
    da_x_s = -u
    da_y_s = 0
    da_z_s = 0
    
    # 2. Tứ diện ABCD là tứ diện vuông đỉnh D (Luôn đúng theo cấu trúc)[cite: 24]
    
    # 3. So sánh thể tích V_ABCD với một cận bound_v[cite: 24]
    bound_v = int(v_val) - 1 if v_val > 2 else int(v_val) + 1
    is_v_gt = v_val > bound_v
    
    # 4. Giá trị OM khi P = MA + MB + MC + \sqrt{3}MD đạt GTNN: đạt được khi M trùng D => OM = OD[cite: 24]
    od_sq_false = od_sq + random.choice([-2, -1, 1, 2])
    str_od_false = latex(sp.sqrt(od_sq_false))
    
    # Nội dung câu hỏi[cite: 24]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho bốn điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$, $D(%s;%s;%s)$ và điểm $M$ tùy ý."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc, xd, yd, zd)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Vectơ DA[cite: 24]
    nb_da_1_d = "\\True $\\vec{DA} = (%s;%s;%s)$" % (da_x, da_y, da_z)
    nb_da_1_s = "$\\vec{DA} = (%s;%s;%s)$" % (da_x_s, da_y_s, da_z_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ của vectơ $\\vec{DA}$ là: \\\\ $\\vec{DA} = (x_A - x_D; y_A - y_D; z_A - z_D) = (%s - %s; %s - %s; %s - %s) = (%s;%s;%s)$."""
        % (xa, xd, ya, yd, za, zd, da_x, da_y, da_z)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Tứ diện ABCD là tứ diện vuông đỉnh D[cite: 24]
    th_da_1_d = "\\True Tứ diện $ABCD$ là tứ diện vuông đỉnh $D$"
    th_da_1_s = "Tứ diện $ABCD$ không phải là tứ diện vuông đỉnh $D$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{DA} = (%s;0;0)$. \\\\ $\\vec{DB} = (x_B - x_D; y_B - y_D; z_B - z_D) = (0;%s;0)$. \\\\ $\\vec{DC} = (x_C - x_D; y_C - y_D; z_C - z_D) = (0;0;%s)$. \\\\ Xét tích vô hướng từng đôi một của các vectơ: \\\\ $\\vec{DA} \\cdot \\vec{DB} = %s \\cdot 0 + 0 \\cdot %s + 0 \\cdot 0 = 0 \\Rightarrow DA \\perp DB$. \\\\ $\\vec{DA} \\cdot \\vec{DC} = %s \\cdot 0 + 0 \\cdot 0 + 0 \\cdot %s = 0 \\Rightarrow DA \\perp DC$. \\\\ $\\vec{DB} \\cdot \\vec{DC} = 0 \\cdot 0 + %s \\cdot 0 + 0 \\cdot %s = 0 \\Rightarrow DB \\perp DC$. \\\\ Ba cạnh $DA, DB, DC$ đôi một vuông góc với nhau, do đó tứ diện $ABCD$ là tứ diện vuông đỉnh $D$."""
        % (u, v, w, u, v, u, w, v, w)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Thể tích tứ diện ABCD[cite: 24]
    if is_v_gt:
        vd_da_1_d = (
            "\\True Thể tích tứ diện $ABCD$ thỏa mãn $V_{ABCD} > %s$" % (bound_v)
        )
        vd_da_1_s = (
            "Thể tích tứ diện $ABCD$ thỏa mãn $V_{ABCD} < %s$" % (bound_v)
        )
    else:
        vd_da_1_d = (
            "\\True Thể tích tứ diện $ABCD$ thỏa mãn $V_{ABCD} < %s$" % (bound_v)
        )
        vd_da_1_s = (
            "Thể tích tứ diện $ABCD$ thỏa mãn $V_{ABCD} > %s$" % (bound_v)
        )
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Độ dài các cạnh của tứ diện vuông đỉnh $D$ là: \\\\ $DA = %s, DB = %s, DC = %s$. \\\\ Thể tích của tứ diện vuông $ABCD$ được tính theo công thức: \\\\ $V_{ABCD} = \\frac{1}{6} DA \\cdot DB \\cdot DC = \\frac{1}{6} \\cdot %s \\cdot %s \\cdot %s = %s$. \\\\ Vì $%s %s %s$ nên khẳng định thể tích $V_{ABCD} %s %s$ là %s."""
        % (
            u,
            v,
            w,
            u,
            v,
            w,
            str_v_val,
            str_v_val,
            ">" if is_v_gt else "<",
            bound_v,
            ">" if is_v_gt else "<",
            bound_v,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Khi P = MA + MB + MC + \sqrt{3}MD đạt GTNN thì OM = ...[cite: 24]
    vdc_da_1_d = (
        "\\True Khi biểu thức $P = MA + MB + MC + \\sqrt{3}MD$ đạt giá trị nhỏ nhất thì $OM = %s$"
        % (str_od_true)
    )
    vdc_da_1_s = (
        "Khi biểu thức $P = MA + MB + MC + \\sqrt{3}MD$ đạt giá trị nhỏ nhất thì $OM = %s$"
        % (str_od_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Xét hệ trục tọa độ mới $Dxyz$ có gốc tọa độ tại $D(%s;%s;%s)$, các tia $Dx, Dy, Dz$ lần lượt cùng hướng với các vectơ $\\vec{DA}, \\vec{DB}, \\vec{DC}$. \\\\ Gọi các vectơ đơn vị trên các trục lần lượt là $\\vec{i}, \\vec{j}, \\vec{k}$. \\\\ Với điểm $M(x;y;z)$ bất kỳ trong hệ tọa độ mới, ta có: \\\\ $\\vec{MA} \\cdot \\vec{i} \\le |\\vec{MA}| \\cdot |\\vec{i}| = MA \\Rightarrow MA \\ge (%s - x)$. \\\\ $\\vec{MB} \\cdot \\vec{j} \\le |\\vec{MB}| \\cdot |\\vec{j}| = MB \\Rightarrow MB \\ge (%s - y)$. \\\\ $\\vec{MC} \\cdot \\vec{k} \\le |\\vec{MC}| \\cdot |\\vec{k}| = MC \\Rightarrow MC \\ge (%s - z)$. \\\\ Cộng từng vế ba bất đẳng thức trên, ta được: \\\\ $MA + MB + MC \\ge %s + %s + %s - (x + y + z) = %s - (x + y + z)$. \\\\ Mặt khác, theo bất đẳng thức Cauchy-Schwarz: \\\\ $x + y + z = 1 \\cdot x + 1 \\cdot y + 1 \\cdot z \\le \\sqrt{1^2 + 1^2 + 1^2} \\cdot \\sqrt{x^2 + y^2 + z^2} = \\sqrt{3} MD$ \\\\ $\\Rightarrow \\sqrt{3}MD - (x + y + z) \\ge 0$. \\\\ Do đó ta có: \\\\ $P = MA + MB + MC + \\sqrt{3}MD \\ge %s + [\\sqrt{3}MD - (x + y + z)] \\ge %s$. \\\\ Đẳng thức xảy ra khi và chỉ khi $x = y = z = 0$, tức là điểm $M$ trùng với điểm $D(%s;%s;%s)$. \\\\ Khi đó khoảng cách từ gốc tọa độ $O(0;0;0)$ đến điểm $M$ là: \\\\ $OM = OD = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$."""
        % (
            xd,
            yd,
            zd,
            u,
            v,
            w,
            u,
            v,
            w,
            u + v + w,
            u + v + w,
            u + v + w,
            xd,
            yd,
            zd,
            xd,
            yd,
            zd,
            od_sq,
            str_od_true,
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
    