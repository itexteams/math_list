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


def bt_dang9_p4_b2_c6_ds10(self):
            #Khai báo biến
            a = randint(5,20) # a là số bất kỳ từ -9 đến 9
            b = randint(7,20) # b là số bất kỳ từ -9 đến 9
            c= randint(2,7) # b là số bất kỳ từ -9 đến 9
            if c>a:
                c= randint(2,4) # b là số bất kỳ từ -9 đến 9
            T=a+b
            def combinations_count(T, c):
                return math.factorial(T) // (math.factorial(T - c) * math.factorial(c))
            def combinations_count(a, c):
                return math.factorial(a) // (math.factorial(a - c) * math.factorial(c))
            def combinations_count(b, c):
                return math.factorial(b) // (math.factorial(b - c) * math.factorial(c))
            x1=combinations_count(T, c)# Không gian mẫu
            x2=combinations_count(a, c)# Số cách chọn bi đỏ
            x3=combinations_count(b, c)# số cách chọn bi xanh
            x4=Rational(x3,x1) # Xác xuất biến cố đối
            x0=1-x4
            n1=Rational(1,127)
            n2=Rational(1,19)
            n3=Rational(1,15)
            list1= ['viên bi','bông hoa','chiếc thẻ','quả cầu','quả bóng','cái kẹo','chiếc bút']
            rd = random.choice(list1)
            #Nội dung câu hỏi
            noidungcauhoi = '''Từ một hộp có $%s$ %s đỏ và $%s$ %s xanh. Lấy ngẫu nhiên $%s$ %s. Tính xác suất để lấy được ít nhất $1$ %s màu đỏ.'''%(latex(a),str(rd),latex(b),str(rd),latex(c),str(rd),str(rd))
            # Các đáp án
            da_d = '\\True$%s$' %(latex(x0))
            da_s1 = '$%s$' %(latex(x0-n1))
            da_s2 = '$%s$' %(latex(x0+n2))
            da_s3 = '$%s$' %(latex(x0+n3))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải 
            loigiai=('Tổng số %s trong hộp là $%s+%s=%s$.  \\\\ \n'
                'Số cách lấy ngẫu nhiên $%s$ %s từ hộp là một tổ hợp chập $%s$ của $%s$ phần tử. \\\\ \n'
                    '      $n(\\Omega)=\\mathrm{C}_{%s}^{%s}=%s$.\\\\ \n'
                    'Gọi $A$ là biến cố "Lấy được ít nhất $%s$ %s đỏ". \\\\ \n'
                    'Khi đó $\\overline{A}$ là biến cố "Cả $%s$ %s lấy được đều màu xanh" và $n(\\overline{A})=\\mathrm{C}_{%s}^{%s}=%s$.\\\\ \n'
                    'Khi đó $\\mathrm{P}(\\overline{A})=\\dfrac{n(\\overline{A})}{n(\\Omega)}=%s$. \\\\ \n'
                    'Vậy $\\mathrm{P}(A)=1-\\mathrm{P}(\\overline{A})=1-%s=%s$.'
                    %(str(rd),latex(a),latex(b),latex(a+b),
                    latex(c),str(rd),latex(c),latex(a+b),
                    latex(a+b),latex(c),latex(x1),
                    latex(c),str(rd),
                    latex(c),str(rd),latex(b),latex(c),latex(x3),
                    latex(x4),
                    latex(x4),latex(x0)))
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','').replace('\\frac','\\dfrac').replace('+-','-').replace('++','+')  
            return content 

