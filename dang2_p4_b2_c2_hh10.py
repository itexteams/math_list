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


def bt_dang2_p4_b2_c2_hh10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(2,10)
                lis0=[30,60]
                goc=random.choice(lis0)
                goc_rad=goc*pi/180

                bi=a/tan(goc_rad)
                bh=bi+a
                bd=sqrt(bh**2+a**2)
                x0=round(sqrt(bh**2+a**2),1)
                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình thang cân $ABCD$, có đáy nhỏ và đường cao cùng bằng $%s$ và góc $\\widehat{ABC}=%s^\\circ$$zz$ Tính độ dài $\\overrightarrow{x}=\\overrightarrow{CB}-\\overrightarrow{AD}+\\overrightarrow{AC}$$zz$ (kết quả làm tròn đến hàng phần chục)$zz$ \n'''
                            %(latex(a), latex(goc))
                            )

                # Nội dung lời giải
                loigiai = (
                        '\\begin{center} \n'    
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                                '\\clip(-2$zz$4778629644712598,-0$zz$626343833170012) rectangle (5$zz$654889254630042,3$zz$565473184644411); \n'
                                '\\draw (-2,0)-- (0,3); \n'
                                '\\draw (0,3)-- (3,3); \n'
                                '\\draw (3,3)-- (5,0); \n'
                                '\\draw (5,0)-- (-2,0); \n'
                                '\\draw (0,3)-- (0,0); \n'
                                '\\draw (3,3)-- (3,0); \n'
                                '\\draw (-2$zz$6151425103393733,0$zz$1576618434785709) node[anchor=north west] {$B$}; \n'
                                '\\draw (-0$zz$45128684278928387,3$zz$6504856854026187) node[anchor=north west] {$A$}; \n'
                                '\\draw (4$zz$842672212552968,0$zz$08902207054451423) node[anchor=north west] {$C$}; \n'
                                '\\draw (2$zz$999723363046841,3$zz$55501977562243) node[anchor=north west] {$D$}; \n'
                                '\\draw (-0$zz$30493911648154838,-0$zz$009592700873126778) node[anchor=north west] {$I$}; \n'
                                '\\draw (2$zz$553375636739105,-0$zz$051406336961051194) node[anchor=north west] {$H$}; \n'
                                '\\draw (-2,0)-- (3,3); \n'
                                '\\draw [shift={(-1$zz$8015774764683667,0$zz$030511625279132783)}] plot[domain=-0$zz$06888586909496919:1$zz$3236178474618479,variable=\\t]({1$zz$*0$zz$44328060302912903*cos(\\t r)+0$zz$*0$zz$44328060302912903*sin(\\t r)},{0$zz$*0$zz$44328060302912903*cos(\\t r)+1$zz$*0$zz$44328060302912903*sin(\\t r)}); \n'
                            '\\end{tikzpicture} \n'
                            '\\end{center} \n'

                        'Từ hình vẽ ta có \\\\ \n'
                        '\\hspace*{1cm}$\\tan %s^\\circ =\\dfrac{AI}{BI} \\Rightarrow BI=\\dfrac{%s}{\\tan %s^\\circ} =%s$$zz$\\\\ \n'
                        'Suy ra $BH=BI+IH=%s +%s =\\left( %s \\right) $$zz$\\\\ \n'
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm}$\\left| \\overrightarrow{x} \\right|=\\left| \\overrightarrow{CB}-\\overrightarrow{AD}+\\overrightarrow{AC} \\right| = \\left| \\overrightarrow{CB}+\\overrightarrow{DA}+\\overrightarrow{AC} \\right| = \\left| \\overrightarrow{CB}+\\overrightarrow{DC} \\right| = \\left| \\overrightarrow{DB} \\right|$$zz$\\\\ \n'
                        '\\hspace*{1cm}$\\left| \\overrightarrow{DB} \\right|=DB = \\sqrt{BH^2+DH^2}=%s$ $\\approx $ $%s$ $zz$\\\\ \n'
                        'Vậy \\\\ \n'
                        '\\hspace*{1cm}$\\left| \\overrightarrow{x}\\right| \\approx %s $$zz$'
                        %(latex(goc),latex(a),latex(goc),latex(bi),
                        latex(bi),latex(a),latex(bh),latex(bd),latex(kq),latex(kq)

                            )
                        )


            if dang=='2':
                # Khai báo biến
                a=randint(2,10)
                lis0=[45]
                goc=random.choice(lis0)
                goc_rad=goc*pi/180

                bi=a/tan(goc_rad)
                bh=bi+a
                bd=sqrt(bh**2+a**2)
                x0=round(sqrt(bh**2+a**2),1)
                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình thang cân $ABCD$, có đáy nhỏ và đường cao cùng bằng $%s$ và góc $\\widehat{ABC}=%s^\\circ$$zz$ Tính độ dài $\\overrightarrow{x}=\\overrightarrow{CB}-\\overrightarrow{AD}+\\overrightarrow{AC}$$zz$ (kết quả làm tròn đến hàng phần chục)$zz$ \n'''
                            %(latex(a), latex(goc))
                            )

                # Nội dung lời giải
                loigiai = (
                        '\\begin{center} \n'    
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                                '\\clip(-2$zz$4778629644712598,-0$zz$626343833170012) rectangle (5$zz$654889254630042,3$zz$565473184644411); \n'
                                '\\draw (-2,0)-- (0,3); \n'
                                '\\draw (0,3)-- (3,3); \n'
                                '\\draw (3,3)-- (5,0); \n'
                                '\\draw (5,0)-- (-2,0); \n'
                                '\\draw (0,3)-- (0,0); \n'
                                '\\draw (3,3)-- (3,0); \n'
                                '\\draw (-2$zz$6151425103393733,0$zz$1576618434785709) node[anchor=north west] {$B$}; \n'
                                '\\draw (-0$zz$45128684278928387,3$zz$6504856854026187) node[anchor=north west] {$A$}; \n'
                                '\\draw (4$zz$842672212552968,0$zz$08902207054451423) node[anchor=north west] {$C$}; \n'
                                '\\draw (2$zz$999723363046841,3$zz$55501977562243) node[anchor=north west] {$D$}; \n'
                                '\\draw (-0$zz$30493911648154838,-0$zz$009592700873126778) node[anchor=north west] {$I$}; \n'
                                '\\draw (2$zz$553375636739105,-0$zz$051406336961051194) node[anchor=north west] {$H$}; \n'
                                '\\draw (-2,0)-- (3,3); \n'
                                '\\draw [shift={(-1$zz$8015774764683667,0$zz$030511625279132783)}] plot[domain=-0$zz$06888586909496919:1$zz$3236178474618479,variable=\\t]({1$zz$*0$zz$44328060302912903*cos(\\t r)+0$zz$*0$zz$44328060302912903*sin(\\t r)},{0$zz$*0$zz$44328060302912903*cos(\\t r)+1$zz$*0$zz$44328060302912903*sin(\\t r)}); \n'
                            '\\end{tikzpicture} \n'
                            '\\end{center} \n'

                        'Từ hình vẽ ta có \\\\ \n'
                        '\\hspace*{1cm}$\\tan %s^\\circ =\\dfrac{AI}{BI} \\Rightarrow BI=\\dfrac{%s}{\\tan %s^\\circ} =%s$$zz$\\\\ \n'
                        'Suy ra $BH=BI+IH=%s +%s = %s $$zz$\\\\ \n'
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm}$\\left| \\overrightarrow{x} \\right|=\\left| \\overrightarrow{CB}-\\overrightarrow{AD}+\\overrightarrow{AC} \\right| = \\left| \\overrightarrow{CB}+\\overrightarrow{DA}+\\overrightarrow{AC} \\right| = \\left| \\overrightarrow{CB}+\\overrightarrow{DC} \\right| = \\left| \\overrightarrow{DB} \\right|$$zz$\\\\ \n'
                        '\\hspace*{1cm}$\\left| \\overrightarrow{DB} \\right|=DB = \\sqrt{BH^2+DH^2}=%s$ $\\approx $ $%s$ $zz$\\\\ \n'
                        'Vậy \\\\ \n'
                        '\\hspace*{1cm}$\\left| \\overrightarrow{x}\\right| \\approx %s $$zz$'
                        %(latex(goc),latex(a),latex(goc),latex(bi),
                        latex(bi),latex(a),latex(bh),latex(bd),latex(kq),latex(kq)

                            )
                        )


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.',',').replace('$zz$','.')
            return content                    

