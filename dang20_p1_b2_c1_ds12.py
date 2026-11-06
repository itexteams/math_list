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


def bt_dang20_p1_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3-Suy nghĩ tìm cách random bài toán
                # Chọn mốc x1, x2 là các điểm cực trị sao cho x1 < x2. (Tương đương 2026 và 2027 trong ảnh)
                x1 = random.randint(10, 3000)
                x2 = x1 + random.randint(1, 10)
                x_truoc = x1 - 1

                # B4-Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                # Đáp án đúng: Hàm số nghịch biến trên [x1; x2] và đồng biến trên [x2; +inf) nên min đạt tại x2
                da = '\\min_{[%s;+\\infty)} f(x) = f(%s)' % (x1, x2)

                # Các phương án nhiễu
                das1 = '\\min_{[%s;+\\infty)} f(x) = f(%s)' % (x1, x1)
                das2 = '\\min_{[%s;+\\infty)} f(x) = f(%s)' % (x1, x_truoc)
                das3 = 'Không xác định'

                # Tạo bảng xét dấu đạo hàm bằng tkz-tab (thay thế cho hình ảnh)
                bang_bien_thien = ('''\\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[nocadre=false,lgt=1.5,espcl=2.5]{$x$ / 1, $f'(x)$ / 1}{$-\\infty$, $%s$, $%s$, $+\\infty$}
            \\tkzTabLine{ , +, 0, -, 0, +, }
            \\end{tikzpicture}
            \\end{center}''' % (x1, x2))

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = f(x)$ xác định, liên tục trên $\\mathbb{R}$ và có bảng xét dấu đạo hàm như sau:
            %s
            Giá trị nhỏ nhất của hàm số $f(x)$ trên nửa khoảng $[%s;+\\infty)$ là''' % (bang_bien_thien, x1))

                # Đưa các đáp án vào danh sách
                da_d = ('\\True $%s$' % da)
                da_s1 = ('$%s$' % das1)
                da_s2 = ('$%s$' % das2)
                da_s3 = das3 # Phương án dạng text, không đặt vào $...$

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Dựa vào bảng xét dấu, xét trên nửa khoảng $[%s; +\\infty)$, ta có: \\\\
            $f'(x) < 0$ trên khoảng $(%s; %s)$ và $f'(x) > 0$ trên khoảng $(%s; +\\infty)$. \\\\
            Suy ra hàm số $y = f(x)$ nghịch biến trên nửa khoảng $[%s; %s]$ và đồng biến trên nửa khoảng $[%s; +\\infty)$. \\\\
            Do đó, trên nửa khoảng $[%s; +\\infty)$, hàm số đạt giá trị nhỏ nhất tại điểm $x = %s$. \\\\
            Vậy $\\min_{[%s;+\\infty)} f(x) = f(%s)$.''' % (x1, x1, x2, x2, x1, x2, x2, x1, x2, x1, x2))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{\n' + str(loigiai) + '\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

