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


def bt_dang9_p4_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Ngẫu nhiên điểm M(x0, y0)
                # Để tránh phương trình đi qua gốc tọa độ (c=0), ta chọn x0 != y0
                x0 = randint(-10, 10)
                y0 = randint(-10, 10)
                while x0 == y0:
                    y0 = randint(-10, 10)

                # Bước 2: Logic bài toán
                # Đường phân giác góc phần tư thứ hai (II) là Delta: x + y = 0
                # Đường thẳng d vuông góc với Delta nên d có dạng: x - y + c = 0
                # M(x0, y0) thuộc d => x0 - y0 + c = 0 => c = y0 - x0
                c_val = y0 - x0

                # Tạo các thành phần cho phương trình: x - y + c = 0
                # Hàm hiển thị dấu cho c
                def format_c(c):
                    if c > 0: return "+ " + str(c)
                    if c < 0: return "- " + str(abs(c))
                    return ""

                # Đáp án đúng: x - y + c = 0
                da_dung = "x - y %s = 0" % (format_c(c_val))

                # Các đáp án nhiễu
                s1 = "x + y %s = 0" % (format_c(c_val))      # Sai vector pháp tuyến
                s2 = "x + y %s = 0" % (format_c(-c_val))     # Sai vector và sai dấu c
                s3 = "x - y %s = 0" % (format_c(-c_val))     # Sai dấu c

                # Các đáp án trắc nghiệm
                du = ["$%s$" % da_dung]
                da = random.choice(du)

                # Danh sách đáp án sai (đảm bảo không trùng đáp án đúng)
                s = ["$%s$" % s1, "$%s$" % s2, "$%s$" % s3]

                # Trình tự chọn đáp án sai để shuffle
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Lập phương trình tổng quát của đường thẳng $d$ đi qua điểm $M(%s;%s)$ và vuông góc với đường phân giác góc phần tư thứ hai.'''
                                  %(latex(x0), latex(y0)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Đường phân giác của góc phần tư thứ hai có phương trình là $\\Delta: x + y = 0$. \\\\
                             Vì đường thẳng $d$ vuông góc với đường thẳng $\\Delta$ nên phương trình tổng quát của $d$ có dạng $x - y + c = 0$. \\\\
                             Mặt khác, đường thẳng $d$ đi qua điểm $M(%s; %s)$, thay tọa độ điểm $M$ vào phương trình đường thẳng $d$ ta được: \\\\
                             $%s - (%s) + c = 0 \\Leftrightarrow %s + c = 0 \\Leftrightarrow c = %s$. \\\\
                             Vậy phương trình tổng quát của đường thẳng $d$ là $%s$.'''
                           %(latex(x0), latex(y0), 
                             latex(x0), latex(y0), latex(x0 - y0), latex(c_val),
                             da_dung
                            ))

            # Xuất câu trắc nghiệm (không dùng tiền tố r cho content)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

