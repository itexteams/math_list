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


def bt_dang24_p3_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                a=randint(10,25)
                k=a/10
                m=4*k
                c=3*k
                t1=5*a
                t2=3*a
                d=randint(10,20)
                kq=d-c
                y=t2*(d-x)+t1*(x**2+m**2)**0.5
                y0=nsimplify(y.subs(x,0))
                y2=y.subs(x,c)
                y3=round(y.subs(x,d),2)


                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Một đường dây điện được nối từ một nhà máy điện ở $A$ đến một hòn đảo ở $C$ như hình vẽ$zz$ Khoảng cách từ $C$ đến $B$ là $%s$ km$zz$ '
                                'Bờ biển chạy thẳng từ $A$ đến $B$ với khoảng cách là $%s$ km$zz$ Tổng chi phí lắp đặt cho $1$ km dây điện trên biển là $%s$ triệu đồng, '
                                'còn trên đất liền là $%s$ triệu đồng$zz$ Hỏi khoảng cách $AM$ bằng bao nhiêu kilômét (điểm $M$ nằm trên đoạn $AB$) để tổng chi phí lắp đặt là nhỏ nhất$zz$ \\\\ \n'
                                '}{'
                                '\\scalebox{0$zz$6}{ '  
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                '\\path \n'
                '(0,0) coordinate (B) \n'
                '(0,4) coordinate (C) \n'
                '(3,0) coordinate (M) \n'
                '(10,0) coordinate (A) \n'
                '; \n'
                '\\draw (A)--(M)--(C)--(B)--(M); \n'
                '\\foreach \\x/\\g in {A/-90,B/-90,C/90,M/-90} \\draw[fill=black] (\\x) circle ($zz$05) node[shift={(\\g:$zz$3)}]{$\\x$}; \n'
                '\\draw (0,2) node[left]  {$%s$km}; \n'
                                '\\end{tikzpicture}}}\n'
                            %(latex(m),latex(d),latex(t1),latex(t2),latex(m)
                            )
                            )
                # Nội dung lời giải
                loigiai = ('Gọi khoảng cách $BM$ là $x$ km, $(0 \\leq x \\leq %s)$$zz$ \\\\ \n'
                        'Khi đó khoảng cách $AM$ là $%s-x$ km$zz$ \\\\ \n'
                        'Khoảng cách $CM$ là $\\sqrt{%s+x^2}$ km$zz$ \\\\ \n'
                        'Chi phí lắp đặt dây điện là $f(x)=%s(%s-x)+%s\\sqrt{%s+x^2}$ (triệu đồng)$zz$\\\\ \n'
                        'Bài toán trở thành tìm $x$ để $f(x)$ đạt giá trị nhỏ nhất$zz$ \\\\ \n'
                        'Ta có \\\\'
                        '$f\'(x)=-%s+\\dfrac{%sx}{\\sqrt{%s+x^2}}$$zz$\\\\ \n'
                        '$f\'(x)=0 \\Leftrightarrow -%s+\\dfrac{%sx}{\\sqrt{%s+x^2}}=0$\\\\ \n'
                        '$\\Leftrightarrow -%s\\sqrt{%s+x^2}+%sx=0$ \\\\ \n'
                        '$\\Leftrightarrow %s\\sqrt{%s+x^2}=%sx$\\\\ \n'
                        '$\\Leftrightarrow \\heva{&x \\geq 0\\\\&%s(%s+x^2)=%sx^2}$ \\\\ \n'
                        '$\\Leftrightarrow x=%s$$zz$\\\\ \n' 
                        'Ta có $f(0)=%s; f(%s)=%s; f(%s) \\approx%s$$zz$\\\\ \n'
                        'Do đó chi phí nhỏ nhất để lắp dây điện là $%s$ triệu đồng khi $BM=%s$ km$zz$\\\\ \n'
                        'Suy ra $AM=%s-%s=%s$ km$zz$'
                        %(latex(d),latex(d),
                        latex(m**2),latex(t2),latex(d),latex(t1),latex(m**2),latex(t2),latex(t1),latex(m**2),
                        latex(t2),latex(t1),latex(m**2),
                        latex(t2),latex(m**2),latex(t1),
                        latex(t2),latex(m**2),latex(t1),
                        latex(t2**2),latex(m**2),latex(t1**2),
                        latex(c),
                        latex(y0),latex(c),latex(y2),latex(d),latex(y3),
                        latex(y2),latex(c),latex(d),latex(c),latex(kq)

                        )
                        )

                #Đáp án
                dapan='\\shortans[0]{$%s$}'%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('$zz$','.').replace('\\frac','\\dfrac')
            return content

