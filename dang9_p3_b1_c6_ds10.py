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


def bt_dang9_p3_b1_c6_ds10(self):
            # Khai báo biến
            # Khai báo biến loại câu hỏi
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # d là số mà số được chọn phải chia hết cho (ví dụ chia hết cho 3)
                d = random.randint(3, 6)

                # a là cận dưới (lớn hơn a), b là cận trên (nhỏ hơn b)
                # Đảm bảo khoảng cách đủ lớn để có nhiều kết quả
                a = random.randint(2, 10)
                b = random.randint(80, 150)

                # Tính toán các giá trị n
                # k = n * d, với a < n*d < b <=> a/d < n < b/d
                n_min = math.floor(a / d) + 1
                n_max = math.ceil(b / d) - 1

                # Kết quả đúng: số các giá trị n thỏa mãn
                kq_int = n_max - n_min + 1
                da = kq_int

                # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = kq_int + random.choice([-2, -1, 1, 2, 3, 4])
                    if sai != kq_int and sai > 0:
                        s.add(sai)

                das = list(s)
                das1 = das[0]
                das2 = das[1]
                das3 = das[2]

                # Câu hỏi
                noidungcauhoi = ('''Chọn ngẫu nhiên một số nguyên lớn hơn $%s$ và nhỏ hơn $%s$. Gọi $B$ là biến cố "Số được chọn chia hết cho $%s$". Số các kết quả thuận lợi cho $B$ bằng bao nhiêu?'''
                                 %(latex(a), latex(b), latex(d)))

                # Các đáp án
                da_d = ('\\True $%s$' % (latex(da)))
                da_s1 = ('$%s$' % (latex(das1)))
                da_s2 = ('$%s$' % (latex(das2)))
                da_s3 = ('$%s$' % (latex(das3)))

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (không viết tắt, trình bày theo mẫu ảnh)
                loigiai = ('''Gọi $k$ là số nguyên thỏa mãn đề bài. \\\\
                             Theo giả thiết, ta có $k \\in \\mathbb{N}^*$, $%s < k < %s$ và $k$ chia hết cho $%s$. \\\\
                             Suy ra $k = %s n$ với $n \\in \\mathbb{N}^*$. \\\\
                             Khi đó: $%s < %s n < %s \\Leftrightarrow \\frac{%s}{%s} < n < \\frac{%s}{%s} \\Leftrightarrow %s < n < %s$. \\\\
                             Vì $n$ là số nguyên nên $n \\in \\left\\{ %s; %s; \\dots; %s \\right\\}$. \\\\
                             Số các giá trị của $n$ là: $%s - %s + 1 = %s$. \\\\
                             Vậy số kết quả thuận lợi cho biến cố $B$ là $%s$.'''
                           %(latex(a), latex(b), latex(d), latex(d),
                             latex(a), latex(d), latex(b), latex(a), latex(d), latex(b), latex(d),
                             latex(round(a/d, 2)).replace('.', ','), latex(round(b/d, 2)).replace('.', ','),
                             latex(n_min), latex(n_min + 1), latex(n_max),
                             latex(n_max), latex(n_min), latex(da), latex(da)))
                dapan=' \\shortans[0]{$%s$} '%(latex(da))
            # B2: Xuất câu trắc nghiệm đúng cấu trúc content
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

