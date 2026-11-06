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


def bt_dang33_p1_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Random các hệ số a, b, c sao cho phương trình đẹp và không đi qua gốc tọa độ (c != 0).
            a_val = random.choice([i for i in range(-5, 6) if i != 0])
            b_val = random.choice([i for i in range(-10, 11) if i != 0])
            c_val = random.choice([i for i in range(-20, 21) if i != 0])

            x, y = symbols('x y')
            duong_thang = a_val*x + b_val*y + c_val

            # Tính toán các giá trị đúng
            k_dung = Rational(-a_val, b_val)
            u_dung = (-b_val, a_val)

            # B4- Điều chỉnh các phương án sai không được trùng đáp án đúng
            # Đáp án đúng (Hệ số góc)
            da_d = '\\True $(d)$ có hệ số góc $k = ' + latex(k_dung) + '$'

            # Sai 1: Vectơ chỉ phương sai (thường lấy nhầm vectơ pháp tuyến hoặc sai dấu)
            u_sai = (a_val, b_val) 
            da_s1 = '$\\vec{u} = (' + str(u_sai[0]) + ';' + str(u_sai[1]) + ')$ là vectơ chỉ phương của $(d)$'

            # Sai 2: Đi qua gốc tọa độ (vì c luôn != 0 nên mệnh đề này luôn sai)
            da_s2 = '$(d)$ đi qua gốc tọa độ'

            # Sai 3: Hệ số góc sai (nghịch đảo hoặc nhầm công thức b/a)
            k_sai = Rational(b_val, a_val)
            if k_sai == k_dung:
                k_sai = k_dung + 1
            da_s3 = '$(d)$ có hệ số góc $k = ' + latex(k_sai) + '$'

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung câu hỏi
            noidungcauhoi = ('Cho đường thẳng $(d): ' + latex(duong_thang) + ' = 0$. Mệnh đề nào sau đây đúng?')

            # Nội dung lời giải chi tiết giống trong ảnh
            # Biến đổi ax + by + c = 0 thành y = kx + m
            buoc_chuyen = latex(b_val) + 'y = ' + latex(-a_val*x) + ' ' + ('-' if c_val > 0 else '+') + ' ' + latex(abs(c_val))
            phuong_trinh_y = 'y = ' + latex(k_dung) + 'x + ' + latex(Rational(-c_val, b_val))

            loigiai = ('Ta có $(d): ' + latex(duong_thang) + ' = 0$ hay $' + phuong_trinh_y + '$. \\\\ '
                       'Suy ra hệ số góc của đường thẳng là $k = ' + latex(k_dung) + '$.')

            # B2- Xuất câu trắc nghiệm theo mẫu (Không dùng tiền tố r)
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

