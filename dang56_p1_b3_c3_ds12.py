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


def bt_dang56_p1_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo các ký hiệu
            m = symbols('m')

            # Chọn ngẫu nhiên k để sqrt(k) là số nguyên cho đẹp, k ở đây đóng vai trò là hằng số tự do trong pt bậc 2
            # Trong ảnh k = 4
            list_k = [1, 4, 9]
            k_val = random.choice(list_k)

            # Chọn hệ số a cho các hàm số bậc 3 (trong ảnh a=1)
            a_val = randint(1, 3)

            # Chọn hằng số tự do c2 cho hàm số thứ hai (trong ảnh c2=3)
            c2 = randint(1, 5)
            # Tính c1 dựa trên k_val để pt hoành độ giao điểm là x^2 - 2mx - k_val = 0
            # x^3 + (a+1)x^2 - 2mx + c1 = x^3 + a*x^2 + c2  => x^2 - 2mx + (c1-c2) = 0
            # Vậy c1 - c2 = -k_val => c1 = c2 - k_val
            c1 = c2 - k_val

            # Phương trình hoành độ giao điểm: x^2 - 2mx - k_val = 0
            # Delta' = m^2 + k_val. Vì k_val > 0 nên luôn có 2 nghiệm x1, x2
            # S = 4/3 * (m^2 + k_val)^(3/2)
            # S_min khi m = 0 => S_min = 4/3 * k_val * sqrt(k_val)

            s_min_val = Rational(4, 3) * k_val * int(math.sqrt(k_val))
            kq_fix = s_min_val

            # Tạo danh sách đáp án
            da_dung = '$%s$' % latex(kq_fix)

            # Tạo các đáp án nhiễu
            s = []
            nhieu1 = Rational(s_min_val.p + s_min_val.q, s_min_val.q)
            nhieu2 = Rational(s_min_val.p * 2, s_min_val.q)
            nhieu3 = Rational(s_min_val.p - 1, s_min_val.q)
            nhieu4 = Rational(s_min_val.p, 2)
            nhieu5 = Rational(3, 4) * k_val

            list_nhieu = [nhieu1, nhieu2, nhieu3, nhieu4, nhieu5]
            selected_nhieu = random.sample([item for item in list_nhieu if item != s_min_val], 3)

            da_s1 = '$%s$' % latex(selected_nhieu[0])
            da_s2 = '$%s$' % latex(selected_nhieu[1])
            da_s3 = '$%s$' % latex(selected_nhieu[2])

            # Nội dung câu hỏi
            noidungcauhoi = (r'Diện tích hình phẳng giới hạn bởi đồ thị của hai hàm số $y = x^3 + %sx^2 - 2mx %s$ ($m$ là tham số) và '
                             r'$y = x^3 + %sx^2 + %s$ đạt giá trị nhỏ nhất bằng'
                             % (latex(a_val + 1), latex(c1) if c1 < 0 else '+ ' + latex(c1), latex(a_val), latex(c2)))

            # Lời giải chi tiết theo mẫu trong ảnh
            # Biểu thức nguyên hàm trong ảnh là: [(x-m)/3 * (x^2-2mx-k) - (2k+2m^2)/3 * x - mk/3]
            linear_coeff = Rational(2*k_val, 3) # Phần chứa 2k/3 + 2m^2/3
            const_part = Rational(k_val, 3)    # Phần mk/3

            loigiai = (r'Xét phương trình hoành độ giao điểm: '
                       r'$x^3 + %sx^2 - 2mx %s = x^3 + %sx^2 + %s \Leftrightarrow x^2 - 2mx - %s = 0$.\\'
                       r'Phương trình luôn có hai nghiệm $x_1; x_2$ ($x_1 < x_2$) thỏa mãn '
                       r'$x_1 + x_2 = 2m; x_1x_2 = -%s \Rightarrow (x_1 - x_2)^2 = 4m^2 + %s$.\\'
                       r'Diện tích hình phẳng:\\'
                       r'$S = \int_{x_1}^{x_2} |x^2 - 2mx - %s| \text{d}x = \left| \left[ \frac{x-m}{3}(x^2 - 2mx - %s) - \frac{%s + 2m^2}{3}x - \frac{%sm}{3} \right] \Big|_{x_1}^{x_2} \right|$\\'
                       r'$ = \frac{%s + 2m^2}{3}|x_2 - x_1| = \frac{4}{3}\sqrt{(m^2 + %s)^3} \ge %s$.\\'
                       r'Vậy $S_{\min} = %s $ khi $ m = 0$.'
                       % (latex(a_val + 1), latex(c1) if c1 < 0 else '+ ' + latex(c1), latex(a_val), latex(c2), latex(k_val),
                          latex(k_val), latex(4*k_val),
                          latex(k_val), latex(k_val), latex(2*k_val), latex(k_val),
                          latex(2*k_val), latex(k_val), latex(kq_fix),
                          latex(kq_fix)))

            # Trộn đáp án
            list_da = [('\\True ' + da_dung), da_s1, da_s2, da_s3]
            random.shuffle(list_da)

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_da[0]) + '}\n'
                       '{' + str(list_da[1]) + '}\n'
                       '{' + str(list_da[2]) + '}\n'
                       '{' + str(list_da[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

