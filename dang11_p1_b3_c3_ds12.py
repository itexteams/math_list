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


def bt_dang11_p1_b3_c3_ds12(self):
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

                du = ['$S=%s$'%(latex(kq3)),
                    ]
                da= random.choice(du)
                s = ['$S=%s$'%(latex(kq3+1)),
                    '$S=%s$'%(latex(kq3+2)),
                    '$S=%s$'%(latex(kq3+3)),
                    '$S=%s$'%(latex(kq3-1)),
                    '$S=%s$'%(latex(kq3-2)),
                    '$S=%s$'%(latex(kq3-3)),
                    '$S=%s$'%(latex(kq3-4)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Cho hai hàm số $f(x)=%s, g(x)=%s$ có đồ thị như hình vẽ. Diện tích phần hình phẳng gạch chéo là \n'
                                '}{'
                                '\\scalebox{0.8}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                                '\\clip(-1,-1.0519516190831026) rectangle (5.169248710998062,4.989679698631484);  \n'
                                '\\draw[line width=0pt,fill=black,pattern=north east lines,pattern color=black, smooth,samples=50,domain=0.0:1.0] plot(\\x,{4.0*\\x}) -- (1.,0.) -- (0.,0.) -- cycle;  \n'
                                '\\draw[line width=0pt,fill=black,pattern=north east lines,pattern color=black, smooth,samples=50,domain=1.0:3.0] plot(\\x,{(\\x-3.0)^(2.0)}) -- (3.,0.) -- (1.,0.) -- cycle;  \n'
                                '\\draw [line width=1.pt,domain=-0.6382108502159634:5.169248710998062] plot(\\x,{(-0.--4.*\\x)/1.});  \n'
                                '\\draw [samples=50,rotate around={0.:(3.,0.)},xshift=3.cm,yshift=0.cm,line width=1.pt,domain=-4.0:4.0)] plot (\\x,{(\\x)^2/2/0.5});  \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,4.)-- (0.,4.);  \n'
                                '\\draw [->,line width=1.pt] (-0.5,0.) -- (5.,0.);  \n'
                                '\\draw [->,line width=1.pt] (0.,-1.) -- (0.,5.);  \n'
                                '\\draw (-0.49770779631562406,0.5) node[anchor=north west] {$O$};  \n'
                                '\\draw (0.7,0.11890716341972433) node[anchor=north west] {$%s$};  \n'
                                '\\draw (-1,4.415958895205099) node[anchor=north west] {$%s$};  \n'
                                '\\draw (2.827531145992406,0) node[anchor=north west] {$%s$};  \n'
                                '\\draw (4.490150617146422,0) node[anchor=north west] {$x$};  \n'
                                '\\draw (-0.5,5) node[anchor=north west] {$y$}; \n'
                                '\\end{tikzpicture}} \n'
                                '}'
                                %(latex(f1),latex(f2),
                                latex(x1),latex(y1),latex(x2)
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Diện tích hình phẳng cần tìm là \\\\ \n'
                        '\\hspace*{1cm} $S=\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s}  g(x) \\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s} %s \\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s}  %s \\text{d}x=%s+%s=%s$.'
                        %(latex(0),latex(x1),latex(x1),latex(x2),
                        latex(0),latex(x1),latex(f1),latex(x1),latex(x2),latex(f2),
                        latex(kq1),latex(kq2),latex(kq3)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

