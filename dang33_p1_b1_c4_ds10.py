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


def bt_dang33_p1_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo các giá trị ngẫu nhiên
                # Hàm số có dạng: sqrt(sqrt(x^2 + 2bx + b^2 + c) - (x + b))
                b = random.randint(-5, 5)
                c = random.randint(1, 10)

                # Biểu thức bên trong căn nhỏ: x^2 + 2bx + (b^2 + c)
                b2c = b**2 + c
                two_b = 2 * b
                expr_inner_quad = x**2 + two_b * x + b2c

                # Biểu thức bậc nhất: x + b
                expr_linear = x + b

                # Hàm số đầy đủ để hiển thị đề bài
                # y = sqrt(sqrt(expr_inner_quad) - (expr_linear))

                # Đáp án đúng
                da_dung = r'$D = \mathbb{R}$'

                # Các đáp án sai (Tạo các khoảng dựa trên nghiệm của x + b = 0)
                nghiem = -b
                s = [
                    r'$D = [%s; +\infty)$' % latex(nghiem),
                    r'$D = (-\infty; %s]$' % latex(nghiem),
                    r'$D = (%s; +\infty)$' % latex(nghiem),
                    r'$D = \mathbb{R} \setminus \{%s\}$' % latex(nghiem),
                    r'$D = \emptyset$'
                ]

                # Chọn ngẫu nhiên 3 đáp án sai từ danh sách s
                list_sai = random.sample(s, 3)

                # Câu hỏi
                # Sử dụng latex() để hiển thị biểu thức đẹp mắt
                noidungcauhoi = (r'Tập xác định của hàm số $y = \sqrt{\sqrt{%s} - (%s)}$ là' 
                                 % (latex(expr_inner_quad), latex(expr_linear)))

                # Các đáp án
                da_d = ('\\True ' + da_dung)
                da_s1 = list_sai[0]
                da_s2 = list_sai[1]
                da_s3 = list_sai[2]

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết y hệt logic trong ảnh)
                loigiai = (r'''Ta có $y = \sqrt{\sqrt{x^2 + %sx + %s} - (x + %s)} = \sqrt{\sqrt{(x + %s)^2 + %s} - (x + %s)}$. \\
            Hàm số xác định khi $\sqrt{(x + %s)^2 + %s} - (x + %s) \geq 0 \Leftrightarrow \sqrt{(x + %s)^2 + %s} \geq x + %s$ \\
            $\Leftrightarrow \left[\begin{aligned} &x + %s < 0 \\ &\begin{cases} x + %s \geq 0 \\ (x + %s)^2 + %s \geq (x + %s)^2 \end{cases} \end{aligned}\right. 
            \Leftrightarrow \left[\begin{aligned} &x + %s < 0 \\ &x + %s \geq 0 \end{aligned}\right. \Leftrightarrow x \in \mathbb{R}$. \\
            Vậy tập xác định của hàm số là $D = \mathbb{R}$.'''
                           % (latex(two_b), latex(b2c), latex(b), latex(b), latex(c), latex(b),
                              latex(b), latex(c), latex(b), latex(b), latex(c), latex(b),
                              latex(b), latex(b), latex(b), latex(c), latex(b),
                              latex(b), latex(b)))

            # Xuất câu trắc nghiệm theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

