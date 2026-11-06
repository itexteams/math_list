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


def bt_dang46_p4_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước B3: Random bài toán
                # nA: Số học sinh học lực Giỏi
                # nB: Số học sinh hạnh kiểm Tốt
                # nAB: Số học sinh vừa Giỏi vừa Tốt (Giao của hai tập hợp)
                nA = randint(15, 30)
                nB = randint(20, 35)
                # Đảm bảo nAB luôn nhỏ hơn nA và nB để bài toán hợp lý
                nAB = randint(5, min(nA, nB) - 5)

                # Kết quả: n(A hợp B) = n(A) + n(B) - n(A giao B)
                kq_val = nA + nB - nAB
                kq = str(kq_val)

                # Bước B4: Tạo các phương án sai không trùng với đáp án đúng
                da = '$%s$' % (kq)

                s = []
                # Phương án sai 1: Quên trừ phần giao
                s1 = nA + nB
                if s1 != kq_val: s.append('$%s$' % latex(s1))

                # Phương án sai 2: Cộng thêm phần giao thay vì trừ
                s2 = nA + nB + nAB
                if s2 != kq_val: s.append('$%s$' % latex(s2))

                # Phương án sai 3: Lấy tổng trừ đi 2 lần phần giao hoặc một số ngẫu nhiên
                s3 = nA + nB - 2*nAB
                if s3 != kq_val and s3 > 0: 
                    s.append('$%s$' % latex(s3))
                else:
                    s.append('$%s$' % latex(kq_val + 5))

                # Đảm bảo đủ phương án nếu có trùng lặp ngẫu nhiên
                while len(s) < 3:
                    random_val = kq_val + randint(2, 10)
                    if str(random_val) not in s and random_val != kq_val:
                        s.append('$%s$' % latex(random_val))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Lớp 10A có $%s$ bạn được xếp loại học lực Giỏi, $%s$ bạn được xếp loại hạnh kiểm Tốt, trong đó có $%s$ bạn vừa được học lực Giỏi vừa được hạnh kiểm Tốt. Tìm số học sinh được xếp loại học lực Giỏi hoặc hạnh kiểm Tốt.'''
                                 %(latex(nA), latex(nB), latex(nAB)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # Sử dụng TikZ để vẽ sơ đồ Venn minh họa
                ve_hinh = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.8, line width=1pt]
                \\draw (0,0) circle (1.5) node[left=1.2cm, above=1.2cm] {$A$};
                \\draw (1.8,0) circle (1.5) node[right=1.2cm, above=1.2cm] {$B$};
                \\node at (-0.5,0) {$%s$};
                \\node at (2.3,0) {$%s$};
                \\node at (0.9,0) {$%s$};
            \\end{tikzpicture}
            \\end{center}''' % (latex(nA - nAB), latex(nB - nAB), latex(nAB)))

                loigiai = ('''%s Gọi $A$ là tập hợp các bạn học sinh được xếp loại học lực Giỏi.\\\\
                         Gọi $B$ là tập hợp các bạn học sinh được xếp loại hạnh kiểm Tốt.\\\\
                         Theo giả thiết, ta có:\\\\
                         Số phần tử của tập hợp $A$ là $n\\left(A\\right) = %s$.\\\\
                         Số phần tử của tập hợp $B$ là $n\\left(B\\right) = %s$.\\\\
                         Số phần tử của tập hợp các bạn vừa Giỏi vừa có hạnh kiểm Tốt là $n\\left(A \\cap B\\right) = %s$.\\\\
                         Số học sinh được xếp loại học lực Giỏi hoặc hạnh kiểm Tốt chính là số phần tử của tập hợp $A \\cup B$.\\\\
                         Áp dụng công thức bao hàm - loại trừ, ta có:\\\\
                         $n\\left(A \\cup B\\right) = n\\left(A\\right) + n\\left(B\\right) - n\\left(A \\cap B\\right)$.\\\\
                         Thay số vào ta được: $n\\left(A \\cup B\\right) = %s + %s - %s = %s$.\\\\
                         Vậy lớp 10A có $%s$ bạn được xếp loại học lực Giỏi hoặc hạnh kiểm Tốt.'''
                         %(ve_hinh,latex(nA), latex(nB), latex(nAB), 
                           latex(nA), latex(nB), latex(nAB), latex(kq_val), 
                           latex(kq_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

