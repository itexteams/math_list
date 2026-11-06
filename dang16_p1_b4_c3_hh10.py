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


def bt_dang16_p1_b4_c3_hh10(self):
            # Khai báo biến
            x = symbols("x")
            y = symbols('y')

            k = randint(1,5)
            a = 5*k
            b1 = [3*k,4*k]
            b = random.choice(b1)
            if b==3*k:
                c=4*k
            else:
                c=3*k 
            pt = Eq(x**2/a**2+y**2/b**2,1)
            lisx0=[a,-a,b,-b,c,-c]
            #x0 = randint(-a, a)
            x0=random.choice(lisx0)
            y0=Rational(b,a)*sqrt(a**2-x0**2)
            y1=Rational(b,a+1)*sqrt(a**2-x0**2)
            y2=Rational(b+1,a)*sqrt(a**2-x0**2)
            y3=Rational(b,a+2)*sqrt(a**2-x0**2)
            lis=['P','Q','C','D','M','N','F','G','I','K']
            diem=random.choice(lis)
            # Câu hỏi
            noidungcauhoi='''Trong mặt phẳng tọa độ $(Oxy)$, cho điểm $%s$ thuộc elip $(E):%s$ và có hoành độ bằng $%s$. Tọa độ của $%s$ là \n'''%(str(diem),latex(pt),latex(x0),str(diem))
            if x0==a or x0==-a:
                # Các đáp án
                da_d = '\\True $%s \\left(%s;%s\\right)$ ' %(str(diem),latex(x0),latex(y0))
                da_s1 = '$%s \\left(%s;%s\\right)$ ' %(str(diem),latex(x0),latex(y0-1))
                da_s2 = '$%s \\left(%s;%s\\right)$ ' %(str(diem),latex(x0),latex(y0+1))
                da_s3 = '$%s \\left(%s;%s\\right)$ ' %(str(diem),latex(x0),latex(y0+2))    

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Gọi tọa độ điểm $%s$ là $(x;y)$. \\\\ \n'
                        'Điểm $%s$ có hoành độ bằng $%s$ nên $x=%s$.\\\\ \n'
                        'Vì $%s$ thuộc $(E)$ nên ta có: $\\dfrac{(%s)^2}{%s}+\\dfrac{y^2}{%s}=1 \\Rightarrow y=%s$. \\\\ \n'
                        'Vậy điểm cần tìm là $%s \\left(%s;%s\\right)$.'
                        %(str(diem),str(diem),latex(x0),latex(x0),str(diem),latex(x0),latex(a**2),latex(b**2),latex(y0),
                        str(diem),latex(x0),latex(y0)
                        ))
            else:
                # Các đáp án
                da_d = '\\True $%s_1 \\left(%s;%s\\right)$ và $%s_2 \\left(%s;%s\\right)$' %(str(diem),latex(x0),latex(y0),str(diem),latex(x0),latex(-y0))
                da_s1 = '$%s_1 \\left(%s;%s\\right)$ và $%s_2 \\left(%s;%s\\right)$' %(str(diem),latex(x0),latex(y1),str(diem),latex(x0),latex(-y1))
                da_s2 = '$%s_1 \\left(%s;%s\\right)$ và $%s_2 \\left(%s;%s\\right)$' %(str(diem),latex(x0),latex(y2),str(diem),latex(x0),latex(-y2))
                da_s3 = '$%s_1 \\left(%s;%s\\right)$ và $%s_2 \\left(%s;%s\\right)$' %(str(diem),latex(x0),latex(y3),str(diem),latex(x0),latex(-y3))     

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Gọi tọa độ điểm $%s$ là $(x;y)$. \\\\ \n'
                        'Điểm $%s$ có hoành độ bằng $%s$ nên $x=%s$.\\\\ \n'
                        'Vì $%s$ thuộc $(E)$ nên ta có: $\\dfrac{(%s)^2}{%s}+\\dfrac{y^2}{%s}=1 \\Rightarrow y=%s$ hoặc $y=%s$. \\\\ \n'
                        'Vậy có hai trường hợp là $%s_1 \\left(%s;%s\\right)$ và $%s_2 \\left(%s;%s\\right)$.'
                        %(str(diem),str(diem),latex(x0),latex(x0),str(diem),latex(x0),latex(a**2),latex(b**2),latex(y0),latex(-y0),
                        str(diem),latex(x0),latex(y0),str(diem),latex(x0),latex(-y0)
                        ))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content 

