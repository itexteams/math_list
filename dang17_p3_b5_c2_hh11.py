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


def bt_dang17_p3_b5_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random độ dài khoảng cách d (đáp án đúng), d nguyên dương từ 2 đến 8
                d_val = randint(2, 8)


                x_val = 2 * d_val

                # A'M = AM / cos(30) = (d * sqrt(3)) / (sqrt(3)/2) = 2 * d
                # Diện tích tam giác A'BC: S = 1/2 * A'M * BC = 1/2 * (2*d) * (2*d) = 2 * d^2
                S_val = 2 * (d_val ** 2)

                # Tính toán lại bằng Sympy để xuất dữ liệu vào lời giải
                d_sym = Integer(d_val)
                x_sym = Integer(x_val)
                S_sym = Integer(S_val)

                # Tính diện tích để biểu diễn trong lời giải: 2 * S / BC = 64 / x
                tu_so_A_M = 2 * S_sym

                # Đáp án đúng
                da = '$%s$' % latex(d_sym)

                # Các đáp án nhiễu (không trùng với đáp án đúng)
                s = []
                for i in [1, 2, 3, -1, -2, -3]:
                    val = d_val + i
                    if val > 0 and val != d_val:
                        s.append('$%s$' % latex(val))

                # Lấy ngẫu nhiên 3 đáp án sai phân biệt
                s = list(set(s))
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho khối lăng trụ tam giác đều $ABC.A'B'C'$. Biết số đo góc nhị diện $[A',BC,A]$ bằng $30^\\circ$ và tam giác $A'BC$ có diện tích bằng $%s$. Khoảng cách giữa hai đường thẳng $AB$ và $A'C'$ bằng bao nhiêu?'''
                                 % (latex(S_sym)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (    '\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=1, line width=1pt, >=stealth]\n'
                    '\\coordinate (A) at (0,0);\n'
                    '\\coordinate (B) at (1.5,-1.2);\n'
                    '\\coordinate (C) at (4,0);\n'
                    '\\coordinate (A\') at (0,4.5);\n'
                    '\\coordinate (B\') at (1.5,3.3);\n'
                    '\\coordinate (C\') at (4,4.5);\n'
                    '\\coordinate (M) at (2.75,-0.6);\n'
                    '\\draw (A\')--(B\')--(C\')--cycle;\n'
                    '\\draw (A)--(B)--(C);\n'
                    '\\draw (A)--(A\') (B)--(B\') (C)--(C\');\n'
                    '\\draw (A\')--(B) (A\')--(M);\n'
                    '\\draw[dashed] (A)--(C) (A)--(M) (A\')--(C);\n'
                    '\\fontfamily{cmr}\\selectfont\n'
                    '\\node[left] at (A) {$A$};\n'
                    '\\node[below] at (B) {$B$};\n'
                    '\\node[right] at (C) {$C$};\n'
                    '\\node[left] at (A\') {$A\'$};\n'
                    '\\node[above] at (B\') {$B\'$};\n'
                    '\\node[right] at (C\') {$C\'$};\n'
                    '\\node[below right] at (M) {$M$};\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}\n'
                    '''Gọi $M$ là trung điểm của $BC$ thì ta có $\\begin{cases} BC \\perp AM \\\\ BC \\perp AA' \\end{cases} \\Rightarrow BC \\perp (A'AM)$. \\\\
                           Suy ra $[A',BC,A] = \\widehat{A'MA} = 30^\\circ$ và đặt $AB = BC = CA = x \\Rightarrow \\begin{cases} AM = \\frac{\\sqrt{3}}{2}x \\\\ A'M = \\frac{2S_{A'BC}}{BC} = \\frac{%s}{x} \\end{cases}$ \\\\
                           $\\Rightarrow \\cos 30^\\circ = \\frac{AM}{A'M} = \\frac{\\frac{\\sqrt{3}}{2}x}{\\frac{%s}{x}} = \\frac{\\sqrt{3}x^2}{%s} = \\frac{\\sqrt{3}}{2} \\Rightarrow x = %s$. \\\\
                           Vậy $AA' = AM \\cdot \\tan 30^\\circ = \\frac{\\sqrt{3}}{2} \\cdot %s \\cdot \\frac{1}{\\sqrt{3}} = %s \\Rightarrow d = %s$. \\\\
                           Khoảng cách giữa hai đường thẳng $AB$ và $A'C'$ bằng $%s$.'''
                           % (latex(tu_so_A_M), latex(tu_so_A_M), latex(2 * tu_so_A_M), latex(x_sym), latex(x_sym), latex(d_sym), latex(d_sym), latex(d_sym)))
                dapan='\\shortans[0]{$%s$}\n'%(d_sym)
            # Xuất câu trắc nghiệm bao gồm hình vẽ TikZ độ dày nét 1pt
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

