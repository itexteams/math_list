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


def bt_dang3_p4_b2_c2_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                u1=3
                d=4
                n=randint(10,50)
                un=u1+(n-1)*d
                sn=n*u1+Rational(n*(n-1)*d,2)
                h1=sn

                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Bạn An dùng các que diêm để xếp thành hình tháp có quy luật được thể hiện trong hình sau \\\\ \n'
                                '\\begin{center} \n'
                                    '\\definecolor{ududff}{rgb}{0.30196078431372547,0.30196078431372547,1.} \n'
                                    '\\definecolor{xdxdff}{rgb}{0.49019607843137253,0.49019607843137253,1.} \n'
                                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                                        '\\clip(-1.068638481257706,-1.1263813466588473) rectangle (11.971544853563877,3.795923454705433); \n'
                                        '\\draw [line width=1.pt] (0.,1.)-- (1.,1.); \n'
                                        '\\draw [line width=1.pt] (0.,1.)-- (0.,0.); \n'
                                        '\\draw [line width=1.pt] (1.,1.)-- (1.,0.); \n'
                                        '\\draw [line width=1.pt] (2.,0.)-- (2.,1.); \n'
                                        '\\draw [line width=1.pt] (2.,1.)-- (3.,1.); \n'
                                        '\\draw [line width=1.pt] (3.,1.)-- (4.,1.); \n'
                                        '\\draw [line width=1.pt] (4.,1.)-- (5.,1.); \n'
                                        '\\draw [line width=1.pt] (5.,1.)-- (5.,0.); \n'
                                        '\\draw [line width=1.pt] (4.,1.)-- (4.,0.); \n'
                                        '\\draw [line width=1.pt] (3.,1.)-- (3.,0.); \n'
                                        '\\draw [line width=1.pt] (3.,1.)-- (3.,2.); \n'
                                        '\\draw [line width=1.pt] (3.,2.)-- (4.,2.); \n'
                                        '\\draw [line width=1.pt] (4.,2.)-- (4.,1.); \n'
                                        '\\draw [line width=1.pt] (6.,0.)-- (6.,1.); \n'
                                        '\\draw [line width=1.pt] (6.,1.)-- (7.,1.); \n'
                                        '\\draw [line width=1.pt] (7.,1.)-- (8.,1.); \n'
                                        '\\draw [line width=1.pt] (8.,1.)-- (9.,1.); \n'
                                        '\\draw [line width=1.pt] (9.,1.)-- (10.,1.); \n'
                                        '\\draw [line width=1.pt] (10.,1.)-- (11.,1.); \n'
                                        '\\draw [line width=1.pt] (7.,1.)-- (7.,0.); \n'
                                        '\\draw [line width=1.pt] (8.,1.)-- (8.,0.); \n'
                                        '\\draw [line width=1.pt] (9.,1.)-- (9.,0.); \n'
                                        '\\draw [line width=1.pt] (10.,1.)-- (10.,0.); \n'
                                        '\\draw [line width=1.pt] (11.,1.)-- (11.,0.); \n'
                                        '\\draw [line width=1.pt] (7.,1.)-- (7.,2.); \n'
                                        '\\draw [line width=1.pt] (7.,2.)-- (10.,2.); \n'
                                        '\\draw [line width=1.pt] (10.,2.)-- (10.,1.); \n'
                                        '\\draw [line width=1.pt] (9.,1.)-- (9.,2.); \n'
                                        '\\draw [line width=1.pt] (8.,1.)-- (8.,2.); \n'
                                        '\\draw [line width=1.pt] (8.,2.)-- (8.,3.); \n'
                                        '\\draw [line width=1.pt] (8.,3.)-- (9.,3.); \n'
                                        '\\draw [line width=1.pt] (9.,3.)-- (9.,2.); \n'
                                        '\\draw (-0.25,-0.36392866672087226) node[anchor=north west] {Tầng 1}; \n'
                                        '\\draw (2.75,-0.36392866672087226) node[anchor=north west] {Tầng 2}; \n'
                                        '\\draw (7.75,-0.36392866672087226) node[anchor=north west] {Tầng 3}; \n'
                                        '\\begin{scriptsize} \n'
                                            '\\draw [fill=xdxdff] (0.,1.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (1.,1.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (2.,1.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (3.,1.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (4.,1.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (5.,1.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (3.,2.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (4.,2.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (6.,1.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (7.,1.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (8.,1.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (9.,1.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (10.,1.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (11.,1.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (7.,2.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (10.,2.) circle (2.5pt); \n'
                                            '\\draw [fill=xdxdff] (9.,2.) circle (2.5pt); \n'
                                            '\\draw [fill=xdxdff] (8.,2.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (8.,3.) circle (2.5pt); \n'
                                            '\\draw [fill=ududff] (9.,3.) circle (2.5pt); \n'
                                        '\\end{scriptsize} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Tính số que diêm để xếp thành hình tháp có $%s$ tầng.'
                                %(latex(n)
                                ))

                # Nội dung lời giải
                loigiai = ('Số que diêm để xếp được tầng đế của tháp là một cấp số cộng với $u_1=3, d=4$. \\\\ \n'
                        'Do đó, số que diêm để xếp được tầng đế của tháp $%s$ tầng là $u_{%s}=u_1+%s d=%s$.\\\\ \n'
                        'Vậy số que diêm để xếp được hình tháp $%s$ tầng là $S=u_1+u_2+\\cdots+u_{%s}=\\dfrac{%s(%s+%s)}{2}=%s$.'
                        %(latex(n),latex(n),latex(n-1),latex(un),
                            latex(n),latex(n),latex(n),latex(u1),latex(un),latex(sn)

                            ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

