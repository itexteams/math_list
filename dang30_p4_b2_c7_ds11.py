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


def bt_dang30_p4_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán:
            # Ta sẽ random k (hệ số của x) và b (hệ số tự do)
            # Để biểu thức đẹp, ta chọn k dương và nhỏ, b có thể âm hoặc dương.
            k = random.randint(2, 5)
            b = random.randint(-10, 10)

            # Hàm số: y = sqrt((kx + b)**3)
            u_base = k*x + b
            f = sqrt(u_base**3)

            # Tính đạo hàm chi tiết theo từng bước
            # Bước 1: Đạo hàm u = (kx + b)^3
            u = u_base**3
            du = sp.diff(u, x) # Kết quả sẽ là 3*k*(kx + b)^2

            # Bước 2: Đạo hàm y' = u' / (2*sqrt(u))
            f_prime = du / (2 * sqrt(u))
            f_prime_simplified = simplify(f_prime)

            # Kết quả đúng
            kq_dung = '$%s$' % latex(f_prime_simplified)

            # Các phương án nhiễu
            # S1: Quên không nhân k (sai công thức hàm hợp)
            s1_val = (3 * (u_base)**2) / (2 * sqrt(u_base**3))
            s1 = '$%s$' % latex(simplify(s1_val))

            # S2: Nhầm mẫu số không có số 2
            s2 = '$%s$' % latex(simplify(du / sqrt(u)))

            # S3: Sai số mũ (ra bình phương thay vì căn bậc 2)
            s3 = '$%s$' % latex(simplify(Rational(3*k, 2) * (u_base)**2))

            # S4: Đảo ngược hệ số
            s4 = '$%s$' % latex(simplify(Rational(2, 3*k) * sqrt(u_base)))

            # Xử lý danh sách đáp án
            da_d = '\\True ' + kq_dung
            list_1 = [da_d, s1, s2, s3, s4]
            final_choices = random.sample([s1, s2, s3, s4], 3) + [da_d]
            random.shuffle(final_choices)

            # B2-Viết lại bài toán
            # Sử dụng latex() để Sympy tự động xử lý dấu (ví dụ: x + (-2) thành x - 2)
            bieu_thuc_goc = latex(u_base)
            noidungcauhoi = r'Tính đạo hàm của hàm số $y = \sqrt{(%s)^3}$.' % bieu_thuc_goc

            # Nội dung lời giải chi tiết
            loigiai = r'''Ta có $y = \sqrt{(%s)^3}$. \\
            Đặt $u = (%s)^3 \Rightarrow u' = 3 \cdot (%s)' \cdot (%s)^2 = 3 \cdot %s \cdot (%s)^2$. \\
            Áp dụng công thức $(\sqrt{u})' = \frac{u'}{2\sqrt{u}}$, ta có: \\
            $y' = \frac{3 \cdot %s \cdot (%s)^2}{2\sqrt{(%s)^3}} = \frac{%s \cdot (%s)^2}{2\sqrt{(%s)^3}} = %s$.''' % (
                bieu_thuc_goc, bieu_thuc_goc, bieu_thuc_goc, bieu_thuc_goc, latex(k), bieu_thuc_goc,
                latex(k), bieu_thuc_goc, bieu_thuc_goc, latex(3*k), bieu_thuc_goc, bieu_thuc_goc, 
                latex(f_prime_simplified)
            )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

