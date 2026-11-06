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


def bt_dang45_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thực hiện random các số trong bài toán để tạo nhiều câu hỏi khác nhau nhưng giữ nguyên cấu trúc logic
                # Hàm A: y = sin(pi/k1 - 2x) có chu kỳ T = 2pi/|-2| = pi
                k1 = random.choice([3, 4, 6])

                # Hàm B: y = cos 2(x + pi/k2) = cos(2x + 2pi/k2) có chu kỳ T = 2pi/2 = pi
                k2 = random.choice([3, 4, 6])
                p2 = Rational(2, k2) # Hệ số pha sau khi nhân phân phối 2*pi/k2

                # Hàm C (Đáp án đúng): y = tan(-m*x + c) có chu kỳ T = pi/|-m| khác pi (m chọn ngẫu nhiên khác 1 và 2)
                m = random.choice([3, 4, 5])
                c = randint(1, 5)

                # Hàm D: y = cos x sin x = 1/2 sin 2x có chu kỳ T = 2pi/2 = pi (giữ nguyên cấu trúc lượng giác cố định)

                # Chuỗi latex cho các hàm số
                fA = 'y = \\sin \\left( \\frac{\\pi}{%s} - 2x \\right)' % (latex(k1))
                fB = 'y = \\cos 2 \\left( x + \\frac{\\pi}{%s} \\right)' % (latex(k2))
                fC = 'y = \\tan (-%sx + %s)' % (latex(m), latex(c))
                fD = 'y = \\cos x \\sin x'

                # Các đáp án trắc nghiệm (Đáp án đúng là hàm C vì có chu kỳ pi/m khác pi)
                du = ['$%s$' % (fC)]
                da = random.choice(du)

                # Phương án sai là các hàm có chu kỳ bằng pi
                das1 = '$%s$' % (fA)
                das2 = '$%s$' % (fB)
                das3 = '$%s$' % (fD)

                # Câu hỏi
                noidungcauhoi = ('''Hàm số nào sau đây có chu kì khác $\\pi$?''')

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải đầy đủ, chi tiết từng bước như trong ảnh mẫu ban đầu
                loigiai = ('''Xét: Hàm số $%s$ tuần hoàn với chu kì $T = \\frac{2\\pi}{|-2|} = \\pi$. \\\\
                           Xét: Hàm số $%s = \\cos \\left( 2x + \\frac{%s\\pi}{%s} \\right)$ tuần hoàn với chu kì $T = \\frac{2\\pi}{|2|} = \\pi$. \\\\
                           Xét: Hàm số $%s$ tuần hoàn với chu kì $T = \\frac{\\pi}{|-%s|} = \\frac{\\pi}{%s} \\Rightarrow \\text{chọn}$. \\\\
                           Xét: Hàm số $%s = \\frac{1}{2}\\sin 2x$ tuần hoàn với chu kì $T = \\frac{2\\pi}{|2|} = \\pi$.'''
                           % (fA, fB, latex(p2.p), latex(p2.q), fC, latex(m), latex(m), fD))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

