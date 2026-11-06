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


def bt_dang68_p4_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán
            # Random các giá trị để tạo biến thể đề bài
            a = random.randint(2, 5)    # Số thực dưới căn: 3
            b = random.randint(2, 4)    # Hệ số của x trong sin: 3
            c = random.randint(2, 4)    # Hệ số của x^2: 2
            d = random.randint(1, 5)    # Số thực trong căn của cos: 2

            # Biểu thức gốc: y = sqrt(a + sin^2(bx - pi/4)) + cos(sqrt(cx^2 + d))
            u_arg = b*x - pi/4
            v_arg = sqrt(c*x**2 + d)
            y = sqrt(a + sin(u_arg)**2) + cos(v_arg)

            # Tính đạo hàm chính xác bằng sympy
            y_prime = diff(y, x)

            # --- B2-Viết lại bài toán theo mẫu code python ---

            # Nội dung câu hỏi
            noidungcauhoi = r'Tính đạo hàm của hàm số $y = \sqrt{%s + \sin^2 \left( %sx - \frac{\pi}{4} \right)} + \cos \sqrt{%sx^2 + %s}$.' % (
                latex(a), latex(b), latex(c), latex(d)
            )

            # Đáp án đúng (đã sửa lỗi triệt tiêu hệ số)
            da_correct = '$' + latex(y_prime).replace('--', '+').replace('+-', '-') + '$'
            da_d = ('\\True ' + da_correct)

            # Tạo các đáp án sai (nhiễu)
            da_s1 = '$' + latex(diff(sqrt(a + sin(u_arg)**2), x) + sin(v_arg) * (c*x/v_arg)).replace('--', '+') + '$' # Sai dấu
            da_s2 = '$' + latex(y_prime / 2).replace('--', '+') + '$' # Thiếu hệ số 2
            da_s3 = '$' + latex(diff(y, x) + 1).replace('--', '+') + '$' # Sai lệch số hạng

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải (Sửa lại phần đạo hàm căn trong cos)
            loigiai = r'''Ta có: $y' = \left( \sqrt{%s + \sin^2 \left( %sx - \frac{\pi}{4} \right)} \right)' + \left( \cos \sqrt{%sx^2 + %s} \right)'$ \\
            + Xét $u = \sqrt{%s + \sin^2 \left( %sx - \frac{\pi}{4} \right)} \Rightarrow u' = \frac{\left( \sin^2 \left( %sx - \frac{\pi}{4} \right) \right)'}{2\sqrt{%s + \sin^2 \left( %sx - \frac{\pi}{4} \right)}} = \frac{%s \cdot 2\sin\left( %sx - \frac{\pi}{4} \right)\cos\left( %sx - \frac{\pi}{4} \right)}{2\sqrt{%s + \sin^2 \left( %sx - \frac{\pi}{4} \right)}} = \frac{%s \sin 2\left( %sx - \frac{\pi}{4} \right)}{2\sqrt{%s + \sin^2 \left( %sx - \frac{\pi}{4} \right)}}$. \\
            + Xét $v = \cos \sqrt{%sx^2 + %s} \Rightarrow v' = -\sin \sqrt{%sx^2 + %s} \cdot \left( \sqrt{%sx^2 + %s} \right)' = -\sin \sqrt{%sx^2 + %s} \cdot \frac{%sx}{\sqrt{%sx^2 + %s}} = -\frac{%sx \sin \sqrt{%sx^2 + %s}}{\sqrt{%sx^2 + %s}}$. \\
            Vậy $y' = %s$.''' % (
                latex(a), latex(b), latex(c), latex(d),
                latex(a), latex(b), latex(b), latex(a), latex(b), latex(b), latex(b), latex(b), latex(a), latex(b), latex(b), latex(b), latex(a), latex(b),
                latex(c), latex(d), latex(c), latex(d), latex(c), latex(d), latex(c), latex(d), latex(2*c), latex(c), latex(d), latex(c), latex(c), latex(d), latex(c), latex(d),
                latex(y_prime)
            )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

