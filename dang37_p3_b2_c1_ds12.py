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


def bt_dang37_p3_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                t=symbols('t')
                a=-1 
                b1=[3,6,9,12,15,18,21]
                b=random.choice(b1)
                c=randint(1,20)
                d=randint(1,20)

                s=a*t**3+b*t**2+c*t+d
                v=3*a*t**2+2*b*t+c
                dh=6*a*t+2*b

                t0=-Rational(b,3*a)
                v0=3*a*t0**2+2*b*t0+c
                s0=a*t0**3+b*t0**2+c*t0+d

                t1=t0+3

                while v0<=0 or s0-d<=0:
                    t=symbols('t')
                    a=-1 
                    b1=[3,6,9,12,15,18,21]
                    b=random.choice(b1)
                    c=randint(1,9)
                    d=randint(1,9)

                    s=a*t**3+b*t**2+c*t+d
                    v=3*a*t**2+2*b*t+c
                    dh=6*a*t+2*b



                    t0=-Rational(b,3*a)
                    v0=3*a*t0**2+2*b*t0+c
                    s0=a*t0**3+b*t0**2+c*t0+d

                    t1=t0+3

                h1=1
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq1=str(kq).replace('.',',')
                # Nội dung câu hỏi
                noidungcauhoi = ('''Một vật chuyển động trên đường thẳng có quãng đường di chuyển trong khoảng thời gian $t$ (giây) được cho bởi phương trình $s(t)=%s$ (m). Hỏi trong khoảng $%s$ (giây) đầu tiên tính từ khi vật bắt đầu chuyển động đến thời điểm vận tốc của vật đạt giá trị lớn nhất thì vật di chuyển được quãng đường dài bao nhiêu mét?'''
                                 %(latex(s),latex(t1)
                                 ))

                # Nội dung lời giải
                loigiai = ('''Vận tốc của vật có phương trình là $v(t)=s'(t)=%s$.\\\\
                           Khi đó $v'(t)=%s$. \\\\
                                   \\hspace*{1.2cm}  $v(t)=0 \\Leftrightarrow %s=0 \\Leftrightarrow t=%s$. \\\\
                                       \\hspace*{1.2cm} Bảng biến thiên \\\\
                                           \\hspace*{1.2cm}  \\begin{tikzpicture}
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$t$/0.7,$v(t)$/0.7,$v(t)$/2.1}
            {$0$,$%s $,$%s$}
            \\tkzTabLine{,+,0,-,}
            \\tkzTabVar{-/$$,+/$%s$,-/$$}
            \\end{tikzpicture} \\\\
            Trong khoảng $%s$ giây đầu, vận tốc lớn nhất của vật đạt được từ khi bắt đầu di chuyển là $%s$ (m/s) tại thời điểm $%s$ giây. \\\\
            Ta có $s(0)=%s ; s(%s)=%s$. \\\\
            Vậy từ khi bắt dầu di chuyển đến thời điểm vận tốc của vật đạt giá trị lớn nhất thì vật di chuyển được quãng đường dài $%s$ (m).'''
                           %(latex(v),
                             latex(dh),latex(dh),latex(t0),
                             latex(t0),latex(t1),latex(v0),
                             latex(t1),latex(v0),latex(t0),
                             latex(d),latex(t0),latex(s0),
                             latex(s0-d)
                           ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}'%(latex(s0-d))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

