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


def bt_dang22_p4_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hàm số: có 2 dạng chính là cot(x) hoặc tan(x) để đổi mới đề bài
                # Chọn ngẫu nhiên giữa tìm tập xác định của cot(x) và tan(x)
                loai_ham = random.choice(['cot', 'tan'])

                # Random ngẫu nhiên các hệ số nhiễu trong hàm số (sin(ax) + cos(bx)) để tạo sự khác biệt
                a = random.randint(2, 6)
                b = random.randint(2, 6)
                while b == a:
                    b = random.randint(2, 6)

                # Tạo chuỗi latex cho hàm số hiển thị trong đề bài
                if loai_ham == 'cot':
                    ham_so = 'y = \\cot x + \\sin %sx + \\cos %sx' % (latex(a), latex(b))
                    dieu_kien = '\\sin x \\neq 0 \\Leftrightarrow x \\neq k\\pi'
                    da_dung = 'D = \\mathbb{R} \\setminus \\{k\\pi, k \\in \\mathbb{Z}\\}'

                    # Các phương án sai
                    s = [
                        'D = \\mathbb{R} \\setminus \\{\\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}\\}',
                        'D = \\mathbb{R} \\setminus \\{\\frac{\\pi}{2} + k2\\pi, k \\in \\mathbb{Z}\\}',
                        'D = \\mathbb{R} \\setminus \\{k2\\pi, k \\in \\mathbb{Z}\\}',
                        'D = \\mathbb{R} \\setminus \\{\\frac{k\\pi}{2}, k \\in \\mathbb{Z}\\}',
                        'D = \\mathbb{R} \\setminus \\{\\pi + k2\\pi, k \\in \\mathbb{Z}\\}'
                    ]
                else:
                    ham_so = 'y = \\tan x + \\sin %sx + \\cos %sx' % (latex(a), latex(b))
                    dieu_kien = '\\cos x \\neq 0 \\Leftrightarrow x \\neq \\frac{\\pi}{2} + k\\pi'
                    da_dung = 'D = \\mathbb{R} \\setminus \\{\\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}\\}'

                    # Các phương án sai
                    s = [
                        'D = \\mathbb{R} \\setminus \\{k\\pi, k \\in \\mathbb{Z}\\}',
                        'D = \\mathbb{R} \\setminus \\{\\frac{\\pi}{2} + k2\\pi, k \\in \\mathbb{Z}\\}',
                        'D = \\mathbb{R} \\setminus \\{k2\\pi, k \\in \\mathbb{Z}\\}',
                        'D = \\mathbb{R} \\setminus \\{\\frac{k\\pi}{2}, k \\in \\mathbb{Z}\\}',
                        'D = \\mathbb{R} \\setminus \\{\\pi + k2\\pi, k \\in \\mathbb{Z}\\}'
                    ]

                # Chọn ngẫu nhiên 3 đáp án sai khác nhau hoàn toàn từ danh sách nhiễu
                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Câu hỏi
                noidungcauhoi = ('''Tìm tập xác định $D$ của hàm số $%s$.'''
                                 % (ham_so))

                # Các đáp án
                da_d = ('\\True $' + str(da_dung) + '$')
                da_s1 = ('$' + str(das1) + '$')
                da_s2 = ('$' + str(das2) + '$') 
                da_s3 = ('$' + str(das3) + '$') 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải đầy đủ, chi tiết theo ảnh gốc
                if loai_ham == 'cot':
                    loigiai = ('''Hàm số xác định khi: $%s$. \\\\
                             Vậy $%s$'''
                             % (dieu_kien, da_dung))
                else:
                    loigiai = ('''Hàm số xác định khi: $%s$. \\\\
                             Vậy $%s$'''
                             % (dieu_kien, da_dung))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

