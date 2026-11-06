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


def bt_dang30_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tham số của bài toán
                a = random.choice([0.01, 0.02, 0.04, 0.05])
                b = random.choice([10, 15, 20, 25, 30])
                kq = random.choice([500, 800, 1000, 1200, 1500, 2000])

                # Tính giá bán p sao cho x = kq là nghiệm của P'(x) = 0
                # P'(x) = -2ax + p - b = 0 => p = 2ax + b
                p = int(round(2 * a * kq + b))
                c = random.choice([500, 1000, 1200, 1500, 2000])

                a_str = str(a).replace('.', ',')
                a2 = round(2 * a, 2)
                a2_str = str(a2).replace('.', ',')
                pmb = p - b

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),
                      ]
                da = random.choice(du)

                # Tạo các phương án sai (đảm bảo không trùng với đáp án đúng)
                s = ['$%s$'%(latex(kq + 100)),
                     '$%s$'%(latex(kq - 100)),
                     '$%s$'%(latex(kq + 200)),
                     '$%s$'%(latex(kq - 200)),
                     '$%s$'%(latex(kq + 50)),
                     '$%s$'%(latex(kq - 50)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một xưởng sản xuất nón bảo hiểm có hàm chi phí sản xuất cho $x$ chiếc nón là $C(x) = %sx^2 + %sx + %s$ (nghìn đồng). Giá bán mỗi chiếc nón là $%s$ nghìn đồng. Số lượng nón cần sản xuất để xưởng đạt lợi nhuận tối đa bằng bao nhiêu?'''
                                 %(a_str, b, c, p))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $x$ ($x > 0$, $x \\in \\mathbb{N}$) là số lượng nón bảo hiểm cần sản xuất.\\\\
                             Doanh thu khi bán $x$ chiếc nón là $R(x) = %sx$ (nghìn đồng).\\\\
                             Hàm lợi nhuận của xưởng là:\\\\
                             $P(x) = R(x) - C(x) = %sx - (%sx^2 + %sx + %s) = -%sx^2 + %sx - %s$.\\\\
                             Xét hàm số $P(x) = -%sx^2 + %sx - %s$ với $x > 0$.\\\\
                             Đạo hàm: $P'(x) = -%sx + %s$.\\\\
                             $P'(x) = 0 \\Leftrightarrow -%sx + %s = 0 \\Leftrightarrow x = \\frac{%s}{%s} = %s$.\\\\
                             Ta có $P'(x) > 0$ khi $0 < x < %s$ và $P'(x) < 0$ khi $x > %s$.\\\\
                             Do đó, hàm số $P(x)$ đạt giá trị lớn nhất tại $x = %s$.\\\\
                             Vậy cần sản xuất $%s$ chiếc nón để lợi nhuận tối đa.'''
                             %(p, 
                               p, a_str, b, c, a_str, pmb, c,
                               a_str, pmb, c,
                               a2_str, pmb,
                               a2_str, pmb, pmb, a2_str, kq,
                               kq, kq,
                               kq,
                               kq))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content  

