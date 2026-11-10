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


def bt_dang71_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A thuộc Ox, B thuộc Oy, C thuộc Oz[cite: 20]
    # A(a; 0; 0), B(0; b; 0), C(0; 0; c) với a, b, c khác 0[cite: 20]
    while True:
        xa = random.choice([2, 3, 4, 5, 6])
        ya = 0
        za = 0
    
        xb = 0
        yb = random.choice([-3, -2, -1, 1, 2, 3])
        zb = 0
    
        xc = 0
        yc = 0
        zc = random.choice([-3, -2, -1, 1, 2, 3])
    
        # Tọa độ vectơ AB = (-xa; yb; 0)[cite: 20]
        ab_x = -xa
        ab_y = yb
        ab_z = 0
    
        # Diện tích tam giác vuông OAB tại O: S_OAB = 1/2 * OA * OB = 1/2 * |xa| * |yb|[cite: 20]
        s_oab = Rational(abs(xa) * abs(yb), 2)
    
        # Thể tích tứ diện vuông OABC tại O: V = 1/6 * OA * OB * OC = 1/6 * |xa| * |yb| * |zc|[cite: 20]
        v_oabc = Rational(abs(xa) * abs(yb) * abs(zc), 6)
    
        break
    
    # 1. Khẳng định a: Điểm C thuộc trục Oz (do xC = 0, yC = 0, zC != 0)[cite: 20]
    
    # 2. Khẳng định b: Tọa độ vectơ AB[cite: 20]
    # Tạo giá trị đúng và sai cho AB[cite: 20]
    ab_false_x = ab_x + random.choice([-1, 1])
    ab_false_y = ab_y + random.choice([-1, 1])
    if ab_false_x == ab_x and ab_false_y == ab_y:
        ab_false_x = -3
        ab_false_y = 2
    
    # 3. Khẳng định c: Diện tích tam giác OAB[cite: 20]
    str_s_true = format_fraction_latex(s_oab.p, s_oab.q)
    s_oab_false = s_oab + random.choice([-1, 1])
    if s_oab_false <= 0:
        s_oab_false = s_oab + Rational(3, 2)
    str_s_false = format_fraction_latex(s_oab_false.p, s_oab_false.q)
    
    # 4. Khẳng định d: Thể tích tứ diện OABC[cite: 20]
    str_v_true = format_fraction_latex(v_oabc.p, v_oabc.q)
    v_oabc_false = v_oabc + random.choice([-Rational(1, 2), Rational(1, 2), Rational(1, 3)])
    if v_oabc_false <= 0:
        v_oabc_false = v_oabc + 1
    str_v_false = format_fraction_latex(v_oabc_false.p, v_oabc_false.q)
    if str_v_false == str_v_true:
        str_v_false = "\\frac{5}{6}"
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho tam giác $ABC$ có $A(%s;0;0), B(0;%s;0)$ và $C(0;0;%s)$."""
        % (xa, yb, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Điểm C thuộc trục Oz[cite: 20]
    nb_da_1_d = "\\True Điểm $C$ thuộc trục $Oz$"
    nb_da_1_s = "Điểm $C$ thuộc trục $Oy$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Điểm $C$ có tọa độ là $C(0;0;%s)$, có hoành độ và tung độ đều bằng $0$ ($x_C = 0, y_C = 0$), cao độ $z_C = %s \\neq 0$. \\\\ Do đó điểm $C$ thuộc trục cao $Oz$."""
        % (zc, zc)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Tọa độ vectơ AB[cite: 20]
    nb_da_2_d = "\\True Tọa độ vectơ $\\vec{AB} = (%s;%s;0)$" % (ab_x, ab_y)
    nb_da_2_s = "Tọa độ vectơ $\\vec{AB} = (%s;%s;0)$" % (ab_false_x, ab_false_y)
    list_th_da_1 = [nb_da_2_d, nb_da_2_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Tọa độ của vectơ $\\vec{AB}$ được xác định bởi: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (0 - %s; %s - 0; 0 - 0) = (%s;%s;0)$. \\\\ Do đó mệnh đề là %s."""
        % (
            xa,
            yb,
            ab_x,
            ab_y,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Diện tích tam giác OAB[cite: 20]
    vd_da_1_d = "\\True Diện tích tam giác $OAB$ bằng $%s$" % (str_s_true)
    vd_da_1_s = "Diện tích tam giác $OAB$ bằng $%s$" % (str_s_false)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì điểm $A(%s;0;0) \\in Ox$ và $B(0;%s;0) \\in Oy$ nên tam giác $OAB$ vuông tại gốc tọa độ $O$. \\\\ Ta có: \\\\ $OA = |x_A| = |%s| = %s$. \\\\ $OB = |y_B| = |%s| = %s$. \\\\ Diện tích tam giác vuông $OAB$ là: \\\\ $S_{OAB} = \\frac{1}{2} OA \\cdot OB = \\frac{1}{2} \\cdot %s \\cdot %s = %s$. \\\\ Do đó khẳng định là %s."""
        % (
            xa,
            yb,
            xa,
            abs(xa),
            yb,
            abs(yb),
            abs(xa),
            abs(yb),
            str_s_true,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Thể tích tứ diện OABC[cite: 20]
    vdc_da_1_d = "\\True Thể tích tứ diện $OABC$ bằng $%s$" % (str_v_true)
    vdc_da_1_s = "Thể tích tứ diện $OABC$ bằng $%s$" % (str_v_false)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì ba điểm $A, B, C$ lần lượt thuộc ba trục tọa độ đôi một vuông góc $Ox, Oy, Oz$ nên tứ diện $OABC$ là tứ diện có ba cạnh $OA, OB, OC$ đôi một vuông góc tại đỉnh $O$. \\\\ Độ dài các cạnh là: \\\\ $OA = |%s| = %s$. \\\\ $OB = |%s| = %s$. \\\\ $OC = |%s| = %s$. \\\\ Thể tích khối tứ diện $OABC$ là: \\\\ $V_{OABC} = \\frac{1}{6} OA \\cdot OB \\cdot OC = \\frac{1}{6} \\cdot %s \\cdot %s \\cdot %s = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            xa,
            abs(xa),
            yb,
            abs(yb),
            zc,
            abs(zc),
            abs(xa),
            abs(yb),
            abs(zc),
            str_v_true,
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
    