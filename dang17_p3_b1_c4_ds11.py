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


def bt_dang17_p3_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- PHẦN 1: RANDOM HỆ SỐ ---
                # Mẫu số có dạng: A*n^2 + B
                A = randint(2, 9)  # Hệ số của n^2 (ví dụ: 3)
                B = randint(1, 10) # Hệ số tự do (ví dụ: 4)

                k = randint(0, 2)

                # Tính số hạng cuối cùng hiển thị trong đề bài
                last_term_const = 2 * k - 1 
                if last_term_const > 0:
                    last_term_str = "2n+%s" % last_term_const
                else:
                    last_term_str = "2n%s" % last_term_const # Xử lý dấu âm, ví dụ 2n-1

                ans_val = Rational(1, A)
                kq = latex(ans_val)
                h1=1/A
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq1=str(kqz).replace('.', ',')

                # Tạo các đáp án nhiễu (Distractors)
                # Nhiễu 1: Đảo ngược (A)
                da_s1_val = A 
                # Nhiễu 2: Sai mẫu (1 / (A+1))
                da_s2_val = Rational(1, A + 1)
                # Nhiễu 3: Sai tử (2 / A)
                da_s3_val = Rational(2, A)
                # Nhiễu 4: Số 0
                da_s4_val = 0

                # Danh sách các đáp án sai tiềm năng
                s = [
                    '$%s$' % latex(da_s1_val),
                    '$%s$' % latex(da_s2_val),
                    '$%s$' % latex(da_s3_val),
                    '$%s$' % latex(da_s4_val)
                ]

                # Lọc đáp án trùng nhau và trùng đáp án đúng
                du = ['$%s$' % kq]
                wrong_choices = []
                for choice in s:
                    if choice not in wrong_choices and choice != du[0]:
                        wrong_choices.append(choice)
                    if len(wrong_choices) == 3: # Chỉ lấy 3 đáp án sai
                        break

                # Gán biến đáp án
                da = du[0]
                das1 = wrong_choices[0]
                das2 = wrong_choices[1]
                das3 = wrong_choices[2]

                # --- PHẦN 3: NỘI DUNG CÂU HỎI ---
                noidungcauhoi = ('''$\\lim_{n \\to +\\infty} \\frac{1 + 3 + 5 + \\dots + %s}{%sn^2 + %s}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 % (last_term_str, A, B))

                # Trộn đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- PHẦN 4: NỘI DUNG LỜI GIẢI (ĐÃ SỬA LỖI) ---
                # Xây dựng chuỗi lời giải linh hoạt theo k
                if k == 0:
                    sum_formula = "n^2"
                    step1_logic = "" # n^2 là công thức cơ bản, không cần giải thích thêm
                    expand_numerator = "n^2"
                    div_num = "1"
                elif k == 1:
                    sum_formula = "(n+1)^2"
                    step1_logic = "=\\frac{(1+2n+1)(n+1)}{2}"
                    expand_numerator = "n^2 + 2n + 1"
                    div_num = "1 + \\frac{2}{n} + \\frac{1}{n^2}"
                else:
                    # Trường hợp k >= 2 hoặc khác
                    sum_formula = "(n+%s)^2" % k
                    # Đã sửa lỗi SyntaxError ở dòng dưới đây: thêm ngoặc kép và dùng %s
                    step1_logic = "=\\frac{(1+2n+%s)(n+%s)}{2}" % (last_term_const, k)
                    expand_numerator = "n^2 + %sn + %s" % (2*k, k**2)
                    div_num = "1 + \\frac{%s}{n} + \\frac{%s}{n^2}" % (2*k, k**2)

                div_den = "%s + \\frac{%s}{n^2}" % (A, B)

                loigiai = ('''Ta có $1 + 3 + 5 + \\dots + (%s) %s = %s$. \\\\
                              $\\begin{aligned} 
                              \\lim_{n \\to +\\infty} \\frac{1 + 3 + 5 + \\dots + %s}{%sn^2 + %s} 
                              &= \\lim_{n \\to +\\infty} \\frac{%s}{%sn^2 + %s} \\\\
                              &= \\lim_{n \\to +\\infty} \\frac{%s}{%sn^2 + %s} \\\\
                              &= \\lim_{n \\to +\\infty} \\frac{%s}{%s} = %s \\approx %s. 
                              \\end{aligned}$'''
                           % (last_term_str, step1_logic, sum_formula, 
                              last_term_str, A, B,
                              sum_formula, A, B,
                              expand_numerator, A, B,
                              div_num, div_den, kq, kq1))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kq1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

