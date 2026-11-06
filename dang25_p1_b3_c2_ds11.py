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


def bt_dang25_p1_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số k cho quan hệ x = ky
                k = random.randint(2, 5)

                # Tạo các hệ số cho Cấp số cộng (AP) sao cho x = ky
                # Cần (a1 + a3 - 2*a2) = -1 và (b1 + b3 - 2*b2) = k
                a1 = random.randint(1, 4)
                a2 = random.randint(3, 6)
                a3 = 2 * a2 - a1 - 1

                b2 = random.randint(2, 5)
                b1 = random.randint(1, 5)
                b3 = 2 * b2 - b1 + k

                # Tạo các hằng số cho Cấp số nhân (GP)
                c1 = random.randint(1, 6)
                c2 = random.randint(1, 5)

                # Hàm format để in ra biểu thức đẹp mắt (không in 1x, 1y)
                def fmt(a, b):
                    s_a = "x" if a == 1 else "%sx" % a
                    s_b = "y" if b == 1 else "%sy" % b
                    return "%s + %s" % (s_a, s_b)

                ap1_str = fmt(a1, b1)
                ap2_str = fmt(a2, b2)
                ap3_str = fmt(a3, b3)

                gp1_str = "x - %s" % c1
                gp2_str = "y + %s" % c2
                gp3_str = "x - %sy" % k

                # Tính toán kết quả thực tế
                y_val = -c2
                x_val = k * y_val
                ans = x_val**2 + y_val**2

                # Tạo các đáp án nhiễu
                pool = [
                    c2**2 * (k**2 - 1),
                    c2**2 * (k + 1)**2,
                    ans + 15,
                    ans - 15,
                    ans + 5,
                    c1**2 * (k**2 + 1)
                ]

                # Lọc đáp án nhiễu để đảm bảo dương và không trùng đáp án đúng
                pool = list(set([val for val in pool if val != ans and val > 0]))
                random.shuffle(pool)

                # Các đáp án trắc nghiệm
                da = '$x^2 + y^2 = %s$' % ans
                das1 = '$x^2 + y^2 = %s$' % pool[0]
                das2 = '$x^2 + y^2 = %s$' % pool[1]
                das3 = '$x^2 + y^2 = %s$' % pool[2]

                # Câu hỏi
                noidungcauhoi = ('''Các số $%s$, $%s$, $%s$ theo thứ tự đó lập thành một cấp số cộng; đồng thời các số $%s$, $%s$, $%s$ theo thứ tự đó lập thành một cấp số nhân. Giá trị $x^2 + y^2$ bằng'''
                                 % (ap1_str, ap2_str, ap3_str, gp1_str, gp2_str, gp3_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Các số $%s$, $%s$, $%s$ theo thứ tự đó lập thành một cấp số cộng nên ta có: \\\\
                             $(%s) + (%s) = 2(%s) \\Leftrightarrow %sx + %sy = %sx + %sy \\Leftrightarrow x = %sy$. (1) \\\\
                             Các số $%s$, $%s$, $%s$ theo thứ tự đó lập thành một cấp số nhân nên ta có: \\\\
                             $(%s)^2 = (%s)(%s)$. (2) \\\\
                             Thay (1) vào (2) ta được: \\\\
                             $(y + %s)^2 = (%sy - %s)(%sy - %sy) \\Leftrightarrow (y + %s)^2 = 0 \\Leftrightarrow y = %s$. \\\\
                             Với $y = %s$, suy ra $x = %s$. \\\\
                             Vậy $x^2 + y^2 = (%s)^2 + (%s)^2 = %s$.'''
                             % (ap1_str, ap2_str, ap3_str,
                                ap1_str, ap3_str, ap2_str, 
                                a1 + a3, b1 + b3, 2 * a2, 2 * b2, k,
                                gp1_str, gp2_str, gp3_str,
                                gp2_str, gp1_str, gp3_str,
                                c2, k, c1, k, k, c2, y_val,
                                y_val, x_val,
                                x_val, y_val, ans))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

