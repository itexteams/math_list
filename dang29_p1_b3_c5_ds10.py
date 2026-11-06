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


def bt_dang29_p1_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Chọn n nguyên dương để tạo ra bài toán
                # Để M = (4n^2 - 6n + 8)/3 là số nguyên, n^2 + 2 phải chia hết cho 3
                # Các giá trị n phù hợp: 5, 8, 11, 14, 17, 20...
                n_valid = [5, 8, 11, 14, 17, 20]
                n_ans = random.choice(n_valid)

                # Bước 2: Tính hệ số M trong phương trình a_{3n-3} = M*n
                # Công thức: a_{3n-3} = 2*n^2 + (4/3)*n*(n-1)*(n-2)
                # => M = 2*n + (4/3)*(n-1)*(n-2) = (6n + 4n^2 - 12n + 8) / 3 = (4n^2 - 6n + 8) / 3
                M = (4 * n_ans**2 - 6 * n_ans + 8) // 3

                # Đáp án đúng
                kq = n_ans

                # Các đáp án sai (nhiễu)
                s = []
                while len(s) < 3:
                    sai = n_ans + random.choice([-3, -2, -1, 1, 2, 3, 4, 5, 6])
                    if sai > 3 and sai != n_ans and sai not in s:
                        s.append(sai)

                # Câu hỏi
                noidungcauhoi = ('''Với $n$ là số nguyên dương, gọi $a_{3n-3}$ là hệ số của $x^{3n-3}$ trong khai triển thành đa thức của $f\\left(x\\right)=\\left(x^2+1\\right)^n\\left(x+2\\right)^n$. Giá trị của $n$ để $a_{3n-3}=%sn$ bằng'''
                                 %(latex(M)))

                # Các phương án
                da_d = ('\\True $n=%s$' % (latex(kq)))
                da_s1 = ('$n=%s$' % (latex(s[0])))
                da_s2 = ('$n=%s$' % (latex(s[1])))
                da_s3 = ('$n=%s$' % (latex(s[2])))

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Tính các hằng số trung gian cho lời giải
                M_str = latex(M)
                four_third = '\\frac{4}{3}'

                loigiai = ('''Ta có khai triển: \\\\
                             $f\\left(x\\right)=\\left(x^2+1\\right)^n\\left(x+2\\right)^n = \\left(\\sum_{k=0}^{n} C_n^k x^{2n-2k}\\right) \\left(\\sum_{i=0}^{n} C_n^i x^{n-i} 2^i\\right) = \\sum_{k=0}^{n} \\left(\\sum_{i=0}^{n} C_n^k C_n^i 2^i x^{3n-2k-i}\\right)$ với $0 \\le i, k \\le n$. \\\\
                             Số hạng chứa $x^{3n-3}$ ứng với $3n - \\left(2k + i\\right) = 3n - 3 \\Leftrightarrow 2k + i = 3$. \\\\
                             Vì $k, i$ là các số tự nhiên nên ta có các trường hợp sau: \\\\
                             Trường hợp 1: $k=1, i=1 \\Rightarrow$ hệ số là $C_n^1 \\cdot C_n^1 \\cdot 2^1 = 2n^2$. \\\\
                             Trường hợp 2: $k=0, i=3 \\Rightarrow$ hệ số là $C_n^0 \\cdot C_n^3 \\cdot 2^3 = 8 \\cdot \\frac{n\\left(n-1\\right)\\left(n-2\\right)}{6} = %s n\\left(n-1\\right)\\left(n-2\\right)$. \\\\
                             Theo giả thiết: $a_{3n-3} = %sn \\Leftrightarrow 2n^2 + %s n\\left(n-1\\right)\\left(n-2\\right) = %sn$. \\\\
                             Vì $n > 0$, chia cả hai vế cho $n$ ta được: \\\\
                             $2n + %s \\left(n-1\\right)\\left(n-2\\right) = %s \\Leftrightarrow 6n + 4\\left(n^2 - 3n + 2\\right) = %s$ \\\\
                             $\\Leftrightarrow 4n^2 - 6n + 8 = %s \\Leftrightarrow 4n^2 - 6n - %s = 0$. \\\\
                             Giải phương trình bậc hai (với $n$ nguyên dương), ta tìm được $n=%s$.'''
                           %(four_third, M_str, four_third, M_str,
                             four_third, latex(3*M), latex(3*M),
                             latex(3*M), latex(3*M-8), latex(kq)
                            ))

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

