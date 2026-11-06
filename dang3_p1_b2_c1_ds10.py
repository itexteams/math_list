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


def bt_dang3_p1_b2_c1_ds10(self):
            #Khai báo biến
            x = symbols('x')
            a = randint(-5, 5)
            b = randint(-5, 5)
            while b == a:  # Chọn lại b nếu bằng a
                b = randint(-5, 5)
            c = randint(-5, 5)
            # Tạo biểu thức đa thức f(x)
            f = a * x**2 + b * x + c
            f1 = a * x**2 + b * x + c+1
            f2 = a * x**2 - b * x + c+2
            f3 = a * x**2 + b * x - c-1
            n = randint(3, 6)
            # Tạo tập hợp kết quả từ f(1) đến f(n)
            kq = {f.subs(x, i) for i in range(1, n + 1)}
            kq1 = {f1.subs(x, i) for i in range(1, n + 1)}
            kq2 = {f2.subs(x, i) for i in range(1, n + 1)}
            kq3 = {f3.subs(x, i) for i in range(1, n + 1)}
            lis1=['A','B','C','D','E','F','G','H']
            tap=random.choice(lis1)

            ds=set(range(1,n+1))
            #Nội dung câu hỏi
            noidungcauhoi = '''Cho tập hợp $%s=\\left \\lbrace %s | x \\in \\mathbb{N^*} , x \\le %s \\right \\rbrace$. Tập hợp $%s$ là \n''' %(str(tap),latex(f),latex(n),str(tap))
            # Các đáp án
            da_d = '\\True $%s=%s$' %(str(tap),latex(kq)) 
            da_s1 = '$%s=%s$' %(str(tap),latex(kq1)) 
            da_s2 = '$%s=%s$' %(str(tap),latex(kq2)) 
            da_s3 = '$%s=%s$' %(str(tap),latex(kq3))  
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=('Vì $x \\in \\mathbb{N^*} , x \\le %s$ nên $x \\in %s$. Ứng với mỗi giá trị của $x$ thay vào biểu thức $%s$ ta được tập hợp $%s=%s$. \\\\ \n'
                    %(latex(n),latex(ds),latex(f),str(tap),latex(kq))
                    )
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n') 
            return content

