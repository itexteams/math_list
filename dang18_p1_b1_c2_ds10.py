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


def bt_dang18_p1_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random giá tiền bút bi từ 2 đến 5 nghìn đồng
                gia_but = randint(2, 5)
                # Random giá tiền vở sao cho lớn hơn giá bút và tạo hệ số rút gọn đẹp
                # Chọn bội số để chia hết hoặc tối giản dễ dàng
                gia_vo = gia_but * randint(2, 4) 

                # Random tổng số tiền (nghìn đồng) chia hết cho gia_but để biểu thức thu gọn đẹp mắt
                # Ví dụ: từ 50 nghìn đến 200 nghìn đồng
                tong_tien = gia_but * randint(20, 50)

                # Rút gọn hệ số của bất phương trình: gia_but * x + gia_vo * y <= tong_tien
                ucln = math.gcd(math.gcd(gia_but, gia_vo), tong_tien)

                a = gia_but // ucln
                b = gia_vo // ucln
                c = tong_tien // ucln

                # Đáp án đúng
                da_dung = '$%sx + %sy \\le %s$' % (latex(a), latex(b), latex(c))

                # Tạo danh sách các phương án sai và lọc trùng
                s = []
                s.append('$%sx + %sy < %s$' % (latex(a), latex(b), latex(c)))
                s.append('$%sx + %sy \\ge %s$' % (latex(a), latex(b), latex(c)))
                s.append('$%sx + %sy > %s$' % (latex(a), latex(b), latex(c)))

                if a != b:
                    s.append('$%sx + %sy \\le %s$' % (latex(b), latex(a), latex(c)))
                    s.append('$%sx + %sy \\ge %s$' % (latex(b), latex(a), latex(c)))

                s.append('$%sx + %sy \\le %s$' % (latex(a), latex(b), latex(c + 10)))

                # Lọc các phần tử trùng với đáp án đúng
                s = [item for item in s if item != da_dung]
                s_distinct = list(set(s))
                random.shuffle(s_distinct)

                das1 = s_distinct[0]
                das2 = s_distinct[1]
                das3 = s_distinct[2]

                # Câu hỏi
                noidungcauhoi = ('''Bạn Nga có $%s$ nghìn đồng để mua vở và bút bi. Nga mua $x$ cái bút bi với giá $%s$ nghìn đồng một bút và mua $y$ quyển vở với giá $%s$ nghìn đồng một quyển vở. Bất phương trình nào sau đây mô tả điều kiện ràng buộc đối với $x$ và $y$?'''
                                 % (latex(tong_tien), latex(gia_but), latex(gia_vo)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Số tiền mua $x$ cái bút bi là $%sx$ (nghìn đồng).\\\\
                             Số tiền mua $y$ quyển vở là $%sy$ (nghìn đồng).\\\\
                             Tổng số tiền Nga mua vở và bút bi là: $%sx + %sy$.\\\\
                             Vì Nga có $%s$ nghìn đồng nên ta có $%sx + %sy \\le %s \\Leftrightarrow %sx + %sy \\le %s$.'''
                           % (latex(gia_but), latex(gia_vo), latex(gia_but), latex(gia_vo),
                              latex(tong_tien), latex(gia_but), latex(gia_vo), latex(tong_tien),
                              latex(a), latex(b), latex(c)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace(' 1x', ' x').replace(' 1y', 'y').replace('+ 1y', 'y').replace('$1x', '$x')
            return content

