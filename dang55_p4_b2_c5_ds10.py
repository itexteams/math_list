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


def bt_dang55_p4_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lượng màu (mặc định là 3 như đề bài, có thể mở rộng)
                k = 3 

                # Tính toán theo logic của lời giải trong ảnh
                # Bước 1: Ô đầu tiên (4 cạnh mới)
                # Chọn 2 màu từ k màu: comb(k, 2). Với mỗi cặp màu có 6 cách tô (hoán vị lặp 4!/(2!2!))
                buoc1 = math.comb(k, 2) * 6

                # Bước 2: 3 ô tiếp theo (mỗi ô có 3 cạnh mới, 1 cạnh chung)
                # Cạnh chung đã có màu. Cần chọn thêm 1 màu nữa và sắp xếp 3 cạnh còn lại.
                # Có (k-1) cách chọn màu thứ hai. Có 3 vị trí đặt màu trùng với cạnh chung.
                buoc2_don = (k - 1) * 3
                buoc2_tong = buoc2_don**3

                # Bước 3: 2 ô cuối (mỗi ô có 2 cạnh mới, 2 cạnh chung)
                # Logic: 2 cạnh chung đã cố định, chỉ còn 2 cách để hoàn thành quy tắc.
                buoc3_don = 2
                buoc3_tong = buoc3_don**2

                # Đáp án đúng
                kq_so = buoc1 * buoc2_tong * buoc3_tong
                da = '$%s$' % (latex(kq_so))

                # Tạo các phương án sai
                s = []
                while len(s) < 3:
                    sai = kq_so + random.choice([-100, 100, -1000, 500, -200, 1000, 2500, -5000])
                    if sai > 0 and sai != kq_so and str(sai) not in s:
                        s.append('$%s$' % (latex(sai)))

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Bé Minh có một bảng hình chữ nhật gồm $6$ hình vuông đơn vị, cố định không xoay như hình vẽ. Bé muốn dùng $%s$ màu để tô tất cả các cạnh của các hình vuông đơn vị, mỗi cạnh tô một lần sao cho mỗi hình vuông đơn vị được tô bởi đúng $2$ màu, trong đó mỗi màu tô đúng $2$ cạnh. Tìm số cách tô màu.
            \\\\
            \\begin{center}
            \\begin{tikzpicture}[scale=0.8, line width=1pt]
            \\draw (0,0) grid (3,2);
            \\end{tikzpicture}
            \\end{center}'''
                                 % (latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Tô màu theo nguyên tắc:\\\\
            - Tô $1$ ô vuông có $4$ cạnh mới: Chọn $2$ trong $%s$ màu có $C_{%s}^2$ cách chọn, ứng với mỗi cặp màu được chọn có $6$ cách tô. Do đó, có $6 \\cdot C_{%s}^2 = %s$ cách tô.\\\\
            - Tô $3$ ô vuông có $3$ cạnh mới (có $1$ cạnh chung với ô trước): Ứng với mỗi ô vuông, ta chọn $1$ trong $%s$ màu còn lại để tô cùng với màu của cạnh đã tô trước đó, có $%s \\cdot C_2^1 = %s$ cách tô. Do đó có $%s^3$ cách tô cho $3$ ô này.\\\\
            - Tô $2$ ô vuông có $2$ cạnh mới (có $2$ cạnh chung với các ô trước): Ứng với mỗi ô vuông có $2$ cách tô màu các cạnh còn lại để thỏa mãn điều kiện. Do đó có $2^2 = 4$ cách tô.\\\\
            Vậy tổng số cách tô màu là: $%s \\cdot C_{%s}^2 \\cdot %s^3 \\cdot 4 = %s$ cách tô.'''
                           % (latex(k), latex(k), latex(k), latex(buoc1), 
                              latex(k-1), latex(k-1), latex(buoc2_don), latex(buoc2_don),
                              latex(6), latex(k), latex(buoc2_don), latex(kq_so)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

