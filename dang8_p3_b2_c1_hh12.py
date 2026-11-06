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


def bt_dang8_p3_b2_c1_hh12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # 1. Random cạnh đáy (d = 2k) và chiều cao SA (h)
        k = random.randint(1, 4)
        d = 2 * k
        h = random.randint(1, 6)

        # 2. Random hệ số cho biểu thức T = m*a + n*sqrt(3)*b + p*c
        m = random.choice([1, 2, 3]) # Giữ hệ số đầu dương
        n = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        p = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])

        # Các giá trị tọa độ
        a = 0
        c_val = h
        # Kết quả tính toán (đã triệt tiêu căn 3)
        kq = 3 * n * k + p * h

        # --- CÁC HÀM XỬ LÝ CHUỖI ĐỂ TRÁNH DẤU + - LỘN XỘN ---
        def format_term(coef, var, is_first=False):
            if coef == 0: return ""
            abs_c = abs(coef)
            c_str = "" if abs_c == 1 else str(abs_c)
            if is_first:
                return f"-{c_str}{var}" if coef < 0 else f"{c_str}{var}"
            else:
                return f" - {c_str}{var}" if coef < 0 else f" + {c_str}{var}"

        expr_m = format_term(m, 'a', True)

        # Xử lý riêng cho cụm chứa căn 3
        if n == 1:
            expr_n = " + \\sqrt{3}b"
        elif n == -1:
            expr_n = " - \\sqrt{3}b"
        elif n > 0:
            expr_n = f" + {n}\\sqrt{{3}}b"
        else:
            expr_n = f" - {abs(n)}\\sqrt{{3}}b"

        expr_p = format_term(p, 'c', False)

        # Ghép và dọn dẹp các dấu thừa
        expr_T = f"{expr_m}{expr_n}{expr_p}".replace("+ -", "- ").replace("- -", "+ ")
        if expr_T.startswith(" + "):
            expr_T = expr_T[3:]

        # --- XỬ LÝ CHUỖI LỜI GIẢI ---
        oa_str = f"\\frac{{{d}\\sqrt{{3}}}}{{2}} = "
        if k == 1:
            oa_str += "\\sqrt{3}"
            b_str_val = "\\sqrt{3}"
        else:
            oa_str += f"{k}\\sqrt{{3}}"
            b_str_val = f"{k}\\sqrt{{3}}"

        # Xử lý chuỗi thế số
        sub_m = "0" if m == 1 else f"{m}\\cdot 0"

        if n == 1:
            sub_n = f"\\sqrt{{3}} \\cdot {b_str_val}"
        elif n == -1:
            sub_n = f"-\\sqrt{{3}} \\cdot {b_str_val}"
        else:
            sub_n = f"{n}\\sqrt{{3}} \\cdot {b_str_val}"

        sub_p = f"{p}\\cdot {c_val}" if abs(p) != 1 else (f"{c_val}" if p == 1 else f"-{c_val}")

        sub_str = f"{sub_m} + {sub_n} + {sub_p}"
        # Ép buộc xử lý dấu thay thế triệt để
        sub_str = sub_str.replace("+ -", "- ").replace("- -", "+ ").replace("+ 0", "").strip()

        # --- TIKZ CODE MÔ PHỎNG HÌNH VẼ ĐÃ FIX NÉT ĐỨT/LIỀN ---
        tikz_code = """\\begin{center}
    \\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (O) at (0,0);
        \\coordinate (C) at (3.5, 0.8);
        \\coordinate (B) at (-3.5, -0.8);
        \\coordinate (A) at (-1.5, 0.5);
        \\coordinate (S) at (-1.5, 4);
        \\coordinate (H) at (0, 3.5);
        \\draw[->] (C) -- (4.5, 1.03) node[above] {$x$};
        \\draw[dashed] (O) -- (A);
        \\draw[->] (A) -- (-2.5, 0.83) node[below] {$y$};
        \\draw[dashed] (O) -- (H);
        \\draw[->] (0, 1.8) -- (0, 5) node[right] {$z$};
        \\draw[dashed] (A) -- (C);
        \\draw (S) -- (H);
        \\draw[thick] (S) -- (B) -- (C) -- cycle; % Mặt bên phải và cạnh đáy BC
        \\draw[dashed] (S) -- (A) -- (B); % Mặt bên trái
        \\draw (0, 0.25) -- (-0.2, 0.3) -- (-0.2, 0.05); % Tại O
        \\draw (-1.5, 0.8) -- (-1.3, 0.8) -- (-1.3, 0.5); % Tại A
        \\draw (0, 3.25) -- (-0.2, 3.2) -- (-0.2, 3.45); % Tại H
        \\node[below right] at (O) {$O$};
        \\node[below] at (C) {$C$};
        \\node[below] at (B) {$B$};
        \\node[left] at (A) {$A$};
        \\node[above] at (S) {$S$};
        \\node[right] at (H) {$H$};
    \\end{tikzpicture}
    \\end{center}"""

        # Đề bài
        noidungcauhoi = (f"Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh bằng ${d}$, $SA$ vuông góc với đáy và "
                         f"$SA$ bằng ${h}$. Thiết lập hệ toạ độ như hình vẽ.\n"
                         f"{tikz_code}\n"
                         f"Biết toạ độ đỉnh $S$ là $(a;b;c)$. Giá trị $T = {expr_T}$ bằng bao nhiêu?"
                         )

        # Nội dung lời giải
        loigiai = (f"Ta có: $OA = {oa_str} \\longrightarrow S(0; {b_str_val}; {h}) \\longrightarrow a = 0; b = {b_str_val}; c = {h}$. \\\\\n"
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

