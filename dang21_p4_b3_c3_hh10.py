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


def bt_dang21_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y, t = symbols('x y t')

            # --- B3: Suy nghĩ tìm cách random bài toán để nghiệm là SỐ HỮU TỶ ---
            def generate_rational_problem():
                while True:
                    # Tọa độ tâm I(a, b) và bán kính R^2
                    a_val = random.randint(-5, 5)
                    b_val = random.randint(-5, 5)
                    R2_val = random.choice([25, 100, 169, 225, 25, 50, 65]) # Ưu tiên R nguyên hoặc R^2 đẹp

                    # Đường thẳng d: x + m*y + n = 0 => x = -mt - n
                    m_val = random.randint(-3, 3)
                    if m_val == 0: m_val = 1
                    n_val = random.randint(-5, 5)

                    # N thuộc d => N(-m*t - n, t). M đối xứng N qua Ox => M(-m*t - n, -t)
                    # Thay M vào (C): (-m*t - n - a)^2 + (-t - b)^2 - R2 = 0
                    # PT có dạng: At^2 + Bt + C = 0
                    A = m_val**2 + 1
                    B = 2 * (m_val * (n_val + a_val) + b_val)
                    C = (n_val + a_val)**2 + b_val**2 - R2_val

                    delta = B**2 - 4*A*C

                    # Điều kiện để nghiệm hữu tỷ: Delta là số chính phương và Delta > 0
                    if delta > 0:
                        sq_delta = int(sqrt(delta))
                        if sq_delta * sq_delta == delta:
                            return a_val, b_val, R2_val, m_val, n_val, A, B, C

            # Lấy bộ số đẹp
            a_v, b_v, R2_v, m_v, n_v, A_v, B_v, C_v = generate_rational_problem()

            # --- B2: Viết lại bài toán theo mẫu code ---

            # 1. Thiết lập biểu thức Sympy
            pt_tron_hien_thi = (x - a_v)**2 + (y - b_v)**2
            pt_d_hien_thi = x + m_v*y + n_v

            # Giải phương trình
            pt_bac_2 = A_v*t**2 + B_v*t + C_v
            sol_t = solve(pt_bac_2, t)

            # Tọa độ các cặp điểm
            pairs = []
            for val_t in sol_t:
                n_x = -m_v * val_t - n_v
                n_y = val_t
                m_x = n_x
                m_y = -val_t
                pairs.append({'M': (m_x, m_y), 'N': (n_x, n_y)})

            # Định dạng hiển thị
            def format_point(p):
                return f"({latex(p[0])}; {latex(p[1])})"

            res_str = " \\text{ hoặc }".join([f"M{format_point(p['M'])}, N{format_point(p['N'])}" for p in pairs])

            # --- Nội dung câu hỏi ---
            noidungcauhoi = f"Trong mặt phẳng với hệ tọa độ $Oxy$, cho đường tròn $(C): {latex(pt_tron_hien_thi)} = {R2_v}$ và đường thẳng $d: {latex(pt_d_hien_thi)} = 0$. Tìm trên $(C)$ điểm $M$ và trên $d$ điểm $N$ sao cho hai điểm $M, N$ đối xứng nhau qua $Ox$."

            # --- Đáp án ---
            da_d = f"\\True ${res_str}$"
            da_s1 = f"$M{format_point((pairs[0]['M'][0]+1, pairs[0]['M'][1]))}, N{format_point((pairs[0]['N'][0]+1, pairs[0]['N'][1]))}$"
            da_s2 = f"$M{format_point((pairs[0]['M'][1], pairs[0]['M'][0]))}, N{format_point((pairs[0]['N'][1], pairs[0]['N'][0]))}$"
            da_s3 = f"$M{format_point((-pairs[0]['M'][0], pairs[0]['M'][1]))}, N{format_point((-pairs[0]['N'][0], pairs[0]['N'][1]))}$"

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # --- Lời giải ---
            x_N_expr = -m_v*t - n_v
            loigiai = f"""Do $N \\in d$ nên $N({latex(x_N_expr)}; t)$. Điểm $M$ đối xứng với $N$ qua $Ox$ nên $M({latex(x_N_expr)}; -t)$. \\\\
            Mặt khác, $M \\in (C)$ nên:
            $$({latex(x_N_expr - a_v)})^2 + ({latex(-t - b_v)})^2 = {R2_v}$$
            $$\\Leftrightarrow {latex(expand(pt_bac_2))} = 0$$
            $$\\Leftrightarrow t = {latex(sol_t[0])} \\text{{ hoặc }} t = {latex(sol_t[1])}$$
            Vậy có các cặp điểm cần tìm là: ${res_str}$."""

            # Thay thế các lỗi hiển thị dấu
            loigiai = loigiai.replace("+-", "-").replace("- -", "+").replace("+ -", "-")

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

