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


def bt_dang45_p4_b1_c5_ds10(self):
            # Khai báo biến
            # Chọn ngẫu nhiên 5 chữ số khác nhau từ 1 đến 9 để đảm bảo không có số 0 (tránh phức tạp hóa bài toán)
            all_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            chosen_digits = random.sample(all_digits, 5)
            chosen_digits.sort()

            d1, d2, d3, d4, d5 = chosen_digits
            sum_d = sum(chosen_digits)

            # Tính toán các thông số theo logic hình ảnh
            # Số các số lập được là chỉnh hợp chập 3 của 5 phần tử: A(5,3) = 60
            so_cac_so = 60 
            # Số lần xuất hiện của mỗi chữ số ở mỗi hàng: 60 / 5 = 12
            so_lan = 12
            # Tổng các số: S = 12 * (d1+d2+d3+d4+d5) * (100 + 10 + 1)
            tong_gia_tri = so_lan * sum_d * 111

            # B4: Tạo các phương án sai không trùng với đáp án đúng
            da_dung = tong_gia_tri
            s = set()
            while len(s) < 3:
                # Tạo các phương án nhiễu bằng cách thay đổi tổng chữ số hoặc số lần xuất hiện
                sai = da_dung + random.choice([-111, 111, -222, 222, -10, 10, -100, 100])
                if sai != da_dung and sai > 0:
                    s.add(sai)

            list_sai = list(s)
            das1 = list_sai[0]
            das2 = list_sai[1]
            das3 = list_sai[2]

            # Nội dung câu hỏi
            # Chuyển danh sách chữ số thành chuỗi định dạng "1, 2, 3, 4, 6"
            str_digits = ", ".join(map(str, chosen_digits))

            noidungcauhoi = ('''Cho 5 chữ số $%s$. Lập các số tự nhiên có 3 chữ số đôi một khác nhau từ 5 chữ số đã cho. Tỉnh tổng của các số lập được.'''
                             %(str_digits))

            # Nội dung lời giải chi tiết (B2)
            loigiai = ('''Mỗi số tự nhiên có 3 chữ số đôi một khác nhau từ 5 chữ số $%s$ là một chỉnh hợp chập 3 của các chữ số này. Do đó, ta lập được $A_5^3 = %s$ số. \\\\
            Do vai trò các số $%s$ như nhau, nên số lần xuất hiện của mỗi chữ số trong các chữ số này ở mỗi hàng là như nhau và bằng $%s : 5 = %s$ lần. \\\\
            Vậy, tổng các số lập được là: \\\\
            $S = %s \\cdot \\left( %s + %s + %s + %s + %s \\right) \\cdot \\left( 100 + 10 + 1 \\right) = %s$.'''
                       %(str_digits, latex(so_cac_so), str_digits, 
                         latex(so_cac_so), latex(so_lan),
                         latex(so_lan), latex(d1), latex(d2), latex(d3), latex(d4), latex(d5), 
                         latex(da_dung)))

            # Thiết lập các đáp án trắc nghiệm
            da_d = ('\\True $%s$' % (latex(da_dung)))
            da_s1 = ('$%s$' % (latex(das1)))
            da_s2 = ('$%s$' % (latex(das2)))
            da_s3 = ('$%s$' % (latex(das3)))

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

