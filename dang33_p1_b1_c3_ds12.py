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


def bt_dang33_p1_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
              # Random hệ số và số mũ của phần đa thức
              a = randint(2, 6)
              k = randint(1, 3)

              # Random dạng hàm lượng giác và dấu
              type_trig = randint(0, 3)
              if type_trig == 0:
                trig_term = -cos(x)
              elif type_trig == 1:
                trig_term = cos(x)
              elif type_trig == 2:
                trig_term = -sin(x)
              else:
                trig_term = sin(x)

              # Hàm số f(x)
              fx = a * x**k + trig_term

              # Nguyên hàm đúng F(x)
              Fx = integrate(fx, x)

              # Đáp án đúng
              du = ['$%s + C$' % (latex(Fx))]
              da = random.choice(du)

              # Các phương án sai (nhiễu)
              # Nhiễu 1: Đạo hàm f'(x) thay vì lấy nguyên hàm
              s1 = '$%s + C$' % (latex(sp.diff(fx, x)))
              # Nhiễu 2: Đổi dấu phần lượng giác
              s2 = '$%s + C$' % (latex(integrate(a * x**k, x) - integrate(trig_term, x)))
              # Nhiễu 3: Sai công thức nguyên hàm đa thức (không chia cho k+1)
              s3 = '$%s + C$' % (latex(a * x ** (k + 1) + integrate(trig_term, x)))
              # Nhiễu 4: Đạo hàm phần đa thức nhưng lấy nguyên hàm phần lượng giác
              s4 = '$%s + C$' % (latex(sp.diff(a * x**k, x) + integrate(trig_term, x)))

              # Lọc bỏ các phương án trùng nhau hoặc trùng với đáp án đúng
              s = [s1, s2, s3, s4]
              s = [item for item in s if item != da]
              s = list(set(s))

              while len(s) < 3:
                extra = '$%s + C$' % (latex(Fx + randint(1, 3) * x))
                if extra != da and extra not in s:
                  s.append(extra)

              das1 = random.choice(s)
              s.remove(das1)
              das2 = random.choice(s)
              s.remove(das2)
              das3 = random.choice(s)

              # Câu hỏi
              noidungcauhoi = 'Nguyên hàm của hàm số $f(x) = %s$ là' % (latex(fx))

              # Các đáp án
              da_d = '\\True ' + str(da)
              da_s1 = str(das1)
              da_s2 = str(das2)
              da_s3 = str(das3)

              # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
              list_1 = [da_d, da_s1, da_s2, da_s3]
              random.shuffle(list_1)

              # Nội dung lời giải
              loigiai = (
                  'Ta có $\\int f(x) \\mathrm{d}x = \\int \\left(%s\\right) \\mathrm{d}x ='
                  ' %s + C$.'
                  % (latex(fx), latex(Fx))
              )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

