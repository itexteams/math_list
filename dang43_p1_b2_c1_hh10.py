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


def bt_dang43_p1_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tạo các số ngẫu nhiên thỏa mãn bất đẳng thức tam giác
                while True:
                    c = random.randint(4, 8)   # AB
                    b = random.randint(6, 12)  # CA
                    a = random.randint(8, 15)  # BC
                    if a + b > c and a + c > b and b + c > a:
                        m = random.randint(3, a - 2) # BM
                        # Kiểm tra xem độ dài AM có hợp lệ và không quá phức tạp không
                        cosB = Rational(c**2 + a**2 - b**2, 2*c*a)
                        AM_sq = c**2 + m**2 - 2*c*m*cosB
                        if AM_sq > 0:
                            break

                AM = sqrt(AM_sq)
                kq = latex(AM)

                # Tạo các phương án sai
                s = []

                # Sai lầm 1: Nhầm dấu trong định lí cosin
                fake1_sq = c**2 + m**2 + 2*c*m*cosB
                fake1 = sqrt(fake1_sq)
                s.append('$%s$' % (latex(fake1)))

                # Sai lầm 2: Không lấy căn bậc 2
                fake2 = AM_sq
                s.append('$%s$' % (latex(fake2)))

                # Sai lầm 3: Sai độ dài BM hoặc CM
                CM = a - m
                AM_sq_fake3 = b**2 + CM**2 - 2*b*CM*Rational(a**2 + b**2 - c**2, 2*a*b)
                if AM_sq_fake3 > 0:
                    fake3 = sqrt(AM_sq_fake3) + random.choice([1, 2]) # Thêm nhiễu để tránh trùng
                    s.append('$%s$' % (latex(fake3)))
                else:
                    s.append('$%s$' % (latex(AM + 1)))

                # Sai lầm 4: Nhiễu ngẫu nhiên
                s.append('$%s$' % (latex(AM + 2)))
                s.append('$%s$' % (latex(sqrt(AM_sq + 5))))
                s.append('$%s$' % (latex(sqrt(AM_sq + 10))))

                # Lọc trùng với đáp án đúng
                unique_s = []
                for option in s:
                    if option != '$%s$' % kq and option not in unique_s:
                        unique_s.append(option)

                # Lấy 3 phương án sai ngẫu nhiên
                random.shuffle(unique_s)
                das1 = unique_s[0]
                das2 = unique_s[1]
                das3 = unique_s[2]

                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Câu hỏi
                noidungcauhoi = ('Tam giác $ABC$ có $BC = %s$, $CA = %s$, $AB = %s$. Trên cạnh $BC$ lấy điểm $M$ sao cho $BM = %s$. Độ dài đoạn thẳng $AM$ bằng'
                                 % (a, b, c, m))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Áp dụng hệ quả của định lí côsin trong tam giác $ABC$, ta có:\\\\ \n'
                           '$\\cos B = \\frac{AB^2 + BC^2 - CA^2}{2 \\cdot AB \\cdot BC} = \\frac{%s^2 + %s^2 - %s^2}{2 \\cdot %s \\cdot %s} = %s$.\\\\ \n'
                           'Áp dụng định lí côsin trong tam giác $ABM$, ta có:\\\\ \n'
                           '$AM^2 = AB^2 + BM^2 - 2 \\cdot AB \\cdot BM \\cdot \\cos B$\\\\ \n'
                           '$\\Rightarrow AM^2 = %s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\left(%s\\right) = %s$.\\\\ \n'
                           'Vậy $AM = %s$.'
                           % (c, a, b, c, a, latex(cosB),
                              c, m, c, m, latex(cosB), latex(AM_sq),
                              kq))


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

