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


def bt_dang36_p4_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            a = symbols('a')

            # B3-Suy nghĩ tìm cách random bài toán
            # Random hệ số của AB, AD và góc tạo bởi (SBC) với đáy
            n1 = random.choice([1, 2, 3]) # Hệ số của a cho cạnh AB
            n2 = random.choice([2, 3, 5, 6]) # Giá trị trong căn cho cạnh AD (a*sqrt(n2))
            goc_val = random.choice([30, 45, 60]) # Góc tạo bởi mặt phẳng (SBC) và đáy

            # Tính toán các đại lượng
            # Diện tích đáy ABCD
            S_day = n1 * a * a * sqrt(n2)

            # Chiều cao SA: SA = AB * tan(goc)
            tan_goc = tan(goc_val * pi / 180)
            SA = n1 * a * tan_goc

            # Thể tích V = 1/3 * S_day * SA
            V_exact = Rational(1, 3) * S_day * SA

            # Tạo các đáp án (B4-Điều chỉnh phương án sai)
            def generate_choices(correct_val):
                choices = [correct_val]
                multipliers = [Rational(1, 3), 3, sqrt(3), Rational(1, 2), 2]
                while len(choices) < 4:
                    m = random.choice(multipliers)
                    wrong = correct_val * m
                    if wrong not in choices:
                        choices.append(wrong)
                random.shuffle(choices)
                return choices

            list_choices = generate_choices(V_exact)

            # Chuẩn bị nội dung LaTeX
            ab_str = latex(n1 * a) if n1 != 1 else "a"
            ad_str = "a\\sqrt{" + str(n2) + "}"
            goc_str = str(goc_val) + "^\\circ"
            v_correct_str = latex(V_exact)

            # B2-Viết lại bài toán và lời giải theo mẫu code python
            noidungcauhoi = (
                "Cho khối chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật, $AB = " + ab_str + "$, "
                "$AD = " + ad_str + "$, $SA$ vuông góc với mặt phẳng đáy và mặt phẳng $(SBC)$ "
                "tạo với đáy một góc $" + goc_str + "$. Tính thể tích khối chóp $S.ABCD$."
            )

            # Tạo TikZ code (Hình vẽ giống 100% ảnh, nét 1pt)
            tikz_code = (
                "\\begin{center} \\begin{tikzpicture}[scale=0.8, line join=round, line cap=round, line width=1pt]\n"
                "\\coordinate (A) at (0,0);\n"
                "\\coordinate (D) at (-1.5,-1.5);\n"
                "\\coordinate (B) at (4,0);\n"
                "\\coordinate (C) at (2.5,-1.5);\n"
                "\\coordinate (S) at (0,4);\n"
                "\\draw (S)--(C)--(D)--(S)--(B)--(C);\n"
                "\\draw [dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (D)--(B);\n"
                "\\node [left] at (A) {$A$};\n"
                "\\node [below left] at (D) {$D$};\n"
                "\\node [right] at (B) {$B$};\n"
                "\\node [below right] at (C) {$C$};\n"
                "\\node [above] at (S) {$S$};\n"
                "\\node [left] at (-0.75, -0.75) {$" + ad_str + "$};\n"
                "\\node [above] at (2, 0) {$" + ab_str + "$};\n"
                "\\draw (0,0.3)--(0.3,0.3)--(0.3,0);\n" # Góc vuông tại A
                "\\draw (3.7,0) arc (180:210:0.5);\n" # Ký hiệu góc 60 tại B
                "\\node at (3.3, 0.3) {$" + goc_str + "$};\n"
                "\\end{tikzpicture} \\end{center}"
            )

            # Lời giải chi tiết
            loigiai = (
                "Ta có $S_{ABCD} = AB \\cdot AD = " + ab_str + " \\cdot " + ad_str + " = " + latex(S_day) + "$.\\\\\n"
                "Vì $\\begin{cases} (SBC) \\cap (ABCD) = BC \\\\ BC \\perp AB \\subset (ABCD) \\\\ BC \\perp SA \\text{ (do } SA \\perp \\text{ đáy)} \\end{cases} "
                "\\Rightarrow BC \\perp (SAB) \\Rightarrow BC \\perp SB$.\\\\\n"
                "Suy ra góc giữa $(SBC)$ và đáy là $\\left( SB, AB \\right) = \\widehat{SBA} = " + goc_str + "$.\\\\\n"
                "Xét tam giác vuông $SAB$ có: $\\tan " + goc_str + " = \\frac{SA}{AB} \\Rightarrow SA = AB \\cdot \\tan " + goc_str + " = " + latex(SA) + "$.\\\\\n"
                "Vậy $V_{S.ABCD} = \\frac{1}{3} S_{ABCD} \\cdot SA = \\frac{1}{3} \\cdot " + latex(S_day) + " \\cdot " + latex(SA) + " = " + v_correct_str + "$."
            )

            # Xuất câu trắc nghiệm (Phần content không dùng tiền tố r, dùng escaped backslash)
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n"
                + str(noidungcauhoi) + "\n"   
                "\\loigiai{" + tikz_code+ str(loigiai) + "}\n"
                "\\end{ex}\n \\end{minipage} \n\n")
            return content

