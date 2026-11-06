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


def bt_dang87_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            if dang == '1':
                # Biến thể 1: Hàm số dạng y = \sqrt[4]{\sin x} - \sqrt{\cos x} (Giống bài gốc) hoặc y = \sqrt[4]{\cos x} - \sqrt{\sin x}
                bien_so = random.choice([('\\sin x', '\\cos x'), ('\\cos x', '\\sin x')])
                ham1, ham2 = bien_so[0], bien_so[1]

                # Kết quả: M = 1, m = -1
                M_val, m_val = 1, -1
                da_chuoi = 'M = 1; m = -1'
                da = '$%s$' % (da_chuoi)

                # Tạo danh sách phương án nhiễu (đảm bảo không trùng với đáp án đúng)
                s = [
                    '$M = 0; m = -1$',
                    '$M = 2; m = 0$',
                    '$M = 1; m = 0$',
                    '$M = 1; m = -2$',
                    '$M = 2; m = -1$'
                ]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = ('''Giá trị lớn nhất $M$ và giá trị nhỏ nhất $m$ của hàm số $y = \\sqrt[4]{%s} - \\sqrt{%s}$ là'''
                                 % (ham1, ham2))

                # Lời giải chi tiết theo mẫu hệ phương trình đánh giá của gốc
                loigiai = ('''Ta có $\\begin{cases} 0 \\le \\sqrt[4]{%s} \\le 1 \\\\ 0 \\le \\sqrt{%s} \\le 1 \\end{cases} \\Rightarrow \\begin{cases} 0 \\le \\sqrt[4]{%s} \\le 1 \\\\ -1 \\le -\\sqrt{%s} \\le 0 \\end{cases} \\Rightarrow -1 \\le y = \\sqrt[4]{%s} - \\sqrt{%s} \\le 1$.\\\\
                           Vậy $M = 1; m = -1$.'''
                           % (ham1, ham2, ham1, ham2, ham1, ham2))

            elif dang == '2':
                # Biến thể 2: Hàm số dạng y = \sqrt[4]{\sin x} + \sqrt{\cos x} hoặc y = \sqrt[4]{\cos x} + \sqrt{\sin x}
                bien_so = random.choice([('\\sin x', '\\cos x'), ('\\cos x', '\\sin x')])
                ham1, ham2 = bien_so[0], bien_so[1]

                # Kết quả: M = 1, m = 0 (vì điều kiện đồng thời sinx >= 0 và cosx >= 0 trên vòng tròn lượng giác)
                M_val, m_val = 1, 0
                da_chuoi = 'M = 1; m = 0'
                da = '$%s$' % (da_chuoi)

                # Tạo danh sách phương án nhiễu
                s = [
                    '$M = 1; m = -1$',
                    '$M = 0; m = -1$',
                    '$M = 2; m = 0$',
                    '$M = 2; m = 1$',
                    '$M = 1; m = \\frac{1}{2}$'
                ]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = ('''Giá trị lớn nhất $M$ và giá trị nhỏ nhất $m$ của hàm số $y = \\sqrt[4]{%s} + \\sqrt{%s}$ là'''
                                 % (ham1, ham2))

                # Lời giải chi tiết
                loigiai = ('''Ta có $\\begin{cases} 0 \\le \\sqrt[4]{%s} \\le 1 \\\\ 0 \\le \\sqrt{%s} \\le 1 \\end{cases}$ và do điều kiện xác định của hàm số đồng thời diễn ra, suy ra $0 \\le y = \\sqrt[4]{%s} + \\sqrt{%s} \\le 1$.\\\\
                           Vậy $M = 1; m = 0$.'''
                           % (ham1, ham2, ham1, ham2))

            # Gán phương án trả lời đúng
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Đưa các đáp án vào danh sách và trộn ngẫu nhiên thứ tự hiển thị
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm đúng khung cấu trúc định dạng
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

