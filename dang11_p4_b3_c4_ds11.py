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


def bt_dang11_p4_b3_c4_ds11(self):
            # Khai báo biến ký hiệu cho SymPy
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến sympy
                x = symbols('x')

                # 1. Random hệ số a trong cos(ax) và giá trị k = f(0)
                # Chọn a sao cho a^2/2 có thể là số nguyên hoặc hữu tỷ đẹp
                a_val = random.randint(1, 5) 
                k_val = random.randint(1, 3)

                # Biểu thức tử số và mẫu số
                tu = 1 - cos(a_val * x)
                mau = x**2
                f_expr = tu / mau

                # 2. Tính giới hạn tại x = 0
                # Công thức: lim (1-cos(ax))/x^2 = a^2 / 2
                limit_val = Rational(a_val**2, 2)

                # 3. Kiểm tra tính liên tục
                is_continuous = (limit_val == k_val)

                # 4. Thiết lập nội dung câu hỏi
                noidungcauhoi = (r'''Cho hàm số $f(x) = \begin{cases} \dfrac{%s}{x^2} & \text{khi } x \neq 0 \\ %s & \text{khi } x = 0 \end{cases}$. Xét tính liên tục của hàm số.'''
                                 %(latex(tu), latex(k_val)))

                # 5. Tạo các đáp án
                if is_continuous:
                    da_dung = r'\True Hàm số liên tục tại $x=0$'
                    s = [
                        r'Hàm số gián đoạn tại $x=0$',
                        r'Hàm số không xác định tại $x=0$',
                        r'Hàm số liên tục trên $(0; +\infty)$ nhưng gián đoạn tại $x=0$'
                    ]
                else:
                    da_dung = r'\True Hàm số gián đoạn tại $x=0$'
                    s = [
                        r'Hàm số liên tục tại $x=0$',
                        r'Hàm số không xác định tại $x=0$',
                        r'Hàm số liên tục trên $\mathbb{R}$'
                    ]

                # Trộn đáp án
                list_1 = [da_dung] + s
                random.shuffle(list_1)

                # 6. Nội dung lời giải chi tiết
                # Sử dụng công thức lượng giác 1 - cos(ax) = 2sin^2(ax/2)
                loigiai = (r'''Hàm số xác định trên $\mathbb{R}$. \\
                           Ta có $f(0) = %s$ và \\
                           $\lim_{x \to 0} f(x) = \lim_{x \to 0} \dfrac{1 - \cos %s x}{x^2} = \lim_{x \to 0} \dfrac{2 \sin^2 \frac{%s x}{2}}{x^2} = \lim_{x \to 0} \dfrac{2 \cdot \left(\frac{%s}{2}\right)^2 \sin^2 \frac{%s x}{2}}{\left(\frac{%s x}{2}\right)^2} = %s$. \\'''
                           %(latex(k_val), 
                             a_val if a_val != 1 else "", 
                             a_val if a_val != 1 else "",
                             a_val,
                             a_val if a_val != 1 else "",
                             a_val if a_val != 1 else "",
                             latex(limit_val)))

                if is_continuous:
                    loigiai += r'Vì $f(0) = \lim_{x \to 0} f(x)$ nên hàm số liên tục tại $x=0$.'
                else:
                    loigiai += r'Vì $f(0) \neq \lim_{x \to 0} f(x)$ nên hàm số gián đoạn tại $x=0$.'

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

