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


def bt_dang13_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Thiết lập bài toán (Ví dụ theo thông số bạn đã đưa ra)
            # y = (x-2)(x)(x+5)(x-7)
            f1, f2, f3, f4 = -2, 0, 5, -7
            k = 2  # Tổng hệ số tự do của mỗi cặp là -2 (x^2 - 2x)
            c1 = 0
            c2 = -35

            # Sử dụng Rational để tính toán chính xác phân số
            constant_t = Rational(1)
            m1 = Rational(c1 - constant_t) # -1
            m2 = Rational(c2 - constant_t) # -36

            # f(t) = t^2 + (m1+m2)t + m1*m2
            b_heso = m1 + m2 # -37
            c_heso = m1 * m2 # 36
            t_I = Rational(-b_heso, 2) # 37/2
            min_val = t_I**2 + b_heso*t_I + c_heso # -1225/4

            # Hàm định dạng: Sử dụng latex() của sympy để tự động chuyển phân số
            def fmt_tex(n):
                return latex(n)

            # Hàm định dạng dấu cho số hạng (ví dụ: -37 -> -37, 36 -> +36)
            def fmt_sign(n):
                s = latex(n)
                return s if s.startswith('-') else f"+{s}"

            noidungcauhoi = r"Tìm giá trị nhỏ nhất của hàm số $y = (x%s)(x%s)(x%s)(x%s)$." % (
                "-2", "", "+5", "-7"
            )

            # Đáp án dạng phân số LaTeX
            kq_true = r"\True $%s$" % fmt_tex(min_val)
            list_1 = [
                kq_true, 
                "$%s$" % fmt_tex(min_val + Rational(1, 4)), 
                "$%s$" % fmt_tex(min_val - Rational(1, 2)), 
                "$%s$" % fmt_tex(min_val + 1)
            ]
            random.shuffle(list_1)

            # Lời giải với định dạng phân số sạch sẽ
            loigiai = r'''Ta có $y = [(x-2)(x)].[(x+5)(x-7)] = (x^2 -2x)(x^2 -2x -35)$. \\
            Đặt $t = x^2 -2x + 1 = (x -1)^2 \ge 0$, ta được $y = f(t) = (t -1)(t -36) = t^2 %s t + %s, t \ge 0$. \\
            Hàm số $y = t^2 %s t + %s$ có $a=1 > 0$ nên bề lõm hướng lên. \\
            Hoành độ đỉnh $t_I = -\frac{b}{2a} = %s \in [0; +\infty)$. \\
            Do đó $\min y = \min f(t) = f\left(%s\right) = %s$.''' % (
                fmt_sign(b_heso), fmt_sign(c_heso), fmt_sign(b_heso), fmt_sign(c_heso), 
                fmt_tex(t_I), fmt_tex(t_I), fmt_tex(min_val)
            )

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('--', '+').replace('+ +', '+')
            return content

