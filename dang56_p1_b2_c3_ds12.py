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


def bt_dang56_p1_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số mũ n trong biểu thức x^n. Giả sử n chạy từ 2 đến 6
                n = random.randint(2, 6)

                # Hàm f(x) cuối cùng sẽ là x^n
                # Tích phân từ 0 đến 1 của x^n là 1/(n+1)
                tu = 1
                mau = n + 1
                kq_sym = Rational(tu, mau)
                kq_latex = latex(kq_sym)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq_latex)]
                da = random.choice(du)

                # Tạo các phương án sai (không trùng với đáp án đúng)
                s_list = [
                    Rational(1, n),
                    Rational(2, n + 1),
                    Rational(1, n + 2),
                    Rational(n, n + 1),
                    Rational(1, 2*n),
                    Rational(3, n + 2)
                ]

                # Lọc bỏ giá trị trùng với đáp án đúng
                s_list = [latex(i) for i in s_list if i != kq_sym]
                random.shuffle(s_list)

                das1 = '$%s$' % s_list[0]
                das2 = '$%s$' % s_list[1]
                das3 = '$%s$' % s_list[2]

                # Biểu thức n*x^(n-1)
                if n == 2:
                    nx_n_1 = "2x"
                    x_n = "x^2"
                else:
                    nx_n_1 = f"{n}x^{{{n-1}}}"
                    x_n = f"x^{{{n}}}"

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $f(x)$ không âm, có đạo hàm trên đoạn $[0;1]$ và thỏa mãn $f(1)=1$, $[2f(x)+1-%s]f'(x)=%s[1+f(x)], \\forall x \\in [0;1]$. Tích phân $\\int\\limits_{0}^{1} f(x) \\mathrm{d}x$ bằng'''
                                 % (x_n, nx_n_1))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Xét trên đoạn $[0;1]$, theo đề bài: $[2f(x)+1-%s]f'(x)=%s[1+f(x)]$ \\\\
                             $\\Leftrightarrow 2f(x) \\cdot f'(x) = %s + (%s-1) \\cdot f'(x) + %s \\cdot f(x)$ \\\\
                             $\\Leftrightarrow [f^2(x)]' = [%s + (%s-1) \\cdot f(x)]'$ \\\\
                             $\\Leftrightarrow f^2(x) = %s + (%s-1) \\cdot f(x) + C \\quad (1)$. \\\\
                             Thay $x=1$ vào $(1)$ ta được: $f^2(1)=1+C \\Leftrightarrow C=0$ (vì $f(1)=1$). \\\\
                             Do đó, $(1)$ trở thành: $f^2(x) = %s + (%s-1) \\cdot f(x)$ \\\\
                             $\\Leftrightarrow f^2(x)-1 = %s-1 + (%s-1) \\cdot f(x)$ \\\\
                             $\\Leftrightarrow [f(x)-1] \\cdot [f(x)+1] = (%s-1) \\cdot [f(x)+1]$ \\\\
                             $\\Leftrightarrow f(x)-1 = %s-1$ (vì $f(x) \\ge 0 \\Rightarrow f(x)+1 > 0, \\forall x \\in [0;1]$) \\\\
                             $\\Leftrightarrow f(x) = %s$. \\\\
                             Vậy $\\int\\limits_{0}^{1} f(x) \\mathrm{d}x = \\int\\limits_{0}^{1} %s \\mathrm{d}x = \\left. \\frac{x^{%s}}{%s} \\right|_0^1 = %s$.'''
                           % (x_n, nx_n_1, nx_n_1, x_n, nx_n_1, x_n, x_n, x_n, x_n, x_n, x_n, x_n, x_n, x_n, x_n, x_n, x_n, n+1, n+1, kq_latex))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

