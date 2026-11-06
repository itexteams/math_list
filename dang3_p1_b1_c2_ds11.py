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


def bt_dang3_p1_b1_c2_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6']
            dang=random.choice(lisdang)

            if dang=='6':
                n=symbols('n')
                lisk=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
                k1=random.choice(lisk)
                lisk.remove(k1)
                k2=random.choice(lisk)
                lisk.remove(k2)
                k3=random.choice(lisk)
                lisk.remove(k3)
                k4=random.choice(lisk)

                lis=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                lis1=[1,2,3,4,5,6,7,8,9]

                a=random.choice(lis)
                lis.remove(a)
                b=random.choice(lis)
                lis.remove(b)
                c=random.choice(lis1)
                lis1.remove(c)
                e=random.choice(lis1)

                f=(a*n+b)/(c*n+e)
                fk1=Rational(a*k1+b,c*k1+e)
                fk2=Rational(a*k2+b,c*k2+e)
                fk3=Rational(a*k3+b,c*k3+e)
                fk4=Rational(a*k4+b,c*k4+e)


                d = [
                    '$u_{%s}=%s$'%(latex(k1),latex(fk1)),
                    ]
                da= random.choice(d)
                s = [
                    '$u_{%s}=%s$'%(latex(k2),latex(fk2+1)),
                    '$u_{%s}=%s$'%(latex(k3),latex(fk3-1)),
                    '$u_{%s}=%s$'%(latex(k4),latex(fk4+2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho dãy số $(u_n)$ có $u_n=%s$. Khẳng định nào sau đây đúng?  \n'
                                %(latex(f)
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
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $u_{%s}=%s$.\\\\ \n'
                        '\\hspace*{1cm} $u_{%s}=%s$.\\\\ \n'
                        '\\hspace*{1cm} $u_{%s}=%s$.\\\\ \n'
                        '\\hspace*{1cm} $u_{%s}=%s$.\\\\ \n'
                        %(latex(k1),latex(fk1),
                        latex(k2),latex(fk2),
                        latex(k3),latex(fk3),
                        latex(k4),latex(fk4),
                        ))

            if dang=='5':
                n=symbols('n')

                k=randint(10,50)

                lis=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                lis1=[1,2,3,4,5,6,7,8,9]

                a=random.choice(lis)
                lis.remove(a)
                b=random.choice(lis)
                lis.remove(b)
                c=random.choice(lis1)
                lis1.remove(c)
                e=random.choice(lis1)

                f=(a*n+b)/(c*n+e)
                fk=Rational(a*k+b,c*k+e)


                d = [
                    '$%s$'%(latex(k)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(k+1)),
                    '$%s$'%(latex(k+2)),
                    '$%s$'%(latex(k+3)),
                    '$%s$'%(latex(k-1)),
                    '$%s$'%(latex(k-2)),
                    '$%s$'%(latex(k-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho dãy số $(u_n)$ có $u_n=%s$. Số $%s$ là số hạng thứ mấy của dãy?  \n'
                                %(latex(f),latex(fk))
                                )

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $u_n=%s \\Leftrightarrow %s=%s$ giải phương trình ta được $n=%s$.\\\\ \n'
                        %(latex(fk),latex(f),latex(fk),latex(k)
                        ))

            if dang=='4':
                n=symbols('n')

                k=randint(1,50)

                lis=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                lis1=[1,2,3,4,5,6,7,8,9]

                a=random.choice(lis)
                lis.remove(a)
                b=random.choice(lis)
                lis.remove(b)
                c=random.choice(lis)

                e=random.choice(lis1)
                lis1.remove(e)
                g=random.choice(lis1)

                f=(a*n**2+b*n+c)/(e*n+g)
                fk=Rational(a*k**2+b*k+c,e*k+g)



                d = [
                    '$%s$'%(latex(fk)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(fk+1)),
                    '$%s$'%(latex(fk+2)),
                    '$%s$'%(latex(fk+3)),
                    '$%s$'%(latex(fk-1)),
                    '$%s$'%(latex(fk-2)),
                    '$%s$'%(latex(fk-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho dãy số $(u_n)$ có $u_n=%s$. Số hạng thứ $%s$ của dãy là \n'
                                %(latex(f),latex(k))
                                )

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $u_{%s}=\\dfrac{%s \\cdot %s^2 +%s \\cdot %s+%s}{%s \\cdot %s +%s} =%s$.\\\\ \n'
                        %(latex(k),latex(a),latex(k),latex(b),latex(k),latex(c),latex(e),latex(k),latex(g),latex(fk)
                        ))

            if dang=='3':
                n=symbols('n')

                lis=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                lis1=[1,2,3,4,5,6,7,8,9]

                a=random.choice(lis)
                lis.remove(a)
                b=random.choice(lis)
                lis.remove(b)
                c=random.choice(lis)

                e=random.choice(lis1)
                lis1.remove(e)
                g=random.choice(lis1)

                f=(a*n**2+b*n+c)/(e*n+g)
                f1=Rational(a*1**2+b*1+c,e*1+g)
                f2=Rational(a*2**2+b*2+c,e*2+g)
                f3=Rational(a*3**2+b*3+c,e*3+g)
                f4=Rational(a*4**2+b*4+c,e*4+g)
                f5=Rational(a*5**2+b*5+c,e*5+g)

                d = [
                    '$%s, %s, %s, %s, %s$'%(latex(f1),latex(f2),latex(f3),latex(f4),latex(f5)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s, %s, %s, %s, %s$'%(latex(f1+1),latex(f2),latex(f3),latex(f4),latex(f5)),
                    '$%s, %s, %s, %s, %s$'%(latex(f1),latex(f2+2),latex(f3),latex(f4),latex(f5)),
                    '$%s, %s, %s, %s, %s$'%(latex(f1),latex(f2),latex(f3+3),latex(f4),latex(f5)),
                    '$%s, %s, %s, %s, %s$'%(latex(f1),latex(f2),latex(f3),latex(f4-1),latex(f5)),
                    '$%s, %s, %s, %s, %s$'%(latex(f1),latex(f2),latex(f3),latex(f4),latex(f5-2)),
                    '$%s, %s, %s, %s, %s$'%(latex(f1-3),latex(f2),latex(f3),latex(f4),latex(f5)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho dãy số $(u_n)$ có $u_n=%s$. Năm số hạng đầu của dãy là  \n'
                                %(latex(f))
                                )

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $u_1=%s, u_2=%s, u_3=%s, u_4=%s, u_5=%s$.\\\\ \n'
                        %(latex(f1),latex(f2),latex(f3),latex(f4),latex(f5)
                        ))

            if dang=='2':
                n=symbols('n')

                k=randint(1,50)

                lis=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                lis1=[1,2,3,4,5,6,7,8,9]

                a=random.choice(lis)
                lis.remove(a)
                b=random.choice(lis)
                lis.remove(b)
                c=random.choice(lis1)
                lis1.remove(c)
                e=random.choice(lis1)

                f=(a*n+b)/(c*n+e)
                fk=Rational(a*k+b,c*k+e)


                d = [
                    '$%s$'%(latex(fk)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(fk+1)),
                    '$%s$'%(latex(fk+2)),
                    '$%s$'%(latex(fk+3)),
                    '$%s$'%(latex(fk-1)),
                    '$%s$'%(latex(fk-2)),
                    '$%s$'%(latex(fk-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho dãy số $(u_n)$ có $u_n=%s$. Số hạng thứ $%s$ của dãy là  \n'
                                %(latex(f),latex(k))
                                )

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $u_{%s}=\\dfrac{%s \\cdot %s +%s}{%s \\cdot %s +%s} =%s$.\\\\ \n'
                        %(latex(k),latex(a),latex(k),latex(b),latex(c),latex(k),latex(e),latex(fk)
                        ))

            if dang=='1':
                n=symbols('n')

                lis=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                lis1=[1,2,3,4,5,6,7,8,9]

                a=random.choice(lis)
                lis.remove(a)
                b=random.choice(lis)
                lis.remove(b)
                c=random.choice(lis1)
                lis1.remove(c)
                e=random.choice(lis1)

                f=(a*n+b)/(c*n+e)
                f1=Rational(a*1+b,c*1+e)
                f2=Rational(a*2+b,c*2+e)
                f3=Rational(a*3+b,c*3+e)
                f4=Rational(a*4+b,c*4+e)
                f5=Rational(a*5+b,c*5+e)

                d = [
                    '$%s, %s, %s, %s, %s$'%(latex(f1),latex(f2),latex(f3),latex(f4),latex(f5)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s, %s, %s, %s, %s$'%(latex(f1+1),latex(f2),latex(f3),latex(f4),latex(f5)),
                    '$%s, %s, %s, %s, %s$'%(latex(f1),latex(f2+2),latex(f3),latex(f4),latex(f5)),
                    '$%s, %s, %s, %s, %s$'%(latex(f1),latex(f2),latex(f3+3),latex(f4),latex(f5)),
                    '$%s, %s, %s, %s, %s$'%(latex(f1),latex(f2),latex(f3),latex(f4-1),latex(f5)),
                    '$%s, %s, %s, %s, %s$'%(latex(f1),latex(f2),latex(f3),latex(f4),latex(f5-2)),
                    '$%s, %s, %s, %s, %s$'%(latex(f1-3),latex(f2),latex(f3),latex(f4),latex(f5)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho dãy số $(u_n)$ có $u_n=%s$. Năm số hạng đầu của dãy là  \n'
                                %(latex(f))
                                )

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $u_1=%s, u_2=%s, u_3=%s, u_4=%s, u_5=%s$.\\\\ \n'
                        %(latex(f1),latex(f2),latex(f3),latex(f4),latex(f5)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n '+ str(noidungcauhoi)+ 
                '\\choice[2] \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')
            return content

