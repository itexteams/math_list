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


def bt_dang45_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Số lượng câu hỏi bạn muốn tạo ra
            so_luong_cau_hoi = 5
            toan_bo_noi_dung = ""

            for cau in range(so_luong_cau_hoi):
                # --- BẮT ĐẦU PHẦN LOGIC RANDOM ---
                scale = random.choice([1, 2, 3])
                shift = random.randint(1, 6)

                if random.choice([True, False]):
                    b1 = [2, 4, 6, 8]
                    b2 = [1, 3, 5, 7, 9]
                else:
                    b1 = [1, 3, 5, 7, 9]
                    b2 = [2, 4, 6, 8]

                box1 = sorted([val * scale + shift for val in b1])
                box2 = sorted([val * scale + shift for val in b2])
                box3 = sorted([val * scale + shift for val in [10, 11, 12]])

                def get_aps(s):
                    s_sorted = sorted(list(s))
                    aps = []
                    for c in itertools.combinations(s_sorted, 3):
                        if c[1] - c[0] == c[2] - c[1]:
                            aps.append(c)
                    return aps

                def fset(s):
                    return "\\{" + "; ".join(map(str, sorted(s))) + "\\}"

                # Tính toán trường hợp 1 (mặt chẵn)
                pairs1 = list(itertools.combinations(box1, 2))
                n_omega1 = len(pairs1)
                str_case1 = ""
                sum_aps1 = 0
                terms1 = []
                for p in pairs1:
                    new_box = box3 + list(p)
                    aps = get_aps(new_box)
                    n_aps = len(aps)
                    sum_aps1 += n_aps
                    terms1.append(str(n_aps))
                    if n_aps > 0:
                        ap_str = ", ".join([fset(ap) for ap in aps])
                        str_case1 += "+ Chuyển $%s$: có $%s$ bộ CSC là $%s$.\\\\\n" % (fset(p), n_aps, ap_str)
                    else:
                        str_case1 += "+ Chuyển $%s$: có $0$ bộ CSC.\\\\\n" % (fset(p))
                sum_str1 = " + ".join(terms1)
                p_A_chan = Rational(sum_aps1, n_omega1 * 10)

                # Tính toán trường hợp 2 (mặt lẻ)
                pairs2 = list(itertools.combinations(box2, 2))
                n_omega2 = len(pairs2)
                str_case2 = ""
                sum_aps2 = 0
                terms2 = []
                for p in pairs2:
                    new_box = box3 + list(p)
                    aps = get_aps(new_box)
                    n_aps = len(aps)
                    sum_aps2 += n_aps
                    terms2.append(str(n_aps))
                    if n_aps > 0:
                        ap_str = ", ".join([fset(ap) for ap in aps])
                        str_case2 += "+ Chuyển $%s$: có $%s$ bộ CSC là $%s$.\\\\\n" % (fset(p), n_aps, ap_str)
                    else:
                        str_case2 += "+ Chuyển $%s$: có $0$ bộ CSC.\\\\\n" % (fset(p))
                sum_str2 = " + ".join(terms2)
                p_A_le = Rational(sum_aps2, n_omega2 * 10)

                # Xác suất toàn phần
                p_total = Rational(1, 2) * p_A_chan + Rational(1, 2) * p_A_le
                a_val = int(p_total * 100)

                t1 = Rational(1, 2) * p_A_chan
                t2 = Rational(1, 2) * p_A_le
                lcm_den = math.lcm(t1.q, t2.q)
                num1 = t1.p * (lcm_den // t1.q)
                num2 = t2.p * (lcm_den // t2.q)

                # Hàm vẽ TikZ
                def generate_tikz(b1, b2, b3):
                    tikz = "\\begin{center}\n\\begin{tikzpicture}[line width=1pt, scale=0.85, every node/.style={transform shape}]\n"
                    w1 = len(b1) * 0.8 + 0.2
                    tikz += "\\draw[blue!80, rounded corners] (0,0) rectangle (%s, 1.5);\n" % w1
                    tikz += "\\node[blue!80] at (%s, 1.8) {Hộp I};\n" % (w1/2)
                    for i, val in enumerate(b1):
                        x = 0.5 + i * 0.8
                        tikz += "\\draw[blue!80] (%s, 0.75) circle (0.35);\n" % x
                        tikz += "\\node[blue!80] at (%s, 0.75) {%s};\n" % (x, val)

                    startX2 = w1 + 0.5
                    w2 = len(b2) * 0.8 + 0.2
                    tikz += "\\draw[green!60!black, rounded corners] (%s,0) rectangle (%s, 1.5);\n" % (startX2, startX2+w2)
                    tikz += "\\node[green!60!black] at (%s, 1.8) {Hộp II};\n" % (startX2 + w2/2)
                    for i, val in enumerate(b2):
                        x = startX2 + 0.5 + i * 0.8
                        tikz += "\\draw[green!60!black] (%s, 0.75) circle (0.35);\n" % x
                        tikz += "\\node[green!60!black] at (%s, 0.75) {%s};\n" % (x, val)

                    startX3 = startX2 + w2 + 0.5
                    w3 = len(b3) * 0.8 + 0.2
                    tikz += "\\draw[violet, rounded corners] (%s,0) rectangle (%s, 1.5);\n" % (startX3, startX3+w3)
                    tikz += "\\node[violet] at (%s, 1.8) {Hộp III};\n" % (startX3 + w3/2)
                    for i, val in enumerate(b3):
                        x = startX3 + 0.5 + i * 0.8
                        tikz += "\\draw[violet] (%s, 0.75) circle (0.35);\n" % x
                        tikz += "\\node[violet] at (%s, 0.75) {%s};\n" % (x, val)

                    startDie = startX3 + w3 + 0.5
                    tikz += "\\begin{scope}[shift={(%s,0.2)}]\n" % startDie
                    tikz += "\\draw[rounded corners=2pt, fill=white] (0,0) rectangle (1,1);\n"
                    tikz += "\\draw[rounded corners=1pt, fill=white] (0,1) -- (0.3,1.3) -- (1.3,1.3) -- (1,1);\n"
                    tikz += "\\draw[rounded corners=1pt, fill=white] (1,0) -- (1.3,0.3) -- (1.3,1.3);\n"
                    tikz += "\\draw (0,1) -- (1,1) -- (1,0);\n"
                    tikz += "\\fill (0.5,0.5) circle (2pt);\n"
                    tikz += "\\fill (0.2,0.8) circle (2pt);\n"
                    tikz += "\\fill (0.8,0.2) circle (2pt);\n"
                    tikz += "\\fill (0.2,0.2) circle (2pt);\n"
                    tikz += "\\fill (0.8,0.8) circle (2pt);\n"
                    tikz += "\\fill (1.15,0.8) circle (1.5pt);\n" 
                    tikz += "\\fill (1.15,0.5) circle (1.5pt);\n"
                    tikz += "\\fill (0.65,1.15) circle (1.5pt);\n" 
                    tikz += "\\node[blue!80!black] at (0.65, -0.4) {Xúc xắc};\n"
                    tikz += "\\end{scope}\n"
                    tikz += "\\end{tikzpicture}\n\\end{center}\n"
                    return tikz

                noidungcauhoi = ('''Có ba hộp đựng bi. Hộp I đựng %s viên bi được đánh số $%s$. Hộp II đựng %s viên bi được đánh số $%s$. Hộp III đựng %s viên bi được đánh số $%s$. Gieo một con xúc xắc cân đối và đồng chất:
            %s - Nếu ra mặt chẵn thì chọn ngẫu nhiên 2 viên từ hộp I bỏ sang hộp III.\\\\
            - Nếu ra mặt lẻ thì chọn ngẫu nhiên 2 viên từ hộp II bỏ sang hộp III. \\\\
            Sau đó, chọn ngẫu nhiên 3 viên bi từ hộp III. Xác suất để ba viên bi rút được lập thành một cấp số cộng là $a\\%%$. Giá trị của $a$ bằng bao nhiêu?''' % (len(box1), fset(box1), len(box2), fset(box2), len(box3), fset(box3), generate_tikz(box1, box2, box3)))

                da = "$%s$" % a_val
                pool = [a_val + i for i in [-4, -3, -2, -1, 1, 2, 3, 4, 5]]
                s = random.sample(pool, 3)

                list_1 = ['\\True ' + str(da), "$%s$" % s[0], "$%s$" % s[1], "$%s$" % s[2]]
                random.shuffle(list_1)

                loigiai = ('''Gọi $A$ là biến cố: "Ba viên bi rút từ hộp III lập thành một cấp số cộng".\\\\
            Xét theo kết quả gieo xúc xắc:\\\\
            1) Xúc xắc ra mặt chẵn $\\left(P = \\frac{1}{2}\\right)$:\\\\
            Chọn ngẫu nhiên 2 viên từ hộp I sang hộp III: có $C\\left(%s,2\\right) = %s$ cách.\\\\
            Khi đó hộp III có 5 viên nên số cách chọn 3 viên là $C\\left(5,3\\right) = 10$.\\\\
            %sSuy ra 
            $$P\\left(A | \\text{chẵn}\\right) = \\frac{%s}{%s \\cdot 10} = \\frac{%s}{%s} = %s.$$\\\\
            2) Xúc xắc ra mặt lẻ $\\left(P = \\frac{1}{2}\\right)$:\\\\
            Chọn ngẫu nhiên 2 viên từ hộp II sang hộp III: có $C\\left(%s,2\\right) = %s$ cách.\\\\
            Khi đó hộp III có 5 viên nên số cách chọn 3 viên là $C\\left(5,3\\right) = 10$.\\\\
            %sDo đó 
            $$P\\left(A | \\text{lẻ}\\right) = \\frac{%s}{%s \\cdot 10} = \\frac{%s}{%s} = %s.$$\\\\
            Áp dụng công thức xác suất toàn phần:\\\\
            $\\begin{aligned} P\\left(A\\right) &= \\left(\\frac{1}{2}\\right) \\cdot P\\left(A | \\text{chẵn}\\right) + \\left(\\frac{1}{2}\\right) \\cdot P\\left(A | \\text{lẻ}\\right) \\\\ &= \\left(\\frac{1}{2}\\right) \\cdot \\left(%s\\right) + \\left(\\frac{1}{2}\\right) \\cdot \\left(%s\\right) \\\\ &= %s + %s = \\frac{%s}{%s} + \\frac{%s}{%s} = %s = %s\\%%. \\end{aligned}$\\\\
            Vậy $a = %s$.'''
                           % (len(box1), n_omega1, str_case1, sum_str1, n_omega1, sum_aps1, n_omega1 * 10, latex(p_A_chan),
                              len(box2), n_omega2, str_case2, sum_str2, n_omega2, sum_aps2, n_omega2 * 10, latex(p_A_le),
                              latex(p_A_chan), latex(p_A_le), latex(t1), latex(t2), num1, lcm_den, num2, lcm_den, latex(p_total), a_val, a_val))
                dapan='\\shortans[0]{$%s$}\n'%(a_val)
                # Đóng gói thành LaTeX
                content = ( '\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                           '\\loigiai{'+str(loigiai)+'}\n'
                           '\\end{ex}\n\\end{minipage} \n\n')
            return content

