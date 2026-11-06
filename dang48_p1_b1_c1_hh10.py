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


def bt_dang48_p1_b1_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hai số a, b sao cho b > a > 0 để thoả mãn điều kiện sin(x) > cos(x)
                a = random.randint(1, 5)
                b = random.randint(a + 1, a + 4)

                # Tính các đại lượng liên quan
                c_sq = a**2 + b**2
                k_val = Rational(c_sq, a*b) # Đây chính là giá trị của (tan(alpha) + cot(alpha))

                # Tính sin(alpha)*cos(alpha) = 1/k
                sin_cos_prod = Rational(a*b, c_sq)

                # (sin - cos)^2 = 1 - 2*sin*cos
                diff_sq = Rational((b - a)**2, c_sq)

                # (sin + cos)^2 = 1 + 2*sin*cos
                sum_sq = Rational((a + b)**2, c_sq)

                # Khai căn
                sin_minus_cos = simplify(sqrt(diff_sq))
                sin_plus_cos = simplify(sqrt(sum_sq))

                # Đáp án đúng: sin(alpha)
                ans_correct = simplify(b / sqrt(c_sq))

                # Tạo các phương án sai (nhiễu)
                ans_w1 = simplify(a / sqrt(c_sq))           # Nhầm sang tính cos(alpha)
                ans_w2 = simplify(Rational(a, b))           # Nhầm sang tính cot(alpha)
                ans_w3 = simplify(Rational(b, a))           # Nhầm sang tính tan(alpha)
                ans_w4 = simplify(1 / sqrt(c_sq))           # Phương án sai sinh ngẫu nhiên

                candidates = [ans_w1, ans_w2, ans_w3, ans_w4]
                s_set = set()
                for cand in candidates:
                    if cand != ans_correct:
                        s_set.add(cand)
                    if len(s_set) == 3:
                        break

                # Dự phòng nếu các nhiễu vô tình bị trùng
                count = 2
                while len(s_set) < 3:
                    ans_fake = simplify(b / sqrt(c_sq + count))
                    if ans_fake != ans_correct:
                        s_set.add(ans_fake)
                    count += 1

                s = list(s_set)

                # Định dạng đáp án
                da_str = '\\sin \\alpha = %s' % latex(ans_correct)
                da_d = '\\True $' + da_str + '$'

                das1 = '$\\sin \\alpha = %s$' % latex(s[0])
                das2 = '$\\sin \\alpha = %s$' % latex(s[1])
                das3 = '$\\sin \\alpha = %s$' % latex(s[2])

                # Câu hỏi
                noidungcauhoi = ('Biết $\\alpha$ là một góc từ $0^\\circ$ đến $180^\\circ$ thỏa mãn $\\tan \\alpha + \\cot \\alpha = %s$ và $\\sin \\alpha > \\cos \\alpha$. $\\sin \\alpha$ bằng' 
                                 % latex(k_val))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $\\tan \\alpha + \\cot \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha} + \\frac{\\cos \\alpha}{\\sin \\alpha} = \\frac{\\sin^2 \\alpha + \\cos^2 \\alpha}{\\sin \\alpha \\cos \\alpha} = \\frac{1}{\\sin \\alpha \\cos \\alpha}$. \\\\
                              Theo giả thiết, $\\tan \\alpha + \\cot \\alpha = %s \\Rightarrow \\frac{1}{\\sin \\alpha \\cos \\alpha} = %s \\Rightarrow \\sin \\alpha \\cos \\alpha = %s$. \\\\
                              Ta có: $\\left(\\sin \\alpha - \\cos \\alpha\\right)^2 = \\sin^2 \\alpha + \\cos^2 \\alpha - 2\\sin \\alpha \\cos \\alpha = 1 - 2 \\cdot \\left(%s\\right) = %s$. \\\\
                              Vì $\\sin \\alpha > \\cos \\alpha$ nên $\\sin \\alpha - \\cos \\alpha > 0$, suy ra $\\sin \\alpha - \\cos \\alpha = %s$. \\\\
                              Lại có: $\\left(\\sin \\alpha + \\cos \\alpha\\right)^2 = \\sin^2 \\alpha + \\cos^2 \\alpha + 2\\sin \\alpha \\cos \\alpha = 1 + 2 \\cdot \\left(%s\\right) = %s$. \\\\
                              Vì $0^\\circ < \\alpha < 180^\\circ$ và $\\sin \\alpha \\cos \\alpha = %s > 0$ nên $\\sin \\alpha > 0$ và $\\cos \\alpha > 0$. Do đó $\\sin \\alpha + \\cos \\alpha > 0$, suy ra $\\sin \\alpha + \\cos \\alpha = %s$. \\\\
                              Cộng hai đẳng thức ta được: $2\\sin \\alpha = \\left(\\sin \\alpha - \\cos \\alpha\\right) + \\left(\\sin \\alpha + \\cos \\alpha\\right) = %s + %s = %s \\Rightarrow \\sin \\alpha = %s$.'''
                           % (latex(k_val), latex(k_val), latex(sin_cos_prod),
                              latex(sin_cos_prod), latex(diff_sq),
                              latex(sin_minus_cos),
                              latex(sin_cos_prod), latex(sum_sq),
                              latex(sin_cos_prod), latex(sin_plus_cos),
                              latex(sin_minus_cos), latex(sin_plus_cos), latex(sin_minus_cos + sin_plus_cos), latex(ans_correct)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

