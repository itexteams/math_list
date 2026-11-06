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


def bt_dang4_p4_b1_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','7']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                m=symbols('m')
                a=randint(4,10)
                b=randint(4,10)

                f=(m*x+a)/(b*x+m)
                fdh=(m**2-a*b)/((b*x+m)**2)

                # Xác định khoảng giá trị
                start = -sqrt(a*b)+0.0001
                end = sqrt(a*b)-0.0001

                # Lấy số nguyên gần nhất
                start_int = math.ceil(start)  # Lấy giá trị nguyên lớn hơn hoặc bằng -3.4
                end_int = math.floor(end)    # Lấy giá trị nguyên nhỏ hơn hoặc bằng 5.6

                # Tính số lượng số nguyên trong khoảng
                kq = end_int - start_int + 1
                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$, với $m$ là tham số. Gọi $S$ là tập hợp tất cả các giá trị nguyên của $m$ để hàm số nghịch biến trên từng khoảng xác định của nó. Số phần tử của $S$ bằng bao nhiêu?'
                                %(latex(f))
                                )

                # Nội dung lời giải
                loigiai = ('Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$;  $y\'=%s$. \\\\ \n' #2
                        'Để hàm số nghịch biến trên từng khoảng xác định của nó thì $m^2-%s<0 \\Leftrightarrow %s<m<%s$. \\\\ \n' #3
                        'Với $m\\in\\mathbb{Z}$ nên $S$ có $%s$ phần tử.' #6
                            %(latex(-m/b),latex(fdh),
                            latex(a*b),latex(-sqrt(a*b)),latex(sqrt(a*b)),
                            latex(kq),)
                            )

                #Đáp án


            if dang=='2':
                x=symbols('x')
                m=symbols('m')
                a=randint(4,10)
                b=randint(4,10)

                f=(-m*x-a)/(-b*x-m)
                fdh=(m**2-a*b)/((-b*x-m)**2)
                # Xác định khoảng giá trị
                start = -sqrt(a*b)+0.0001
                end = sqrt(a*b)-0.0001

                # Lấy số nguyên gần nhất
                start_int = math.ceil(start)  # Lấy giá trị nguyên lớn hơn hoặc bằng -3.4
                end_int = math.floor(end)    # Lấy giá trị nguyên nhỏ hơn hoặc bằng 5.6

                # Tính số lượng số nguyên trong khoảng
                kq = end_int - start_int + 1
                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$, với $m$ là tham số. Gọi $S$ là tập hợp tất cả các giá trị nguyên của $m$ để hàm số nghịch biến trên từng khoảng xác định của nó. Số phần tử của $S$ bằng bao nhiêu?'
                                %(latex(f))
                                )

                # Nội dung lời giải
                loigiai = ('Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. $y\'=%s$. \\\\ \n' #2
                        'Để hàm số nghịch biến trên từng khoảng xác định của nó thì $m^2-%s<0 \\Leftrightarrow %s<m<%s$. \\\\ \n' #3
                        'Với $m\\in\\mathbb{Z}$ nên $S$ có $%s$ phần tử.' #6
                            %(latex(-m/b),latex(fdh),
                            latex(a*b),latex(-sqrt(a*b)),latex(sqrt(a*b)),
                            latex(kq),)
                            )

                #Đáp án


            if dang=='3':
                x=symbols('x')
                m=symbols('m')
                a=randint(4,10)
                b=randint(4,10)

                f=(m*x-a)/(b*x-m)
                fdh=(-m**2+a*b)/((b*x-m)**2)
                # Xác định khoảng giá trị
                start = -sqrt(a*b)+0.0001
                end = sqrt(a*b)-0.0001

                # Lấy số nguyên gần nhất
                start_int = math.ceil(start)  # Lấy giá trị nguyên lớn hơn hoặc bằng -3.4
                end_int = math.floor(end)    # Lấy giá trị nguyên nhỏ hơn hoặc bằng 5.6

                # Tính số lượng số nguyên trong khoảng
                kq = end_int - start_int + 1
                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$, với $m$ là tham số. Gọi $S$ là tập hợp tất cả các giá trị nguyên của $m$ để hàm số đồng biến trên từng khoảng xác định của nó. Số phần tử của $S$ bằng bao nhiêu?'
                                %(latex(f))
                                )

                # Nội dung lời giải
                loigiai = ('Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. $y\'=%s$. \\\\ \n' #2
                        'Để hàm số đồng biến trên từng khoảng xác định của nó thì $-m^2+%s>0 \\Leftrightarrow %s<m<%s$. \\\\ \n' #3
                        'Với $m\\in\\mathbb{Z}$ nên $S$ có $%s$ phần tử.' #6
                            %(latex(m/b),latex(fdh),
                            latex(a*b),latex(-sqrt(a*b)),latex(sqrt(a*b)),
                            latex(kq),)
                            )

                #Đáp án


            if dang=='4':
                x=symbols('x')
                m=symbols('m')
                a=randint(4,10)
                b=randint(4,10)

                f=(m*x+a)/(-b*x-m)
                fdh=(-m**2+a*b)/((-b*x-m)**2)
                # Xác định khoảng giá trị
                start = -sqrt(a*b)+0.0001
                end = sqrt(a*b)-0.0001

                # Lấy số nguyên gần nhất
                start_int = math.ceil(start)  # Lấy giá trị nguyên lớn hơn hoặc bằng -3.4
                end_int = math.floor(end)    # Lấy giá trị nguyên nhỏ hơn hoặc bằng 5.6

                # Tính số lượng số nguyên trong khoảng
                kq = end_int - start_int + 1
                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$, với $m$ là tham số. Gọi $S$ là tập hợp tất cả các giá trị nguyên của $m$ để hàm số đồng biến trên từng khoảng xác định của nó. Số phần tử của $S$ bằng bao nhiêu?'
                                %(latex(f))
                                )

                # Nội dung lời giải
                loigiai = ('Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. $y\'=%s$. \\\\ \n' #2
                        'Để hàm số đồng biến trên từng khoảng xác định của nó thì $-m^2+%s>0 \\Leftrightarrow %s<m<%s$. \\\\ \n' #3
                        'Với $m\\in\\mathbb{Z}$ nên $S$ có $%s$ phần tử.' #6
                            %(latex(-m/b),latex(fdh),
                            latex(a*b),latex(-sqrt(a*b)),latex(sqrt(a*b)),
                            latex(kq),)
                            )

                #Đáp án


            if dang=='5':
                x=symbols('x')
                m=symbols('m')
                a=randint(4,15)
                b=randint(4,10)

                f=(-m*x+a)/(-b*x+m)
                fdh=(-m**2+a*b)/((-b*x+m)**2)
                # Xác định khoảng giá trị
                start = -sqrt(a*b)+0.0001
                end = sqrt(a*b)-0.0001

                # Lấy số nguyên gần nhất
                start_int = math.ceil(start)  # Lấy giá trị nguyên lớn hơn hoặc bằng -3.4
                end_int = math.floor(end)    # Lấy giá trị nguyên nhỏ hơn hoặc bằng 5.6

                # Tính số lượng số nguyên trong khoảng
                kq = end_int - start_int + 1
                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$, với $m$ là tham số. Gọi $S$ là tập hợp tất cả các giá trị nguyên của $m$ để hàm số đồng biến trên từng khoảng xác định của nó. Số phần tử của $S$ bằng bao nhiêu?'
                                %(latex(f))
                                )

                # Nội dung lời giải
                loigiai = ('Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. $y\'=%s$. \\\\ \n' #2
                        'Để hàm số đồng biến trên từng khoảng xác định của nó thì $-m^2+%s>0 \\Leftrightarrow %s<m<%s$. \\\\ \n' #3
                        'Với $m\\in\\mathbb{Z}$ nên $S$ có $%s$ phần tử.' #6
                            %(latex(m/b),latex(fdh),
                            latex(a*b),latex(-sqrt(a*b)),latex(sqrt(a*b)),
                            latex(kq),)
                            )

                #Đáp án


            if dang=='7':
                x=symbols('x')
                m=symbols('m')
                a=randint(4,15)
                b=randint(4,10)
                c=randint(4,10)

                f=(a*x+m**2)/(b*x+c)
                fdh=(-b*m**2+a*c)/((b*x+c)**2)
                x0=Rational(a*c,b)
                # Xác định khoảng giá trị
                start = -sqrt(x0)+0.0001
                end = sqrt(x0)-0.0001

                # Lấy số nguyên gần nhất
                start_int = math.ceil(start)  # Lấy giá trị nguyên lớn hơn hoặc bằng -3.4
                end_int = math.floor(end)    # Lấy giá trị nguyên nhỏ hơn hoặc bằng 5.6

                # Tính số lượng số nguyên trong khoảng
                kq = end_int - start_int + 1
                # Nội dung câu hỏi
                noidungcauhoi = ('Có bao nhiêu giá trị nguyên của tham số $m$ để hàm số $y=%s$ đồng biến trên từng khoảng xác định của nó?'
                                %(latex(f))
                                )

                # Nội dung lời giải
                loigiai = ('Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. $y\'=%s$. \\\\ \n' #2
                        'Để hàm số đồng biến trên từng khoảng xác định của nó thì $-%sm^2+%s>0 \\Leftrightarrow -\\sqrt{%s}<m<\\sqrt{%s}$. \\\\ \n' #3
                        'Với $m\\in\\mathbb{Z}$ nên $S$ có $%s$ phần tử.' #6
                            %(latex(Rational(-c,b)),latex(fdh),
                            latex(b),latex(a*c),latex(x0),latex(x0),
                            latex(kq),)
                            )

                #Đáp án


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content  

