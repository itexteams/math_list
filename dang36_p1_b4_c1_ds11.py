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


def bt_dang36_p1_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random trường hợp vế phải của phương trình để tạo bài toán khác nhau
                # TH 1: cos(2x) = -1/2 (bài mẫu)
                # TH 2: cos(2x) = 1/2
                loai = random.choice([1, 2])

                if loai == 1:
                    v_str = '-\\frac{1}{2}'
                    phi_str = '\\frac{2\\pi}{3}'
                    x_str = '\\frac{\\pi}{3}'
                    # Nghiệm thỏa mãn làm góc tam giác: pi/3 hoặc 2*pi/3
                    # Bộ góc tam giác cân có góc pi/3: {pi/3, pi/3, pi/3}
                    # Bộ góc tam giác cân có góc 2pi/3: {2pi/3, pi/6, pi/6}
                    da_str = '\\left\\{ \\frac{\\pi}{3};\\frac{\\pi}{3};\\frac{\\pi}{3} \\right\\}; \\left\\{ \\frac{2\\pi}{3};\\frac{\\pi}{6};\\frac{\\pi}{6} \\right\\}'

                    # Phần text bổ trợ cho lời giải
                    thoa_man_text = 'x = \\frac{\\pi}{3} \\text{ hoặc } x = \\frac{2\\pi}{3}'
                    ket_luan_text = '\\left\\{ \\frac{\\pi}{3};\\frac{\\pi}{3};\\frac{\\pi}{3} \\right\\} \\text{ hoặc } \\left\\{ \\frac{2\\pi}{3};\\frac{\\pi}{6};\\frac{\\pi}{6} \\right\\}'

                    # Tạo phương án sai
                    s = [
                        '\\left\\{ \\frac{2\\pi}{3};\\frac{\\pi}{6};\\frac{\\pi}{6} \\right\\}',
                        '\\left\\{ \\frac{\\pi}{3};\\frac{\\pi}{3};\\frac{\\pi}{3} \\right\\}',
                        '\\left\\{ \\frac{\\pi}{3};\\frac{\\pi}{3};\\frac{\\pi}{3} \\right\\}; \\left\\{ \\frac{\\pi}{4};\\frac{\\pi}{4};\\frac{\\pi}{2} \\right\\}',
                        '\\left\\{ \\frac{\\pi}{4};\\frac{\\pi}{4};\\frac{\\pi}{2} \\right\\}; \\left\\{ \\frac{2\\pi}{3};\\frac{\\pi}{6};\\frac{\\pi}{6} \\right\\}'
                    ]
                else:
                    v_str = '\\frac{1}{2}'
                    phi_str = '\\frac{\\pi}{3}'
                    x_str = '\\frac{\\pi}{6}'
                    # Nghiệm thỏa mãn làm góc tam giác: pi/6 hoặc 5*pi/6
                    # Bộ góc tam giác cân có góc pi/6 ở đỉnh: {pi/6, 5pi/12, 5pi/12} hoặc ở đáy: {pi/6, pi/6, 2pi/3}
                    # Bộ góc tam giác cân có góc 5pi/6 ở đỉnh: {5pi/6, pi/12, pi/12}
                    da_str = '\\left\\{ \\frac{\\pi}{6};\\frac{\\pi}{6};\\frac{2\\pi}{3} \\right\\}; \\left\\{ \\frac{\\pi}{6};\\frac{5\\pi}{12};\\frac{5\\pi}{12} \\right\\}; \\left\\{ \\frac{5\\pi}{6};\\frac{\\pi}{12};\\frac{\\pi}{12} \\right\\}'

                    thoa_man_text = 'x = \\frac{\\pi}{6} \\text{ hoặc } x = \\frac{5\\pi}{6}'
                    ket_luan_text = '\\left\\{ \\frac{\\pi}{6};\\frac{\\pi}{6};\\frac{2\\pi}{3} \\right\\}, \\left\\{ \\frac{\\pi}{6};\\frac{5\\pi}{12};\\frac{5\\pi}{12} \\right\\} \\text{ hoặc } \\left\\{ \\frac{5\\pi}{6};\\frac{\\pi}{12};\\frac{\\pi}{12} \\right\\}'

                    s = [
                        '\\left\\{ \\frac{\\pi}{6};\\frac{\\pi}{6};\\frac{2\\pi}{3} \\right\\}',
                        '\\left\\{ \\frac{\\pi}{4};\\frac{\\pi}{4};\\frac{\\pi}{2} \\right\\}',
                        '\\left\\{ \\frac{\\pi}{3};\\frac{\\pi}{3};\\frac{\\pi}{3} \\right\\}; \\left\\{ \\frac{\\pi}{6};\\frac{\\pi}{6};\\frac{2\\pi}{3} \\right\\}',
                        '\\left\\{ \\frac{\\pi}{4};\\frac{\\pi}{4};\\frac{\\pi}{2} \\right\\}; \\left\\{ \\frac{5\\pi}{6};\\frac{\\pi}{12};\\frac{\\pi}{12} \\right\\}'
                    ]

                # Thiết lập đáp án đúng
                da = '$%s$' % da_str

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Tìm số đo ba góc của một tam giác cân biết rằng có số đo của một góc là nghiệm của phương trình $\\cos 2x = %s$?'''
                                 % v_str)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải hoàn chỉnh trình bày chi tiết từng bước như bài mẫu
                loigiai = ('''Ta có: $\\cos 2x = %s \\Leftrightarrow 2x = \\pm %s + k2\\pi \\Leftrightarrow x = \\pm %s + k\\pi, \\left( k \\in \\mathbb{Z} \\right)$. \\\\
                           Do số đo một góc là nghiệm nên $%s$ thỏa mãn. \\\\
                           Vậy tam giác có số đo ba góc là: $%s$.'''
                           % (v_str, phi_str, x_str, thoa_man_text, ket_luan_text))

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

