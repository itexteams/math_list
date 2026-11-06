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


def bt_dang22_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Để giải bài toán dễ dàng, ta chọn a, b sao cho vector chỉ phương u(-b; a) đẹp
            a = random.randint(1, 5)
            b = -random.randint(1, 5) # Chọn b âm để giống dạng 4x - 3y
            c = random.randint(1, 10)

            # Điểm E(xE, yE) và F(xF, yF)
            xE = random.randint(-5, 5)
            yE = random.randint(-5, 5)
            xF = random.randint(-5, 5)
            yF = random.randint(-5, 5)

            # Đảm bảo E và F không trùng nhau để bài toán có nghĩa
            while xE == xF and yE == yF:
                xF = random.randint(-5, 5)
                yF = random.randint(-5, 5)

            # Tìm một điểm M(x0, y0) thuộc Delta để viết phương trình tham số
            # Giải ax + by + c = 0 => chọn x0 sao cho (c + a*x0) chia hết cho |b| hoặc dùng Rational
            x0 = 0
            y0 = Rational(-c - a*x0, b)

            # Vector chỉ phương u = (-b, a)
            u1, u2 = -b, a

            # Phương trình tham số của Delta: x = x0 + u1*t, y = y0 + u2*t
            t = symbols('t')
            xB = x0 + u1*t
            yB = y0 + u2*t

            # Điều kiện B cách đều E và F: EB^2 = FB^2
            eq = (xB - xE)**2 + (yB - yE)**2 - ((xB - xF)**2 + (yB - yF)**2)
            sol_t = solve(eq, t)

            if sol_t:
                t_val = sol_t[0]
                xB_val = xB.subs(t, t_val)
                yB_val = yB.subs(t, t_val)

                # Tạo đáp án đúng
                da_dung = f"$B\\left({latex(xB_val)}; {latex(yB_val)}\\right)$"

                # Tạo các đáp án nhiễu
                s = [
                    f"$B\\left({latex(xB_val + 1)}; {latex(yB_val)}\\right)$",
                    f"$B\\left({latex(xB_val)}; {latex(yB_val + 1)}\\right)$",
                    f"$B\\left({latex(xB_val - 1)}; {latex(yB_val - 2)}\\right)$",
                    f"$B\\left({latex(yB_val)}; {latex(xB_val)}\\right)$"
                ]
                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Nội dung câu hỏi
                # Xử lý dấu cho phương trình đường thẳng
                b_str = f"- {abs(b)}y" if b < 0 else f"+ {b}y"
                c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"
                dt_str = f"{a}x {b_str} {c_str} = 0"

                noidungcauhoi = (f"Cho đường thẳng $\\Delta: {dt_str}$. "
                                 f"Tìm điểm $B$ thuộc đường thẳng $\\Delta$ và cách đều hai điểm $E({xE};{yE}), F({xF};{yF})$.")

                # Nội dung lời giải
                # Xử lý trình bày vector và điểm M
                u_vec = f"\\vec{{u}}({u1};{u2})"
                pt_ts = f"\\begin{{cases}} x = {latex(xB)} \\\\ y = {latex(yB)} \\end{{cases}}"

                loigiai = (f"Dễ thấy $M({x0};{latex(y0)})$ thuộc đường thẳng $\\Delta$ và ${u_vec}$ là một vectơ chỉ phương của $\\Delta$ nên có "
                           f"phương trình tham số là ${pt_ts}$.\\\\ "
                           f"Vì $B \\in \\Delta$ nên $B({latex(xB)}; {latex(yB)})$. Điểm $B$ cách đều hai điểm $E({xE};{yE}), F({xF};{yF})$ suy ra:\\\\ "
                           f"$EB^2 = FB^2 \\Leftrightarrow ({latex(xB - xE)})^2 + ({latex(yB - yE)})^2 = ({latex(xB - xF)})^2 + ({latex(yB - yF)})^2$\\\\ "
                           f"$\\Leftrightarrow t = {latex(t_val)}$.\\\\ "
                           f"Suy ra $B\\left({latex(xB_val)}; {latex(yB_val)}\\right)$.")

                # Xuất câu trắc nghiệm
                da_d = '\\True ' + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n').replace('1x','x').replace('1y','y')
            return content 

