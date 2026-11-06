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


def bt_dang4_p3_b3_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến và logic random
            lis_k = [2, 3, 4]  # Hệ số k trong f(kx)
            k = random.choice(lis_k)
            k2 = k**2
            k4 = k**4

            h_k_val = random.randint(2, 15)  # Giá trị h''(k)
            h_1_val = random.randint(2, 15)  # Giá trị h''(1)


            g_k_val = k2 * h_k_val
            da_val = h_1_val + g_k_val

            # Chuyển số sang định dạng chuỗi có dấu phẩy nếu là số thập phân (ở đây là số nguyên)
            da = str(da_val).replace('.', ',')

            # Tạo các phương án sai không trùng với đáp án đúng
            s = []
            while len(s) < 3:
                sai = da_val + random.choice([-10, -5, 5, 10, 15, 20, -15])
                if sai != da_val and sai > 0 and str(sai) not in s:
                    s.append('$%s$' % (str(sai).replace('.', ',')))

            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Câu hỏi
            noidungcauhoi = ('''Biết hàm số $y = f\\left(x\\right) - f\\left(%sx\\right)$ liên tục trên $\\mathbb{R}$ và có đạo hàm cấp hai với mọi $x \\in \\mathbb{R}$, biết $y''\\left(%s\\right) = %s, y''\\left(1\\right) = %s$. Đạo hàm cấp hai của hàm số $g\\left(x\\right) = f\\left(x\\right) - f\\left(%sx\\right)$ tại $x = 1$ bằng bao nhiêu?'''
                             % (latex(k), latex(k), latex(h_k_val), latex(h_1_val), latex(k2)))

            # Các đáp án
            da_d = ('\\True $' + str(da) + '$')
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Trộn phương án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ('''Đặt $h\\left(x\\right) = f\\left(x\\right) - f\\left(%sx\\right)$ và $g\\left(x\\right) = f\\left(x\\right) - f\\left(%sx\\right)$.\\\\
            Ta có $h'\\left(x\\right) = f'\\left(x\\right) - %sf'\\left(%sx\\right) \\Rightarrow h''\\left(x\\right) = f''\\left(x\\right) - %sf''\\left(%sx\\right)$.\\\\
            Tương tự $g'\\left(x\\right) = f'\\left(x\\right) - %sf'\\left(%sx\\right) \\Rightarrow g''\\left(x\\right) = f''\\left(x\\right) - %sf''\\left(%sx\\right)$.\\\\
            Tại $x=1$ ta có $g''\\left(1\\right) = f''\\left(1\\right) - %sf''\\left(%s\\right)$.\\\\
            Theo giả thiết ta có hệ phương trình:\\\\
            $\\begin{cases} h''\\left(%s\\right) = f''\\left(%s\\right) - %sf''\\left(%s\\right) = %s & (1) \\\\ h''\\left(1\\right) = f''\\left(1\\right) - %sf''\\left(%s\\right) = %s & (2) \\end{cases}$\\\\
            Từ $(1)$ nhân cả hai vế với $%s$ ta được:\\\\
            $%sf''\\left(%s\\right) - %sf''\\left(%s\\right) = %s \\quad (3)$.\\\\
            Cộng từng vế của $(2)$ và $(3)$ ta được:\\\\
            $f''\\left(1\\right) - %sf''\\left(%s\\right) = %s + %s = %s$.\\\\
            Vậy $g''\\left(1\\right) = %s$.'''
                       % (latex(k), latex(k2),
                          latex(k), latex(k), latex(k2), latex(k),
                          latex(k2), latex(k2), latex(k4), latex(k2),
                          latex(k4), latex(k2),
                          latex(k), latex(k), latex(k2), latex(k2), latex(h_k_val),
                          latex(k2), latex(k), latex(h_1_val),
                          latex(k2), latex(k2), latex(k), latex(k4), latex(k2), latex(g_k_val),
                          latex(k4), latex(k2), latex(h_1_val), latex(g_k_val), latex(da_val),
                          latex(da_val)
                          ))
            dapan='\\shortans[0]{$%s$}\n'%(da_val)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content   

