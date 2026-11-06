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


def bt_dang54_p1_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random các tham số của bài toán
                # Parabol y = x^2 + 2x + c. Trong hình c = -1.
                c = randint(-3, 1)
                # Cận tích phân x từ 0 đến 1 (giữ nguyên theo đề)

                # Giá trị nhỏ nhất của y = (x+1)^2 + c - 1 là y_min = c - 1
                # Để m < y_min với mọi x, chọn M2 < c - 1
                M2 = c - 2
                M1 = -randint(4000, 5000)

                # Điều kiện S <= K. Trong hình K = 2021
                K = randint(2000, 3000)

                # Tính toán diện tích S
                # S = tích phân từ 0 đến 1 của (x^2 + 2x + c - m) dx
                # S = [x^3/3 + x^2 + cx - mx] từ 0 đến 1
                # S = 1/3 + 1 + c - m = 4/3 + c - m

                const_val = Rational(4, 3) + c
                # S <= K <=> const_val - m <= K <=> m >= const_val - K
                L = const_val - K
                m_min_allowed = math.ceil(float(L))

                # Số giá trị nguyên m thuộc [M1, M2] và m >= m_min_allowed
                # Tập hợp các giá trị m là {max(M1, m_min_allowed), ..., M2}
                start_m = max(M1, m_min_allowed)
                kq_val = M2 - start_m + 1

                # Kết quả đúng
                kq = str(kq_val)

                # Bước 4: Tạo các phương án sai không trùng với đáp án đúng
                s_vals = set()
                while len(s_vals) < 3:
                    sai = kq_val + random.choice([-2, -1, 1, 2, 10, -10, 100])
                    if sai != kq_val and sai > 0:
                        s_vals.add(f'${sai}$')

                s_list = list(s_vals)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Gọi $S$ là diện tích hình phẳng giới hạn bởi parabol $y = x^2 + 2x %s$ và các đường thẳng $y = m$, $x = 0$, $x = 1$. Có bao nhiêu giá trị nguyên của tham số $m \\in [%s; %s]$ để $S \\le %s$?'''
                                 % (('+' + str(c) if c > 0 else (str(c) if c < 0 else '')), 
                                    latex(M1), latex(M2), latex(K)))

                # Đáp án
                da_d = ('\\True $%s$' % kq)

                # Nội dung lời giải
                # f(x) = x^2 + 2x + c = (x+1)^2 + c - 1 >= c - 1
                y_min = c - 1
                # m <= M2 < y_min nên m < x^2 + 2x + c

                # Tính phân thức 4/3 + c
                tp_text = latex(Rational(4, 3) + c)
                can_duoi = latex(L)

                loigiai = ('''Ta có: $y = x^2 + 2x %s = (x+1)^2 %s \\ge %s \\, \\forall x \\in \\mathbb{R}$. \\\\
                             Mà $m \\in [%s; %s]$ nên $m < x^2 + 2x %s \\, \\forall x \\in [0;1]$. \\\\
                             Suy ra $S = \\int\\limits_{0}^{1} (x^2 + 2x %s - m) \\text{d}x = \\left( \\frac{x^3}{3} + x^2 %s x - mx \\right) \\bigg|_0^1 = %s - m$. \\\\
                             Khi đó: $S \\le %s \\Leftrightarrow %s - m \\le %s \\Leftrightarrow m \\ge %s \\approx %s$. \\\\
                             Vì $m \\in [%s; %s], m \\in \\mathbb{Z}$ nên có $%s$ số nguyên $m$.'''
                           % (('+' + str(c) if c > 0 else (str(c) if c < 0 else '')),
                              latex(c-1), latex(y_min),
                              latex(M1), latex(M2),
                              ('+' + str(c) if c > 0 else (str(c) if c < 0 else '')),
                              ('+' + str(c) if c > 0 else (str(c) if c < 0 else '')),
                              ('+' + str(c) if c > 0 else (str(c) if c < 0 else '')),
                              tp_text,
                              latex(K), tp_text, latex(K), latex(L), round(float(L), 2),
                              latex(M1), latex(M2), kq))

                # Xuất câu trắc nghiệm
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

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

