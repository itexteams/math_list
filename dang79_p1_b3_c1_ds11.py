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


def bt_dang79_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1', '2']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bài toán gốc: y = sin(x) trên khoảng (5pi/4; 7pi/4)
                # Cực tiểu tại x = 3pi/2 có sin(x) = -1. Các đầu mút là -sqrt(2)/2
                # Tập giá trị là [-1; -sqrt(2)/2)
                ten_ham = '\\sin x'
                khoang_x = '\\left(\\frac{5\\pi}{4};\\frac{7\\pi}{4}\\right)'

                # Định dạng chuỗi đáp án đúng (thay thế dấu chấm thập phân bằng dấu phẩy)
                da = '\\left[-1;-\\frac{\\sqrt{2}}{2}\\right)'

                # Các đáp án nhiễu
                s = [
                    '\\left[-\\frac{\\sqrt{2}}{2};0\\right]',
                    '[-1;1]',
                    '\\left[\\frac{\\sqrt{2}}{2};1\\right]',
                    '\\left(-1;-\\frac{\\sqrt{2}}{2}\\right)',
                    '\\left[-\\frac{\\sqrt{2}}{2};1\\right]'
                ]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                noidungcauhoi = ('''Khi $x$ thay đổi trong khoảng $%s$ thì $y = %s$ lấy mọi giá trị thuộc''' 
                                 % (khoang_x, ten_ham))

                loigiai = (''' - Trong nửa khoảng $\\left(\\frac{5\\pi}{4};\\frac{3\\pi}{2}\\right]$:\\\\
                           Hàm số $y = \\sin x$ giảm nên $\\sin\\frac{3\\pi}{2} \\le \\sin x < \\sin\\frac{5\\pi}{4} \\Rightarrow -1 \\le \\sin x < -\\frac{\\sqrt{2}}{2}$.\\\\
                           - Trong nửa khoảng $\\left[\\frac{3\\pi}{2};\\frac{7\\pi}{4}\\right)$:\\\\
                           Hàm số $y = \\sin x$ tăng nên $\\sin\\frac{3\\pi}{2} \\le \\sin x < \\sin\\frac{7\\pi}{4} \\Rightarrow -1 \\le \\sin x < -\\frac{\\sqrt{2}}{2}$.\\\\
                           - Vậy khi $x$ thay đổi trong khoảng $%s$ thì $y = %s$ lấy mọi giá trị thuộc $%s$.'''
                           % (khoang_x, ten_ham, da))

            elif dang=='2':
                # Bài toán tương tự phát triển: y = cos(x) trên khoảng (3pi/4; 5pi/4)
                # Cực tiểu tại x = pi có cos(x) = -1. Các đầu mút là -sqrt(2)/2
                # Tập giá trị là [-1; -sqrt(2)/2)
                ten_ham = '\\cos x'
                khoang_x = '\\left(\\frac{3\\pi}{4};\\frac{5\\pi}{4}\\right)'

                da = '\\left[-1;-\\frac{\\sqrt{2}}{2}\\right)'

                s = [
                    '\\left[-\\frac{\\sqrt{2}}{2};0\\right]',
                    '[-1;1]',
                    '\\left[\\frac{\\sqrt{2}}{2};1\\right]',
                    '\\left(-1;-\\frac{\\sqrt{2}}{2}\\right)',
                    '\\left(0;\\frac{\\sqrt{2}}{2}\\right]'
                ]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                noidungcauhoi = ('''Khi $x$ thay đổi trong khoảng $%s$ thì $y = %s$ lấy mọi giá trị thuộc''' 
                                 % (khoang_x, ten_ham))

                loigiai = (''' - Trong nửa khoảng $\\left(\\frac{3\\pi}{4};\\pi\\right]$:\\\\
                           Hàm số $y = \\cos x$ giảm nên $\\cos\\pi \\le \\cos x < \\cos\\frac{3\\pi}{4} \\Rightarrow -1 \\le \\cos x < -\\frac{\\sqrt{2}}{2}$.\\\\
                           - Trong nửa khoảng $\\left[\\pi;\\frac{5\\pi}{4}\\right)$:\\\\
                           Hàm số $y = \\cos x$ tăng nên $\\cos\\pi \\le \\cos x < \\cos\\frac{5\\pi}{4} \\Rightarrow -1 \\le \\cos x < -\\frac{\\sqrt{2}}{2}$.\\\\
                           - Vậy khi $x$ thay đổi trong khoảng $%s$ thì $y = %s$ lấy mọi giá trị thuộc $%s$.'''
                           % (khoang_x, ten_ham, da))

            # Cài đặt cấu trúc đáp án chuẩn hóa đầu ra
            da_d = ('\\True ' + '$' + str(da) + '$')
            da_s1 = '$' + str(das1) + '$'
            da_s2 = '$' + str(das2) + '$'
            da_s3 = '$' + str(das3) + '$'

            # Trộn thứ tự phương án chọn
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
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

