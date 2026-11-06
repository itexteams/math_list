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


def bt_dang51_p4_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số n của hàm số y = tan(nx). Ví dụ n = 2, 3, 4
                # Với n = 2, bài toán sẽ trùng khớp hoàn toàn với dữ liệu mẫu trong ảnh
                n = random.choice([2, 3, 4])

                # Tính toán các giá trị lượng giác phụ thuộc vào n
                # Chu kỳ T = pi/n
                # Điểm gián đoạn đầu tiên trong khoảng (0; pi/n) là pi/(2n)
                goc_str = '%sx' % (latex(n)) if n > 1 else 'x'

                val_pi_n = '\\frac{\\pi}{%s}' % (latex(n))
                val_pi_2n = '\\frac{\\pi}{%s}' % (latex(2*n))

                # Định dạng các khoảng biến thiên cho phương án và lời giải
                khoang_1 = '\\left( 0; %s \\right)' % (val_pi_2n)
                khoang_2 = '\\left( %s; %s \\right)' % (val_pi_2n, val_pi_n)
                khoang_tong = '\\left( 0; %s \\right)' % (val_pi_n)
                tap_bo = '\\left\\{ %s \\right\\}' % (val_pi_2n)

                # Câu hỏi
                noidungcauhoi = ('''Xét sự biến thiên của hàm số $y = \\tan %s$ trên một chu kì tuần hoàn.''' % (str(goc_str)))

                # Định dạng các phương án trả lời (Không chứa dấu chấm ở cuối phương án)
                da_d = ('\\True Hàm số đã cho đồng biến trên khoảng $%s$ và $%s$' % (str(khoang_1), str(khoang_2)))
                da_s1 = ('Hàm số đã cho đồng biến trên khoảng $%s$ và nghịch biến trên khoảng $%s$' % (str(khoang_1), str(khoang_2)))
                da_s2 = ('Hàm số đã cho luôn đồng biến trên khoảng $%s$' % (str(khoang_tong)))
                da_s3 = ('Hàm số đã cho nghịch biến trên khoảng $%s$ và đồng biến trên khoảng $%s$' % (str(khoang_1), str(khoang_2)))

                # Đưa các đáp án vào một danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết đầy đủ từng bước sử dụng định dạng %s
                loigiai = ('''Tập xác định của hàm số đã cho là $D = \\mathbb{R} \\setminus \\left\\{ %s + k%s \\mid k \\in \\mathbb{Z} \\right\\}$. \\\\
                           Hàm số $y = \\tan %s$ tuần hoàn với chu kì $%s$, dựa vào các phương án A; B; C; D thì ta sẽ xét tính đơn điệu của hàm số trên $%s \\setminus %s$. \\\\
                           Dựa theo kết quả khảo sát sự biến thiên của hàm số $y = \\tan x$ ở phần lý thuyết ta có thể suy ra với hàm số $y = \\tan %s$ đồng biến trên khoảng $%s$ và $%s$.'''
                           % (str(val_pi_2n), str(val_pi_n), str(goc_str), str(val_pi_n), str(khoang_tong), str(tap_bo), str(goc_str), str(khoang_1), str(khoang_2)))

            # Xuất câu trắc nghiệm theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content




