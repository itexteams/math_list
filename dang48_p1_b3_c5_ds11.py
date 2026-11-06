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


def bt_dang48_p1_b3_c5_ds11(self):
            # Khai báo biến
            # --- Hàm hỗ trợ chuyển dấu chấm thành dấu phẩy cho số thập phân ---
            def format_vn(value):
                # Nếu là số nguyên thì trả về chuỗi nguyên, nếu là số thực thì thay . bằng ,
                s = str(value)
                if '.' in s:
                    # Loại bỏ .0 nếu là số nguyên (ví dụ 42.0 -> 42)
                    if s.endswith('.0'):
                        return s[:-2]
                    return s.replace('.', ',')
                return s

            # --- B3: Tư duy Random bài toán ---
            lis_mu = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]
            mu_val = random.choice(lis_mu)
            depth_val = random.randint(10, 50) 

            # Tính số mũ k = mu * depth
            k_val = round(mu_val * depth_val, 1)

            # Chuyển đổi sang định dạng tiếng Việt (dùng dấu phẩy)
            mu = format_vn(mu_val)
            depth = format_vn(depth_val)
            k = format_vn(k_val)

            # --- Thiết lập đáp án ---
            # Đáp án đúng là e^k
            da_dung = '$e^{%s}$ lần' % (k)

            # Tạo các đáp án nhiễu (sử dụng format_vn cho các số lẻ nếu có)
            s = [
                '$e^{-%s}$ lần' % (k),
                '$e^{%s}$ lần' % (format_vn(round(k_val/2, 1))),
                '$e^{%s}$ lần' % (format_vn(k_val + 10)),
                '$e^{-%s}$ lần' % (format_vn(2*k_val)),
                '$e^{21}$ lần' # Giữ một số đáp án tĩnh nếu muốn giống đề mẫu
            ]

            random.shuffle(s)
            das1, das2, das3 = s[:3]

            # --- Nội dung câu hỏi ---
            noidungcauhoi = ('''Cường độ ánh sáng đi qua môi trường nước biển giảm dần theo công thức $I = I_0 e^{-\\mu x}$, với $I_0$ là cường độ ánh sáng lúc ánh sáng bắt đầu đi vào môi trường nước biển và $x$ là độ dày của môi trường đó (độ sâu). Biết rằng môi trường nước biển có hằng số hấp thụ là $\\mu = %s$. Hỏi ở độ sâu $%s$ mét thì cường độ ánh sáng giảm đi bao nhiêu lần so với cường độ ánh sáng lúc ánh sáng bắt đầu đi vào nước biển?'''
                             %(mu, depth))

            # --- Nội dung lời giải ---
            loigiai = ('''Khi mới bắt đầu đi vào môi trường nước biển thì $x=0 \\Rightarrow I_1 = I_0 \\cdot e^0$. \\\\
            Ở độ sâu $%s$ mét thì $I_2 = I_0 \\cdot e^{-\\mu \\cdot %s} = I_0 \\cdot e^{-%s \\cdot %s} = I_0 \\cdot e^{-%s}$. \\\\
            Vậy ta có: $\\frac{I_1}{I_2} = \\frac{I_0 \\cdot e^0}{I_0 \\cdot e^{-%s}} = e^{%s}$. \\\\
            Vậy cường độ ánh sáng $I_2$ giảm $e^{%s}$ lần so với $I_1$.'''
                       %(depth, depth, mu, depth, k, k, k, k))

            # --- Xuất câu trắc nghiệm theo mẫu ---
            da_d = '\\True ' + da_dung
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

