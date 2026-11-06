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


def bt_dang34_p1_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Sinh ngẫu nhiên ba cạnh a, b, c tạo thành tam giác hợp lệ với a < b < c
                valid_triangle = False
                while not valid_triangle:
                    sides = random.sample(range(2, 10), 3)
                    sides.sort()
                    a, b, c = sides[0], sides[1], sides[2]
                    # Điều kiện tồn tại tam giác
                    if a + b > c:
                        valid_triangle = True

                # Tính cos góc bé nhất (góc A đối diện cạnh a)
                cosA_val = Rational(b**2 + c**2 - a**2, 2*b*c)

                # Tính sin góc bé nhất
                sinA_val = simplify(sqrt(1 - cosA_val**2))

                # Tính cos và sin các góc khác làm phương án nhiễu (sai lầm thường gặp)
                cosB_val = Rational(a**2 + c**2 - b**2, 2*a*c)
                sinB_val = simplify(sqrt(1 - cosB_val**2))

                cosC_val = Rational(a**2 + b**2 - c**2, 2*a*b)
                sinC_val = simplify(sqrt(1 - cosC_val**2))

                kq = latex(sinA_val)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Lọc các phương án sai đảm bảo không trùng với đáp án đúng
                distractors = [cosA_val, sinB_val, sinC_val]
                unique_s = []
                for d in distractors:
                    if d != sinA_val and d not in unique_s:
                        unique_s.append(d)

                # Bổ sung nhiễu nếu chưa đủ 3 phương án sai
                while len(unique_s) < 3:
                    # Sinh nhiễu bằng cách lấy căn ngẫu nhiên chia cho mẫu số
                    bogus_num = random.randint(5, 20)
                    bogus_den = random.randint(5, 12)
                    bogus = simplify(sqrt(bogus_num) / bogus_den)
                    if bogus != sinA_val and bogus not in unique_s:
                        unique_s.append(bogus)

                s = [
                    '$%s$' % (latex(unique_s[0])),
                    '$%s$' % (latex(unique_s[1])),
                    '$%s$' % (latex(unique_s[2]))
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('Tam giác có ba cạnh lần lượt là $%s, %s, %s$. Góc bé nhất của tam giác có $\\sin$ bằng bao nhiêu?'
                                 % (a, b, c))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('Giả sử tam giác $ABC$ có ba cạnh $a=%s, b=%s, c=%s$. \\\\ '
                           'Trong một tam giác, góc đối diện với cạnh nhỏ nhất là góc nhỏ nhất. Vì $a < b < c$ nên góc bé nhất là góc $A$. \\\\ '
                           'Áp dụng hệ quả của định lí côsin, ta có: \\\\ '
                           '$\\cos A = \\frac{b^2 + c^2 - a^2}{2bc} = \\frac{%s^2 + %s^2 - %s^2}{2 \\cdot %s \\cdot %s} = \\frac{%s + %s - %s}{%s} = %s$. \\\\ '
                           'Mặt khác, vì $0^\\circ < A < 180^\\circ$ nên $\\sin A > 0$. Ta có: \\\\ '
                           '$\\sin^2 A + \\cos^2 A = 1 \\Rightarrow \\sin A = \\sqrt{1 - \\cos^2 A} = \\sqrt{1 - \\left(%s\\right)^2} = %s$.'
                           % (a, b, c, 
                              b, c, a, b, c, b**2, c**2, a**2, 2*b*c, latex(cosA_val), 
                              latex(cosA_val), kq))

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

