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


def bt_dang3_p3_b2_c1_ds10(self):
            #Khai báo biến
            a = randint(2,9) # b là số bất kỳ từ 1 đến 30
            b = randint(2,9) # b là số bất kỳ từ 1 đến 30
            c = randint(2,9) # b là số bất kỳ từ 1 đến 30
            d = randint(2,9) # b là số bất kỳ từ 1 đến 30
            e = randint(2,9) # b là số bất kỳ từ 1 đến 30
            f = randint(2,9) # b là số bất kỳ từ 1 đến 30
            t = randint(3,9)
            x0=t
            list1=['Toán','Văn','Hóa']
            list2=['Sử','Địa','Lý']
            list3=['Tin','Tiếng Anh']
            list4=[2,-2]
            rd1 = random.choice(list1)
            rd2 = random.choice(list2)
            rd3 = random.choice(list3)
            rd4 = random.choice(list4)
            list3=['dang1','dang2']
            rd = random.choice(list3)

            lisdang=['2']
            dang=random.choice(lisdang)
            if dang=='1':

                # Nội dung câu hỏi
                noidungcauhoi =('''Lớp $10A$ có $%s$ học sinh trong đó có $%s$ em học giỏi môn %s, $%s$ em học giỏi môn %s, $%s$ em học giỏi môn %s,
                            $%s$ em học giỏi cả môn %s và môn %s, $%s$ em học giỏi cả môn %s và môn %s, $%s$ em học giỏi cả môn %s và môn %s.
                            Biết rằng mỗi học sinh trong lớp học giỏi ít nhất một trong $3$ môn %s, %s, %s. Hỏi lớp $10A$ có bao nhiêu bạn học giỏi cả ba môn %s, %s, %s.?\\\\'''
                            %(latex(a+b+c+d+e+f+t),latex(t+d+f+a),str(rd1),latex(t+d+e+b),str(rd2),latex(t+e+f+c),str(rd3),
                            latex(t+d),str(rd1),str(rd2),latex(t+e),str(rd2),str(rd3),latex(t+f),str(rd1),str(rd3),
                            str(rd1),str(rd2),str(rd3),str(rd1),str(rd2),str(rd3)))

                # Nội dung lời giải
                loigiai = ('Gọi\\\\ \n'
                    '$x$ là số học sinh chỉ giỏi %s;\\\\ \n'
                    '$y$  là số học sinh chỉ giỏi %s;\\\\ \n'
                    '$z$  là số học sinh chỉ giỏi %s;\\\\ \n'
                    '$a$  là số học sinh chỉ giỏi %s và %s;\\\\ \n'
                    '$b$  là số học sinh chỉ giỏi %s và %s;\\\\ \n'
                    '$c$  là số học sinh chỉ giỏi %s và %s;\\\\ \n'
                    '$d$  là số học sinh giỏi cả $3$ môn. \\\\ \n'
                    'Theo đề ra ta có hệ phương trình:'
                    '$\\heva{& x+a+c+d=%s\\\\& y+a+b+d=%s\\\\& z+b+c+d=%s\\\\& a+d=%s\\\\& b+d=%s\\\\& c+d=%s\\\\& x+y+z+a+b+c+d=%s}$\\\\ \n'
                    'Giải hệ ta được $d=%s$ nên số học sinh giỏi cả $3$ môn là $%s$ học sinh.'
                    %(str(rd1),str(rd2),str(rd3),str(rd1),str(rd2),str(rd2),str(rd3),str(rd1),str(rd3),
                    latex(t+d+f+a),latex(t+d+e+b),latex(t+e+f+c),latex(t+d),latex(t+e),latex(t+f),latex(a+b+c+d+e+f+t),latex(t),latex(t)))
                hinhve =('	\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick,scale=1.5]\n'
                    '\\draw[black] (0,0) circle (1cm);\n'
                    '\\node at (-0.5,0.2) {$x$};\n'
                    '\\draw[black] (1,0) circle (1cm);\n'
                    '\\node at (1.5,0.2) {$y$};\n'
                    '\\draw[black] (0.5,-1) circle (1cm);\n'
                    '\\node at (0.5,-1.5) {$z$};\n'
                    '\\node at (0.5,0.4) {$a$};\n'
                    '\\node at (1,-0.7) {$b$};\n'
                    '\\node at (-0.2,-0.7) {$c$};\n'
                    '\\node at (0.5,-0.4) {$d$};\n'
                    '\\begin{scope}\n'
                        '\\clip (0,0) circle (1cm);\n'
                        '\\clip (1,0) circle (1cm);\n'
                        '\\clip (0.5,-1) circle (1cm);\n'
                        '\\fill[pattern=north east lines, pattern color=black] (1,0) circle (1cm);\n'
                        '\\fill[pattern=north east lines, pattern color=black] (0,0) circle (1cm);\n'
                        '\\fill[pattern=north east lines, pattern color=black] (0.5,-1) circle (1cm);\n'
                        '\\draw[black] (1,0) circle (1cm);\n'
                        '\\draw[black] (0,0) circle (1cm);\n'			
                        '\\draw[black] (0.5,-1) circle (1cm);\n'
                    '\\end{scope}\n'
                '\\end{tikzpicture} \n'        )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(x0))

            if dang=='2':

                # Nội dung câu hỏi
                noidungcauhoi =('''Trong lớp $10A$ có $%s$ em học giỏi môn %s, $%s$ em học giỏi môn %s, $%s$ em học giỏi môn %s,
                            $%s$ em học giỏi cả môn %s và môn %s, $%s$ em học giỏi cả môn %s và môn %s, $%s$ em học giỏi cả môn %s và môn %s,
                            có $%s$ bạn học giỏi cả ba môn %s, %s, %s. Biết rằng mỗi học sinh trong lớp học giỏi ít nhất một trong $3$ môn %s, %s, %s. Hỏi Lớp $10A$ có bao nhiêu học sinh?'''
                            %(latex(t+d+f+a),str(rd1),latex(t+d+e+b),str(rd2),latex(t+e+f+c),str(rd3),
                            latex(t+d),str(rd1),str(rd2),latex(t+e),str(rd2),str(rd3),latex(t+f),str(rd1),str(rd3),
                            latex(t),str(rd1),str(rd2),str(rd3),str(rd1),str(rd2),str(rd3)))

                # Nội dung lời giải
                loigiai = ('Gọi\\\\ \n'
                    '$x$ là số học sinh chỉ giỏi %s;\\\\ \n'
                    '$y$  là số học sinh chỉ giỏi %s;\\\\ \n'
                    '$z$  là số học sinh chỉ giỏi %s;\\\\ \n'
                    '$a$  là số học sinh chỉ giỏi %s và %s;\\\\ \n'
                    '$b$  là số học sinh chỉ giỏi %s và %s;\\\\ \n'
                    '$c$  là số học sinh chỉ giỏi %s và %s;\\\\ \n'
                    '$d$  là số học sinh giỏi cả $3$ môn. \\\\ \n'
                    'Theo đề ra ta có hệ phương trình:'
                    '$\\heva{& x+a+c+d=%s\\\\& y+a+b+d=%s\\\\& z+b+c+d=%s\\\\& a+d=%s\\\\& b+d=%s\\\\& c+d=%s\\\\& d=%s}$\\\\ \n'
                    'Giải hệ ta được $x+y+z+a+b+c+d=%s$ nên số học sinh lớp $10A$ là $%s$ học sinh.'
                    %(str(rd1),str(rd2),str(rd3),str(rd1),str(rd2),str(rd2),str(rd3),str(rd1),str(rd3),
                    latex(t+d+f+a),latex(t+d+e+b),latex(t+e+f+c),latex(t+d),latex(t+e),latex(t+f),latex(t),latex(a+b+c+d+e+f+t),latex(a+b+c+d+e+f+t)))
                hinhve =('	\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick,scale=1.5]\n'
                    '\\draw[black] (0,0) circle (1cm);\n'
                    '\\node at (-0.5,0.2) {$x$};\n'
                    '\\draw[black] (1,0) circle (1cm);\n'
                    '\\node at (1.5,0.2) {$y$};\n'
                    '\\draw[black] (0.5,-1) circle (1cm);\n'
                    '\\node at (0.5,-1.5) {$z$};\n'
                    '\\node at (0.5,0.4) {$a$};\n'
                    '\\node at (1,-0.7) {$b$};\n'
                    '\\node at (-0.2,-0.7) {$c$};\n'
                    '\\node at (0.5,-0.4) {$d$};\n'
                    '\\begin{scope}\n'
                        '\\clip (0,0) circle (1cm);\n'
                        '\\clip (1,0) circle (1cm);\n'
                        '\\clip (0.5,-1) circle (1cm);\n'
                        '\\fill[pattern=north east lines, pattern color=black] (1,0) circle (1cm);\n'
                        '\\fill[pattern=north east lines, pattern color=black] (0,0) circle (1cm);\n'
                        '\\fill[pattern=north east lines, pattern color=black] (0.5,-1) circle (1cm);\n'
                        '\\draw[black] (1,0) circle (1cm);\n'
                        '\\draw[black] (0,0) circle (1cm);\n'			
                        '\\draw[black] (0.5,-1) circle (1cm);\n'
                    '\\end{scope}\n'
                '\\end{tikzpicture} \n'        )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(a+b+c+d+e+f+t))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{\\immini{'+str(loigiai)+'}\n{'+str(hinhve)+'}}'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

