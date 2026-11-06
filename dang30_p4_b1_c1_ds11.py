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


def bt_dang30_p4_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B1 & B3: Nghiên cứu đề bài và tìm cách random hằng số năm trong biểu thức của góc x
                nam_tren = random.randint(2024, 2030)
                nam_duoi = nam_tren - 1

                # Kết quả cuối cùng luôn luôn là một số nguyên không đổi: -1
                kq_nguyen = -1
                da = '$%s$' % (latex(kq_nguyen))

                # Phương án trắc nghiệm nhiễu (B4: Lọc trùng đảm bảo không trùng với đáp án đúng)
                s = [
                    '$%s$' % (latex(1)),
                    '$%s$' % (latex(0)),
                    '$%s$' % (latex(-2)),
                    '$%s$' % (latex(2)),
                    '$%s$' % (latex(Rational(1, 4))).replace('.', ','),
                    '$%s$' % (latex(Rational(-1, 4))).replace('.', ',')
                ]

                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # B2: Viết lại y hệt bài toán gồm đề bài (Sử dụng định dạng %s)
                noidungcauhoi = ('''Tính giá trị biểu thức $A = \\frac{(1 - \\tan^2 x)^2}{4\\tan^2 x} - \\frac{1}{4\\sin^2 x \\cos^2 x}$ khi $x = \\frac{%s\\pi}{%s}$.'''
                                 % (latex(nam_tren), latex(nam_duoi)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # B2: Viết lại nội dung lời giải chi tiết (Sử dụng định dạng %s, không viết tắt, xuống dòng dùng \\\\)
                loigiai = ('''Biến đổi số hạng thứ nhất của biểu thức bằng cách sử dụng mối liên hệ $\\tan x = \\frac{\\sin x}{\\cos x}$: \\\\
                           $\\frac{(1 - \\tan^2 x)^2}{4\\tan^2 x} = \\frac{\\left(1 - \\frac{\\sin^2 x}{\\cos^2 x}\\right)^2}{4 \\cdot \\frac{\\sin^2 x}{\\cos^2 x}} = \\frac{\\left(\\frac{\\cos^2 x - \\sin^2 x}{\\cos^2 x}\\right)^2}{\\frac{4\\sin^2 x}{\\cos^2 x}} = \\frac{(\\cos^2 x - \\sin^2 x)^2}{4\\sin^2 x \\cos^2 x}$. \\\\
                           Thay kết quả vừa biến đổi vào biểu thức $A$ ban đầu, ta có mẫu số chung: \\\\
                           $A = \\frac{(\\cos^2 x - \\sin^2 x)^2}{4\\sin^2 x \\cos^2 x} - \\frac{1}{4\\sin^2 x \\cos^2 x} = \\frac{(\\cos^2 x - \\sin^2 x)^2 - 1}{4\\sin^2 x \\cos^2 x}$. \\\\
                           Khai triển hằng đẳng thức tử số: \\\\
                           $(\\cos^2 x - \\sin^2 x)^2 = \\cos^4 x + \\sin^4 x - 2\\sin^2 x \\cos^2 x$. \\\\
                           Sử dụng công thức bổ trợ: $\\sin^4 x + \\cos^4 x = 1 - 2\\sin^2 x \\cos^2 x$, ta thu được: \\\\
                           $(\\cos^2 x - \\sin^2 x)^2 = 1 - 2\\sin^2 x \\cos^2 x - 2\\sin^2 x \\cos^2 x = 1 - 4\\sin^2 x \\cos^2 x$. \\\\
                           Khi đó tử số của $A$ trở thành: \\\\
                           $(1 - 4\\sin^2 x \\cos^2 x) - 1 = -4\\sin^2 x \\cos^2 x$. \\\\
                           Do đó, ta rút gọn được biểu thức $A$: \\\\
                           $A = \\frac{-4\\sin^2 x \\cos^2 x}{4\\sin^2 x \\cos^2 x} = -1$. \\\\
                           Vì biểu thức $A$ nhận giá trị hằng số bằng $-1$ với mọi hằng số góc $x$ thuộc tập xác định, nên tại hằng số góc $x = \\frac{%s\\pi}{%s}$ giá trị biểu thức $A$ bằng $-1$.'''
                           % (latex(nam_tren), latex(nam_duoi)))

            # Xuất câu trắc nghiệm đúng chuẩn cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

