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


def bt_dang10_p3_b2_c6_ds10(self):
            #Khai báo biến
            a = randint(5,10) # a là số bất kỳ từ -9 đến 9
            b = randint(7,11) # b là số bất kỳ từ -9 đến 9
            c= randint(3,7) # b là số bất kỳ từ -9 đến 9
            d=3
            T=a+b+c
            def combinations_count(T, d):
                return math.factorial(T) // (math.factorial(T - d) * math.factorial(d))
            x1=combinations_count(T, d)# Không gian mẫu
            x0=Rational(a*b*c,x1) # Xác suất 3 quả khác màu
            n1=Rational(1,127)
            n2=Rational(1,19)
            n3=Rational(1,15)
            list1= ['viên bi','bông hoa','chiếc thẻ','quả cầu','quả bóng','cái kẹo','chiếc bút']
            rd = random.choice(list1)
            #Nội dung câu hỏi
            noidungcauhoi = '''Từ một hộp có $%s$ %s đỏ và $%s$ %s xanh và $%s$ %s vàng, lấy ngẫu nhiên $3$ %s. Xác suất để lấy được $3$ %s màu khác nhau bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''%(latex(a),str(rd),latex(b),str(rd),latex(c),str(rd),str(rd),str(rd))
            # Các đáp án
            da_d = '\\True$%s$' %(latex(x0))
            da_s1 = '$%s$' %(latex(x0-n1))
            da_s2 = '$%s$' %(latex(x0+n2))
            da_s3 = '$%s$' %(latex(x0+n3))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải 
            h1=x0
            number = Decimal(float(h1))  # Số cần làm tròn
            kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kqz=str(kq1).replace('.', ',')
            loigiai=('Tổng số %s trong hộp là $%s+%s+%s=%s$.  \\\\ \n'
                'Số cách lấy ngẫu nhiên $3$ %s từ hộp là một tổ hợp chập $3$ của $%s$ phần tử. \\\\ \n'
                    'Số phần tử của không gian mẫu là $n(\\Omega)=\\mathrm{C}_{%s}^{%s}=%s$.\\\\ \n'
                    'Gọi $A$ là biến cố "Lấy được $3$ %s khác màu". Ta có: \\\\ \n'
                    'Số cách lấy $1$ %s từ $%s$ %s màu đỏ là $\\mathrm{C}_{%s}^{1}=%s$.\\\\ \n'
                    'Số cách lấy $1$ %s từ $%s$ %s màu xanh là $\\mathrm{C}_{%s}^{1}=%s$.\\\\ \n'
                    'Số cách lấy $1$ %s từ $%s$ %s màu vàng là $\\mathrm{C}_{%s}^{1}=%s$.\\\\ \n'
                    'Khi đó số phần tử của biến cố $A$ là $n(A)=%s \\cdot %s \\cdot %s=%s$. \\\\ \n'
                    'Vậy xác suất của biến cố $A$ là $\\mathrm{P}(A)=\\dfrac{n(A)}{n(\\Omega)}=\\dfrac{%s}{%s}=%s \\approx %s$.'
                    %(str(rd),latex(a),latex(b),latex(c),latex(a+b+c),
                    str(rd),latex(a+b+c),
                    latex(a+b+c),latex(3),latex(x1),
                    str(rd),
                    str(rd),latex(a),str(rd),latex(a),latex(a),
                    str(rd),latex(a),str(rd),latex(b),latex(b),
                    str(rd),latex(a),str(rd),latex(c),latex(c),
                    latex(a),latex(b),latex(c),latex(a*b*c),
                    latex(a*b*c),latex(x1),latex(x0),kqz))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','').replace('\\frac','\\dfrac').replace('+-','-').replace('++','+')  
            return content 

