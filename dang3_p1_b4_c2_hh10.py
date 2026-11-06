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


def bt_dang3_p1_b4_c2_hh10(self):
            # Khai báo biến
            a=randint(-9,9)
            b=randint(-9,9)
            c=randint(-9,9)
            d=randint(-9,9)
            e=randint(-9,9)
            f=randint(-9,9)


            m=randint(-9,9)
            n=randint(-9,9)
            k=randint(-9,9)
            if m==0 or n==0 or k==0:
                m=randint(-9,9)
                n=randint(-9,9)
                k=randint(-9,9)

            i=randint(-3,3)
            if i==0:
                i=randint(-3,3)


            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='1':
                #Nội ung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, cho vectơ $\\vec{a} =(%s;%s)$ và $\\vec{b} =(%s;%s)$. Tọa độ vectơ $\\vec{u}=%s \\vec{a}+%s \\vec{b}$ là  \n'
                                %(latex(a),latex(b),latex(c),latex(d),latex(m),latex(n)
                                ))
                # Các đáp án
                da_d = '\\True $\\vec{u}=(%s;%s)$' %(latex(m*a+n*c),latex(m*b+n*d))
                da_s1 = '$\\vec{u}=(%s;%s)$' %(latex(m*a+n*c+i),latex(m*b+n*d))
                da_s2 = '$\\vec{u}=(%s;%s)$' %(latex(m*a+n*c),latex(m*b+n*d-i))
                da_s3 = '$\\vec{u}=(%s;%s)$' %(latex(m*a+n*c-2*i),latex(m*b+n*d))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n '
                        '$%s\\vec{a} =(%s;%s)$.\\\\ \n'
                        '$%s\\vec{b} =(%s;%s)$.\\\\ \n'
                        'Suy ra $\\vec{u}=%s \\vec{a}+%s \\vec{b} =(%s+%s;%s+%s)=(%s;%s)$.'
                        %(latex(m),latex(m*a),latex(m*b),
                        latex(n),latex(n*c),latex(n*d),
                        latex(m),latex(n),latex(m*a),latex(n*c),latex(m*b),latex(n*d),latex(m*a+n*c),latex(m*b+n*d)
                        ))
            if dang=='2':
                #Nội ung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, cho vectơ $\\vec{a} =(%s;%s)$, $\\vec{b} =(%s;%s)$ và $\\vec{c} =(%s;%s)$. Tọa độ vectơ $\\vec{u}=%s \\vec{a}+%s \\vec{b} +%s \\vec{c}$ là  \n'
                                %(latex(a),latex(b),latex(c),latex(d),latex(e),latex(f),latex(m),latex(n),latex(k)
                                ))
                # Các đáp án
                da_d = '\\True $\\vec{u}=(%s;%s)$' %(latex(m*a+n*c+k*e),latex(m*b+n*d+k*f))
                da_s1 = '$\\vec{u}=(%s;%s)$' %(latex(m*a+n*c+k*e-i),latex(m*b+n*d+k*f))
                da_s2 = '$\\vec{u}=(%s;%s)$' %(latex(m*a+n*c+k*e),latex(m*b+n*d+k*f+2*i))
                da_s3 = '$\\vec{u}=(%s;%s)$' %(latex(m*a+n*c+k*e+i),latex(m*b+n*d+k*f))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n '
                        '$%s\\vec{a} =(%s;%s)$.\\\\ \n'
                        '$%s\\vec{b} =(%s;%s)$.\\\\ \n'
                        '$%s\\vec{c} =(%s;%s)$.\\\\ \n'
                        'Suy ra $\\vec{u}=%s \\vec{a}+%s \\vec{b}+%s \\vec{c} =(%s+%s+%s;%s+%s+%s)=(%s;%s)$.'
                        %(latex(m),latex(m*a),latex(m*b),
                        latex(n),latex(n*c),latex(n*d),
                        latex(k),latex(k*e),latex(k*f),
                        latex(m),latex(n),latex(k),latex(m*a),latex(n*c),latex(k*e),latex(m*b),latex(n*d),latex(k*f),latex(m*a+n*c+k*e),latex(m*b+n*d+k*f)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-').replace('0 \\vec{a}', '').replace('0 \\vec{b}', '').replace('0 \\vec{c}', '').replace('1 \\vec{a}', '\\vec{a}').replace('1 \\vec{b}', '\\vec{b}').replace('1 \\vec{c}', '\\vec{c}').replace('-1 \\vec{a}', '-\\vec{a}').replace('-1 \\vec{c}', '-\\vec{c}').replace('-1 \\vec{a}', '-\\vec{a}')
            return content

