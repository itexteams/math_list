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


def bt_dang40_p4_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu 'a' và biến tích phân 'x'
            a = symbols('a')
            x = symbols('x')

            k = randint(1, 5) * 2 # Chọn hệ số k chẵn để tích phân kx ra số nguyên (k/2)
            L = -randint(1, 2)    # Cận dưới (âm)
            R = randint(1, 2)     # Cận trên (dương)


            int1_expr = k * x
            res1 = integrate(int1_expr, (x, L, 0))

            # Tích phân phần 2: từ 0 đến R của a*(x - x^2) dx
            int2_part = x - x**2
            res2_val = integrate(int2_part, (x, 0, R))
            res2 = a * res2_val

            # Kết quả cuối cùng
            final_ans = res1 + res2

            # B4: Tạo các phương án sai (đảm bảo không trùng với đáp án đúng)
            da_dung = '$%s$' % latex(simplify(final_ans))

            wrong_choices = set()
            while len(wrong_choices) < 3:
                # Tạo các biến thể sai bằng cách thay đổi dấu hoặc hệ số
                offsets = [Rational(1, 2), 1, Rational(1, 3), 2]
                wrong_val = res1 + random.choice([-1, 1]) * random.choice(offsets) + a * (res2_val + random.choice([-1, 1]) * random.choice(offsets))
                wrong_str = '$%s$' % latex(simplify(wrong_val))
                if wrong_str != da_dung:
                    wrong_choices.add(wrong_str)

            list_wrong = list(wrong_choices)

            # Nội dung câu hỏi
            noidungcauhoi = (r'Cho số thực $a$ và hàm số $f(x) = \begin{cases} %sx & \text{khi } x \le 0 \\ a(x - x^2) & \text{khi } x > 0 \end{cases}$. '
                             r'Tính $\int_{%s}^{%s} f(x) \text{d}x$.' 
                             % (latex(k) if k != 1 else "", latex(L), latex(R)))

            # Nội dung lời giải chi tiết
            loigiai = (r'Ta thấy, $\int_{%s}^{%s} f(x) \text{d}x = \int_{%s}^{0} f(x) \text{d}x + \int_{0}^{%s} f(x) \text{d}x = \int_{%s}^{0} %sx \text{d}x + \int_{0}^{%s} a(x - x^2) \text{d}x$.\\'
                       r'$= \left( %s x^2 \right) \bigg|_{%s}^{0} + a \left( \frac{x^2}{2} - \frac{x^3}{3} \right) \bigg|_{0}^{%s} = %s + a \left(%s\right) = %s$.'
                       % (latex(L), latex(R), latex(L), latex(R), latex(L), latex(k), latex(R),
                          latex(Rational(k, 2)), latex(L), latex(R), latex(res1), latex(res2_val), latex(simplify(final_ans))))

            # Sắp xếp các phương án
            da_d = '\\True ' + da_dung
            list_1 = [da_d] + list_wrong
            random.shuffle(list_1)

            # Xuất nội dung theo mẫu LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

