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


def bt_dang12_p4_b2_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số lượng học sinh nam và nữ (n nam, n nữ)
                # Để bài toán hay, ta chọn n trong khoảng từ 2 đến 3 (như ảnh là n=3)
                n = random.randint(2, 4)
                tong_hs = 2 * n

                # Tính toán không gian mẫu
                omega = math.factorial(tong_hs)

                # Biến cố A: Các bạn nữ đứng cạnh nhau
                # Coi n bạn nữ là 1 nhóm, kết hợp với n bạn nam => có n + 1 thực thể
                # Số cách xếp: (n + 1)! * n!
                na = math.factorial(n + 1) * math.factorial(n)
                pa = Rational(na, omega)

                # Biến cố B: Nam nữ đứng xen kẽ nhau
                # Có 2 trường hợp: Nam đứng đầu hoặc Nữ đứng đầu
                # Số cách xếp: 2 * (n! * n!)
                nb = 2 * (math.factorial(n) * math.factorial(n))
                pb = Rational(nb, omega)

                # Biến cố C: A hợp B (do A và B xung khắc vì n >= 2)
                pc = pa + pb

                # Đáp án đúng
                da = '$%s$' % (latex(pc))

                # Tạo các đáp án nhiễu
                s = [
                    '$%s$' % (latex(pa)), # Chỉ tính A
                    '$%s$' % (latex(pb)), # Chỉ tính B
                    '$%s$' % (latex(Rational(1, 2))),
                    '$%s$' % (latex(Rational(2, 5))),
                    '$%s$' % (latex(Rational(1, 10))),
                    '$%s$' % (latex(1 - pc)) # Biến cố đối
                ]

                # Loại bỏ đáp án đúng khỏi danh sách nhiễu nếu lỡ trùng
                s = [item for item in s if item != da]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Có $%s$ học sinh gồm $%s$ nam và $%s$ nữ xếp thành hàng ngang để chụp ảnh. Tính xác suất để các bạn nữ đứng cạnh nhau hoặc nam nữ đứng xen kẽ nhau.'''
                                 % (latex(tong_hs), latex(n), latex(n)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo mẫu ảnh
                loigiai = ('''Không gian mẫu $n\\left(\\Omega\\right) = %s! = %s$. \\\\
                           Gọi biến cố $A$: "các bạn nữ đứng cạnh nhau" $\\Rightarrow n\\left(A\\right) = %s! \\cdot %s! = %s$. \\\\
                           $P\\left(A\\right) = \\frac{n\\left(A\\right)}{n\\left(\\Omega\\right)} = \\frac{%s}{%s} = %s$. \\\\
                           Gọi biến cố $B$: "nam nữ đứng xen kẽ" $\\Rightarrow n\\left(B\\right) = 2 \\cdot %s! \\cdot %s! = %s$. \\\\
                           $P\\left(B\\right) = \\frac{n\\left(B\\right)}{n\\left(\\Omega\\right)} = \\frac{%s}{%s} = %s$. \\\\
                           Gọi $C$ là biến cố "các bạn nữ đứng cạnh nhau hoặc nam nữ đứng xen kẽ". Suy ra $C = A \\cup B$. \\\\
                           Do $A, B$ xung khắc nên $P\\left(C\\right) = P\\left(A\\right) + P\\left(B\\right) = %s + %s = %s$.'''

                           % (latex(tong_hs), latex(omega),
                              latex(n + 1), latex(n), latex(na),
                              latex(na), latex(omega), latex(pa),
                              latex(n), latex(n), latex(nb),
                              latex(nb), latex(omega), latex(pb),
                              latex(pa), latex(pb), latex(pc)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

