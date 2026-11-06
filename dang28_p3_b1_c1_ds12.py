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


def bt_dang28_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tham số của bài toán
                # P = c*I - d*I^2 -> P' = c - 2d*I > 0 -> I < c/(2d)
                # Khoảng (0; c/(2d)) => a = 0, b = c/(2d) => a+b = c/(2d)
                d_val = random.choice([0.25, 0.5, 0.1, 0.2, 0.4])
                b_val = random.choice([10, 12, 15, 20, 24, 30])

                # Calculate c based on b_val and d_val to ensure b is the chosen value
                c = round(b_val * 2 * d_val, 2)

                if c.is_integer():
                    c = int(c)

                a = 0
                b = b_val
                kq = a + b

                d_str = str(d_val).replace('.', ',')
                c_str = str(c).replace('.', ',')
                d2_str = str(round(2 * d_val, 2)).replace('.', ',')
                if float(d2_str.replace(',', '.')) == 1.0:
                    d2_str = ""

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),
                      ]
                da = random.choice(du)

                # Tạo các phương án sai (đảm bảo không trùng với đáp án đúng)
                s = ['$%s$'%(latex(kq + 10)),
                     '$%s$'%(latex(kq - 10)),
                     '$%s$'%(latex(kq + 5)),
                     '$%s$'%(latex(kq - 5)),
                     '$%s$'%(latex(kq * 2)),
                     '$%s$'%(latex(kq + 2)),
                     '$%s$'%(latex(abs(kq - 2))),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Công suất $P$ (đơn vị W) của một mạch điện được xác định bởi công thức $P = %sI - %sI^2$ với $I \\ (I > 0, \\text{ đơn vị A})$ là cường độ dòng điện. Biết công suất $P$ tăng khi cường độ dòng điện $I$ ở trong khoảng $(a;b)$. Giá trị $a+b$ bằng bao nhiêu?'''
                                 %(c_str, d_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                if d2_str == "":
                    loigiai = ('''Ta có $P'(I) = %s - 2 \\cdot %s I = %s - I$.\\\\
                             Công suất $P$ tăng khi và chỉ khi đạo hàm $P'(I) > 0$.\\\\
                             $P'(I) > 0 \\Leftrightarrow %s - I > 0 \\Leftrightarrow I < %s$.\\\\
                             Kết hợp với điều kiện $I > 0$, ta được khoảng cường độ dòng điện để công suất tăng là $(0; %s)$.\\\\
                             Suy ra $a = 0$ và $b = %s$.\\\\
                             Vậy $a + b = 0 + %s = %s$.'''
                             %(c_str, d_str, c_str, 
                               c_str, b,
                               b,
                               b,
                               b, kq))
                else:
                    loigiai = ('''Ta có $P'(I) = %s - 2 \\cdot %s I = %s - %sI$.\\\\
                             Công suất $P$ tăng khi và chỉ khi đạo hàm $P'(I) > 0$.\\\\
                             $P'(I) > 0 \\Leftrightarrow %s - %sI > 0 \\Leftrightarrow I < %s$.\\\\
                             Kết hợp với điều kiện $I > 0$, ta được khoảng cường độ dòng điện để công suất tăng là $(0; %s)$.\\\\
                             Suy ra $a = 0$ và $b = %s$.\\\\
                             Vậy $a + b = 0 + %s = %s$.'''
                             %(c_str, d_str, c_str, d2_str,
                               c_str, d2_str, b,
                               b,
                               b,
                               b, kq))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content  

