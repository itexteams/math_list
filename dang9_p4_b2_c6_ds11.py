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


def bt_dang9_p4_b2_c6_ds11(self):
            # Khai báo biến
            # Chọn tổng số thẻ N (thường là 10, 12, 15, 20 để xác suất ra số thập phân đẹp)
            list_N = [10, 20]
            N = random.choice(list_N)

            # Random ngưỡng k1 và k2 sao cho A và B xung khắc (không có phần tử chung)
            # Trong ảnh: N=10, k1=6, k2=5.
            k1 = random.randint(N // 2 + 1, N - 2)  # Ngưỡng cho biến cố A
            k2 = random.randint(2, k1 - 1)          # Ngưỡng cho biến cố B

            # Tính toán số phần tử
            nA = N - k1
            nB = k2

            # Tính xác suất
            pA = Rational(nA, N)
            pB = Rational(nB, N)
            p_union = pA + pB

            # Chuyển đổi sang định dạng hiển thị (dấu phẩy cho số thập phân)
            def format_decimal(val):
                res = str(float(val)).replace('.', ',')
                if res.endswith(',0'):
                    res = res[:-2]
                return res

            da_dung_val = format_decimal(p_union)
            pA_str = format_decimal(pA)
            pB_str = format_decimal(pB)

            # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
            s = set()
            # Sai lầm 1: Chỉ tính P(A)
            s.add(format_decimal(pA))
            # Sai lầm 2: Chỉ tính P(B)
            s.add(format_decimal(pB))
            # Sai lầm 3: Tính tích xác suất (nhầm sang biến cố độc lập)
            s.add(format_decimal(pA * pB))
            # Sai lầm 4: Một giá trị ngẫu nhiên khác
            s.add(format_decimal(Rational(random.randint(1, N-1), N)))

            # Loại bỏ đáp án đúng nếu lỡ trùng trong set s
            if da_dung_val in s:
                s.remove(da_dung_val)

            list_sai = list(s)
            random.shuffle(list_sai)

            das1 = list_sai[0]
            das2 = list_sai[1]
            das3 = list_sai[2]

            # Bước 2: Viết lại nội dung theo mẫu
            noidungcauhoi = (
                'Một chiếc hộp có ' + str(N) + ' chiếc thẻ cùng loại được đánh số từ 1 đến ' + str(N) + '. Rút ngẫu nhiên từ hộp ra 1 thẻ. Xét các biến cố:\\\\'
                'A: "Số ghi trên thẻ được lấy ra là số lớn hơn ' + str(k1) + '";\\\\'
                'B: "Số ghi trên thẻ được lấy ra là không vượt quá ' + str(k2) + '";\\\\'
                'Tính xác suất của biến cố $A \\cup B$.'
            )

            # Tạo danh sách các phần tử của A và B cho lời giải
            list_A = "{" + "; ".join(map(str, range(k1 + 1, N + 1))) + "}"
            list_B = "{" + "; ".join(map(str, range(1, k2 + 1))) + "}"

            loigiai = (
                'Không gian mẫu $n\\left(\\Omega\\right) = ' + str(N) + '$.\\\\'
                'A: "Số ghi trên thẻ được lấy ra là số lớn hơn ' + str(k1) + '" $\\Rightarrow A = ' + list_A + ' \\Rightarrow n\\left(A\\right) = ' + str(nA) + '$.\\\\'
                '$P\\left(A\\right) = \\frac{n\\left(A\\right)}{n\\left(\\Omega\\right)} = ' + pA_str + '$.\\\\'
                'B: "Số ghi trên thẻ được lấy ra là không vượt quá ' + str(k2) + '" $\\Rightarrow B = ' + list_B + ' \\Rightarrow n\\left(B\\right) = ' + str(nB) + '$.\\\\'
                '$P\\left(B\\right) = \\frac{n\\left(B\\right)}{n\\left(\\Omega\\right)} = ' + pB_str + '$.\\\\'
                'Vì $A, B$ là hai biến cố xung khắc nên: $P\\left(A \\cup B\\right) = P\\left(A\\right) + P\\left(B\\right) = ' + da_dung_val + '$.'
            )

            # Các đáp án
            da_d = '\\True $' + da_dung_val + '$'
            da_s1 = '$' + das1 + '$'
            da_s2 = '$' + das2 + '$'
            da_s3 = '$' + das3 + '$'

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Xuất câu trắc nghiệm theo đúng cấu trúc content
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

