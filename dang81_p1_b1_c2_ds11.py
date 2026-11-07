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


def bt_dang81_p1_b1_c2_ds11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Dãy tăng: u_n = (a*n + b)/(n + c) với a*c - b > 0
        # Đảm bảo mẫu số n + c > 0 với mọi n >= 1 bằng cách chọn c >= 1
        # Trong đề gốc: a = 1, b = -2, c = 1 -> a*c - b = 1 - (-2) = 3 > 0 -> dãy tăng
        c_tang = random.randint(1, 3)
        b_tang = random.randint(-4, -1)
        a_tang = 1
        k_tang = a_tang * c_tang - b_tang  # k_tang > 0
        
        # Chuỗi hiển thị cho dãy tăng u_n = (n + b)/(n + c)
        if b_tang < 0:
            tu_tang = 'n - %d' % abs(b_tang)
        elif b_tang == 0:
            tu_tang = 'n'
        else:
            tu_tang = 'n + %d' % b_tang
    
        if c_tang == 1:
            mau_tang = 'n + 1'
        else:
            mau_tang = 'n + %d' % c_tang
    
        da_tang = '$u_n = \\frac{%s}{%s}$' % (tu_tang, mau_tang)
    
        # 3 phương án sai:
        # Sai 1: Dãy số bậc nhất giảm u_n = -a1*n + b1 (với a1 > 0)
        a1 = random.randint(2, 4)
        b1 = random.randint(3, 7)
        da_sai1 = '$u_n = -%dn + %d$' % (a1, b1)
    
        # Sai 2: Dãy nghịch đảo u_n = k2/n hoặc k2/(n+p) (với k2 > 0) -> luôn giảm
        k2 = random.randint(1, 3)
        if k2 == 1:
            da_sai2 = '$u_n = \\frac{1}{n}$'
        else:
            da_sai2 = '$u_n = \\frac{%d}{n}$' % k2
    
        # Sai 3: Dãy bậc 2 nghịch biến u_n = -a3*n^2 hoặc -n^2 + ...
        a3 = random.randint(1, 3)
        if a3 == 1:
            da_sai3 = '$u_n = -n^2$'
        else:
            da_sai3 = '$u_n = -%dn^2$' % a3
    
        # Các đáp án trắc nghiệm
        da = da_tang
        s = [da_sai1, da_sai2, da_sai3]
    
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        # Câu hỏi
        noidungcauhoi = '''Trong các dãy số $u_n$ cho bởi công thức của số hạng tổng quát $u_n$ dưới đây, dãy số nào là dãy số tăng?'''
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Tính toán cho lời giải
        if b_tang < 0:
            tu_n1 = '(n + 1) - %d' % abs(b_tang)
            tu_n1_gon = 'n - %d' % (abs(b_tang) - 1) if (abs(b_tang) - 1) > 0 else ('n' if (abs(b_tang) - 1) == 0 else 'n + 1')
        else:
            tu_n1 = '(n + 1) + %d' % b_tang
            tu_n1_gon = 'n + %d' % (b_tang + 1)
    
        mau_n1 = '(n + 1) + %d' % c_tang
        mau_n1_gon = 'n + %d' % (c_tang + 1)
    
        # Nội dung lời giải
        loigiai = ('''Xét từng phương án:
    \\\\
    * Xét dãy số $u_n = \\frac{%s}{%s}$:
    \\\\
    Ta có với mọi $n \\ge 1, n \\in \\mathbb{N}^*$:
    \\\\
    $u_{n+1} - u_n = \\frac{%s}{%s} - \\frac{%s}{%s} = \\frac{(%s)(%s) - (%s)(%s)}{(%s)(%s)} = \\frac{%d}{(%s)(%s)} > 0$.
    \\\\
    Do đó $u_{n+1} > u_n$ với mọi $n \\ge 1$, suy ra dãy số $(u_n)$ là dãy số tăng.
    \\\\
    * Xét dãy số %s:
    \\\\
    Ta có $u_{n+1} - u_n = [-%d(n + 1) + %d] - (-%dn + %d) = -%d < 0$ nên dãy số này là dãy số giảm.
    \\\\
    * Xét dãy số %s:
    \\\\
    Ta có $u_{n+1} - u_n = \\frac{%d}{n + 1} - \\frac{%d}{n} = \\frac{-%d}{n(n + 1)} < 0$ với mọi $n \\ge 1$ nên dãy số này là dãy số giảm.
    \\\\
    * Xét dãy số %s:
    \\\\
    Ta có $u_{n+1} - u_n = %s(n + 1)^2 - (%sn^2) = %s(2n + 1) < 0$ với mọi $n \\ge 1$ nên dãy số này là dãy số giảm.
    \\\\
    Vậy dãy số tăng là dãy số $u_n = \\frac{%s}{%s}$.'''
                   % (tu_tang, mau_tang,
                      tu_n1_gon, mau_n1_gon, tu_tang, mau_tang,
                      tu_n1_gon, mau_tang, tu_tang, mau_n1_gon,
                      mau_n1_gon, mau_tang,
                      k_tang,
                      mau_n1_gon, mau_tang,
                      da_sai1,
                      a1, b1, a1, b1, a1,
                      da_sai2,
                      k2, k2, k2,
                      da_sai3,
                      ('-' if a3 == 1 else '-%d' % a3),
                      ('-' if a3 == 1 else '-%d' % a3),
                      ('-' if a3 == 1 else '-%d' % a3),
                      tu_tang, mau_tang
                      ))
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n'
               '{' + str(list_1[1]) + '}\n'
               '{' + str(list_1[2]) + '}\n'
               '{' + str(list_1[3]) + '}\n'
               '{' + str(list_1[0]) + '}\n'
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
    