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


def bt_dang47_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thực hiện ngẫu nhiên hóa bằng cách xáo trộn hệ số góc của x ở các phương án nhưng giữ nguyên tính chất logic của bài toán ban đầu
                # Thay đổi hệ số 2 trong các phương án ban đầu thành k ngẫu nhiên (chọn 2, 3 hoặc 4)
                k = random.choice([2, 3, 4])

                # Cấu trúc các cặp hàm số dựa trên hệ số k mới:
                # Cặp A: y = cos x (chu kỳ 2pi) và y = cot(x/2) (chu kỳ 2pi) -> Cùng chu kỳ
                fA1 = 'y = \\cos x'
                fA2 = 'y = \\cot \\frac{x}{2}'
                ckA = '2\\pi'

                # Cặp B (Đáp án đúng): y = sin x (chu kỳ 2pi) và y = tan(kx) (chu kỳ pi/k) -> Chu kỳ khác nhau
                fB1 = 'y = \\sin x'
                fB2 = 'y = \\tan %sx' % (latex(k))
                ckB1 = '2\\pi'
                ckB2 = '\\frac{\\pi}{%s}' % (latex(k))

                # Cặp C: y = sin(x/2) (chu kỳ 4pi) và y = cos(x/2) (chu kỳ 4pi) -> Cùng chu kỳ
                fC1 = 'y = \\sin \\frac{x}{2}'
                fC2 = 'y = \\cos \\frac{x}{2}'
                ckC = '4\\pi'

                # Cặp D: y = tan(kx) (chu kỳ pi/k) và y = cot(kx) (chu kỳ pi/k) -> Cùng chu kỳ
                fD1 = 'y = \\tan %sx' % (latex(k))
                fD2 = 'y = \\cot %sx' % (latex(k))
                ckD = '\\frac{\\pi}{%s}' % (latex(k))

                # Chuỗi hiển thị các cặp phương án
                str_A = '%s \\,\\, \\text{và}  \\,\\,  %s' % (fA1, fA2)
                str_B = '%s  \\,\\,  \\text{và}  \\,\\,  %s' % (fB1, fB2)
                str_C = '%s  \\,\\,  \\text{và}  \\,\\,  %s' % (fC1, fC2)
                str_D = '%s  \\,\\,  \\text{và}  \\,\\,  %s' % (fD1, fD2)

                # Các đáp án trắc nghiệm (Cặp B luôn có chu kỳ khác nhau)
                du = ['$%s$' % (str_B)]
                da = random.choice(du)

                s = [
                    '$%s$' % (str_A),
                    '$%s$' % (str_C),
                    '$%s$' % (str_D)
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Hai hàm số nào sau đây có chu kì khác nhau?''')

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết, đầy đủ từng bước mô phỏng theo mẫu hình ảnh
                loigiai = ('''Xét: Hai hàm số $%s$ và $%s$ có cùng chu kì là $%s$. \\\\
                           Xét: Hai hàm số $%s$ có chu kì là $%s$, hàm số $%s$ có chu kì là $%s$. \\\\
                           Xét: Hai hàm số $%s$ và $%s$ có cùng chu kì là $%s$. \\\\
                           Xét: Hai hàm số $%s$ và $%s$ có cùng chu kì là $%s$.'''
                           % (fA1, fA2, ckA, fB1, ckB1, fB2, ckB2, fC1, fC2, ckC, fD1, fD2, ckD))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

