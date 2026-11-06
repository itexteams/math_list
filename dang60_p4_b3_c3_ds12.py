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


def bt_dang60_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Cấu trúc: y = k*x^2 + p*x + q và y = k*x^4 + p*x + q
            # Để diện tích đẹp và giống mẫu, ta giữ nguyên các nghiệm giao điểm là -1, 0, 1
            k = random.randint(1, 5) # Hệ số nhân để thay đổi kết quả
            p = random.randint(-5, 5) # Hệ số của x
            q = random.randint(-5, 5) # Hệ số tự do

            f1 = k*x**2 + p*x + q
            f2 = k*x**4 + p*x + q

            # Phương trình hoành độ giao điểm: k*x^2 - k*x^4 = 0 <=> x = 0, x = 1, x = -1
            # Diện tích S = k * 4/15
            S_val = Rational(4 * k, 15)

            # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
            da_dung = '$%s$' % latex(S_val)

            # Tạo danh sách đáp án sai
            s = []
            list_sai_candidates = [
                Rational(2 * k, 15), 
                Rational(8 * k, 15), 
                Rational(4 * k, 5), 
                Rational(k, 15), 
                Rational(7 * k, 15), 
                Rational(4 * k, 3)
            ]

            for item in list_sai_candidates:
                if item != S_val:
                    s.append('$%s$' % latex(item))

            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # B2: Viết lại nội dung câu hỏi (sử dụng \text{d}x theo yêu cầu)
            noidungcauhoi = (r'Tính diện tích hình phẳng được giới hạn bởi các đường $y = %s$ và $y = %s$.'
                             % (latex(f1), latex(f2)))

            # Các đáp án
            da_d = ('\\True ' + str(da_dung))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết (Bám sát mẫu hình ảnh)
            # Hiệu hai hàm số: (k*x^2 + px + q) - (k*x^4 + px + q) = k(x^2 - x^4)
            diff = f1 - f2
            loigiai = (r'''Phương trình hoành độ giao điểm của $y = %s$ và $y = %s$ là \\
                $ %s = %s \Leftrightarrow %s = 0 \Leftrightarrow \left[\begin{aligned} &x = 0 \\ &x = 1 \\ &x = -1 \end{aligned}\right. $ \\
                Diện tích hình phẳng cần tìm là \\
                $S = \int_{-1}^{1} \left| %s \right| \text{d}x = \int_{-1}^{0} \left| %s \right| \text{d}x + \int_{0}^{1} \left| %s \right| \text{d}x$ \\
                $= \left| \int_{-1}^{0} \left( %s \right) \text{d}x \right| + \left| \int_{0}^{1} \left( %s \right) \text{d}x \right| \\ = \left| \left( %s \right) \bigg|_{-1}^{0} \right| + \left| \left( %s \right) \bigg|_{0}^{1} \right| \\ = %s + %s = %s.$'''
                % (latex(f1), latex(f2), 
                   latex(f1), latex(f2), latex(diff),
                   latex(diff), latex(diff), latex(diff),
                   latex(diff), latex(diff),
                   latex(integrate(diff, x)), latex(integrate(diff, x)),
                   latex(abs(integrate(diff, (x, -1, 0)))), 
                   latex(abs(integrate(diff, (x, 0, 1)))), 
                   latex(S_val)
                  ))

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

