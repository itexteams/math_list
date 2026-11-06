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


def bt_dang11_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khởi tạo biến ký hiệu
            x = symbols('x')

            # BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM BÀI TOÁN
            # Để bài toán có ý nghĩa và liên tục tại x=1:
            # Hàm có dạng: f(x) = (sqrt(ax + b) - cx) / (x - 1)
            # Điều kiện 1: ax + b > 0 tại x=1 => a + b > 0
            # Điều kiện 2: Để có dạng 0/0 tại x=1, ta cần sqrt(a + b) - c = 0 => c = sqrt(a + b)
            # Để bài toán "đẹp", ta chọn a + b là một số chính phương (k^2).

            def generate_problem():
                # Chọn k sao cho sqrt(a+b) = k. Chọn k từ 2 đến 5 để số không quá lớn.
                k = random.randint(2, 5)
                # Chọn a ngẫu nhiên
                a = random.randint(1, 10)
                # Tính b và c
                b = k**2 - a
                c = k

                # Biểu thức f(x) khi x khác 1
                f_expr = (sqrt(a*x + b) - c*x) / (x - 1)

                # Tính f(1) để hàm số liên tục (L'Hopital hoặc định nghĩa giới hạn)
                # f(1) = lim_{x->1} f(x) = a/(2*sqrt(a+b)) - c
                f1_val = Rational(a, 2*k) - c

                # Tính đạo hàm f'(1) bằng định nghĩa
                # f'(1) = lim_{x->1} [f(x) - f(1)] / (x - 1)
                f_prime_1 = limit((f_expr - f1_val) / (x - 1), x, 1)

                return a, b, c, f1_val, f_prime_1

            a, b, c, f1_val, kq_limit = generate_problem()

            # --- TẠO CÁC ĐÁP ÁN TRẮC NGHIỆM ---
            kq_dung = '$%s$' % latex(kq_limit)

            # Tạo các đáp án nhiễu (sai)
            s = [
                '$%s$' % latex(kq_limit + Rational(1, 2)),
                '$%s$' % latex(kq_limit - Rational(1, 4)),
                '$%s$' % latex(kq_limit * Rational(1, 2)),
                '$0$',
                '\\text{Không tồn tại}'
            ]
            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # --- NỘI DUNG CÂU HỎI ---
            # f(x) = \begin{cases} \frac{\sqrt{ax+b}-cx}{x-1} & \text{khi } x \neq 1 \\ f1 & \text{khi } x = 1 \end{cases}
            noidungcauhoi = r'''Cho hàm số $f(x) = \begin{cases} \dfrac{\sqrt{%sx + %s} - %sx}{x - 1} & \text{khi } x \neq 1 \\ %s & \text{khi } x = 1 \end{cases}$. Tính $f'(1)$.''' % (
                latex(a), latex(b), latex(c), latex(f1_val)
            )

            # --- NỘI DUNG LỜI GIẢI ---
            # Bước 1: Tính giới hạn để kiểm tra liên tục
            lim_f = limit((sqrt(a*x + b) - c*x) / (x - 1), x, 1)

            # Bước 2: Tính f'(1)
            # Biểu thức tử số: [sqrt(ax+b) - cx] - f1(x-1)
            tu_so = (sqrt(a*x + b) - c*x) - f1_val*(x - 1)
            mau_so = (x - 1)**2

            loigiai = r''' Ta có $\lim_{x \to 1} f(x) = \lim_{x \to 1} \frac{\sqrt{%sx + %s} - %sx}{x - 1} = %s = f(1)$. 
            Suy ra hàm số liên tục tại $x=1$. \\
            Theo định nghĩa đạo hàm:
            $f'(1) = \lim_{x \to 1} \frac{f(x) - f(1)}{x - 1} = \lim_{x \to 1} \frac{\frac{\sqrt{%sx + %s} - %sx}{x - 1} - \left(%s\right)}{x - 1}$ \\
            $= \lim_{x \to 1} \frac{\sqrt{%sx + %s} - %sx - (%s)(x-1)}{(x-1)^2}$. \\
            Tính giới hạn này bằng cách nhân liên hợp hoặc khai triển Taylor, ta được kết quả:
            $f'(1) = %s$.''' % (latex(a), latex(b), latex(c), latex(lim_f), 
                   latex(a), latex(b), latex(c), latex(f1_val),
                   latex(a), latex(b), latex(c), latex(f1_val),
                   latex(kq_limit))

            # Xử lý hiển thị dấu -- thành +
            loigiai = loigiai.replace('--', '+').replace('+-', '-')

            # --- XUẤT CÂU TRẮC NGHIỆM ---
            da_d = '\\True ' + kq_dung
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('1x','x')
            return content

