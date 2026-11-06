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


def bt_dang32_p1_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các giá trị ngẫu nhiên
                # Hàm số có dạng: sqrt(x + a + 1 + 2*sqrt(x + a)) + 1/(b - x)
                a = randint(2, 15)
                b = randint(1, 10)

                # Đảm bảo b không trùng với điểm đầu mút -a để tập xác định có ý nghĩa
                if b == -a:
                    b = a + 1

                # Tính toán các thành phần để đưa vào đề bài
                a_plus_1 = a + 1
                minus_a = -a

                # Đáp án đúng
                da_dung = r'D = [%s; +\infty) \setminus \{%s\}' % (minus_a, b)

                # Các đáp án nhiễu (sai)
                s1 = r'D = (%s; +\infty) \setminus \{%s\}' % (minus_a, b) # Sai ngoặc vuông/tròn
                s2 = r'D = [%s; +\infty)' % (minus_a) # Thiếu điều kiện mẫu số
                s3 = r'D = (-\infty; %s] \setminus \{%s\}' % (minus_a, b) # Ngược dấu bất phương trình
                s4 = r'D = [%s; %s]' % (minus_a, b) # Sai định dạng khoảng
                s5 = r'D = \mathbb{R} \setminus \{%s\}' % (b) # Quên điều kiện căn thức

                # Chọn ngẫu nhiên 3 đáp án sai từ danh sách nhiễu
                list_sai_all = [s1, s2, s3, s4, s5]
                random.shuffle(list_sai_all)

                da_s1 = '$' + list_sai_all[0] + '$'
                da_s2 = '$' + list_sai_all[1] + '$'
                da_s3 = '$' + list_sai_all[2] + '$'

                # Câu hỏi
                noidungcauhoi = (r'Tập xác định của hàm số $y = \sqrt{x + %s + 2\sqrt{x + %s}} + \frac{1}{%s - x}$ là'
                                 % (latex(a_plus_1), latex(a), latex(b)))

                # Các đáp án trắc nghiệm
                da_d = r'\True $' + da_dung + '$'

                # Trộn thứ tự đáp án
                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # Nội dung lời giải
                loigiai = (r'''Ta có $y = \sqrt{x + %s + 2\sqrt{x + %s}} + \frac{1}{%s - x} = \sqrt{(\sqrt{x + %s} + 1)^2} + \frac{1}{%s - x} = \sqrt{x + %s} + 1 + \frac{1}{%s - x}$. \\
                            Hàm số xác định khi $\begin{cases} x + %s \ge 0 \\ %s - x \neq 0 \end{cases} \Leftrightarrow \begin{cases} x \ge %s \\ x \neq %s \end{cases}$. \\
                            Vậy tập xác định của hàm số là $D = [%s; +\infty) \setminus \{%s\}$.'''
                           % (latex(a_plus_1), latex(a), latex(b), latex(a), latex(b), latex(a), latex(b),
                              latex(a), latex(b), latex(minus_a), latex(b), latex(minus_a), latex(b)))

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

