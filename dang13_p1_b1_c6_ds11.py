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


def bt_dang13_p1_b1_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1 & 3: Nghiên cứu đề bài và tạo thông số ngẫu nhiên
                # n_x: số quả cầu xanh, n_t: số quả cầu trắng
                n_x = randint(4, 10)
                n_t = randint(5, 12)

                # Tính toán lời giải
                # Số cách chọn 2 quả xanh: C(n_x, 2)
                nA = math.comb(n_x, 2)
                # Số cách chọn 2 quả trắng: C(n_t, 2)
                nB = math.comb(n_t, 2)
                # Tổng số cách: n(H) = n(A) + n(B)
                kq_chinh_xac = nA + nB

                # Bước 4: Tạo các phương án sai không trùng với đáp án đúng
                s_fake = set()
                while len(s_fake) < 3:
                    # Tạo phương án sai dựa trên các lỗi thường gặp hoặc ngẫu nhiên
                    sai1 = math.comb(n_x + n_t, 2) # Chọn 2 quả bất kỳ
                    sai2 = n_x * n_t               # Chọn 1 xanh 1 trắng
                    sai3 = nA + nB + randint(1, 5) # Sai số ngẫu nhiên
                    sai4 = abs(nA + nB - randint(1, 5))

                    candidates = [sai1, sai2, sai3, sai4]
                    for c in candidates:
                        if c != kq_chinh_xac and c > 0:
                            s_fake.add(c)
                        if len(s_fake) == 3:
                            break

                list_fake = list(s_fake)

                # Định dạng đáp án
                da_d = '\\True ' + str(kq_chinh_xac).replace('.', ',')
                da_s1 = str(list_fake[0]).replace('.', ',')
                da_s2 = str(list_fake[1]).replace('.', ',')
                da_s3 = str(list_fake[2]).replace('.', ',')

                # Đưa các đáp án vào danh sách và trộn
                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # Bước 2: Viết lại bài toán và lời giải theo mẫu (Thay ( ) bằng \left( \right))
                noidungcauhoi = ('''Một hộp có $%s$ quả cầu xanh khác nhau và $%s$ quả cầu trắng khác nhau. Lấy ngẫu nhiên đồng thời $2$ quả cầu. Số cách lấy ra hai quả cầu cùng màu là'''
                                 % (latex(n_x), latex(n_t)))

                loigiai = ('''Gọi biến cố $A$ "Lấy ra hai quả cầu màu xanh"\\\\
            Biến cố $B$ "Lấy ra hai quả cầu màu trắng".\\\\
            Biến cố $H$ "Lấy ra hai quả cầu cùng màu"\\\\
            Khi đó $H = A \\cup B$ và $A \\cap B = \\varnothing$.\\\\
            Do hai biến cố $A$ và $B$ là xung khắc nên $n\\left(H\\right) = n\\left(A\\right) + n\\left(B\\right)$\\\\
            Số các kết quả thuận lợi cho biến cố $A$ là: $n\\left(A\\right) = C_{%s}^{2} = %s$.\\\\
            Số các kết quả thuận lợi cho biến cố $B$ là: $n\\left(B\\right) = C_{%s}^{2} = %s$.\\\\
            Số các kết quả thuận lợi cho biến cố $H$ là: $n\\left(H\\right) = n\\left(A\\right) + n\\left(B\\right) = %s + %s = %s$.'''
                           % (latex(n_x), latex(nA), latex(n_t), latex(nB), latex(nA), latex(nB), latex(kq_chinh_xac)))

            # Xuất câu trắc nghiệm (không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_ans[0]) + '}\n'
                '{' + str(list_ans[1]) + '}\n'
                '{' + str(list_ans[2]) + '}\n'
                '{' + str(list_ans[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

