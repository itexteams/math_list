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


def bt_dang13_p3_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random một hệ số nguyên dương m để nhân vào hai vế nhằm tạo ra nhiều bài toán khác nhau.
                # Biểu thức gốc có k = 1, khi nhân thêm m vào vế trái thì giá trị k mới sẽ bằng m.
                m = randint(1, 6)
                k_val = m

                # Đáp án đúng
                da = '$%s$' % (latex(k_val))

                # Tạo các phương án nhiễu không trùng đáp án đúng
                s = []
                cac_phuong_an_nhieu = [0, 2*m, m+1, m-1, 2, 4, 3]
                for phan_tu in cac_phuong_an_nhieu:
                    val_sai = '$%s$' % (latex(phan_tu))
                    if val_sai != da and val_sai not in s:
                        s.append(val_sai)

                while len(s) < 3:
                    sai_rand = randint(1, 10)
                    if sai_rand != k_val:
                        val_sai = '$%s$' % (latex(sai_rand))
                        if val_sai not in s:
                            s.append(val_sai)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Thiết lập chuỗi hiển thị theo hệ số m
                if m == 1:
                    str_tu_so = '3 - 4\\cos 2a + \\cos 4a'
                    str_mau_so = '3 + 4\\cos 2a + \\cos 4a'

                    str_lg1 = '\\frac{2\\cos^2 2a - 4\\cos 2a + 2}{2\\cos^2 2a + 4\\cos 2a + 2}'
                    str_lg2 = '\\frac{2(\\cos^2 2a - 2\\cos 2a + 1)}{2(\\cos^2 2a + 2\\cos 2a + 1)}'
                    str_lg3 = '\\frac{(1 - \\cos 2a)^2}{(1 + \\cos 2a)^2}'
                    str_lg4 = '\\frac{[1 - (1 - 2\\sin^2 a)]^2}{[1 + (2\\cos^2 a - 1)]^2}'
                    str_lg5 = '\\frac{4\\sin^4 a}{4\\cos^4 a} = \\tan^4 a'
                else:
                    str_tu_so = '%s(3 - 4\\cos 2a + \\cos 4a)' % (latex(m))
                    str_mau_so = '3 + 4\\cos 2a + \\cos 4a'

                    str_lg1 = '%s \\cdot \\frac{2\\cos^2 2a - 4\\cos 2a + 2}{2\\cos^2 2a + 4\\cos 2a + 2}' % (latex(m))
                    str_lg2 = '%s \\cdot \\frac{2(\\cos^2 2a - 2\\cos 2a + 1)}{2(\\cos^2 2a + 2\\cos 2a + 1)}' % (latex(m))
                    str_lg3 = '%s \\cdot \\frac{(1 - \\cos 2a)^2}{(1 + \\cos 2a)^2}' % (latex(m))
                    str_lg4 = '%s \\cdot \\frac{[1 - (1 - 2\\sin^2 a)]^2}{[1 + (2\\cos^2 a - 1)]^2}' % (latex(m))
                    str_lg5 = '%s \\cdot \\frac{4\\sin^4 a}{4\\cos^4 a} = %s\\tan^4 a' % (latex(m), latex(m))

                # Câu hỏi
                noidungcauhoi = ('''Biết $\\frac{%s}{%s} = k \\tan^4 a$. Giá trị của $k$ bằng bao nhiêu?''' % (str_tu_so, str_mau_so))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước rõ ràng như ảnh mẫu
                loigiai = ('''Ta có: $\\frac{%s}{%s} = %s$ \\\\
                           $= %s$ \\\\
                           $= %s$ \\\\
                           $= %s$ \\\\
                           $= %s$. \\\\
                           Vậy $k = %s$.'''
                           % (str_tu_so, str_mau_so, str_lg1, str_lg2, str_lg3, str_lg4, str_lg5, latex(k_val)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(k_val))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

