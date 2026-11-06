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


def bt_dang22_p3_b2_c2_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tọa độ nguyên cho C và D
                x_c = random.choice([1, 2])
                y_d = random.choice([-1])

                # Phương trình theo đoạn chắn là x/x_c + y/y_d = 1
                # Do đó a = 1/x_c và b = 1/y_d
                a = Rational(1, x_c)
                b = Rational(1, y_d)

                # Tính kết quả a+b ở dạng phân số (latex)
                kq = latex(a + b)
                h1=1/x_c+1/y_d
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.', ',')

                # Hàm xử lý dấu thông minh để hiển thị hệ số trong lời giải
                def format_eq(coef_a, coef_b):
                    # Xử lý a
                    if coef_a == 1: term_a = "x"
                    elif coef_a == -1: term_a = "-x"
                    else: term_a = f"{latex(coef_a)}x"

                    # Xử lý b
                    if coef_b == 1: term_b = "+y"
                    elif coef_b == -1: term_b = "-y"
                    elif coef_b > 0: term_b = f"+{latex(coef_b)}y"
                    else: term_b = f"{latex(coef_b)}y" # Số âm đã tự có dấu trừ

                    return f"{term_a}{term_b}"

                eq_str = format_eq(a, b)

                # Xử lý tránh ghi đè số -1 trên trục y nếu y_d ngẫu nhiên trúng -1
                node_num_d = f"node[left] {{${y_d}$}}" if y_d != -1 else ""

                # TikZ code - Tính 2 điểm cho đường thẳng d2 trong TikZ
                # Rút y từ pt: x/x_c + y/y_d = 1 => y = (1 - x/x_c) * y_d
                y1_tikz = (1 - (-3)/x_c) * y_d
                y2_tikz = (1 - (3)/x_c) * y_d

                tikz_code = f"""\\begin{{center}}
                \\begin{{tikzpicture}}[>=stealth, scale=1.2, line width=1pt]
                \\clip (-3,-2) rectangle (3,2);
                \\fill[pattern=north east lines, pattern color=black] (-3,-2) rectangle (3,2);
                \\fill[white] (-3, 2) -- (2, -3) -- (3, -3) -- (3, 2) -- cycle; 
                \\fill[pattern=north east lines, pattern color=black] (-3, {y1_tikz}) -- (3, {y2_tikz}) -- (3, 3) -- (-3, 3) -- cycle; 
                \\draw[->] (-3,0) -- (3,0) node[below] {{$x$}};
                \\draw[->] (0,-2) -- (0,2) node[left] {{$y$}};
                \\node at (0,0) [below left] {{$O$}};
                \\draw[black] (-3, 2) -- (2, -3);
                \\draw[black] (-3, {y1_tikz}) -- (3, {y2_tikz});
                \\coordinate (A) at (-1,0);
                \\coordinate (B) at (0,-1);
                \\coordinate (C) at ({x_c},0);
                \\coordinate (D) at (0,{y_d});
                \\fill (0,0) circle (1pt);
                \\fill (A) circle (1pt) node[above left] {{$-1$}};
                \\fill (B) circle (1pt) node[below left] {{$-1$}};
                \\fill (C) circle (1pt) node[above right] {{${x_c}$}};
                \\fill (D) circle (1pt) node[below left] {{${y_d}$}};
                \\end{{tikzpicture}}
                \\end{{center}}"""

                # Câu hỏi (đã sửa bất phương trình 1 thành dạng chữ ax+by)
                noidungcauhoi = (f"Phần không tô đậm trong hình vẽ dưới đây biểu diễn tập nghiệm của hệ bất phương trình "
                                 f"$\\begin{{cases}} ax+by-1<0 \\\\ x+y+1>0 \\end{{cases}}$. Tính $a+b$."
                                 f"{tikz_code}")

                # Lời giải chi tiết
                loigiai = (f"Đường thẳng đi qua hai điểm $A(-1; 0), B(0; -1)$ là $(\\Delta_1): x + y + 1 = 0$.\\\\ \n"
                           f"Đường thẳng đi qua hai điểm $C({x_c}; 0), D(0; {y_d})$ là $(\\Delta_2): \\frac{{x}}{{{x_c}}} + \\frac{{y}}{{{y_d}}} = 1 \\Leftrightarrow {eq_str}-1=0$.\\\\ \n"
                           f"Dựa vào miền nghiệm của hệ bất phương trình, ta suy ra $a = {latex(a)}; b = {latex(b)} \\Rightarrow a + b = {kq}$.")

            dapan='\\shortans[0]{$%s$}\n'%(kqz)
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+dapan+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

