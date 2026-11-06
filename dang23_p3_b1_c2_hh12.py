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


def bt_dang23_p3_b1_c2_hh12(self):
    # Khai báo biến dạng bài
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # 1. Random hệ số tỉ lệ k1, k2
        k1 = random.choice([2, 3])
        k2 = random.choice([4, 5, 6])

        # Bội chung nhỏ nhất của k1 và k2
        L = math.lcm(k1, k2)

        # 2. Random tung độ và cao độ của M
        m2 = random.randint(1, 5)
        m3 = random.randint(1, 5)

        # 3. Tính m1 sao cho a = m1 + m2*k1 + m3*k2 chia hết cho L
        temp = m2 * k1 + m3 * k2
        r = (L - (temp % L)) % L
        if r == 0:
            r = L
        m1 = r + L * random.randint(0, 2)

        # 4. Tính toán các giá trị a, b, c nguyên
        a = m1 + m2 * k1 + m3 * k2
        b_val = a // k1
        c_val = a // k2

        # Kết quả T = a + b + c (Số nguyên)
        T = a + b_val + c_val

        # Đáp án đúng
        du = ['$%s$' % (latex(T))]
        da = random.choice(du)

        # Các phương án sai (nguyên, dương, không trùng đáp án đúng)
        s_raw = [T + 1, T - 1, T + 2, T - 2, T + 3, T - 3, T + 4, T - 4]
        s = ['$%s$' % (latex(val)) for val in s_raw if val > 0 and val != T]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong không gian với hệ trục tọa độ $Oxyz$, mặt phẳng $(P)\\colon bcx+acy+abz-abc=0$ qua điểm $M(%s;%s;%s)$ và cắt các tia $Ox,Oy,Oz$ lần lượt tại $A,B,C$ sao cho $OA=%sOB=%sOC$. Tổng $T=a+b+c$ bằng bao nhiêu?'''
                         % (latex(m1), latex(m2), latex(m3), latex(k1), latex(k2)))

        # Các phương án lựa chọn
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Trộn ngẫu nhiên 4 đáp án
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Phương trình mặt phẳng $(P)\\colon bcx+acy+abz-abc=0 \\Leftrightarrow \\frac{x}{a}+\\frac{y}{b}+\\frac{z}{c}=1$.\\\\
    Vì $(P)$ cắt các tia $Ox, Oy, Oz$ lần lượt tại $A, B, C$ nên $A(a;0;0)$, $B(0;b;0)$, $C(0;0;c)$ với $a,b,c>0$.\\\\
    Theo giả thiết $OA=%sOB=%sOC \\Rightarrow a=%sb=%sc \\Rightarrow b=\\frac{a}{%s}, c=\\frac{a}{%s}$.\\\\
    Mặt phẳng $(P)$ đi qua $M(%s;%s;%s)$ nên ta có:
    $$\\frac{%s}{a}+\\frac{%s}{b}+\\frac{%s}{c}=1 \\Leftrightarrow \\frac{%s}{a}+\\frac{%s \\cdot %s}{a}+\\frac{%s \\cdot %s}{a}=1 \\Leftrightarrow \\frac{%s}{a}=1 \\Leftrightarrow a=%s.$$
    Suy ra $b=%s$, $c=%s$.\\\\
    Vậy $T=a+b+c=%s+%s+%s=%s$.'''
                   % (latex(k1), latex(k2), latex(k1), latex(k2), latex(k1), latex(k2),
                      latex(m1), latex(m2), latex(m3),
                      latex(m1), latex(m2), latex(m3), 
                      latex(m1), latex(m2), latex(k1), latex(m3), latex(k2), 
                      latex(a), latex(a),
                      latex(b_val), latex(c_val),
                      latex(a), latex(b_val), latex(c_val), latex(T)
                     ))
    dapan='\\shortans[0]{$%s$}\n'%(latex(T))
    # Xuất câu trắc nghiệm theo mẫu chuẩn
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n\\end{minipage} \n\n')
    return content

