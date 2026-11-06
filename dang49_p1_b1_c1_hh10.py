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


def bt_dang49_p1_b1_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Chọn cặp số (a, b) sao cho a < b và gcd(a, b) = 1 để tan(alpha) = a/b < 1
                pairs = [(1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (2, 5), (3, 5), (4, 5)]
                a, b = random.choice(pairs)

                # Giá trị đúng của tan(alpha) và tan(alpha) > 1
                tan_correct = Rational(a, b)
                tan_wrong1 = Rational(b, a)

                # Tính sin(alpha)*cos(alpha) = p và tan(alpha) + cot(alpha) = m
                p = Rational(a * b, a**2 + b**2)
                m = Rational(a**2 + b**2, a * b)

                # Tạo các phương án nhiễu (giống cấu trúc các đáp án ở đề gốc)
                c_sq = a**2 + b**2
                val_cos = simplify(a / sqrt(c_sq))
                val_sin = simplify(b / sqrt(c_sq))

                # Đáp án đúng
                da = '$\\tan \\alpha = %s$' % latex(tan_correct)

                # Các phương án sai
                w1 = '$\\tan \\alpha = %s$' % latex(tan_wrong1)
                w2 = '$\\tan \\alpha = %s$' % latex(val_cos)
                w3 = '$\\tan \\alpha = %s$' % latex(val_sin)

                s_set = set([w1, w2, w3])
                if da in s_set:
                    s_set.remove(da)

                count = 1
                while len(s_set) < 3:
                    fake_tan = Rational(a + count, b + count + 1)
                    fake_str = '$\\tan \\alpha = %s$' % latex(fake_tan)
                    if fake_str != da and fake_str not in s_set:
                        s_set.add(fake_str)
                    count += 1

                s = list(s_set)
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('Biết $\\alpha$ là một góc từ $0^\\circ$ đến $180^\\circ$ thỏa mãn $\\sin \\alpha \\cdot \\cos \\alpha = %s$ và $\\tan \\alpha < 1$. $\\tan \\alpha$ bằng'
                                 % latex(p))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuẩn bị phương trình bậc 2 trong lời giải: A*t^2 - (a^2+b^2)*t + A = 0
                eq_coeff_A = a * b
                eq_coeff_B = -(a**2 + b**2)

                if eq_coeff_A == 1:
                    quad_str = 't^2 %s t + 1 = 0' % latex(eq_coeff_B)
                else:
                    quad_str = '%st^2 %s t + %s = 0' % (latex(eq_coeff_A), latex(eq_coeff_B), latex(eq_coeff_A))

                # Nội dung lời giải
                loigiai = ('''Ta có $\\tan \\alpha + \\cot \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha} + \\frac{\\cos \\alpha}{\\sin \\alpha} = \\frac{\\sin^2 \\alpha + \\cos^2 \\alpha}{\\sin \\alpha \\cdot \\cos \\alpha} = \\frac{1}{\\sin \\alpha \\cdot \\cos \\alpha}$. \\\\
                              Theo giả thiết $\\sin \\alpha \\cdot \\cos \\alpha = %s$, suy ra $\\tan \\alpha + \\cot \\alpha = \\frac{1}{%s} = %s$. \\\\
                              Đặt $t = \\tan \\alpha$, ta có phương trình: \\\\
                              $t + \\frac{1}{t} = %s \\Leftrightarrow %s$. \\\\
                              Giải phương trình trên ta được $t = %s$ hoặc $t = %s$. \\\\
                              Vì $\\tan \\alpha < 1$ nên ta chọn $t = %s$. \\\\
                              Vậy $\\tan \\alpha = %s$.'''
                           % (latex(p), latex(p), latex(m),
                              latex(m), quad_str,
                              latex(tan_correct), latex(tan_wrong1),
                              latex(tan_correct),
                              latex(tan_correct)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

