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


def bt_dang26_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Hàm số có dạng y = (ax + b) / (cx + d)
            # Để đồ thị (C) cắt Ox, Oy và có tiếp tuyến, ta cần ad - bc != 0 và c != 0
            while True:
                a = random.randint(-3, 5)
                b = random.randint(-5, 5)
                c = random.choice([-2, -1, 1, 2])
                d = random.randint(-5, 5)
                if a*d - b*c != 0:
                    break

            k_ratio = 4 # OA = 4OB

            # Định nghĩa hàm số
            y = (a*x + b) / (c*x + d)
            y_prime = diff(y, x)

            # Hệ số góc tiếp tuyến f'(x0)
            # OA = k*OB => |tan A| = OB/OA = 1/k
            # Hệ số góc m = +- 1/k. 
            # Tuy nhiên, f'(x0) = (ad-bc)/(cx0+d)^2 luôn cùng dấu với (ad-bc)
            m_val = Rational(1, k_ratio)

            # Giải phương trình f'(x0) = m_val hoặc f'(x0) = -m_val
            sol_x0_pos = solve(y_prime - m_val, x)
            sol_x0_neg = solve(y_prime + m_val, x)

            # Lọc các nghiệm thực và tính tiếp tuyến
            tiep_tuyen_list = []
            x0_list = sol_x0_pos + sol_x0_neg

            for x0 in x0_list:
                if x0.is_real:
                    y0 = y.subs(x, x0)
                    m = y_prime.subs(x, x0)
                    # Phương trình: y = m(x - x0) + y0 => y = mx - m*x0 + y0
                    b_line = simplify(-m*x0 + y0)

                    # Format phương trình y = mx + b
                    m_tex = latex(m)
                    b_tex = latex(b_line)
                    sign = "+" if b_line > 0 else ""
                    if b_line == 0: sign = ""; b_tex = ""

                    line_eq = f"y = {m_tex}x {sign} {b_tex}".replace("+ -", "- ")
                    tiep_tuyen_list.append((x0, y0, m, line_eq))

            # B2: Viết lại nội dung theo mẫu
            noidungcauhoi = (f"Cho hàm số $y = {latex(y)}$ có đồ thị $(C)$. Viết phương trình tiếp tuyến của $(C)$ "
                             f"cắt trục $Ox, Oy$ lần lượt tại hai điểm $A$ và $B$ thỏa mãn điều kiện $OA = {k_ratio}OB$.")

            # Giả sử lấy kết quả từ các nghiệm tìm được để làm đáp án đúng
            if tiep_tuyen_list:
                da_dung_str = " và ".join([f"${item[3]}$" for item in tiep_tuyen_list])
                da_d = f"\\True {da_dung_str}"

                # Tạo đáp án nhiễu (thay đổi hệ số tự do hoặc hệ số góc)
                da_s1 = f"$y = {latex(-m_val)}x + 1$ và $y = {latex(-m_val)}x - 2$"
                da_s2 = f"$y = {latex(m_val)}x + {latex(Rational(1,2))}$"
                da_s3 = f"$y = -{k_ratio}x + 3$"
            else:
                da_d = "\\True Không có tiếp tuyến thỏa mãn"
                da_s1 = "$y = x+1$"; da_s2 = "$y = 2x$"; da_s3 = "$y = -x$"

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = f"Giả sử tiếp tuyến của $(C)$ tại $M(x_0; y_0)$ cắt $Ox$ tại $A$, $Oy$ tại $B$ sao cho $OA = {k_ratio}OB$. \\\\"
            loigiai += f"Do tam giác $OAB$ vuông tại $O$ nên $\\tan A = \\frac{{OB}}{{OA}} = \\frac{1}{{{k_ratio}}}$. \\\\"
            loigiai += f"Suy ra hệ số góc tiếp tuyến bằng $\\frac{1}{{{k_ratio}}}$ hoặc $-\\frac{1}{{{k_ratio}}}$. \\\\"
            loigiai += f"Ta có $y' = {latex(y_prime)}$. \\\\"

            if tiep_tuyen_list:
                m_fixed = tiep_tuyen_list[0][2]
                loigiai += f"Dựa vào biểu thức $y'$, ta có phương trình: ${latex(y_prime)} = {latex(m_fixed)}$. \\\\"
                loigiai += f"Giải phương trình ta được " + " hoặc ".join([f"$x_0 = {latex(item[0])}$" for item in tiep_tuyen_list]) + ". \\\\"
                for item in tiep_tuyen_list:
                    loigiai += f"Với $x_0 = {latex(item[0])} \\Rightarrow y_0 = {latex(item[1])}$, phương trình tiếp tuyến là: ${item[3]}$. \\\\"
            else:
                loigiai += "Không tìm thấy giá trị $x_0$ thỏa mãn phương trình hệ số góc."

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

