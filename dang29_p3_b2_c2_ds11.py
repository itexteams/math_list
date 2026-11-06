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


def bt_dang29_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- 1. Random hóa bài toán Cấp số cộng ---
                # n là số hàng cây, cũng là đáp án đúng
                # Chọn n ngẫu nhiên trong khoảng hợp lý (ví dụ từ 40 đến 150)
                n = random.randint(40, 150) 

                # Tính tổng số cây Sn = n(n+1)/2
                Sn = n * (n + 1) // 2 

                # Chuyển sang dạng chuỗi để đưa vào latex
                n_str = str(n)
                Sn_str = str(Sn)
                hai_Sn = 2 * Sn
                nghiem_am = -(n + 1)

                # --- 2. Tạo các Đáp án Trắc nghiệm ---
                # Đáp án đúng
                da = '$%s$'%(n_str)

                # Tạo các đáp án nhiễu
                # Sử dụng các giá trị gần n
                s = ['$%s$'%(str(n+1)),
                     '$%s$'%(str(n+2)),
                     '$%s$'%(str(n-1)),
                     '$%s$'%(str(n-2)),
                     '$%s$'%(str(n + random.choice([3, 5, 10]))), # Nhiễu xa hơn
                     '$%s$'%(str(n - random.choice([3, 5, 10]))), # Nhiễu xa hơn
                    ]

                # Chọn 3 đáp án sai ngẫu nhiên
                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Câu hỏi
                noidungcauhoi = ('''Một người trồng cây theo các hàng ngang với quy luật: ở hàng thứ nhất có 1 cây, ở hàng thứ hai có 2 cây, ở hàng thứ ba có 3 cây, $\\dots$, ở hàng thứ $n$ có $n$ cây. Biết rằng người ta trồng hết $%s$ cây.
            Hỏi số hàng cây được trồng theo cách trên là bao nhiêu?'''
                                 %(Sn_str))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Bài toán là tìm số $n$ khi biết tổng $S_n$ của một cấp số cộng với số hạng đầu $u_1=1$ và công sai $d=1$.
            Sử dụng công thức tổng cấp số cộng:
            $$S_n = \\frac{n(u_1+u_n)}{2} = \\frac{n(1+n)}{2}$$
            Theo đề bài, tổng số cây là $%s$, ta có phương trình:
            $$\\frac{n(n+1)}{2} = %s$$
            $$\\Leftrightarrow n(n+1) = %s$$
            $$\\Leftrightarrow n^2 + n - %s = 0$$
            Giải phương trình bậc hai (hoặc nhẩm $n(n+1)$ gần bằng $%s$):
            $$\\begin{cases} n = %s \\text{ (thỏa mãn } n \\in \\mathbb{N}^* \\text{)} \\\\ n = %s \\text{ (không thỏa mãn)} \\end{cases}$$
            Vậy số hàng cây được trồng là $%s$.'''
                       %(Sn_str, Sn_str, str(hai_Sn), str(hai_Sn), str(hai_Sn), n_str, str(nghiem_am), n_str))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(n_str))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

