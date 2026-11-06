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


def bt_dang49_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Hàm để tạo phương trình đường thẳng ax + by + c = 0 từ hai điểm hoặc một điểm và hệ số
            def tạo_pt_dt(p1, p2=None, vtcp=None):
                x, y = symbols('x y')
                if p2:
                    a = p1[1] - p2[1]
                    b = p2[0] - p1[0]
                    c = -(a * p1[0] + b * p1[1])
                elif vtcp:
                    # vtcp = (u1, u2) -> vtpt = (u2, -u1)
                    a, b = vtcp[1], -vtcp[0]
                    c = -(a * p1[0] + b * p1[1])

                # Rút gọn hệ số
                u = gcd(gcd(a, b), c)
                if a < 0 or (a == 0 and b < 0):
                    u = -u
                return a // u, b // u, c // u

            def format_pt(a, b, c):
                x, y = symbols('x y')
                expr = a*x + b*y + c
                return latex(expr) + " = 0"

            # Khai báo biến và chọn dạng (ở đây chỉ có 1 dạng)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Chọn tọa độ nguyên cho tâm I và đỉnh A
                # Để C cũng nguyên, I và A nên là số nguyên
                xA, yA = random.randint(-5, 5), random.randint(-5, 5)
                xI, yI = random.randint(-5, 5), random.randint(-5, 5)

                # Đảm bảo I khác A
                while xI == xA and yI == yA:
                    xI, yI = random.randint(-5, 5), random.randint(-5, 5)

                # Tính tọa độ C (I là trung điểm AC)
                xC = 2 * xI - xA
                yC = 2 * yI - yA

                # Bước 2: Tạo các đường thẳng
                # d1 (AC) đi qua A và I
                a1, b1, c1 = tạo_pt_dt((xA, yA), (xI, yI))

                # d2 (BD) đi qua I, chọn hệ số ngẫu nhiên (không trùng d1)
                a2, b2 = random.randint(-3, 3), random.randint(-3, 3)
                while a2*b1 == a1*b2 or (a2 == 0 and b2 == 0):
                    a2, b2 = random.randint(-3, 3), random.randint(-3, 3)
                c2 = -(a2 * xI + b2 * yI)
                a2, b2, c2 = tạo_pt_dt((xI, yI), vtcp=(b2, -a2)) # Chuẩn hóa

                # AB đi qua A, chọn hệ số ngẫu nhiên (không trùng d1)
                a3, b3 = random.randint(-3, 3), random.randint(-3, 3)
                while a3*b1 == a1*b3 or (a3 == 0 and b3 == 0):
                    a3, b3 = random.randint(-3, 3), random.randint(-3, 3)
                c3 = -(a3 * xA + b3 * yA)
                a3, b3, c3 = tạo_pt_dt((xA, yA), vtcp=(b3, -a3)) # Chuẩn hóa

                # Tọa độ điểm C là đáp án đúng
                da = 'C(' + str(xC) + ';' + str(yC) + ')'

                # Tạo các phương án sai
                s = []
                while len(s) < 3:
                    dx, dy = random.randint(-3, 3), random.randint(-3, 3)
                    if dx == 0 and dy == 0: continue
                    fake_C = 'C(' + str(xC + dx) + ';' + str(yC + dy) + ')'
                    if fake_C not in s and fake_C != da:
                        s.append(fake_C)

                das1, das2, das3 = s[0], s[1], s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho hình bình hành $ABCD$, biết hai đường chéo $AC$ và $BD$ lần lượt nằm trên hai đường thẳng $d_1: %s, d_2: %s$ và phương trình đường thẳng $AB: %s$. Tọa độ điểm $C$ là'''
                                 %(format_pt(a1, b1, c1), format_pt(a2, b2, c2), format_pt(a3, b3, c3)))

                # Các đáp án
                da_d = '\\True ' + da
                da_s1 = das1
                da_s2 = das2
                da_s3 = das3

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $I$ là tâm của hình bình hành. Ta có $I = AC \\cap BD$ nên tọa độ điểm $I(x;y)$ thỏa mãn hệ 
                           $\\begin{cases} %s \\\\ %s \\end{cases} \\Rightarrow I(%s;%s)$.\\\\
                           Do $A = AB \\cap AC$ nên tọa độ điểm $A(x;y)$ thỏa mãn hệ 
                           $\\begin{cases} %s \\\\ %s \\end{cases} \\Rightarrow A(%s;%s)$.\\\\
                           Hình bình hành có hai đường chéo cắt nhau tại trung điểm mỗi đường nên $I$ là trung điểm $AC$ suy ra $%s$.'''
                           %(format_pt(a1, b1, c1), format_pt(a2, b2, c2), latex(xI), latex(yI),
                             format_pt(a3, b3, c3), format_pt(a1, b1, c1), latex(xA), latex(yA),
                             da))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

