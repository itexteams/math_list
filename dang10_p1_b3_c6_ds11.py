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


def bt_dang10_p1_b3_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random bài toán
                # Chọn xác suất trúng của người thứ nhất p1 (từ 60% đến 95%)
                p1 = randint(12, 19) * 5
                # Chọn xác suất trúng của người thứ hai p2 (từ 50% đến 90%)
                p2 = randint(10, 18) * 5

                # Tính kết quả đúng
                kq_val = (p1 * p2) / 100

                # Hàm định dạng số: thay dấu . bằng ,
                def format_vn(val):
                    return str(val).replace('.', ',')

                # Đáp án đúng
                da_dung = format_vn(kq_val) + '\\%'

                # Bước 4: Tạo phương án sai không trùng phương án đúng
                s_list = []
                # Sai lầm 1: Tính xác suất ít nhất 1 người trúng
                w1 = p1 + p2 - (p1 * p2 / 100)
                # Sai lầm 2: Tính xác suất cả hai cùng trượt
                w2 = (100 - p1) * (100 - p2) / 100
                # Sai lầm 3: Tổng xác suất (nếu nhỏ hơn 100)
                w3 = float(p1 + p2)
                # Sai lầm 4: Trung bình cộng
                w4 = (p1 + p2) / 2

                potential_wrongs = [w1, w2, w3, w4]
                for val in potential_wrongs:
                    if val > 0 and val < 100:
                        formatted = format_vn(val) + '\\%'
                        if formatted != da_dung and formatted not in s_list:
                            s_list.append(formatted)

                # Bổ sung nếu chưa đủ 3 đáp án sai
                offset = 5
                while len(s_list) < 3:
                    fake = format_vn(abs(kq_val + offset)) + '\\%'
                    if fake != da_dung and fake not in s_list:
                        s_list.append(fake)
                    offset += 5

                random.shuffle(s_list)
                das1, das2, das3 = s_list[0], s_list[1], s_list[2]

                # Câu hỏi (Dùng \%% để Python hiểu là ký tự % và không bị lỗi format)
                noidungcauhoi = ('''Hai xạ thủ cùng bắn vào bia. Xác suất người thứ nhất bắn trúng là $%s\\%%$. Xác suất người thứ hai bắn trúng là $%s\\%%$. Xác suất để cả hai người cùng bắn trúng là'''
                                 %(latex(p1), latex(p2)))

                # Các đáp án
                da_d = ('\\True $' + str(da_dung))+'$'
                da_s1 = '$'+str(das1)+'$'
                da_s2 = '$'+str(das2) +'$'
                da_s3 = '$'+str(das3) +'$'

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Sử dụng \left( \right) và chi tiết như trong ảnh)
                loigiai = ('''Gọi $A_i$ là biến cố người thứ $i$ bắn trúng $\\left( i = \\overline{1,2} \\right)$.\\\\
                             Vì $A_1, A_2$ là độc lập nên xác suất để hai người bắn trúng là:\\\\
                             $P\\left( A_1 A_2 \\right) = P\\left( A_1 \\right) P\\left( A_2 \\right) = %s\\%% \\cdot %s\\%% = %s\\%%$.'''
                           %(latex(p1), latex(p2), format_vn(kq_val)))

            # Xuất câu trắc nghiệm theo đúng cấu trúc yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

