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


def bt_dang42_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khởi tạo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Tạo các số ngẫu nhiên sao cho logic bài toán không đổi
                # b|x| - c != 0 => x != +/- c/b
                # x + a >= 0 => x >= -a
                # Để giữ cấu trúc giống hình, ta cần -a < -c/b
                b = random.randint(2, 5)
                c = random.randint(1, 7)
                # Rút gọn phân số c/b
                phan_so = Rational(c, b)

                # Đảm bảo -a nhỏ hơn -c/b (tức là a > c/b)
                a = random.randint(int(phan_so) + 1, int(phan_so) + 4)
                n = random.randint(2, 5) # Số mũ của x trên tử

                # 2. Tính toán các giá trị hiển thị
                minus_a = -a
                val_frac = latex(phan_so)

                # 3. Kết quả đúng (Đáp án)
                # D = [-a; +inf) \ { -c/b; c/b }
                da_dung = r'D = [%s; +\infty) \setminus \left\{ -%s; %s \right\}' % (latex(minus_a), val_frac, val_frac)

                # 4. Tạo các phương án sai (Distractors)
                s = [
                    # Sai ngoặc vuông thành ngoặc tròn
                    r'D = (%s; +\infty) \setminus \left\{ -%s; %s \right\}' % (latex(minus_a), val_frac, val_frac),
                    # Thiếu giá trị âm trong tập loại trừ
                    r'D = [%s; +\infty) \setminus \left\{ %s \right\}' % (latex(minus_a), val_frac),
                    # Sai tập xác định của căn (lấy toàn bộ R)
                    r'D = \mathbb{R} \setminus \left\{ -%s; %s \right\}' % (val_frac, val_frac),
                    # Nhầm dấu của a
                    r'D = [%s; +\infty) \setminus \left\{ -%s; %s \right\}' % (latex(a), val_frac, val_frac),
                    # Nhầm dấu trong ngoặc nhọn
                    r'D = [%s; +\infty) \setminus \left\{ %s \right\}' % (latex(minus_a), latex(-phan_so))
                ]

                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # 5. Nội dung câu hỏi
                noidungcauhoi = (r'Tìm tập xác định của hàm số $y = \sqrt{x + %s} + \frac{x^%s}{%s|x| - %s}$.'
                                 % (latex(a), latex(n), latex(b), latex(c)))

                # 6. Nội dung lời giải
                loigiai = (r'''Điều kiện xác định của hàm số $\begin{cases} x + %s \geq 0 \\ %s|x| - %s \neq 0 \end{cases} \Leftrightarrow \begin{cases} x \geq %s \\ |x| \neq \frac{%s}{%s} \end{cases} \Leftrightarrow \begin{cases} x \geq %s \\ x \neq -%s \\ x \neq %s \end{cases}$. \\
                             Vậy tập xác định của hàm số là $%s$.'''
                           % (latex(a), latex(b), latex(c), latex(minus_a), latex(c), latex(b), 
                              latex(minus_a), val_frac, val_frac, da_dung))

                # 7. Sắp xếp đáp án
                da_d = '\\True $' + da_dung + '$'
                list_1 = [da_d, '$' + das1 + '$', '$' + das2 + '$', '$' + das3 + '$']
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

