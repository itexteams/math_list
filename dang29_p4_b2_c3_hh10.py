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


def bt_dang29_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            def tao_bo_so_dep():
                # Danh sách bộ số (M, S) đảm bảo nghiệm a, b đẹp
                danh_sach_bo_dep = [
                    {'M': (3, 2), 'S': 12}, # Nghiệm: a=4, a=9
                    {'M': (1, 1), 'S': 4},  # Nghiệm: a=2 (tiếp xúc)
                    {'M': (2, 4), 'S': 12}, # Nghiệm: a=4, a=6
                    {'M': (1, 2), 'S': 6},  # Nghiệm: a=2, a=3
                    {'M': (4, 1), 'S': 9},  # Nghiệm: a=3, a=6
                    {'M': (2, 2), 'S': 8},  # Nghiệm: a=4
                ]
                return random.choice(danh_sach_bo_dep)

            # --- Khởi tạo dữ liệu ---
            bo_so = tao_bo_so_dep()
            x0, y0 = bo_so['M']
            S = bo_so['S']

            x, y, a_sym = symbols('x y a')

            # Phương trình: x0/a + y0/(S-a) = 1 => a^2 - (x0 - y0 + S)a + x0*S = 0
            he_so_a = 1
            he_so_b = -(x0 - y0 + S)
            he_so_c = x0 * S

            # Giải tìm a
            list_a = solve(he_so_a*a_sym**2 + he_so_b*a_sym + he_so_c, a_sym)

            results = []
            for val_a in list_a:
                val_b = S - val_a
                # Điều kiện cắt tia Ox, Oy là a > 0 và b > 0
                if val_a > 0 and val_b > 0:
                    # Phương trình: bx + ay - ab = 0
                    # Rút gọn hệ số bằng GCD (Ước chung lớn nhất)
                    A_val = int(val_b)
                    B_val = int(val_a)
                    C_val = -int(val_a * val_b)

                    u = math.gcd(math.gcd(A_val, B_val), C_val)

                    # Tạo biểu thức đại số đã rút gọn
                    pt_dt = (A_val//u)*x + (B_val//u)*y + (C_val//u)
                    results.append({'a': val_a, 'b': val_b, 'pt': pt_dt})

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (f"Trong mặt phẳng với hệ tọa độ $Oxy$, lập phương trình đường thẳng $\\Delta$ đi qua "
                             f"$M({x0};{y0})$ và cắt tia $Ox$ tại $A$, cắt tia $Oy$ tại $B$ "
                             f"sao cho $OA + OB = {S}$.")

            # --- Đáp án ---
            # Đáp án đúng (Lọc trùng nếu phương trình giống nhau trong trường hợp nghiệm kép)
            da_dung_list = list(set([f"${latex(r['pt'])} = 0$" for r in results]))
            da_d = "\\True " + " và ".join(da_dung_list)

            # Tạo các đáp án nhiễu
            s = [
                f"${latex(x + y - S)} = 0$",
                f"${latex(y0*x + x0*y - x0*y0)} = 0$",
                f"${latex(x + y - (x0+y0))} = 0$",
                f"${latex(x - y + 1)} = 0$"
            ]
            random.shuffle(s)
            da_s1, da_s2, da_s3 = s[0], s[1], s[2]

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # --- Lời giải chi tiết ---
            loigiai = (f"Do $\\Delta$ cắt tia $Ox$ tại $A(a; 0)$ và tia $Oy$ tại $B(0; b)$ ($a, b > 0$)\\\\\n"
                       f"nên phương trình $\\Delta$ có dạng: $\\frac{{x}}{{a}} + \\frac{{y}}{{b}} = 1$ hay $bx + ay - ab = 0$.\\\\\n"
                       f"Theo giả thiết $OA + OB = {S} \\Rightarrow a + b = {S} \\Rightarrow b = {S} - a$. (*)\\\\\n"
                       f"Vì $M({x0}; {y0}) \\in \\Delta$ nên: $\\frac{{{x0}}}{{a}} + \\frac{{{y0}}}{{b}} = 1$.\\\\\n"
                       f"Thay (*) vào ta có: ${x0}({S} - a) + {y0}a = a({S} - a) \\Leftrightarrow a^2 - {abs(he_so_b)}a + {he_so_c} = 0$.\\\\\n"
                       f"Giải phương trình ta được: " + " hoặc ".join([f"$a = {latex(r)}$" for r in list_a]) + ".\\\\\n")

            for r in results:
                loigiai += (f"Với $a = {latex(r['a'])}$, suy ra $b = {S} - {latex(r['a'])} = {latex(r['b'])} $."
                            f" Ta có $\\Delta: {latex(r['pt'])} = 0$.\\\\\n")

            # --- Xuất kết quả theo định dạng yêu cầu ---
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content 

