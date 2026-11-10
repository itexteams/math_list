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


def bt_dang67_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hai điểm A và B[cite: 20]
    while True:
        xa = random.randint(1, 3)
        ya = random.randint(1, 4)
        za = random.randint(1, 3)
    
        xb = random.randint(1, 4)
        yb = random.randint(-3, 0)
        zb = random.randint(2, 5)
    
        # Cao độ trung điểm I của AB: z_I = (za + zb)/2[cite: 20]
        zi_val = Rational(za + zb, 2)
    
        # Điểm M1 thỏa mãn 3*M1A + 2*M1B = 0 <=> M1 = (3A + 2B)/5[cite: 20]
        zm1_val = Rational(3 * za + 2 * zb, 5)
    
        # M2 trên (Oxy) để MA^2 + MB^2 nhỏ nhất => M2 là hình chiếu của I lên (Oxy)[cite: 20]
        # M2( (xa + xb)/2; (ya + yb)/2; 0 )[cite: 20]
        xm2_val = Rational(xa + xb, 2)
        ym2_val = Rational(ya + yb, 2)
    
        if (xa, ya, za) != (xb, yb, zb):
            break
    
    # 1. Khẳng định a: Trung điểm của đoạn thẳng AB có cao độ nhỏ hơn / lớn hơn bound_a[cite: 20]
    bound_a = math.ceil(float(zi_val))
    if bound_a == float(zi_val):
        bound_a += 1
    is_zi_lt_bound = float(zi_val) < bound_a
    
    str_zi = format_fraction_latex(zi_val.p, zi_val.q)
    
    # 2. Khẳng định b: Hình chiếu vuông góc của A trên mặt phẳng (Oyz) là điểm có hoành độ bằng 0 (luôn đúng)[cite: 20]
    
    # 3. Khẳng định c: Điểm M thỏa mãn 3*MA + 2*MB = 0 thì M có cao độ bằng zm1_val[cite: 20]
    str_zm1_true = format_fraction_latex(zm1_val.p, zm1_val.q)
    zm1_val_false = Rational(zm1_val.p + random.choice([-1, 1]), zm1_val.q)
    str_zm1_false = format_fraction_latex(zm1_val_false.p, zm1_val_false.q)
    if str_zm1_false == str_zm1_true:
        str_zm1_false = "\\frac{9}{5}"[cite: 20]
    
    # 4. Khẳng định d: Điểm M trên (Oxy) sao cho MA^2 + MB^2 nhỏ nhất, khi đó M(xm2; ym2; 0)[cite: 20]
    str_xm2_true = format_fraction_latex(xm2_val.p, xm2_val.q)
    str_ym2_true = format_fraction_latex(ym2_val.p, ym2_val.q)
    str_pt_d_true = "M\\left(%s;%s;0\\right)" % (str_xm2_true, str_ym2_true)
    
    # Tọa độ sai: đổi sai hoành độ hoặc tung độ[cite: 20]
    xm2_val_false = Rational(xm2_val.p + random.choice([-1, 1]), xm2_val.q)
    str_xm2_false = format_fraction_latex(xm2_val_false.p, xm2_val_false.q)
    str_pt_d_false = "M\\left(%s;%s;0\\right)" % (str_xm2_false, str_ym2_true)
    if str_pt_d_false == str_pt_d_true:
        str_pt_d_false = "M\\left(1;\\frac{1}{2};0\\right)"[cite: 20]
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho hai điểm $A(%s;%s;%s), B(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Trung điểm của đoạn thẳng AB có cao độ nhỏ hơn / lớn hơn bound_a[cite: 20]
    if is_zi_lt_bound:
        nb_da_1_d = (
            "\\True Trung điểm của đoạn thẳng $AB$ có cao độ nhỏ hơn $%s$" % (bound_a)
        )
        nb_da_1_s = (
            "Trung điểm của đoạn thẳng $AB$ có cao độ lớn hơn $%s$" % (bound_a)
        )
    else:
        nb_da_1_d = (
            "\\True Trung điểm của đoạn thẳng $AB$ có cao độ lớn hơn $%s$" % (bound_a)
        )
        nb_da_1_s = (
            "Trung điểm của đoạn thẳng $AB$ có cao độ nhỏ hơn $%s$" % (bound_a)
        )
    
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Gọi $I$ là trung điểm của đoạn thẳng $AB$. \\\\ Cao độ của điểm $I$ được tính theo công thức: \\\\ $z_I = \\frac{z_A + z_B}{2} = \\frac{%s + (%s)}{2} = %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            za,
            zb,
            str_zi,
            str_zi,
            "<" if is_zi_lt_bound else ">",
            bound_a,
            "đúng" if "\\True" in nb_da_1 else "sai",
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Hình chiếu vuông góc của A trên mặt phẳng (Oyz) là điểm có hoành độ bằng 0[cite: 20]
    th_da_1_d = (
        "\\True Hình chiếu vuông góc của $A(%s;%s;%s)$ trên mặt phẳng $(Oyz)$ là điểm có hoành độ bằng $0$"
        % (xa, ya, za)
    )
    th_da_1_s = (
        "Hình chiếu vuông góc của $A(%s;%s;%s)$ trên mặt phẳng $(Oyz)$ là điểm có hoành độ bằng $%s$"
        % (xa, ya, za, xa)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Mặt phẳng tọa độ $(Oyz)$ có phương trình là $x = 0$. \\\\ Hình chiếu vuông góc của điểm $A(%s;%s;%s)$ lên mặt phẳng $(Oyz)$ là điểm $A'(0;%s;%s)$. \\\\ Điểm này có hoành độ bằng $0$. \\\\ Do đó mệnh đề là %s."""
        % (
            xa,
            ya,
            za,
            ya,
            za,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Điểm M thỏa mãn 3*MA + 2*MB = 0 thì M có cao độ bằng ...[cite: 20]
    vd_da_1_d = (
        "\\True Điểm $M$ thỏa mãn $3\\vec{MA} + 2\\vec{MB} = \\vec{0}$ thì $M$ có cao độ bằng $%s$"
        % (str_zm1_true)
    )
    vd_da_1_s = (
        "Điểm $M$ thỏa mãn $3\\vec{MA} + 2\\vec{MB} = \\vec{0}$ thì $M$ có cao độ bằng $%s$"
        % (str_zm1_false)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có hệ thức vectơ: \\\\ $3\\vec{MA} + 2\\vec{MB} = \\vec{0} \\Leftrightarrow 3(\\vec{OA} - \\vec{OM}) + 2(\\vec{OB} - \\vec{OM}) = \\vec{0}$ \\\\ $\\Leftrightarrow 5\\vec{OM} = 3\\vec{OA} + 2\\vec{OB} \\Leftrightarrow \\vec{OM} = \\frac{3\\vec{OA} + 2\\vec{OB}}{5}$. \\\\ Suy ra cao độ của điểm $M$ là: \\\\ $z_M = \\frac{3z_A + 2z_B}{5} = \\frac{3 \\cdot (%s) + 2 \\cdot (%s)}{5} = %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            za,
            zb,
            str_zm1_true,
            str_zm1_true,
            "=" if "\\True" in vd_da_1 else "\\neq",
            str_zm1_true if "\\True" in vd_da_1 else str_zm1_false,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Tồn tại điểm M trên mặt phẳng (Oxy) sao cho MA^2 + MB^2 nhỏ nhất, khi đó M(...)[cite: 20]
    vdc_da_1_d = (
        "\\True Tồn tại điểm $M$ trên mặt phẳng $(Oxy)$ sao cho $MA^2 + MB^2$ nhỏ nhất, khi đó $%s$"
        % (str_pt_d_true)
    )
    vdc_da_1_s = (
        "Tồn tại điểm $M$ trên mặt phẳng $(Oxy)$ sao cho $MA^2 + MB^2$ nhỏ nhất, khi đó $%s$"
        % (str_pt_d_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_xi = format_fraction_latex(xa + xb, 2)
    str_yi = format_fraction_latex(ya + yb, 2)
    
    loigiai_vdc_1 = (
        """Gọi $I$ là trung điểm của đoạn thẳng $AB$. Tọa độ điểm $I$ là: \\\\ $I\\left(\\frac{x_A + x_B}{2}; \\frac{y_A + y_B}{2}; \\frac{z_A + z_B}{2}\\right) = I\\left(%s; %s; %s\\right)$. \\\\ Với mọi điểm $M$, ta có hệ thức: \\\\ $MA^2 + MB^2 = (\\vec{MI} + \\vec{IA})^2 + (\\vec{MI} + \\vec{IB})^2 = 2MI^2 + 2\\vec{MI}(\\vec{IA} + \\vec{IB}) + IA^2 + IB^2 = 2MI^2 + \\frac{AB^2}{2}$. \\\\ Do hai điểm $A, B$ cố định nên $AB$ không đổi, vì vậy $MA^2 + MB^2$ nhỏ nhất khi và chỉ khi $MI$ ngắn nhất. \\\\ Vì điểm $M$ thuộc mặt phẳng tọa độ $(Oxy)$ nên $MI$ ngắn nhất khi $M$ là hình chiếu vuông góc của điểm $I$ lên mặt phẳng $(Oxy)$. \\\\ Suy ra tọa độ điểm $M$ là: \\\\ $M(x_I; y_I; 0) = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            str_xi,
            str_yi,
            str_zi,
            str_pt_d_true,
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
    