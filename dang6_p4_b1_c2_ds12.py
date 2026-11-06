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


def bt_dang6_p4_b1_c2_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Các bộ tần số đảm bảo Q1 nằm ở nhóm 2 và Q3 nằm ở nhóm 6 (để giữ nguyên cấu trúc bài giải)
        combos = [
            [2, 3, 1, 1, 1, 2, 2],
            [1, 3, 2, 1, 1, 3, 1],
            [2, 2, 1, 2, 1, 2, 2],
            [1, 2, 2, 2, 1, 2, 2]
        ]
        combo = random.choice(combos)
        f1, f2, f3, f4, f5, f6, f7 = combo

        # Tính tần số tích luỹ
        cf1 = f1
        cf2 = f1 + f2
        cf3 = cf2 + f3
        cf4 = cf3 + f4
        cf5 = cf4 + f5
        cf6 = cf5 + f6
        cf7 = cf6 + f7

        # Xây dựng mảng phân bổ các nhóm vào 12 tháng để vẽ biểu đồ hình chuông
        bins = []
        for k, f in enumerate(combo):
            bins.extend([k+1]*f)
        bins.sort()

        # Phân bổ lượng mưa tăng dần vào giữa năm
        m_bins = [0]*12
        m_bins[0] = bins[0]
        m_bins[11] = bins[1]
        m_bins[1] = bins[2]
        m_bins[10] = bins[3]
        m_bins[2] = bins[4]
        m_bins[9] = bins[5]
        m_bins[3] = bins[6]
        m_bins[8] = bins[7]
        m_bins[4] = bins[8]
        m_bins[7] = bins[9]
        m_bins[5] = bins[10]
        m_bins[6] = bins[11]

        # Random chiều cao cột của từng tháng (nằm trọn trong nhóm tương ứng)
        heights = []
        for i in range(12):
            b = m_bins[i]
            low = (b-1)*50
            high = b*50
            # Lấy giá trị random an toàn cách mép 5 đơn vị để học sinh dễ nhìn biểu đồ
            val = random.randint(low + 5, high - 5) if b > 1 else random.randint(5, high - 5)
            heights.append(val)

        # Tạo mã TikZ cho biểu đồ
        tikz_bars = ""
        romans = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
        for i in range(12):
            h_units = heights[i] / 100.0
            x_start = i * 0.5
            x_end = (i + 1) * 0.5
            x_mid = i * 0.5 + 0.25
            tikz_bars += f"    \\fill[cyan!60, draw=black, thin] ({x_start},0) rectangle ({x_end}, {h_units}); \\node[below] at ({x_mid},0) {{{romans[i]}}};\n"

        # Tính toán Q1, Q3, Delta
        Q1_exact = 50 + (3 - f1) / f2 * 50
        Q1_rounded = int(Decimal(Q1_exact).to_integral_value(ROUND_HALF_UP))

        Q3_exact = 250 + (9 - 8) / f6 * 50
        Q3_rounded = int(Decimal(Q3_exact).to_integral_value(ROUND_HALF_UP))

        Delta_Q = Q3_rounded - Q1_rounded

        # Xác định dấu bằng hay xấp xỉ
        sign_Q1 = "=" if abs(Q1_exact - Q1_rounded) < 1e-9 else "\\approx"
        sign_Q3 = "=" if abs(Q3_exact - Q3_rounded) < 1e-9 else "\\approx"

        # Nội dung câu hỏi
        noidungcauhoi = (
            'Hình dưới là biểu đồ biểu diễn lượng mưa trung bình của các tháng trong năm ở thành phố A.\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[>=stealth, scale=1, font=\\small]\n'
            '\\draw[cyan!30, thin, step=0.5] (0,0) grid (6.5,3.9);\n'
            '\\draw[->] (0,0) -- (6.8,0) node[below] {Tháng};\n'
            '\\draw[->] (0,0) -- (0,4) node[left] {mm};\n'
            '\\foreach \\y in {50, 100, 150, 200, 250, 300, 350} {\n'
            '    \\draw (0,\\y/100) -- (-0.1,\\y/100) node[left] {\\y};\n'
            '}\n'
            '\\draw (0,0) -- (-0.1,0) node[left] {0};\n'
            f'{tikz_bars}'
            '\\node[below, font=\\itshape\\scriptsize] at (3.25, -0.6) {Hình 3.2. Biểu đồ lượng mưa ở thành phố A};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
            'a) Lập bảng số liệu ghép nhóm về lượng mưa của thành phố $A$, với độ dài các nhóm là 50 và đầu mút phải của nhóm cuối cùng là 350. \\'
            'b) Xác định khoảng tứ phân vị của mẫu số liệu (làm tròn kết quả đến hàng đơn vị). Nêu ý nghĩa của kết quả tìm được.'
        )

        # Nội dung lời giải
        loigiai = (
            'a) Bảng số liệu về lượng mưa của thành phố A:\n'
            '\\begin{center}\n'
            '\\begin{tabular}{|c|c|c|}\n'
            '\\hline\n'
            '\\textbf{Lượng mưa (mm)} & \\textbf{Tần số} & \\textbf{Tần số tích luỹ} \\\\ \n'
            '\\hline\n'
            f'$[0;50)$ & {f1} & {cf1} \\\\ \n'
            '\\hline\n'
            f'$[50;100)$ & {f2} & {cf2} \\\\ \n'
            '\\hline\n'
            f'$[100;150)$ & {f3} & {cf3} \\\\ \n'
            '\\hline\n'
            f'$[150;200)$ & {f4} & {cf4} \\\\ \n'
            '\\hline\n'
            f'$[200;250)$ & {f5} & {cf5} \\\\ \n'
            '\\hline\n'
            f'$[250;300)$ & {f6} & {cf6} \\\\ \n'
            '\\hline\n'
            f'$[300;350)$ & {f7} & {cf7} \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}'
            'b) $n = 12$ nên $\\frac{n}{4} = 3; \\frac{3n}{4} = 9$.\\\\'
            f'Nhóm chứa $Q_1$ là $[50;100)$. $Q_1 = 50 + \\frac{{3-{f1}}}{{{f2}}} \\cdot 50 {sign_Q1} {Q1_rounded}$. \\\\'
            f'Nhóm chứa $Q_3$ là $[250;300)$. $Q_3 = 250 + \\frac{{9-8}}{{{f6}}} \\cdot 50 {sign_Q3} {Q3_rounded}$. Vậy $\\Delta_Q = {Q3_rounded} - {Q1_rounded} = {Delta_Q}$. \\\\'
            f'Kết quả tìm được cho thấy: Hằng năm, ở thành phố $A$ có 3 tháng có lượng mưa trung bình không vượt quá ${Q1_rounded}mm$ và 3 tháng có lượng mưa trung bình ít nhất là ${Q3_rounded}mm$. Trong 6 tháng còn lại, lượng mưa trung bình đạt từ ${Q1_rounded}mm$ đến ${Q3_rounded}mm$ và như vậy là lượng mưa của 6 tháng này có thể chênh lệch nhau đến ${Delta_Q}mm$.'
        )

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

