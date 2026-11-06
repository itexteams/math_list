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


def bt_dang22_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến thể loại
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 & B3: Nghiên cứu đề bài và tạo biến ngẫu nhiên
                # Hàm số có dạng y = x / (a^2 - x^2) - sqrt(-x)
                # Ta chọn a từ 1 đến 5 để số liệu đẹp
                a = randint(1, 5)
                a2 = a**2

                # Tính toán các thành phần để hiển thị
                # Điều kiện: a^2 - x^2 != 0 và -x >= 0
                # <=> x != +/- a và x <= 0
                # Vì a > 0 nên x = a luôn bị loại bởi điều kiện x <= 0. 
                # Do đó tập xác định là D = (-inf; 0] \ {-a}

                # B2: Viết lại bài toán theo mẫu
                # Đáp án đúng
                da_dung = '$D = (-\\infty; 0] \\setminus \\{%s\\}$' % (latex(-a))

                # B4: Tạo các phương án sai (không trùng với đáp án đúng)
                s = [
                    '$D = (-\\infty; 0) \\setminus \\{%s\\}$' % (latex(-a)), # Sai ngoặc ở 0
                    '$D = (-\\infty; 0] \\setminus \\{%s\\}$' % (latex(a)),  # Sai dấu của giá trị loại trừ
                    '$D = (-\\infty; %s] \\setminus \\{%s\\}$' % (latex(a), latex(-a)), # Sai cận khoảng
                    '$D = \\mathbb{R} \\setminus \\{\\pm %s\\}$' % (latex(a)), # Thiếu điều kiện căn thức
                    '$D = (-\\infty; 0]$', # Thiếu điều kiện mẫu thức
                    '$D = [0; +\\infty) \\setminus \\{%s\\}$' % (latex(a)) # Sai chiều bất phương trình
                ]

                # Chọn ngẫu nhiên 3 đáp án sai từ danh sách
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Tìm tập xác định của hàm số $y = \\frac{x}{%s - x^2} - \\sqrt{-x}$.'''
                                 % (latex(a2)))

                # Các đáp án chuẩn hóa
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Tráo thứ tự đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Hàm số xác định khi $\\begin{cases} %s - x^2 \\neq 0 \\\\ -x \\geq 0 \\end{cases} 
                           \\Leftrightarrow \\begin{cases} x \\neq \\pm %s \\\\ x \\leq 0 \\end{cases} 
                           \\Leftrightarrow %s \\neq x \\leq 0$. \\\\
                           Vậy tập xác định của hàm số là $D = (-\\infty; 0] \\setminus \\{%s\\}$.'''
                           % (latex(a2), latex(a), latex(-a), latex(-a)))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

