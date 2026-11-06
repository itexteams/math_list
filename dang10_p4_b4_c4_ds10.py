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


def bt_dang10_p4_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thiết kế bài toán: sqrt(x^2 - 2ax + b) = x^2 - 2ax + c
                # Đặt t = x^2 - 2ax + b. Phương trình: sqrt(t) = t + c - b
                # Gọi k = b - c (trong ảnh k = 5 - 3 = 2)
                # Phương trình: sqrt(t) = t - k <=> t = (t - k)^2 (với t >= k)
                # <=> t^2 - (2k + 1)t + k^2 = 0
                # Để có nghiệm đẹp, biệt thức Delta = (2k+1)^2 - 4k^2 = 4k + 1 phải là số chính phương.
                # Chọn k từ tập {2, 6, 12, 20} để 4k+1 lần lượt là {9, 25, 49, 81}

                k = random.choice([2, 6, 12])
                a = randint(1, 4) # Hệ số của x là -2a

                # Giải t^2 - (2k+1)t + k^2 = 0
                delta_t = 4*k + 1
                sqrt_delta = int(math.sqrt(delta_t))
                t1 = (2*k + 1 - sqrt_delta) // 2 # Nghiệm t nhỏ (thường < k, loại)
                t2 = (2*k + 1 + sqrt_delta) // 2 # Nghiệm t lớn (thường >= k, nhận)

                # Để x^2 - 2ax + b = t2 có nghiệm duy nhất (như ảnh), ta chọn b sao cho 
                # x^2 - 2ax + (b - t2) = 0 có Delta_x = 0 => b - t2 = a^2 => b = a^2 + t2
                b = a**2 + t2
                c = b - k

                # Các hệ số khai triển của x^2 - 2ax + b
                hso_x = -2*a

                # Biểu thức trong và ngoài căn
                f_trong = x**2 + hso_x*x + b
                f_ngoai = x**2 + hso_x*x + c

                # Đáp án đúng là 1 nghiệm
                da_d = '\\True $1$'

                # Các phương án sai
                s = ['$0$', '$2$', '$3$', 'Vô số']
                random.shuffle(s)
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Tìm số nghiệm của phương trình $\\sqrt{%s} = %s$.'''
                                 %(latex(f_trong), latex(f_ngoai)))

                # Nội dung lời giải
                loigiai = ('''Ta có: $x^2 %s x + %s = (x %s %s)^2 + %s > 0, \\forall x \\in \\mathbb{R}$. \\\\
                             Đặt $t = x^2 %s x + %s$, ta có phương trình trở thành $\\sqrt{t} = t - %s$ \\\\
                             $\\sqrt{t} = t - %s \\Leftrightarrow \\begin{cases} t \\ge %s \\\\ t = (t - %s)^2 \\end{cases} 
                             \\Leftrightarrow \\begin{cases} t \\ge %s \\\\ t^2 - %st + %s = 0 \\end{cases} 
                             \\Leftrightarrow \\begin{cases} t \\ge %s \\\\ \\left[ \\begin{aligned} t &= %s \\\\ t &= %s \\end{aligned} \\right. \\end{cases} \\Rightarrow t = %s$. \\\\
                             Khi đó $%s = x^2 %s x + %s \\Leftrightarrow (x %s %s)^2 = 0 \\Leftrightarrow x = %s$. Thử lại ta thấy $x = %s$ thỏa mãn. \\\\
                             Suy ra phương trình đã cho có $1$ nghiệm.'''
                           %(latex(hso_x), latex(b), '-' if a > 0 else '+', abs(a), latex(t2),
                             latex(hso_x), latex(b), latex(k),
                             latex(k), latex(k), latex(k),
                             latex(k), latex(2*k+1), latex(k**2),
                             latex(k), latex(t1), latex(t2), latex(t2),
                             latex(t2), latex(hso_x), latex(b), '-' if a > 0 else '+', abs(a), latex(a), latex(a)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

