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


def bt_dang52_p4_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random kiểu hàm số để tạo nhiều câu hỏi khác nhau:
                # k = 1 tương ứng với y = sin x - cos x (giống ảnh gốc)
                # k = 2 tương ứng với y = sin x + cos x (biến thể ngẫu nhiên)
                k = random.choice([1, 2])

                if k == 1:
                    ham_goc = 'y = \\sin x - \\cos x'
                    ham_bien_doi = 'y = \\sin x - \\cos x = \\sqrt{2}\\sin\\left( x - \\frac{\\pi}{4} \\right)'
                    doan_xet = '\\left[ -\\frac{\\pi}{4}; \\frac{7\\pi}{4} \\right]'
                    khoang_db = '$\\left( -\\frac{\\pi}{4}; \\frac{3\\pi}{4} \\right)$'
                    khoang_nb = '$\\left( \\frac{3\\pi}{4}; \\frac{7\\pi}{4} \\right)$'
                    khoang_sai_luon_nb = '$\\left( -\\frac{\\pi}{4}; \\frac{7\\pi}{4} \\right)$'

                    # Phương án đúng là A
                    pa_A = 'Hàm số đã cho đồng biến trên khoảng %s' % (khoang_db)
                    pa_B = 'Hàm số đã cho đồng biến trên khoảng %s' % (khoang_nb)
                    pa_C = 'Hàm số đã cho có tập giá trị là $[-1; 1]$'
                    pa_D = 'Hàm số đã cho luôn nghịch biến trên khoảng %s' % (khoang_sai_luon_nb)

                else:
                    ham_goc = 'y = \\sin x + \\cos x'
                    ham_bien_doi = 'y = \\sin x + \\cos x = \\sqrt{2}\\sin\\left( x + \\frac{\\pi}{4} \\right)'
                    doan_xet = '\\left[ -\\frac{3\\pi}{4}; \\frac{5\\pi}{4} \\right]'
                    khoang_db = '$\\left( -\\frac{3\\pi}{4}; \\frac{\\pi}{4} \\right)$'
                    khoang_nb = '$\\left( \\frac{\\pi}{4}; \\frac{5\\pi}{4} \\right)$'
                    khoang_sai_luon_nb = '$\\left( -\\frac{3\\pi}{4}; \\frac{5\\pi}{4} \\right)$'

                    # Phương án đúng là A
                    pa_A = 'Hàm số đã cho đồng biến trên khoảng %s' % (khoang_db)
                    pa_B = 'Hàm số đã cho đồng biến trên khoảng %s' % (khoang_nb)
                    pa_C = 'Hàm số đã cho có tập giá trị là $[-1; 1]$'
                    pa_D = 'Hàm số đã cho luôn nghịch biến trên khoảng %s' % (khoang_sai_luon_nb)

                # Câu hỏi sử dụng %s đúng cấu trúc mẫu
                noidungcauhoi = ('''Xét sự biến thiên của hàm số $%s$.''' % (str(ham_goc)))

                # Định dạng các phương án trả lời trắc nghiệm (không chứa dấu chấm ở cuối)
                da_d = ('\\True ' + str(pa_A) )
                da_s1 =   str(pa_B) 
                da_s2 =   str(pa_C) 
                da_s3 =   str(pa_D) 

                # Đưa các đáp án vào một danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo từng bước như ảnh gốc, sử dụng %s
                loigiai = ('''Ta có $%s$. \\\\
                           Từ đây ta có thể loại đáp án C, do tập giá trị của hàm số là $[-\\sqrt{2}; \\sqrt{2}]$. \\\\
                           Hàm số đã cho tuần hoàn với chu kỳ $2\\pi$ do vậy ta xét sự biến thiên của hàm số trên đoạn $%s$. \\\\
                           Ta có: \\\\
                           Hàm số đồng biến trên khoảng $%s$. \\\\
                           Hàm số nghịch biến trên khoảng $%s$.'''
                           % (str(ham_bien_doi), str(doan_xet), str(khoang_db), str(khoang_nb)))

            # Xuất câu trắc nghiệm đúng định dạng mẫu của hệ thống
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content



