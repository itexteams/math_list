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


def bt_dang36_p4_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số a, b, c sao cho biệt thức Delta là số dương không chính phương 
                # để giống với đề bài mẫu (có căn thức)
                while True:
                    a = randint(1, 3)
                    b = randint(-5, 5)
                    c = randint(-20, -10)
                    delta = b**2 - 4*a*c
                    if delta > 0 and not math.sqrt(delta).is_integer():
                        break

                f = a*x**2 + b*x + c

                # Tìm nghiệm của tam thức
                x1 = ( -b - sqrt(delta) ) / (2*a)
                x2 = ( -b + sqrt(delta) ) / (2*a)

                # Tính toán các giá trị xấp xỉ để tìm số nghiệm nguyên
                val1 = float(x1.evalf())
                val2 = float(x2.evalf())

                nghiem_nguyen = []
                for i in range(math.ceil(val1), math.floor(val2) + 1):
                    nghiem_nguyen.append(i)

                so_nghiem = len(nghiem_nguyen)

                # Đáp án đúng
                da = '$%s$' % (so_nghiem)

                # Tạo các đáp án sai
                s = []
                while len(s) < 3:
                    sai = so_nghiem + random.choice([-3, -2, -1, 1, 2, 3])
                    if sai > 0 and sai != so_nghiem and str(sai) not in s:
                        s.append(str(sai))

                das1 = '$%s$' % s[0]
                das2 = '$%s$' % s[1]
                das3 = '$%s$' % s[2]

                # Câu hỏi
                noidungcauhoi = ('Tìm số nghiệm nguyên của bất phương trình $%s \\le 0$.'
                                 % (latex(f)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết với bảng xét dấu
                loigiai = ('''Xét $f(x) = %s$. \\\\
                            $f(x) = 0 \\Leftrightarrow x = \\frac{%s \\pm \\sqrt{%s}}{%s}$. \\\\
                            Ta có bảng xét dấu: 
                            \\begin{center}
                            \\begin{tabular}{|c|ccccccc|}
                            \\hline
                            $x$ & $-\\infty$ & & $\\frac{%s - \\sqrt{%s}}{%s}$ & & $\\frac{%s + \\sqrt{%s}}{%s}$ & & $+\\infty$ \\\\
                            \\hline
                            $f(x)$ & & $+$ & $0$ & $-$ & $0$ & $+$ & \\\\
                            \\hline
                            \\end{tabular} \\end{center}
                            Tập nghiệm của bất phương trình là $S = \\left[ \\frac{%s - \\sqrt{%s}}{%s}; \\frac{%s + \\sqrt{%s}}{%s} \\right]$. \\\\
                            Vì $\\frac{%s - \\sqrt{%s}}{%s} \\approx %s$ và $\\frac{%s + \\sqrt{%s}}{%s} \\approx %s$ nên bất phương trình có $%s$ nghiệm nguyên là $%s$.'''
                           % (latex(f), 
                              latex(-b), latex(delta), latex(2*a),
                              latex(-b), latex(delta), latex(2*a), latex(-b), latex(delta), latex(2*a),
                              latex(-b), latex(delta), latex(2*a), latex(-b), latex(delta), latex(2*a),
                              latex(-b), latex(delta), latex(2*a), round(val1, 2),
                              latex(-b), latex(delta), latex(2*a), round(val2, 2),
                              so_nghiem, ', '.join(map(str, nghiem_nguyen))
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

