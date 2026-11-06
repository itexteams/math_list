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


def bt_dang11_p3_b2_c1_hh12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # 1. Random thời gian bay
        t = random.choice([5, 10, 12, 15, 20, 30])

        # 2. Random tọa độ điểm A
        xA = random.randint(50, 150)
        yA = random.randint(20, 80)
        zA = random.randint(2, 8)

        # 3. Random vectơ độ dời (khoảng cách máy bay di chuyển trong t phút)
        vx = random.choice([50, 60, 80, 100, 120])
        vy = random.choice([30, 40, 50, 60, 80])
        vz = random.choice([2, 3, 4, 5, 6])

        # Tính tọa độ điểm B (B = A + v)
        xB = xA + vx
        yB = yA + vy
        zB = zA + vz

        # Tính tọa độ điểm C (C = B + v)
        xC = xB + vx
        yC = yB + vy
        zC = zB + vz

        # 4. Random hệ số m, n, p cho biểu thức T = m*a + n*b + p*c
        m = random.choice([1, 2, 3]) # Hệ số đầu ưu tiên dương
        n = random.randint(-3, 3)
        p = random.randint(-3, 3)

        # Đảm bảo hệ số không bằng 0
        if n == 0: n = 1
        if p == 0: p = 1

        kq = m * xC + n * yC + p * zC

        # --- CÁC HÀM XỬ LÝ CHUỖI ĐỂ TRÁNH DẤU + - LỘN XỘN ---
        def format_term(coef, var, is_first=False):
            if coef == 0: return ""
            abs_coef = abs(coef)
            coef_str = "" if abs_coef == 1 else str(abs_coef)
            if is_first:
                return f"-{coef_str}{var}" if coef < 0 else f"{coef_str}{var}"
            else:
                return f" - {coef_str}{var}" if coef < 0 else f" + {coef_str}{var}"

        # Chuỗi biểu thức T
        expr_str = f"{format_term(m, 'a', True)}{format_term(n, 'b', False)}{format_term(p, 'c', False)}"
        expr_str = expr_str.replace("+ -", "- ").replace("- -", "+ ")

        def format_sub(coef, val):
            if coef == 0: return "0"
            if coef == 1: return f"{val}"
            if coef == -1: return f"(-{val})" if val > 0 else f"{val}"
            val_str = f"({val})" if val < 0 else f"{val}"
            return f"{coef}\\cdot {val_str}"

        # Chuỗi phép thế
        sub_str = f"{format_sub(m, xC)} + {format_sub(n, yC)} + {format_sub(p, zC)}"
        sub_str = sub_str.replace("+ -", "- ").replace("- -", "+ ").replace("+ 0", "").replace("- 0", "").strip()

        # Xử lý tọa độ âm khi viết phương trình (vd: x - (-5) -> x + 5)
        def format_minus_coord(var, val):
            if val > 0: return f"{var} - {val}"
            elif val < 0: return f"{var} + {abs(val)}"
            else: return f"{var}"

        bc_x_str = format_minus_coord('x', xB)
        bc_y_str = format_minus_coord('y', yB)
        bc_z_str = format_minus_coord('z', zB)

        # 5. Khởi tạo nội dung câu hỏi và lời giải
        noidungcauhoi = (f"Trong không gian chọn hệ trục tọa độ cho trước, đơn vị đo lấy kilômét, ra đa phát hiện một "
                         f"máy bay di chuyển với vận tốc và hướng không đổi từ điểm $A({xA}; {yA}; {zA})$ đến điểm "
                         f"$B({xB}; {yB}; {zB})$ trong {t} phút. Nếu máy bay tiếp tục giữ nguyên vận tốc và hướng bay thì tọa "
                         f"độ của máy bay sau {t} phút tiếp theo là $(a;b;c)$, giá trị $T = {expr_str}$ bằng bao nhiêu?")

        # TikZ mô phỏng vectơ theo hình ảnh lời giải
        tikz_code = """\\begin{center}
    \\begin{tikzpicture}[>=stealth, scale=1]
        \\filldraw[red] (0,0) circle (1.5pt);
        \\filldraw[red] (3,0) circle (1.5pt);
        \\filldraw[red] (6,0) circle (1.5pt);
        \\draw[->, thick, blue] (0,0) -- (2.9,0);
        \\draw[->, thick, blue] (3,0) -- (5.9,0);
        \\node[below] at (0,0) {$A$};
        \\node[below] at (3,0) {$B$};
        \\node[below] at (6,0) {$C$};
    \\end{tikzpicture}
    \\end{center}"""

        loigiai = (f"{tikz_code}\n"
                   f"Gọi $C(x; y; z)$ là tọa độ của máy bay sau {t} phút tiếp theo.\\\\\n"
                   f"Ta có: $\\overrightarrow{{AB}} = ({vx}; {vy}; {vz}); \\overrightarrow{{BC}} = ({bc_x_str}; {bc_y_str}; {bc_z_str})$.\\\\\n"
                   f"Vì máy bay giữ nguyên hướng bay nên $\\overrightarrow{{AB}}$ và $\\overrightarrow{{BC}}$ cùng hướng.\\\\\n"
                   f"Do máy bay tiếp tục giữ nguyên vận tốc và thời gian bay từ $A \\to B$ bằng thời gian bay từ $B \\to C$ nên $\\overrightarrow{{AB}} = \\overrightarrow{{BC}}$.\\\\\n"
                   f"Suy ra $\\overrightarrow{{AB}} = \\overrightarrow{{BC}} \\Leftrightarrow \\begin{{cases}} {vx} = {bc_x_str} \\\\ {vy} = {bc_y_str} \\\\ {vz} = {bc_z_str} \\end{{cases}} "
                   f"\\Leftrightarrow \\begin{{cases}} x = {xC} \\\\ y = {yC} \\\\ z = {zC} \\end{{cases}} \\Rightarrow C({xC}; {yC}; {zC})$.\\\\\n"
                   f"Tọa độ của máy bay sau {t} phút tiếp theo là $C({xC}; {yC}; {zC}) \\longrightarrow a = {xC}; b = {yC}; c = {zC}$.\\\\\n"
                   f"Vậy $T = {sub_str} = {kq}$.")
        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content

