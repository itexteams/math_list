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


def bt_dang22_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số liệu (chuyển dấu . thành dấu , cho số thập phân)
            def format_num(num):
                if num == int(num):
                    return str(int(num))
                return str(round(num, 2)).replace('.', ',')

            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số liệu xung quanh các giá trị thực tế của đề bài gốc
                a = random.randint(200, 205) * 100 # Cẩm phả
                b = random.randint(210, 215) * 100 # Thiên Trường
                c = random.randint(230, 235) * 100 # Hàng Đẫy
                d = random.randint(200, 205) * 100 # Thanh Hoá
                e = random.randint(350, 400) * 100 # Mỹ Đình

                # Tính toán
                tong5 = a + b + c + d + e
                tb5 = tong5 / 5

                tong4 = a + b + c + d
                tb4 = tong4 / 4

                diff = tb5 - tb4

                # Định dạng chuỗi xuất ra LaTeX
                a_s = format_num(a)
                b_s = format_num(b)
                c_s = format_num(c)
                d_s = format_num(d)
                e_s = format_num(e)
                tong5_s = format_num(tong5)
                tb5_s = format_num(tb5)
                tong4_s = format_num(tong4)
                tb4_s = format_num(tb4)
                diff_s = format_num(diff)

                # Các đáp án trắc nghiệm
                da = f'Giảm ${diff_s}$'

                # Tạo các phương án sai ngẫu nhiên
                s = [
                    f'Tăng ${diff_s}$',
                    f'Giảm ${format_num(diff + random.randint(10, 50) * 10)}$',
                    f'Giảm ${format_num(diff - random.randint(10, 50) * 10)}$',
                    f'Tăng ${format_num(diff + random.randint(10, 50) * 10)}$',
                    f'Tăng ${format_num(diff - random.randint(10, 50) * 10)}$'
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Bảng sau đây cho biết số chỗ ngồi của một số sân vận động được sử dụng trong Giải Bóng đá Vô địch Quốc gia Việt Nam năm 2018 (số liệu gần đúng).
            \\begin{center}
            \\begin{tabular}{|c|c|c|c|c|c|}
            \\hline
            \\textbf{Sân vận động} & Cẩm phả & Thiên Trường & Hàng Đẫy & Thanh Hoá & Mỹ Đình \\\\
            \\hline
            \\textbf{Chỗ ngồi} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
            \\hline
            \\end{tabular}
            \\end{center}
            Giá trị số trung bình bị ảnh hưởng như thế nào nếu bỏ đi số liệu chỗ ngồi của Sân vận động Quốc gia Mỹ Đình?'''
                                 %(a_s, b_s, c_s, d_s, e_s))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Số trung bình cộng các số liệu của $5$ sân vận động là:
            $$ \\frac{%s + %s + %s + %s + %s}{5} = \\frac{%s}{5} = %s $$
            Khi bỏ đi số liệu chỗ ngồi của sân Mỹ Đình, ta có số trung bình cộng của $4$ sân còn lại là:
            $$ \\frac{%s + %s + %s + %s}{4} = \\frac{%s}{4} = %s $$
            Ta có: $%s - %s = %s > 0$.\\\\
            Vậy nếu bỏ đi số liệu của sân Mỹ Đình thì giá trị số trung bình giảm $%s$.'''
                         %(a_s, b_s, c_s, d_s, e_s, tong5_s, tb5_s,
                           a_s, b_s, c_s, d_s, tong4_s, tb4_s,
                           tb5_s, tb4_s, diff_s,
                           diff_s))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

