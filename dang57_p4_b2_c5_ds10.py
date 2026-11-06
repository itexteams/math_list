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


def bt_dang57_p4_b2_c5_ds10(self):
            # Khai báo biến
            # Để đảm bảo x, y, z nguyên dương và hệ có nghiệm, ta chọn x, y, z trước.

            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lượng bộ sách khác loại
                x = randint(3, 5) # Bộ Toán - Hóa
                y = randint(4, 6) # Bộ Hóa - Lý
                z = randint(5, 7) # Bộ Lý - Toán

                # Tính số lượng sách mỗi loại
                n_toan = x + z
                n_ly = y + z
                n_hoa = x + y

                # Tổng số học sinh (tổng số phần thưởng)
                n_hs = x + y + z

                # Giá trị đáp án đúng (số cách chia)
                # C(n_hs, x) * C(n_hs - x, y) * C(z, z)
                # Trong đề mẫu, đáp án B được viết dưới dạng C(15, 6) * C(9, 4) -> C(s, z) * C(s-z, x)
                da_val = math.comb(n_hs, z) * math.comb(n_hs - z, x)
                da = "$C_{%s}^{%s}C_{%s}^{%s}$" % (latex(n_hs), latex(z), latex(n_hs - z), latex(x))

                # Tạo các phương án sai (B4: Điều chỉnh không trùng đáp án đúng)
                s = []
                # Phương án sai kiểu A: Thay đổi chỉ số
                s1 = "$C_{%s}^{%s}C_{%s}^{%s}$" % (latex(n_hs), latex(z+1), latex(n_hs - z - 1), latex(x-1))
                # Phương án sai kiểu C: Thay đổi chỉ số
                s2 = "$C_{%s}^{%s}C_{%s}^{%s}$" % (latex(n_hs), latex(x-1), latex(n_hs - x + 1), latex(y))
                # Phương án sai kiểu D: Chọn 2 từ tổng số sách
                s3 = "$C_{%s}^{2}$" % (latex(n_toan + n_ly + n_hoa))

                s = [s1, s2, s3]
                # Kiểm tra tránh trùng lặp ngẫu nhiên (dù xác suất rất thấp với công thức này)
                if da in s: s.remove(da)
                while len(s) < 3:
                    random_val = randint(1, 10)
                    extra = "$C_{%s}^{%s}C_{%s}^{%s}$" % (latex(n_hs), latex(z), latex(n_hs - z), latex(x + random_val))
                    if extra != da: s.append(extra)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Có $%s$ quyển sách toán giống nhau, $%s$ quyển sách lý giống nhau và $%s$ quyển sách hóa giống nhau. Tìm số cách trao giải thưởng cho $%s$ học sinh có kết quả thi cao nhất của khối A trong kì thi thử lần hai của trường THPT A, biết mỗi phần thưởng là hai quyển sách khác loại.'''
                                 %(latex(n_toan), latex(n_ly), latex(n_hoa), latex(n_hs)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết lại y hệt bài toán gốc)
                total_books = n_toan + n_ly + n_hoa
                loigiai = ('''Có duy nhất một cách chia $%s$ quyển sách thành $%s$ bộ, mỗi bộ gồm hai quyển sách khác loại, trong đó có:\\\\
                             + $%s$ bộ giống nhau gồm 1 toán và 1 hóa.\\\\
                             + $%s$ bộ giống nhau gồm 1 hóa và 1 lí.\\\\
                             + $%s$ bộ giống nhau gồm 1 lí và toán.\\\\
                             Số cách trao phần thưởng cho $%s$ học sinh được tính như sau:\\\\
                             + Chọn ra $%s$ người để trao bộ sách toán và hóa $\\Rightarrow$ có $C_{%s}^{%s}$ cách.\\\\
                             + Chọn ra $%s$ người để trao bộ sách hóa và lí $\\Rightarrow$ có $C_{%s}^{%s}$ cách.\\\\
                             + Còn lại $%s$ người trao bộ sách toán và lí $\\Rightarrow$ có 1 cách.\\\\
                             Vậy số cách trao phần thưởng là $C_{%s}^{%s} \\cdot C_{%s}^{%s} = $ %s $\\cdot$ %s $= %s$.'''
                           %(latex(total_books), latex(n_hs),
                             latex(x), latex(y), latex(z), latex(n_hs),
                             latex(x), latex(n_hs), latex(x),
                             latex(y), latex(n_hs - x), latex(y),
                             latex(z),
                             latex(n_hs), latex(z), latex(n_hs - z), latex(x), 
                             da, da, latex(da_val)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

