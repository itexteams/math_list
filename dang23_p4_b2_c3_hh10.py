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


def bt_dang23_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3-Suy nghĩ tìm cách random bài toán
                x0 = random.randint(-5, 5)
                y0 = random.randint(-5, 5)

                # Random hệ số a, b của d: ax + by + c = 0
                a = random.choice([i for i in range(-5, 6) if i != 0])
                b = random.choice([i for i in range(-5, 6) if i != 0])
                c = random.randint(-10, 10)

                # 1. Đường thẳng d' qua A và vuông góc d: bx - ay + C' = 0
                # C' = ay0 - bx0
                c_p = a*y0 - b*x0

                # 2. Tìm hình chiếu H là giao của d và d'
                deno = a**2 + b**2
                xh = Rational(b**2 * x0 - a*b * y0 - a*c, deno)
                yh = Rational(a**2 * y0 - a*b * x0 - b*c, deno)

                # 3. Tọa độ điểm đối xứng A'
                xa_p = 2*xh - x0
                ya_p = 2*yh - y0

                # Hàm định dạng phương trình chuẩn (Sửa lỗi - - thành +)
                def format_eq(h_a, h_b, h_c=None, side_zero=True):
                    # Xử lý hạng tử đầu tiên
                    res = f"{h_a}x".replace("1x", "x").replace("-1x", "-x")
                    # Xử lý hạng tử thứ hai (y)
                    if h_b > 0: res += f" + {h_b}y"
                    else: res += f" - {-h_b}y"
                    res = res.replace(" 1y", " y").replace("-1y", "-y")
                    # Xử lý hằng số tự do
                    if h_c is not None:
                        if h_c > 0: res += f" + {h_c}"
                        elif h_c < 0: res += f" - {-h_c}"
                        if side_zero: res += " = 0"
                    return res

                line_d = format_eq(a, b, c)
                # Phương trình d' dạng bx - ay + C = 0
                line_d_p = format_eq(b, -a, c_p)
                # Dạng đại số ở dòng đầu lời giải (bx - ay + C = 0)
                line_d_p_gen = format_eq(b, -a) + " + C = 0"

                # B2-Viết lại bài toán
                noidungcauhoi = "Cho đường thẳng $d: " + line_d + "$ và điểm $A(" + str(x0) + ";" + str(y0) + ")$. Tìm tọa độ điểm $A'$ đối xứng của $A$ qua $d$."

                # Lời giải chi tiết - Đã sửa lỗi hiển thị dấu
                loigiai = "Phương trình $d'$ đi qua $A$, vuông góc với $d$ có dạng $" + line_d_p_gen + "$. \\\\ "
                loigiai += "$d'$ qua $A(" + str(x0) + ";" + str(y0) + ")$ nên $" + latex(b*x0) + " - " + latex(a*y0) + " + C = 0 \\Rightarrow C = " + latex(c_p) + "$. \\\\ "
                loigiai += "Do đó $d': " + line_d_p + "$. \\\\ "
                loigiai += "Hình chiếu $H$ là giao điểm của $d$ và $d'$ nên có tọa độ thỏa mãn hệ \\\\ "
                loigiai += "$\\begin{cases} " + line_d + " \\\\ " + line_d_p + " \\end{cases} \\Leftrightarrow \\begin{cases} x = " + latex(xh) + " \\\\ y = " + latex(yh) + " \\end{cases}$. "
                loigiai += "Khi đó $H\\left(" + latex(xh) + "; " + latex(yh) + "\\right)$. \\\\ "
                loigiai += "$A'$ đối xứng với $A$ qua $d$ khi $H$ là trung điểm của $AA' \\Leftrightarrow \\begin{cases} x_{A'} = 2x_H - x_A = " + latex(xa_p) + " \\\\ y_{A'} = 2y_H - y_A = " + latex(ya_p) + " \\end{cases}$. \\\\ "
                loigiai += "Vậy $A'\\left(" + latex(xa_p) + "; " + latex(ya_p) + "\\right)$."

                # Đáp án
                da_d = "\\True $A'\\left(" + latex(xa_p) + "; " + latex(ya_p) + "\\right)$"
                s = [
                    "$A'\\left(" + latex(xh) + "; " + latex(yh) + "\\right)$",
                    "$A'\\left(" + latex(xa_p + 1) + "; " + latex(ya_p) + "\\right)$",
                    "$A'\\left(" + latex(ya_p) + "; " + latex(xa_p) + "\\right)$"
                ]
                random.shuffle(s)
                list_1 = [da_d, s[0], s[1], s[2]]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -','+').replace('- +','-')
            return content 

