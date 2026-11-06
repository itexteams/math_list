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


def bt_dang2_p4_b1_c1_hh10(self):
            #Khai báo biến
            a = randint(1,6) # a là số bất kỳ từ 1 đến 25
            c = randint(-6,-1)
            b = randint(7,20)
            g = Rational(a,b)
            h = Rational(c,b)
            x0 = sqrt(1-g**2)
            x01 = sqrt(1-h**2)
            x1= Rational((b**2-a**2),(b**2))
            x2= Rational((b**2-c**2),(b**2))
            list3=['dang1','dang2','dang3','dang4']
            rd = random.choice(list3)
            #Nội ung câu hỏi
            if rd=='dang1':
                noidungcauhoi = ('''Cho $\\sin\\alpha=%s$, với $0^\\circ<\\alpha<90^\\circ$. Tính giá trị của $\\cos\\alpha$.'''
                            %(latex(g)))

            # Nội dung lời giải
                loigiai=('Ta có: $\\cos^2\\alpha=1-\\sin^2\\alpha\\Leftrightarrow \\cos^2\\alpha=1-\\left(%s\\right)^2=%s\\Leftrightarrow  \\cos\\alpha=\\pm %s$.\\\\ \n'
                    'Vì $0^\\circ<\\alpha<90^\\circ$ nên $\\cos\\alpha>0$. Vậy $\\cos\\alpha=%s$.\\\\ \n'
                    %(latex(g),latex(x1),latex(x0),latex(x0)))

            if rd=='dang2':
                noidungcauhoi = ('''Cho $\\sin\\alpha=%s$, với $90^\\circ<\\alpha<180^\\circ$. Tính giá trị của $\\cos\\alpha$.'''
                            %(latex(g)))

            # Nội dung lời giải
                loigiai=('Ta có: $\\sin^2\\alpha=1-\\cos^2\\alpha\\Leftrightarrow \\sin^2\\alpha=1-\\left(%s\\right)^2=%s\\Leftrightarrow \\sin\\alpha=\\pm %s$.\\\\ \n'
                    'Vì $90^\\circ<\\alpha<180^\\circ$ nên $\\cos\\alpha<0$. Vậy $\\cos\\alpha=-%s$.\\\\ \n'
                    %(latex(g),latex(x1),latex(x0),latex(x0)))

            if rd=='dang3':
                noidungcauhoi = ('''Cho $\\cos\\alpha=%s$, với $0^\\circ<\\alpha<90^\\circ$. Tính giá trị của $\\sin\\alpha$ là'''
                            %(latex(g)))

            # Nội dung lời giải
                loigiai=('Ta có: $\\sin^2\\alpha=1-\\cos^2\\alpha\\Leftrightarrow \\sin^2\\alpha=1-\\left(%s\\right)^2=%s\\Leftrightarrow \\sin\\alpha=\\pm %s$.\\\\ \n'
                    'Vì $0^\\circ<\\alpha<90^\\circ$ nên $\\sin\\alpha>0$. Vậy $\\sin\\alpha=%s$.\\\\ \n'
                    %(latex(g),latex(x1),latex(x0),latex(x0)))

            if rd=='dang4':
                noidungcauhoi = ('''Cho $\\cos\\alpha=%s$, với $90^\\circ<\\alpha<180^\\circ$. Tính giá trị của $\\sin\\alpha$ là'''
                            %(latex(h)))

            # Nội dung lời giải
                loigiai=('Ta có: $\\sin^2\\alpha=1-\\cos^2\\alpha\\Leftrightarrow \\sin^2\\alpha=1-\\left(%s\\right)^2=%s\\Leftrightarrow \\sin\\alpha=\\pm %s$.\\\\ \n'
                    'Vì $90^\\circ<\\alpha<180^\\circ$ nên $\\sin\\alpha>0$. Vậy $\\sin\\alpha=%s$.\\\\ \n'
                    %(latex(h),latex(x2),latex(x01),latex(x01)))
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content   

