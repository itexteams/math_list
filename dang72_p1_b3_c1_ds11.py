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


def bt_dang72_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thực hiện ngẫu nhiên hóa bằng cách chọn hệ số góc k của x (ví dụ: k = 2, k = 4, k = 6, ...)
                # Để giữ nguyên tập góc ban đầu nằm trong góc phần tư thứ I, ta chọn ngẫu nhiên trong tập hợp hợp lý.
                # Ví dụ chọn k = 2 (giống mẫu gốc) hoặc k = 4, k = 6 để khoảng của k*x luôn là dạng (0, m*pi/2) thuận tiện xét dấu.
                k = random.choice([2, 4])

                # Tính toán khoảng tương ứng của x và k*x
                # Với k = 2, x thuộc (0; pi/4) -> 2x thuộc (0; pi/2)
                # Với k = 4, x thuộc (0; pi/8) -> 4x thuộc (0; pi/2)
                if k == 2:
                    khoang_x = '\\left( 0; \\frac{\\pi}{4} \\right)'
                    khoang_kx = '\\left( 0; \\frac{\\pi}{2} \\right)'
                else:
                    khoang_x = '\\left( 0; \\frac{\\pi}{8} \\right)'
                    khoang_kx = '\\left( 0; \\frac{\\pi}{2} \\right)'

                goc_str = '%sx' % (latex(k))

                # Định nghĩa chuỗi cho các hàm số trong đề bài
                ham1_str = 'y = -\\sin %sx' % (latex(k))
                ham2_str = 'y = -1 + \\cos %sx' % (latex(k))

                # Câu hỏi sử dụng %s đúng cấu trúc mẫu
                noidungcauhoi = ('''Với $x \\in %s$, mệnh đề nào sau đây là đúng?''' % (str(khoang_x)))

                # Thiết lập các khẳng định trắc nghiệm (không chứa dấu chấm ở cuối phương án)
                da_d = ('\\True Cả hai hàm số $%s$ và $%s$ đều nghịch biến' % (str(ham1_str), str(ham2_str)))
                da_s1 = ('Cả hai hàm số $%s$ và $%s$ đều đồng biến' % (str(ham1_str), str(ham2_str)))
                da_s2 = ('Hàm số $%s$ nghịch biến, hàm số $%s$ đồng biến' % (str(ham1_str), str(ham2_str)))
                da_s3 = ('Hàm số $%s$ đồng biến, hàm số $%s$ nghịch biến' % (str(ham1_str), str(ham2_str)))

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo từng bước như ảnh gốc, sử dụng %s
                loigiai = ('''Ta có $x \\in %s \\rightarrow %s \\in %s$ thuộc góc phần tư thứ I. Do đó \\\\
                           Hàm số $y = \\sin %sx$ đồng biến nên $%s$ nghịch biến. \\\\
                           Hàm số $y = \\cos %sx$ nghịch biến nên $%s$ nghịch biến. \\\\
                           Vậy: Cả hai hàm số $%s$ và $%s$ đều nghịch biến.'''
                           % (str(khoang_x), str(goc_str), str(khoang_kx),
                              str(goc_str), str(ham1_str),
                              str(goc_str), str(ham2_str),
                              str(ham1_str), str(ham2_str)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

