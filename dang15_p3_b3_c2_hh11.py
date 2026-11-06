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


def bt_dang15_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng bài (ở đây là 1 dạng duy nhất)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Random bài toán
                # n là hệ số của SA (SA = n*a), m là hệ số của cạnh đáy (AB = m*a)
                n = random.randint(1, 3)
                m = random.randint(2, 5)

                # Tính toán đáp án đúng: cot(phi) = AB/SA = m/n
                ans_val = Rational(m, n)
                da_dung = '$cot \\varphi = %s$' % (latex(ans_val))

                # B4: Tạo các phương án sai (không trùng đáp án đúng)
                s = []
                # Phương án nghịch đảo n/m
                w1 = Rational(n, m)
                if w1 != ans_val:
                    s.append('$cot \\varphi = %s$' % (latex(w1)))

                # Phương án m/(2n)
                w2 = Rational(m, 2 * n)
                if w2 != ans_val:
                    s.append('$cot \\varphi = %s$' % (latex(w2)))

                # Phương án dùng Pitago (thường học sinh nhầm sang cos hoặc sin)
                # Ví dụ: n / sqrt(m^2 + n^2)
                w3_val = Rational(n, 1) / sqrt(m**2 + n**2)
                s.append('$cot \\varphi = \\frac{\\sqrt{%s}}{%s}$' % (m**2 + n**2, m**2 + n**2))

                # Bổ sung thêm phương án ngẫu nhiên nếu chưa đủ 3 câu sai
                while len(s) < 3:
                    rand_val = Rational(random.randint(1, 5), random.randint(1, 5))
                    item = '$cot \\varphi = %s$' % (latex(rand_val))
                    if item != da_dung and item not in s:
                        s.append(item)

                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # B2: Viết lại đề bài và lời giải theo mẫu
                # Hình vẽ TikZ
                hinh_ve = (
                    '\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=0.8, line width=1pt, font=\\footnotesize]\n'
                    '\\coordinate (A) at (0,0);\n'
                    '\\coordinate (B) at (-1.5,-1.5);\n'
                    '\\coordinate (C) at (2.5,-1.5);\n'
                    '\\coordinate (D) at (4,0);\n'
                    '\\coordinate (S) at (0,3.5);\n'
                    '\\draw [dashed] (S)--(A) (A)--(B) (A)--(D);\n'
                    '\\draw (S)--(B)--(C)--(D)--(S) (S)--(C);\n'
                    '\\node [above] at (S) {$S$};\n'
                    '\\node [left] at (A) {$A$};\n'
                    '\\node [below left] at (B) {$B$};\n'
                    '\\node [below right] at (C) {$C$};\n'
                    '\\node [right] at (D) {$D$};\n'
                    '\\draw (0,0.3)--(-0.15,0.15)--(-0.15,-0.15);\n' # Ký hiệu vuông góc tại A (tương đối)
                    '\\end{tikzpicture}\n'
                    '\\end{center}'
                )

                noidungcauhoi = (
                    'Cho hình chóp $S.ABCD$ có đáy là hình vuông cạnh $%sa$, cạnh bên $SA$ vuông góc mặt đáy và $SA = %sa$. '
                    'Gọi $\\varphi$ là góc tạo bởi $SB$ và mặt phẳng $\\left( ABCD \\right)$. $cot \\varphi$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'
                    % (latex(m) if m != 1 else '', latex(n) if n != 1 else '')
                )
                h1=ans_val
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.', ',')

                # Nội dung lời giải chi tiết
                loigiai = (
                    'Ta có $SA \\perp \\left( ABCD \\right)$ nên $A$ là hình chiếu của $S$ lên mặt phẳng $\\left( ABCD \\right)$. \\\\'
                    'Suy ra $AB$ là hình chiếu của $SB$ lên mặt phẳng $\\left( ABCD \\right)$. \\\\'
                    'Do đó $\\left( SB, \\left( ABCD \\right) \\right) = \\left( SB, BA \\right) = \\widehat{SBA}$. \\\\'
                    'Vậy $\\varphi = \\widehat{SBA}$. \\\\'
                    'Trong tam giác $SAB$ vuông tại $A$, ta có: \\\\'
                    '$cot \\varphi = \\frac{AB}{SA} = \\frac{%sa}{%sa} = %s$.'
                    % (latex(m) if m != 1 else '', latex(n) if n != 1 else '', latex(ans_val))
                )
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'  + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + hinh_ve+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

