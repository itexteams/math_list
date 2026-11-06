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


def bt_dang46_p1_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thiết lập các hệ số ngẫu nhiên
                # (P): y = x^2 + c
                # d: y = mx + k
                # Để giống hình mẫu (c=1, k=2), ta chọn h = k - c > 0
                c = randint(1, 5)
                h = randint(1, 4)
                k = c + h

                # Đáp án đúng luôn là m = 0 cho dạng bài này
                m0 = 0
                da = '$m = %s$' % (latex(m0))

                # Các đáp án nhiễu
                s = [
                    '$m = 1$',
                    '$m = 2$',
                    '$m = -1$',
                    '$m = -2$',
                    '$m = \\pm 1$',
                    '$m = \\pm 2$'
                ]

                # Đảm bảo phương án sai không trùng đáp án đúng
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Cho Parabol $(P): y = x^2 + %s$ và đường thẳng $d: y = mx + %s$ với $m$ là tham số. Gọi $m_0$ là giá trị của $m$ để diện tích hình phẳng giới hạn bởi $(P)$ và $d$ là nhỏ nhất. Giá trị của $m_0$ bằng'''
                                 %(latex(c), latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tính toán các giá trị cho lời giải (phân số và căn thức)
                # S_min = (4 * h * sqrt(h)) / 3
                delta_val = 4 * h
                area_min_val = Rational(2 * h * 2, 3) # Phần số trước căn
                # Để hiển thị đẹp: S = sqrt(m^2 + 4h) * (m^2/6 + 2h/3)

                # Nội dung lời giải (Sử dụng \text{d}x theo yêu cầu)
                loigiai = ('''Phương trình hoành độ của $(P)$ và $d$ là $x^2 - mx - %s = 0 \\quad (1)$. \\\\
                         Dễ thấy (1) luôn có 2 nghiệm phân biệt. Gọi $a, b$ ($a < b$) là các nghiệm của (1) thì diện tích hình phẳng giới hạn bởi $(P)$ và $d$ là \\\\
                         $S = \\int_{a}^{b} |x^2 - mx - %s| \\text{d}x = \\left| \\int_{a}^{b} (x^2 - mx - %s) \\text{d}x \\right| = \\left| \\left( \\frac{x^3}{3} - \\frac{mx^2}{2} - %sx \\right) \\bigg|_{a}^{b} \\right|$\\\\
                         $= \\left| \\frac{b^3 - a^3}{3} - \\frac{m(b^2 - a^2)}{2} - %s(b - a) \\right| = |b - a| \\cdot \\left| \\frac{b^2 + ab + a^2}{3} - \\frac{m(b + a)}{2} - %s \\right|$\\\\
                         $= \\sqrt{(b+a)^2 - 4ab} \\cdot \\left| \\frac{(b+a)^2 - ab}{3} - \\frac{m(b+a)}{2} - %s \\right|$\\\\
                         Mà $a+b=m, ab=-%s$ nên $S = \\sqrt{m^2 + %s} \\cdot \\left( \\frac{m^2}{6} + \\frac{%s}{3} \\right) \\geq \\frac{%s\\sqrt{%s}}{3}$.\\\\
                         Do đó $\\min S = \\frac{%s\\sqrt{%s}}{3}$ khi $m = 0$.'''
                         %(latex(h), latex(h), latex(h), latex(h), latex(h), latex(h), latex(h), latex(h), latex(4*h), latex(2*h), latex(4*h), latex(h), latex(4*h), latex(h)
                         ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

