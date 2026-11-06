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


def bt_dang26_p1_b1_c5_ds10(self):
            # Khai báo biến
            # B3: Suy nghĩ tìm cách random bài toán
            # Random tập hợp gồm 4 chữ số khác nhau từ 1 đến 9 (không chọn số 0 để giống đề bài mẫu)
            digits_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            selected_digits = random.sample(digits_pool, 4)
            selected_digits.sort()
            digits_str = ", ".join(map(str, selected_digits))

            # Tính toán kết quả: Vì chọn 4 chữ số khác nhau để lập số có 4 chữ số khác nhau
            # Kết quả luôn là 4! = 4 * 3 * 2 * 1 = 24
            # Để bài toán thú vị hơn và đúng tính chất random, ta có thể random số lượng chữ số trong tập hợp (n)
            n = len(selected_digits) 
            kq_val = math.factorial(n)

            # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            s = set()
            s.add(n**n) # Trường hợp các chữ số có thể lặp lại
            s.add(sum(selected_digits)) # Tổng các chữ số (nhiễu)
            s.add(n * (n-1)) # Chỉnh hợp chập 2 (nhiễu)
            s.add(kq_val + 12)
            s.add(kq_val - 12)

            # Lọc bỏ giá trị trùng với đáp án đúng và đảm bảo số dương
            s = {x for x in s if x != kq_val and x > 0}
            wrong_choices = random.sample(list(s), 3)

            # Các đáp án trắc nghiệm
            da = '$%s$' % (latex(kq_val))
            das1 = '$%s$' % (latex(wrong_choices[0]))
            das2 = '$%s$' % (latex(wrong_choices[1]))
            das3 = '$%s$' % (latex(wrong_choices[2]))

            # B2: Viết lại y hệt bài toán theo mẫu code python
            # Câu hỏi
            noidungcauhoi = ('''Cho các số $%s$ có thể lập được bao nhiêu số tự nhiên có $%s$ chữ số với các chữ số khác nhau?'''
                             % (digits_str, latex(n)))

            # Các đáp án
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải (Viết chi tiết, không viết tắt, dùng %s)
            loigiai = ('''Gọi số tự nhiên có $%s$ chữ số cần tìm là: $\\overline{abcd}, a \\neq 0$, khi đó: \\\\
                         $a$ có $%s$ cách chọn \\\\
                         $b$ có $%s$ cách chọn \\\\
                         $c$ có $%s$ cách chọn \\\\
                         $d$ có $%s$ cách chọn \\\\
                         Vậy có: $%s \\cdot %s \\cdot %s \\cdot %s = %s$ số.'''
                       % (latex(n), 
                          latex(n), 
                          latex(n-1), 
                          latex(n-2), 
                          latex(n-3),
                          latex(n), latex(n-1), latex(n-2), latex(n-3), latex(kq_val)
                         ))

            # Xuất câu trắc nghiệm (Phần content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

