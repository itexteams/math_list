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


def bt_dang54_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Chọn cặp công sai d1, d2 sao cho gcd(d1, d2) = 1 và d1 < d2
                pairs = [(3, 5), (2, 5), (3, 7), (4, 5), (3, 4), (2, 7), (4, 7), (5, 7)]
                d1, d2 = random.choice(pairs)

                # Random số hạng đầu x1, y1
                x1 = randint(1, 6)
                y1 = randint(1, 6)

                # Tìm n0, m0 nhỏ nhất nguyên dương sao cho x_n0 = y_m0
                found = False
                for n0 in range(1, d2 + 1):
                    for m0 in range(1, d1 + 1):
                        if x1 + (n0 - 1) * d1 == y1 + (m0 - 1) * d2:
                            found = True
                            break
                    if found:
                        break

                # Giá trị số hạng chung đầu tiên C
                C = x1 + (n0 - 1) * d1

                # Số lượng số hạng N
                N = randint(1500, 2500)

                # Các số hạng đầu tiên của mỗi dãy
                x1_term1 = x1
                x1_term2 = x1 + d1
                x1_term3 = x1 + 2 * d1

                y1_term1 = y1
                y1_term2 = y1 + d2
                y1_term3 = y1 + 2 * d2

                # Tính giới hạn giá trị của k
                k_max_n = (N - n0) // d2
                k_max_m = (N - m0) // d1
                k_max = min(k_max_n, k_max_m)

                # Đáp án đúng
                ans = k_max + 1
                da_val = latex(ans)

                # Tạo danh sách các phương án sai (distractors)
                s_set = set()
                s_set.add(latex(k_max_n + 2))
                s_set.add(latex(k_max_m + 1))
                s_set.add(latex(k_max_m))
                s_set.add(latex(k_max_m + 2))
                s_set.add(latex(k_max_n))
                s_set.add(latex((N // d2) + 1))

                s_set.discard(da_val)

                s_list = list(s_set)
                random.shuffle(s_list)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hai cấp số cộng $(x_n): %s, %s, %s, \\dots$ và $(y_n): %s, %s, %s, \\dots$. Hỏi trong $%s$ số hạng đầu tiên của mỗi cấp số có bao nhiêu số hạng chung?'''
                                 % (latex(x1_term1), latex(x1_term2), latex(x1_term3),
                                    latex(y1_term1), latex(y1_term2), latex(y1_term3),
                                    latex(N)))

                # Định dạng các phương án trả lời
                da_d = ('\\True $%s$' % (da_val))
                da_s1 = ('$%s$' % (das1))
                da_s2 = ('$%s$' % (das2))
                da_s3 = ('$%s$' % (das3))

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Cấp số cộng $(x_n)$ có số hạng đầu $x_1 = %s$ và công sai $d_1 = %s$, có số hạng tổng quát là $x_n = %s + (n-1) \\cdot %s$ với $1 \\le n \\le %s$. \\\\
            Cấp số cộng $(y_n)$ có số hạng đầu $y_1 = %s$ và công sai $d_2 = %s$, có số hạng tổng quát là $y_m = %s + (m-1) \\cdot %s$ với $1 \\le m \\le %s$. \\\\
            Số hạng chung nhỏ nhất của hai cấp số cộng là $%s$, tương ứng với $n = %s$ và $m = %s$. \\\\
            Khi đó, các số hạng chung $x_n = y_m$ thỏa mãn: \\\\
            $%s(n - %s) = %s(m - %s)$. \\\\
            Do $\\gcd(%s, %s) = 1$ nên $(n - %s)$ phải chia hết cho $%s$. \\\\
            Đặt $n - %s = %sk \\Rightarrow n = %s + %sk$ với $k \\in \\mathbb{N}$. \\\\
            Thế vào biểu thức trên ta được $m = %s + %sk$. \\\\
            Vì $1 \\le n \\le %s$ và $1 \\le m \\le %s$ nên: \\\\
            $\\begin{cases} 1 \\le %s + %sk \\le %s \\\\ 1 \\le %s + %sk \\le %s \\end{cases} \\Leftrightarrow \\begin{cases} 0 \\le k \\le %s \\\\ 0 \\le k \\le %s \\end{cases} \\Leftrightarrow 0 \\le k \\le %s$. \\\\
            Vì $k \\in \\mathbb{N}$ nên $k \\in \\{0, 1, 2, \\dots, %s\\}$, có tất cả $%s$ giá trị $k$ thỏa mãn. \\\\
            Vậy có $%s$ số hạng chung.'''
                           % (latex(x1), latex(d1), latex(x1), latex(d1), latex(N),
                              latex(y1), latex(d2), latex(y1), latex(d2), latex(N),
                              latex(C), latex(n0), latex(m0),
                              latex(d1), latex(n0), latex(d2), latex(m0),
                              latex(d1), latex(d2), latex(n0), latex(d2),
                              latex(n0), latex(d2), latex(n0), latex(d2),
                              latex(m0), latex(d1),
                              latex(N), latex(N),
                              latex(n0), latex(d2), latex(N), latex(m0), latex(d1), latex(N), latex(k_max_n), latex(k_max_m), latex(k_max),
                              latex(k_max), latex(ans),
                              latex(ans)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{\n' + str(loigiai) + '\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

