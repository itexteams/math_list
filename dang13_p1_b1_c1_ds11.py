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


def bt_dang13_p1_b1_c1_ds11(self):
            # Khai báo biến

            lis=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
            dang=random.choice(lis)
            if dang=='16':
                goc1=randint(271,359)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '\\True $\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha =\\cot \\left( %s \\right) =\\cot \\left(%s+%s \\right) =\\cot %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $\\dfrac{3\\pi}{2} <%s<2\\pi$  (góc phần tư thứ tư) nên $\\cot %s <0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha <0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='15':
                goc1=randint(271,359)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '\\True $\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha =\\tan \\left( %s \\right) =\\tan \\left(%s+%s \\right) =\\tan %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $\\dfrac{3\\pi}{2} <%s<2\\pi$  (góc phần tư thứ tư) nên $\\tan %s <0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha <0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='14':
                goc1=randint(271,359)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '\\True $\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha =\\cos \\left( %s \\right) =\\cos \\left(%s+%s \\right) =\\cos %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $\\dfrac{3\\pi}{2} <%s<2\\pi$  (góc phần tư thứ tư) nên $\\cos %s >0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha <0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='13':
                goc1=randint(271,359)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '\\True $\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha =\\sin \\left( %s \\right) =\\sin \\left(%s+%s \\right) =\\sin %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $\\dfrac{3\\pi}{2} <%s<2\\pi$  (góc phần tư thứ tư) nên $\\sin %s <0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha <0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='12':
                goc1=randint(181,269)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '\\True $\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha =\\cot \\left( %s \\right) =\\cot \\left(%s+%s \\right) =\\cot %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $\\pi <%s<\\dfrac{3\\pi}{2}$  (góc phần tư thứ ba) nên $\\cot %s >0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha >0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='11':
                goc1=randint(181,269)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '\\True $\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha =\\tan \\left( %s \\right) =\\tan \\left(%s+%s \\right) =\\tan %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $\\pi <%s<\\dfrac{3\\pi}{2}$  (góc phần tư thứ ba) nên $\\tan %s >0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha >0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='10':
                goc1=randint(181,269)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '\\True $\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha =\\cos \\left( %s \\right) =\\cos \\left(%s+%s \\right) =\\cos %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $\\pi <%s<\\dfrac{3\\pi}{2}$  (góc phần tư thứ ba) nên $\\cos %s <0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha >0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='9':
                goc1=randint(181,269)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '\\True $\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha =\\sin \\left( %s \\right) =\\sin \\left(%s+%s \\right) =\\sin %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $\\pi <%s<\\dfrac{3\\pi}{2}$  (góc phần tư thứ ba) nên $\\sin %s <0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha >0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='8':
                goc1=randint(91,197)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '\\True $\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha =\\cot \\left( %s \\right) =\\cot \\left(%s+%s \\right) =\\cot %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $\\dfrac{\\pi}{2} < %s < \\pi $ (góc phần tư thứ hai) nên $\\cot %s <0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha <0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='7':
                goc1=randint(91,197)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '\\True $\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha =\\tan \\left( %s \\right) =\\tan \\left(%s+%s \\right) =\\tan %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $\\dfrac{\\pi}{2} < %s < \\pi $ (góc phần tư thứ hai) nên $\\tan %s <0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha <0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='6':
                goc1=randint(91,197)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '\\True $\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha =\\cos \\left( %s \\right) =\\cos \\left(%s+%s \\right) =\\cos %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $\\dfrac{\\pi}{2} < %s < \\pi $ (góc phần tư thứ hai) nên $\\cos %s <0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha <0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='5':
                goc1=randint(91,197)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '\\True $\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha =\\sin \\left( %s \\right) =\\sin \\left(%s+%s \\right) =\\sin %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $\\dfrac{\\pi}{2} < %s < \\pi $ (góc phần tư thứ hai) nên $\\sin %s >0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha <0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha <0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='4':
                goc1=randint(1,89)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '\\True $\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha =\\cot \\left( %s \\right) =\\cot \\left(%s+%s \\right) =\\cot %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $0<%s<\\dfrac{\\pi}{2}$ (góc phần tư thứ nhất) nên $\\cot %s >0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha >0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='3':
                goc1=randint(1,89)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '\\True $\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha =\\tan \\left( %s \\right) =\\tan \\left(%s+%s \\right) =\\tan %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $0<%s<\\dfrac{\\pi}{2}$  (góc phần tư thứ nhất) nên $\\tan %s >0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha >0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='2':
                goc1=randint(1,89)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '\\True $\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha =\\cos \\left( %s \\right) =\\cos \\left(%s+%s \\right) =\\cos %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $0<%s<\\dfrac{\\pi}{2}$  (góc phần tư thứ nhất) nên $\\cos %s >0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha >0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )
            if dang=='1':
                goc1=randint(1,89)
                goc1_rad=goc1*pi/180
                k=randint(-20,20)
                while k==0:
                    k=randint(-20,20)
                goc2=k*360
                goc2_rad=k*2*pi
                goc=goc1+goc2
                goc_rad=goc*pi/180
                # Câu hỏi
                noidungcauhoi=('''Cho góc $\\alpha =%s$. Khẳng định nào sau đây là đúng? \n'''
                            %(latex(goc_rad))
                            )
                # Các đáp án
                da_d = '\\True $\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có. \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\alpha =\\sin \\left( %s \\right) =\\sin \\left(%s+%s \\right) =\\sin %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $0<%s<\\dfrac{\\pi}{2}$  (góc phần tư thứ nhất) nên $\\sin %s >0$. \\\\ \n'
                        'Tương tự ta có \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\alpha >0$. \\\\ \n'
                        '\\hspace*{1cm} $\\cot \\alpha >0$. '
                        %(latex(goc_rad),latex(goc1_rad),latex(goc2_rad),latex(goc1_rad),
                        latex(goc1_rad), latex(goc1_rad),
                            )
                        )


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')
            return content

