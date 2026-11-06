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


def bt_dang10_p4_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                k=randint(1,9)
                x1=1*k
                x2=3*k
                y1=4*k*x1

                f1=4*k*x
                f2=(x-3*k)**2

                y11=2*k*x**2
                y12=2*k*0**2
                y13=2*k*x1**2
                kq1=abs(y13-y12)

                y21=Rational(1,3)*x**3-3*k*x**2+9*(k**2)*x
                y22=Rational(1,3)*x1**3-3*k*x1**2+9*(k**2)*x1
                y23=Rational(1,3)*x2**3-3*k*x2**2+9*(k**2)*x2
                kq2=abs(y23-y22)

                kq3=kq1+kq2

                while kq3>9999:
                # Khai báo biến
                    x=symbols('x')
                    k=randint(1,9)
                    x1=1*k
                    x2=3*k
                    y1=4*k*x1

                    f1=4*k*x
                    f2=(x-3*k)**2

                    y11=2*k*x**2
                    y12=2*k*0**2
                    y13=2*k*x1**2
                    kq1=abs(y13-y12)

                    y21=Rational(1,3)*x**3-3*k*x**2+9*(k**2)*x
                    y22=Rational(1,3)*x1**3-3*k*x1**2+9*(k**2)*x1
                    y23=Rational(1,3)*x2**3-3*k*x2**2+9*(k**2)*x2
                    kq2=abs(y23-y22)

                    kq3=kq1+kq2

                h1=kq3

                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Cho hai hàm số $f(x)=%s, g(x)=%s$ có đồ thị như hình vẽ$zz$ Tính diện tích phần hình phẳng gạch chéo (làm tròn kết quả đến hàng đơn vị)$zz$ \n'
                                '}{'
                                '\\scalebox{0$zz$8}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                                '\\clip(-0$zz$6382108502159634,-1$zz$0519516190831026) rectangle (5$zz$169248710998062,4$zz$989679698631484);  \n'
                                '\\draw[line width=0pt,fill=black,pattern=north east lines,pattern color=black, smooth,samples=50,domain=0$zz$0:1$zz$0] plot(\\x,{4$zz$0*\\x}) -- (1$zz$,0$zz$) -- (0$zz$,0$zz$) -- cycle;  \n'
                                '\\draw[line width=0pt,fill=black,pattern=north east lines,pattern color=black, smooth,samples=50,domain=1$zz$0:3$zz$0] plot(\\x,{(\\x-3$zz$0)^(2$zz$0)}) -- (3$zz$,0$zz$) -- (1$zz$,0$zz$) -- cycle;  \n'
                                '\\draw [line width=1$zz$pt,domain=-0$zz$6382108502159634:5$zz$169248710998062] plot(\\x,{(-0$zz$--4$zz$*\\x)/1$zz$});  \n'
                                '\\draw [samples=50,rotate around={0$zz$:(3$zz$,0$zz$)},xshift=3$zz$cm,yshift=0$zz$cm,line width=1$zz$pt,domain=-4$zz$0:4$zz$0)] plot (\\x,{(\\x)^2/2/0$zz$5});  \n'
                                '\\draw [line width=1$zz$pt,dash pattern=on 2pt off 2pt] (1$zz$,4$zz$)-- (0$zz$,4$zz$);  \n'
                                '\\draw [->,line width=1$zz$pt] (-0$zz$5,0$zz$) -- (5$zz$,0$zz$);  \n'
                                '\\draw [->,line width=1$zz$pt] (0$zz$,-1$zz$) -- (0$zz$,5$zz$);  \n'
                                '\\draw (-0$zz$49770779631562406,0$zz$5) node[anchor=north west] {$O$};  \n'
                                '\\draw (0$zz$7,0$zz$11890716341972433) node[anchor=north west] {$%s$};  \n'
                                '\\draw (-0$zz$7,4$zz$415958895205099) node[anchor=north west] {$%s$};  \n'
                                '\\draw (2$zz$827531145992406,0) node[anchor=north west] {$%s$};  \n'
                                '\\draw (4$zz$490150617146422,0) node[anchor=north west] {$x$};  \n'
                                '\\draw (-0$zz$5,5) node[anchor=north west] {$y$}; \n'
                                '\\end{tikzpicture}} \n'
                                '}'
                                %(latex(f1),latex(f2),
                                latex(x1),latex(y1),latex(x2)
                                ))

                # Nội dung lời giải
                loigiai=('Diện tích hình phẳng cần tìm là \\\\ \n'
                        '\\hspace*{1cm} $S=\\displaystyle\\int\\limits_{%s}^{%s} \\left| f(x) \\right|\\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} \\left| g(x) \\right|\\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s} \\left| %s \\right|\\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} \\left| %s \\right|\\text{d}x=%s+%s=%s$$zz$\\\\ \n'
                        'Vậy diện tích hình phẳng xấp sỉ bằng $%s$$zz$'
                        %(latex(0),latex(x1),latex(x1),latex(x2),
                        latex(0),latex(x1),latex(f1),latex(x1),latex(x2),latex(f2),
                        latex(kq1),latex(kq2),latex(kq3),
                        latex(kq)
                        ))

                #Đáp án


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content 

