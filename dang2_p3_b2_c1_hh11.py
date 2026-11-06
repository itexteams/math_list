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


def bt_dang2_p3_b2_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(2,9)
                h1=a/(2*a+4 )
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Gọi $M, N$ là trung điểm của $BD$ và $BC$, $I, J$ thuộc $AN, AM$ sao cho $AI=%sAN, AJ=%sAM$. Tỉ số giữa $IJ$ và $CD$ bằng bao nhiêu? \n'
                                %(latex(Rational(a,a+2)),latex(Rational(a,a+2))
                                ))

                # Nội dung lời giải
                loigiai = (

                        '\\begin{center}  \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                            '\\clip(-0.7342063492380041,-2.733457718096196) rectangle (4.625934442291535,3.7643456087783744); \n'
                            '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (4.,0.); \n'
                            '\\draw [line width=1.pt] (0.,0.)-- (1.,-2.); \n'
                            '\\draw [line width=1.pt] (1.,-2.)-- (4.,0.); \n'
                            '\\draw [line width=1.pt] (0.,0.)-- (2.,3.); \n'
                            '\\draw [line width=1.pt] (2.,3.)-- (4.,0.); \n'
                            '\\draw [line width=1.pt] (2.,3.)-- (1.,-2.); \n'
                            '\\draw [line width=1.pt] (2.,3.)-- (0.488,-0.976); \n'
                            '\\draw [line width=1.pt] (2.,3.)-- (2.4815384615384617,-1.0123076923076924); \n'
                            '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.488,-0.976)-- (2.4815384615384617,-1.0123076923076924); \n'
                            '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.3092187135170814,0.4235066937618277)-- (1.0332409012131716,0.4577816291161181); \n'
                            '\\draw (1.7,3.5) node[anchor=north west] {A}; \n'
                            '\\draw (0.6,-2) node[anchor=north west] {B}; \n'
                            '\\draw (3.9,0.2) node[anchor=north west] {C}; \n'
                            '\\draw (-0.5,0.2) node[anchor=north west] {D}; \n'
                            '\\draw (0,-1) node[anchor=north west] {M}; \n'
                            '\\draw (2.5,-0.8) node[anchor=north west] {N}; \n'
                            '\\draw (2.3,0.7) node[anchor=north west] {I}; \n'
                            '\\draw (0.5,0.85) node[anchor=north west] {J}; \n'
                        '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'

                            'Ta có \\\\ \n'
                        '$MN // CD$ và $MN = \\dfrac{1}{2}CD$ \\hspace*{1cm} (1). \\\\ \n'
                        'Theo giả thiết $\\dfrac{AI}{AN} = \\dfrac{AJ}{AM} = %s$. \\\\ \n'
                        'Suy ra $IJ // MN$ và $IJ=%s MN$ \\hspace*{1cm} (2). \\\\ \n'
                        'Từ (1) và (2) suy ra $IJ // CD$ và $IJ=%sCD$.'
                        %(latex(Rational(a,a+2)),latex(Rational(a,a+2)),
                            latex(Rational(a,2*a+4))
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content                 

