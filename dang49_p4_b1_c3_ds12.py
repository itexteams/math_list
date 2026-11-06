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


def bt_dang49_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                x = symbols('x')

                # Tạo ngẫu nhiên 2 nghiệm nguyên phân biệt cho mẫu số
                roots = random.sample([-4, -3, -2, -1, 1, 2, 3, 4], 2)
                x1, x2 = roots[0], roots[1]

                # Tạo ngẫu nhiên hệ số A, B cho quá trình tách phân thức: A/(x-x1) + B/(x-x2)
                # Lấy |A| != |B| để các phương án nhiễu hoán vị không bị trùng lặp
                A = random.choice([2, 3, 4, 5, -2, -3, -4, -5])
                B = random.choice([1, 6, -1, -6])

                # Biểu thức mẫu số: (x-x1)(x-x2)
                den_expr_factored = (x - x1) * (x - x2)
                den_expr_expanded = expand(den_expr_factored)

                # Biểu thức tử số: A*(x-x2) + B*(x-x1)
                num_expr = A * (x - x2) + B * (x - x1)
                num_expr_expanded = expand(num_expr)

                # Chuỗi LaTeX của hàm số đề bài
                y_tex = "\\frac{%s}{%s}" % (latex(num_expr_expanded), latex(den_expr_expanded))

                # Hàm hỗ trợ định dạng chuỗi tách phân thức
                term1_tex = "\\frac{%s}{%s}" % (A, latex(x - x1)) if A > 0 else "-\\frac{%s}{%s}" % (abs(A), latex(x - x1))
                term2_tex = "+ \\frac{%s}{%s}" % (B, latex(x - x2)) if B > 0 else "- \\frac{%s}{%s}" % (abs(B), latex(x - x2))
                split_tex = "%s %s" % (term1_tex, term2_tex)

                # Tính nguyên hàm đúng: A*ln|x-x1| + B*ln|x-x2|
                F_correct_expr = A * log(Abs(x - x1)) + B * log(Abs(x - x2))
                F_correct_tex = latex(F_correct_expr)

                # CÁC PHƯƠNG ÁN NHIỄU (SAI)
                # Nhiễu 1: Đổi dấu cả A và B
                F_w1_expr = -A * log(Abs(x - x1)) - B * log(Abs(x - x2))
                F_w1_tex = latex(F_w1_expr) + " + C"

                # Nhiễu 2: Hoán đổi vị trí A và B cho 2 nghiệm
                F_w2_expr = B * log(Abs(x - x1)) + A * log(Abs(x - x2))
                F_w2_tex = latex(F_w2_expr) + " + C"

                # Nhiễu 3: Đổi dấu cộng / trừ giữa 2 log
                F_w3_expr = A * log(Abs(x - x1)) - B * log(Abs(x - x2))
                F_w3_tex = latex(F_w3_expr) + " + C"

                # Nhiễu 4: Quên cộng C
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
                s = [ans for ans in s_candidates if ans != da and ans != '$%s + C$' % (F_correct_tex)]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

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
                           % (y_tex, latex(num_expr_expanded), latex(den_expr_factored), split_tex, split_tex, F_correct_tex))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n').replace('\\log', '\\ln')
            return content 

