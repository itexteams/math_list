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


def bt_dang11_p4_b2_c4_ds11(self):
            # Khai báo biến
            # Khởi tạo biến
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Chọn ngẫu nhiên hướng tiến tới của x
            huong_limit = random.choice([r'+\infty', r'-\infty'])

            # Tạo biểu thức bằng phương pháp nhân ngược để số luôn đẹp
            A = random.randint(2, 6)      # Hệ số a
            B = random.randint(-15, -5)   # Hệ số b
            D = random.randint(1, 6)      # Số thực trong mẫu (x + D)
            C = random.randint(2, 25)     # Phần dư

            # Tính toán các hệ số tử số: (Ax + B)(x + D) + C = Ax^2 + (AD + B)x + (BD + C)
            m1 = A
            m2 = A * D + B
            m3 = B * D + C

            # Kết quả đúng
            a_val = A
            b_val = B
            tong = a_val + b_val

            # Tạo các đáp án nhiễu
            s = list(set([tong + 11, tong - 11, tong + 3, tong - 7, abs(tong), -abs(tong), A - B]))
            if tong in s: s.remove(tong)
            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # --- Nội dung câu hỏi ---
            # Sử dụng f-string và r-string để quản lý ký tự đặc biệt
            noidungcauhoi = r'''Cho hai số thực $a$ và $b$ thỏa mãn $\lim_{x \to %s} \left( \frac{%s}{x + %s} - ax - b \right) = 0$. Tính $a+b$.''' % (
                huong_limit, latex(m1*x**2 + m2*x + m3), latex(D)
            )

            # --- Nội dung lời giải ---
            loigiai = r'''Ta có: $\frac{%s}{x + %s} = %s %s + \frac{%s}{x + %s}$. \\
            Khi đó, giới hạn trở thành: 
            $$\lim_{x \to %s} \left( %s %s + \frac{%s}{x + %s} - ax - b \right) = 0$$
            $$\Leftrightarrow \lim_{x \to %s} \left( (%s - a)x + (%s - b) + \frac{%s}{x + %s} \right) = 0$$
            Vì $\lim_{x \to %s} \frac{%s}{x + %s} = 0$, nên để giới hạn trên bằng $0$ với mọi $x$ tiến ra vô cực, ta phải có: 
            $\begin{cases} %s - a = 0 \\ %s - b = 0 \end{cases} \Leftrightarrow \begin{cases} a = %s \\ b = %s \end{cases}$. \\
            Vậy $a + b = %s + (%s) = %s$.''' % (
                latex(m1*x**2 + m2*x + m3), latex(D), latex(A*x), latex(B), latex(C), latex(D),
                huong_limit, latex(A*x), latex(B), latex(C), latex(D),
                huong_limit, latex(A), latex(B), latex(C), latex(D),
                huong_limit, latex(C), latex(D),
                latex(A), latex(B), latex(A), latex(B),
                latex(A), latex(B), latex(tong)
            )

            # --- Xuất câu trắc nghiệm ---
            da_d = r'\True %s' % tong
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

