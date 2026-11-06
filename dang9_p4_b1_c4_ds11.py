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


def bt_dang9_p4_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                n = symbols('n')

                # --- B3: Suy nghĩ tìm cách random bài toán ---

                # 1. Tử số: Một biểu thức lượng giác bị chặn
                # Tổng quát: a*cos(n) + b*sin(n) + c
                a = randint(1, 5)
                b = randint(1, 5)
                c = randint(-2, 2)

                # Chuẩn bị chuỗi LaTeX cho hằng số c
                if c == 0:
                    c_str = ''
                elif c > 0:
                    c_str = f'+ {c}'
                else:
                    c_str = f'{c}'

                # Chọn biểu thức tử số ngẫu nhiên
                list_numerator = [
                    (a*cos(n) + b*sin(n), f'{a}\\cos n + {b}\\sin n'), # sin/cos
                    (a*sin(n) + c, f'{a}\\sin n {c_str}'),           # sin + const
                    (a*cos(n) + c, f'{a}\\cos n {c_str}'),           # cos + const
                    (a*cos(n) + b*sin(n) + c, f'{a}\\cos n + {b}\\sin n {c_str}') # tổng quát
                ]
                numerator_expr, numerator_latex_str = random.choice(list_numerator)

                # Tính giá trị chặn trên cụ thể cho từng trường hợp (|Tử số| <= limit_bound)
                if numerator_expr == a*cos(n) + b*sin(n):
                    limit_bound = sqrt(a**2 + b**2)
                elif numerator_expr == a*sin(n) + c:
                    limit_bound = Abs(a) + Abs(c)
                elif numerator_expr == a*cos(n) + c:
                    limit_bound = Abs(a) + Abs(c)
                else: # a*cos(n) + b*sin(n) + c
                    limit_bound = sqrt(a**2 + b**2) + Abs(c)

                limit_bound_latex = latex(limit_bound) # Giá trị chặn trên (dạng LaTeX)


                # 2. Mẫu số: Đa thức bậc >= 2 tiến ra vô cùng
                d = randint(2, 5) # Bậc của đa thức
                e = randint(1, 3) # Hệ số của n^d
                f = randint(1, 5) # Hằng số
                denominator_expr = e*n**d + f
                denominator_latex_str = latex(denominator_expr)

                # 3. Hàm số cần tính giới hạn
                limit_expr = numerator_expr / denominator_expr

                # --- B2: Viết lại bài toán theo mẫu code python (với các biến ngẫu nhiên) ---

                # Câu hỏi
                noidungcauhoi = (f'''Tính giá trị của $\\lim_{{n \\to +\\infty}} \\frac{{{numerator_latex_str}}}{{{denominator_latex_str}}}$.''')

                # Đáp án đúng (luôn là 0)
                kq = 0
                da = '0'

                # Nội dung lời giải
                loigiai = (f'''Ta có: \\\\
                Vì $|\\cos n| \\le 1$ và $|\\sin n| \\le 1$ nên tử số bị chặn: \\\\
                $|{numerator_latex_str}| \\le {limit_bound_latex}$. \\\\
                Khi đó, ta có bất đẳng thức: \\\\
                $$0 \\le \\left|\\frac{{{numerator_latex_str}}}{{{denominator_latex_str}}}\\right| \\le \\frac{{|{numerator_latex_str}|}}{{{denominator_latex_str}}} \\le \\frac{{{limit_bound_latex}}}{{{denominator_latex_str}}}.$$
                Mặt khác, ta thấy: \\\\
                $$\\lim_{{n \\to +\\infty}} 0 = 0$$
                $$\\lim_{{n \\to +\\infty}} \\frac{{{limit_bound_latex}}}{{{denominator_latex_str}}} = 0$$
                (Vì $\\lim_{{n \\to +\\infty}} {denominator_latex_str} = +\\infty$). \\\\
                Theo \\textbf{{Định lý kẹp}} (hoặc Nguyên lý giới hạn trung gian), ta suy ra: \\\\
                $$\\lim_{{n \\to +\\infty}} \\frac{{{numerator_latex_str}}}{{{denominator_latex_str}}} = 0.$$''')


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('phtramc', '\\%s')
            return content

