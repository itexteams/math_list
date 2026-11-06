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


def bt_dang60_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Khởi tạo các tham số ngẫu nhiên
                b = random.choice([1, 2, 3])
                c_val = random.randint(-10, 10)

                xA = random.randint(-5, 5)
                yA = random.randint(-5, 5)
                xB = random.randint(-5, 5)
                yB = random.choice([Rational(random.randint(-5, 5), 2), random.randint(-5, 5)])

                k1 = random.randint(2, 5)
                k2 = random.randint(1, 4)

                # Bước 2: Tính toán bằng Sympy
                m = symbols('m')
                xM = -b*m - c_val
                yM = m

                MA2_expr = expand((xA - xM)**2 + (yA - yM)**2)
                MB2_expr = expand((xB - xM)**2 + (yB - yM)**2)
                f_m = expand(k1*MA2_expr + k2*MB2_expr)

                coeff_A = f_m.coeff(m, 2)
                coeff_B = f_m.coeff(m, 1)
                coeff_C = f_m.coeff(m, 0)

                m_min = Rational(-coeff_B, 2*coeff_A)
                val_min = f_m.subs(m, m_min)

                xM_final = xM.subs(m, m_min)
                yM_final = m_min

                # Bước 3: Chuẩn bị nội dung hiển thị (Thay đổi ngoặc tại đây)
                line_eq = 'x + %sy + %s = 0' % (latex(b) if b != 1 else '', latex(c_val))
                line_eq = line_eq.replace('+ -', '- ').replace(' 1y', ' y')

                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho đường thẳng $d:%s$ và hai điểm $A\\left(%s;%s\\right)$, $B\\left(%s;%s\\right)$. Điểm $M$ thuộc $d$ sao cho $%s MA^2 + %s MB^2$ nhỏ nhất là'''
                                %(line_eq, latex(xA), latex(yA), latex(xB), latex(yB), latex(k1), latex(k2)))

                da_dung = '$M\\left(%s;%s\\right)$' % (latex(xM_final), latex(yM_final))

                s = [
                    '$M\\left(%s;%s\\right)$' % (latex(xM_final + 1), latex(yM_final)),
                    '$M\\left(%s;%s\\right)$' % (latex(xM_final), latex(yM_final + 1)),
                    '$M\\left(%s;%s\\right)$' % (latex(xM_final - 1), latex(yM_final - 1)),
                    '$M\\left(%s;%s\\right)$' % (latex(xA), latex(yA)),
                    '$M\\left(%s;%s\\right)$' % (latex(xB), latex(yB))
                ]
                s = [item for item in s if item != da_dung]
                random.shuffle(s)

                da_s1, da_s2, da_s3 = s[0], s[1], s[2]
                list_1 = ['\\True ' + da_dung, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 4: Viết lời giải chi tiết (Thay đổi ngoặc tại đây)
                loigiai = ('''Điểm $M \\in d$ nên có tọa độ dạng $M\\left(%s; m\\right)$.\\\\
                             Ta có $\\vec{MA} = \\left(%s; %s\\right)$, suy ra $%s MA^2 = %s \\left[ \\left(%s\\right)^2 + \\left(%s\\right)^2 \\right]$.\\\\
                             $\\vec{MB} = \\left(%s; %s\\right)$, suy ra $%s MB^2 = %s \\left[ \\left(%s\\right)^2 + \\left(%s\\right)^2 \\right]$.\\\\
                             Do đó $%s MA^2 + %s MB^2 = %s m^2 %s m + %s = %s\\left(m - %s\\right)^2 + %s$.\\\\
                             Dấu "=" xảy ra khi và chỉ khi $m = %s$.\\\\
                             Vậy $%s MA^2 + %s MB^2$ đạt giá trị nhỏ nhất bằng $%s$ khi $M\\left(%s; %s\\right)$.'''
                             %(latex(xM), latex(xA-xM), latex(yA-yM), latex(k1), latex(k1), latex(xA-xM), latex(yA-yM),
                               latex(xB-xM), latex(yB-yM), latex(k2), latex(k2), latex(xB-xM), latex(yB-yM),
                               latex(k1), latex(k2), latex(coeff_A), ('+ ' + latex(coeff_B) if coeff_B >= 0 else latex(coeff_B)), latex(coeff_C), 
                               latex(coeff_A), latex(m_min), latex(val_min),
                               latex(m_min),
                               latex(k1), latex(k2), latex(val_min), latex(xM_final), latex(yM_final)))

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

