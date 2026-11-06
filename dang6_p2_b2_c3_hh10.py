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


def bt_dang6_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y, t = symbols('x y t')

            # --- HÀM HỖ TRỢ ---
            def get_random_excluded(start, end, excluded=[0, 1, -1]):
                """Chọn số ngẫu nhiên và tránh các số trong danh sách excluded"""
                res = random.randint(start, end)
                while res in excluded:
                    res = random.randint(start, end)
                return res

            def simplify_vector(a, b):
                """Tối giản tọa độ vectơ (a, b)"""
                common = math.gcd(a, b)
                # Chia cho common để tối giản, đảm bảo tọa độ đầu tiên dương để trình bày đẹp
                ra, rb = a // common, b // common
                if ra < 0 or (ra == 0 and rb < 0):
                    ra, rb = -ra, -rb
                return ra, rb

            # --- RANDOM DỮ LIỆU ---

            # Câu a: Tham số -> Tổng quát
            x0_a = get_random_excluded(-5, 5)
            y0_a = get_random_excluded(-10, 10)
            u1_raw = get_random_excluded(-6, 6)
            u2_raw = get_random_excluded(-6, 6)

            # Tối giản vectơ chỉ phương u
            u1_a, u2_a = simplify_vector(u1_raw, u2_raw)

            # Vectơ pháp tuyến n từ u=(u1, u2) là n=(u2, -u1). Tối giản n:
            n1_a, n2_a = simplify_vector(u2_a, -u1_a)

            # PT tổng quát: n1(x - x0) + n2(y - y0) = 0
            pt_dung_a_expr = simplify(n1_a*(x - x0_a) + n2_a*(y - y0_a))
            pt_sai_a_expr = simplify(u1_a*(x - x0_a) + u2_a*(y - y0_a)) # Dùng nhầm u làm n

            # Câu b: Đoạn chắn (Giữ nguyên vì dạng x/a + y/b thường không cần tối giản kiểu vectơ)
            a_b = get_random_excluded(-8, 8) 
            b_b = get_random_excluded(-8, 8) 

            # Câu c: Vuông góc và qua O(0,0)
            A_c = get_random_excluded(-9, 9)
            B_c = get_random_excluded(-9, 9)
            C_c = get_random_excluded(-15, 15)

            # d: Ax + By + C = 0 có n=(A, B). Delta vuông góc d => n_delta = u_d = (B, -A)
            n1_c, n2_c = simplify_vector(B_c, -A_c)
            pt_dung_c_expr = simplify(n1_c*x + n2_c*y)
            pt_sai_c_expr = simplify(A_c*x + B_c*y) # Nhầm sang song song

            # Câu d: Song song qua M (Hệ số góc k)
            xm_d = get_random_excluded(-5, 5)
            ym_d = get_random_excluded(-5, 5)
            k_d = get_random_excluded(-5, 5)
            m_orig_d = get_random_excluded(-10, 10)
            const_dung_d = ym_d - k_d * xm_d
            const_sai_d = const_dung_d + random.choice([-3, -2, 2, 3])

            # Nội dung câu hỏi
            noidungcauhoi = "Trong mặt phẳng tọa độ $Oxy$."

            ########################################################################
            # Lập danh sách đáp án và lời giải chi tiết
            ########################################################################

            # --- Câu a ---
            txt_pt_a = "\\begin{cases} x = %s %s %s t \\\\ y = %s %s %s t \\end{cases}" % (
                x0_a, "+" if u1_a > 0 else "-", abs(u1_a), 
                y0_a, "+" if u2_a > 0 else "-", abs(u2_a)
            )
            nb_da_1_d = "\\True Phương trình tổng quát của đường thẳng $d: %s$ là $%s = 0$" % (txt_pt_a, latex(pt_dung_a_expr))
            nb_da_1_s = "Phương trình tổng quát của đường thẳng $d: %s$ là $%s = 0$" % (txt_pt_a, latex(pt_sai_a_expr))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ("Đường thẳng $d$ đi qua điểm $M(%s; %s)$ và có vectơ chỉ phương $\\vec{u} = (%s; %s)$. \\\\"
                           "Suy ra $d$ có vectơ pháp tuyến tối giản là $\\vec{n} = (%s; %s)$. \\\\"
                           "Phương trình tổng quát: $%s(x - %s) %s %s(y - %s) = 0 \\Leftrightarrow %s = 0$." 
                           % (x0_a, y0_a, u1_a, u2_a, n1_a, n2_a, n1_a, x0_a, "+" if n2_a > 0 else "-", abs(n2_a), y0_a, latex(pt_dung_a_expr)))

            # --- Câu b ---
            th_da_1_d = "\\True Phương trình đường thẳng đi qua $A(0;%s)$, $B(%s;0)$ là $\\frac{x}{%s} + \\frac{y}{%s} = 1$" % (b_b, a_b, a_b, b_b)
            th_da_1_s = "Phương trình đường thẳng đi qua $A(0;%s)$, $B(%s;0)$ là $\\frac{x}{%s} + \\frac{y}{%s} = 1$" % (b_b, a_b, b_b, a_b)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ("Đường thẳng cắt trục hoành tại $B(%s; 0)$ và cắt trục tung tại $A(0; %s)$. \\\\"
                           "Áp dụng công thức đoạn chắn $\\frac{x}{a} + \\frac{y}{b} = 1$ với $a=%s, b=%s$." % (a_b, b_b, a_b, b_b))

            # --- Câu c ---
            vd_da_1_d = "\\True Đường thẳng $\\Delta$ qua $O(0;0)$ và vuông góc với $d: %s x %s %s y + %s = 0$ là $%s = 0$" % (A_c, "+" if B_c > 0 else "", B_c, C_c, latex(pt_dung_c_expr))
            vd_da_1_s = "Đường thẳng $\\Delta$ qua $O(0;0)$ và vuông góc với $d: %s x %s %s y + %s = 0$ là $%s = 0$" % (A_c, "+" if B_c > 0 else "", B_c, C_c, latex(pt_sai_c_expr))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ("Đường thẳng $d$ có $\\vec{n}_d = (%s; %s)$. \\\\"
                           "Vì $\\Delta \\perp d$ nên $\\Delta$ có vectơ pháp tuyến $\\vec{n}_{\\Delta} = \\vec{u}_d = (%s; %s)$. \\\\"
                           "Tối giản vectơ pháp tuyến ta được $\\vec{n}_{\\Delta} = (%s; %s)$. \\\\"
                           "Phương trình $\\Delta$: $%s x %s %s y = 0$." 
                           % (A_c, B_c, B_c, -A_c, n1_c, n2_c, n1_c, "+" if n2_c > 0 else "-", abs(n2_c)))

            # --- Câu d ---
            vdc_da_1_d = "\\True Đường thẳng $\\Delta'$ qua $M(%s; %s)$ và song song với $d': y = %s x + %s$ là $y = %s x %s %s$" % (xm_d, ym_d, k_d, m_orig_d, k_d, "+" if const_dung_d > 0 else "", const_dung_d)
            vdc_da_1_s = "Đường thẳng $\\Delta'$ qua $M(%s; %s)$ và song song với $d': y = %s x + %s$ là $y = %s x %s %s$" % (xm_d, ym_d, k_d, m_orig_d, k_d, "+" if const_sai_d > 0 else "", const_sai_d)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ("$\\Delta' // d'$ nên $\\Delta'$ có hệ số góc $k = %s$. \\\\"
                            "Phương trình: $y = %s(x - %s) + %s \\Leftrightarrow y = %s x %s %s$." 
                            % (k_d, k_d, xm_d, ym_d, k_d, "+" if const_dung_d > 0 else "", const_dung_d))

            # --- LOGIC XUẤT BÀI ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a, ans_b, ans_c, ans_d = random.choice(list_nb_da_1), random.choice(list_th_da_1), random.choice(list_vd_da_1), random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+').replace('--', '+')
            return content   

