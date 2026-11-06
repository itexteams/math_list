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


def bt_dang6_p4_b5_c2_hh10(self):
            # Khai báo biến
            i=randint(-3,3)
            if i==0:
                i=randint(-3,3)

            lis0=['A','B','C','D','E','H','P','Q','M','N']
            d1=random.choice(lis0)
            lis0.remove(d1)
            d2=random.choice(lis0)
            lis0.remove(d2)
            d3=random.choice(lis0)
            lis0.remove(d3)
            d4=random.choice(lis0)

            lis1=[0,30,45,90,120,135,150,180]
            g11=random.choice(lis1)
            lis1.remove(g11)
            g12=random.choice(lis1)
            lis1.remove(g12)
            g13=random.choice(lis1)

            lis2=[90,30,45,60,0,135,150,180]
            g21=random.choice(lis2)
            lis2.remove(g21)
            g22=random.choice(lis2)
            lis2.remove(g22)
            g23=random.choice(lis2)

            lis3=[30,45,60,120,135,150,0,180]
            g31=random.choice(lis3)
            lis3.remove(g31)
            g32=random.choice(lis3)
            lis3.remove(g32)
            g33=random.choice(lis3)

            lis4=[90,30,180,60,45,135,150,0]
            g41=random.choice(lis4)
            lis4.remove(g41)
            g42=random.choice(lis4)
            lis4.remove(g42)
            g43=random.choice(lis4)

            lis5=[90,135,180,60,120,0,150,45]
            g51=random.choice(lis5)
            lis5.remove(g51)
            g52=random.choice(lis5)
            lis5.remove(g52)
            g53=random.choice(lis5)

            lis6=[90,135,180,60,120,0,30,45]
            g61=random.choice(lis6)
            lis6.remove(g61)
            g62=random.choice(lis6)
            lis6.remove(g62)
            g63=random.choice(lis6)


            lisdang=['1','2','3','4','5','6']
            dang=random.choice(lisdang)
            if dang=='6':

                # Nội dung câu hỏi
                noidungcauhoi =('Cho tam giác đều $%s%s%s$ có tâm $O$, $I$ là trung điểm của $%s%s$. Tính số đo góc $\\left( \\overrightarrow{O%s} ,\\overrightarrow{%s%s} \\right)$.'
                                %(str(d1),str(d2),str(d3),str(d2),str(d3), str(d1),str(d1),str(d3)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Ta có \\\\ \n'
                        '$\\left( \\overrightarrow{O%s} ,\\overrightarrow{%s%s} \\right)=180^\\circ-30^\\circ=150^\\circ$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-3.5082521596683605,-2.324972514432068) rectangle (3.9337747347675935,3.9179238006678525);  \n'
                            '\\draw (0.,3.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (-2.598076211353316,-1.5)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (2.598076211353316,-1.5)-- (0.,3.);  \n'
                            '\\draw (0.,3.)-- (0.,-1.5);  \n'
                            '\\draw (0.,0.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (0.,0.)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (0,3.53) node[anchor=north] {%s};  \n'
                            '\\draw (-2.8,-1.5) node[anchor=north west] {%s};  \n'
                            '\\draw (2.6,-1.5) node[anchor=north west] {%s};  \n'
                            '\\draw (0,0.5) node[anchor=north west] {O};  \n'
                            '\\draw (-0.03448213087018273,-1.632690942856631) node[anchor=north] {I};  \n'
                        '\\end{tikzpicture}  \n'
                        '} \n'

                        %(str(d1),str(d1),str(d3),
                        str(d1),str(d2),str(d3),
                        ))



            if dang=='5':

                # Nội dung câu hỏi
                noidungcauhoi =('Cho tam giác đều $%s%s%s$ có tâm $O$, $I$ là trung điểm của $%s%s$. Tính số đo góc $\\left( \\overrightarrow{%sO} ,\\overrightarrow{%s%s} \\right)$.'
                                %(str(d1),str(d2),str(d3),str(d2),str(d3), str(d1),str(d1),str(d3)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Ta có \\\\ \n'
                        '$\\left( \\overrightarrow{%sO} ,\\overrightarrow{%s%s} \\right)=\\widehat{O%s%s}=30^\\circ$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-3.5082521596683605,-2.324972514432068) rectangle (3.9337747347675935,3.9179238006678525);  \n'
                            '\\draw (0.,3.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (-2.598076211353316,-1.5)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (2.598076211353316,-1.5)-- (0.,3.);  \n'
                            '\\draw (0.,3.)-- (0.,-1.5);  \n'
                            '\\draw (0.,0.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (0.,0.)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (0,3.53) node[anchor=north] {%s};  \n'
                            '\\draw (-2.8,-1.5) node[anchor=north west] {%s};  \n'
                            '\\draw (2.6,-1.5) node[anchor=north west] {%s};  \n'
                            '\\draw (0,0.5) node[anchor=north west] {O};  \n'
                            '\\draw (-0.03448213087018273,-1.632690942856631) node[anchor=north] {I};  \n'
                        '\\end{tikzpicture}  \n'
                        '} \n'

                        %(str(d1),str(d1),str(d3),str(d1),str(d3),
                        str(d1),str(d2),str(d3),
                        ))


            if dang=='4':

                # Nội dung câu hỏi
                noidungcauhoi =  ('Cho tam giác đều $%s%s%s$ có tâm $O$, $I$ là trung điểm của $%s%s$. Tính số đo góc $\\left( \\overrightarrow{O%s} ,\\overrightarrow{O%s} \\right)$.'
                                %(str(d1),str(d2),str(d3),str(d2),str(d3), str(d2),str(d3)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Ta có \\\\ \n'
                        '$\\left( \\overrightarrow{O%s} ,\\overrightarrow{O%s} \\right)=\\widehat{%sO%s}=120^\\circ$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-3.5082521596683605,-2.324972514432068) rectangle (3.9337747347675935,3.9179238006678525);  \n'
                            '\\draw (0.,3.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (-2.598076211353316,-1.5)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (2.598076211353316,-1.5)-- (0.,3.);  \n'
                            '\\draw (0.,3.)-- (0.,-1.5);  \n'
                            '\\draw (0.,0.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (0.,0.)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (0,3.53) node[anchor=north] {%s};  \n'
                            '\\draw (-2.8,-1.5) node[anchor=north west] {%s};  \n'
                            '\\draw (2.6,-1.5) node[anchor=north west] {%s};  \n'
                            '\\draw (0,0.5) node[anchor=north west] {O};  \n'
                            '\\draw (-0.03448213087018273,-1.632690942856631) node[anchor=north] {I};  \n'
                        '\\end{tikzpicture}  \n'
                        '} \n'

                        %(str(d2),str(d3),str(d2),str(d3),
                        str(d1),str(d2),str(d3),
                        ))


            if dang=='3':

                # Nội dung câu hỏi

                noidungcauhoi = ('Cho tam giác đều $%s%s%s$ có tâm $O$, $I$ là trung điểm của $%s%s$. Tính số đo góc $\\left( \\overrightarrow{I%s} ,\\overrightarrow{I%s} \\right)$.'
                                %(str(d1),str(d2),str(d3),str(d2),str(d3), str(d1),str(d2)
                                ))

                # Nội dung lời giải
                loigiai =('\\immini{ \n'
                        'Ta có \\\\ \n'
                        '$\\left( \\overrightarrow{I%s} ,\\overrightarrow{I%s} \\right)=\\widehat{%sI%s}=90^\\circ$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-3.5082521596683605,-2.324972514432068) rectangle (3.9337747347675935,3.9179238006678525);  \n'
                            '\\draw (0.,3.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (-2.598076211353316,-1.5)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (2.598076211353316,-1.5)-- (0.,3.);  \n'
                            '\\draw (0.,3.)-- (0.,-1.5);  \n'
                            '\\draw (0.,0.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (0.,0.)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (0,3.53) node[anchor=north] {%s};  \n'
                            '\\draw (-2.8,-1.5) node[anchor=north west] {%s};  \n'
                            '\\draw (2.6,-1.5) node[anchor=north west] {%s};  \n'
                            '\\draw (0,0.5) node[anchor=north west] {O};  \n'
                            '\\draw (-0.03448213087018273,-1.632690942856631) node[anchor=north] {I};  \n'
                        '\\end{tikzpicture}  \n'
                        '} \n'

                        %(str(d1),str(d2),str(d1),str(d2),
                        str(d1),str(d2),str(d3),
                        ))


            if dang=='2':

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tam giác đều $%s%s%s$ có tâm $O$, $I$ là trung điểm của $%s%s$. Tính số đo góc $\\left( \\overrightarrow{%s%s} ,\\overrightarrow{%s%s} \\right)$.'
                                %(str(d1),str(d2),str(d3),str(d2),str(d3), str(d2),str(d3),str(d3),str(d1)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Ta có \\\\ \n'
                        '$\\left( \\overrightarrow{%s%s} ,\\overrightarrow{%s%s} \\right)=180^\\circ-60^\\circ=120^\\circ$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-3.5082521596683605,-2.324972514432068) rectangle (3.9337747347675935,3.9179238006678525);  \n'
                            '\\draw (0.,3.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (-2.598076211353316,-1.5)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (2.598076211353316,-1.5)-- (0.,3.);  \n'
                            '\\draw (0.,3.)-- (0.,-1.5);  \n'
                            '\\draw (0.,0.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (0.,0.)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (0,3.53) node[anchor=north] {%s};  \n'
                            '\\draw (-2.8,-1.5) node[anchor=north west] {%s};  \n'
                            '\\draw (2.6,-1.5) node[anchor=north west] {%s};  \n'
                            '\\draw (0,0.5) node[anchor=north west] {O};  \n'
                            '\\draw (-0.03448213087018273,-1.632690942856631) node[anchor=north] {I};  \n'
                        '\\end{tikzpicture}  \n'
                        '} \n'

                        %(str(d2),str(d3),str(d3),str(d1),
                        str(d1),str(d2),str(d3),
                        ))


            if dang=='1':

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tam giác đều $%s%s%s$ có tâm $O$, $I$ là trung điểm của $%s%s$. Tính số đo góc $\\left( \\overrightarrow{%s%s} ,\\overrightarrow{%s%s} \\right)$.'
                                %(str(d1),str(d2),str(d3),str(d2),str(d3),str(d1),str(d2),str(d1),str(d3)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Ta có \\\\ \n'
                        '$\\left( \\overrightarrow{%s%s} ,\\overrightarrow{%s%s} \\right)=\\widehat{%s%s%s}=60^\\circ$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-3.5082521596683605,-2.324972514432068) rectangle (3.9337747347675935,3.9179238006678525);  \n'
                            '\\draw (0.,3.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (-2.598076211353316,-1.5)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (2.598076211353316,-1.5)-- (0.,3.);  \n'
                            '\\draw (0.,3.)-- (0.,-1.5);  \n'
                            '\\draw (0.,0.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (0.,0.)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (0,3.53) node[anchor=north] {%s};  \n'
                            '\\draw (-2.8,-1.5) node[anchor=north west] {%s};  \n'
                            '\\draw (2.6,-1.5) node[anchor=north west] {%s};  \n'
                            '\\draw (0,0.5) node[anchor=north west] {O};  \n'
                            '\\draw (-0.03448213087018273,-1.632690942856631) node[anchor=north] {I};  \n'
                        '\\end{tikzpicture}  \n'
                        '} \n'

                        %(str(d1),str(d2),str(d1),str(d3),str(d2),str(d1),str(d3),
                        str(d1),str(d2),str(d3),
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

