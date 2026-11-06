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


def bt_dang57_p1_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn ngẫu nhiên n trong khoảng từ 10 đến 30 để số không quá lớn
                n_val = randint(10, 25)

                # Tính tổng S = 1 + 2 + ... + n = n(n+1)/2
                S_val = n_val * (n_val + 1) // 2

                # Chọn cơ số logarit ngẫu nhiên (thường là số nguyên tố nhỏ)
                base = random.choice([2, 3, 5, 7])

                # Random biểu thức P = a*n + b
                coeff_a = randint(2, 4)
                coeff_b = randint(1, 10)
                final_P = coeff_a * n_val + coeff_b

                # Đáp án đúng
                kq = final_P
                da = '$%s$' % latex(kq)

                # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    # Tạo các phương án nhiễu quanh đáp án đúng
                    sai = kq + random.choice([-5, -3, -2, -1, 1, 2, 3, 5, 10])
                    if sai != kq and sai > 0:
                        s.add('$%s$' % latex(sai))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # B2: Viết lại đề bài và lời giải
                # Câu hỏi
                noidungcauhoi = (r'''Gọi $n$ là số nguyên dương sao cho $\frac{1}{\log_{%s} x} + \frac{1}{\log_{%s^2} x} + \frac{1}{\log_{%s^3} x} + \dots + \frac{1}{\log_{%s^n} x} = \frac{%s}{\log_{%s} x}$ đúng với mọi $x$ dương, $x \neq 1$. Giá trị của biểu thức $P = %sn + %s$ bằng'''
                                 % (latex(base), latex(base), latex(base), latex(base), latex(S_val), latex(base), latex(coeff_a), latex(coeff_b)))

                # Nội dung lời giải
                loigiai = (r'''Ta có:
            \begin{align*}
            &\frac{1}{\log_{%s} x} + \frac{1}{\log_{%s^2} x} + \dots + \frac{1}{\log_{%s^n} x} = \frac{%s}{\log_{%s} x} \\
            \Leftrightarrow &\log_x %s + 2\log_x %s + \dots + n\log_x %s = %s \log_x %s \\
            \Leftrightarrow &\log_x %s (1 + 2 + 3 + \dots + n) = %s \log_x %s \\
            \Leftrightarrow &1 + 2 + 3 + \dots + n = %s \\
            \Leftrightarrow &\frac{n(n+1)}{2} = %s \\
            \Leftrightarrow &n^2 + n - %s = 0 \\
            \Leftrightarrow &\left[\begin{aligned} &n = %s \\ &n = -%s \end{aligned}\right.
            \end{align*}
            Vì $n$ là số nguyên dương nên chọn $n = %s$. \\
            Thay vào biểu thức $P$ ta được: $P = %s \cdot %s + %s = %s$.'''
                           % (base, base, base, S_val, base,
                              base, base, base, S_val, base,
                              base, S_val, base,
                              S_val,
                              S_val,
                              2 * S_val,
                              n_val, n_val + 1,
                              n_val,
                              coeff_a, n_val, coeff_b, kq))

                # Đưa các đáp án vào danh sách
                da_d = '\\True ' + str(da)
                list_ans = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_ans)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

