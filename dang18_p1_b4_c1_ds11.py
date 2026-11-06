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


def bt_dang18_p1_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và tạo tính ngẫu nhiên cho bài toán (B3)
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            if dang == '1':
                # Dạng gốc từ hình ảnh: cos(x + \pi/4) = \sqrt{2}/2
                goc_alpha = '\\frac{\\pi}{4}'
                ve_phai = '\\frac{\\sqrt{2}}{2}'

                # Nghiệm nhánh 1: x + \pi/4 = \pi/4 + k2\pi => x = k2\pi
                # Nghiệm nhánh 2: x + \pi/4 = -\pi/4 + k2\pi => x = -\pi/2 + k2\pi
                n1_d = 'k2\\pi'
                n2_d = '-\\frac{\\pi}{2} + k2\\pi'

                # Các tổ hợp nghiệm sai để làm phương án nhiễu (B4)
                n1_s1 = 'k2\\pi'
                n2_s1 = '-\\frac{\\pi}{2} + k\\pi'

                n1_s2 = 'k\\pi'
                n2_s2 = '-\\frac{\\pi}{2} + k\\pi'

                n1_s3 = 'k\\pi'
                n2_s3 = '-\\frac{\\pi}{2} + k2\\pi'

            else:
                # Dạng biến đổi ngẫu nhiên: cos(x + \pi/3) = 1/2
                goc_alpha = '\\frac{\\pi}{3}'
                ve_phai = '\\frac{1}{2}'

                # Nghiệm nhánh 1: x + \pi/3 = \pi/3 + k2\pi => x = k2\pi
                # Nghiệm nhánh 2: x + \pi/3 = -\pi/3 + k2\pi => x = -2\pi/3 + k2\pi
                n1_d = 'k2\\pi'
                n2_d = '-\\frac{2\\pi}{3} + k2\\pi'

                # Các tổ hợp nghiệm sai tương ứng
                n1_s1 = 'k2\\pi'
                n2_s1 = '-\\frac{2\\pi}{3} + k\\pi'

                n1_s2 = 'k\\pi'
                n2_s2 = '-\\frac{2\\pi}{3} + k\\pi'

                n1_s3 = 'k\\pi'
                n2_s3 = '-\\frac{2\\pi}{3} + k2\\pi'

            # Cấu trúc chuỗi hiển thị câu hỏi dùng định dạng %s
            noidungcauhoi = ('''Nghiệm của phương trình $\\cos \\left( x + %s \\right) = %s$ là''' 
                             % (goc_alpha, ve_phai))

            # Cấu trúc lời giải hiển thị chi tiết từng bước bằng hệ thống ngoặc nhọn hệ phương trình của LaTeX
            loigiai = ('''Phương trình $\\cos \\left( x + %s \\right) = %s \\Leftrightarrow \\cos \\left( x + %s \\right) = \\cos \\left( %s \\right) \\Leftrightarrow \\left[\\begin{aligned} & x + %s = %s + k2\\pi \\\\ & x + %s = -%s + k2\\pi \\end{aligned}\\right. \\Leftrightarrow \\left[\\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned}\\right. (k \\in \\mathbb{Z})$.'''
                       % (goc_alpha, ve_phai, goc_alpha, goc_alpha, goc_alpha, goc_alpha, goc_alpha, goc_alpha, n1_d, n2_d))

            # Tạo chuỗi hiển thị cho các phương án trắc nghiệm hình dấu ngoặc vuông vuông (Đảm bảo không chứa dấu chấm ở cuối)
            da_text = '\\left[\\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned}\\right. (k \\in \\mathbb{Z})' % (n1_d, n2_d)
            das1_text = '\\left[\\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned}\\right. (k \\in \\mathbb{Z})' % (n1_s1, n2_s1)
            das2_text = '\\left[\\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned}\\right. (k \\in \\mathbb{Z})' % (n1_s2, n2_s2)
            das3_text = '\\left[\\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned}\\right. (k \\in \\mathbb{Z})' % (n1_s3, n2_s3)

            da_d = ('\\True $' + str(da_text) + '$')
            da_s1 = '$' + str(das1_text) + '$'
            da_s2 = '$' + str(das2_text) + '$'
            da_s3 = '$' + str(das3_text) + '$'

            # Đưa các đáp án vào một danh sách chọn ngẫu nhiên thứ tự hiển thị
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo định dạng minipage mẫu cấu trúc đề bài yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

