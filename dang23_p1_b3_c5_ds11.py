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


def bt_dang23_p1_b3_c5_ds11(self):
            # Khai báo biến
            # --- KHỞI TẠO DỮ LIỆU ---
            lis_base = ['e', 2, 3, 5]
            base_val = random.choice(lis_base)

            # Thiết lập hàm số và điểm đúng
            if base_val == 'e':
                ham_so_tex = r'\ln x'
                # Các điểm thuộc đồ thị: (x, y)
                pts = [(1, 0), ('e', 1), ('e^2', 2)]
                p_select = random.choice(pts)
                x_val_tex = str(p_select[0])
                y_val_tex = str(p_select[1])
                loi_giai_tinh = r'\ln ' + x_val_tex + ' = ' + y_val_tex
            else:
                a = base_val
                ham_so_tex = r'\log_{%s} x' % a
                pts = [(1, 0), (a, 1), (a**2, 2)]
                p_select = random.choice(pts)
                x_val_tex = str(p_select[0])
                y_val_tex = str(p_select[1])
                loi_giai_tinh = r'\log_{%s} %s = %s' % (a, x_val_tex, y_val_tex)

            # Đáp án đúng
            da_dung = '(%s; %s)' % (x_val_tex, y_val_tex)

            # --- TẠO PHƯƠNG ÁN SAI (BƯỚC 4) ---
            s = []
            # Nhiễu 1: Đảo ngược tọa độ
            nhieu1 = '(%s; %s)' % (y_val_tex, x_val_tex)
            if nhieu1 != da_dung: s.append(nhieu1)

            # Nhiễu 2: Thay đổi giá trị y
            nhieu2 = '(%s; %s)' % (x_val_tex, random.choice(['-1', '3', '0' if y_val_tex != '0' else '1']))
            if nhieu2 != da_dung: s.append(nhieu2)

            # Nhiễu 3: Điểm có tọa độ âm (log ko xác định)
            nhieu3 = '(-1; 0)'
            if nhieu3 != da_dung: s.append(nhieu3)

            # Nhiễu 4: Điểm ngẫu nhiên khác
            nhieu4 = '(0; 1)'
            if nhieu4 != da_dung: s.append(nhieu4)

            # Lấy 3 phương án sai duy nhất
            list_sai = list(set(s))
            random.shuffle(list_sai)
            das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = r'Đồ thị hàm số $y = %s$ đi qua điểm nào sau đây?' % ham_so_tex

            # Các đáp án
            da_d = r'\True $%s$' % da_dung
            da_s1 = '$%s$' % das1
            da_s2 = '$%s$' % das2
            da_s3 = '$%s$' % das3

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # --- NỘI DUNG LỜI GIẢI ---
            loigiai = r'''Với $x = %s \Rightarrow y = %s$. \\
                          Vậy đồ thị hàm số đi qua điểm $(%s; %s)$.''' % (x_val_tex, loi_giai_tinh, x_val_tex, y_val_tex)

            # --- XUẤT KẾT QUẢ ---
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n')
            return content

