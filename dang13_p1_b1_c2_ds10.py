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


def bt_dang13_p1_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến sympy
            x, y = symbols('x y')

            # B1 & B3: Nghiên cứu đề bài và thiết lập random
            # Bất phương trình dạng ax + by >= c
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            c = random.randint(1, 10)

            # Tạo điểm M(x0, y0) sao cho thuộc miền nghiệm (Đáp án đúng)
            # Chọn x0, y0 ngẫu nhiên rồi điều chỉnh c' >= c
            x0 = random.randint(-2, 5)
            y0 = random.randint(-2, 5)
            while a*x0 + b*y0 < c:
                x0 += 1
                y0 += 1

            # Tạo 3 điểm sai (không thuộc miền nghiệm)
            wrong_points = []
            while len(wrong_points) < 3:
                xw = random.randint(-5, 5)
                yw = random.randint(-5, 5)
                if a*xw + b*yw < c:
                    point = (xw, yw)
                    if point not in wrong_points:
                        wrong_points.append(point)

            # Thiết lập nội dung câu hỏi
            noidungcauhoi = ('''Biểu diễn miền nghiệm của bất phương trình $%s x + %s y \\geq %s$ là miền $(H)$. Điểm nào sau đây thuộc $(H)$?'''
                            %(latex(a) if a != 1 else "", latex(b) if b != 1 else "", latex(c)))

            # Xử lý hiển thị dấu + - (trong trường hợp b âm, nhưng ở đây b dương cho đơn giản)
            noidungcauhoi = noidungcauhoi.replace('+ -', '- ').replace('- -', '+ ')

            # Các đáp án
            da_d = '\\True $M(%s;%s)$' % (latex(x0), latex(y0))
            da_s1 = '$P(%s;%s)$' % (latex(wrong_points[0][0]), latex(wrong_points[0][1]))
            da_s2 = '$N(%s;%s)$' % (latex(wrong_points[1][0]), latex(wrong_points[1][1]))
            da_s3 = '$Q(%s;%s)$' % (latex(wrong_points[2][0]), latex(wrong_points[2][1]))

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            val_check = a*x0 + b*y0
            loigiai = ('''Thay $x = %s, y = %s$ vào bất phương trình ta được $%s \\cdot (%s) + %s \\cdot (%s) \\geq %s \\Leftrightarrow %s \\geq %s$ (đúng). \\\\
                         Vậy điểm $M(%s;%s)$ thuộc miền nghiệm của bất phương trình.'''
                      %(latex(x0), latex(y0), latex(a), latex(x0), latex(b), latex(y0), latex(c), latex(val_check), latex(c), latex(x0), latex(y0)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

