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


def bt_dang28_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            # Dãy nhiễu 1 (Cấp số cộng phân số giống phương án A)
            b = random.choice([2, 3, 4])
            a = randint(1, 3)
            d1 = randint(1, 3)
            s1_1, s1_2, s1_3, s1_4, s1_5 = a, a+d1, a+2*d1, a+3*d1, a+4*d1
            str_s1 = "\\frac{%s}{%s}; \\frac{%s}{%s}; \\frac{%s}{%s}; \\frac{%s}{%s}; \\frac{%s}{%s}" % (s1_1, b, s1_2, b, s1_3, b, s1_4, b, s1_5, b)

            # Dãy nhiễu 2 (Cấp số cộng hằng số giống phương án B)
            c = randint(1, 6)
            str_s2 = "%s; %s; %s; %s; %s" % (c, c, c, c, c)

            # Dãy nhiễu 3 (Cấp số cộng từ số âm giống phương án C)
            u_start = randint(-10, -5)
            d3 = randint(2, 4)
            s3_1, s3_2, s3_3, s3_4, s3_5 = u_start, u_start+d3, u_start+2*d3, u_start+3*d3, u_start+4*d3
            str_s3 = "%s; %s; %s; %s; %s" % (s3_1, s3_2, s3_3, s3_4, s3_5)

            # Dãy đúng (Không phải cấp số cộng giống phương án D)
            v1 = randint(3, 8)
            d4 = randint(2, 4)
            v2 = v1 - d4
            v3 = v2 - d4
            v4 = v3 - d4 + 1  # Làm sai lệch quy luật để không là cấp số cộng
            v5 = v4 - d4 - 1
            str_s4 = "%s; %s; %s; %s; %s" % (v1, v2, v3, v4, v5)

            # Tính các công sai giả để đưa vào lời giải
            diff1 = v2 - v1
            diff2 = v3 - v2
            diff3 = v4 - v3

            # Hàm phụ trợ format dấu ngoặc cho số âm trong phép trừ
            def f_num(n):
                if n < 0:
                    return '(%s)' % n
                return str(n)

            # Các đáp án trắc nghiệm
            da = '$%s$' % str_s4
            das1 = '$%s$' % str_s1
            das2 = '$%s$' % str_s2
            das3 = '$%s$' % str_s3

            # Câu hỏi
            noidungcauhoi = '%s' % ('Trong các dãy số sau, dãy số nào không phải cấp số cộng?')

            # Các đáp án
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ('''Xét dãy số $%s$: \\\\
            Ta có $u_2 - u_1 = %s - %s = %s$; \\\\
            $u_3 - u_2 = %s - %s = %s$; \\\\
            $u_4 - u_3 = %s - %s = %s$. \\\\
            Vì $u_4 - u_3 \\neq u_2 - u_1$ (do $%s \\neq %s$) nên dãy số này không phải là cấp số cộng. \\\\
            Các dãy số còn lại đều có hiệu hai số hạng liên tiếp là một hằng số nên chúng là các cấp số cộng.''' % (
                str_s4,
                v2, f_num(v1), diff1,
                v3, f_num(v2), diff2,
                v4, f_num(v3), diff3,
                diff3, diff1
            ))

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

