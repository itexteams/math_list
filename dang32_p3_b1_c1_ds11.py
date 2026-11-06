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


def bt_dang32_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':

                # Random giá trị x = m*pi/n để tạo tính ngẫu nhiên cho đề bài
                n = random.randint(2020, 2030)
                m = n + 1

                # Đáp án đúng dưới dạng chuỗi có dấu phẩy
                da = '$1,5$'

                # Tạo danh sách các phương án nhiễu (không trùng với đáp án đúng)
                s = ['$1$', '$2$', '$2,5$', '$0,5$', '$-1,5$', '$3$']
                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Câu hỏi dựa trên hình ảnh image_1a24c3.png
                noidungcauhoi = ('''Cho biểu thức $C = \\cos^2 x + \\cos^2\\left(\\frac{\\pi}{3} + x\\right) + \\cos^2\\left(\\frac{\\pi}{3} - x\\right)$ khi $x = \\frac{%s\\pi}{%s}$ thì $C$ bằng bao nhiêu?'''
                                 %(latex(m), latex(n)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước
                loigiai=('''Sử dụng công thức hạ bậc $\\cos^2 \\alpha = \\frac{1 + \\cos 2\\alpha}{2}$, ta biến đổi biểu thức $C$ như sau:\\\\
                         $C = \\frac{1 + \\cos 2x}{2} + \\frac{1 + \\cos\\left(\\frac{2\\pi}{3} + 2x\\right)}{2} + \\frac{1 + \\cos\\left(\\frac{2\\pi}{3} - 2x\\right)}{2}$\\\\
                         $C = \\frac{3}{2} + \\frac{1}{2} \\left[ \\cos 2x + \\cos\\left(\\frac{2\\pi}{3} + 2x\\right) + \\cos\\left(\\frac{2\\pi}{3} - 2x\\right) \\right]$.\\\\
                         Áp dụng công thức biến đổi tổng thành tích $\\cos A + \\cos B = 2\\cos\\frac{A+B}{2}\\cos\\frac{A-B}{2}$, ta có:\\\\
                         $\\cos\\left(\\frac{2\\pi}{3} + 2x\\right) + \\cos\\left(\\frac{2\\pi}{3} - 2x\\right) = 2\\cos\\frac{2\\pi}{3}\\cos 2x = 2 \\cdot \\left(-\\frac{1}{2}\\right) \\cdot \\cos 2x = -\\cos 2x$.\\\\
                         Thay vào biểu thức $C$, ta được:\\\\
                         $C = \\frac{3}{2} + \\frac{1}{2} \\left[ \\cos 2x - \\cos 2x \\right] = \\frac{3}{2} = 1,5$.\\\\
                         Như vậy, giá trị của biểu thức $C$ độc lập với biến $x$ và luôn bằng $1,5$.\\\\
                         Do đó, với $x = \\frac{%s\\pi}{%s}$ thì giá trị của $C$ vẫn bằng $1,5$.'''
                         %(latex(m), latex(n)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(1.5))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

