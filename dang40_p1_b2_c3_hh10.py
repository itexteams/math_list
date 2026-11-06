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


def bt_dang40_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Tạo các tham số ngẫu nhiên
                # Chọn tọa độ A nguyên để bài toán dễ theo dõi
                xa, ya = randint(-4, 4), randint(-4, 4)
                A = Point(xa, ya)

                # Hàm tạo đường thẳng đi qua 1 điểm và không đi qua điểm khác (để tránh A nằm trên phân giác)
                def generate_bisector(pt_exclude):
                    while True:
                        # Chọn hệ số a, b nhỏ
                        a = randint(-3, 3)
                        b = randint(-3, 3)
                        if a == 0 and b == 0: continue
                        # Chọn c sao cho pt_exclude không thuộc đường thẳng
                        c = randint(-5, 5)
                        if a * pt_exclude.x + b * pt_exclude.y + c != 0:
                            return a, b, c

                a1, b1, c1 = generate_bisector(A)
                d1_eq = a1*x + b1*y + c1

                a2, b2, c2 = generate_bisector(A)
                # Đảm bảo d2 không trùng hoặc song song d1
                while a1*b2 == a2*b1:
                    a2, b2, c2 = generate_bisector(A)
                d2_eq = a2*x + b2*y + c2

                # Hàm tìm điểm đối xứng dùng linsolve để tránh lỗi TypeError
                def get_reflection(P, a, b, c):
                    # Hệ phương trình: 
                    # 1. Trung điểm thuộc đường thẳng
                    # 2. Vector PP' cùng phương pháp tuyến (a, b)
                    eq1 = a * (x + P.x)/2 + b * (y + P.y)/2 + c
                    eq2 = b * (x - P.x) - a * (y - P.y)
                    sol = list(linsolve([eq1, eq2], (x, y)))
                    return Point(sol[0][0], sol[0][1])

                A1 = get_reflection(A, a1, b1, c1)
                A2 = get_reflection(A, a2, b2, c2)

                # Viết phương trình BC đi qua A1 và A2
                dx = A2.x - A1.x
                dy_val = A2.y - A1.y
                if dx == 0:
                    bc_raw = x - A1.x
                else:
                    bc_raw = (y - A1.y)*dx - (x - A1.x)*dy_val

                # Rút gọn phương trình BC cho đẹp
                bc_poly = Poly(bc_raw, x, y)
                coeffs = bc_poly.coeffs()
                common = gcd(coeffs)
                bc_eq_final = bc_raw / common
                if Poly(bc_eq_final, x, y).coeffs()[0] < 0:
                    bc_eq_final = -bc_eq_final

                # Tìm B = d1 giao BC
                sol_B = list(linsolve([d1_eq, bc_eq_final], (x, y)))
                bx, by = sol_B[0]

                # Tìm C = d2 giao BC
                sol_C = list(linsolve([d2_eq, bc_eq_final], (x, y)))
                cx, cy = sol_C[0]

                # Bước 3: Định dạng hiển thị
                def fmt_coord(pt_x, pt_y):
                    return "\\left(" + latex(pt_x) + ";" + latex(pt_y) + "\\right)"

                ans_correct = "$B" + fmt_coord(bx, by) + "$ và $C" + fmt_coord(cx, cy) + "$"

                # Tạo đáp án nhiễu
                s = [
                    "$B" + fmt_coord(bx + 1, by) + "$ và $C" + fmt_coord(cx, cy - 1) + "$",
                    "$B" + fmt_coord(bx, by + 1) + "$ và $C" + fmt_coord(cx - 1, cy) + "$",
                    "$B" + fmt_coord(by, bx) + "$ và $C" + fmt_coord(cy, cx) + "$",
                    "$B" + fmt_coord(-bx, -by) + "$ và $C" + fmt_coord(-cx, -cy) + "$"
                ]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho tam giác $ABC$ có $A\\left(%s;%s\\right)$ và hai đường phân giác trong của góc $B$ và $C$ có phương trình lần lượt là $d_1:%s=0$ và $d_2:%s=0$. Tọa độ điểm $B$ và $C$ là'''
                                 % (latex(xa), latex(ya), latex(d1_eq), latex(d2_eq)))

                # Làm sạch dấu cho câu hỏi
                noidungcauhoi = noidungcauhoi.replace('+ -', '-').replace('- -', '+')

                # Nội dung lời giải chi tiết
                loigiai = ('''Gọi $A_1$ là điểm đối xứng của $A$ qua phân giác $d_1$. \\\\
            Suy ra tọa độ điểm $A_1(x; y)$ là nghiệm của hệ: \\\\
            $\\begin{cases} %s \\cdot \\frac{x+%s}{2} + %s \\cdot \\frac{y+%s}{2} + %s = 0 \\\\ %s(x-%s) - %s(y-%s) = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$.  \\\\ Ta được $A_1%s$. \\\\
            Gọi $A_2$ là điểm đối xứng của $A$ qua phân giác $d_2$, tương tự ta tính được $A_2%s$. \\\\
            Đường thẳng $BC$ đi qua hai điểm $A_1, A_2$ nên $BC$ có phương trình: $%s=0$. \\\\
            Vì $B = d_1 \\cap BC$ nên tọa độ của $B$ là nghiệm của hệ $\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$. \\\\ Ta được $B%s$. \\\\
            Tương tự $C = d_2 \\cap BC$ nên ta được $C%s$.'''
                           % (latex(a1), latex(-xa), latex(b1), latex(-ya), latex(c1),
                              latex(b1), latex(xa), latex(a1), latex(ya),
                              latex(A1.x), latex(A1.y), fmt_coord(A1.x, A1.y),
                              fmt_coord(A2.x, A2.y), latex(bc_eq_final),
                              latex(d1_eq), latex(bc_eq_final),
                              latex(bx), latex(by), fmt_coord(bx, by),
                              fmt_coord(cx, cy)
                             ))

                # Làm sạch dấu cho lời giải
                loigiai = loigiai.replace('+ -', '-').replace('- -', '+')

                # Xuất câu trắc nghiệm
                da_d = '\\True ' + ans_correct
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

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

