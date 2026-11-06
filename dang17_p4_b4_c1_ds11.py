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


def bt_dang17_p4_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và tạo tính ngẫu nhiên cho bài toán (B3)
            lisdang = ['1', '2', '3']
            dang = random.choice(lisdang)

            if dang == '1':
                # Dạng gốc: 2sin(x) - 1 = 0 <=> sin(x) = 1/2
                a, b = 2, 1
                val_latex = '\\frac{1}{2}'
                goc_latex = '\\frac{\\pi}{6}'
                nghiem1 = '\\frac{\\pi}{6} + k2\\pi'
                nghiem2 = '\\frac{5\\pi}{6} + k2\\pi'

                da_text = 'S = \\left\\{ \\frac{\\pi}{6} + k2\\pi; \\frac{5\\pi}{6} + k2\\pi, k \\in \\mathbb{Z} \\right\\}'
                das1 = 'S = \\left\\{ \\frac{\\pi}{3} + k2\\pi; -\\frac{2\\pi}{3} + k2\\pi, k \\in \\mathbb{Z} \\right\\}' # Bẫy nghiệm cos
                das2 = 'S = \\left\\{ \\frac{\\pi}{6} + k2\\pi; -\\frac{\\pi}{6} + k2\\pi, k \\in \\mathbb{Z} \\right\\}' # Bẫy đối xứng qua Ox
                das3 = 'S = \\left\\{ \\frac{1}{2} + k2\\pi, k \\in \\mathbb{Z} \\right\\}'

            elif dang == '2':
                # Dạng 2: 2sin(x) - sqrt(2) = 0 <=> sin(x) = sqrt(2)/2
                a, b = 2, sqrt(2)
                val_latex = '\\frac{\\sqrt{2}}{2}'
                goc_latex = '\\frac{\\pi}{4}'
                nghiem1 = '\\frac{\\pi}{4} + k2\\pi'
                nghiem2 = '\\frac{3\\pi}{4} + k2\\pi'

                da_text = 'S = \\left\\{ \\frac{\\pi}{4} + k2\\pi; \\frac{3\\pi}{4} + k2\\pi, k \\in \\mathbb{Z} \\right\\}'
                das1 = 'S = \\left\\{ \\pm\\frac{\\pi}{4} + k2\\pi, k \\in \\mathbb{Z} \\right\\}'
                das2 = 'S = \\left\\{ \\frac{\\pi}{4} + k\\pi; \\frac{3\\pi}{4} + k\\pi, k \\in \\mathbb{Z} \\right\\}' # Bẫy chu kỳ k*pi
                das3 = 'S = \\left\\{ \\frac{\\sqrt{2}}{2} + k2\\pi, k \\in \\mathbb{Z} \\right\\}'

            else:
                # Dạng 3: 2sin(x) - sqrt(3) = 0 <=> sin(x) = sqrt(3)/2
                a, b = 2, sqrt(3)
                val_latex = '\\frac{\\sqrt{3}}{2}'
                goc_latex = '\\frac{\\pi}{3}'
                nghiem1 = '\\frac{\\pi}{3} + k2\\pi'
                nghiem2 = '\\frac{2\\pi}{3} + k2\\pi'

                da_text = 'S = \\left\\{ \\frac{\\pi}{3} + k2\\pi; \\frac{2\\pi}{3} + k2\\pi, k \\in \\mathbb{Z} \\right\\}'
                das1 = 'S = \\left\\{ \\frac{\\pi}{6} + k2\\pi; \\frac{5\\pi}{6} + k2\\pi, k \\in \\mathbb{Z} \\right\\}'
                das2 = 'S = \\left\\{ \\pm\\frac{\\pi}{3} + k2\\pi, k \\in \\mathbb{Z} \\right\\}'
                das3 = 'S = \\left\\{ \\frac{\\sqrt{3}}{2} + k2\\pi, k \\in \\mathbb{Z} \\right\\}'

            # Câu hỏi sử dụng định dạng %s đúng quy chuẩn
            noidungcauhoi = ('''Giải phương trình $%s\\sin x - %s = 0$.''' 
                             % (latex(a), latex(b)))

            # Nội dung lời giải chi tiết theo từng bước tương tự đề gốc
            loigiai = ('''Ta có: $%s\\sin x - %s = 0 \\Leftrightarrow \\sin x = %s \\Leftrightarrow \\sin x = \\sin %s \\Leftrightarrow \\left[\\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned}\\right. k \\in \\mathbb{Z}$.''' 
                       % (latex(a), latex(b), val_latex, goc_latex, nghiem1, nghiem2))

            # Gán phương án trả lời (Không thêm dấu chấm ở cuối các phương án)
            da_d = ('\\True $' + str(da_text) + '$')
            da_s1 = '$' + str(das1) + '$'
            da_s2 = '$' + str(das2) + '$'
            da_s3 = '$' + str(das3) + '$'

            # Đưa các đáp án vào danh sách và trộn ngẫu nhiên (B4)
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo định dạng minipage mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

