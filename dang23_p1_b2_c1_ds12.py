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


def bt_dang23_p1_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3-Suy nghĩ tìm cách random bài toán
                # Xét hàm số y = x^3 - 3*k^2*x + m trên đoạn [a; b]
                # Đạo hàm y' = 3x^2 - 3k^2 = 0 có nghiệm x = k và x = -k.
                # Chọn k > 0 và đoạn [a; b] sao cho chỉ có nghiệm x = k thuộc [a; b].
                x = symbols('x')
                k = random.randint(1, 4)
                a = random.randint(0, k - 1)
                b = random.randint(k + 1, k + 3)
                m = random.randint(1, 10)

                # Biểu thức hàm số y
                expr = x**3 - 3 * (k**2) * x + m
                expr_tex = latex(expr)

                # Đạo hàm y'
                y_prime = 3 * x**2 - 3 * (k**2)
                y_prime_tex = latex(y_prime)

                # Tính giá trị hàm số tại các điểm cần xét
                val_a = expr.subs(x, a)
                val_k = expr.subs(x, k)
                val_b = expr.subs(x, b)

                # Giá trị nhỏ nhất chắc chắn đạt tại x = k (vì hàm giảm từ a đến k, tăng từ k đến b)
                ans_x = k

                # B4-Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                da = '$x = %s$' % ans_x

                # Tạo các phương án nhiễu sai khác đáp án đúng
                choices = [a, b, a + 1, b - 1, b + 1, a + 2, b + 2]
                choices = list(set(choices) - {ans_x})
                das = random.sample(choices, 3)

                das1 = '$x = %s$' % das[0]
                das2 = '$x = %s$' % das[1]
                das3 = '$x = %s$' % das[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Trên đoạn $[%s; %s]$, hàm số $y = %s$ đạt giá trị nhỏ nhất tại điểm''' % (a, b, expr_tex))

                # Đưa các đáp án vào danh sách
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Hàm số $y = %s$ xác định và liên tục trên đoạn $[%s; %s]$. \\\\
            Ta có $y' = %s$. \\\\
            Cho $y' = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow \\left[ \\begin{array}{l} x = %s \\\\ x = %s \\end{array} \\right.$. \\\\
            Vì $x \\in [%s; %s]$ nên ta chỉ xét $x = %s$. \\\\
            Ta có: \\\\
            $y(%s) = %s$; \\\\
            $y(%s) = %s$; \\\\
            $y(%s) = %s$. \\\\
            Vậy giá trị nhỏ nhất của hàm số trên đoạn $[%s; %s]$ là $%s$, đạt tại điểm $x = %s$.''' % 
                           (expr_tex, a, b, 
                            y_prime_tex, 
                            y_prime_tex, k, -k, 
                            a, b, k, 
                            a, val_a, 
                            k, val_k, 
                            b, val_b, 
                            a, b, val_k, k))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{\n' + str(loigiai) + '\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

