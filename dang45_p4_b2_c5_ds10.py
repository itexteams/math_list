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


def bt_dang45_p4_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (giữ cấu trúc mẫu)
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # a: số học sinh lớp 12A, b: số học sinh lớp 12B, c: số học sinh lớp 12C
                a = randint(4, 5)
                b = randint(3, 4)
                c = randint(2, 3)
                k = 5 # Số học sinh cần chọn
                n = a + b + c # Tổng số học sinh

                # Tính toán các giá trị tổ hợp bằng sympy
                c_total = binomial(n, k)
                c_ab = binomial(a + b, k)
                c_ac = binomial(a + c, k)
                c_bc = binomial(b + c, k)

                # Kết quả đúng
                kq_val = c_total - (c_ab + c_ac + c_bc)
                da = '$%s$' % (latex(kq_val))

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s = []
                while len(s) < 3:
                    sai = kq_val + random.choice([-20, -10, 10, 20, 30, 40, 50])
                    if sai > 0 and sai != kq_val and str(sai) not in s:
                        s.append('$%s$' % (latex(sai)))

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (B2 - Viết lại y hệt đề bài theo mẫu)
                noidungcauhoi = ('''Đội văn nghệ của nhà trường gồm $%s$ học sinh lớp 12A, $%s$ học sinh lớp 12B và $%s$ học sinh lớp 12C. Chọn ngẫu nhiên $%s$ học sinh từ đội văn nghệ để biểu diễn trong lễ bế giảng. Tìm số cách chọn sao cho lớp nào cũng có học sinh được chọn.'''
                                 % (latex(a), latex(b), latex(c), latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2 - Viết lại chi tiết theo mẫu ảnh)
                loigiai = ('''Số cách chọn ngẫu nhiên $%s$ học sinh từ $%s$ học sinh là $C_{%s}^{%s}$ cách. \\\\
                             Số cách chọn $%s$ học sinh mà chỉ có học sinh từ $2$ lớp là: $C_{%s}^{%s} + C_{%s}^{%s} + C_{%s}^{%s}$ cách. \\\\
                             (Lưu ý: Vì số học sinh tối đa của mỗi lớp đều nhỏ hơn $%s$ nên không có trường hợp $%s$ học sinh được chọn chỉ từ $1$ lớp). \\\\
                             Vậy số cách chọn $%s$ học sinh có cả $3$ lớp là: \\\\
                             $C_{%s}^{%s} - \\left( C_{%s}^{%s} + C_{%s}^{%s} + C_{%s}^{%s} \\right) = %s - \\left( %s + %s + %s \\right) = %s$.'''
                           % (latex(k), latex(n), latex(n), latex(k),
                              latex(k), latex(a+b), latex(k), latex(a+c), latex(k), latex(b+c), latex(k),
                              latex(k), latex(k),
                              latex(k), latex(n), latex(k), latex(a+b), latex(k), latex(a+c), latex(k), latex(b+c), latex(k),
                              latex(c_total), latex(c_ab), latex(c_ac), latex(c_bc), latex(kq_val)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

