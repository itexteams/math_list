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


def bt_dang30_p4_b1_c5_ds10(self):
            # Khai báo biến
            # để chữ số hàng nghìn 'a' luôn cố định là 1 (vì số nhỏ nhất bắt đầu bằng 2 là 2134).

            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các giá trị
                n_limit = random.choice([2011, 2013, 2015, 2017])
                digits_set = '\\left\\{ 1, 2, 3, \\dots, 9 \\right\\}'

                # Tính toán kết quả
                # Bước 1: Chọn d chẵn từ {2, 4, 6, 8} -> 4 cách
                so_cach_d = 4
                # Bước 2: Chọn a = 1 -> 1 cách
                so_cach_a = 1
                # Bước 3: Chọn b, c từ 7 chữ số còn lại (9 chữ số - a - d)
                # Số cách chọn b, c là chỉnh hợp chập 2 của 7: 7 * 6
                so_cach_bc = 7 * 6

                kq_count = so_cach_a * so_cach_d * so_cach_bc

                # B4-Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                kq = kq_count
                du = ['$%s$' % (latex(kq))]
                da = random.choice(du)

                # Tạo danh sách các phương án nhiễu
                s_list = [kq + 2, kq + 4, kq + 6, kq - 4, kq - 2, kq + 10]
                random.shuffle(s_list)

                das1 = '$%s$' % (latex(s_list[0]))
                das2 = '$%s$' % (latex(s_list[1]))
                das3 = '$%s$' % (latex(s_list[2]))

                # Câu hỏi
                noidungcauhoi = ('''Cho các chữ số $%s$. Từ các chữ số đó hãy tìm số các số chẵn gồm $4$ chữ số khác nhau và không vượt quá $%s$.'''
                                 % (digits_set, latex(n_limit)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (B2)
                loigiai = ('''Gọi số cần lập là $x = \\overline{abcd}$ với $a, b, c, d \\in \\left\\{ 1, 2, 3, 4, 5, 6, 7, 8, 9 \\right\\}$ và các chữ số đôi một khác nhau. \\\\
            Vì $x$ là số chẵn nên $d \\in \\left\\{ 2, 4, 6, 8 \\right\\}$. \\\\
            Đồng thời $x \\le %s$. Vì các chữ số thuộc tập từ $1$ đến $9$ nên số nhỏ nhất có $4$ chữ số khác nhau bắt đầu bằng chữ số $2$ là $2134$. \\\\
            Do $2134 > %s$ nên chữ số hàng nghìn $a$ chỉ có thể chọn là $1$. \\\\
            + Với $a = 1$: Chữ số $a$ có $1$ cách chọn. \\\\
            + Khi đó, chữ số $d$ có $4$ cách chọn (từ tập $\\left\\{ 2, 4, 6, 8 \\right\\}$). \\\\
            + Sau khi chọn $a$ và $d$, ta còn $9 - 2 = 7$ chữ số để chọn cho $b$ và $c$. \\\\
            Số cách chọn và sắp xếp hai chữ số $b, c$ là $A_7^2 = 7 \\cdot 6 = 42$ cách. \\\\
            Suy ra có tất cả: $1 \\cdot 4 \\cdot 7 \\cdot 6 = %s$ số.'''
                           % (latex(n_limit), latex(n_limit), latex(kq_count)))

            # Xuất câu trắc nghiệm (Không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

