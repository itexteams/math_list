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


def bt_dang44_p1_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo các thông số random cho cấp số nhân
                # m là nghịch đảo của công bội q (ví dụ m=3 thì q=1/3)
                m = random.randint(2, 5)
                q = Rational(1, m)

                # u1 là số hạng đầu
                u1 = random.randint(2, 15)

                # Chỉ số của các số hạng để tạo tỷ số ux / uy
                x_idx = random.randint(2, 4)
                diff = random.choice([3, 5]) # khoảng cách chỉ số (y - x), chọn số lẻ để duy trì dấu của q
                y_idx = x_idx + diff

                # Tỷ số k = ux / uy = 1 / (q^diff) = m^diff
                k = m**diff

                # Chỉ số z của số hạng cần tìm
                z = random.randint(y_idx + 1, y_idx + 3)

                # Tính toán đáp án đúng
                kq = u1 * (q**(z-1))

                # Tạo các đáp án nhiễu (sai)
                # Sai lầm 1: Nhầm công bội thành m thay vì 1/m
                kq_s1 = u1 * (m**(z-1))
                # Sai lầm 2: Quên trừ 1 ở số mũ (u_n = u1 * q^n)
                kq_s2 = u1 * (q**z)
                # Sai lầm 3: Nhầm công bội thành m và quên trừ 1
                kq_s3 = u1 * (m**z)

                # Các đáp án trắc nghiệm (đưa về chuỗi LaTeX)
                da = 'u_{%s} = %s' % (z, latex(kq))
                das1 = 'u_{%s} = %s' % (z, latex(kq_s1))
                das2 = 'u_{%s} = %s' % (z, latex(kq_s2))
                das3 = 'u_{%s} = %s' % (z, latex(kq_s3))

                # Câu hỏi
                noidungcauhoi = ('''Cho cấp số nhân $(u_n)$, biết $u_1 = %s$, $\\frac{u_{%s}}{u_{%s}} = %s$. Số hạng $u_{%s}$ là'''
                                 % (latex(u1), latex(x_idx), latex(y_idx), latex(k), latex(z)))

                # Các phương án
                da_d = ('\\True $%s$' % str(da))
                da_s1 = ('$%s$' % str(das1))
                da_s2 = ('$%s$' % str(das2)) 
                da_s3 = ('$%s$' % str(das3)) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $q$ là công bội của cấp số nhân $(u_n)$.\\\\
                            Ta có $\\frac{u_{%s}}{u_{%s}} = \\frac{u_1 \\cdot q^{%s}}{u_1 \\cdot q^{%s}} = \\frac{1}{q^{%s}}$.\\\\
                            Theo giả thiết, $\\frac{1}{q^{%s}} = %s \\Rightarrow q^{%s} = \\frac{1}{%s} \\Rightarrow q = %s$.\\\\
                            Vậy số hạng $u_{%s} = u_1 \\cdot q^{%s} = %s \\cdot \\left(%s\\right)^{%s} = %s$.'''
                         % (latex(x_idx), latex(y_idx), latex(x_idx-1), latex(y_idx-1), latex(diff),
                            latex(diff), latex(k), latex(diff), latex(k), latex(q),
                            latex(z), latex(z-1), latex(u1), latex(q), latex(z-1), latex(kq)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

