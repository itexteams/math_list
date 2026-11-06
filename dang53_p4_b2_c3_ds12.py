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


def bt_dang53_p4_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            lis_K = [9, 18, 27, 36, 45, 54, 12, 15, 21]
            K_val = random.choice(lis_K)

            # Tính toán các hệ số dựa trên logic giải bài
            # a = 4K/9
            a = Rational(4 * K_val, 9)
            b = -3 * a
            c = 2 * a

            def f(val):
                return a*val**3 + b*val**2 + c*val

            ans_val = f(4)

            # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            da_d = '$%s$' % latex(ans_val)
            s = set()
            while len(s) < 3:
                # Tạo các phương án sai quanh đáp án đúng
                sai = ans_val + random.choice([-20, -10, 5, 10, 15, 20, 30, -5, 40])
                if sai != ans_val and sai > 0:
                    s.add('$%s$' % latex(sai))

            list_sai = list(s)
            da_s1, da_s2, da_s3 = list_sai[0], list_sai[1], list_sai[2]

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $f(x) = ax^3 + bx^2 + cx$ thỏa mãn $f(1-x) + f(1+x) = 0$ với mọi $x$ và $\int_{0}^{3} f(x) \text{d}x = %s$. Tính $f(4)$.'''
                             % (latex(K_val)))

            # Các đáp án
            da_d_marked = '\\True ' + str(da_d)
            list_1 = [da_d_marked, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải (B2: Viết lại y hệt logic trong hình)
            loigiai = (r'''Có $f(1-x) + f(1+x) = 0$. \\
                         Khi đó: \\
                         $x = 0 \Rightarrow 2f(1) = 0 \Leftrightarrow a + b + c = 0 \quad (1)$ \\
                         $x = 1 \Rightarrow f(0) + f(2) = 0 \Leftrightarrow 8a + 4b + 2c = 0 \quad (2)$ \\
                         Gọi $F(x)$ là nguyên hàm của $f(x) \Rightarrow F(x) = \frac{ax^4}{4} + \frac{bx^3}{3} + \frac{cx^2}{2} + C$. \\
                         $\int_{0}^{3} f(x) \text{d} x = %s \Leftrightarrow F(3) - F(0) = %s \Leftrightarrow \frac{81}{4}a + 9b + \frac{9}{2}c = %s \quad (3)$ \\
                         Từ (1), (2), (3) suy ra $a = %s, b = %s, c = %s$. \\
                         Vậy $f(4) = %s$.'''
                       % (latex(K_val), latex(K_val), latex(K_val), 
                          latex(a), latex(b), latex(c), latex(ans_val)))

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

