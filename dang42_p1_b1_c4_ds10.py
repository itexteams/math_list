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


def bt_dang42_p1_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Khởi tạo các giá trị ngẫu nhiên cho bài toán
                # Hàm số có dạng: y = 1/sqrt(x-m) + sqrt(-x + am + b) trên khoảng (c; d)
                a = random.randint(2, 3) # Hệ số của m trong căn thứ 2
                c = random.randint(-3, 2) # Cận trái của khoảng
                d = c + random.randint(1, 2) # Cận phải của khoảng (đảm bảo d > c)

                # Để bài toán có nghiệm đẹp và tập nghiệm m không rỗng:
                # Ta cần m <= c và m >= (d-b)/a. Chọn b sao cho (d-b)/a < c
                # => d - b < ac => b > d - ac.
                b_min = d - a*c + 1
                b = random.randint(b_min, b_min + 5)

                # 2. Tính toán kết quả (Lời giải)
                # Điều kiện: x > m và x <= am + b => m < x <= am + b
                # Để hàm số xác định trên (c; d) thì (c; d) phải là tập con của (m; am + b]
                # => m <= c và am + b >= d

                m_upper = c
                # Giải am + b >= d => m >= (d-b)/a
                m_lower_val = Rational(d - b, a)

                # Đáp án đúng dưới dạng LaTeX
                kq_chuan = r'%s \le m \le %s' % (latex(m_lower_val), latex(m_upper))
                da = '$%s$' % kq_chuan

                # 3. Tạo các phương án sai (Distractors)
                s = set()
                while len(s) < 3:
                    # Tạo các biến thể sai: sai dấu, sai cận, hoặc sai bất đẳng thức
                    options = [
                        r'%s < m \le %s' % (latex(m_lower_val), latex(m_upper)), # Sai dấu ngoặc
                        r'%s \le m < %s' % (latex(m_lower_val), latex(m_upper)), # Sai dấu ngoặc
                        r'm \le %s' % latex(m_upper), # Thiếu cận
                        r'm \ge %s' % latex(m_lower_val), # Thiếu cận
                        r'%s \le m \le %s' % (latex(m_lower_val - 1), latex(m_upper)), # Sai giá trị số
                        r'%s \le m \le %s' % (latex(m_lower_val), latex(m_upper + 1)), # Sai giá trị số
                        r'm \in \varnothing'
                    ]
                    choice = '$' + random.choice(options) + '$'
                    if choice != da:
                        s.add(choice)

                list_s = list(s)
                das1, das2, das3 = list_s[0], list_s[1], list_s[2]

                # 4. Nội dung câu hỏi
                noidungcauhoi = (r'Tìm $m$ để hàm số $y = \frac{1}{\sqrt{x-m}} + \sqrt{-x + %sm + %s}$ xác định trên $(%s; %s)$.'
                                 % (latex(a), latex(b), latex(c), latex(d)))

                # 5. Nội dung lời giải
                loigiai = (r'''Hàm số xác định khi $\begin{cases} x - m > 0 \\ -x + %sm + %s \ge 0 \end{cases} \Leftrightarrow \begin{cases} x > m \\ x \le %sm + %s \end{cases} \Leftrightarrow m < x \le %sm + %s$. \\
                          Do để hàm số xác định trên $(%s; %s)$, ta phải có: \\
                          $\begin{cases} m \le %s \\ %sm + %s \ge %s \end{cases} \Leftrightarrow \begin{cases} m \le %s \\ %sm \ge %s \end{cases} \Leftrightarrow \begin{cases} m \le %s \\ m \ge %s \end{cases} \Leftrightarrow %s \le m \le %s$. \\
                          Vậy %s thỏa mãn yêu cầu bài toán.'''
                          % (latex(a), latex(b), latex(a), latex(b), latex(a), latex(b),
                             latex(c), latex(d),
                             latex(c), latex(a), latex(b), latex(d),
                             latex(c), latex(a), latex(d-b),
                             latex(c), latex(m_lower_val), latex(m_lower_val), latex(m_upper),
                             da))

                # Đưa các đáp án vào danh sách và xáo trộn
                da_d = '\\True ' + str(da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

