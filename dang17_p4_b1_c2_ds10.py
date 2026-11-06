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


def bt_dang17_p4_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random giá tiền hoa cúc từ 3000 đến 6000 đồng (bước 1000)
                gia_cuc = randint(3, 6) * 1000
                # Random giá tiền hoa hồng từ 7000 đến 9000 đồng (bước 1000)
                gia_hong = randint(7, 9) * 1000

                # Random tổng số tiền mang đi từ 80000 đến 150000 đồng (bước 5000)
                tong_tien = randint(16, 30) * 5000

                # Tính toán các hệ số rút gọn khi chia cho 1000
                a = gia_cuc // 1000
                b = gia_hong // 1000
                c = tong_tien // 1000

                # Đáp án đúng
                da_dung = '$%sx + %sy \\le %s$' % (latex(a), latex(b), latex(c))

                # Tạo danh sách các phương án sai và lọc trùng để đảm bảo tính phân biệt
                s = []
                s.append('$%sx + %sy \\ge %s$' % (latex(a), latex(b), latex(c)))
                s.append('$%sx + %sy \\le %s$' % (latex(gia_cuc // 100), latex(gia_hong // 100), latex(c)))
                s.append('$%sx + %sy > %s$' % (latex(gia_cuc // 100), latex(gia_hong // 100), latex(c)))
                s.append('$%sx + %sy < %s$' % (latex(a), latex(b), latex(c)))

                if a != b:
                    s.append('$%sx + %sy \\le %s$' % (latex(b), latex(a), latex(c)))

                # Lọc các phần tử trùng với đáp án đúng
                s = [item for item in s if item != da_dung]
                s_distinct = list(set(s))
                random.shuffle(s_distinct)

                das1 = s_distinct[0]
                das2 = s_distinct[1]
                das3 = s_distinct[2]

                # Câu hỏi
                noidungcauhoi = ('''Hà mang $%s$ đồng ra chợ mua hoa cúc và hoa hồng. Một bông hoa cúc có giá $%s$ đồng, một bông hoa hồng có giá $%s$ đồng. Lập bất phương trình bậc nhất hai ẩn biểu diễn số tiền mà Hà phải chi để mua $x$ bông hoa cúc và $y$ bông hoa hồng.'''
                                 % (latex(tong_tien), latex(gia_cuc), latex(gia_hong)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Số tiền Hà dùng để mua $x$ bông hoa cúc và $y$ bông hoa hồng là $%sx + %sy$.\\\\
                             Mà Hà mang $%s$ đồng nên ta có: $%sx + %sy \\le %s \\Leftrightarrow %sx + %sy \\le %s$.'''
                           % (latex(gia_cuc), latex(gia_hong), latex(tong_tien), 
                              latex(gia_cuc), latex(gia_hong), latex(tong_tien),
                              latex(a), latex(b), latex(c)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

