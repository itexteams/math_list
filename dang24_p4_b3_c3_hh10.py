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


def bt_dang24_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            m = symbols('m')

            def generate_problem():
                # B3: Suy nghĩ tìm cách random bài toán
                # Để m hữu tỉ và bài toán "đẹp", ta cần d(I, d) = R/sqrt(2) = k (với k là số hữu tỉ)
                # Ta chọn R^2 = 2*k^2. Chọn k = 1 => R^2 = 2.
                # Phương trình khoảng cách: |A + mB| / sqrt(1 + m^2) = k
                # => (B^2 - k^2)m^2 + 2ABm + (A^2 - k^2) = 0
                # Để m đẹp, Delta' = k^2(A^2 + B^2 - k^2) phải là số chính phương.

                attempts = 0
                while attempts < 1000:
                    k = random.choice([1, 2]) # k = R/sqrt(2)
                    R2 = 2 * (k**2)

                    # Random tọa độ tâm I(xI, yI)
                    xI = random.randint(-4, 4)
                    yI = random.randint(-4, 4)

                    # Hệ số đường thẳng d: x + m(y - y0) + x0 = 0 <=> x + my - my0 + x0 = 0
                    # Gọi A = xI + x0, B = yI - y0
                    # Ta cần k^2(A^2 + B^2 - k^2) là số chính phương
                    A = random.randint(-5, 5)
                    B = random.randint(-5, 5)

                    delta_val = k**2 * (A**2 + B**2 - k**2)
                    if delta_val > 0 and math.isqrt(delta_val)**2 == delta_val:
                        # Tìm x0, y0 từ A, B
                        x0 = A - xI
                        y0 = yI - B

                        # Kiểm tra xem có tạo ra được phương trình m không (tránh trường hợp vô nghiệm hoặc m trùng nhau quá đơn giản)
                        coeffs = [B**2 - k**2, 2*A*B, A**2 - k**2]
                        solutions = solve(coeffs[0]*m**2 + coeffs[1]*m + coeffs[2], m)

                        if len(solutions) == 2 and solutions[0] != solutions[1]:
                            # Tính các hệ số của đường tròn: x^2 + y^2 + 2ax + 2by + c = 0
                            # (x-xI)^2 + (y-yI)^2 = R^2  => x^2 + y^2 - 2xIx - 2yIy + (xI^2 + yI^2 - R^2) = 0
                            c_circle = xI**2 + yI**2 - R2

                            # Biểu diễn đường thẳng d: x + my + (x0 - m*y0) = 0
                            # Trong đề bài mẫu: x + my - 2m + 3 = 0 => x0 = 3, y0 = 2
                            return xI, yI, R2, x0, y0, solutions, c_circle
                    attempts += 1

            # Khởi tạo dữ liệu
            xI, yI, R2, x0, y0, solutions, c_circle = generate_problem()

            # B1 & B2: Thiết lập nội dung đề bài và lời giải
            R = sqrt(R2)
            dist_val = R/sqrt(2)

            # Định dạng hiển thị phương trình đường thẳng d
            # d: x + my + (x0) - (y0)m = 0
            line_const = x0
            line_m_coeff = -y0

            def format_exp(val, var="", first=False):
                if val == 0: return ""
                if val > 0:
                    res = "+{0}".format(latex(val)) if not first else "{0}".format(latex(val))
                else:
                    res = "{0}".format(latex(val))
                return res + var

            # Tạo chuỗi phương trình
            str_circle = f"x^2 + y^2 {format_exp(-2*xI, 'x')} {format_exp(-2*yI, 'y')} {format_exp(c_circle, '', False)} = 0"
            str_line = f"x + my {format_exp(line_m_coeff, 'm')} {format_exp(line_const, '', False)} = 0"

            noidungcauhoi = (f"Trong mặt phẳng với hệ trục tọa độ $Oxy$, cho đường tròn $(C): {str_circle}$ và đường thẳng $d: {str_line}$. Gọi $I$ là tâm của $(C)$. Tìm $m$ để $d$ cắt $(C)$ tại hai điểm phân biệt $A, B$ thỏa mãn diện tích $\\Delta IAB$ lớn nhất.")

            # Lời giải chi tiết
            # Nội dung lời giải (Sử dụng r"..." và .format)
            loigiai = (r"Đường tròn $(C)$ có tâm $I({0}; {1})$ và bán kính $R = {2}$.\\" 
                       r"$d$ cắt $(C)$ tại hai điểm phân biệt khi $d(I, d) < R$.\\" 
                       r"Ta có $S_{{\Delta IAB}} = \frac{{1}}{{2}} IA \cdot IB \cdot \sin \widehat{{AIB}} = \frac{{1}}{{2}} R^2 \sin \widehat{{AIB}} = {3} \sin \widehat{{AIB}}$.\\" 
                       r"Do đó $S_{{\Delta IAB}}$ lớn nhất khi $\sin \widehat{{AIB}} = 1 \Leftrightarrow \widehat{{AIB}} = 90^\circ$.\\" 
                       r"Khi đó tam giác $IAB$ vuông cân tại $I$ nên khoảng cách từ $I$ đến $d$ là:\\" 
                       r"$IH = \frac{{IA}}{{\sqrt{{2}}}} = \frac{{{2}}}{{\sqrt{{2}}}} = {4}$.\\" 
                       r"Ta có $d(I, d) = {4} \Leftrightarrow \frac{{|{0} + m({1}) {5} {6}|}}{{\sqrt{{1+m^2}}}} = {4}$ \\" 
                       r"$\Leftrightarrow \frac{{|{7} {8}|}}{{\sqrt{{1+m^2}}}} = {4}$ \\" 
                       r"$\Leftrightarrow ({7} {8})^2 = {9}(1+m^2)$ \\" 
                       r"Giải phương trình trên ta được $\left[ \begin{{array}}{{l}} m = {10} \\ m = {11} \end{{array}} \right.$ (thỏa mãn điều kiện $d(I, d) < R$).").format(
                           xI, yI, latex(R), latex(Rational(R2, 2)), latex(dist_val), 
                           format_exp(line_m_coeff, 'm'), format_exp(line_const, '', False),
                           latex(xI + line_const), format_exp(yI + line_m_coeff, 'm', False),
                           latex(dist_val**2), latex(solutions[0]), latex(solutions[1])
                       )

            # Các đáp án trắc nghiệm
            da_dung = "$m = {0}; m = {1}$".format(latex(solutions[0]), latex(solutions[1]))
            distractors = [
                f"$m = {latex(-solutions[0])}; m = {latex(solutions[1])}$",
                f"$m = {latex(solutions[0])}; m = {latex(-solutions[1])}$",
                f"$m = 1; m = {latex(solutions[0]+1)}$",
                f"$m = 0; m = {latex(solutions[1]-2)}$",
                f"$m = {latex(solutions[0])}$",
                f"Không có giá trị $m$"
            ]
            random.shuffle(distractors)
            list_1 = ['\\True ' + da_dung, distractors[0], distractors[1], distractors[2]]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

