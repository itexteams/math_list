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


def bt_dang34_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, y, t = symbols('x y t')

            # Vòng lặp để đảm bảo tìm được bộ số có nghiệm hữu tỉ đẹp
            while True:
                try:
                    # --- B1: Sinh số liệu ngẫu nhiên ---
                    xI_val = random.randint(-3, 3)
                    yI_val = random.randint(-3, 3)

                    # Đường thẳng d: ax + by + c = 0. Chọn b=1 hoặc -1 để rút y theo t dễ
                    a_coeff = random.randint(1, 3)
                    b_coeff = random.choice([-1, 1])
                    c_coeff = -(a_coeff * xI_val + b_coeff * yI_val)

                    line_eq = a_coeff * x + b_coeff * y + c_coeff
                    y_t = simplify((-a_coeff * t - c_coeff) / b_coeff)

                    # Chọn bán kính R^2 là tổng 2 số chính phương để tọa độ A, B nguyên
                    r_sq = random.choice([5, 10, 13, 17, 25, 26, 40, 50])

                    def get_points(center_x, center_y, r2):
                        pts = []
                        for dx in range(-10, 11):
                            for dy in range(-10, 11):
                                if dx**2 + dy**2 == r2:
                                    pts.append((center_x + dx, center_y + dy))
                        return pts

                    all_pts = get_points(xI_val, yI_val, r_sq)
                    if len(all_pts) < 2: continue
                    A_pt, B_pt = random.sample(all_pts, 2)

                    # --- B2: Giải chi tiết ---
                    dist_A_sq = (A_pt[0] - t)**2 + (A_pt[1] - y_t)**2
                    dist_B_sq = (B_pt[0] - t)**2 + (B_pt[1] - y_t)**2

                    ia_exp = expand(dist_A_sq)
                    ib_exp = expand(dist_B_sq)

                    sol_list = solve(ia_exp - ib_exp, t)
                    if not sol_list: continue
                    sol_t = sol_list[0]
                    if not sol_t.is_rational: continue # Chỉ lấy nghiệm hữu tỉ

                    final_yI = y_t.subs(t, sol_t)
                    break # Đã tìm được bộ số đẹp, thoát vòng lặp
                except:
                    continue

            # --- B3: Xử lý hiển thị (Dấu - - thành + và + - thành -) ---
            def clean(expr):
                return str(latex(expr)).replace("+ -", "-").replace("- -", "+")

            d_lat = clean(line_eq)
            y_t_lat = clean(y_t)

            noidungcauhoi = (f"Trong mặt phẳng với hệ tọa độ $Oxy$, cho đường thẳng $d: {d_lat} = 0$ "
                             f"và hai điểm $A({A_pt[0]};{A_pt[1]}), B({B_pt[0]};{B_pt[1]})$. "
                             f"Lập phương trình đường tròn $(C)$ có tâm thuộc $d$ và đi qua hai điểm $A, B$.")

            def fmt_c(x0, y0, r2):
                px = "x" if x0 == 0 else (f"(x - {latex(x0)})" if x0 > 0 else f"(x + {latex(abs(x0))})")
                py = "y" if y0 == 0 else (f"(y - {latex(y0)})" if y0 > 0 else f"(y + {latex(abs(y0))})")
                return f"{px}^2 + {py}^2 = {r2}".replace("- 0", "")

            circle_res = fmt_c(sol_t, final_yI, r_sq)

            loigiai = (
                f"Gọi $I(t; y_I)$ là tâm của đường tròn $(C)$. Do $I \\in d$ nên: "
                f"${latex(a_coeff)}t {'+' if b_coeff > 0 else ''} {latex(b_coeff)}y_I {'+' if c_coeff > 0 else ''} {latex(c_coeff)} = 0 \\Rightarrow y_I = {y_t_lat}$.\\\\ "
                f"Tâm $I(t; {y_t_lat})$. Vì $A, B \\in (C) \\Rightarrow IA^2 = IB^2$\\\\ "
                f"$\\Leftrightarrow ( {A_pt[0]} - t )^2 + ( {A_pt[1]} - ({y_t_lat}) )^2 = ( {B_pt[0]} - t )^2 + ( {B_pt[1]} - ({y_t_lat}) )^2$\\\\ "
                f"$\\Leftrightarrow {clean(ia_exp)} = {clean(ib_exp)}$\\\\ "
                f"$\\Leftrightarrow {clean(simplify(ia_exp - ib_exp))} = 0 \\Leftrightarrow t = {latex(sol_t)}$.\\\\ "
                f"Suy ra $I({latex(sol_t)}; {latex(final_yI)})$ và $R^2 = {r_sq}$.\\\\ "
                f"Vậy $(C): {circle_res}$.")

            # Đáp án
            da_dung = f"${circle_res}$"
            list_1 = ['\\True ' + da_dung, 
                      f"${fmt_c(-sol_t, final_yI, r_sq)}$", 
                      f"${fmt_c(sol_t, -final_yI, r_sq)}$", 
                      f"${fmt_c(sol_t, final_yI, r_sq + 5)}$"]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

