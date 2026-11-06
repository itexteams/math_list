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


def bt_dang43_p3_b4_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số tiền gửi, lãi suất và số tiền mục tiêu
                A = random.randint(40, 90)           # Số tiền gửi ban đầu (triệu đồng)
                r = random.randint(5, 10)            # Lãi suất phần trăm
                S = random.randint(A + 30, A + 80)   # Số tiền mục tiêu (triệu đồng)

                # Tính toán kết quả
                # n > log_{1+r/100}(S/A)
                val = math.log(S/A, 1 + r/100)
                n = int(val) + 1  # Số năm ít nhất (làm tròn lên)

                # Xử lý số liệu in ra cho lời giải làm tròn 3 chữ số thập phân
                kq3 = Decimal(float(val)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
                val_str = str(kq3).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (n)]
                da = random.choice(du)

                # Sinh các phương án sai ngẫu nhiên (không trùng lặp với đáp án đúng)
                s_set = set()
                offsets = [1, -1, 2, -2, 3]
                for off in offsets:
                    dist_val = n + off
                    if dist_val > 0:
                        s_set.add('$%s$' % str(dist_val))

                if da in s_set:
                    s_set.remove(da)

                s = list(s_set)
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một người gửi $%s$ triệu đồng vào ngân hàng với lãi suất $%s\\%%$ một năm. Biết rằng nếu không rút tiền ra khỏi ngân hàng thì cứ sau mỗi năm số tiền lãi sẽ nhập vào gốc để tính lãi cho năm tiếp theo. Hỏi sau ít nhất bao nhiêu năm người đó nhận được số tiền nhiều hơn $%s$ triệu đồng gồm cả gốc lẫn lãi?'''
                                 % (A, r, S))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có: $S = A.(1+r)^n$. Để số tiền cả gốc lẫn lãi lớn hơn $%s$ triệu\\\\
                Suy ra $n > \\log_{1+r}\\left(\\frac{S}{A}\\right) = \\log_{1+%s\\%%}\\left(\\frac{%s}{%s}\\right) \\approx %s$ nên sau ít nhất $%s$ năm thì người đó nhận được số tiền cả gốc lẫn lãi nhiều hơn $%s$ triệu.'''
                           % (S, r, S, A, val_str, n, S))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                       '\\choice \n'
                       '{'+str(list_1[1])+'}\n'
                       '{'+str(list_1[2])+'}\n'
                       '{'+str(list_1[3])+'}\n'
                       '{'+str(list_1[0])+'}\n'
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

