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


def bt_dang37_p1_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số b (tương ứng số 4 trong mẫu) và c (tương ứng số 9 trong mẫu)
                b = random.randint(3, 7)
                c = random.randint(5, 15)

                # Khoảng thời gian T (tương ứng số 10 trong mẫu), đảm bảo lớn hơn b để điểm cực trị nằm trong đoạn
                T = b + random.randint(3, 6)

                # Tính toán các giá trị liên quan đến vận tốc v(t) = -t^2 + 2b*t + c
                coef_2b = 2 * b
                v_max = b**2 + c
                v_T = -T**2 + coef_2b * T + c

                # Đáp án đúng
                da_str = "$%s$ (m/s)" % (v_max)
                da = random.choice([da_str])

                # Tạo các phương án nhiễu logic
                s = [
                    "$%s$ (m/s)" % (v_max + random.randint(15, 40)),
                    "$%s$ (m/s)" % (c),
                    "$%s$ (m/s)" % (v_max - random.randint(5, 12)),
                    "$%s$ (m/s)" % (v_max + random.randint(45, 70)),
                    "$%s$ (m/s)" % (abs(v_T) if v_T != 0 else v_max + 10)
                ]

                # Lọc trùng và loại bỏ đáp án đúng khỏi danh sách nhiễu
                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một chất điểm chuyển động theo quy luật $S = -\\frac{1}{3}t^3 + %st^2 + %st$ với $t$ (giây) là khoảng thời gian tính từ lúc vật bắt đầu chuyển động và $S$ (mét) là quãng đường vật chuyển động trong thời gian đó. Hỏi trong khoảng thời gian $%s$ giây, kể từ lúc bắt đầu chuyển động, vận tốc lớn nhất của chất điểm là bao nhiêu?'''
                                 % (latex(b), latex(c), latex(T)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết sử dụng đạo hàm
                loigiai = ('''Vận tốc của chất điểm là đạo hàm bậc nhất của quãng đường theo thời gian:\\\\
                           $v(t) = S'(t) = -t^2 + %st + %s$ (m/s).\\\\
                           Xét hàm số $v(t)$ trên đoạn $[0; %s]$, ta có:\\\\
                           $v'(t) = -2t + %s$.\\\\
                           Cho $v'(t) = 0 \\Leftrightarrow -2t + %s = 0 \\Leftrightarrow t = %s$.\\\\
                           Ta tính các giá trị của hàm số $v(t)$ tại các điểm mút và điểm cực trị:\\\\
                           $v(0) = %s$ (m/s).\\\\
                           $v(%s) = -%s^2 + %s \\cdot %s + %s = %s$ (m/s).\\\\
                           $v(%s) = -%s^2 + %s \\cdot %s + %s = %s$ (m/s).\\\\
                           So sánh các giá trị trên, ta thấy vận tốc lớn nhất của chất điểm trong khoảng thời gian $%s$ giây kể từ lúc bắt đầu chuyển động là $%s$ m/s đạt được tại $t = %s$ s.'''
                           % (latex(coef_2b), latex(c), latex(T),
                              latex(coef_2b), latex(coef_2b), latex(b),
                              latex(c),
                              latex(b), latex(b), latex(coef_2b), latex(b), latex(c), latex(v_max),
                              latex(T), latex(T), latex(coef_2b), latex(T), latex(c), latex(v_T),
                              latex(T), latex(v_max), latex(b)))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

