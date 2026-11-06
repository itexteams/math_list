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


def bt_dang12_p3_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random một hệ số nguyên dương k từ 1 đến 6 để nhân vào biểu thức gốc nhằm tạo sự đổi mới cho câu hỏi
                # Biểu thức gốc có a = 4, khi nhân thêm k vào cả 2 vế thì giá trị a mới sẽ bằng 4 * k (luôn là số nguyên)
                k = randint(1, 6)
                a_val = 4 * k

                # Đáp án đúng
                da = '$%s$' % (latex(a_val))

                # Tạo các phương án nhiễu (luôn là số nguyên và không trùng với đáp án đúng)
                s = []
                cac_phuong_an_nhieu = [1*k, 2*k, 3*k, 5*k, 6*k, 8*k, 2, 4, 8]
                for phan_tu in cac_phuong_an_nhieu:
                    val_sai = '$%s$' % (latex(phan_tu))
                    if val_sai != da and val_sai not in s:
                        s.append(val_sai)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Thiết lập chuỗi hiển thị theo hệ số k
                if k == 1:
                    str_ve_trai = '\\tan^2 x + \\cot^2 x + 2'
                    str_lg1 = '(\\tan^2 x + 1) + (\\cot^2 x + 1)'
                    str_lg2 = '\\frac{1}{\\cos^2 x} + \\frac{1}{\\sin^2 x}'
                    str_lg3 = '\\frac{\\sin^2 x + \\cos^2 x}{\\sin^2 x \\cos^2 x}'
                    str_lg4 = '\\frac{1}{\\sin^2 x \\cos^2 x}'
                    str_lg5 = '\\frac{1}{(\\sin x \\cos x)^2}'
                    str_lg6 = '\\frac{1}{\\frac{1}{4}\\sin^2 2x}'
                else:
                    str_ve_trai = '%s\\left(\\tan^2 x + \\cot^2 x + 2\\right)' % (latex(k))
                    str_lg1 = '%s\\left[(\\tan^2 x + 1) + (\\cot^2 x + 1)\\right]' % (latex(k))
                    str_lg2 = '%s\\left(\\frac{1}{\\cos^2 x} + \\frac{1}{\\sin^2 x}\\right)' % (latex(k))
                    str_lg3 = '%s\\left(\\frac{\\sin^2 x + \\cos^2 x}{\\sin^2 x \\cos^2 x}\\right)' % (latex(k))
                    str_lg4 = '%s\\left(\\frac{1}{\\sin^2 x \\cos^2 x}\\right)' % (latex(k))
                    str_lg5 = '%s\\left(\\frac{1}{(\\sin x \\cos x)^2}\\right)' % (latex(k))
                    str_lg6 = '%s\\left(\\frac{1}{\\frac{1}{4}\\sin^2 2x}\\right)' % (latex(k))

                # Câu hỏi
                noidungcauhoi = ('''Biết $%s = \\frac{a}{\\sin^2 2x}$. Giá trị của $a$ bằng bao nhiêu?''' % (str_ve_trai))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước rõ ràng như ảnh mẫu
                loigiai = ('''$%s = \\frac{%s}{\\sin^2 2x} \\Leftrightarrow %s = \\frac{%s}{\\sin^2 2x}$ \\\\
                           $\\Leftrightarrow %s = \\frac{%s}{\\sin^2 2x} \\Leftrightarrow %s = \\frac{%s}{\\sin^2 2x}$ \\\\
                           $\\Leftrightarrow %s = \\frac{%s}{\\sin^2 2x} \\Leftrightarrow %s = \\frac{%s}{\\sin^2 2x}$ \\\\
                           $\\Leftrightarrow %s = \\frac{%s}{\\sin^2 2x}$. \\\\
                           Vậy $a = %s$.'''
                           % (str_ve_trai, latex(a_val), str_lg1, latex(a_val),
                              str_lg2, latex(a_val), str_lg3, latex(a_val),
                              str_lg4, latex(a_val), str_lg5, latex(a_val),
                              str_lg6, latex(a_val), latex(a_val)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(a_val))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

