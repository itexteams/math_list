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


def bt_dang12_p4_b1_c1_hh12(self):
            # Khai báo biến
            def round_SA(a): 
                # Chuyển số về float để xử lý
                val = float(a)
                if val == int(val):
                    return "", str(int(val))

                str_val = f"{val:.5f}".rstrip('0')
                integer_part = str(int(val))
                decimal_part = str_val.split('.')[1] if '.' in str_val else ""

                if len(integer_part) >= 3:
                    number = Decimal(str(val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    circle = "(làm tròn đến hàng đơn vị)."
                elif len(integer_part) == 2:
                    number = Decimal(str(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    circle = "(làm tròn đến hàng phần mười)."
                else:
                    number = Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    circle = "(làm tròn đến hàng phần trăm)."

                return circle, str(number).replace('.', ',')

            # ============ XÂY DỰNG BÀI TOÁN ===============================
            # Sinh ngẫu nhiên đối số
            khoi_luong = random.randint(15, 35) # Cân nặng em bé hợp lý hơn
            dai_cau_truot = random.randint(25, 50) / 10 # 2.5m đến 5.0m
            goc_nghieng = random.randint(5, 9) * 5 # 25, 30, 35, 40, 45 độ
            g = 9.8

            # Tính toán
            kq_a = khoi_luong * g
            # Công A = P * d * cos(90 - alpha) = P * d * sin(alpha)
            kq_b = float(kq_a) * float(dai_cau_truot) * math.sin(math.radians(goc_nghieng))

            # Định dạng LaTeX
            kq_a_latex = f"{kq_a:.1f}".replace('.', '{,}')
            dai_cau_truot_latex = f"{dai_cau_truot}".replace('.', '{,}')
            g_latex = "9{,}8"

            tikz_code = f"""\\begin{{tikzpicture}}[scale=0.8, font=\\footnotesize]
                    \\coordinate (B) at (0,0);
                    \\coordinate (H) at (5,0);
                    \\coordinate (A) at (5,{{5*tan({goc_nghieng})}});
                    \\draw[thick] (B) -- (H) -- (A) -- cycle;
                    \\draw (4.7,0) -- (4.7,0.3) -- (5,0.3);
                    \\draw[red, thick, ->] ($(B)!0.6!(A)$) -- ++(0,-1.5) node[right] {{$\\vec{{P}}$}};
                    \\draw[blue, thick, ->] ($(B)!0.6!(A)$) -- ($(B)!0.3!(A)$);
                    \\node at ($(B)!0.45!(A) + (-0.3,0.3)$) {{$\\vec{{d}}$}};
                    \\draw (1,0) arc (0:{goc_nghieng}:1);
                    \\node at ({goc_nghieng/2}:1.3) {{${goc_nghieng}^\\circ$}};
                    \\path (A) -- (B) node[sloped, pos=0.5, below] {{${dai_cau_truot_latex}$ m}};
                \\end{{tikzpicture}}"""

            de_bai = f"""\\immini{{ Một em nhỏ nặng $m = {khoi_luong}$ kg trượt từ đỉnh xuống hết một cầu trượt dài $d = {dai_cau_truot_latex}$ m. 
                    Biết rằng cầu trượt nghiêng một góc ${goc_nghieng}^\\circ$ so với phương nằm ngang. Lấy gia tốc rơi tự do $g = {g_latex}$ m/s$^2$.
                    }}{{{tikz_code}}}"""

            ds_abcd = [
                (f"Tính độ lớn của trọng lực $\\vec{{P}}$ tác dụng lên em nhỏ.",
                 f"""Độ lớn trọng lực: $P = m \\cdot g = {khoi_luong} \\cdot {g_latex} = {kq_a_latex}$ (N)."""),

                (f"Tính công $A$ sinh bởi trọng lực $\\vec{{P}}$ khi em nhỏ trượt hết chiều dài cầu trượt {round_SA(kq_b)[0]}",
                 f"""Góc hợp bởi trọng lực $\\vec{{P}}$ (thẳng đứng) và hướng dịch chuyển (dọc mặt nghiêng) là $\\theta = 90^\\circ - {goc_nghieng}^\\circ = {90-goc_nghieng}^\\circ$. \\\\
                    Công của trọng lực: $A = P \\cdot d \\cdot \\cos \\theta = {kq_a_latex} \\cdot {dai_cau_truot_latex} \\cdot \\cos {90-goc_nghieng}^\\circ \\approx {round_SA(kq_b)[1]}$ (J).""")
            ]

            # =========== PHẦN XUẤT CODE LATEX ==============
            so_cot = '1'
            hoi_item = f"\n\\begin{{listEX}}[{so_cot}]\n"
            for j in range(len(ds_abcd)):
                hoi_item += f"\\item {ds_abcd[j][0]} \n"
            hoi_item += f"\\end{{listEX}}\n"

            giai_item = f"\n\\begin{{listEX}}[1]\n"
            for j in range(len(ds_abcd)):
                giai_item += f"\\item {ds_abcd[j][1]}\n"
            giai_item += f"\\end{{listEX}}\n"

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + de_bai + hoi_item +
                '\n\\loigiai{ \n'
                + giai_item + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

