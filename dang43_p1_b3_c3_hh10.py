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


def bt_dang43_p1_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến sympy
            x_sym, y_sym, m_sym = sp.symbols('x y m')

            # Random nghiệm trước để đảm bảo bài toán luôn có nghiệm nguyên đẹp
            m1 = random.randint(-4, 4)
            m2 = random.choice([m for m in range(-4, 5) if m != m1])

            # Random đường thẳng d: x + y + c = 0
            c = random.randint(-4, 4)

            # Tính tọa độ b của tâm I. Để pt bậc 2 có 2 nghiệm m1, m2 thì a - b = m1 + m2 + c
            b = random.randint(-3, 3)
            a = m1 + m2 + c + b

            # Tính khoảng cách MI bình phương (D2 = MI^2)
            D2 = (m1 - a)**2 + (m1 + c + b)**2

            # Đảm bảo D2 đủ lớn để tồn tại bán kính R
            while D2 <= 1:
                m1 = random.randint(-4, 4)
                m2 = random.choice([m for m in range(-4, 5) if m != m1])
                c = random.randint(-4, 4)
                b = random.randint(-3, 3)
                a = m1 + m2 + c + b
                D2 = (m1 - a)**2 + (m1 + c + b)**2

            # Random bán kính R
            R = random.randint(1, int(math.sqrt(D2 - 1)))
            R2 = R**2

            # Tính AM^2 (Theo Pytago trong tam giác vuông MAI)
            AM2 = D2 - R2

            # Phương trình đường tròn (C): x^2 + y^2 - 2ax - 2by + E = 0
            E = a**2 + b**2 - R2
            circle_expr = x_sym**2 + y_sym**2 - 2*a*x_sym - 2*b*y_sym + E
            circle_str = sp.latex(circle_expr) + " = 0"

            # Phương trình đường thẳng d
            line_expr = x_sym + y_sym + c
            line_str = sp.latex(line_expr) + " = 0"

            # Tọa độ M theo m
            M_y_expr = -m_sym - c
            M_y_str = sp.latex(M_y_expr)

            # Tính diện tích (S) và nửa diện tích
            S_val = R * sp.sqrt(AM2)
            S_str = sp.latex(sp.simplify(S_val))
            half_S_str = sp.latex(sp.simplify(S_val / 2))
            AM_str = sp.latex(sp.simplify(sp.sqrt(AM2)))

            # Biểu thức trong dấu căn của MI (Dùng sympy để tự xử lý dấu +- và --)
            expr1 = a - m_sym
            expr2 = m_sym + b + c
            quad_expr = 2*m_sym**2 - 2*(m1+m2)*m_sym + 2*m1*m2

            # Tọa độ cụ thể của M1, M2
            y1 = -m1 - c
            y2 = -m2 - c

            # ==================== NỘI DUNG CÂU HỎI VÀ ĐÁP ÁN ====================
            # Câu hỏi
            noidungcauhoi = (f"Trong mặt phẳng với hệ trục tọa độ $Oxy$, cho đường tròn $(C): {circle_str}$. "
                             f"Gọi $I$ là tâm và $R$ là bán kính của $(C)$. Tọa độ điểm $M$ thuộc đường thẳng "
                             f"$d: {line_str}$ sao cho từ $M$ kẻ được hai tiếp tuyến $MA, MB$ đến $(C)$ "
                             f"($A, B$ là các tiếp điểm) thỏa mãn tứ giác $MAIB$ có diện tích bằng ${S_str}$ là")

            # Lời giải chi tiết
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
                f"Đường tròn $(C)$ có tâm $I({a}, {b})$ và bán kính $R = {R}$.\\\\\n"
                f"Ta có $S_{{\\Delta MAI}} = \\frac{{1}}{{2}}S_{{MAIB}} = {half_S_str} "
                f"\\Leftrightarrow \\frac{{1}}{{2}}AM.AI = {half_S_str} \\Leftrightarrow AM = \\frac{{{S_str}}}{{AI}} = {AM_str}$.\\\\\n"
                f"Suy ra $MI = \\sqrt{{AM^2 + AI^2}} = \\sqrt{{{D2}}}$. Do $M \\in d$ nên $M(m, {M_y_str})$. Ta có:\\\\\n"
                f"$MI = \\sqrt{{{D2}}} \\Leftrightarrow \\sqrt{{({sp.latex(expr1)})^2 + ({sp.latex(expr2)})^2}} = \\sqrt{{{D2}}}$\\\\\n"
                f"$\\Leftrightarrow {sp.latex(quad_expr)} = 0$\\\\\n"
                f"$\\Leftrightarrow \\left[ \\begin{{matrix}} m = {m1} \\\\ m = {m2} \\end{{matrix}} \\right.$\\\\\n"
                f"Vậy $M({m1}, {y1})$ hoặc $M({m2}, {y2})$."
            )

            # Các đáp án trắc nghiệm
            da_dung = f"$M({m1}, {y1})$ hoặc $M({m2}, {y2})$"

            # Tạo danh sách đáp án nhiễu (sai dấu, ngược tọa độ...)
            distractors = [
                f"$M({-m1}, {-y1})$ hoặc $M({-m2}, {-y2})$",
                f"$M({y1}, {m1})$ hoặc $M({y2}, {m2})$",
                f"$M({m1}, {-y1})$ hoặc $M({m2}, {-y2})$",
                f"$M({m2}, {y1})$ hoặc $M({m1}, {y2})$",
                f"$M({-m2}, {y2})$ hoặc $M({-m1}, {y1})$",
                f"$M({m1+1}, {y1})$ hoặc $M({m2-1}, {y2})$"
            ]
            # Lọc loại bỏ đáp án nhiễu trùng với đáp án đúng
            distractors = list(set([d for d in distractors if d != da_dung]))
            random.shuffle(distractors)

            da_d = ('\\True ' + da_dung)
            da_s1 = distractors[0]
            da_s2 = distractors[1]
            da_s3 = distractors[2]

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # ==================== XUẤT CÂU TRẮC NGHIỆM ====================
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

