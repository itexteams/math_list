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


def bt_dang12_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên toạ độ các điểm A, B, C không thẳng hàng
    # Để trọng tâm G nằm trên mặt phẳng (Oxy), ta có zA + zB + zC = 0
    # Để điểm N thuộc (Oxy) thẳng hàng với A, B có toạ độ nguyên đẹp,
    # ta chọn zB - zA là ước của zA (đặc biệt chọn zB - zA = 1 hoặc -1)
    while True:
        xa = random.randint(-4, 4)
        ya = random.randint(-4, 4)
        za = random.choice([-2, -1, 1, 2])
    
        delta_z = random.choice([-1, 1])
        zb = za + delta_z
    
        xb = random.randint(-4, 4)
        yb = random.randint(-4, 4)
    
        # Để zG = 0 thì zC = -(zA + zb)
        zc = -(za + zb)
    
        xc = random.randint(-4, 4)
        yc = random.randint(-4, 4)
    
        # Vectơ AB và AC
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        # Tích có hướng [AB, AC] để kiểm tra ba điểm không thẳng hàng
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and (xa, ya) != (xb, yb)
            and ab_z != 0
        ):
            break
    
    # 1. Toạ độ vectơ AB
    # ab_x, ab_y, ab_z đã tính ở trên
    
    # 2. Trọng tâm G của tam giác ABC
    # xG = (xa + xb + xc)/3, yG = (ya + yb + yc)/3, zG = (za + zb + zc)/3 = 0 => G thuộc (Oxy)
    
    # 3. Điểm M sao cho AB + CM = 0 <=> CM = -AB = BA <=> M = C + BA = C + A - B
    xm = xc + xa - xb
    ym = yc + ya - yb
    zm = zc + za - zb
    
    # Toạ độ sai của M (ví dụ nhầm sang M = C + AB)
    xm_s = xc + xb - xa
    ym_s = yc + yb - ya
    zm_s = zc + zb - za
    
    # 4. Điểm N thuộc mặt phẳng (Oxy) sao cho A, B, N thẳng hàng
    # N(xN; yN; 0). Do A, B, N thẳng hàng nên vector AN = k * vector AB
    # => 0 - za = k * (zb - za) => k = -za / (zb - za)
    k_val = Rational(-za, ab_z)
    xn = xa + k_val * ab_x
    yn = ya + k_val * ab_y
    zn = 0
    
    str_xn = format_fraction_latex(xn.p, xn.q)
    str_yn = format_fraction_latex(yn.p, yn.q)
    
    # Toạ độ sai của N
    xn_s = xn + random.choice([-2, 1, 2])
    yn_s = yn + random.choice([-1, 1, 2])
    str_xn_s = format_fraction_latex(xn_s.p, xn_s.q)
    str_yn_s = format_fraction_latex(yn_s.p, yn_s.q)
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian $Oxyz$, cho các điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$ và $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Phát biểu a: Vectơ AB
    nb_da_1_d = "\\True $\\vec{AB} = (%s;%s;%s)$" % (ab_x, ab_y, ab_z)
    nb_da_1_s = "$\\vec{AB} = (%s;%s;%s)$" % (-ab_x, -ab_y, -ab_z)
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
    # Phát biểu b: Trọng tâm G của tam giác ABC nằm trên mặt phẳng (Oxy)
    th_da_1_d = "\\True Trọng tâm $G$ của tam giác $ABC$ nằm trên mặt phẳng $(Oxy)$"
    th_da_1_s = "Trọng tâm $G$ của tam giác $ABC$ nằm trên mặt phẳng $(Oyz)$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Cao độ của trọng tâm $G$ của tam giác $ABC$ là: \\\\ $z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{%s + (%s) + (%s)}{3} = 0$. \\\\ Do $z_G = 0$ nên trọng tâm $G$ nằm trên mặt phẳng $(Oxy)$."""
        % (za, zb, zc)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Phát biểu c: Toạ độ điểm M sao cho AB + CM = 0
    vd_da_1_d = (
        "\\True Toạ độ điểm $M$ sao cho $\\vec{AB} + \\vec{CM} = \\vec{0}$ là $(%s;%s;%s)$"
        % (xm, ym, zm)
    )
    vd_da_1_s = (
        "Toạ độ điểm $M$ sao cho $\\vec{AB} + \\vec{CM} = \\vec{0}$ là $(%s;%s;%s)$"
        % (xm_s, ym_s, zm_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có $\\vec{AB} + \\vec{CM} = \\vec{0} \\Leftrightarrow \\vec{CM} = -\\vec{AB}$. \\\\ Gọi toạ độ điểm $M(x_M; y_M; z_M)$, ta có: \\\\ $\\vec{CM} = (x_M - (%s); y_M - (%s); z_M - (%s))$ và $-\\vec{AB} = (%s;%s;%s)$. \\\\ Suy ra: \\\\ $\\begin{cases} x_M - (%s) = %s \\\\ y_M - (%s) = %s \\\\ z_M - (%s) = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_M = %s \\\\ y_M = %s \\\\ z_M = %s \\end{cases} \\Rightarrow M(%s;%s;%s)$."""
        % (
            xc,
            yc,
            zc,
            -ab_x,
            -ab_y,
            -ab_z,
            xc,
            -ab_x,
            yc,
            -ab_y,
            zc,
            -ab_z,
            xm,
            ym,
            zm,
            xm,
            ym,
            zm,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Phát biểu d: Toạ độ điểm N thuộc mặt phẳng (Oxy) sao cho A, B, N thẳng hàng
    vdc_da_1_d = (
        "\\True Toạ độ điểm $N$ thuộc mặt phẳng $(Oxy)$, sao cho $A, B, N$ thẳng hàng là $(%s;%s;0)$"
        % (str_xn, str_yn)
    )
    vdc_da_1_s = (
        "Toạ độ điểm $N$ thuộc mặt phẳng $(Oxy)$, sao cho $A, B, N$ thẳng hàng là $(%s;%s;0)$"
        % (str_xn_s, str_yn_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_k = format_fraction_latex(k_val.p, k_val.q)
    
    loigiai_vdc_1 = (
        """Vì điểm $N$ thuộc mặt phẳng $(Oxy)$ nên $N$ có toạ độ dạng $N(x_N; y_N; 0)$. \\\\ Ta có $\\vec{AB} = (%s;%s;%s)$ và $\\vec{AN} = (x_N - (%s); y_N - (%s); 0 - (%s)) = (x_N - (%s); y_N - (%s); %s)$. \\\\ Ba điểm $A, B, N$ thẳng hàng khi và chỉ khi tồn tại số thực $k$ sao cho $\\vec{AN} = k\\vec{AB}$: \\\\ $\\Leftrightarrow \\begin{cases} x_N - (%s) = k \\cdot (%s) \\\\ y_N - (%s) = k \\cdot (%s) \\\\ %s = k \\cdot (%s) \\end{cases} \\Leftrightarrow \\begin{cases} k = %s \\\\ x_N = (%s) + (%s) \\cdot (%s) = %s \\\\ y_N = (%s) + (%s) \\cdot (%s) = %s \\end{cases}$ \\\\ Vậy $N(%s;%s;0)$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            xa,
            ya,
            za,
            xa,
            ya,
            -za,
            xa,
            ab_x,
            ya,
            ab_y,
            -za,
            ab_z,
            str_k,
            xa,
            str_k,
            ab_x,
            str_xn,
            ya,
            str_k,
            ab_y,
            str_yn,
            str_xn,
            str_yn,
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
    