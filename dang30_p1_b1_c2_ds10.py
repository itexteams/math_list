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


def bt_dang30_p1_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các hệ số của bất phương trình: a(x + b) - c < dx - ey + f
                a = randint(2, 6)
                b = randint(1, 5)
                c = randint(1, 10)
                # Đảm bảo hệ số của x sau khi rút gọn luôn dương (a - d > 0)
                d = randint(1, a - 1)
                e = randint(1, 5)
                f = randint(1, 10)

                # Tính toán các hằng số trung gian
                ab = a * b
                val1 = ab - c

                # Rút gọn về dạng: Ax + By + C < 0
                A = a - d
                B = e
                C = val1 - f

                # Tạo đáp án đúng: Điểm KHÔNG thuộc miền nghiệm -> A*x + B*y + C >= 0
                xt = randint(-3, 3)
                yt_min = math.ceil((-C - A*xt) / B)
                yt = randint(yt_min, yt_min + 3)

                # Tạo 3 đáp án sai: Điểm THUỘC miền nghiệm -> A*x + B*y + C < 0
                false_points = []
                while len(false_points) < 3:
                    xf = randint(-3, 3)
                    yf_max = math.floor((-C - A*xf) / B)
                    # Đảm bảo dấu < (nghiêm ngặt)
                    if (-C - A*xf) / B == yf_max:
                        yf_max -= 1
                    yf = randint(yf_max - 3, yf_max)
                    if (xf, yf) not in false_points and (xf, yf) != (xt, yt):
                        false_points.append((xf, yf))

                # Các đáp án (không có dấu chấm ở cuối)
                da = '$(%s; %s)$' % (xt, yt)
                das1 = '$(%s; %s)$' % (false_points[0][0], false_points[0][1])
                das2 = '$(%s; %s)$' % (false_points[1][0], false_points[1][1])
                das3 = '$(%s; %s)$' % (false_points[2][0], false_points[2][1])

                # Câu hỏi
                noidungcauhoi = ('Miền nghiệm của bất phương trình $%s(x + %s) - %s < %sx - %sy + %s$ là phần mặt phẳng \\textbf{không} chứa điểm nào?'
                                 % (a, b, c, d, e, f))

                # Xử lý định dạng chuỗi để hiển thị dấu + / - đẹp mắt trong lời giải
                if val1 > 0:
                    str_val1 = "+ " + str(val1)
                elif val1 < 0:
                    str_val1 = "- " + str(abs(val1))
                else:
                    str_val1 = ""

                if C > 0:
                    str_C = "+ " + str(C)
                elif C < 0:
                    str_C = "- " + str(abs(C))
                else:
                    str_C = ""

                val_test = A*xt + B*yt + C

                # Nội dung lời giải phân tích từng bước như người thật
                loigiai = ('Ta có: $%s(x + %s) - %s < %sx - %sy + %s$ \\\\\n'
                           '$\\Leftrightarrow %sx + %s - %s < %sx - %sy + %s$ \\\\\n'
                           '$\\Leftrightarrow %sx %s < %sx - %sy + %s$ \\\\\n'
                           '$\\Leftrightarrow %sx + %sy %s < 0$. \\\\\n'
                           'Thay tọa độ điểm $%s$ vào bất phương trình rút gọn trên ta được: $%s \\cdot (%s) + %s \\cdot (%s) %s = %s \\ge 0$ (Không thỏa mãn). \\\\\n'
                           'Vậy miền nghiệm của bất phương trình không chứa điểm $%s$.'
                           % (a, b, c, d, e, f, 
                              a, ab, c, d, e, f,
                              a, str_val1, d, e, f,
                              A, B, str_C,
                              da.replace('$', ''), A, xt, B, yt, str_C, val_test,
                              da.replace('$', '')))

                # Gắn thẻ đáp án đúng
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách rồi trộn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

