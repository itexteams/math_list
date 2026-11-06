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


def bt_dang21_p4_b3_c4_ds10(self):
            # Khai báo biến
            # Khởi tạo biến
            x = symbols('x')

            # B1: Random thông số a, b và DẤU của bất phương trình
            a = random.randint(2, 5)
            b = random.randint(1, 4)
            if a == b: a += 1

            list_dau = [
                (r'\geq', 'ge', True), 
                (r'\leq', 'le', True), 
                (r'>', 'gt', False), 
                (r'<', 'lt', False)
            ]
            dau_tex, dau_name, has_equal = random.choice(list_dau)

            # Các nghiệm
            nghiem_mau1 = -b
            nghiem_mau2 = a
            nghiem_tu = Rational(a - b, 2)
            roots = sorted([nghiem_mau1, nghiem_tu, nghiem_mau2])

            tu_rut_gon = simplify((x - a)**2 - (x + b)**2) 

            # B2: Hàm tạo khoảng với \left \right
            def get_interval(low, high, include_low, include_high):
                low_tex = latex(low) if low != float('-inf') else r'-\infty'
                high_tex = latex(high) if high != float('inf') else r'+\infty'
                left_bracket = r'\left[' if include_low else r'\left('
                right_bracket = r'\right]' if include_high else r'\right)'
                return f"{left_bracket} {low_tex}; {high_tex} {right_bracket}"

            if dau_name in ['ge', 'gt']:
                int1 = f"\\left( -\\infty; {latex(roots[0])} \\right)"
                int2 = get_interval(roots[1], roots[2], has_equal, False)
                tap_nghiem = f"{int1} \\cup {int2}"
            else:
                int1 = get_interval(roots[0], roots[1], False, has_equal)
                int2 = f"\\left( {latex(roots[2])}; +\\infty \\right)"
                tap_nghiem = f"{int1} \\cup {int2}"

            # B3: Nội dung câu hỏi
            noidungcauhoi = r'Giải bất phương trình $\frac{x-%s}{x+%s} %s \frac{x+%s}{x-%s}$.' % (a, b, dau_tex, b, a)

            da_dung = r'\True $%s$' % tap_nghiem
            da_s1 = r'$%s$' % tap_nghiem.replace(r'\left[', r'\left(').replace(r'\right]', r'\right)') 
            da_s2 = r'$\left( -\infty; %s \right]$' % latex(nghiem_tu)
            da_s3 = r'$\left( %s; +\infty \right)$' % latex(nghiem_mau2)

            list_da = [da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_da)

            # B4: Lời giải với bảng xét dấu CÓ KHUNG
            loigiai = r'''Điều kiện xác định: $x \neq %s$ và $x \neq %s$. \\
            Bất phương trình tương đương:
            $$\frac{x-%s}{x+%s} - \frac{x+%s}{x-%s} %s 0 \Leftrightarrow \frac{%s}{(x+%s)(x-%s)} %s 0$$
            Xét dấu các thành phần:
            \begin{itemize}
                \item Tử thức: $%s = 0 \Leftrightarrow x = %s$.
                \item Mẫu thức: $(x+%s)(x-%s) = 0 \Leftrightarrow x = %s$ hoặc $x = %s$.
            \end{itemize}
            Bảng xét dấu:
            \begin{center}
            \renewcommand{\arraystretch}{1.2}
            \begin{tabular}{|c|cccccccccc|}
            \hline
            $x$ & $-\infty$ & & $%s$ & & $%s$ & & $%s$ & & $+\infty$ \\ \hline
            Tử thức & & $+$ & | & $+$ & $0$ & $-$ & | & $-$ & \\ \hline
            Mẫu thức & & $+$ & $0$ & $-$ & | & $-$ & $0$ & $+$ & \\ \hline
            Vế trái & & $+$ & || & $-$ & $0$ & $+$ & || & $-$ & \\ \hline
            \end{tabular}
            \end{center}
            Dựa vào bảng xét dấu và chiều của bất phương trình ($%s$), ta có tập nghiệm:
            $S = %s$.''' % (latex(nghiem_mau1), latex(nghiem_mau2), a, b, b, a, dau_tex, 
                   latex(tu_rut_gon), b, a, dau_tex,
                   latex(tu_rut_gon), latex(nghiem_tu), b, a, latex(nghiem_mau1), latex(nghiem_mau2),
                   latex(roots[0]), latex(roots[1]), latex(roots[2]),
                   dau_tex, tap_nghiem)

            # B5: Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

