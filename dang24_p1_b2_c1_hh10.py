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


def bt_dang24_p1_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3 - Logic Random bài toán: 
                # Khởi tạo danh sách các bộ 3 số Pytago để đảm bảo tam giác luôn vuông và nghiệm đẹp
                pythagorean_triples = [
                    (3, 4, 5), (6, 8, 10), (9, 12, 15), (12, 16, 20),
                    (5, 12, 13), (10, 24, 26), 
                    (8, 15, 17)
                ]

                # Chọn ngẫu nhiên một bộ 3 số
                a, b, c = random.choice(pythagorean_triples)

                # Hoán vị ngẫu nhiên 2 cạnh góc vuông AB và AC
                if random.choice([True, False]):
                    AB, AC, BC = a, b, c
                else:
                    AB, AC, BC = b, a, c

                # Tính bán kính đường tròn nội tiếp r (Theo đúng công thức r = S/p)
                # Vì 1/2 ở tử và mẫu triệt tiêu nên ta có r = (AB*AC) / (AB+AC+BC)
                r_val = Rational(AB * AC, AB + AC + BC)

                # Câu hỏi
                noidungcauhoi = ('''Cho tam giác $ABC$ có $AB=%s$, $AC=%s$, $BC=%s$. Bán kính đường tròn nội tiếp tam giác bằng'''
                                 %(AB, AC, BC))

                # Các đáp án trắc nghiệm
                da = r_val

                # Tạo các đáp án gây nhiễu (Dùng Rational để ra phân số giống mẫu đề bài)
                s = [
                    Rational(AB + AC, BC), 
                    Rational(BC, AB + AC), 
                    Rational(AB * AC, BC), 
                    Rational(AB + AC + BC, AB * AC),
                    Rational(AB * AC * 2, AB + AC + BC)
                ]
                # Lọc bỏ đáp án trùng với đáp án đúng và đảm bảo dương
                s = list(set([val for val in s if val != r_val and val > 0]))

                # Dự phòng nếu thuật toán lọc trùng làm thiếu đáp án nhiễu
                if len(s) < 3: 
                    s.extend([r_val + 1, Rational(2, 3), Rational(3, 4), Rational(4, 5)])
                    s = list(set([val for val in s if val != r_val]))

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Định dạng LaTeX cho các đáp án
                da_d = ('\\True $%s$' % latex(da))
                da_s1 = ('$%s$' % latex(das1))
                da_s2 = ('$%s$' % latex(das2))
                da_s3 = ('$%s$' % latex(das3))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Vì $AB^2 + AC^2 = BC^2$ nên tam giác $ABC$ vuông tại $A$.\\\\
            Do đó bán kính đường tròn nội tiếp $r = \\frac{S}{p} = \\frac{\\frac{1}{2}AB.AC}{\\frac{1}{2}(AB+AC+BC)} = \\frac{%s.%s}{%s+%s+%s} = %s$.'''
                           %(AB, AC, AB, AC, BC, latex(r_val)))

            # Xử lý chuỗi hiển thị tránh lỗi dấu + - hoặc - - theo lưu ý
            noidungcauhoi = noidungcauhoi.replace('+ -', '-').replace('- -', '+')
            loigiai = loigiai.replace('+ -', '-').replace('- -', '+')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

