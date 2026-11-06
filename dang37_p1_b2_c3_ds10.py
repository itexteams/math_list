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


def bt_dang37_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các giá trị xi liên tiếp
                x1 = random.randint(1, 10)
                x2 = x1 + 1
                x3 = x1 + 2
                x4 = x1 + 3
                x5 = x1 + 4

                # Random các tần số tương đối (tổng bằng 1.0)
                splits = sorted(random.sample(range(5, 100, 5), 4))
                f1_int = splits[0]
                f2_int = splits[1] - splits[0]
                f3_int = splits[2] - splits[1]
                f4_int = splits[3] - splits[2]
                f5_int = 100 - splits[3]

                f1 = f1_int / 100
                f2 = f2_int / 100
                f3 = f3_int / 100
                f4 = f4_int / 100
                f5 = f5_int / 100

                # Tính toán kết quả số trung bình
                mean_val = x1*f1 + x2*f2 + x3*f3 + x4*f4 + x5*f5

                # Chuẩn hóa định dạng hiển thị kết quả đúng (dấu phẩy theo chuẩn VN)
                kq = str(round(mean_val, 3)).replace('.', ',')
                if kq.endswith(',0'):
                    kq = kq[:-2]

                # Chuẩn hóa định dạng hiển thị cho bảng tần số
                sf1 = str(f1).replace('.', ',')
                sf2 = str(f2).replace('.', ',')
                sf3 = str(f3).replace('.', ',')
                sf4 = str(f4).replace('.', ',')
                sf5 = str(f5).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các đáp án nhiễu
                s = [
                    '$%s$'%(str(round(mean_val + 0.15, 2)).replace('.', ',')),
                    '$%s$'%(str(round(mean_val - 0.25, 2)).replace('.', ',')),
                    '$%s$'%(str(round(mean_val + 0.5, 2)).replace('.', ',')),
                    '$%s$'%(str(round(mean_val - 0.5, 2)).replace('.', ',')),
                    '$%s$'%(str(round(mean_val + 1.25, 2)).replace('.', ',')),
                    '$%s$'%(str(round(mean_val - 1.15, 2)).replace('.', ',')),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi (sử dụng dạng tabular chuẩn của LaTeX cho bảng)
                noidungcauhoi = ('''Cho mẫu số liệu có bảng tần số tương đối như sau:
            \\begin{center}
            \\begin{tabular}{|l|c|c|c|c|c|}
            \\hline
            Giá trị $x_i$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
            \\hline
            Tần số tương đối $f_i$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
            \\hline
            \\end{tabular}
            \\end{center}
            Ta có số trung bình của mẫu số liệu là:'''
                                 %(x1, x2, x3, x4, x5, sf1, sf2, sf3, sf4, sf5))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có số trung bình của mẫu số liệu là: \\\\
            $\\overline{x} = %s \\cdot %s + %s \\cdot %s + %s \\cdot %s + %s \\cdot %s + %s \\cdot %s = %s$.'''
                           %(x1, sf1, x2, sf2, x3, sf3, x4, sf4, x5, sf5, kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

