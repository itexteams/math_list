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


def bt_dang68_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tạo các hệ số ngẫu nhiên để bài toán luôn có nghiệm đẹp
                # d2: x = x0 + u1*t ; y = y0 + u2*t
                # Để x = 0 thì t = -x0/u1. Chọn u1 = 1 để t luôn nguyên.
                u1 = 1
                x0 = randint(1, 4)
                u2 = randint(1, 3)
                y0 = randint(5, 10)

                # Tính tọa độ giao điểm trên trục tung
                t_val = -x0 # vì x0 + 1*t = 0
                y_val = y0 + u2 * t_val

                # Đảm bảo y_val > 0 để bài toán tương tự mẫu
                if y_val <= 0: y_val = 2 

                # d1: cx*x + cy*m*y - m^2 = 0
                cx = randint(2, 6)
                cy = randint(1, 4)

                # Tại x = 0: cy * m * y_val - m^2 = 0 <=> m * (cy * y_val - m) = 0
                m1 = 0
                m2 = cy * y_val

                # Các đáp án
                # Đáp án đúng
                kq_dung = 'm = 0 \\text{ hoặc } m = ' + str(m2)

                # Tạo các phương án sai (không trùng đáp án đúng)
                s = [
                    'm = 0 \\text{ hoặc } m = ' + str(-m2),
                    'm = 0 \\text{ hoặc } m = ' + str(m2 // 2 if m2 % 2 == 0 else m2 + 1),
                    'm = 0 \\text{ hoặc } m = ' + str(m2 + 2),
                    'm = 0 \\text{ hoặc } m = ' + str(abs(m2 - 4))
                ]
                # Loại bỏ giá trị trùng nếu có
                s = list(set(s))
                if kq_dung in s: s.remove(kq_dung)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('Tìm giá trị của tham số $m$ để hai đường thẳng $d_1: ' + str(cx) + 'x + ' + str(cy) + 'my - m^2 = 0$ và $d_2: \\begin{cases} x = ' + str(x0) + ' + t \\\\ y = ' + str(y0) + ' + ' + str(u2) + 't \\end{cases}$ cắt nhau tại một điểm thuộc trục tung.')

                # Các đáp án
                da_d = ('\\True $' + str(kq_dung) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('Điểm nằm trên trục tung có hoành độ $x = 0$. \\\\'
                           'Thay $x = 0$ vào phương trình đường thẳng $d_2$, ta có: \\\\'
                           '$\\begin{cases} 0 = ' + str(x0) + ' + t \\\\ y = ' + str(y0) + ' + ' + str(u2) + 't \\end{cases} \\Leftrightarrow \\begin{cases} t = ' + str(t_val) + ' \\\\ y = ' + str(y0) + ' + ' + str(u2) + '(' + str(t_val) + ') = ' + str(y_val) + ' \\end{cases}$. \\\\'
                           'Vậy giao điểm của $d_2$ và trục tung là $A(0; ' + str(y_val) + ')$. \\\\'
                           'Để $d_1$ và $d_2$ cắt nhau tại $A$, thì $A \\in d_1$. Thay tọa độ $A$ vào phương trình $d_1$: \\\\'
                           '$' + str(cx) + '\\cdot 0 + ' + str(cy) + 'm \\cdot ' + str(y_val) + ' - m^2 = 0 \\Leftrightarrow ' + str(cy * y_val) + 'm - m^2 = 0 \\Leftrightarrow \\left[ \\begin{array}{l} m = 0 \\\\ m = ' + str(m2) + ' \\end{array} \\right.$.')

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

