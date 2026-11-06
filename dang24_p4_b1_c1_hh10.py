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


def bt_dang24_p4_b1_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random công sai d và số hạng đầu u1
                d = random.choice([1, 2, 3, 4, 5])

                # Chọn u1 sao cho un = 90 - u1 thuộc dãy, tức là (90 - 2*u1) chia hết cho d
                u1_candidates = [x for x in range(1, 40) if (90 - 2*x) % d == 0]
                u1 = random.choice(u1_candidates)

                # Tính toán các số hạng trong dãy
                un = 90 - u1
                u2 = u1 + d
                u3 = u1 + 2*d
                un_1 = un - d
                un_2 = un - 2*d

                # Tính số lượng số hạng và số cặp
                N = (un - u1) // d + 1
                so_cap = N // 2

                # Tính kết quả tổng
                kq = Rational(N, 2)
                kq_str = latex(kq).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq_str)]
                da = random.choice(du)

                # Tạo tập đáp án nhiễu, đảm bảo không trùng với đáp án đúng
                s_set = [kq + 1, kq - 1, kq + 2, kq - 2, Rational(N+1, 2), Rational(N-1, 2)]
                s_set = list(set(s_set))
                if kq in s_set:
                    s_set.remove(kq)

                s = ['$%s$'%(latex(val)).replace('.', ',') for val in random.sample(s_set, 3)]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Tính $\\sin^2 %s^\\circ + \\sin^2 %s^\\circ + \\sin^2 %s^\\circ + \\dots + \\sin^2 %s^\\circ + \\sin^2 %s^\\circ + \\sin^2 %s^\\circ$.'''
                                 % (u1, u2, u3, un_2, un_1, un))

                # Các đáp án (Quy định: Không dấu chấm ở cuối các phương án)
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Chia trường hợp tổng có số hạng chẵn hoặc lẻ)
                if N % 2 == 0:
                    loigiai = ('''Dãy các số đo góc: $%s^\\circ, %s^\\circ, %s^\\circ, \\dots, %s^\\circ, %s^\\circ, %s^\\circ$ là một cấp số cộng với số hạng đầu là $%s$, công sai $d = %s$.\\\\
                        Số các số hạng của tổng là: $\\frac{%s - %s}{%s} + 1 = %s$.\\\\
                        Ghép các số hạng từ ngoài vào trong, ta được $%s$ cặp:\\\\
                        $S = (\\sin^2 %s^\\circ + \\sin^2 %s^\\circ) + (\\sin^2 %s^\\circ + \\sin^2 %s^\\circ) + \\dots$\\\\
                        Nhận thấy trong mỗi cặp, tổng hai góc luôn bằng $90^\\circ$ (hai góc phụ nhau).\\\\
                        Áp dụng tính chất hai góc phụ nhau $\\sin(90^\\circ - \\alpha) = \\cos\\alpha$, ta có:\\\\
                        $\\sin^2 %s^\\circ + \\sin^2 %s^\\circ = \\sin^2 %s^\\circ + \\cos^2 %s^\\circ = 1$.\\\\
                        Tương tự cho các cặp còn lại, do đó mỗi cặp có tổng bằng $1$.\\\\
                        Vậy $S = 1 + 1 + \\dots + 1 = %s \\cdot 1 = %s$.'''
                    % (u1, u2, u3, un_2, un_1, un, u1, d,
                       un, u1, d, N,
                       so_cap,
                       u1, un, u2, un_1,
                       u1, un, u1, u1,
                       so_cap, kq_str))
                else:
                    loigiai = ('''Dãy các số đo góc: $%s^\\circ, %s^\\circ, %s^\\circ, \\dots, %s^\\circ, %s^\\circ, %s^\\circ$ là một cấp số cộng với số hạng đầu là $%s$, công sai $d = %s$.\\\\
                        Số các số hạng của tổng là: $\\frac{%s - %s}{%s} + 1 = %s$.\\\\
                        Ghép các số hạng từ ngoài vào trong, ta được $%s$ cặp và dư lại góc ở chính giữa là $45^\\circ$:\\\\
                        $S = (\\sin^2 %s^\\circ + \\sin^2 %s^\\circ) + (\\sin^2 %s^\\circ + \\sin^2 %s^\\circ) + \\dots + \\sin^2 45^\\circ$.\\\\
                        Nhận thấy trong mỗi cặp, tổng hai góc luôn bằng $90^\\circ$ (hai góc phụ nhau).\\\\
                        Áp dụng tính chất hai góc phụ nhau $\\sin(90^\\circ - \\alpha) = \\cos\\alpha$, ta có:\\\\
                        $\\sin^2 %s^\\circ + \\sin^2 %s^\\circ = \\sin^2 %s^\\circ + \\cos^2 %s^\\circ = 1$.\\\\
                        Tương tự cho các cặp còn lại, do đó mỗi cặp có tổng bằng $1$.\\\\
                        Vậy $S = %s \\cdot 1 + \\sin^2 45^\\circ = %s + \\left(\\frac{\\sqrt{2}}{2}\\right)^2 = %s + \\frac{1}{2} = %s$.'''
                    % (u1, u2, u3, un_2, un_1, un, u1, d,
                       un, u1, d, N,
                       so_cap,
                       u1, un, u2, un_1,
                       u1, un, u1, u1,
                       so_cap, so_cap, so_cap, kq_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

