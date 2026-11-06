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


def bt_dang29_p1_b3_c4_ds10(self):
            # Khai báo biến
            # --- KHỞI TẠO BIẾN ---
            m = symbols('m')

            # --- BƯỚC 1: TÌM BỘ SỐ ĐẸP ---
            while True:
                k1, k2, k3 = random.randint(-5, 5), random.randint(-5, 5), random.randint(-10, 10)
                if k3 == 0 or k1 == k2: continue

                A = m + k1
                B = 2 * (m + k2)
                C = k3

                # Tính Delta'
                b_p = m + k2
                d_s1 = expand(b_p**2)
                d_s2 = expand(A * C)
                delta_f = simplify(d_s1 - d_s2)

                poly_d = Poly(delta_f, m)
                if poly_d.degree() != 2: continue

                h = poly_d.all_coeffs()
                a_d, b_d, c_d = h[0], h[1], h[2]

                delta_m = b_d**2 - 4*a_d*c_d
                if delta_m > 0:
                    sq = int(delta_m**0.5)
                    if sq * sq == delta_m:
                        roots = sorted(solve(delta_f, m))
                        m1, m2 = roots[0], roots[1]
                        m_cam = -k1
                        if m_cam != m1 and m_cam != m2: break

            # --- BƯỚC 2: CHUẨN HÓA LATEX ---
            m1_t, m2_t, mc_t = latex(m1), latex(m2), latex(m_cam)
            delta_t = latex(delta_f)
            A_t, B_t, C_t = latex(A), latex(B), latex(C)

            cases_2n = "\\begin{cases} a \\neq 0 \\\\ \\Delta' > 0 \\end{cases}"
            inf_p, inf_n = "+\\infty", "-\\infty"

            def get_logic(d_type, a_val, v1, v2):
                outside = (d_type == ">" and a_val > 0) or (d_type == "<" and a_val < 0)
                if outside:
                    return "m < " + str(v1) + " \\text{ hoặc } m > " + str(v2), "(" + str(inf_n) + "; " + str(v1) + ") \\cup (" + str(v2) + "; " + str(inf_p) + ")"
                return str(v1) + " < m < " + str(v2), "(" + str(v1) + "; " + str(v2) + ")"

            # --- BƯỚC 3: XỬ LÝ DẠNG BÀI ---
            delta_step = "\\Delta' = (" + latex(b_p) + ")^2 - (" + A_t + ")(" + C_t + ") = " + latex(d_s1) + " - (" + latex(d_s2) + ") = " + delta_t

            lisdang = ['1', '2', '4']
            dang = random.choice(lisdang)

            if dang == '1': # Hai nghiệm phân biệt
                yeucau = "có hai nghiệm phân biệt"
                cond, tap = get_logic(">", a_d, m1_t, m2_t)
                da_dung = "m \\in " + tap + " \\setminus \\{ " + mc_t + " \\}"
                loigiai = ("Phương trình (1) có hai nghiệm phân biệt $\\Leftrightarrow " + cases_2n + "$ \\\\ \n"
                           "$\\bullet$ $a \\neq 0 \\Leftrightarrow " + A_t + " \\neq 0 \\Leftrightarrow m \\neq " + mc_t + "$. \\\\ \n"
                           "$\\bullet$ $" + delta_step + "$. \\\\ \n"
                           "Xét dấu $\\Delta' > 0 \\Leftrightarrow " + delta_t + " > 0 \\Leftrightarrow " + cond + "$ \\\\ \n"
                           "Kết hợp điều kiện $a \\neq 0$, ta được: $" + da_dung + "$.")

            elif dang == '2': # Vô nghiệm
                yeucau = "vô nghiệm"
                cond, tap = get_logic("<", a_d, m1_t, m2_t)
                da_dung = "m \\in " + tap
                loigiai = ("Phương trình (1) vô nghiệm trong các trường hợp sau: \\\\ \n"
                           "$\\bullet$ TH1: $a = 0 \\Leftrightarrow m = " + mc_t + "$. Thay vào (1) ta được PT bậc nhất có nghiệm (Loại). \\\\ \n"
                           "$\\bullet$ TH2: $a \\neq 0$ và $\\Delta' < 0 \\Leftrightarrow \\begin{cases} m \\neq " + mc_t + " \\\\ " + delta_t + " < 0 \\end{cases}$. \\\\ \n"
                           "Giải hệ điều kiện ta được: $m \\in " + tap + "$.")

            else: # Có nghiệm
                yeucau = "có nghiệm"
                _, tap = get_logic(">", a_d, m1_t, m2_t)
                da_dung = tap.replace("(", "[").replace(")", "]").replace("[" + inf_n, "(" + inf_n).replace(inf_p + "]", inf_p + ")")
                loigiai = ("Phương trình (1) có nghiệm khi xảy ra một trong hai trường hợp sau: \\\\ \n"
                           "$\\bullet$ TH1: $a = 0 \\Leftrightarrow m = " + mc_t + "$. Thay vào (1) ta được phương trình bậc nhất luôn có nghiệm (Nhận $m = " + mc_t + "$). \\\\ \n"
                           "$\\bullet$ TH2: $a \\neq 0$ và $\\Delta' \\geq 0 \\Leftrightarrow \\begin{cases} m \\neq " + mc_t + " \\\\ " + delta_t + " \\geq 0 \\end{cases} \\Rightarrow m \\in " + da_dung + " \\setminus \\{ " + mc_t + " \\}$. \\\\ \n"
                           "Hợp hai trường hợp ta có kết quả cuối cùng: $" + da_dung + "$.")

            # --- BƯỚC 4: TỔNG HỢP ---
            noidungcauhoi = "Giá trị nào của $m$ để phương trình $(" + A_t + ")x^2 + (" + B_t + ")x + " + C_t + " = 0$ (1) " + yeucau + "?"

            da_d = "\\True $" + da_dung + "$"
            s = ["$m \\in (" + m1_t + "; " + m2_t + ")$", 
                 "$m \\in \\mathbb{R} \\setminus \\{ " + mc_t + " \\}$", 
                 "$m > " + m2_t + "$", 
                 "$m < " + m1_t + "$"]

            random.shuffle(s)
            da_s1 = s[0]
            da_s2 = s[1]
            da_s3 = s[2]

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('( -', '(-')
            return content

