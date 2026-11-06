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


def bt_dang45_p4_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random mẫu số m của góc x/m (Bài gốc m = 2)
                m = random.choice([2, 3, 4])
                # Random hằng số c dương để nhân tử thứ hai luôn vô nghiệm và dương (Bài gốc c = 2)
                c = random.choice([2, 3])

                # Phương trình: (2cos(x/m) - 1)(sin(x/m) + c) = 0
                # Vì sin(x/m) + c > 0 nên phương trình <=> cos(x/m) = 1/2 <=> x/m = +- pi/3 + k2pi <=> x = +- m*pi/3 + k * 2*m*pi
                chu_ky = 2 * m

                # Đáp án đúng dưới dạng chuỗi LaTeX
                da_val = 'x=\\pm \\frac{%s\\pi}{3}+k%s\\pi ,\\left( k\\in \\mathbb{Z} \\right)' % (latex(m) if m != 1 else '', latex(chu_ky))
                da = '$%s$' % da_val

                # Tạo các phương án sai (nhiễu) không trùng đáp án đúng
                s = [
                    '$x=\\pm \\frac{%s\\pi}{3}+k2\\pi ,\\left( k\\in \\mathbb{Z} \\right)$' % (latex(m) if m != 1 else ''),
                    '$x=\\pm \\frac{\\pi}{3}+k2\\pi ,\\left( k\\in \\mathbb{Z} \\right)$',
                    '$x=\\pm \\frac{\\pi}{3}+k%s\\pi ,\\left( k\\in \\mathbb{Z} \\right)$' % (latex(chu_ky)),
                    '$x=\\pm \\frac{%s\\pi}{3}+k%s\\pi ,\\left( k\\in \\mathbb{Z} \\right)$' % (latex(m+1), latex(chu_ky)),
                    '$x=\\pm \\frac{\\pi}{6}+k%s\\pi ,\\left( k\\in \\mathbb{Z} \\right)$' % (latex(chu_ky))
                ]
                # Lọc bỏ giá trị trùng nếu có
                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Giải phương trình $\\left( 2\\cos \\frac{x}{%s}-1 \\right)\\left( \\sin \\frac{x}{%s}+%s \\right)=0$.'''
                                 % (latex(m), latex(m), latex(c)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết trình bày rõ ràng từng bước như bản gốc
                loigiai = ('''Vì $-1\\le \\sin \\frac{x}{%s}\\le 1, \\forall x\\in \\mathbb{R}\\Rightarrow \\sin \\frac{x}{%s}+%s>0$ \\\\
                           Vậy phương trình tương đương \\\\
                           $2\\cos \\frac{x}{%s}-1=0\\Leftrightarrow \\cos \\frac{x}{%s}=\\frac{1}{2}\\Leftrightarrow \\frac{x}{%s}=\\pm \\frac{\\pi}{3}+k2\\pi $ \\\\
                           $\\Leftrightarrow %s$.'''
                           % (latex(m), latex(m), latex(c),
                              latex(m), latex(m), latex(m),
                              da_val))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

