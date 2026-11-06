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


def bt_dang38_p4_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- BƯỚC RANDOM SỐ LIỆU ---
                # Chọn bán kính R1 ngẫu nhiên trong khoảng từ 10 đến 100
                r1 = randint(10, 100)

                # Tính toán kết quả đúng
                # Theo bài toán: h = 4 * R1
                kq_val = 4 * r1
                kq = str(kq_val)

                # Tạo các phương án nhiễu
                # Nhiễu 1: Chỉ tính tổng bán kính (2 * R1)
                ans_wrong1 = 2 * r1
                # Nhiễu 2: Tính sai công thức (3 * R1)
                ans_wrong2 = 3 * r1
                # Nhiễu 3: Kết quả đúng cộng lệch một chút hoặc 5 * R1
                ans_wrong3 = 5 * r1

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                s = [
                    '$%s$'%(ans_wrong1),
                    '$%s$'%(ans_wrong2),
                    '$%s$'%(ans_wrong3),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- NỘI DUNG CÂU HỎI ---
                noidungcauhoi = ('''Một mô hình gồm các khối cầu xếp chồng lên nhau tạo thành một cột thẳng đứng. Biết rằng mỗi khối cầu có bán kính gấp đôi khối cầu nằm ngay trên nó và bán kính khối cầu dưới cùng là $%s$ cm. Tính chiều cao (đơn vị: cm) của mô hình.'''
                                  %(r1))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # --- NỘI DUNG LỜI GIẢI ---
                # Sử dụng raw string (r'...') để tránh lỗi escape ký tự \ trong LaTeX
                loigiai = r'''Gọi bán kính khối cầu dưới cùng là $R_1 = %s$ cm. \\
                Gọi $R_2, R_3, \dots, R_n$ lần lượt là bán kính của các khối cầu nằm ngay trên khối cầu dưới cùng. \\
                Ta có $R_2 = \frac{R_1}{2}, R_3 = \frac{R_2}{2} = \frac{R_1}{4}, \dots, R_n = \frac{R_{n-1}}{2} = \frac{R_1}{2^{n-1}}$. \\
                Gọi $h_n$ là chiều cao của mô hình gồm có $n$ khối cầu chồng lên nhau. \\
                Ta có:
                $$h_n = 2R_1 + 2R_2 + \dots + 2R_n = 2\left(R_1 + \frac{1}{2}R_1 + \dots + \frac{1}{2^{n-1}}R_1\right) = 2R_1 \left(1 + \frac{1}{2} + \dots + \frac{1}{2^{n-1}}\right)$$
                Suy ra chiều cao mô hình là:
                $$h = \lim_{n \to +\infty} h_n = \lim_{n \to +\infty} \left[ 2R_1 \left(1 + \frac{1}{2} + \frac{1}{4} + \dots + \frac{1}{2^{n-1}} \right) \right]$$
                Xét dãy số $1; \frac{1}{2}; \frac{1}{4}; \dots; \frac{1}{2^{n-1}}; \dots$ là một cấp số nhân lùi vô hạn có $u_1 = 1$ và công bội $q = \frac{1}{2}$ nên tổng của dãy là:
                $$S = \frac{1}{1 - \frac{1}{2}} = 2$$
                Suy ra $h = 2R_1 \cdot 2 = 4R_1 = 4 \cdot %s = %s$ (cm). \\
                Vậy chiều cao mô hình là $%s$ cm.''' % (r1, r1, kq, kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

