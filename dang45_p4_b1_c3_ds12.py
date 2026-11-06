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


def bt_dang45_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                x = symbols('x')

                # Random các hệ số của tử số ax^3 + bx^2 + cx + d
                a = random.choice([2, 4, 6, 8, -2, -4, -6])
                b = random.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
                c = random.choice([2, 4, 6, 8, -2, -4, -6, -8])
                d = random.choice([-7, -5, -3, -1, 1, 3, 5, 7])

                # Biểu thức tử số
                num_expr = a*x**3 + b*x**2 + c*x + d

                # Biểu thức hàm số y dạng phân thức
                y_tex = "\\frac{%s}{x^2}" % (latex(num_expr))

                # Biểu thức sau khi tách từng phân số và rút gọn: ax + b + c/x + d/x^2
                split_expr = a*x + b + c/x + d/x**2
                split_tex = latex(split_expr)

                # Tính nguyên hàm đúng:
                # int(a*x) = (a/2)*x^2
                # int(b) = b*x
                # int(c/x) = c*ln|x|
                # int(d/x^2) = -d/x
                term1 = Rational(a, 2)*x**2
                term2 = b*x
                term3 = c*log(Abs(x))
                term4 = -Rational(d, 1)/x

                F_correct_expr = term1 + term2 + term3 + term4
                F_correct_tex = latex(F_correct_expr)

                # Các phương án sai (nhiễu)
                # Sai 1: Đổi dấu ở phần -d/x thành +d/x (hoặc ngược lại)
                F_wrong1_expr = term1 + term2 + term3 - term4
                F_wrong1_tex = latex(F_wrong1_expr) + " + C"

                # Sai 2: Nhầm sang đạo hàm
                F_wrong2_expr = diff(num_expr/x**2, x)
                F_wrong2_tex = latex(F_wrong2_expr) + " + C"

                # Sai 3: Quên cộng C
                F_wrong3_tex = latex(F_correct_expr)

                # Sai 4: Đổi dấu hệ số b
                F_wrong4_expr = term1 - term2 + term3 + term4
                F_wrong4_tex = latex(F_wrong4_expr) + " + C"

                # Đáp án đúng
                du = ['$%s + C$' % (F_correct_tex)]
                da = random.choice(du)

                # Danh sách các câu sai
                s_candidates = [
                    '$%s$' % (F_wrong1_tex),
                    '$%s$' % (F_wrong2_tex),
                    '$%s$' % (F_wrong3_tex),
                    '$%s$' % (F_wrong4_tex)
                ]

                # Lọc bỏ nếu trùng đáp án đúng
                s = [ans for ans in s_candidates if ans != da and ans != '$%s + C$' % (F_correct_tex)]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('Tìm nguyên hàm của hàm số $y = %s$.' % (y_tex))

                # Các đáp án trắc nghiệm
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Hướng dẫn: Tách riêng từng phân số, rút gọn $x$ rồi lấy nguyên hàm. \\\\ '
                           'Ta có $y = %s = \\frac{%s}{x^2} + \\frac{%s}{x^2} + \\frac{%s}{x^2} + \\frac{%s}{x^2} = %s$. \\\\ '
                           'Họ tất cả các nguyên hàm của hàm số đã cho là: \\\\ '
                           '$\\int %s \\mathrm{d}x = \\int \\left( %s \\right) \\mathrm{d}x = %s + C$.' 
                           % (y_tex, latex(a*x**3), latex(b*x**2), latex(c*x), latex(d), split_tex, y_tex, split_tex, F_correct_tex))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 

