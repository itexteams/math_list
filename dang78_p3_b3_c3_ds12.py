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


def bt_dang78_p3_b3_c3_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Điểm giao với Ox: x = x0 = 2
        x0 = 2
        h1 = random.choice([2, 4, 6])
        m1 = Rational(h1, x0)  # Hệ số góc của nhánh 1: y = -m1*x + h1

        # Nhánh 2: đi qua (x0, 0) và (x_end, h2)
        x_end = 6
        h2 = random.choice([1, 2, 3])
        m2 = Rational(h2, x_end - x0)
        c2 = -m2 * x0

        # Tính diện tích
        S1 = Rational(1, 2) * x0 * h1
        S2 = Rational(1, 2) * (x_end - x0) * h2
        S_total = S1 + S2

        # Chuỗi hàm số
        str_f1 = latex(-m1*x + h1)
        str_f2 = latex(m2*x + c2)

        number = Decimal(float(S_total))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        if S_total == int(S_total):
            kq_str = str(int(S_total))
        else:
            kq_str = str(kq).replace('.', ',')

        # Điểm kéo dài ngoài biên cho đồ thị TikZ
        y_start = float(m1 * Rational(4, 10) + h1)
        y_end = float(m2 * Rational(68, 10) + c2)

        # Vẽ hình TikZ 100% nét đen 1pt, gạch sọc theo mẫu
        # Đã thay toàn bộ các dấu % chú thích thành %% để tránh lỗi định dạng chuỗi
        tikz_code = ('''\\begin{center}
    \\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\usetikzlibrary{patterns}
        \\draw[->, line width=1pt] (-0.8,0) -- (7.5,0) node[above] {$x$};
        \\draw[->, line width=1pt] (0,-0.8) -- (0,5.2) node[right] {$y$};
        \\fill (0,0) circle (1pt) node[below left] {$0$};
        \\fill[pattern=north east lines, pattern color=black] (0,0) -- (0,%d) -- (%d,0) -- cycle;
        \\fill[pattern=north east lines, pattern color=black] (%d,0) -- (%d,%d) -- (%d,0) -- cycle;
        \\draw[line width=1pt] (-0.4, %.2f) -- (%d, 0);
        \\draw[line width=1pt] (%d, 0) -- (6.8, %.2f);
        \\draw[line width=1pt] (0,0) -- (0,%d);
        \\draw[line width=1pt] (%d,0) -- (%d,%d);
        \\foreach \\i in {1, 2, 3, 4, 5, 6, 7} {
            \\draw[line width=1pt] (\\i, 2pt) -- (\\i, -2pt) node[below] {$\\i$}; }
        \\foreach \\j in {1, 2, 3, 4} {
            \\draw[line width=1pt] (2pt, \\j) -- (-2pt, \\j) node[left] {$\\j$}; }
    \\end{tikzpicture}
    \\end{center}''' % (h1, x0, x0, x_end, h2, x_end,
                       y_start, x0,
                       x0, y_end,
                       h1, x_end, x_end, h2))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho đồ thị hàm số $f(x) = \\begin{cases} %s & (x \\le %d) \\\\ %s & (x > %d) \\end{cases}$. Hình phẳng $S$ (phần gạch sọc) dưới đây có diện tích bằng bao nhiêu?
    %s''' % (str_f1, x0, str_f2, x0, tikz_code))

        # Nội dung lời giải
        loigiai = ('''Dựa vào đồ thị, phần hình phẳng được gạch sọc gồm hai tam giác vuông: \\\\
                   - Tam giác vuông thứ nhất có các đỉnh $(0; 0)$, $(0; %d)$, $(%d; 0)$, có diện tích là: \\\\
                   $S_1 = \\frac{1}{2} \\cdot %d \\cdot %d = %s$. \\\\
                   - Tam giác vuông thứ hai có các đỉnh $(%d; 0)$, $(%d; 0)$, $(%d; %d)$, có diện tích là: \\\\
                   $S_2 = \\frac{1}{2} \\cdot (%d - %d) \\cdot %d = %s$. \\\\
                   Vậy tổng diện tích hình phẳng cần tìm là: \\\\
                   $S = S_1 + S_2 = %s + %s = %s$.'''
                   % (h1, x0,
                      x0, h1, latex(S1),
                      x0, x_end, x_end, h2,
                      x_end, x0, h2, latex(S2),
                      latex(S1), latex(S2), kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n' +
               '\\end{minipage}\n\n')
    return content

