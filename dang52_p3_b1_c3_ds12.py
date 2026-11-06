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


def bt_dang52_p3_b1_c3_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':


        k = randint(1, 10)  # Hệ số nhân ở tử số: f(x) = k / (1 + sin x)
        a_val = -k
        b_val = 2
        c_val = 4
        t_val = a_val + b_val + c_val

        # Xử lý hiển thị tử số
        if k == 1:
            tu_so = "1"
        else:
            tu_so = "%d" % k

        # Nội dung câu hỏi
        noidungcauhoi = ('''Gọi $F(x)$ là một nguyên hàm của hàm số $f(x) = \\frac{%s}{1 + \\sin x}$. Biết $F(x) = a \\cdot \\cot\\left(\\frac{x}{b} + \\frac{\\pi}{c}\\right) + C$. Khi đó hãy tính giá trị biểu thức $T = a + b + c$?'''
                         % (tu_so))

        # Nội dung lời giải
        loigiai = ('''Ta có: \\\\
                   $1 + \\sin x = 1 + \\cos\\left(\\frac{\\pi}{2} - x\\right) = 2\\cos^2\\left(\\frac{\\pi}{4} - \\frac{x}{2}\\right) = 2\\sin^2\\left(\\frac{x}{2} + \\frac{\\pi}{4}\\right)$. \\\\
                   Do đó: \\\\
                   $F(x) = \\int \\frac{%s}{1 + \\sin x} \\,\\mathrm{d}x = \\int \\frac{%s}{2\\sin^2\\left(\\frac{x}{2} + \\frac{\\pi}{4}\\right)} \\,\\mathrm{d}x$. \\\\
                   Đặt $u = \\frac{x}{2} + \\frac{\\pi}{4} \\Rightarrow \\mathrm{d}u = \\frac{1}{2} \\,\\mathrm{d}x \\Rightarrow \\mathrm{d}x = 2\\,\\mathrm{d}u$. \\\\
                   Khi đó: \\\\
                   $F(x) = \\int \\frac{%s}{\\sin^2 u} \\,\\mathrm{d}u = %s\\cot u + C = %s\\cot\\left(\\frac{x}{2} + \\frac{\\pi}{4}\\right) + C$. \\\\
                   Suy ra: $a = %d$, $b = %d$, $c = %d$. \\\\
                   Vậy giá trị của biểu thức $T = a + b + c = (%d) + %d + %d = %d$.'''
                   % (tu_so,
                      tu_so,
                      tu_so,
                      str(a_val),
                      str(a_val),
                      a_val, b_val, c_val,
                      a_val, b_val, c_val, t_val))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(t_val))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n' +
               '\\end{minipage}\n\n')
    return content


