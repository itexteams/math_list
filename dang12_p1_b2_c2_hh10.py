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


def bt_dang12_p1_b2_c2_hh10(self):
            # Khai báo biến
            lis0 = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
            a=random.choice(lis0)
            lis1=[30,45,60,90]
            goc=random.choice(lis1)
            goc_rad=goc*pi/180

            goc1=180-goc
            goc1_rad=goc1*pi/180

            oc=sqrt(a**2+a**2-2*a*a*cos(goc1_rad))
            kq=round(sqrt(a**2+a**2-2*a*a*cos(goc1_rad)),1)
            kq1=round(sqrt(1+2*a**2+a**2-2*a*a*cos(goc1_rad)),1)
            kq2=round(sqrt(2+a**2+a**2+2*a*a*cos(goc1_rad)),1)
            kq3=round(sqrt(3+a**2+a**2+a*a*cos(goc1_rad)),1)

            #Nội ung câu hỏi
            noidungcauhoi = ('''Có hai lực $\\overrightarrow{F_1}, \\overrightarrow{F_2}$ cùng tác động vào một vật tại điểm $O$, biết hai lực $\\overrightarrow{F_1}, \\overrightarrow{F_2}$ đều có cường độ là $%s$ (N) và hợp với nhau một góc $%s^\\circ$$zz$ Cường độ của lực tổng hợp mà vật đó phải chịu là\n'''
                            %(latex(a),latex(goc)
                            ))
            # Các đáp án
            da_d = '\\True $%s$ (N)'%(latex(kq))
            da_s1 = ' $%s$ (N)'%(latex(kq1))
            da_s2 = ' $%s$ (N)'%(latex(kq2))
            da_s3 = ' $%s$ (N)'%(latex(kq3))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=(
                    '\\begin{center} \n'    
                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                        '\\clip(-2$zz$351084719979218,-2$zz$7141564237883467) rectangle (6$zz$699935900585451,2$zz$7995672241256186); \n'
                        '\\draw [->] (0$zz$,0$zz$) -- (3$zz$,2$zz$); \n'
                        '\\draw [->] (0$zz$,0$zz$) -- (3$zz$,-2$zz$); \n'
                        '\\draw [dash pattern=on 2pt off 2pt] (3$zz$,2$zz$)-- (6$zz$,0$zz$); \n'
                        '\\draw [dash pattern=on 2pt off 2pt] (6$zz$,0$zz$)-- (3$zz$,-2$zz$); \n'
                        '\\draw [->] (0$zz$,0$zz$) -- (6$zz$,0$zz$); \n'
                        '\\draw (0$zz$,0$zz$5262619126060105)-- (0$zz$,-0$zz$527325538130491); \n'
                        '\\draw (0$zz$,0$zz$5262619126060105)-- (-2$zz$003381888545266,0$zz$5156196151238236); \n'
                        '\\draw (0$zz$,-0$zz$527325538130491)-- (-1$zz$9820972935808923,-0$zz$5379678356126779); \n'
                        '\\draw (-1$zz$9820972935808923,-0$zz$5379678356126779)-- (-2$zz$003381888545266,0$zz$5156196151238236); \n'
                        '\\draw (-0$zz$67330283059987087,0$zz$2555513498123736) node[anchor=north west] {$O$}; \n'
                        '\\draw (2$zz$79776015711692,2$zz$5056371031890285) node[anchor=north west] {$A$}; \n'
                        '\\draw (2$zz$8788443284097727,-2$zz$0148054463874945) node[anchor=north west] {$B$}; \n'
                        '\\draw (6$zz$1728887871819085,0$zz$07311196440345559) node[anchor=north west] {C}; \n'
                        '\\draw (0$zz$5862122526714753,1$zz$6441177832024716) node[anchor=north west] {$\\overrightarrow{F_1}$}; \n'
                        '\\draw (1$zz$0760767312598688,-1$zz$0215243480500522) node[anchor=north west] {$\\overrightarrow{F_2}$}; \n'
                    '\\end{tikzpicture} \n'
                        '\\end{center} \n'

                    'Giẳ sử $\\overrightarrow{F_1}=\\overrightarrow{OA}$ và $\\overrightarrow{F_2}=\\overrightarrow{OB}$$zz$\\\\\n'
                    'Theo quy tắc hình bình hành $\\overrightarrow{F_1}+\\overrightarrow{F_2}=\\overrightarrow{OA}+\\overrightarrow{OB}=\\overrightarrow{OC}$$zz$ \\\\ \n'
                    'Ta có $\\widehat{AOB}=%s^\\circ$ và $OA=OB=%s$$zz$\\\\ \n'
                    'Suy ra $\\widehat{OAC}=%s^\\circ$ và $AC=%s$$zz$\\\\ \n'
                    'Áp dụng định lí cosin cho tam giác $AOC$ ta có \\\\ \n'
                    '$OC=\\sqrt{OA^2+AC^2-2OA \\cdot AC \\cos %s^\\circ}=%s=%s$$zz$ \\\\ \n'
                    'Vậy cường độ của lực tổng hợp mà vật đó phải chịu là $%s$ (N)$zz$'
                    %(latex(goc),latex(a),
                    latex(goc1),latex(a),
                    latex(goc1),latex(oc),latex(kq),latex(kq)
                        )
                    )
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('.',',').replace('$zz$','.')
            return content

