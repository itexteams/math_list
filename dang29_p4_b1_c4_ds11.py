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


def bt_dang29_p4_b1_c4_ds11(self):
            # Khai báo biến
            # B1- Thiết lập biến
            n = symbols('n')

            # B3- Random bài toán
            k = random.choice([2, 3, 4, 5]) 
            a = k**2
            c = k**3
            b_val = random.randint(2, 25) 
            d_val = random.randint(2, 25)

            # Tính toán giá trị giới hạn
            lim1 = Rational(b_val, 2*k)
            final_res = lim1

            tu_nhanh1 = f"{b_val}n"
            tu_nhanh2 = f"-{d_val}n" 

            noidungcauhoi = r'Tính giới hạn $\lim_{n \to +\infty} n \left( \sqrt{%sn^2 + %s} - \sqrt[3]{%sn^3 + %s} \right)$.' % (latex(a), b_val, latex(c), d_val)

            # Đáp án
            da_d = r'\True $%s$' % latex(final_res)
            s = [r'$+\infty$', r'$0$', r'$%s$' % latex(final_res + 1)]
            random.shuffle(s)
            list_1 = [da_d, s[0], s[1], s[2]]
            random.shuffle(list_1)

            # LỜI GIẢI: Loại bỏ hoàn toàn n^2 ở tử thức Nhánh 2 theo yêu cầu
            loigiai = (r'''Ta có: $\lim_{n \to +\infty} n \left( \sqrt{%sn^2 + %s} - \sqrt[3]{%sn^3 + %s} \right) = \lim_{n \to +\infty} n \left[ \left( \sqrt{%sn^2 + %s} - %sn \right) + \left( %sn - \sqrt[3]{%sn^3 + %s} \right) \right]$ \\\\
            = $\lim_{n \to +\infty} \left[ n \left( \sqrt{%sn^2 + %s} - %sn \right) + n \left( %sn - \sqrt[3]{%sn^3 + %s} \right) \right]$. \\\\
            Ta có: $\lim_{n \to +\infty} n \left( \sqrt{%sn^2 + %s} - %sn \right) = \lim_{n \to +\infty} \frac{%s}{\sqrt{%sn^2 + %s} + %sn} = \lim_{n \to +\infty} \frac{%s}{\sqrt{%s + \frac{%s}{n^2}} + %s} = \frac{%s}{%s + %s} = %s$. \\\\
            Ta có: $\lim_{n \to +\infty} n \left( %sn - \sqrt[3]{%sn^3 + %s} \right) = \lim_{n \to +\infty} \frac{%s}{(%sn)^2 + %sn\sqrt[3]{%sn^3 + %s} + \sqrt[3]{(%sn^3 + %s)^2}} = 0$. \\\\
            Vậy $\lim_{n \to +\infty} n \left( \sqrt{%sn^2 + %s} - \sqrt[3]{%sn^3 + %s} \right) = %s + 0 = %s$.''' 
            % (
                # Dòng 1 & 2: 16 biến
                latex(a), b_val, latex(c), d_val, latex(a), b_val, k, k, latex(c), d_val,
                latex(a), b_val, k, k, latex(c), d_val,
                # Dòng 3 (Nhánh 1): Tử số dùng tu_nhanh1 (12 biến)
                latex(a), b_val, k, tu_nhanh1, latex(a), b_val, k, b_val, a, b_val, k, b_val, k, k, latex(lim1),
                # Dòng 4 (Nhánh 2): Tử số dùng tu_nhanh2 (Đã sửa từ n^2 thành n) (10 biến)
                k, latex(c), d_val, tu_nhanh2, k, k, latex(c), d_val, latex(c), d_val,
                # Kết luận: 6 biến
                latex(a), b_val, latex(c), d_val, latex(lim1), latex(final_res)
            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

