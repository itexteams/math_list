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


def bt_dang63_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hai điểm A và B sao cho trung điểm I có tọa độ nguyên đẹp[cite: 22]
    while True:
        xa = random.randint(2, 6)
        ya = random.randint(-5, -1)
        za = random.randint(4, 8)
    
        # Chọn điểm B sao cho tổng các tọa độ chẵn[cite: 22]
        xb = random.choice([2, 4, 6])
        if (xa + xb) % 2 != 0:
            xb += 1
    
        yb = random.randint(2, 6)
        if (ya + yb) % 2 != 0:
            yb += 1
    
        zb = random.randint(2, 6)
        if (za + zb) % 2 != 0:
            zb += 1
    
        # Tọa độ trung điểm I của AB[cite: 22]
        xi = (xa + xb) // 2
        yi = (ya + yb) // 2
        zi = (za + zb) // 2
    
        # Vectơ AB[cite: 22]
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        # Khi M thuộc (Oxy) để MA . MB nhỏ nhất, M là hình chiếu của I lên (Oxy): M(xi; yi; 0)[cite: 22]
        om_sq = xi**2 + yi**2
    
        if (xa, ya, za) != (xb, yb, zb) and ab_x != 0 and ab_y != 0 and ab_z != 0:
            break
    
    # 1. Khẳng định a: Vectơ AB[cite: 22]
    ab_false_x = ab_x
    ab_false_y = -ab_y if ab_y != 0 else 2
    ab_false_z = ab_z
    
    # 2. Khẳng định b: Khoảng cách từ A đến mặt phẳng (Oxy) bằng |za|[cite: 22]
    dist_a_oxy = abs(za)
    dist_a_oxy_false = dist_a_oxy + random.choice([-2, -1, 1, 2])
    if dist_a_oxy_false <= 0:
        dist_a_oxy_false = dist_a_oxy + 3
    
    # 3. Khẳng định c: Trung điểm đoạn thẳng AB có tung độ bằng yi[cite: 22]
    yi_true = yi
    yi_false = yi + random.choice([-2, -1, 1, 2])
    
    # 4. Khẳng định d: OM = sqrt(om_sq)[cite: 22]
    om_sym = sp.sqrt(om_sq)
    str_om_true = latex(om_sym)
    om_sym_false = sp.sqrt(om_sq + random.choice([-3, -2, 2, 3]))
    str_om_false = latex(om_sym_false)
    if str_om_false == str_om_true:
        str_om_false = "2\\sqrt{3}"[cite: 22]
    
    # Nội dung câu hỏi[cite: 22]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$ cho hai điểm $A(%s;%s;%s), B(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Vectơ AB[cite: 22]
    nb_da_1_d = "\\True $\\vec{AB} = (%s;%s;%s)$" % (ab_x, ab_y, ab_z)
    nb_da_1_s = "$\\vec{AB} = (%s;%s;%s)$" % (ab_false_x, ab_false_y, ab_false_z)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Tọa độ của vectơ $\\vec{AB}$ là: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (xb, xa, yb, ya, zb, za, ab_x, ab_y, ab_z)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Điểm A cách mặt phẳng (Oxy) một khoảng bằng dist_a_oxy[cite: 22]
    th_da_1_d = (
        "\\True Điểm $A$ cách mặt phẳng $(Oxy)$ một khoảng bằng $%s$" % (dist_a_oxy)
    )
    th_da_1_s = (
        "Điểm $A$ cách mặt phẳng $(Oxy)$ một khoảng bằng $%s$" % (dist_a_oxy_false)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Mặt phẳng tọa độ $(Oxy)$ có phương trình là $z = 0$. \\\\ Khoảng cách từ điểm $A(%s;%s;%s)$ đến mặt phẳng $(Oxy)$ là: \\\\ $d(A, (Oxy)) = |z_A| = |%s| = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            xa,
            ya,
            za,
            za,
            dist_a_oxy,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Trung điểm đoạn thẳng AB có tung độ bằng yi[cite: 22]
    vd_da_1_d = (
        "\\True Trung điểm đoạn thẳng $AB$ có tung độ bằng $%s$" % (yi_true)
    )
    vd_da_1_s = (
        "Trung điểm đoạn thẳng $AB$ có tung độ bằng $%s$" % (yi_false)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Gọi $I$ là trung điểm của đoạn thẳng $AB$. \\\\ Tọa độ điểm $I$ được tính theo công thức: \\\\ $\\begin{cases} x_I = \\frac{x_A + x_B}{2} = \\frac{%s + (%s)}{2} = %s \\\\ y_I = \\frac{y_A + y_B}{2} = \\frac{%s + (%s)}{2} = %s \\\\ z_I = \\frac{z_A + z_B}{2} = \\frac{%s + (%s)}{2} = %s \\end{cases} \\Rightarrow I(%s;%s;%s)$. \\\\ Do đó trung điểm của đoạn thẳng $AB$ có tung độ bằng $y_I = %s$. Khẳng định là %s."""
        % (
            xa,
            xb,
            xi,
            ya,
            yb,
            yi,
            za,
            zb,
            zi,
            xi,
            yi,
            zi,
            yi_true,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Tồn tại điểm M trên mặt phẳng (Oxy) sao cho MA.MB nhỏ nhất, khi đó OM = ...[cite: 22]
    vdc_da_1_d = (
        "\\True Tồn tại điểm $M$ trên mặt phẳng $(Oxy)$ sao cho $\\vec{MA} \\cdot \\vec{MB}$ nhỏ nhất, khi đó $OM = %s$"
        % (str_om_true)
    )
    vdc_da_1_s = (
        "Tồn tại điểm $M$ trên mặt phẳng $(Oxy)$ sao cho $\\vec{MA} \\cdot \\vec{MB}$ nhỏ nhất, khi đó $OM = %s$"
        % (str_om_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Gọi $I(%s;%s;%s)$ là trung điểm của đoạn thẳng $AB$. \\\\ Ta có: \\\\ $\\vec{MA} \\cdot \\vec{MB} = (\\vec{MI} + \\vec{IA}) \\cdot (\\vec{MI} + \\vec{IB}) = (\\vec{MI} + \\vec{IA}) \\cdot (\\vec{MI} - \\vec{IA}) = MI^2 - IA^2 = MI^2 - \\frac{AB^2}{4}$. \\\\ Vì $A, B$ cố định nên $AB$ không đổi, do đó tích vô hướng $\\vec{MA} \\cdot \\vec{MB}$ nhỏ nhất khi và chỉ khi đoạn thẳng $MI$ ngắn nhất. \\\\ Do điểm $M$ thuộc mặt phẳng tọa độ $(Oxy)$ nên $MI$ ngắn nhất khi $M$ là hình chiếu vuông góc của điểm $I$ lên mặt phẳng $(Oxy)$. \\\\ Suy ra tọa độ điểm $M$ là: $M(x_I; y_I; 0) = M(%s; %s; 0)$. \\\\ Khi đó độ dài đoạn thẳng $OM$ là: \\\\ $OM = \\sqrt{x_M^2 + y_M^2 + z_M^2} = \\sqrt{(%s)^2 + (%s)^2 + 0^2} = \\sqrt{%s} = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            xi,
            yi,
            zi,
            xi,
            yi,
            xi,
            yi,
            om_sq,
            str_om_true,
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
    