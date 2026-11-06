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


def bt_dang36_p4_b1_c5_ds10(self):
            # Khai báo biến
            # Random số phần tử của tập A (từ 0 đến n). Để lập được số có 5 chữ số khác nhau, n ít nhất phải là 5.
            n = random.randint(6, 9)
            tap_A = list(range(n + 1))
            str_A = "{" + ",".join(map(str, tap_A)) + "}"

            # Tính toán lời giải
            # Gọi số cần lập là x = abcde (có gạch đầu)
            # Vì chia hết cho 5 nên e thuộc {0, 5}

            # Trường hợp 1: e = 0
            # e có 1 cách chọn.
            # a, b, c, d được chọn từ tập A \ {0}, tức là chọn 4 số từ n số còn lại và sắp xếp.
            # Số cách chọn a, b, c, d là: n * (n-1) * (n-2) * (n-3)
            c1_a = n
            c1_b = n - 1
            c1_c = n - 2
            c1_d = n - 3
            count1 = c1_a * c1_b * c1_c * c1_d

            # Trường hợp 2: e = 5
            # e có 1 cách chọn.
            # a khác 0 và a khác 5 nên a có (n-1) cách chọn.
            # b, c, d được chọn từ tập A \ {a, e}, tức là chọn 3 số từ (n+1 - 2) = n-1 số còn lại.
            # Số cách chọn b, c, d là: (n-1) * (n-2) * (n-3)
            c2_e = 1
            c2_a = n - 1
            c2_b = n - 1
            c2_c = n - 2
            c2_d = n - 3
            count2 = c2_a * c2_b * c2_c * c2_d

            # Tổng số các số thỏa mãn
            kq_dung = count1 + count2

            # B4: Điều chỉnh các phương án sai không được trùng với đáp án đúng
            s = set()
            while len(s) < 3:
                sai = kq_dung + random.choice([-50, -40, -30, -20, 20, 30, 40, 50, 100]) + random.randint(1, 10)
                if sai != kq_dung and sai > 0:
                    s.add(sai)

            list_sai = list(s)
            da_s1 = "$%s$" % list_sai[0]
            da_s2 = "$%s$" % list_sai[1]
            da_s3 = "$%s$" % list_sai[2]
            da_d = "\\True $%s$" % kq_dung

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # B2: Viết lại nội dung theo mẫu
            noidungcauhoi = ('''Cho tập $A = %s$. Từ tập $A$ tìm số các số tự nhiên gồm $5$ chữ số khác nhau và chia hết cho $5$.''' 
                             % (str_A))

            loigiai = ('''Gọi $x = \\overline{abcde}$ là số cần lập với $a, b, c, d, e$ đôi một khác nhau, $e \\in \\left\\{ 0,5 \\right\\}$ và $a \\neq 0$. \\\\
            Trường hợp 1: Với $e = 0 \\Rightarrow e$ có $1$ cách chọn. \\\\
            Cách chọn $4$ chữ số $a, b, c, d$ từ tập $A \\setminus \\left\\{ 0 \\right\\}$ là $A_{%s}^{4} = %s \\cdot %s \\cdot %s \\cdot %s = %s$. \\\\
            Trường hợp này có $%s$ số. \\\\
            Trường hợp 2: Với $e = 5 \\Rightarrow e$ có $1$ cách chọn. \\\\
            Vì $a \\neq 0$ và $a \\neq e$ nên $a$ có $%s$ cách chọn. \\\\
            Các chữ số $b, c, d$ được chọn từ $A \\setminus \\left\\{ a, e \\right\\}$ nên có $A_{%s}^{3} = %s \\cdot %s \\cdot %s = %s$ cách chọn. \\\\
            Trường hợp này có $1 \\cdot %s \\cdot %s = %s$ số. \\\\
            Vậy có $%s + %s = %s$ số thỏa mãn yêu cầu bài toán.'''
                       % (latex(n), latex(c1_a), latex(c1_b), latex(c1_c), latex(c1_d), latex(count1),
                          latex(count1),
                          latex(c2_a), latex(n-1), latex(c2_b), latex(c2_c), latex(c2_d), latex(c2_b * c2_c * c2_d),
                          latex(c2_a), latex(c2_b * c2_c * c2_d), latex(count2),
                          latex(count1), latex(count2), latex(kq_dung)
                         ))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

