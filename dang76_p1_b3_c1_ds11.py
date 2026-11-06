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


def bt_dang76_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random chọn giữa hàm số y = tan x (h = 1) và y = tan 2x (h = 2)
                h = random.choice([1, 2])

                if h == 1:
                    ham_str = 'y = \\tan x'
                    pa_A = 'Hàm số $y = \\tan x$ luôn luôn tăng'
                    pa_B = '\\True Hàm số $y = \\tan x$ luôn luôn tăng trên từng khoảng xác định'
                    pa_C = 'Hàm số $y = \\tan x$ tăng trong các khoảng $(\\pi + k2\\pi; 2\\pi + k2\\pi), k \\in \\mathbb{Z}$'
                    pa_D = 'Hàm số $y = \\tan x$ tăng trong các khoảng $(k2\\pi; \\pi + k2\\pi), k \\in \\mathbb{Z}$'

                    khoang_dung = '$\\left( -\\frac{\\pi}{2} + k\\pi; \\frac{\\pi}{2} + k\\pi \\right), k \\in \\mathbb{Z}$'

                    # Đồ thị TikZ cho hàm số y = tan x
                    tikz_graph = (
                        "\\begin{center} \\begin{tikzpicture}[scale=0.8, line width=1pt, >=latex]\n"
                        "\\draw[->] (-4.5,0) -- (4.5,0) node[below] {$x$};\n"
                        "\\draw[->] (0,-3.5) -- (0,3.5) node[right] {$y$};\n"
                        "\\node[below left] at (0,0) {$O$};\n"
                        "\\draw[dashed, line width=0.5pt] (-1.57, -3.5) -- (-1.57, 3.5) node[below, yshift=-7cm] {$-\\frac{\\pi}{2}$};\n"
                        "\\draw[dashed, line width=0.5pt] (1.57, -3.5) -- (1.57, 3.5) node[below, yshift=-7cm] {$\\frac{\\pi}{2}$};\n"
                        "\\draw[dashed, line width=0.5pt] (-4.71, -3.5) -- (-4.71, 3.5);\n"
                        "\\draw[dashed, line width=0.5pt] (4.71, -3.5) -- (4.71, 3.5);\n"
                        "\\draw[domain=-1.35:1.35, smooth, samples=100, line width=1pt] plot (\\x, {tan(\\x r)});\n"
                        "\\draw[domain=1.8:4.4, smooth, samples=100, line width=1pt] plot (\\x, {tan(\\x r)});\n"
                        "\\draw[domain=-4.4:-1.8, smooth, samples=100, line width=1pt] plot (\\x, {tan(\\x r)});\n"
                        "\\filldraw (-3.14,0) circle (1.5pt) node[above left] {$-\\pi$};\n"
                        "\\filldraw (3.14,0) circle (1.5pt) node[above left] {$\\pi$};\n"
                        "\\node[below left] at (-1.57,0) {$-\\frac{\\pi}{2}$};\n"
                        "\\node[below right] at (1.57,0) {$\\frac{\\pi}{2}$};\n"
                        "\\node[below left] at (-3.92,0) {$-\\frac{3\\pi}{2}$};\n"
                        "\\node[below right] at (3.92,0) {$\\frac{3\\pi}{2}$};\n"
                        "\\end{tikzpicture} \\end{center}"
                    )
                else:
                    ham_str = '$y = \\tan 2x$'
                    pa_A = 'Hàm số $y = \\tan 2x$ luôn luôn tăng'
                    pa_B = '\\True Hàm số $y = \\tan 2x$ luôn luôn tăng trên từng khoảng xác định'
                    pa_C = 'Hàm số $y = \\tan 2x$ tăng trong các khoảng $\\left(\\frac{\\pi}{2} + k\\pi; \\pi + k\\pi\\right), k \\in \\mathbb{Z}$'
                    pa_D = 'Hàm số $y = \\tan 2x$ tăng trong các khoảng $\\left(\\frac{k\\pi}{2}; \\frac{\\pi}{2} + \\frac{k\\pi}{2}\\right), k \\in \\mathbb{Z}$'

                    khoang_dung = '$\\left( -\\frac{\\pi}{4} + \\frac{k\\pi}{2}; \\frac{\\pi}{4} + \\frac{k\\pi}{2} \\right), k \\in \\mathbb{Z}$'

                    # Đồ thị TikZ cho hàm số y = tan 2x
                    tikz_graph = (
                        "\\begin{center} \\begin{tikzpicture}[scale=0.8, line width=1pt, >=latex]\n"
                        "\\draw[->] (-4.5,0) -- (4.5,0) node[below] {$x$};\n"
                        "\\draw[->] (0,-3.5) -- (0,3.5) node[right] {$y$};\n"
                        "\\node[below left] at (0,0) {$O$};\n"
                        "\\draw[dashed, line width=0.5pt] (-0.785, -3.5) -- (-0.785, 3.5);\n"
                        "\\draw[dashed, line width=0.5pt] (0.785, -3.5) -- (0.785, 3.5);\n"
                        "\\draw[dashed, line width=0.5pt] (-2.355, -3.5) -- (-2.355, 3.5);\n"
                        "\\draw[dashed, line width=0.5pt] (2.355, -3.5) -- (2.355, 3.5);\n"
                        "\\draw[domain=-0.68:0.68, smooth, samples=100, line width=1pt] plot (\\x, {tan(2*\\x r)});\n"
                        "\\draw[domain=0.9:2.2, smooth, samples=100, line width=1pt] plot (\\x, {tan(2*\\x r)});\n"
                        "\\draw[domain=-2.2:-0.9, smooth, samples=100, line width=1pt] plot (\\x, {tan(2*\\x r)});\n"
                        "\\filldraw (-1.57,0) circle (1.5pt) node[above left] {$-\\frac{\\pi}{2}$};\n"
                        "\\filldraw (1.57,0) circle (1.5pt) node[above left] {$\\frac{\\pi}{2}$};\n"
                        "\\node[below left] at (-0.785,0) {$-\\frac{\\pi}{4}$};\n"
                        "\\node[below right] at (0.785,0) {$\\frac{\\pi}{4}$};\n"
                        "\\node[below left] at (-2.355,0) {$-\\frac{3\\pi}{4}$};\n"
                        "\\node[below right] at (2.355,0) {$\\frac{3\\pi}{4}$};\n"
                        "\\end{tikzpicture} \\end{center}"
                    )

                # Câu hỏi sử dụng %s đúng cấu trúc mẫu
                noidungcauhoi = ('''Chọn khẳng định đúng?''')

                # Định dạng các phương án trả lời trắc nghiệm (không chứa dấu chấm ở cuối)
                da_d = str(pa_B)
                da_s1 = str(pa_A)
                da_s2 = str(pa_C)
                da_s3 = str(pa_D)

                # Đưa các đáp án vào một danh sách trộn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết được trình bày đầy đủ từng bước như ảnh mẫu, sử dụng %s
                loigiai = ('''Với A ta thấy hàm số $%s$ không xác định tại mọi điểm $x \\in \\mathbb{R}$ nên tồn tại các điểm làm \\\\
                           %s
                           cho hàm số bị gián đoạn nên hàm số không thể luôn tăng. \\\\
                           Với B ta thấy B đúng vì hàm số $%s$ đồng biến trên mỗi khoảng $%s$.'''
                           % (str(ham_str), str(tikz_graph), str(ham_str), str(khoang_dung)))

            # Xuất câu trắc nghiệm đúng định dạng hệ thống mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

