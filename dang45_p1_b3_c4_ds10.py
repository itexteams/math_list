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


def bt_dang45_p1_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random các hệ số sao cho bài toán có nghiệm đẹp hoặc kiểm soát được
                # Phương trình: (x-1)[x^2 + 2(m+a)x + bm + c] = 0
                # Trong ảnh gốc: a=3, b=4, c=12
                a = randint(1, 4)
                b = randint(2, 5)
                c = b * randint(2, 4) # Đảm bảo có nhân tử chung để giải hệ dễ hơn nếu cần

                # Biến số m cho Sympy
                m_sym = symbols('m')

                # Delta phẩy của phương trình bậc hai (*): x^2 + 2(m+a)x + bm + c = 0
                # Delta' = (m+a)^2 - (bm + c) = m^2 + (2a-b)m + (a^2 - c)
                # Để đơn giản và giống mẫu, ta sẽ lấy lại thông số gần giống ảnh để đảm bảo có nghiệm m
                a, b, c = 3, 4, 12 

                # Các điều kiện từ hình ảnh:
                # 1. Delta' > 0: m^2 + 2m - 3 > 0 <=> m < -3 hoặc m > 1
                # 2. x1+1 + x2+1 > 0 <=> -2(m+3) + 2 > 0 <=> -2m - 4 > 0 <=> m < -2
                # 3. (x1+1)(x2+1) > 0 <=> x1x2 + (x1+x2) + 1 > 0 <=> (4m+12) - 2(m+3) + 1 > 0 <=> 2m + 7 > 0 <=> m > -3.5
                # Kết hợp: -3.5 < m < -3

                # Đáp án đúng theo cấu trúc latex
                da_str = '$-\\frac{7}{2} < m < -3$ và $m \\neq -\\frac{19}{6}$'
                da = da_str

                # Các phương án nhiễu (thay đổi dấu hoặc giá trị)
                s = [
                    '$-\\frac{7}{2} < m < -3$',
                    '$m < -3$ và $m \\neq -\\frac{19}{6}$',
                    '$m > -\\frac{7}{2}$ và $m \\neq -\\frac{19}{6}$',
                    '$-3 < m < 1$ và $m \\neq -\\frac{19}{6}$',
                    '$m < -3.5$',
                    '$m > 1$'
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Giá trị của $m$ để phương trình $(x-1)[x^2 + 2(m+%s)x + %sm + %s] = 0$ có ba nghiệm phân biệt lớn hơn $-1$ là'''
                                  %(latex(a), latex(b), latex(c)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai=('''Ta có:
                         $(x-1)[x^2 + 2(m+%s)x + %sm + %s] = 0 \\Leftrightarrow \\left[\\begin{array}{l} x=1 \\\\ x^2 + 2(m+%s)x + %sm + %s = 0 \\quad (*) \\end{array}\\right.$ \\\\
                         Phương trình đã cho có ba nghiệm phân biệt lớn hơn $-1$ khi và chỉ khi phương trình $(*)$ có hai nghiệm phân biệt $x_1, x_2$ lớn hơn $-1$ và khác $1$. \\\\
                         Điều này tương đương với: \\\\
                         $\\begin{cases} \\Delta' > 0 \\\\ x_1 + 1 + x_2 + 1 > 0 \\\\ (x_1 + 1)(x_2 + 1) > 0 \\\\ 1^2 + 2(m+%s) \\cdot 1 + %sm + %s \\neq 0 \\end{cases} 
                         \\Leftrightarrow \\begin{cases} (m+%s)^2 - (%sm + %s) > 0 \\\\ -2(m+%s) + 2 > 0 \\\\ (%sm + %s) - 2(m+%s) + 1 > 0 \\\\ %sm + %s \\neq 0 \\end{cases}$ \\\\
                         $\\Leftrightarrow \\begin{cases} m^2 + 2m - 3 > 0 \\\\ -2m - 4 > 0 \\\\ 2m + 7 > 0 \\\\ 6m + 19 \\neq 0 \\end{cases}
                         \\Leftrightarrow \\begin{cases} m < -3 \\text{ hoặc } m > 1 \\\\ m < -2 \\\\ m > -\\frac{7}{2} \\\\ m \\neq -\\frac{19}{6} \\end{cases} 
                         \\Leftrightarrow \\begin{cases} -\\frac{7}{2} < m < -3 \\\\ m \\neq -\\frac{19}{6} \\end{cases}$.'''
                         %(latex(a), latex(b), latex(c), latex(a), latex(b), latex(c), 
                           latex(a), latex(b), latex(c), latex(a), latex(b), latex(c), 
                           latex(a), latex(b), latex(c), latex(a), latex(b+2), latex(1+2*a+c)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n' +
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

