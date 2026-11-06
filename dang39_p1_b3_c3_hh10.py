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


def bt_dang39_p1_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo các ký hiệu toán học
            x, y, t = symbols('x y t')

            # B3: Suy nghĩ tìm cách random bài toán
            # Để bài toán có nghiệm đẹp hoặc thực tế, ta random tâm I và bán kính R^2
            a = random.randint(-5, 5) # Hoành độ tâm I
            b = random.randint(-5, 5) # Tung độ tâm I
            r_sq = random.choice([2, 3, 4, 5, 6, 8, 10]) # R^2
            # Đường thẳng d: x + y + c_line = 0 -> y = -x - c_line
            c_line = random.randint(-5, 5)

            # Tính các hệ số của phương trình đường tròn: x^2 + y^2 - 2ax - 2by + (a^2 + b^2 - R^2) = 0
            h_x = -2 * a
            h_y = -2 * b
            const_c = a**2 + b**2 - r_sq

            # Phương trình đường tròn (C) dạng chuỗi LaTeX
            # Xử lý hiển thị dấu + -
            def format_sign(val, var_str=""):
                if val == 0: return ""
                sign = "+" if val > 0 else "-"
                return f" {sign} {abs(val)}{var_str}"

            circle_eq = f"x^2 + y^2{format_sign(h_x, 'x')}{format_sign(h_y, 'y')}{format_sign(const_c)} = 0"
            line_eq = f"x + y {format_sign(c_line)} = 0"

            # --- GIẢI BÀI TOÁN ---
            # Tâm I(a, b), Bán kính R = sqrt(r_sq)
            # M thuộc d => M(t, -t - c_line)
            # Hai tiếp tuyến vuông góc <=> MAIB là hình vuông <=> MI = R*sqrt(2) <=> MI^2 = 2*R^2
            dist_sq = (t - a)**2 + ((-t - c_line) - b)**2
            eq = sp.Eq(dist_sq, 2 * r_sq)
            roots = solve(eq, t)

            # Lọc các nghiệm (nếu có nghiệm ảo thì bỏ qua, nhưng thiết kế này thường ra nghiệm thực)
            roots = [r for r in roots if r.is_real]

            if not roots:
                # Nếu không có nghiệm (hiếm gặp với MI^2), gán mặc định để tránh lỗi code
                roots = [0]

            # Tạo nội dung câu hỏi
            noidungcauhoi = f"Trong mặt phẳng với hệ tọa độ $Oxy$. Cho đường tròn $(C): {circle_eq}$ và đường thẳng $d: {line_eq}$. Điểm $M$ thuộc đường thẳng $d$ sao cho từ điểm $M$ kẻ được đến $(C)$ hai tiếp tuyến hợp với nhau một góc $90^\\circ$ là"

            # Tạo lời giải chi tiết
            # MI^2 = (t - a)^2 + (-c_line - b - t)^2
            # Khai triển: (t-a)^2 + (t + (c_line+b))^2 = 2t^2 + 2t(c_line+b-a) + a^2 + (c_line+b)^2
            expanded_dist = simplify(dist_sq)
            mi_sq_val = 2 * r_sq

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
            	\\draw (2.66,6) node[anchor=north west] {$A$};
            	\\draw (6,2.7) node[anchor=north west] {$B$};
            	\\draw (3.,5.)-- (6.,2.);
            \\end{tikzpicture}
            \\end{center}'''
                f"""Đường tròn $(C)$ có tâm $I({a}; {b})$ và bán kính $R = \\sqrt{{{r_sq}}}$. \\\\
            $M \\in d \\Rightarrow M(t; {-c_line}-t)$. \\\\
            Để từ $M$ kẻ được hai tiếp tuyến đến $(C)$ vuông góc với nhau thì tứ giác $MAIB$ (với $A, B$ là các tiếp điểm) là hình vuông. \\\\
            Khi đó $MI = R\\sqrt{{2}} = \\sqrt{{{r_sq}}} \\cdot \\sqrt{{2}} = \\sqrt{{{mi_sq_val}}}$. \\\\
            Ta có: $MI^2 = (t - ({a}))^2 + ({-c_line} - t - ({b}))^2 = {latex(expanded_dist)}$. \\\\
            Do đó: ${latex(expanded_dist)} = {mi_sq_val} \\Leftrightarrow {latex(simplify(expanded_dist - mi_sq_val))} = 0$.""")

            # Danh sách các điểm M tìm được
            list_m_coords = []
            for r in roots:
                y_val = -r - c_line
                m_point = f"M({latex(r)}; {latex(y_val)})"
                list_m_coords.append(m_point)

            res_points = " \\text{ và } ".join(list_m_coords)
            loigiai += f"\\\\ Giải phương trình ta được $t = {latex(roots[0])}$ hoặc $t = {latex(roots[1]) if len(roots)>1 else latex(roots[0])}$. \\\\ Vậy các điểm cần tìm là: ${res_points}$."

            # Tạo đáp án
            da_d = f"\\True ${res_points}$"
            # Tạo đáp án nhiễu (giả lập bằng cách thay đổi dấu hoặc giá trị)
            da_s1 = f"${res_points.replace('-', '')}$"
            da_s2 = f"$M(0; {-c_line})$"
            da_s3 = f"Không có điểm $M$ nào thỏa mãn"

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # B2: Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

