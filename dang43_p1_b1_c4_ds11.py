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


def bt_dang43_p1_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: SUY NGHĨ TÌM CÁCH RANDOM ---
                # Bài toán gốc là n+4 và n+1. Ta tổng quát hóa thành n+a và n+b
                # Để đảm bảo tử số dương và dễ nhìn giống bài mẫu, ta chọn a > b > 0

                b = randint(1, 5)        # Random số bé (ví dụ n+1)
                delta = randint(1, 9)    # Khoảng cách giữa 2 số
                a = b + delta            # Random số lớn (ví dụ n+4)

                # Tính toán các giá trị phụ trợ để điền vào lời giải
                tu_so = a - b            # Tử số sau khi nhân liên hợp: (n+a) - (n+b) = a - b

                # --- CÁC ĐÁP ÁN TRẮC NGHIỆM ---
                # Đáp án đúng luôn là 0 vì bậc tử (0) nhỏ hơn bậc mẫu (2/3)
                kq = 0

                # Tạo các đáp án nhiễu
                # Nhiễu 1: Kết quả là chính cái tử số (quên chia mẫu)
                nhieu_1 = tu_so 
                # Nhiễu 2: Kết quả là 1
                nhieu_2 = 1
                # Nhiễu 3: Dương vô cùng
                nhieu_3 = "+\\infty"

                du = ['$%s$' % kq]
                da = random.choice(du) # Đáp án đúng

                s = [
                    '$%s$' % nhieu_1,
                    '$%s$' % nhieu_2,
                    '$%s$' % nhieu_3
                ]

                # Chọn ngẫu nhiên vị trí các đáp án sai
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (
                    'Giới hạn $L = \\lim_{n\\to+\\infty} \\left(\\sqrt[3]{n+%s} - \\sqrt[3]{n+%s}\\right)$ bằng' 
                    % (a, b)
                )

                # Các đáp án để hiển thị
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- B2: VIẾT LẠI Y HỆT LỜI GIẢI (CÓ THAM SỐ) ---
                # Sử dụng cấu trúc LaTeX khớp với hình ảnh
                loigiai = ('''$L = \\lim_{n\\to+\\infty} \\left(\\sqrt[3]{n+%s} - \\sqrt[3]{n+%s}\\right)$ \\\\
                $= \\lim_{n\\to+\\infty} \\dfrac{%s}{\\sqrt[3]{(n+%s)^2} + \\sqrt[3]{(n+%s)(n+%s)} + \\sqrt[3]{(n+%s)^2}}$ \\\\
                $= \\lim_{n\\to+\\infty} \\dfrac{%s}{\\sqrt[3]{n^2\\cdot\\left(1+\\dfrac{%s}{n}\\right)^2} + \\sqrt[3]{n^2\\cdot\\left(1+\\dfrac{%s}{n}\\right)\\left(1+\\dfrac{%s}{n}\\right)} + \\sqrt[3]{n^2\\cdot\\left(1+\\dfrac{%s}{n}\\right)^2}}$ \\\\
                $= \\lim_{n\\to+\\infty} \\dfrac{%s}{\\sqrt[3]{n^2}\\left[\\sqrt[3]{\\left(1+\\dfrac{%s}{n}\\right)^2} + \\sqrt[3]{\\left(1+\\dfrac{%s}{n}\\right)\\left(1+\\dfrac{%s}{n}\\right)} + \\sqrt[3]{\\left(1+\\dfrac{%s}{n}\\right)^2}\\right]} = 0.$''' % (
                    a, b,                        # Dòng 1: Đề bài
                    tu_so, a, a, b, b,           # Dòng 2: Nhân liên hợp
                    tu_so, a, a, b, b,           # Dòng 3: Rút n^2 trong căn (bước trung gian mô phỏng logic)
                    tu_so, a, a, b, b            # Dòng 4: Kết quả cuối cùng
                ))

            # Xuất câu trắc nghiệm
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

