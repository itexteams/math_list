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


def bt_dang11_p4_b3_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random xác suất của 3 vận động viên (từ 0,5 đến 0,95)
                p1_val = random.choice([0.7, 0.75, 0.8, 0.85, 0.9])
                p2_val = random.choice([0.6, 0.65, 0.7, 0.75, 0.8])
                p3_val = random.choice([0.5, 0.55, 0.6, 0.65, 0.7])

                # Tính toán đáp án đúng
                kq_val = p1_val * p2_val * p3_val
                # Làm tròn và đổi dấu phẩy cho hiển thị
                kq_str = str(round(kq_val, 3)).replace('.', ',')

                # Tạo các đáp án nhiễu
                # Sai lầm 1: Tổng xác suất (nếu > 1 thì lấy 1 trừ đi)
                s1_val = round(abs(1 - (p1_val * p2_val)), 3)
                # Sai lầm 2: Xác suất ít nhất một người vượt qua
                s2_val = round(1 - (1 - p1_val) * (1 - p2_val) * (1 - p3_val), 3)
                # Sai lầm 3: Trung bình cộng hoặc một số ngẫu nhiên
                s3_val = round((p1_val + p2_val + p3_val) / 3, 3)

                da = '$P = %s$' % kq_str

                # Danh sách các phương án sai, đảm bảo không trùng đáp án đúng
                s = [
                    '$P = %s$' % str(s1_val).replace('.', ','),
                    '$P = %s$' % str(s2_val).replace('.', ','),
                    '$P = %s$' % str(s3_val).replace('.', ','),
                    '$P = %s$' % str(round(kq_val + 0.12, 3)).replace('.', ','),
                    '$P = %s$' % str(round(abs(kq_val - 0.15), 3)).replace('.', ',')
                ]

                # Loại bỏ giá trị nếu lỡ trùng với đáp án đúng
                s = [x for x in s if x != da]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Có ba vận động viên cùng thi chạy vượt rào. Xác suất để ba vận động viên này vượt qua được rào lần lượt là $%s; %s; %s$. Tính xác suất để cả ba vận động viên vượt qua được rào.'''
                                 % (str(p1_val).replace('.', ','), str(p2_val).replace('.', ','), str(p3_val).replace('.', ',')))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn ngẫu nhiên đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Gọi biến cố $A$: "Cả ba vận động viên vượt qua được rào".\\\\
                             Gọi $A_i$ là biến cố: "Vận động viên thứ $i$ vượt qua được rào" với $i \\in \\left\\{1; 2; 3\\right\\}$.\\\\
                             Theo bài ra ta có: $P\\left(A_1\\right) = %s; P\\left(A_2\\right) = %s; P\\left(A_3\\right) = %s$.\\\\
                             Vì các vận động viên thi đấu độc lập nên các biến cố $A_1, A_2, A_3$ độc lập với nhau.\\\\
                             Vậy xác suất để cả ba vận động viên cùng vượt qua rào là:\\\\
                             $P\\left(A\\right) = P\\left(A_1\\right) \\cdot P\\left(A_2\\right) \\cdot P\\left(A_3\\right) = %s \\cdot %s \\cdot %s = %s$.'''
                           % (str(p1_val).replace('.', ','), str(p2_val).replace('.', ','), str(p3_val).replace('.', ','),
                              str(p1_val).replace('.', ','), str(p2_val).replace('.', ','), str(p3_val).replace('.', ','),
                              kq_str))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

