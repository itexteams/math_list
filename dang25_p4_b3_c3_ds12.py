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


def bt_dang25_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # a là cận (thường là 1 hoặc 2 để số không quá lớn)
                # n là số mũ (chọn số chẵn để biểu thức sqrt(a^n - x^n) xác định trên [-a, a])
                a = random.choice([1, 2])
                n = random.choice([2, 4])

                # Biểu thức cạnh hình vuông: sqrt(a^n - x^n)
                canh = sqrt(a**n - x**n)
                # Diện tích mặt cắt S(x) = canh^2
                Sx = a**n - x**n

                # Tính toán thể tích V = tích phân từ -a đến a của Sx
                # Sử dụng \text{d}x theo yêu cầu
                V_val = integrate(Sx, (x, -a, a))

                # Đáp án đúng
                kq = latex(V_val)
                da = '$%s$' % kq

                # Bước 4: Điều chỉnh các phương án sai không trùng đáp án đúng
                # Các phương án sai phổ biến: thiếu tích phân, nhầm công thức khối tròn xoay (nhân pi), hoặc sai cận
                s_options = []

                # Sai 1: Quên không bình phương cạnh (nếu tích phân tính được số hữu tỉ)
                W1 = integrate(canh, (x, -a, a))
                if W1 != V_val: s_options.append('$%s$' % latex(W1))

                # Sai 2: Nhầm sang công thức vật thể tròn xoay (nhân thêm pi)
                W2 = pi * V_val
                if W2 != V_val: s_options.append('$%s$' % latex(W2))

                # Sai 3: Tính tích phân từ 0 đến a (nửa thể tích)
                W3 = integrate(Sx, (x, 0, a))
                if W3 != V_val: s_options.append('$%s$' % latex(W3))

                # Sai 4: Một giá trị ngẫu nhiên khác
                W4 = V_val + Rational(1, 2)
                if W4 != V_val: s_options.append('$%s$' % latex(W4))

                # Đảm bảo đủ số lượng đáp án sai
                while len(s_options) < 3:
                    random_val = V_val + random.randint(1, 5)
                    if random_val != V_val:
                        s_options.append('$%s$' % latex(random_val))

                das1 = '$%s$' % latex(V_val + 1)
                das2 = '$%s$' % latex(V_val + 2)
                das3 = '$%s$' % latex(V_val - 1)

                # Câu hỏi
                noidungcauhoi = (r'''Cho một vật thể giới hạn bởi hai mặt phẳng vuông góc với trục $Ox$ tại các điểm có hoành độ $x = -%s$ và $x = %s$. Một mặt phẳng vuông góc với trục $Ox$ tại $x$ ($-%s \le x \le %s$) cắt vật thể đó theo một mặt cắt là hình vuông có cạnh bằng $%s$. Tính thể tích vật thể.'''
                                 %(latex(a), latex(a), latex(a), latex(a), latex(canh)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Sử dụng \text{d}x)
                # Nguyên hàm của Sx
                nguyen_ham = integrate(Sx, x)

                loigiai = (r'''Diện tích hình vuông cạnh $%s$ là $S(x) = \left(%s\right)^2 = %s$. \\
                             Thể tích cần tìm là $V = \int_{-%s}^{%s} S(x) \text{d}x = \int_{-%s}^{%s} \left(%s\right) \text{d}x = \left(%s\right) \bigg|_{-%s}^{%s} = %s$.'''
                           %(latex(canh), latex(canh), latex(Sx), 
                             latex(a), latex(a), latex(a), latex(a), latex(Sx), 
                             latex(nguyen_ham), latex(a), latex(a), latex(V_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

