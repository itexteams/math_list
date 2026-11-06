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


def bt_dang12_p3_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo các dạng toán
            lisdang = ['1', '2', '3']
            dang = random.choice(lisdang)

            if dang == '1': # Trường hợp đường thẳng nằm ngang y = -c (giống ảnh)
                c = 7
                a = 0
                b = 1
                x1 = random.randint(1, 10)
                x2 = x1 + random.randint(1, 5)
                if random.choice([True, False]): x1, x2 = x2, x1

                xA, yA = x1, -c
                xB, yB = x2, -c

                kq_val = a + b
                loigiai_huong = "Vì hai điểm $A, B$ có cùng tung độ $y = -%s$ nên đường thẳng $AB$ có phương trình là $y = -%s$ hay $y + %s = 0$." % (c, c, c)

            elif dang == '2': # Trường hợp đường thẳng đứng x = -c
                c = 7
                a = 1
                b = 0
                y1 = random.randint(-10, 10)
                y2 = y1 + random.randint(1, 5)
                if random.choice([True, False]): y1, y2 = y2, y1

                xA, yA = -c, y1
                xB, yB = -c, y2

                kq_val = a + b
                loigiai_huong = "Vì hai điểm $A, B$ có cùng hoành độ $x = -%s$ nên đường thẳng $AB$ có phương trình là $x = -%s$ hay $x + %s = 0$." % (c, c, c)

            else: # Trường hợp đường thẳng x + y = -c
                c = 7
                a = 1
                b = 1
                xA = random.randint(-5, 0)
                yA = -c - xA
                xB = xA + random.randint(1, 3)
                yB = -c - xB

                kq_val = a + b
                loigiai_huong = "Véc-tơ $\\vec{AB} = (%s; %s)$. Véc-tơ pháp tuyến chọn là $\\vec{n} = (1; 1)$. Phương trình đường thẳng là $1(x - (%s)) + 1(y - (%s)) = 0 \\Leftrightarrow x + y + %s = 0$." % (latex(xB-xA), latex(yB-yA), latex(xA), latex(yA), c)

            # --- Xử lý đáp án ---
            kq = str(kq_val)
            da = '$%s$' % kq

            # Tạo các phương án sai không trùng với đáp án đúng
            s_list = []
            while len(s_list) < 3:
                sai = kq_val + random.choice([-2, -1, 1, 2, 3, 4])
                if sai >= 0 and str(sai) != kq and str(sai) not in s_list:
                    s_list.append(str(sai))

            das1 = '$%s$' % s_list[0]
            das2 = '$%s$' % s_list[1]
            das3 = '$%s$' % s_list[2]

            # --- Nội dung câu hỏi ---
            noidungcauhoi = ('''Phương trình tổng quát của đường thẳng đi qua hai điểm $A(%s; %s)$ và $B(%s; %s)$ là : $(d) : ax + by + 7 = 0; a, b \\in \\mathbb{N}$. Giá trị $a + b$ bằng bao nhiêu?'''
                             % (latex(xA), latex(yA), latex(xB), latex(yB)))

            # --- Nội dung lời giải chi tiết ---
            loigiai = ('''Ta có vectơ $\\vec{AB} = (%s; %s)$. \\\\
                         %s \\\\
                         Đối chiếu với phương trình $(d): ax + by + 7 = 0$, ta có $a = %s$ và $b = %s$. \\\\
                         Vậy $a + b = %s + %s = %s$.'''
                       % (latex(xB - xA), latex(yB - yA), loigiai_huong, a, b, a, b, kq_val))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(kq_val)
            # Các đáp án
            da_d = '\\True ' + str(da)
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

