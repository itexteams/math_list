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


def bt_dang50_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                x = symbols('x')

                # Tạo ngẫu nhiên nghiệm kép x0 cho mẫu số
                x0 = random.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5])

                # Tạo ngẫu nhiên hệ số A và D cho việc tách: A/(x-x0) + D/(x-x0)^2
                A = random.choice([2, 3, 4, 5, 6, -2, -3, -4, -5])
                D = random.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5])

                # Suy ra B sao cho Ax + B = A(x - x0) + D
                B = D - A * x0

                # Biểu thức mẫu số: (x-x0)^2
                den_expr_factored = (x - x0)**2
                den_expr_expanded = expand(den_expr_factored)

                # Biểu thức tử số: Ax + B
                num_expr = A * x + B

                # Chuỗi LaTeX của hàm số đề bài
                y_tex = "\\frac{%s}{%s}" % (latex(num_expr), latex(den_expr_expanded))

                # Xử lý chuỗi để in ra lời giải
                if x0 > 0:
                    x_x0_tex = "x - %s" % x0
                else:
                    x_x0_tex = "x + %s" % abs(x0)

                if D > 0:
                    split_num_tex = "%s(%s) + %s" % (A, x_x0_tex, D)
                    term1_tex = "\\frac{%s}{%s}" % (A, x_x0_tex) if A > 0 else "-\\frac{%s}{%s}" % (abs(A), x_x0_tex)
                    term2_tex = "+ \\frac{%s}{%s}" % (D, latex(den_expr_factored))
                else:
                    split_num_tex = "%s(%s) - %s" % (A, x_x0_tex, abs(D))
                    term1_tex = "\\frac{%s}{%s}" % (A, x_x0_tex) if A > 0 else "-\\frac{%s}{%s}" % (abs(A), x_x0_tex)
                    term2_tex = "- \\frac{%s}{%s}" % (abs(D), latex(den_expr_factored))

                split_tex = "%s %s" % (term1_tex, term2_tex)

                # Tính nguyên hàm đúng: A*ln|x - x0| - D/(x - x0)
                F_correct_expr = A * log(Abs(x - x0)) - Rational(D, 1) / (x - x0)
                F_correct_tex = latex(F_correct_expr)

                # CÁC PHƯƠNG ÁN NHIỄU (SAI)
                # Nhiễu 1: Tính sai dấu của phần D
                F_w1_expr = A * log(Abs(x - x0)) + Rational(D, 1) / (x - x0)
                F_w1_tex = latex(F_w1_expr) + " + C"

                # Nhiễu 2: Quên lấy nguyên hàm của mẫu bình phương (vẫn để nguyên mũ 2)
                F_w2_expr = A * log(Abs(x - x0)) - Rational(D, 1) / den_expr_factored
                F_w2_tex = latex(F_w2_expr) + " + C"

                # Nhiễu 3: Sai dấu phần A và sai dấu phần D
                F_w3_expr = -A * log(Abs(x - x0)) + Rational(D, 1) / (x - x0)
                F_w3_tex = latex(F_w3_expr) + " + C"

                # Nhiễu 4: Quên + C
                F_w4_tex = latex(F_correct_expr)

                # Đưa đáp án đúng vào
                du = ['$%s + C$' % (F_correct_tex)]
                da = random.choice(du)

                # Danh sách các câu sai
                s_candidates = [
                    '$%s$' % (F_w1_tex),
                    '$%s$' % (F_w2_tex),
                    '$%s$' % (F_w3_tex),
                    '$%s$' % (F_w4_tex)
                ]

                # Lọc phương án trùng với đáp án đúng
                s = []
                for ans in s_candidates:
                    if ans not in s and ans != da and ans != '$%s + C$' % (F_correct_tex):
                        s.append(ans)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('Tìm nguyên hàm của hàm số $y = %s$.' % (y_tex))

                # Đánh dấu đáp án đúng/sai
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Ta có $y = %s = \\frac{%s}{%s} = %s$. \\\\ '
                           'Họ tất cả các nguyên hàm của hàm số đã cho là: \\\\ '
                           '$\\int \\left( %s \\right) \\mathrm{d}x = %s + C$.' 
                           % (y_tex, split_num_tex, latex(den_expr_factored), split_tex, split_tex, F_correct_tex))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n').replace('\\log', '\\ln')
            return content 

