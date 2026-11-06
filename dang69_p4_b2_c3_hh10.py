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


def bt_dang69_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo hệ số ngẫu nhiên cho d1, d2 để có giao điểm
                while True:
                    a1, b1, c1 = randint(-5, 5), randint(-5, 5), randint(-10, 10)
                    a2, b2, c2 = randint(-5, 5), randint(-5, 5), randint(-10, 10)
                    # Loại bỏ trường hợp hệ số bằng 0 ở cả x và y hoặc d1 song song d2
                    if (a1**2 + b1**2 != 0) and (a2**2 + b2**2 != 0) and (a1*b2 - a2*b1 != 0):
                        break

                # Tạo hệ số cho d3
                while True:
                    a3, b3, c3 = randint(-5, 5), randint(-5, 5), randint(-10, 10)
                    if a3**2 + b3**2 != 0:
                        break

                # Biểu thức các đường thẳng (Sử dụng sympy để tự động xử lý hệ số 1)
                expr_d1 = a1*x + b1*y + c1
                expr_d2 = a2*x + b2*y + c2
                expr_d3 = a3*x + b3*y + c3

                # Giải hệ phương trình tìm giao điểm A
                sol = solve([expr_d1, expr_d2], (x, y))
                xA, yA = sol[x], sol[y]

                # Đường thẳng d song song d3 có dạng: a3*x + b3*y + c = 0
                # Thay tọa độ A vào: a3*xA + b3*yA + c = 0 => c = -(a3*xA + b3*yA)
                c_temp = -(a3*xA + b3*yA)

                # Điều kiện song song (c khác c3)
                if c_temp == c3:
                    c3 = c3 + 1
                    expr_d3 = a3*x + b3*y + c3

                # Đưa về dạng số nguyên tối giản (nhân với mẫu số chung của c_temp)
                denom = c_temp.q if hasattr(c_temp, 'q') else 1
                A_fin, B_fin, C_fin = a3*denom, b3*denom, c_temp*denom

                # Đảm bảo hệ số đầu tiên dương cho đẹp
                if A_fin < 0 or (A_fin == 0 and B_fin < 0):
                    A_fin, B_fin, C_fin = -A_fin, -B_fin, -C_fin

                res_expr = A_fin*x + B_fin*y + C_fin

                # Các đáp án
                da_d = '\\True $%s = 0$' % (latex(res_expr))

                # Tạo phương án sai bằng cách đổi dấu hoặc thay đổi hệ số tự do
                s = [
                    '$%s = 0$' % (latex(A_fin*x + B_fin*y - C_fin)),
                    '$%s = 0$' % (latex(A_fin*x - B_fin*y + C_fin)),
                    '$%s = 0$' % (latex(A_fin*x + B_fin*y + C_fin + 5)),
                ]
                random.shuffle(s)

                # Câu hỏi
                noidungcauhoi = ('''Cho ba đường thẳng $d_1: %s = 0$, $d_2: %s = 0$, $d_3: %s = 0$. Lập phương trình đường thẳng $d$ đi qua giao điểm của $d_1$ và $d_2$, và song song với $d_3$.'''
                                 %(latex(expr_d1), latex(expr_d2), latex(expr_d3)))

                list_1 = [da_d, s[0], s[1], s[2]]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''$\\begin{cases} d_1: %s = 0 \\\\ d_2: %s = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases} \\rightarrow d_1 \\cap d_2 = A\\left( %s; %s \\right)$. Ta có \\\\
                           $\\begin{cases} A \\in d \\\\ d \\parallel d_3: %s = 0 \\end{cases} \\rightarrow \\begin{cases} A \\in d \\\\ d: %s + c = 0 \\, (c \\neq %s) \\end{cases} \\rightarrow %s \\cdot \\left(%s\\right) + %s \\cdot \\left(%s\\right) + c = 0 \\Leftrightarrow c = %s$. \\\\
                           Vậy $d: %s + %s = 0 \\Leftrightarrow d: %s = 0$.'''
                           %(latex(expr_d1), latex(expr_d2), latex(xA), latex(yA), latex(xA), latex(yA),
                             latex(expr_d3), latex(a3*x + b3*y), latex(c3),
                             latex(a3), latex(xA), latex(b3), latex(yA), latex(c_temp),
                             latex(a3*x + b3*y), latex(c_temp), latex(res_expr)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

