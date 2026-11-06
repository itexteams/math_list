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


def bt_dang2_p3_b2_c1_ds10(self):
            # Khai báo biến
            a = randint(12,20) # a là số bất kỳ từ 1 đến 25
            b = randint(12,20) # b là số bất kỳ từ 1 đến 30
            c = randint(5,11) # a là số bất kỳ từ 1 đến 25
            d = randint(8,15) # b là số bất kỳ từ 1 đến 30
            x0=a+b-c+d
            e=[-2,2]
            rde = random.choice(e)
            list1=['Toán','Văn','Tiếng Anh']
            list2=['Sử','Địa','Lý','Hóa']
            rd1 = random.choice(list1)
            rd2 = random.choice(list2)
            #Nội ung câu hỏi
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':
                # Nội dung câu hỏi
                noidungcauhoi = ('''Một lớp có $%s$ học sinh giỏi %s, $%s$ học sinh giỏi %s, $%s$ học sinh giỏi cả môn %s và môn %s và có $%s$ học sinh không giỏi môn nào cả. Hỏi lớp đó có bao nhiêu học sinh?\n'''
                            %(latex(a),str(rd1),latex(b),str(rd2),latex(c),str(rd1),str(rd2),latex(d)))

                # Nội dung lời giải
                loigiai = ('\\begin{center} \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick,scale=1.2] \n'
                            '\\draw[] (0.3,-0.3) circle (1.4cm); \n'
                            '\\draw[] (1,0.2) circle (1.5cm); \n'
                            '\\draw[] (1,0) circle (2.3cm); \n'
                            '\\node at (-0.7,-0.6) {$%s$}; \n'
                            '\\node at (1.5,1) {$%s$}; \n'
                            '\\node at (2.0,-1.5) {$%s$}; \n'
                            '\\node at (0.7,0.2) {$%s$}; \n'
                            '\\begin{scope} \n'
                            '\\clip (0.3,-0.3) circle (1.4cm); \n'
                            '\\clip (1,0.2) circle (1.5cm); \n'
                            '\\draw[pattern=north east lines]  circle (2cm); \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture} \n'
                            '\\end{center} \n'

                            'Ta có:\\\\ \n'
                            'Số học sinh chỉ giỏi môn %s là $%s - %s = %s$ học sinh.\\\\ \n'
                            'Số học sinh chỉ giỏi môn %s là $%s -%s = %s$ học sinh.\\\\ \n'
                            'Số học sinh giỏi cả hai môn %s và %s là $%s$ học sinh.\\\\ \n'
                            'Số học sinh không giỏi môn nào là %s học sinh.\\\\ \n'
                            'Vậy tổng số học sinh của lớp là $%s + % s+ %s + %s= %s$ học sinh.'
                            %(str(a-c),str(b-c),str(d),str(c),
                            str(rd1),latex(a),latex(c),latex(a-c),
                            str(rd2),latex(b),latex(c),latex(b-c),
                            str(rd1),str(rd2),latex(c),latex(d),
                            latex(a-c),latex(b-c),latex(c),latex(d),latex(x0)
                                ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(x0))
            if dang=='2':
                # Nội dung câu hỏi
                noidungcauhoi = ('''Một lớp có %s học sinh, trong đó có $%s$ học sinh giỏi %s, $%s$ học sinh giỏi %s, và có $%s$ học sinh không giỏi môn nào cả. Hỏi lớp đó có bao nhiêu học sinh giỏi cả hai môn?\n'''
                            %(latex(x0),latex(a),str(rd1),latex(b),str(rd2),latex(d)))

                # Nội dung lời giải
                loigiai = ('\\begin{center} \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick,scale=1.2] \n'
                            '\\draw[] (0.3,-0.3) circle (1.4cm); \n'
                            '\\draw[] (1,0.2) circle (1.5cm); \n'
                            '\\draw[] (1,0) circle (2.3cm); \n'
                            '\\node at (-0.7,-0.6) {$%s$}; \n'
                            '\\node at (1.5,1) {$%s$}; \n'
                            '\\node at (2.0,-1.5) {$%s$}; \n'
                            '\\node at (0.7,0.2) {$%s$}; \n'
                            '\\begin{scope} \n'
                            '\\clip (0.3,-0.3) circle (1.4cm); \n'
                            '\\clip (1,0.2) circle (1.5cm); \n'
                            '\\draw[pattern=north east lines]  circle (2cm); \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture} \n'
                            '\\end{center} \n'

                            'Ta có:\\\\ \n'
                            'Số học sinh giỏi ít nhất một trong hai môn %s và %s là: $%s - %s = %s$ học sinh.\\\\ \n'
                            'Số học sinh giỏi cả hai môn %s và %s là: \\\\ \n'
                            ' $(%s + %s) - %s = %s$ học sinh.'
                            %(str(a-c),str(b-c),str(d),str(c),
                            str(rd1),str(rd2),latex(x0),latex(d),latex(x0-d),
                            str(rd1),str(rd2),latex(a),latex(b),latex(x0-d),latex(c)
                                ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(c))

            if dang=='3':
                # Nội dung câu hỏi
                noidungcauhoi = ('''Một lớp có %s học sinh, trong đó có $%s$ học sinh giỏi %s, $%s$ học sinh giỏi %s, $%s$ học sinh giỏi cả môn %s và môn %s. Hỏi lớp đó có bao nhiêu học sinh không giỏi môn nào cả?\n'''
                            %(latex(x0),latex(a),str(rd1),latex(b),str(rd2),latex(c),str(rd1),str(rd2)))

                # Nội dung lời giải
                loigiai = ('\\begin{center} \n'
                           '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick,scale=1.2] \n'
                            '\\draw[] (0.3,-0.3) circle (1.4cm); \n'
                            '\\draw[] (1,0.2) circle (1.5cm); \n'
                            '\\draw[] (1,0) circle (2.3cm); \n'
                            '\\node at (-0.7,-0.6) {$%s$}; \n'
                            '\\node at (1.5,1) {$%s$}; \n'
                            '\\node at (2.0,-1.5) {$%s$}; \n'
                            '\\node at (0.7,0.2) {$%s$}; \n'
                            '\\begin{scope} \n'
                            '\\clip (0.3,-0.3) circle (1.4cm); \n'
                            '\\clip (1,0.2) circle (1.5cm); \n'
                            '\\draw[pattern=north east lines]  circle (2cm); \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture} \n'
                            '\\end{center} \n'

                            'Ta có:\\\\ \n'
                            'Số học sinh chỉ giỏi môn %s là $%s - %s = %s$ học sinh.\\\\ \n'
                            'Số học sinh chỉ giỏi môn %s là $%s -%s = %s$ học sinh.\\\\ \n'
                            'Số học sinh giỏi cả hai môn %s và %s là $%s$ học sinh.\\\\ \n'
                            'Số học sinh không giỏi môn nào là $%s - %s - %s - %s = %s$ học sinh.'
                            %(str(a-c),str(b-c),str(d),str(c),
                            str(rd1),latex(a),latex(c),latex(a-c),
                            str(rd2),latex(b),latex(c),latex(b-c),
                            str(rd1),str(rd2),latex(c),
                            latex(x0),latex(a-c),latex(b-c),latex(c),latex(d)
                                ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(d))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content                                

