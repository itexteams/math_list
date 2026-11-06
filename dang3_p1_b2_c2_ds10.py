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


def bt_dang3_p1_b2_c2_ds10(self):
            #Khai báo biến
            a1 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            b1 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            c1 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            a2 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            b2 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            c2 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            a3 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            b3 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            c3 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            x1 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            y1 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            x2 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            y2 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            x3 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            y3 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            x4 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            y4 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            x5 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            y5 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            x6 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            y6 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            while a1*x1+b1*y1>c1 or a2*x1+b2*y1<c2 or a3*x1+b3*y1>c3 or a1*x4+b1*y4<c1 or a2*x5+b2*y5>c2 or a3*x6+b3*y6<c3 or a1==0 or b1==0 or a2==0 or b2==0 or a3==0 or b3==0:
                a1 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                b1 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                c1 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                a2 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                b2 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                c2 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                a3 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                b3 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                c3 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                x1 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                y1 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                x2 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                y2 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                x3 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                y3 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                x4 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                y4 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                x5 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                y5 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                x6 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
                y6 = randint(-9,9) # b là số bất kỳ từ 1 đến 30
            list3=['dang1','dang2','dang3']
            rd = random.choice(list3)
            #Nội ung câu hỏi
            if rd=='dang1':
                noidungcauhoi = ('''Miền nghiệm của hệ bất phương trình $\\heva{& %sx+%sy<%s\\\\& %sx+%sy>%s\\\\& %sx+%sy<%s}$ chứa điểm nào sau đây \n'''
                            %(latex(a1),latex(b1),latex(c1),latex(a2),latex(b2),latex(c2),latex(a3),latex(b3),latex(c3)))
            # Các đáp án
                da_d = '\\True $(%s;%s)$'%(latex(x1),latex(y1))
                da_s1 = '$(%s;%s)$'%(latex(x4),latex(y4))
                da_s2 = '$(%s;%s)$'%(latex(x5),latex(y5))
                da_s3 = '$(%s;%s)$'%(latex(x6),latex(y6))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Cặp số $(%s;%s)$ thỏa mãn tất cả các bất phương trình trong hệ nên thuộc miền nghiệm của hệ đã cho.' %(latex(x1),latex(y1)))
            if rd=='dang2':
                noidungcauhoi = ('''Miền nghiệm của hệ bất phương trình $\\heva{& %sx+%sy-%s>0\\\\& %sx+%sy-%s<0\\\\& %sx+%sy-%s<0}$ chứa điểm nào sau đây \n'''
                            %(latex(a2),latex(b2),latex(c2),latex(a1),latex(b1),latex(c1),latex(a3),latex(b3),latex(c3)))
            # Các đáp án
                da_d = '\\True $(%s;%s)$'%(latex(x1),latex(y1))
                da_s1 = '$(%s;%s)$'%(latex(x4),latex(y4))
                da_s2 = '$(%s;%s)$'%(latex(x5),latex(y5))
                da_s3 = '$(%s;%s)$'%(latex(x6),latex(y6))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Cặp số $(%s;%s)$ thỏa mãn tất cả các bất phương trình trong hệ nên thuộc miền nghiệm của hệ đã cho.' %(latex(x1),latex(y1)))
            if rd=='dang3':
                noidungcauhoi = ('''Miền nghiệm của hệ bất phương trình $\\heva{& %sx+%sy<%s\\\\& %sx+%sy-%s<0\\\\& %sx+%sy>%s}$ chứa điểm nào sau đây \n'''
                            %(latex(a3),latex(b3),latex(c3),latex(a1),latex(b1),latex(c1),latex(a2),latex(b2),latex(c2)))
            # Các đáp án
                da_d = '\\True $(%s;%s)$'%(latex(x1),latex(y1))
                da_s1 = '$(%s;%s)$'%(latex(x4),latex(y4))
                da_s2 = '$(%s;%s)$'%(latex(x5),latex(y5))
                da_s3 = '$(%s;%s)$'%(latex(x6),latex(y6))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Cặp số $(%s;%s)$ thỏa mãn tất cả các bất phương trình trong hệ nên thuộc miền nghiệm của hệ đã cho.' %(latex(x1),latex(y1)))
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','+').replace('\\frac','\\dfrac').replace('+-','-').replace('++','+').replace('-1x','-x').replace('1x','x').replace('-1y','-y').replace('1y','y').replace('-+','-'). replace('0y','0'). replace('+0',''). replace('-0',''). replace('+0','')
            return content

