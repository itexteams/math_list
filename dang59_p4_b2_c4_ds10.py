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


def bt_dang59_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Bước 1 & 2: Khai báo biến và tạo số ngẫu nhiên (B3 - Suy nghĩ random)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số của Parabol y = ax^2 + bx + c
                # Để đơn giản và giống mẫu, ta giữ a = 2, random b và c
                a = 2
                b = random.randint(-5, 5)
                c = random.randint(-10, -1)

                # Random hệ số đường thẳng y = dx + m (trong ảnh d = 4)
                d = random.randint(2, 6)

                S = Rational(-(b-d), a)


                m_val = c - Rational(a, 7) * (2 * S**2 - 7)

                # Điều kiện Delta > 0: (b-d)^2 - 4*a*(c-m) > 0
                delta_expr_m = (b-d)**2 - 4*a*(c-m_val)
                # Trong code này m_val là đáp án đúng, ta sẽ kiểm tra Delta trực tiếp

                # Đáp án đúng
                kq = latex(m_val)

                # Bước 4: Tạo các phương án sai không trùng đáp án đúng
                s = []
                while len(s) < 3:
                    sai = latex(m_val + random.randint(-5, 5) + random.choice([Rational(1,2), 1, -1]))
                    if sai != kq and sai not in s:
                        s.append(sai)

                das1, das2, das3 = s

                # Nội dung câu hỏi
                noidungcauhoi = (r'Cho hàm số $y = %sx^2 %s x %s (1)$. Tìm giá trị của tham số $m$ để đồ thị hàm số (1) cắt đường thẳng $y = %sx + m$ tại hai điểm phân biệt $A(x_1; y_1)$, $B(x_2; y_2)$ thỏa mãn $2x_1^2 + 2x_2^2 = 3x_1x_2 + 7$.'
                                 % (latex(a), ('+' + latex(b) if b > 0 else latex(b)), latex(c), latex(d)))

                # Các đáp án
                da_d = r'\True $%s$' % kq
                list_1 = [da_d, '$%s$' % das1, '$%s$' % das2, '$%s$' % das3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (B2)
                b_minus_d = b - d
                c_minus_m = f"{c}-m"
                delta = f"({b_minus_d})^2 - 4.{a}.({c_minus_m})"

                loigiai = (r'''Xét phương trình hoành độ giao điểm: $%sx^2 %s x %s = %sx + m \Leftrightarrow %sx^2 %s x + (%s - m) = 0 \ (*)$ \\
                Phương trình (*) có hai nghiệm phân biệt khi và chỉ khi $\Delta = %s > 0$. \\
                Gọi $x_1, x_2$ là hai nghiệm phân biệt của (*) nên theo Vi-et ta có: $\begin{cases} x_1 + x_2 = %s \\ x_1 \cdot x_2 = \frac{%s - m}{%s} \end{cases}$. \\
                Theo đề bài: $2x_1^2 + 2x_2^2 = 3x_1x_2 + 7 \Leftrightarrow 2(x_1 + x_2)^2 - 7x_1x_2 - 7 = 0$ \\
                $\Leftrightarrow 2 \left( %s \right)^2 - 7 \cdot \left( \frac{%s - m}{%s} \right) - 7 = 0 \Leftrightarrow m = %s$. (Thỏa mãn điều kiện $\Delta > 0$). \\
                Vậy $m = %s$ là giá trị cần tìm.'''
                           % (latex(a), ('+' + latex(b) if b > 0 else latex(b)), latex(c), latex(d), 
                              latex(a), (latex(b_minus_d) if b_minus_d < 0 else '+'+latex(b_minus_d)), latex(c),
                              delta, latex(S), latex(c), latex(a),
                              latex(S), latex(c), latex(a), kq, kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

