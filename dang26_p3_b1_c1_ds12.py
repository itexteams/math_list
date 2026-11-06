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


def bt_dang26_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tham số của bài toán
                # Chọn u chẵn để b = 1.5*u luôn là số nguyên
                u = random.choice([2, 4, 6, 8, 10, 12]) 
                s_dist = random.choice([150, 200, 250, 300, 350, 400])

                a = u
                b = int(1.5 * u)
                kq = a + b

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),
                      ]
                da = random.choice(du)

                # Tạo các phương án sai (đảm bảo không trùng với đáp án đúng)
                s = ['$%s$'%(latex(kq + 1)),
                     '$%s$'%(latex(kq + 2)),
                     '$%s$'%(latex(kq + 3)),
                     '$%s$'%(latex(abs(kq - 1))),
                     '$%s$'%(latex(abs(kq - 2))),
                     '$%s$'%(latex(kq * 2)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một con cá hồi bơi ngược dòng để vượt khoảng cách là $%s$ km. Vận tốc dòng nước là $%s$ km/h. Nếu vận tốc bơi của cá khi nước đứng yên là $v$ (km/h) thì năng lượng tiêu hao của cá trong $t$ giờ được cho bởi công thức $E(v) = cv^3t$, trong đó $c$ là hằng số và $E$ tính bằng Jun. Biết vận tốc bơi của cá khi nước đứng yên nằm ở khoảng $(a;b)$ thì năng lượng tiêu hao của cá giảm. Giá trị $a+b$ bằng bao nhiêu?'''
                                 %(latex(s_dist), latex(u)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $v$ (km/h) là vận tốc bơi của cá khi nước đứng yên. Vì cá bơi ngược dòng nên vận tốc thực tế của cá là $v - %s$ (km/h), điều kiện $v > %s$.\\\\
                             Thời gian để cá bơi hết quãng đường $%s$ km là $t = \\frac{%s}{v - %s}$ (giờ).\\\\
                             Năng lượng tiêu hao của cá để vượt quãng đường đó là:\\\\
                             $E(v) = c \\cdot v^3 \\cdot t = c \\cdot v^3 \\cdot \\frac{%s}{v - %s} = %sc \\cdot \\frac{v^3}{v - %s}$ (Jun).\\\\
                             Xét hàm số $f(v) = \\frac{v^3}{v - %s}$ với $v > %s$.\\\\
                             Ta có $f'(v) = \\frac{3v^2(v - %s) - v^3 \\cdot 1}{(v - %s)^2} = \\frac{3v^3 - %sv^2 - v^3}{(v - %s)^2} = \\frac{2v^3 - %sv^2}{(v - %s)^2} = \\frac{v^2(2v - %s)}{(v - %s)^2}$.\\\\
                             Để năng lượng tiêu hao giảm thì $f'(v) < 0 \\Leftrightarrow 2v - %s < 0 \\Leftrightarrow v < %s$.\\\\
                             Kết hợp với điều kiện $v > %s$, ta được khoảng tốc độ để năng lượng giảm là $(%s; %s)$.\\\\
                             Suy ra $a = %s$ và $b = %s$.\\\\
                             Vậy $a + b = %s + %s = %s$.'''
                             %(latex(u), latex(u),
                               latex(s_dist), latex(s_dist), latex(u),
                               latex(s_dist), latex(u), latex(s_dist), latex(u),
                               latex(u), latex(u),
                               latex(u), latex(u), latex(3*u), latex(u), latex(3*u), latex(u), latex(3*u), latex(u),
                               latex(3*u), latex(b),
                               latex(u), latex(a), latex(b),
                               latex(a), latex(b),
                               latex(a), latex(b), latex(kq)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content  

