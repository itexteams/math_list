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


def bt_dang16_p4_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                a=randint(2,14)
                x0=2*a*sqrt(2)/5
                f=((a**2)/2)*x**4-(a*sqrt(2)/2)*x**5
                f0=((a**2)/2)*x0**4-(a*sqrt(2)/2)*x0**5
                v=(1/3)*sqrt(f0)
                h1=v

                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Từ một tấm bìa hình vuông cạnh $%s$ dm, người ta cắt bỏ bốn tam giác cân bằng nhau có cạnh đáy là cạnh của hình vuông ban đầu và đỉnh là đỉnh của một hình vuông nhỏ phía trong rồi gập lên, ghép lại tạo thành một khối chóp tứ giác đều (hình bên). Thể tích lớn nhất của khối chóp bằng bao nhiêu dm$^3$? (Làm tròn kết quả đến hàng phần mười). \n'
                                '} \n'
                                '{ \n'
                                '\\scalebox{0.6}{'
                                    '''\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                                    \\draw  [line width=1]  (136.07,38.33) -- (354.67,38.33) -- (354.67,256.93) -- (136.07,256.93) -- cycle ;
                                    \\draw  [fill={rgb, 255:red, 240; green, 232; blue, 131 }  ,fill opacity=1 ][line width=1]  (245.37,75.43) -- (317.57,147.63) -- (245.37,219.83) -- (173.17,147.63) -- cycle ;
                                    \\draw  [fill={rgb, 255:red, 240; green, 232; blue, 131 }  ,fill opacity=1 ][line width=1]  (245.37,75.43) -- (173.17,147.63) -- (136.07,38.33) -- cycle ;
                                    \\draw  [fill={rgb, 255:red, 240; green, 232; blue, 131 }  ,fill opacity=1 ][line width=1]  (354.67,38.33) -- (317.57,147.63) -- (245.37,75.43) -- cycle ;
                                    \\draw  [fill={rgb, 255:red, 240; green, 232; blue, 131 }  ,fill opacity=1 ][line width=1]  (354.67,256.93) -- (245.37,219.83) -- (317.57,147.63) -- cycle ;
                                    \\draw  [fill={rgb, 255:red, 240; green, 232; blue, 131 }  ,fill opacity=1 ][line width=1]  (245.37,219.83) -- (136.07,256.93) -- (173.17,147.63) -- cycle ;
                                \\end{tikzpicture}'''
                                '}} \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

                    '\\begin{center} \n'
                    '\\scalebox{0.6}{'
                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                        '\\clip(-1.282439024390243,-1.1274146341463402) rectangle (6.3663414634146385,6.092097560975613); \n'
                        '\\draw [line width=1.pt] (0.,0.)-- (0.,5.); \n'
                        '\\draw [line width=1.pt] (0.,5.)-- (5.,5.); \n'
                        '\\draw [line width=1.pt] (5.,5.)-- (5.,0.); \n'
                        '\\draw [line width=1.pt] (5.,0.)-- (0.,0.); \n'
                        '\\draw [line width=1.pt] (0.7995121951219477,2.5)-- (2.5,4.200487804878053); \n'
                        '\\draw [line width=1.pt] (2.5,4.200487804878053)-- (4.200487804878052,2.5); \n'
                        '\\draw [line width=1.pt] (4.200487804878052,2.5)-- (2.5,0.7995121951219477); \n'
                        '\\draw [line width=1.pt] (2.5,0.7995121951219477)-- (0.7995121951219477,2.5); \n'
                        '\\draw [line width=1.pt] (0.,5.)-- (2.5,4.200487804878053); \n'
                        '\\draw [line width=1.pt] (2.5,4.200487804878053)-- (5.,5.); \n'
                        '\\draw [line width=1.pt] (5.,5.)-- (4.200487804878052,2.5); \n'
                        '\\draw [line width=1.pt] (4.200487804878052,2.5)-- (5.,0.); \n'
                        '\\draw [line width=1.pt] (5.,0.)-- (2.5,0.7995121951219477); \n'
                        '\\draw [line width=1.pt] (2.5,0.7995121951219477)-- (0.,0.); \n'
                        '\\draw [line width=1.pt] (0.,0.)-- (0.7995121951219477,2.5); \n'
                        '\\draw [line width=1.pt] (0.7995121951219477,2.5)-- (0.,5.); \n'
                        '\\draw [line width=1.pt] (0.,5.)-- (5.,0.); \n'
                        '\\draw (-0.6775609756097551,5.5) node[anchor=north west] {$A$}; \n'
                        '\\draw (5.098048780487808,5.5) node[anchor=north west] {$B$}; \n'
                        '\\draw (5.059024390243906,0.12136585365853828) node[anchor=north west] {$C$}; \n'
                        '\\draw (-0.75560975609756,0.12136585365853828) node[anchor=north west] {$D$}; \n'
                        '\\draw (2.2297560975609776,4.9) node[anchor=north west] {$M$}; \n'
                        '\\draw (4.356585365853661,3.0677073170731735) node[anchor=north west] {$N$}; \n'
                        '\\draw (2.190731707317075,0.7) node[anchor=north west] {$P$}; \n'
                        '\\draw (0.14195121951219639,3.048195121951222) node[anchor=north west] {$Q$}; \n'
                        '\\draw (0.8248780487804893,3.6) node[anchor=north west] {$H$}; \n'
                        '\\draw (3.049268292682929,1.5) node[anchor=north west] {$K$}; \n'
                        '\\draw (2.42487804878049,3) node[anchor=north west] {$O$}; \n'
                        '\\draw (3.2639024390243927,3.8) node[anchor=north west] {$x$}; \n'
                    '\\end{tikzpicture}} \n'
                '\\end{center} \n'
                            'Gọi cạnh đáy của hình chóp tứ giác đều là $x$ dm với $0<x<%s$. \\\\ \n'
                        'Ta có $AH=\\dfrac{AC-HK}{2}=%s-\\dfrac{x}{2}$. \\\\ \n'
                        'Đường cao của hình chóp tứ giác đều là \\\\ \n'
                        '\\hspace*{1cm} $h=\\sqrt{AH^2-OH^2}=\\sqrt{\\left( %s-\\dfrac{x}{2} \\right)^2 -\\left( \\dfrac{x}{2} \\right)^2}=\\sqrt{%s-%s x}$. \\\\ \n'
                        'Thể tích khối chóp là \\\\ \n'
                        '\\hspace*{1cm} $V=\\dfrac{1}{3} hx^2=\\dfrac{1}{3} x^2 \\sqrt{%s-%s x}=\\dfrac{1}{3} \\sqrt{x^4 \\left( %s-%s x \\right)}$. \\\\ \n'
                        'Để tìm giá trị lớn nhất của $V$, ta tìm giá trị lớn nhất của hàm số $f(x)=x^4 \\left( %s-%s x \\right)$ với $0<x<%s$. \\\\ \n'
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=%s x^3-%s x^4, f\'(x)=0$ khi $x=0$ hoặc $x=%s$. \\\\ \n'
                        '\\hspace*{1cm} Bảng biến thiên \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                        '{$x$/1.2,$f\'(x)$/0.7,$f(x)$/2.1}  \n'
                        '{$0$,$%s$,$%s$}  \n'
                        '\\tkzTabLine{,+,0,-,}  \n'
                        '\\tkzTabVar{-/$$,+/$f \\left( %s \\right)$,-/$$}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng biến thiên ta có $\\max f(x)=f \\left( %s \\right) \\approx %s$ tại $x=%s$.\\\\ \n'
                        'Vậy thể tích lớn nhất của khối chóp bằng \\\\ \n'
                        '\\hspace*{1cm} $V_{\\text{max}}=\\dfrac{1}{3} \\sqrt{\\left( %s \\right)^4 \\left( %s-%s \\cdot %s \\right)} \\approx %s$ dm$^3$.'

                        %(latex(a*sqrt(2)),
                            latex(a*sqrt(2)/2),
                            latex(a*sqrt(2)/2),
                            latex(Rational(a**2,2)),latex(a*sqrt(2)/2),
                            latex(Rational(a**2,2)),latex(a*sqrt(2)/2),latex(Rational(a**2,2)),latex(a*sqrt(2)/2),
                            latex(Rational(a**2,2)),latex(a*sqrt(2)/2),latex(a*sqrt(2)),
                            latex(2*a**2),latex(5*a*sqrt(2)/2),latex(2*a*sqrt(2)/5),
                            latex(x0),latex(a*sqrt(2)),
                            latex(x0),
                            latex(x0),latex(f0),latex(x0),
                            latex(x0),latex(Rational(a**2,2)),latex(a*sqrt(2)/2),latex(x0),latex(kq)
                            ))

                #Đáp án


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

