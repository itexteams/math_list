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


def bt_dang45_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: SINH DỮ LIỆU ĐỂ KẾT QUẢ LUÔN LÀ SỐ NGUYÊN ---
                # Ta xây dựng dựa trên trục đối xứng IJ
                # Chọn J (trung điểm CD) là số nguyên hoặc nửa nguyên để C, D nguyên
                # Để an toàn nhất, ta chọn J, I sao cho các phép tính sau đó không bị phân số khó chịu

                # Chọn vectơ u = (u1, u2) là vectơ chỉ phương của hai đáy
                # Chọn u1, u2 sao cho u1^2 + u2^2 không quá lớn
                u1 = randint(1, 5) * random.choice([-1, 1])
                u2 = randint(1, 5) * random.choice([-1, 1])

                # Để C, D, A, B là số nguyên:
                # Chọn J là điểm nguyên
                xJ = randint(-15, 10)
                yJ = randint(-15, 10)

                # Chọn vectơ v vuông góc với u: v = (-u2, u1)
                # I = J + k*v (I nằm trên trục đối xứng)
                k_val = randint(2, 5)
                xI = xJ - k_val * u2
                yI = yJ + k_val * u1

                # Độ dài đáy CD = 2*m1*u, AB = 2*m2*u
                m1 = randint(3, 6)
                m2 = randint(1, 2) # m1 != m2 để là hình thang, m2 < m1 để giống hình mẫu

                # Tính tọa độ các đỉnh
                # D = J - m1*u, C = J + m1*u
                xD, yD = xJ - m1 * u1, yJ - m1 * u2
                xC, yC = xJ + m1 * u1, yJ + m1 * u2

                # A = I - m2*u, B = I + m2*u
                xA, yA = xI - m2 * u1, yI - m2 * u2
                xB, yB = xI + m2 * u1, yI + m2 * u2

                # --- BƯỚC 2: TÍNH TOÁN CÁC THÀNH PHẦN LỜI GIẢI (GIỐNG ẢNH) ---
                # Véc tơ AB
                u_ab1 = xB - xA
                u_ab2 = yB - yA

                # Phương trình CD: đi qua D, nhận vecAB làm VTCP -> VTPT n = (-u_ab2, u_ab1)
                n_cd_x = -u_ab2
                n_cd_y = u_ab1
                g_cd = math.gcd(abs(int(n_cd_x)), abs(int(n_cd_y)))
                a_cd, b_cd = n_cd_x // g_cd, n_cd_y // g_cd
                if a_cd < 0 or (a_cd == 0 and b_cd < 0):
                    a_cd, b_cd = -a_cd, -b_cd
                c_cd = -(a_cd * xD + b_cd * yD)

                # Trung điểm I của AB (đã có xI, yI ở trên, ép kiểu Rational để latex đẹp)
                I_coord = (Rational(xA + xB, 2), Rational(yA + yB, 2))

                # Phương trình IJ: qua I, vuông góc CD -> nhận vecAB làm VTPT
                n_ij_x = u_ab1
                n_ij_y = u_ab2
                g_ij = math.gcd(abs(int(n_ij_x)), abs(int(n_ij_y)))
                a_ij, b_ij = n_ij_x // g_ij, n_ij_y // g_ij
                if a_ij < 0 or (a_ij == 0 and b_ij < 0):
                    a_ij, b_ij = -a_ij, -b_ij
                c_ij = -(a_ij * xI + b_ij * yI)

                # --- BƯỚC 3: TẠO NỘI DUNG ---
                noidungcauhoi = ('Trong mặt phẳng với hệ tọa độ $Oxy$, cho ba điểm $A(%s;%s)$, $B(%s;%s)$, $D(%s;%s)$ là các đỉnh của hình thang cân $ABCD$ trong đó $AB$ song song với $CD$. Tìm tọa độ điểm $C$.'
                                 % (latex(xA), latex(yA), latex(xB), latex(yB), latex(xD), latex(yD)))

                def fmt_eq(a, b, c):
                    def term(coeff, var):
                        if coeff == 0: return ""
                        if coeff == 1: return f"+{var}"
                        if coeff == -1: return f"-{var}"
                        return f"{coeff:+g}{var}"
                    s = term(a, "x") + term(b, "y") + f"{c:+g}"
                    if s.startswith("+"): s = s[1:]
                    return s + "=0"

                loigiai = ('''Đường thẳng $CD$ đi qua $D(%s;%s)$ và nhận $\\overrightarrow{AB}=(%s;%s)$ làm vectơ chỉ phương nên có phương trình $%s$. \\\\
            Gọi $I, J$ lần lượt là trung điểm của $AB$ và $CD$. \\\\
            Ta có $I\\left(%s;%s\\right)$ và $IJ \\perp CD$. \\\\
            Phương trình đường thẳng $IJ$ là $%s$. \\\\
            Mà $J = IJ \\cap CD$ nên tọa độ điểm $J$ là nghiệm của hệ: $\\begin{cases} %s \\\\ %s \\end{cases}$, ta được $J\\left(%s;%s\\right)$. \\\\
            Theo tính chất hình thang cân thì $J$ là trung điểm của $CD$, suy ra $C(%s;%s)$.'''
                           % (latex(xD), latex(yD), latex(u_ab1), latex(u_ab2), fmt_eq(a_cd, b_cd, c_cd),
                              latex(I_coord[0]), latex(I_coord[1]), fmt_eq(a_ij, b_ij, c_ij),
                              fmt_eq(a_cd, b_cd, c_cd), fmt_eq(a_ij, b_ij, c_ij),
                              latex(xJ), latex(yJ), latex(xC), latex(yC)))

                # Đáp án
                da_dung = '$(%s;%s)$' % (latex(xC), latex(yC))
                s1 = '$(%s;%s)$' % (latex(xC + randint(1, 3)), latex(yC - randint(1, 3)))
                s2 = '$(%s;%s)$' % (latex(xD + u_ab1), latex(yD + u_ab2)) # Tọa độ nếu là hbh
                s3 = '$(%s;%s)$' % (latex(yC), latex(xC))

                list_ans = [da_dung, s1, s2, s3]
                # Trộn và đánh dấu True
                list_ans_formatted = []
                for i, ans in enumerate(list_ans):
                    if i == 0: list_ans_formatted.append('\\True ' + ans)
                    else: list_ans_formatted.append(ans)

                random.shuffle(list_ans_formatted)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

