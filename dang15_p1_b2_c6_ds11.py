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


def bt_dang15_p1_b2_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (Dạng 1: Xác suất lấy bi cùng màu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hóa xác suất cho hộp 1 (mẫu số thường là 4, 5, 10 để ra số thập phân đẹp)
                mau1 = random.choice([4, 5, 10])
                tu1 = random.randint(1, mau1 - 1)
                p_a1 = Rational(tu1, mau1) # Xác suất bi Đỏ hộp 1
                p_b1 = 1 - p_a1             # Xác suất bi Xanh hộp 1

                # Random hóa xác suất cho hộp 2 (mẫu số thường là 8, 10)
                mau2 = random.choice([8, 10])
                tu2 = random.randint(1, mau2 - 1)
                p_a2 = Rational(tu2, mau2) # Xác suất bi Đỏ hộp 2
                p_b2 = 1 - p_a2             # Xác suất bi Xanh hộp 2

                # Tính toán kết quả: P = P(A1)*P(A2) + P(B1)*P(B2)
                kq_rational = p_a1 * p_a2 + p_b1 * p_b2

                # Chuyển đổi sang định dạng chuỗi thập phân cho đề bài (dùng dấu phẩy)
                p_a1_str = str(float(p_a1)).replace('.', ',')
                p_b1_str = str(float(p_b1)).replace('.', ',')
                p_a2_str = str(float(p_a2)).replace('.', ',')
                p_b2_str = str(float(p_b2)).replace('.', ',')

                # Đáp án đúng (để dưới dạng phân số tối giản như trong ảnh)
                da = '$%s$' % (latex(kq_rational))

                # Tạo các phương án sai
                s = []
                # Sai lầm 1: Chỉ tính trường hợp cùng màu đỏ
                sai1 = p_a1 * p_a2
                # Sai lầm 2: Chỉ tính trường hợp cùng màu xanh
                sai2 = p_b1 * p_b2
                # Sai lầm 3: Tính trường hợp khác màu
                sai3 = p_a1 * p_b2 + p_a2 * p_b1

                list_sai_raw = [sai1, sai2, sai3]
                for itemsai in list_sai_raw:
                    if itemsai != kq_rational:
                        s.append('$%s$' % (latex(itemsai)))

                # Bổ sung nếu trùng hoặc thiếu
                while len(s) < 3:
                    temp_tu = random.randint(1, 15)
                    temp_mau = random.choice([16, 32, 40])
                    temp_kq = Rational(temp_tu, temp_mau)
                    if temp_kq != kq_rational:
                        s.append('$%s$' % (latex(temp_kq)))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Có 2 hộp đựng bi, lấy mỗi hộp 1 viên bi. Biết ở hộp thứ nhất, xác suất lấy 1 viên bi màu đỏ là $%s$, xác suất lấy được 1 viên bi màu xanh là $%s$. Ở hộp thứ hai, xác suất lấy 1 viên bi màu đỏ là $%s$, xác suất lấy được 1 viên bi màu xanh là $%s$. Xác suất lấy được hai viên bi cùng màu là'''
                                 % (p_a1_str, p_b1_str, p_a2_str, p_b2_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Gọi $A_1$ là biến cố lấy được 1 viên bi màu đỏ ở hộp 1. Ta có $P\\left(A_1\\right)=%s$. \\\\
                            Gọi $B_1$ là biến cố lấy được 1 viên bi màu xanh ở hộp 1. Ta có $P\\left(B_1\\right)=%s$. \\\\
                            Gọi $A_2$ là biến cố lấy được 1 viên bi màu đỏ ở hộp 2. Ta có $P\\left(A_2\\right)=%s$. \\\\
                            Gọi $B_2$ là biến cố lấy được 1 viên bi màu xanh ở hộp 2. Ta có $P\\left(B_2\\right)=%s$. \\\\
                            Vậy xác suất của biến cố lấy được 2 viên bi cùng màu là \\\\
                            $P\\left(A_1A_2 \\cup B_1B_2\\right) = P\\left(A_1\\right).P\\left(A_2\\right) + P\\left(B_1\\right)P\\left(B_2\\right) = %s.%s + %s.%s = %s$.'''
                           % (p_a1_str, p_b1_str, p_a2_str, p_b2_str, 
                              p_a1_str, p_a2_str, p_b1_str, p_b2_str, latex(kq_rational)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

