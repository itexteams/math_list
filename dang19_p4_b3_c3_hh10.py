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


def bt_dang19_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Biến số
            x, y, m = symbols('x y m')

            # B1 & B3: Nghiên cứu và tìm cách random bài toán
            # Để bài toán đẹp, ta chọn tâm I và bán kính R là số nguyên
            a = random.randint(-3, 3)
            b = random.randint(-3, 3)
            R = random.randint(2, 4)

            # Đường thẳng d: x + y + c = 0. 
            # Để có 2 tiếp tuyến và tam giác MAB vuông thì MI = R*sqrt(2)
            # Khoảng cách từ I đến d phải <= R*sqrt(2)
            # d(I, d) = |a + b + c| / sqrt(2) <= R*sqrt(2) => |a + b + c| <= 2R
            c = random.randint(-(a + b) - 2*R + 1, -(a + b) + 2*R - 1)

            # Phương trình đường tròn (C): x^2 + y^2 - 2ax - 2by + (a^2 + b^2 - R^2) = 0
            k = a**2 + b**2 - R**2
            circle_expr = x**2 + y**2 - 2*a*x - 2*b*y + k
            # Rút gọn hiển thị dấu (ví dụ + - thành -) thông qua sympy
            circle_latex = latex(circle_expr) + " = 0"

            # Đường thẳng d: x + y + c = 0
            line_latex = "x + y" + (" + " if c > 0 else " - ") + str(abs(c)) + " = 0"

            # Giải phương trình tìm M
            # M thuộc d => M(m, -m-c)
            # MI^2 = 2*R^2
            dist_sq = (m - a)**2 + (-m - c - b)**2
            eq_mi = Eq(dist_sq, 2*R**2)
            # Khai triển phương trình để trình bày lời giải
            expanded_eq = expand(dist_sq - 2*R**2)
            sol_m = solve(eq_mi, m)

            # Tính tọa độ M tương ứng
            list_M = []
            for val_m in sol_m:
                val_y = -val_m - c
                list_M.append((val_m, val_y))

            # Tính tọa độ M tương ứng
            list_M = []
            for val_m in sol_m:
                val_y = -val_m - c
                list_M.append((val_m, val_y))

            # Chuẩn bị đáp án trắc nghiệm
            def format_pt(pt):
                # pt là một tuple (x, y)
                return f"M\\left({latex(pt[0])}; {latex(pt[1])}\\right)"

            if len(list_M) == 2:
                da_dung = f"${format_pt(list_M[0])}$ hoặc ${format_pt(list_M[1])}$"

                # SỬA LỖI TẠI ĐÂY: Truy xuất index [0] và [1] của từng điểm
                # Tạo điểm sai 1 bằng cách tịnh tiến tọa độ x+1, y-1
                m1_sai = (list_M[0][0] + 1, list_M[0][1] - 1)
                m2_sai = (list_M[1][0] + 1, list_M[1][1] - 1)
                sai1 = f"${format_pt(m1_sai)}$ hoặc ${format_pt(m2_sai)}$"

                # Tạo điểm sai 2 bằng cách đổi chỗ x và y
                m1_sai2 = (list_M[0][1], list_M[0][0])
                m2_sai2 = (list_M[1][1], list_M[1][0])
                sai2 = f"${format_pt(m1_sai2)}$ hoặc ${format_pt(m2_sai2)}$"

                # Tạo điểm sai 3 bằng cách đổi dấu tọa độ
                m1_sai3 = (-list_M[0][0], -list_M[0][1])
                m2_sai3 = (-list_M[1][0], -list_M[1][1])
                sai3 = f"${format_pt(m1_sai3)}$ hoặc ${format_pt(m2_sai3)}$"
            else:
                da_dung = "Không có điểm M thỏa mãn"
                sai1, sai2, sai3 = "$M(1;1)$", "$M(2;2)$", "$M(0;0)$"

            # B2: Viết lại bài toán theo mẫu
            noidungcauhoi = (f"Trong mặt phẳng với hệ trục tọa độ $Oxy$, cho đường tròn $(C): {circle_latex}$. "
                             f"Gọi $I$ là tâm và $R$ là bán kính của $(C)$. Tìm tọa độ điểm $M$ thuộc đường thẳng "
                             f"$d: {line_latex}$ sao cho từ $M$ kẻ được hai tiếp tuyến $MA, MB$ đến $(C)$ "
                             f"($A, B$ là các tiếp điểm) thỏa mãn tam giác $MAB$ vuông.")

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
                f"Đường tròn $(C)$ có tâm $I({a}; {b})$ và bán kính $R = {R}$.\\\\ "
                       f"Vì $\\triangle MAB$ vuông tại $M$ và $MA, MB$ là hai tiếp tuyến nên tứ giác $MAIB$ là hình vuông.\\\\ "
                       f"Suy ra $MI = R\\sqrt{{2}} = {R}\\sqrt{{2}}$.\\\\ "
                       f"Do $M \\in d$ nên tọa độ $M$ có dạng $M(m; {-c}-m)$.\\\\ "
                       f"Ta có: $MI^2 = (R\\sqrt{{2}})^2 \\Leftrightarrow (m - {a})^2 + ({-c}-m - {b})^2 = {2*R**2}$ \\\\ "
                       f"$\\Leftrightarrow {latex(expanded_eq)} = 0$. \\\\ "
                       f"Giải phương trình ta được " + " hoặc ".join([f"$m = {latex(val)}$" for val in sol_m]) + ".\\\\ "
                       f"Vậy tọa độ điểm $M$ cần tìm là: {da_dung}.")

            # Các đáp án
            da_d = ('\\True ' + str(da_dung))
            list_1 = [da_d, str(sai1), str(sai2), str(sai3)]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -','+').replace('- +','-').replace('+ -','-')
            return content

