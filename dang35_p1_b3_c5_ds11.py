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


def bt_dang35_p1_b3_c5_ds11(self):
            # Khai báo biến
            # Chọn k_val là căn bậc hai của cơ số (để f(x) + f(1-x) = 1)
            k_val = random.choice([2, 3, 4, 5]) 
            base_val = k_val**2 

            # Chọn số lượng số hạng n (phải là số chẵn như trong hình mẫu n=200)
            n_val = random.choice([100, 150, 200, 250, 300])

            # --- B1 & B2: Nghiên cứu đề và tính toán ---
            # Số cặp có tổng bằng 1 là từ f(1/n) đến f((n-1)/n) trừ số ở giữa f(1/2)
            # Công thức: num_pairs = (n/2) - 1
            num_pairs = (n_val // 2) - 1

            # f(1/2) luôn bằng 1/2 với dạng hàm này
            f_half = Rational(1, 2)

            # f(1) = base / (base + k)
            f_one = Rational(base_val, base_val + k_val)

            # Tổng A = num_pairs * 1 + f(1/2) + f(1)
            tong_A = num_pairs + f_half + f_one

            # --- B4: Điều chỉnh các phương án sai ---
            da_dung = '$%s$' % (latex(tong_A))
            s_list = []
            while len(s_list) < 3:
                # Tạo đáp án sai xung quanh đáp án đúng
                sai_so = random.choice([Rational(1, 2), Rational(1, 3), 1, 2, Rational(5, 6)])
                huong = random.choice([1, -1])
                da_sai = '$%s$' % (latex(simplify(tong_A + huong * sai_so)))
                if da_sai != da_dung and da_sai not in s_list:
                    s_list.append(da_sai)

            # Đưa vào danh sách và shuffle
            da_d = '\\True ' + da_dung
            list_1 = [da_d, s_list[0], s_list[1], s_list[2]]
            random.shuffle(list_1)

            # --- Nội dung câu hỏi ---
            noidungcauhoi = ('''Cho hàm số $f(x) = \\frac{%s^x}{%s^x + %s}$. Giá trị biểu thức $A = f\\left(\\frac{1}{%s}\\right) + f\\left(\\frac{2}{%s}\\right) + \\dots + f\\left(\\frac{%s}{%s}\\right)$ bằng'''
                             % (latex(base_val), latex(base_val), latex(k_val), 
                                latex(n_val), latex(n_val), latex(n_val), latex(n_val)))

            # --- Nội dung lời giải ---
            # Chia nhỏ để kiểm soát số lượng biến %s chính xác
            lg_1 = ('''Với mọi $a, b$ thỏa mãn $a+b=1$, ta có:\\\\
            $f(a)+f(b) = \\frac{%s^a}{%s^a + %s} + \\frac{%s^b}{%s^b + %s} = \\frac{%s^a(%s^b+%s) + %s^b(%s^a+%s)}{(%s^a+%s)(%s^b+%s)}$\\\\
            $= \\frac{2\\cdot %s^{a+b} + %s(%s^a+%s)}{%s^{a+b} + %s(%s^a+%s) + %s^2} = \\frac{2\\cdot %s + %s(%s^a+%s)}{%s + %s(%s^a+%s) + %s} = 1$.\\\\'''
                % (latex(base_val), latex(base_val), latex(k_val), latex(base_val), latex(base_val), latex(k_val),
                   latex(base_val), latex(base_val), latex(k_val), latex(base_val), latex(base_val), latex(k_val),
                   latex(base_val), latex(k_val), latex(base_val), latex(k_val),
                   latex(base_val), latex(k_val), latex(base_val), latex(base_val),
                   latex(base_val), latex(k_val), latex(base_val), latex(base_val), latex(k_val),
                   latex(base_val), latex(k_val), latex(base_val), latex(base_val),
                   latex(base_val), latex(k_val), latex(base_val), latex(base_val), latex(base_val)))

            lg_2 = ('''Khi đó:\\\\
            $A = \\left[f\\left(\\frac{1}{%s}\\right) + f\\left(\\frac{%s}{%s}\\right)\\right] + \\dots + \\left[f\\left(\\frac{%s}{%s}\\right) + f\\left(\\frac{%s}{%s}\\right)\\right] + f\\left(\\frac{%s}{%s}\\right) + f(1)$\\\\
            $A = %s \\cdot 1 + f\\left(\\frac{1}{2}\\right) + f(1) = %s + \\frac{1}{2} + %s = %s$.\\\\
            Vậy $A = %s$.'''
                % (latex(n_val), latex(n_val-1), latex(n_val),
                   latex(num_pairs), latex(n_val), latex(n_val-num_pairs), latex(n_val),
                   latex(n_val//2), latex(n_val),
                   latex(num_pairs), latex(num_pairs), latex(f_one), latex(tong_A), latex(tong_A)))

            loigiai = lg_1 + lg_2

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

