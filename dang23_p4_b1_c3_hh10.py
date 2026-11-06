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


def bt_dang23_p4_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Random tọa độ điểm M(x0, y0)
                x0 = random.randint(-10, 10)
                y0 = random.randint(-10, 10)

                # Random tọa độ VTCP u(a, b), đảm bảo u khác vecto không
                a = random.choice([i for i in range(-10, 11) if i != 0])
                b = random.choice([i for i in range(-10, 11) if i != 0])

                # Hàm tạo chuỗi phương trình tham số LaTeX
                def format_ptts(px, py, pa, pb):
                    # Xử lý dấu cho pa, pb khi viết trong phương trình
                    sa = f"+ {pa}" if pa > 0 else f"- {abs(pa)}"
                    sb = f"+ {pb}" if pb > 0 else f"- {abs(pb)}"
                    return r"\begin{cases} x = %s %s t \\ y = %s %s t \end{cases}" % (px, sa, py, sb)

                # Đáp án đúng
                da_dung = "$%s$" % format_ptts(x0, y0, a, b)

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                s = []
                # Sai kiểu 1: Đảo tọa độ điểm và vecto
                s.append("$%s$" % format_ptts(a, b, x0, y0))
                # Sai kiểu 2: Đảo x, y của điểm M
                s.append("$%s$" % format_ptts(y0, x0, a, b))
                # Sai kiểu 3: Đảo hoành độ và tung độ của VTCP
                s.append("$%s$" % format_ptts(x0, y0, b, a))
                # Sai kiểu 4: Nhầm sang Vecto pháp tuyến (đổi dấu và đảo vị trí)
                s.append("$%s$" % format_ptts(x0, y0, -b, a))

                # Loại bỏ trùng lặp nếu có và xóa đáp án đúng khỏi danh sách sai
                s = list(set(s))
                if da_dung in s:
                    s.remove(da_dung)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Lập phương trình tham số của đường thẳng $d$ đi qua điểm $M(%s;%s)$ và có VTCP $\\vec{u} = (%s;%s)$.'''
                                 %(latex(x0), latex(y0), latex(a), latex(b)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Chi tiết, không viết tắt)
                loigiai = ('''Đường thẳng $d$ đi qua điểm $M(x_0; y_0)$ và có vectơ chỉ phương $\\vec{u} = (a; b)$ có phương trình tham số là:
                             $$\\begin{cases} x = x_0 + at \\\\ y = y_0 + bt \\end{cases} (t \\in \\mathbb{R})$$
                             Thay tọa độ điểm $M(%s; %s)$ và tọa độ vectơ chỉ phương $\\vec{u} = (%s; %s)$ vào công thức trên, ta được:
                             $%s$.'''
                           %(latex(x0), latex(y0), latex(a), latex(b), format_ptts(x0, y0, a, b)))

            # Xuất câu trắc nghiệm (Không dùng tiền tố r trong phần content)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 


