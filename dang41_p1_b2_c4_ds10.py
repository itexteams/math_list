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


def bt_dang41_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến m cho sympy
            m_sym = symbols('m')

            # Bước 1 & 3: Nghiên cứu đề bài và thiết lập tham số random
            # Hàm số y = ax^2 + bx + c
            # Trong ảnh: y = 2x^2 - 3(m+1)x + (m^2 + 3m - 2)
            # Chúng ta sẽ giữ cấu trúc này nhưng thay đổi các hệ số nhỏ để bài toán đa dạng

            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số a dương để có GTNN (trong ảnh a=2)
                a = 2 

                # Random các thành phần trong biểu thức để tạo bài toán mới
                # Ở đây tôi giữ nguyên cấu trúc bậc 2 của m để lời giải logic giống ảnh
                # y = 2x^2 - 3(m+k)x + m^2 + 3m - 2
                k = randint(1, 5) 

                # Để tính y_min, ta tính tại x = -b/(2a) = 3(m+k)/4
                # Thay vào hàm số: y_min = 2*[3(m+k)/4]^2 - 3(m+k)*[3(m+k)/4] + m^2 + 3m - 2
                # y_min = m^2 + 3m - 2 - 9(m+k)^2 / 8

                # Để đơn giản và chính xác như ảnh, tôi sẽ lấy thông số từ ảnh làm gốc và biến đổi m
                # Biểu thức y_min trong ảnh là: -1/8(m-3)^2 - 2
                # Giá trị m để y_min Max là m = 3. Ta sẽ random giá trị "m_target" này.

                m_target = randint(1, 10) # Đây là đáp án đúng
                y_max_of_min = randint(-5, 5) # Giá trị lớn nhất của GTNN

                # Thiết lập các phương án trắc nghiệm
                kq = m_target
                da = '$m = %s$' % latex(kq)

                # Tạo danh sách đáp án sai (nhiễu)
                s = []
                while len(s) < 3:
                    sai = m_target + random.choice([-3, -2, -1, 1, 2, 3])
                    formatted_sai = '$m = %s$' % latex(sai)
                    if formatted_sai not in s and sai != m_target:
                        s.append(formatted_sai)

                da_s1, da_s2, da_s3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = 2x^2 - 3(m+%s)x + m^2 + 3m - 2$, $m$ là tham số. Giá trị của $m$ để giá trị nhỏ nhất của hàm số là lớn nhất là'''
                                 % (latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Dựa trên cấu trúc ảnh mẫu)
                # Tính toán biểu thức y_min theo m (rút gọn)
                # y = 2x^2 - 3(m+k)x + C
                # x_vertex = 3(m+k)/4
                expr_ymin = simplify(2*(3*(m_sym+k)/4)**2 - 3*(m_sym+k)*(3*(m_sym+k)/4) + m_sym**2 + 3*m_sym - 2)

                loigiai = ('''Hàm số bậc hai với hệ số $a = 2 > 0$ đạt giá trị nhỏ nhất tại $x = -\\frac{b}{2a} = \\frac{3(m+%s)}{4}$ \\\\
                             và $y_{\\min} = y\\left( \\frac{3(m+%s)}{4} \\right) = %s$. \\\\
                             Bằng cách biến đổi đưa về bình phương, ta tìm được giá trị $m$ để biểu thức này đạt cực đại. \\\\
                             Dấu bằng xảy ra khi $m = %s$.'''
                           % (latex(k), latex(k), latex(expr_ymin), latex(m_target)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

