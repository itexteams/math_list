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


def bt_dang49_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số góc để tạo ra nhiều câu hỏi khác nhau nhưng giữ tính chất
                # Chọn ngẫu nhiên hệ số của x cho hàm thứ nhất (a) và hàm thứ hai (b) sao cho gcd(a,b)=1
                # Để giữ nguyên dạng đáp án T = 2*pi, ta có thể cho một cặp như (2, 3), (2, 5), v.v.
                pairs = [(2, 3), (2, 5), (3, 4), (3, 5)]
                a, b = random.choice(pairs)

                # Các hằng số dịch pha ngẫu nhiên
                p1 = random.choice([3, 4, 6])
                p2 = random.choice([3, 4, 6])

                # Hệ số biên độ trước cos
                amp = randint(2, 5)

                # Tính toán chu kỳ thành phần
                # T1 = 2*pi / a
                if 2 % a == 0:
                    T1_str = '%s\\pi' % (latex(Rational(2, a)))
                else:
                    T1_str = '\\frac{2\\pi}{%s}' % (latex(a))

                # T2 = 2*pi / b
                if 2 % b == 0:
                    T2_str = '%s\\pi' % (latex(Rational(2, b)))
                else:
                    T2_str = '\\frac{2\\pi}{%s}' % (latex(b))

                # Chu kỳ tổng hợp T = BCNN(T1, T2) = 2*pi / BCLN(a, b) = 2*pi vì gcd(a,b)=1
                T_val = 2
                da_str = 'T = %s\\pi' % (latex(T_val))

                du = ['$%s$' % (da_str)]
                da = random.choice(du)

                # Các phương án sai không trùng đáp án đúng
                s_candidates = ['T = \\pi', 'T = 3\\pi', 'T = 4\\pi', 'T = 6\\pi']
                s_candidates = [c for c in s_candidates if c != da_str]
                s = ['$%s$' % (choice) for choice in s_candidates]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Khởi tạo chuỗi latex các hàm số thành phần
                f1_latex = 'y = \\sin \\left( %sx + \\frac{\\pi}{%s} \\right)' % (latex(a), latex(p1))
                f2_latex = 'y = %s\\cos \\left( %sx - \\frac{\\pi}{%s} \\right)' % (latex(amp), latex(b), latex(p2))
                f_total_latex = 'y = \\sin \\left( %sx + \\frac{\\pi}{%s} \\right) + %s\\cos \\left( %sx - \\frac{\\pi}{%s} \\right)' % (latex(a), latex(p1), latex(amp), latex(b), latex(p2))

                # Câu hỏi
                noidungcauhoi = ('''Chu kì $T$ của hàm số $%s$ là''' % (f_total_latex))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết, đầy đủ từng bước
                loigiai = ('''Hàm số $%s$ tuần hoàn với chu kì $T_1 = \\frac{2\\pi}{%s} = %s$. \\\\
                           Hàm số $%s$ tuần hoàn với chu kì $T_2 = \\frac{2\\pi}{%s} = %s$. \\\\
                           Suy ra hàm số $%s$ tuần hoàn với chu kì $T = %s\\pi$.'''
                           % (f1_latex, latex(a), T1_str, f2_latex, latex(b), T2_str, f_total_latex, latex(T_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

