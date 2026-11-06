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


def bt_dang18_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            while True:
                # Random tọa độ tâm I(a,b), bán kính R và hệ số c của đường thẳng d
                a = random.randint(-3, 3)
                b = random.randint(-3, 3)
                R = random.randint(2, 4)
                c = random.randint(-4, 4)

                # Loại trường hợp tâm trùng gốc tọa độ cho bớt đơn điệu
                if a == 0 and b == 0: 
                    continue

                # Hệ số tự do của phương trình đường tròn: x^2 + y^2 - 2ax - 2by + dc = 0
                dc = a**2 + b**2 - R**2

                # Hệ số phương trình bậc 2 theo m: 2m^2 + B*m + C_coeff = 0
                A = 2
                B = 2 * (b + c - a)
                C_coeff = a**2 + (b + c)**2 - 4 * R**2

                # Tính Delta phẩy để đảm bảo có 2 nghiệm phân biệt và là số vô tỉ
                delta_prime = (B / 2)**2 - A * C_coeff
                if delta_prime > 0 and int(math.sqrt(delta_prime))**2 != delta_prime:
                    break

            m = symbols('m')

            # 1. Định dạng phương trình đường tròn và đường thẳng
            circle_expr = x**2 + y**2 - 2*a*x - 2*b*y + dc
            circle_str = latex(circle_expr) + ' = 0'

            line_expr = x + y + c
            line_str = latex(line_expr) + ' = 0'

            # 2. Các đại lượng trong lời giải
            R2 = 2 * R
            y_m_expr = -m - c
            y_m_str = latex(y_m_expr)

            # 3. Xử lý chuỗi biểu thức khoảng cách (hiển thị đẹp dấu + -)
            term1 = "(-m)^2" if a == 0 else f"({a}-m)^2"

            bc_sum = b + c
            if bc_sum > 0:
                term2 = f"(m+{bc_sum})^2"
            elif bc_sum < 0:
                term2 = f"(m{bc_sum})^2"
            else:
                term2 = "m^2"

            eq_poly = 2*m**2 + B*m + C_coeff
            eq_str = latex(eq_poly) + " = 0"

            # 4. Giải phương trình tìm m
            m_sols = solve(eq_poly, m)
            M1_x, M2_x = m_sols[0], m_sols[1]
            M1_y, M2_y = -M1_x - c, -M2_x - c

            # 5. Khởi tạo đáp án trắc nghiệm
            ans_correct = f"M\\left({latex(M1_x)}; {latex(M1_y)}\\right) \\text{{ hoặc }} M\\left({latex(M2_x)}; {latex(M2_y)}\\right)"

            # Đáp án nhiễu 1: Tính sai tọa độ y của M (lỗi dấu c)
            M1_y_w1, M2_y_w1 = -M1_x + c, -M2_x + c
            ans_w1 = f"M\\left({latex(M1_x)}; {latex(M1_y_w1)}\\right) \\text{{ hoặc }} M\\left({latex(M2_x)}; {latex(M2_y_w1)}\\right)"

            # Đáp án nhiễu 2: Đảo lộn x và y
            ans_w2 = f"M\\left({latex(M1_y)}; {latex(M1_x)}\\right) \\text{{ hoặc }} M\\left({latex(M2_y)}; {latex(M2_x)}\\right)"

            # Đáp án nhiễu 3: Sai dấu của toàn bộ tọa độ
            ans_w3 = f"M\\left({latex(-M1_x)}; {latex(-M1_y)}\\right) \\text{{ hoặc }} M\\left({latex(-M2_x)}; {latex(-M2_y)}\\right)"

            da_d = ('\\True $%s$' % ans_correct)
            da_s1 = '$%s$' % ans_w1
            da_s2 = '$%s$' % ans_w2
            da_s3 = '$%s$' % ans_w3

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Câu hỏi
            noidungcauhoi = (f"Trong mặt phẳng với hệ trục tọa độ $Oxy$, cho đường tròn $(C): {circle_str}$. "
                             f"Gọi $I$ là tâm và $R$ là bán kính của $(C)$. Tìm tọa độ điểm $M$ thuộc đường thẳng $d: {line_str}$ "
                             f"sao cho từ $M$ kẻ được hai tiếp tuyến $MA, MB$ đến $(C)$ ($A, B$ là các tiếp điểm) thỏa mãn "
                             f"tam giác $MAB$ đều.")

            # Nội dung lời giải
            loigiai = ('''\\begin{center}
                           \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=0.6cm,y=0.6cm]
            	\\clip(-3,-1) rectangle (9,6);
            	\\draw (3.,2.)-- (3.,5.);
            	\\draw (6.,2.)-- (3.,2.);
            	\\draw(3.,2.) circle (1.8cm);
            	\\draw (0.,5.)-- (6.,5.);
            	\\draw (6.,5.)-- (6.,0.);
            	\\draw (3.,2.)-- (6.,5.);
            	\\draw (4.,6.)-- (9.35,3.289);
            	\\draw (8.3,4.9) node[anchor=north west] {$d$};
            	\\draw (2.6,2) node[anchor=north west] {$I$};
            	\\draw (6.,6.) node[anchor=north west] {$M$};
            	\\draw (4,3.3) node[anchor=north west] {$H$};
            	\\draw (2.66,6) node[anchor=north west] {$A$};
            	\\draw (6,2.7) node[anchor=north west] {$B$};
            	\\draw (3.,5.)-- (6.,2.);
            \\end{tikzpicture}
            \\end{center}'''

                f"Tam giác $MAB$ đều, suy ra $\\widehat{{AMI}} = 30^\\circ$.\\\\\n"
                       f"Xét tam giác $MAI$ vuông tại $A$, ta có $MI = \\frac{{IA}}{{\\sin \\widehat{{AMI}}}} = 2IA = {R2}$.\\\\\n"
                       f"Do $M \\in d$ nên $M(m; {y_m_str})$. Ta có\\\\\n"
                       f"$MI = {R2} \\Leftrightarrow \\sqrt{{{term1} + {term2}}} = {R2}$\\\\\n"
                       f"$\\Leftrightarrow {eq_str}$\\\\\n"
                       f"$\\Leftrightarrow m = {latex(M1_x)} \\text{{ hoặc }} m = {latex(M2_x)}$\\\\\n"
                       f"Vậy $M\\left({latex(M1_x)}; {latex(M1_y)}\\right)$ hoặc $M\\left({latex(M2_x)}; {latex(M2_y)}\\right)$.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

