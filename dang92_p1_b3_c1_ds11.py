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


def bt_dang92_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và tạo tính ngẫu nhiên cho bài toán
            lisdang = ['1', '2', '3', '4']
            dang = random.choice(lisdang)

            # Chọn ngẫu nhiên hàm gốc là sinx hoặc cosx
            ham_goc = random.choice(['\\cos x', '\\sin x'])

            if dang == '1':
                # Phép tịnh tiến sang phải: y = f(x - a)
                huong_dung = 'qua phải'
                b_thuc = 'x - \\frac{\\pi}{2}'
                loigiai_huong = 'sang phải 1 đoạn'

                da_text = 'Tịnh tiến $(C)$ qua phải một đoạn có độ dài là $\\frac{\\pi}{2}$'
                das1 = 'Tịnh tiến $(C)$ qua trái một đoạn có độ dài là $\\frac{\\pi}{2}$'
                das2 = 'Tịnh tiến $(C)$ lên trên một đoạn có độ dài là $\\frac{\\pi}{2}$'
                das3 = 'Tịnh tiến $(C)$ xuống dưới một đoạn có độ dài là $\\frac{\\pi}{2}$'

            elif dang == '2':
                # Phép tịnh tiến sang trái: y = f(x + a)
                huong_dung = 'qua trái'
                b_thuc = 'x + \\frac{\\pi}{2}'
                loigiai_huong = 'sang trái 1 đoạn'

                da_text = 'Tịnh tiến $(C)$ qua trái một đoạn có độ dài là $\\frac{\\pi}{2}$'
                das1 = 'Tịnh tiến $(C)$ qua phải một đoạn có độ dài là $\\frac{\\pi}{2}$'
                das2 = 'Tịnh tiến $(C)$ lên trên một đoạn có độ dài là $\\frac{\\pi}{2}$'
                das3 = 'Tịnh tiến $(C)$ xuống dưới một đoạn có độ dài là $\\frac{\\pi}{2}$'

            elif dang == '3':
                # Phép tịnh tiến lên trên: y = f(x) + a
                huong_dung = 'lên trên'
                # Điều chỉnh hiển thị cấu trúc biểu thức hàm số cho phù hợp với trường hợp tịnh tiến theo trục tung
                if ham_goc == '\\cos x':
                    b_thuc_full = '\\cos x + \\frac{\\pi}{2}'
                else:
                    b_thuc_full = '\\sin x + \\frac{\\pi}{2}'

                da_text = 'Tịnh tiến $(C)$ lên trên một đoạn có độ dài là $\\frac{\\pi}{2}$'
                das1 = 'Tịnh tiến $(C)$ xuống dưới một đoạn có độ dài là $\\frac{\\pi}{2}$'
                das2 = 'Tịnh tiến $(C)$ qua phải một đoạn có độ dài là $\\frac{\\pi}{2}$'
                das3 = 'Tịnh tiến $(C)$ qua trái một đoạn có độ dài là $\\frac{\\pi}{2}$'

            else:
                # Phép tịnh tiến xuống dưới: y = f(x) - a
                huong_dung = 'xuống dưới'
                if ham_goc == '\\cos x':
                    b_thuc_full = '\\cos x - \\frac{\\pi}{2}'
                else:
                    b_thuc_full = '\\sin x - \\frac{\\pi}{2}'

                da_text = 'Tịnh tiến $(C)$ xuống dưới một đoạn có độ dài là $\\frac{\\pi}{2}$'
                das1 = 'Tịnh tiến $(C)$ lên trên một đoạn có độ dài là $\\frac{\\pi}{2}$'
                das2 = 'Tịnh tiến $(C)$ qua phải một đoạn có độ dài là $\\frac{\\pi}{2}$'
                das3 = 'Tịnh tiến $(C)$ qua trái một đoạn có độ dài là $\\frac{\\pi}{2}$'

            # Định dạng chuỗi hiển thị biểu thức cho câu hỏi tùy theo dạng tịnh tiến
            if dang in ['1', '2']:
                if ham_goc == '\\cos x':
                    b_thuc_cauhoi = '\\cos \\left( %s \\right)' % b_thuc
                else:
                    b_thuc_cauhoi = '\\sin \\left( %s \\right)' % b_thuc
            else:
                b_thuc_cauhoi = b_thuc_full

            # Khởi tạo nội dung câu hỏi và lời giải sử dụng %s đúng cấu trúc format mẫu
            noidungcauhoi = ('''Đồ thị hàm số $y = %s$ được suy ra từ đồ thị $(C)$ của hàm số $y = %s$ bằng cách''' 
                             % (b_thuc_cauhoi, ham_goc))

            if dang in ['1', '2']:
                loigiai = ('''Đồ thị hàm số $y = %s$ được suy ra từ đồ thị $(C)$ của hàm số $y = %s$ bằng cách tịnh tiến %s có độ dài là $\\frac{\\pi}{2}$.''' 
                           % (b_thuc_cauhoi, ham_goc, loigiai_huong))
            else:
                loigiai = ('''Đồ thị hàm số $y = %s$ được suy ra từ đồ thị $(C)$ của hàm số $y = %s$ bằng cách tịnh tiến lên trên hoặc xuống dưới theo trục tung một đoạn có độ dài là $\\frac{\\pi}{2}$. Do đó phương án đúng là tịnh tiến %s.''' 
                           % (b_thuc_cauhoi, ham_goc, huong_dung))

            # Định dạng các phương án trắc nghiệm không chứa dấu chấm ở cuối
            da_d = ('\\True ' + str(da_text))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào danh sách và trộn ngẫu nhiên thứ tự
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm định dạng mẫu minipage
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

