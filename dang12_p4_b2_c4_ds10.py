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


def bt_dang12_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 3: RANDOM BÀI TOÁN ---
                k_val = random.randint(2, 6)
                a_sym = symbols('a')

                # Giải các trường hợp
                sol_th1 = solve(a_sym**2 - 2*a_sym + 2 - k_val, a_sym)
                res_th1 = [s for s in sol_th1 if s.evalf() < 0]

                sol_th2 = solve(-2*a_sym + 2 - k_val, a_sym)
                res_th2 = [s for s in sol_th2 if 0 <= s.evalf() <= 4]

                sol_th3 = solve(a_sym**2 - 10*a_sym + 18 - k_val, a_sym)
                res_th3 = [s for s in sol_th3 if s.evalf() > 4]

                # Xử lý chuỗi hiển thị cho các nghiệm được chọn để tránh lỗi backslash trong f-string
                txt_res1 = latex(res_th1[0]) if res_th1 else "vô nghiệm"
                txt_res2 = latex(sol_th2[0])
                if not res_th2:
                    txt_res2 += r" < 0 \text{ (không thỏa mãn)}"
                else:
                    txt_res2 = "a = " + latex(res_th2[0])

                txt_res3 = latex(res_th3[0]) if res_th3 else "vô nghiệm"

                # --- BƯỚC 4: ĐIỀU CHỈNH PHƯƠNG ÁN ---
                final_sols = res_th1 + res_th2 + res_th3
                da_dung_str = " \\,\\, \\text{hoặc} \\,\\, ".join(["a = " + latex(s) for s in final_sols])
                da = f"${da_dung_str}$"

                # Tạo danh sách các phương án sai
                s = [
                    f"$a = {latex(1 + sqrt(k_val - 1))}$",
                    f"$a = {latex(5 - sqrt(10 + k_val - 3))}$",
                    f"$a = {latex(1 - sqrt(k_val + 2))}$",
                    f"$a = {latex(1 + sqrt(k_val + 5))}$"
                ]
                s = [item for item in s if item != da]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Nội dung câu hỏi
                noidungcauhoi = (f"Tìm giá trị của $a$ sao cho giá trị nhỏ nhất của hàm số $y = f(x) = 4x^2 - 4ax + (a^2 - 2a + 2)$ trên đoạn $[0;2]$ bằng ${k_val}$.")

                # --- BƯỚC 2: VIẾT LỜI GIẢI (Đã sửa lỗi backslash) ---
                loigiai = (f'''Parabol có hệ số theo $x^2$ là $4 > 0$ nên bề lõm hướng lên. \\\\
            Hoành độ đỉnh $x_I = \\frac{{a}}{{2}}$. \\\\
            Nếu $\\frac{{a}}{{2}} < 0 \\Leftrightarrow a < 0$ thì $x_I < 0 < 2$. Suy ra $f(x)$ đồng biến trên $[0;2]$. \\\\
            Do đó $\\min f(x) = f(0) = a^2 - 2a + 2$. Theo yêu cầu bài toán: \\\\
            $a^2 - 2a + 2 = {k_val} \\Leftrightarrow a^2 - 2a - {k_val-2} = 0 \\Leftrightarrow a = {latex(sol_th1[0])}, a = {latex(sol_th1[1])}$.\\\\
            Vì $a < 0$ nên ta chọn $a = {txt_res1}$. \\\\
            Nếu $0 \\le \\frac{{a}}{{2}} \\le 2 \\Leftrightarrow 0 \\le a \\le 4$ thì $x_I \\in [0;2]$. Suy ra $f(x)$ đạt giá trị nhỏ nhất tại đỉnh. \\\\
            Do đó $\\min f(x) = f\\left(\\frac{{a}}{{2}}\\right) = -2a + 2$. Theo yêu cầu bài toán: \\\\
            $-2a + 2 = {k_val} \\Leftrightarrow a = {txt_res2}$. \\\\
            Nếu $\\frac{{a}}{{2}} > 2 \\Leftrightarrow a > 4$ thì $x_I > 2 > 0$. Suy ra $f(x)$ nghịch biến trên $[0;2]$. \\\\
            Do đó $\\min f(x) = f(2) = a^2 - 10a + 18$. Theo yêu cầu bài toán: \\\\
            $a^2 - 10a + 18 = {k_val} \\Leftrightarrow a^2 - 10a + {18-k_val} = 0 \\Leftrightarrow a = {latex(sol_th3[0])}, a = {latex(sol_th3[1])}$.\\\\
            Vì $a > 4$ nên ta chọn $a = {txt_res3}$. \\\\
            Vậy {da} thỏa mãn yêu cầu bài toán.''')

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

