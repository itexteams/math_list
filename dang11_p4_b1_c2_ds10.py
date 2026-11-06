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


def bt_dang11_p4_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến và chọn dạng (giữ cấu trúc mẫu)
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Random hệ số a, b, c cho bất phương trình ax + by >= c (hoặc <=, >, <)
                # Ở đây mẫu là x + 2y >= 0
                a = random.choice([1, 2, 3, 4, 5])
                b = random.choice([1, 2, 3, 4, 5])
                c = random.randint(-10, 10)
                y_val = random.randint(-5, 5)

                # Tạo chuỗi hiển thị bất phương trình
                # Chú ý xử lý dấu để không bị hiển thị + - hoặc 1x
                expr_left = ""
                if a == 1: expr_left += "x"
                else: expr_left += f"{a}x"

                if b == 1: expr_left += " + y"
                else: expr_left += f" + {b}y"

                # Thay thế các trường hợp dấu đặc biệt nếu có số âm (ví dụ + - thành -)
                expr_left = expr_left.replace("+ -", "- ")

                dau = random.choice(["\\ge", "\\le", ">", "<"])

                # B2: Viết lại y hệt bài toán theo mẫu
                # Câu hỏi
                noidungcauhoi = ('''Cho bất phương trình bậc nhất hai ẩn $%s %s %s$. Với $y = %s$, tìm số giá trị của $x$ thỏa mãn bất phương trình đã cho.'''
                                %(expr_left, dau, latex(c), latex(y_val)))

                # Đáp án đúng luôn là Vô số
                da_d = '\\True Vô số'

                # Các đáp án nhiễu
                s = ['0', '1', '2', '2026', '100','%s'%(latex(a),)] 
                random.shuffle(s)

                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # B1: Nghiên cứu lời giải - Bất phương trình bậc nhất luôn có vô số nghiệm khi cố định 1 biến
                loigiai = ('''Thay $y = %s$ vào bất phương trình ta được: $%s \\cdot x + %s \\cdot (%s) %s %s \\Leftrightarrow %s x %s %s$. \\\\
                           Đây là bất phương trình bậc nhất một ẩn $x$, do đó luôn có vô số giá trị $x$ thỏa mãn.'''
                          %(latex(y_val), latex(a), latex(b), latex(y_val), dau, latex(c), latex(a), dau, latex(c - b*y_val)))

            # Xuất câu trắc nghiệm (Đúng định dạng yêu cầu)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

