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


def bt_dang48_p1_b2_c7_ds11(self):
            # Khai báo biến
            # Khởi tạo biến ký hiệu
            x = symbols('x')

            # Bước 1: Định nghĩa hàm số gốc
            f = sqrt(tan(x) + cot(x))

            # Bước 2: Tạo điểm x0 ngẫu nhiên để bài toán phong phú (mặc định trong ảnh là pi/4)
            # Ở đây ta chọn các giá trị đẹp để kết quả không quá phức tạp
            list_x0 = [pi/6, pi/4, pi/3]
            x0 = random.choice(list_x0)

            # Bước 3: Tính đạo hàm f'(x)
            f_prime = diff(f, x)

            # Tính giá trị cụ thể tại x0
            kq_tri = f_prime.subs(x, x0)

            # Chuyển đổi công thức đạo hàm sang dạng giống trong ảnh để trình bày lời giải
            # f'(x) = (tanx + cotx)' / (2 * sqrt(tanx + cotx))
            tu_so_dao_ham = "(1/\\cos^2 x - 1/\\sin^2 x)"
            mau_so_dao_ham = "2\\sqrt{\\tan x + \\cot x}"

            # Bước 4: Tạo các đáp án nhiễu
            da_dung = '$%s$' % latex(kq_tri)
            s = [
                '$1$', '$-1$', '$0$', '$\\sqrt{2}$', '$-\\sqrt{2}$', 
                '$\\frac{1}{2}$', '$-\\frac{1}{2}$', '$\\sqrt{3}$'
            ]

            # Loại bỏ đáp án đúng khỏi danh sách nhiễu nếu nó tồn tại
            if da_dung in s:
                s.remove(da_dung)

            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # --- Nội dung hiển thị ---

            noidungcauhoi = (r'Đạo hàm của hàm số $f(x) = \sqrt{\tan x + \cot x}$ tại điểm $x = %s$ bằng' 
                             % latex(x0))

            # Viết lại lời giải chi tiết theo mẫu hình ảnh
            loigiai = (r'''Ta có: $f'(x) = \frac{(\tan x + \cot x)'}{2\sqrt{\tan x + \cot x}} = \frac{\frac{1}{\cos^2 x} - \frac{1}{\sin^2 x}}{2\sqrt{\tan x + \cot x}}$ \\
                       $= \frac{\sin^2 x - \cos^2 x}{2\sin^2 x \cos^2 x \sqrt{\tan x + \cot x}} = \frac{-2\cos 2x}{\sin^2 2x \sqrt{\tan x + \cot x}}$. \\
                       Suy ra $f'\left(%s\right) = %s$.''' 
                       % (latex(x0), latex(kq_tri)))

            # Đưa các đáp án vào danh sách
            da_d = '\\True ' + da_dung
            list_1 = [da_d, das1, das2, das3]
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content

