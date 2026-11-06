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


def bt_dang38_p4_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Tạo nghiệm ngẫu nhiên để bài toán luôn đẹp
                # Giả sử 3 nghiệm là a, b, c với a < b < c
                a = random.randint(-6, -3)
                b = random.randint(-2, 1)
                c = random.randint(2, 5)

                # Đảm bảo các nghiệm phân biệt
                while b <= a: b += 1
                while c <= b: c += 1

                # Biểu thức: (x - c) * (x^2 - (a+b)x + ab) = 0
                # Trong ảnh mẫu: (x - 2)(x^2 + 5x + 4) >= 0 => c=2, a=-4, b=-1

                f_linear = x - c
                f_quad = expand((x - a)*(x - b))
                f_cubic = expand(f_linear * f_quad)

                # Hệ số để đưa vào latex
                str_cubic = latex(f_cubic)
                str_quad = latex(f_quad)
                str_linear = latex(f_linear)

                # Đáp án đúng
                kq_chuan = '$[' + str(a) + ';' + str(b) + '] \\cup [' + str(c) + ';+\\infty)$'

                # Các đáp án trắc nghiệm
                du = [kq_chuan]
                da = random.choice(du)

                s = [
                    '$(-\\infty;' + str(a) + '] \\cup [' + str(b) + ';' + str(c) + ']$',
                    '$[' + str(a) + ';' + str(b) + '] \\cup (' + str(c) + ';+\\infty)$',
                    '$(-\\infty;' + str(a) + ') \\cup (' + str(b) + ';' + str(c) + ')$',
                    '$[' + str(a) + ';' + str(c) + ']$',
                    '$(-\\infty;' + str(b) + '] \\cup [' + str(c) + ';+\\infty)$',
                    '$(' + str(a) + ';' + str(b) + ') \\cup (' + str(c) + ';+\\infty)$'
                ]

                # Loại bỏ đáp án đúng nếu lỡ trùng trong danh sách sai
                if da in s:
                    s.remove(da)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('Giải bất phương trình $%s \\ge 0$.' % (str_cubic))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết dùng tabular cho bảng xét dấu
                loigiai = (
                    'Bất phương trình $%s \\ge 0 \\Leftrightarrow (%s)(%s) \\ge 0$. \\\\\n'
                    'Phương trình $%s = 0 \\Leftrightarrow \\left[\\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned}\\right.$ và $%s = 0 \\Leftrightarrow x = %s$. \\\\\n'
                    'Lập bảng xét dấu: '
                    '\\begin{center}\n'
                    '\\begin{tabular}{|c|ccccccccc|}\n'
                    '\\hline\n'
                    '$x$ & $-\\infty$ & & $%s$ & & $%s$ & & $%s$ & & $+\\infty$ \\\\ \\hline\n'
                    '$%s$ & & $+$ & $0$ & $-$ & $0$ & $+$ & $|$ & $+$ & \\\\ \\hline\n'
                    '$%s$ & & $-$ & $|$ & $-$ & $|$ & $-$ & $0$ & $+$ & \\\\ \\hline\n'
                    '$(%s)(%s)$ & & $-$ & $0$ & $+$ & $0$ & $-$ & $0$ & $+$ & \\\\ \\hline\n'
                    '\\end{tabular}\n'
                    '\\end{center}\n'
                    'Dựa vào bảng xét dấu, ta thấy rằng $(%s)(%s) \\ge 0 \\Leftrightarrow x \\in$ %s.'
                    % (str_cubic, str_linear, str_quad, 
                       str_quad, latex(a), latex(b), str_linear, latex(c),
                       latex(a), latex(b), latex(c),
                       str_quad, str_linear, str_linear, str_quad,
                       str_linear, str_quad, kq_chuan)
                )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

