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


def bt_dang5_p4_b3_c4_ds10(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(1,9)
                d=randint(-9,9)
                e=randint(-9,9)
                while a==0 or d==0 or a+2>=b-1:
                    x=symbols('x')
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(1,9)
                    d=randint(1,9)
                    e=randint(1,9)

                fx=x**2-(a+b)*x+a*b
                gx=d*x+e
                hx=(a-c*d)*x + (b-c*e)

                # Xác định khoảng giá trị
                start = a+0.5
                end = b-0.5

                # Lấy số nguyên gần nhất
                start_int = math.ceil(start)  # Lấy giá trị nguyên lớn hơn hoặc bằng -3.4
                end_int = math.floor(end)    # Lấy giá trị nguyên nhỏ hơn hoặc bằng 5.6

                # Tính số lượng số nguyên trong khoảng
                kq = end_int - start_int + 1

                # Câu hỏi
                noidungcauhoi = ('Tìm số nghiệm nguyên của bất phương trình $%s< 0$.'
                                %(latex(fx)))

                # Nội dung lời giải
                loigiai=('Đặt $f(x)=%s$.\\\\ \n'
                    'Ta có $f(x)=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{& x=%s \\\\&x=%s}$. \\\\ \n'
                        'Hệ số $a=1>0$ nên $f(x)< 0 \\Leftrightarrow x\\in (%s;%s)$.\\\\ \n'
                        'Vậy số nghiệm nguyên của bất phương trình là $%s$.'

                        %(latex(fx),
                            latex(fx),latex(a),latex(b),
                        latex(a),latex(b),
                        latex(kq),)
                        )


            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(1,9)
                d=randint(-9,9)
                e=randint(-9,9)
                while a==0 or d==0 or a>=b-1:
                    x=symbols('x')
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(1,9)
                    d=randint(1,9)
                    e=randint(1,9)

                fx=x**2-(a+b)*x+a*b
                gx=d*x+e
                hx=(a-c*d)*x + (b-c*e)

                # Xác định khoảng giá trị
                start = a
                end = b

                # Lấy số nguyên gần nhất
                start_int = math.ceil(start)  # Lấy giá trị nguyên lớn hơn hoặc bằng -3.4
                end_int = math.floor(end)    # Lấy giá trị nguyên nhỏ hơn hoặc bằng 5.6

                # Tính số lượng số nguyên trong khoảng
                kq = end_int - start_int + 1

                # Câu hỏi
                noidungcauhoi = ('Tìm số nghiệm nguyên của bất phương trình $%s\\le 0$.'
                                %(latex(fx)))

                # Nội dung lời giải
                loigiai=('Đặt $f(x)=%s$.\\\\ \n'
                    'Ta có $f(x)=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{& x=%s \\\\&x=%s}$. \\\\ \n'
                        'Hệ số $a=1>0$ nên $f(x)\\le0 \\Leftrightarrow x\\in [%s;%s]$.\\\\ \n'
                        'Vậy số nghiệm nguyên của bất phương trình là $%s$.'

                        %(latex(fx),
                            latex(fx),latex(a),latex(b),
                        latex(a),latex(b),
                        latex(kq),)
                        )


            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(1,9)
                d=randint(-9,9)
                e=randint(-9,9)
                while a==0 or d==0 or a+2>=b-1:
                    x=symbols('x')
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(1,9)
                    d=randint(1,9)
                    e=randint(1,9)

                fx=-x**2+(a+b)*x-a*b
                gx=d*x+e
                hx=(a-c*d)*x + (b-c*e)
                # Xác định khoảng giá trị
                start = a+0.5
                end = b-0.5

                # Lấy số nguyên gần nhất
                start_int = math.ceil(start)  # Lấy giá trị nguyên lớn hơn hoặc bằng -3.4
                end_int = math.floor(end)    # Lấy giá trị nguyên nhỏ hơn hoặc bằng 5.6

                # Tính số lượng số nguyên trong khoảng
                kq = end_int - start_int + 1

                # Câu hỏi
                noidungcauhoi = ('Tìm số nghiệm nguyên của bất phương trình $%s> 0$.'
                                %(latex(fx)))

                # Nội dung lời giải
                loigiai=('Đặt $f(x)=%s$.\\\\ \n'
                    'Ta có $f(x)=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{& x=%s \\\\&x=%s}$. \\\\ \n'
                        'Hệ số $a=-1<0$ nên $f(x)> 0\\Leftrightarrow x\\in (%s;%s)$.\\\\ \n'
                        'Vậy số nghiệm nguyên của bất phương trình là $%s$.'

                        %(latex(fx),
                            latex(fx),latex(a),latex(b),
                        latex(a),latex(b),
                        latex(kq),)
                        )


            if dang=='4':
                # Khai báo biến
                x=symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(1,9)
                d=randint(-9,9)
                e=randint(-9,9)
                while a==0 or d==0 or a+1>=b:
                    x=symbols('x')
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(1,9)
                    d=randint(1,9)
                    e=randint(1,9)

                fx=-x**2+(a+b)*x-a*b
                gx=d*x+e
                hx=(a-c*d)*x + (b-c*e)
                # Xác định khoảng giá trị
                start = a
                end = b

                # Lấy số nguyên gần nhất
                start_int = math.ceil(start)  # Lấy giá trị nguyên lớn hơn hoặc bằng -3.4
                end_int = math.floor(end)    # Lấy giá trị nguyên nhỏ hơn hoặc bằng 5.6

                # Tính số lượng số nguyên trong khoảng
                kq = end_int - start_int + 1
                # Câu hỏi
                noidungcauhoi = ('Tìm số nghiệm nguyên của bất phương trình $%s\\ge 0$.'
                                %(latex(fx)))

                # Nội dung lời giải
                loigiai=('Đặt $f(x)=%s$.\\\\ \n'
                    'Ta có $f(x)=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{& x=%s \\\\&x=%s}$. \\\\ \n'
                        'Hệ số $a=-1<0$ nên $f(x)\\ge 0 \\Leftrightarrow x\\in [%s;%s]$.\\\\ \n'
                        'Vậy số nghiệm nguyên của bất phương trình là $%s$.'

                        %(latex(fx),
                            latex(fx),latex(a),latex(b),
                        latex(a),latex(b),
                        latex(kq),)
                        )


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('--', '+').replace('21\\vec', '21f\\vec').replace('51\\vec', '51f\\vec').replace('81\\vec', '81f\\vec').replace('1\\vec', '\\vec').replace('21f\\vec', '21\\vec').replace('51f\\vec', '51\\vec').replace('81f\\vec', '81\\vec')
            return content

