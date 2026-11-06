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


def bt_dang29_p3_b1_c5_ds10(self):
            # Khai báo biến
            # Bước 1: Nghiên cứu và Bước 3: Random bài toán
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random tập hợp chữ số từ {0, 1, ..., n}
                # Trong ảnh là n=5, ta có thể cho n chạy từ 5 đến 7
                n_max = random.randint(5, 7)
                tap_hop = list(range(n_max + 1))
                chu_so_str = ", ".join(map(str, tap_hop))

                # Số các chữ số lẻ trong tập hợp
                le = [x for x in tap_hop if x % 2 != 0]
                so_cach_d = len(le)

                # Số lượng chữ số của số cần lập (trong ảnh là 4)
                k = 4

                # Tính toán số cách chọn theo logic bài toán
                # Gọi số là abcd
                # 1. Chọn d (số lẻ): so_cach_d cách
                # 2. Chọn a (a khác 0 và a khác d): tổng số - 2 (loại 0 và d)
                so_cach_a = len(tap_hop) - 2

                # 3. Chọn b (b khác a, d): tổng số - 2
                so_cach_b = len(tap_hop) - 2

                # 4. Chọn c (c khác a, b, d): tổng số - 3
                so_cach_c = len(tap_hop) - 3

                kq_num = so_cach_d * so_cach_a * so_cach_b * so_cach_c
                kq = str(kq_num)

                # Bước 4: Điều chỉnh phương án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = kq_num + random.choice([-10, -5, 1, 2, 5, 10, 11])
                    if sai != kq_num and sai > 0:
                        s.add(str(sai))

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Từ các chữ số $%s$ có thể lập được bao nhiêu số lẻ gồm $%s$ chữ số khác nhau?'''
                                 %(chu_so_str, latex(k)))

                # Nội dung lời giải chi tiết (không viết tắt, đúng định dạng yêu cầu)
                loigiai = ('''Gọi số cần tìm có dạng $\\overline{abcd}$ với $\\left(a, b, c, d\\right) \\in A = \\left\\{%s\\right\\}$. \\\\
            Vì $\\overline{abcd}$ là số lẻ nên $d \\in \\left\\{%s\\right\\}$, suy ra $d$ có $%s$ cách chọn. \\\\
            Khi đó: \\\\
            - Chữ số $a$ có $%s$ cách chọn (vì $a \\neq 0$ và $a \\neq d$). \\\\
            - Chữ số $b$ có $%s$ cách chọn (vì $b \\neq a$ và $b \\neq d$). \\\\
            - Chữ số $c$ có $%s$ cách chọn (vì $c \\neq a, b, d$). \\\\
            Vậy có tất cả $%s \\times %s \\times %s \\times %s = %s$ số cần tìm.'''
                           %(chu_so_str, ", ".join(map(str, le)), latex(so_cach_d), 
                             latex(so_cach_a), latex(so_cach_b), latex(so_cach_c),
                             latex(so_cach_d), latex(so_cach_a), latex(so_cach_b), latex(so_cach_c), latex(kq_num)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))

                # Các đáp án
                da_d = ('\\True ' + str(kq))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm (Không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

