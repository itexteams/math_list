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


def bt_dang3_p1_b2_c6_ds10(self):
            #Khai báo biến
            a = randint(5,12) # a là số bất kỳ từ -9 đến 9
            b = randint(7,15) # b là số bất kỳ từ -9 đến 9
            c= randint(2,7) # b là số bất kỳ từ -9 đến 9
            if c>a:
                c= randint(2,3) # b là số bất kỳ từ -9 đến 9
            T=a+b
            def combinations_count(T, c):
                return math.factorial(T) // (math.factorial(T - c) * math.factorial(c))
            def combinations_count(a, c):
                return math.factorial(a) // (math.factorial(a - c) * math.factorial(c))
            def combinations_count(b, c):
                return math.factorial(b) // (math.factorial(b - c) * math.factorial(c))
            x1=combinations_count(T, c)
            x2=combinations_count(a, c)
            x3=combinations_count(b, c)
            x0=Rational(x2+x3,x1)
            n1=Rational(1,127)
            n2=Rational(1,19)
            n3=Rational(1,15)
            lis1=['Toán','Vật lí','Hóa học','Sinh học','Tin học']
            sach1=random.choice(lis1)
            lis2=['Ngữ văn','Tiếng Anh','Lịch sử','Địa lí','Công nghệ']
            sach2=random.choice(lis2)
            #Nội dung câu hỏi
            noidungcauhoi = '''Trên kệ sách có $%s$ quyển sách %s và $%s$ quyển sách %s. Lấy ngẫu nhiên $%s$ quyển, xác suất của biến cố “$%s$ quyển sách được chọn cùng loại” là''' %(latex(a),str(sach1),latex(b),str(sach2),latex(c),latex(c))
            # Các đáp án
            da_d = '\\True$%s$' %(latex(x0))
            da_s1 = '$%s$' %(latex(x0-n1))
            da_s2 = '$%s$' %(latex(x0+n2))
            da_s3 = '$%s$' %(latex(x0+n3))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=( 'Gọi $A$ là biến cố "Lấy được $%s$ quyển sách cùng loại". \\\\ \n'
                    'Số cách chọn $%s$ quyển sách từ $%s$ quyển là tổ hợp chập $%s$ của $%s$ phần tử: $n(\\Omega)=\\mathrm{C}_{%s}^{%s}=%s$.\\\\ \n'
                    'Số cách lấy $%s$ quyển sách %s là tổ hợp chập $%s$ của $%s$ phần tử: $\\mathrm{C}_{%s}^{%s}$ = $%s$ .\\\\ \n'
                    'Số cách lấy $%s$ quyển sách %s là tổ hợp chập $%s$ của $%s$ phần tử: $\\mathrm{C}_{%s}^{%s}$ = $%s$. \\\\ \n'
                    'Do đó, số phần tử của biến cố $A$ là $n(A)=%s+%s$. \\\\ \n'
                    'Vậy xác suất của biến cố $A$ là $\\mathrm{P}(A)=\\frac{%s+%s}{%s}=%s$.'
                    %(latex(c),latex(c),latex(a+b),latex(c),latex(a+b),latex(a+b),latex(c),
                    latex(x1),latex(c),str(sach1),latex(c),latex(a),latex(a),latex(c),
                    latex(x2),latex(c),str(sach2),latex(c),latex(b),latex(b),latex(c),
                    latex(x3),latex(x2),latex(x3),latex(x2),latex(x3),latex(x1),latex(x0)))
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac') 
            return content  

