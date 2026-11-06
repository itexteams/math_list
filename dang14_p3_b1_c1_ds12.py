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


def bt_dang14_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                a_sym, b_sym, c_sym, d_sym = symbols('a b c d')

                while True:
                    x1 = randint(-3, 0)
                    x2 = x1 + randint(2, 5)

                    y1 = randint(-20, 20)
                    y2 = randint(-20, 20)

                    if y1 == y2 or x1 == 0 or x2 == 0:
                        continue

                    eq1 = a_sym * x1**3 + b_sym * x1**2 + c_sym * x1 + d_sym - y1
                    eq2 = a_sym * x2**3 + b_sym * x2**2 + c_sym * x2 + d_sym - y2
                    eq3 = 3 * a_sym * x1**2 + 2 * b_sym * x1 + c_sym
                    eq4 = 3 * a_sym * x2**2 + 2 * b_sym * x2 + c_sym

                    sol = solve((eq1, eq2, eq3, eq4), (a_sym, b_sym, c_sym, d_sym))

                    if sol:
                        a_val = sol[a_sym]
                        b_val = sol[b_sym]
                        c_val = sol[c_sym]
                        d_val = sol[d_sym]

                        if all(isinstance(val, (Integer, int)) or (isinstance(val, Rational) and val.q <= 4) for val in [a_val, b_val, c_val, d_val]):
                            break

                P_val = a_val + b_val + c_val + d_val
                kq = latex(P_val).replace('.', ',')

                du = ['$%s$' % (kq)]
                da = random.choice(du)

                s_candidates = [P_val + 2, P_val - 2, P_val + 5, P_val - 5, -P_val, P_val + randint(10, 20)]
                s = []
                for val in s_candidates:
                    val_str = latex(val).replace('.', ',')
                    s.append('$%s$' % (val_str))

                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Biết hàm số $y = ax^3 + bx^2 + cx + d$ có hai điểm cực trị là $(%s; %s)$ và $(%s; %s)$. Giá trị biểu thức $P = a + b + c + d$ bằng bao nhiêu?'''
                                 % (latex(x1), latex(y1), latex(x2), latex(y2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuẩn bị chuỗi hiển thị hệ phương trình rút gọn cực kỳ chuẩn chỉnh về mặt dấu toán học
                # Dòng 1: x1^3*a + x1^2*b + x1*c + d = y1
                eq1_a = '%sa' % (latex(x1**3))
                eq1_b = '+%sb' % (latex(x1**2)) if x1**2 >= 0 else '%sb' % (latex(x1**2))
                eq1_c = '+%sc' % (latex(x1)) if x1 >= 0 else '%sc' % (latex(x1))

                # Dòng 2: x2^3*a + x2^2*b + x2*c + d = y2
                eq2_a = '%sa' % (latex(x2**3))
                eq2_b = '+%sb' % (latex(x2**2)) if x2**2 >= 0 else '%sb' % (latex(x2**2))
                eq2_c = '+%sc' % (latex(x2)) if x2 >= 0 else '%sc' % (latex(x2))

                # Dòng 3: 3*x1^2*a + 2*x1*b + c = 0
                eq3_a = '%sa' % (latex(3 * x1**2))
                eq3_b = '+%sb' % (latex(2 * x1)) if 2 * x1 >= 0 else '%sb' % (latex(2 * x1))

                # Dòng 4: 3*x2^2*a + 2*x2*b + c = 0
                eq4_a = '%sa' % (latex(3 * x2**2))
                eq4_b = '+%sb' % (latex(2 * x2)) if 2 * x2 >= 0 else '%sb' % (latex(2 * x2))

                # Lời giải chi tiết
                loigiai = ('''Hàm số đã cho là $y = ax^3 + bx^2 + cx + d$.\\\\
                           Ta có đạo hàm: $y\' = 3ax^2 + 2bx + c$.\\\\
                           Vì đồ thị hàm số có hai điểm cực trị là $A(%s; %s)$ và $B(%s; %s)$ nên ta có hệ phương trình sau:\\\\
                           $$\\left\\{\\begin{aligned} & a \\cdot (%s)^3 + b \\cdot (%s)^2 + c \\cdot (%s) + d = %s \\\\ & a \\cdot (%s)^3 + b \\cdot (%s)^2 + c \\cdot (%s) + d = %s \\\\ & 3a \\cdot (%s)^2 + 2b \\cdot (%s) + c = 0 \\\\ & 3a \\cdot (%s)^2 + 2b \\cdot (%s) + c = 0 \\end{aligned}\\right. \\Leftrightarrow \\left\\{\\begin{aligned} & %s %s %s + d = %s \\\\ & %s %s %s + d = %s \\\\ & %s %s + c = 0 \\\\ & %s %s + c = 0 \\end{aligned}\\right.$$\\\\
                           Giải hệ phương trình bậc nhất bốn ẩn trên, ta thu được:\\\\
                           $a = %s$, $b = %s$, $c = %s$, $d = %s$.\\\\
                           Yêu cầu bài toán tính giá trị biểu thức $P = a + b + c + d$.\\\\
                           Thay các giá trị vừa tìm được vào biểu thức ta có:\\\\
                           $P = %s + %s + %s + %s = %s$.\\\\ 
                           Vậy giá trị của biểu thức $P$ là $%s$.'''
                           % (latex(x1), latex(y1), latex(x2), latex(y2),
                              latex(x1), latex(x1), latex(x1), latex(y1),
                              latex(x2), latex(x2), latex(x2), latex(y2),
                              latex(x1), latex(x1),
                              latex(x2), latex(x2),
                              eq1_a, eq1_b, eq1_c, latex(y1),
                              eq2_a, eq2_b, eq2_c, latex(y2),
                              eq3_a, eq3_b,
                              eq4_a, eq4_b,
                              latex(a_val), latex(b_val), latex(c_val), latex(d_val),
                              latex(a_val), latex(b_val), latex(c_val), latex(d_val), latex(P_val),
                              latex(P_val)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(P_val))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

