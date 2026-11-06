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


def bt_dang47_p4_b3_c3_hh10(self):
            # Khai báo biến
            # --- B1 & B3: Nghiên cứu đề bài và thiết lập Random ---
            def generate_problem():
                # Chọn tâm I và bán kính R sao cho R nguyên
                a = random.randint(-3, 3)
                b = random.randint(-3, 3)
                R = random.randint(3, 5)
                c_circle = a**2 + b**2 - R**2

                # d1 = -2a, d2 = -2b
                d1, d2 = -2*a, -2*b

                # Chọn đường thẳng d: x + y + c_line = 0
                c_line = random.randint(-5, 5)

                # Chọn m_target để MI đẹp (MI^2 là số nguyên)
                m_target = random.randint(-2, 2)
                MI2_val = (m_target - a)**2 + (-m_target - c_line - b)**2

                # Đảm bảo MI > R để có tiếp tuyến
                while MI2_val <= R**2:
                    m_target += 1
                    MI2_val = (m_target - a)**2 + (-m_target - c_line - b)**2

                MI_val = sqrt(MI2_val)
                AB_val = (2 * R * sqrt(MI2_val - R**2)) / MI_val
                AB_latex = latex(simplify(AB_val))

                # Giải tìm m
                m = symbols('m')
                coeff_a = 2
                coeff_b = 2 * (c_line + b - a)
                coeff_c = a**2 + (c_line + b)**2 - MI2_val
                roots = solve(coeff_a*m**2 + coeff_b*m + coeff_c, m)

                results = []
                for r in roots:
                    results.append(f"M({r}; {-r - c_line})")
                da = " \\, \\, \\text{hoặc} \\, \\,".join(results)

                # Đáp án nhiễu
                s = [
                    f"$M({m_target + 1}; {- (m_target + 1) - c_line})$",
                    f"$M({m_target - 1}; {- (m_target - 1) - c_line})$",
                    f"$M({m_target}; {m_target + c_line + 1})$",
                    f"$M(0; {c_line})$"
                ]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # --- Xử lý hiển thị dấu phương trình ---
                sign1 = "+" if d1 >= 0 else ""
                sign2 = "+" if d2 >= 0 else ""
                sign3 = "+" if c_circle >= 0 else ""
                pt_tron = f"x^2 + y^2 {sign1}{d1}x {sign2}{d2}y {sign3}{c_circle} = 0".replace("+ -", "- ").replace("- -", "+ ")

                noidungcauhoi = (f"Trong mặt phẳng với hệ tọa độ $Oxy$, cho đường tròn $(C): {pt_tron}$. "
                                 f"Gọi $I$ là tâm và $R$ là bán kính của $(C)$. Tìm tọa độ điểm $M$ thuộc đường thẳng "
                                 f"$d: x + y + {c_line} = 0$ sao cho từ $M$ kẻ được hai tiếp tuyến $MA, MB$ đến $(C)$ "
                                 f"($A, B$ là các tiếp điểm) thỏa mãn $AB = {AB_latex}$.")
                noidungcauhoi = noidungcauhoi.replace("+ -", "- ").replace("- -", "+ ")

                # --- LỜI GIẢI (Chú ý doubling braces {{ }} cho LaTeX) ---
                AH_latex = latex(simplify(AB_val/2))
                MI_latex = latex(simplify(MI_val))

                # Sử dụng rf để viết LaTeX tự nhiên hơn (raw f-string)
                # Sửa lại đoạn từ dòng 84 đến dòng 93
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
                    rf"Đường tròn $(C)$ có tâm $I({a}; {b})$, bán kính $R = {R}$. \\"
                    rf"Gọi $H = MI \cap AB$, suy ra $AH \perp MI$ và $AH = \frac{{AB}}{{2}} = {AH_latex}$. \\"
                    rf"Xét tam giác $MAI$ vuông tại $A$ có $AH$ là đường cao nên "
                    rf"$MI = \frac{{AI^2}}{{HI}} = \frac{{AI^2}}{{\sqrt{{AI^2 - AH^2}}}} = {MI_latex}$. \\"
                    rf"Do $M \in d$ nên $M(m; {-c_line} - m)$. Ta có: \\"
                    rf"$MI = {MI_latex} \Leftrightarrow \sqrt{{({a} - m)^2 + ({b} - ({-c_line} - m))^2}} = {MI_latex}$. \\"
                    rf"$\Leftrightarrow {coeff_a}m^2 + {coeff_b}m + {coeff_c} = 0$ \\"
                    rf"$\Leftrightarrow \left[ \begin{{array}}{{l}} m = {latex(roots[0])} \\ m = {latex(roots[1])} \end{{array}} \right.$ \\"
                    rf"Vậy ${da} $."
                )
                loigiai = loigiai.replace("+ -", "- ").replace("- -", "+ ")

                da_d = '\\True $' + da + '$'
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)
                return noidungcauhoi, list_1, loigiai

            noidungcauhoi, list_1, loigiai = generate_problem()

            # --- Xuất câu trắc nghiệm (Giữ nguyên định dạng mẫu) ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

