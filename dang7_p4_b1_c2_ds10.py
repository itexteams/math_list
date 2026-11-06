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


def bt_dang7_p4_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Random các hệ số c1, c2, c3 (số dương để tránh lỗi dấu)
                c1 = randint(1, 9)
                c2 = randint(2, 6) # Mẫu số
                c3 = randint(1, 5)

                # Random dấu của bất phương trình: >=, <=, >, <
                list_dau = ['>=', '<=', '>', '<']
                dau_chon = random.choice(list_dau)

                # Chuyển đổi sang định dạng LaTeX tương ứng
                dict_dau_tex = {
                    '>=': '\\ge',
                    '<=': '\\le',
                    '>': '>',
                    '<': '<'
                }
                dau_tex = dict_dau_tex[dau_chon]

                # Tính toán kết quả (Công thức tìm a không đổi cho mọi dấu)
                a = c2 * c3 - c1

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (a)]
                da = random.choice(du)

                # Tạo danh sách đáp án sai xung quanh kết quả đúng
                s = [
                    '$%s$' % (a + 1),
                    '$%s$' % (a - 1),
                    '$%s$' % (a + 2),
                    '$%s$' % (a - 2),
                    '$%s$' % (a + 3),
                    '$%s$' % (a - 3),
                    '$%s$' % (a + c2),
                ]

                das1, das2, das3 = random.sample(s, 3)

                # Câu hỏi (Tự động thay đổi dạng m >= a, m <= a,... dựa vào dau_tex)
                noidungcauhoi = ('''Các giá trị của tham số $m$ có dạng $m %s a$ sao cho $\\begin{cases} x = 0 \\\\ y = -1 \\end{cases}$ là nghiệm của bất phương trình $mx - \\frac{m+%s}{%s}y - %s %s 0$. Tìm $a$.'''
                                 % (dau_tex, c1, c2, c3, dau_tex))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Đã xử lý hiển thị trừ của trừ thành cộng: - ... * (-1) -> + ...)
                loigiai = ('''Ta có $\\begin{cases} x = 0 \\\\ y = -1 \\end{cases}$ là nghiệm của bất phương trình $mx - \\frac{m+%s}{%s}y - %s %s 0$ khi và chỉ khi \\\\
            $m \\cdot 0 - \\frac{m+%s}{%s}(-1) - %s %s 0 \\Leftrightarrow \\frac{m+%s}{%s} - %s %s 0 \\Leftrightarrow m+%s %s %s \\Leftrightarrow m %s %s$. \\\\
            Vậy $a = %s$.'''
                           % (c1, c2, c3, dau_tex,
                              c1, c2, c3, dau_tex, c1, c2, c3, dau_tex, c1, dau_tex, c2*c3, dau_tex, a, 
                              a))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

