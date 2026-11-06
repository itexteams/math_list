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


def bt_dang22_p1_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random u1 và q
                u1 = random.choice([-2, -3, -4, -5, 2, 3, 4, 5])
                q = random.choice([2, 3, 4, 5, -2, -3, -4, -5])

                # Tính các số hạng tiếp theo
                u2 = u1 * q
                u3 = u2 * q
                u4 = u3 * q

                # Tính bình phương
                x_sq = u1 * u3

                # Hai trường hợp của x
                x1 = math.isqrt(x_sq)
                x2 = -x1

                # Tính y tương ứng
                y1 = (u3 * u3) / x1 if x1 != 0 else 0
                y2 = (u3 * u3) / x2 if x2 != 0 else 0

                # Xử lý format int cho số nguyên
                if y1 == int(y1): y1 = int(y1)
                if y2 == int(y2): y2 = int(y2)


                da_x = u2
                da_y = u4

                da = '$\\begin{cases} x = %s \\\\ y = %s \\end{cases}$' % (da_x, da_y)

                # Tạo các phương án sai
                # Phương án 1: Sai dấu cả x và y
                s1_x = -da_x
                s1_y = da_y+1

                # Phương án 2: Sai dấu của x
                s2_x = -da_x
                s2_y = da_y

                # Phương án 3: Sai dấu của y
                s3_x = da_x
                s3_y = -da_y

                # Phương án 4: Số cộng (cấp số cộng nhiễu)
                d = (u3 - u1) / 2
                s4_x = int(u1 + d)
                s4_y = int(u3 + d)

                s = [
                    '$\\begin{cases} x = %s \\\\ y = %s \\end{cases}$' % (s1_x, s1_y),
                    '$\\begin{cases} x = %s \\\\ y = %s \\end{cases}$' % (s2_x, s2_y),
                    '$\\begin{cases} x = %s \\\\ y = %s \\end{cases}$' % (s3_x, s3_y),
                    '$\\begin{cases} x = %s \\\\ y = %s \\end{cases}$' % (s4_x, s4_y)
                ]

                # Loại bỏ các đáp án trùng
                s_unique = []
                for opt in s:
                    if opt != da and opt not in s_unique:
                        s_unique.append(opt)

                # Đảm bảo đủ 3 phương án sai
                while len(s_unique) < 3:
                    rand_x = random.randint(-10, 10)
                    rand_y = random.randint(-50, 50)
                    opt = '$\\begin{cases} x = %s \\\\ y = %s \\end{cases}$' % (rand_x, rand_y)
                    if opt != da and opt not in s_unique:
                        s_unique.append(opt)

                random.shuffle(s_unique)
                das1 = s_unique[0]
                das2 = s_unique[1]
                das3 = s_unique[2]

                # Câu hỏi
                noidungcauhoi = ('''Với giá trị $x$, $y$ nào dưới đây thì các số hạng lần lượt là $%s$; $x$; $%s$; $y$ theo thứ tự đó lập thành cấp số nhân?'''
                                 % (u1, u3))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Theo tính chất của cấp số nhân, ta có: $x^2 = %s \\cdot (%s) = %s \\Leftrightarrow \\left[ \\begin{array}{l} x = %s \\\\ x = %s \\end{array} \\right.$. \\\\
                             Với $x = %s$, ta có công bội $q = \\frac{%s}{%s} = %s$. Suy ra $y = %s \\cdot (%s) = %s$. \\\\
                             Với $x = %s$, ta có công bội $q = \\frac{%s}{%s} = %s$. Suy ra $y = %s \\cdot (%s) = %s$. \\\\
                             Đối chiếu các phương án, ta chọn đáp án thỏa mãn một trong hai trường hợp trên (trong câu hỏi này là trường hợp $x = %s, y = %s$).'''
                             % (u1, u3, x_sq, x1, x2,
                                x1, x1, u1, frac(x1, u1) if u1 != 0 else 0, u3, frac(x1, u1) if u1 != 0 else 0, int(u3 * frac(x1, u1)) if u1 != 0 else 0,
                                x2, x2, u1, frac(x2, u1) if u1 != 0 else 0, u3, frac(x2, u1) if u1 != 0 else 0, int(u3 * frac(x2, u1)) if u1 != 0 else 0,
                                da_x, da_y))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

