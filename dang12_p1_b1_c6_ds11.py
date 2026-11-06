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


def bt_dang12_p1_b1_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # m: số học sinh nam, f: số học sinh nữ
                m = randint(4, 7)
                f = randint(5, 8)

                # Tính toán số cách chọn
                # Biến cố A: 2 nam, 1 nữ
                nA = math.comb(m, 2) * math.comb(f, 1)
                # Biến cố B: 1 nam, 2 nữ
                nB = math.comb(m, 1) * math.comb(f, 2)
                # Tổng số cách (Biến cố H)
                kq_v = nA + nB

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                kq = str(kq_v).replace('.', ',')
                da_dung = '$%s$' % (kq)

                # Tạo danh sách các phương án sai
                s_wrong = set()
                # Các trường hợp sai phổ biến: chọn bất kì 3 người, hoặc chỉ tính 1 trường hợp
                sai_tong = math.comb(m + f, 3)
                if sai_tong != kq_v: s_wrong.add(sai_tong)
                if nA != kq_v: s_wrong.add(nA)
                if nB != kq_v: s_wrong.add(nB)

                # Bổ sung thêm các đáp án nhiễu khác để đủ 3 câu sai
                offset = 5
                while len(s_wrong) < 6:
                    val = kq_v + offset
                    if val != kq_v and val > 0:
                        s_wrong.add(val)
                    val_sub = kq_v - offset
                    if val_sub != kq_v and val_sub > 0:
                        s_wrong.add(val_sub)
                    offset += 5

                s_list = list(s_wrong)
                random.shuffle(s_list)

                das1 = '$%s$' % (str(s_list[0]).replace('.', ','))
                das2 = '$%s$' % (str(s_list[1]).replace('.', ','))
                das3 = '$%s$' % (str(s_list[2]).replace('.', ','))

                # Câu hỏi
                noidungcauhoi = ('''Một đội văn nghệ có $%s$ học sinh nam và $%s$ học sinh nữ. Giáo viên phụ trách đội muốn chọn ra một đội tốp ca gồm $3$ học sinh sao cho có cả nam và nữ cùng tham gia. Số cách chọn một đội như vậy là'''
                                 % (latex(m), latex(f)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 1 & 2: Viết lại lời giải chi tiết theo mẫu ảnh
                # Lời giải chi tiết, sử dụng \left( \right) và ký hiệu tổ hợp C_n^k
                loigiai = ('''Gọi $H$: "Trong $3$ học sinh chọn ra có cả nam và nữ"; \\\\
                             $A$: "Trong $3$ học sinh chọn ra có $2$ học sinh nam và $1$ học sinh nữ"; \\\\
                             $B$: "Trong $3$ học sinh chọn ra có $1$ học sinh nam và $2$ học sinh nữ". \\\\
                             Khi đó $H = A \\cup B$ và $A \\cap B = \\varnothing$. \\\\
                             Do hai biến cố $A$ và $B$ là xung khắc nên $n\\left(H\\right) = n\\left(A\\right) + n\\left(B\\right)$. \\\\
                             Số các kết quả thuận lợi cho biến cố $A$ là: $n\\left(A\\right) = C_{%s}^{2} \\cdot C_{%s}^{1} = %s$. \\\\
                             Số các kết quả thuận lợi cho biến cố $B$ là: $n\\left(B\\right) = C_{%s}^{1} \\cdot C_{%s}^{2} = %s$. \\\\
                             Số các kết quả thuận lợi cho biến cố $H$ là: $n\\left(H\\right) = n\\left(A\\right) + n\\left(B\\right) = %s + %s = %s$.'''
                           % (latex(m), latex(f), latex(nA),
                              latex(m), latex(f), latex(nB),
                              latex(nA), latex(nB), latex(kq_v)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

