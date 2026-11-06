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


def bt_dang71_p1_b2_c4_ds10(self):
            # Khai báo biến
            # --- KHỞI TẠO BIẾN ---
            x = symbols('x')


            x1 = random.randint(-5, 2)
            x2 = random.randint(x1 + 2, 6) # Đảm bảo xA < xB và cách nhau ít nhất 2 đơn vị


            b1 = random.randint(-3, 3)
            c1 = random.randint(-3, 3)


            b2 = b1 - (x1 + x2)
            c2 = c1 + x1 * x2

            # Hàm số cụ thể
            y1 = x**2 + b1*x + c1
            y2 = 2*x**2 + b2*x + c2

            # Tọa độ giao điểm
            y_A = y1.subs(x, x1)
            y_B = y1.subs(x, x2)

            # Tính độ dài AB: sqrt((x2-x1)^2 + (yB-yA)^2)
            dist_sq = (x2 - x1)**2 + (y_B - y_A)**2
            dist_val = sqrt(dist_sq)

            # --- XỬ LÝ ĐÁP ÁN ---
            kq = "$%s$" % latex(dist_val)

            # Tạo các phương án nhiễu (tránh trùng đáp án đúng)
            s = set()
            while len(s) < 3:
                fake_val = random.choice([
                    sqrt(dist_sq + random.randint(2, 10)),
                    sqrt(abs(dist_sq - random.randint(2, 10))),
                    dist_val + random.randint(1, 5),
                    2 * dist_val
                ])
                fake_str = "$%s$" % latex(fake_val)
                if fake_str != kq:
                    s.add(fake_str)

            list_s = list(s)
            da_d = '\\True ' + kq
            list_1 = [da_d] + list_s
            random.shuffle(list_1)

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Cho hai parabol có phương trình $y = %s$ và $y = %s$. Biết hai parabol cắt nhau tại hai điểm $A$ và $B$ ($x_A < x_B$). Độ dài đoạn thẳng $AB$ là'''
                             %(latex(y1), latex(y2)))

            # --- NỘI DUNG LỜI GIẢI ---
            loigiai = ('''Phương trình hoành độ giao điểm của hai parabol:
                $$ %s = %s \\Leftrightarrow x^2 - %sx %s = 0 \\Leftrightarrow \\left[\\begin{aligned} &x = %s \\\\ &x = %s \\end{aligned}\\right. $$
                Với $x = %s \\Rightarrow y = %s$; với $x = %s \\Rightarrow y = %s$, do đó hai giao điểm là $A(%s;%s)$ và $B(%s;%s)$.
                Từ đó $AB = \\sqrt{(%s - (%s))^2 + (%s - %s)^2} = %s$.'''
                %(latex(y2), latex(y1), latex(x1+x2), latex(x1*x2), latex(x1), latex(x2),
                  latex(x1), latex(y_A), latex(x2), latex(y_B), 
                  latex(x1), latex(y_A), latex(x2), latex(y_B),
                  latex(x2), latex(x1), latex(y_B), latex(y_A), latex(dist_val)
                ))

            # --- XUẤT KẾT QUẢ ---
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

