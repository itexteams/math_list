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


def bt_dang26_p1_b2_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random điểm A(x0, y0, z0)
                x0 = randint(-5, 5)
                while x0 == 0: x0 = randint(-5, 5)

                y0 = randint(-5, 5)
                while y0 == 0 or y0 == x0: y0 = randint(-5, 5)

                z0 = randint(-5, 5)
                while z0 == 0 or z0 in (x0, y0): z0 = randint(-5, 5)

                # Random vectơ chỉ phương u(u1, u2, u3)
                u1 = randint(-5, 5)
                while u1 == 0: u1 = randint(-5, 5)

                u2 = randint(-5, 5)
                while u2 == 0 or u2 == u1: u2 = randint(-5, 5)

                u3 = randint(-5, 5)
                while u3 == 0 or u3 in (u1, u2): u3 = randint(-5, 5)

                # Hàm trợ giúp định dạng tử số của phương trình chính tắc
                def fmt_num(var, val):
                    if val > 0:
                        return '%s - %s' % (var, latex(val))
                    else:
                        return '%s + %s' % (var, latex(-val))

                # Phương án đúng
                eq_correct = '\\frac{%s}{%s} = \\frac{%s}{%s} = \\frac{%s}{%s}' % (
                    fmt_num('x', x0), latex(u1),
                    fmt_num('y', y0), latex(u2),
                    fmt_num('z', z0), latex(u3)
                )
                du = ['$%s$' % eq_correct]
                da = random.choice(du)

                # Các phương án sai
                eq_w1 = '\\frac{%s}{%s} = \\frac{%s}{%s} = \\frac{%s}{%s}' % (
                    fmt_num('x', x0), latex(u1),
                    fmt_num('y', -y0), latex(u2),
                    fmt_num('z', -z0), latex(u3)
                )
                eq_w2 = '\\frac{%s}{%s} = \\frac{%s}{%s} = \\frac{%s}{%s}' % (
                    fmt_num('x', x0), latex(u1),
                    fmt_num('y', -y0), latex(u2),
                    fmt_num('z', z0), latex(u3)
                )
                eq_w3 = '\\frac{%s}{%s} = \\frac{%s}{%s} = \\frac{%s}{%s}' % (
                    fmt_num('x', x0), latex(u1),
                    fmt_num('y', y0), latex(u2),
                    fmt_num('z', -z0), latex(u3)
                )

                s = [
                    '$%s$' % eq_w1,
                    '$%s$' % eq_w2,
                    '$%s$' % eq_w3
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Trong không gian với hệ tọa độ $Oxyz$, phương trình của đường thẳng đi qua điểm $A(%s; %s; %s)$ và có một vectơ chỉ phương $\\vec{u} = (%s; %s; %s)$ là'''
                                 % (latex(x0), latex(y0), latex(z0), latex(u1), latex(u2), latex(u3)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Phương trình chính tắc của đường thẳng đi qua điểm $A(x_0; y_0; z_0)$ và có vectơ chỉ phương $\\vec{u} = (a; b; c)$ ($a, b, c \\neq 0$) là:\\\\
            $\\frac{x - x_0}{a} = \\frac{y - y_0}{b} = \\frac{z - z_0}{c}$.\\\\
            Thay tọa độ điểm $A(%s; %s; %s)$ và vectơ chỉ phương $\\vec{u} = (%s; %s; %s)$ vào công thức trên, ta được phương trình đường thẳng là:\\\\
            $%s$.'''
                           % (latex(x0), latex(y0), latex(z0),
                              latex(u1), latex(u2), latex(u3),
                              eq_correct))

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

