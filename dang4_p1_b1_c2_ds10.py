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


def bt_dang4_p1_b1_c2_ds10(self):
            #Khai báo biến
            x = symbols('x')
            y = symbols('y')
            m = symbols('m')
            x0 = randint(-5, 5)
            y0 = randint(-5, 5)
            a = randint(-5, 5)
            b = randint(-5, 5)
            c = randint(-5, 5)
            while a*x0+c*y0==0:
                x0 = randint(-5, 5)
                y0 = randint(-5, 5)
                a = randint(-5, 5)
                c = randint(-5, 5)
            d = randint(-5, 5)
            e = randint(-5, 5)
            lis=['>','\\ge','<','\\le']
            dau=random.choice(lis)
            if a*x0+c*y0>0 and dau=='>':
                bpt=(a*m+b)*x+(c*m+d)*y+e
                bt1=a*m+b
                bt2=c*m+d
                bt3=expand((a*m+b)*x0+(c*m+d)*y0+e)
                bt4=-Rational(b*x0+d*y0+e,a*x0+c*y0)

                #Nội dung câu hỏi
                noidungcauhoi = ('Cho bất phương trình bậc nhất hai ẩn $%s>0$. Giá trị của tham số $m$ để cặp số $x=%s, y=%s$ là nghiệm của bất phương trình là'
                                    %(latex(bpt),latex(x0),latex(y0)))
                # Các đáp án
                da_d = '\\True $m>%s$'%(latex(bt4))
                da_s1 = '$m<%s$'%(latex(bt4))
                da_s2 = '$m>%s$'%(latex(bt4+1))
                da_s3 = '$m<%s$'%(latex(bt4+1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có $x=%s, y=%s$ là nghiệm của bất phương trình $%s>0$ khi và chỉ khi \\\\ \n'
                        '$(%s)(%s)+(%s)(%s)+%s>0 \\Leftrightarrow %s>0 \\Leftrightarrow m>%s$.'
                        %(latex(x0),latex(y0),latex(bpt),
                        latex(x0),latex(bt1),latex(y0),latex(bt2),latex(e),latex(bt3),latex(bt4)
                        ) )
            if a*x0+c*y0>0 and dau=='\\ge':
                bpt=(a*m+b)*x+(c*m+d)*y+e
                bt1=a*m+b
                bt2=c*m+d
                bt3=expand((a*m+b)*x0+(c*m+d)*y0+e)
                bt4=-Rational(b*x0+d*y0+e,a*x0+c*y0)

                #Nội dung câu hỏi
                noidungcauhoi = ('Cho bất phương trình bậc nhất hai ẩn $%s \\ge 0$. Giá trị của tham số $m$ để cặp số $x=%s, y=%s$ là nghiệm của bất phương trình là'
                                    %(latex(bpt),latex(x0),latex(y0)))
                # Các đáp án
                da_d = '\\True $m \\ge %s$'%(latex(bt4))
                da_s1 = '$m \\ge %s$'%(latex(bt4+1))
                da_s2 = '$m \\le %s$'%(latex(bt4))
                da_s3 = '$m \\le %s$'%(latex(bt4+1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có $x=%s, y=%s$ là nghiệm của bất phương trình $%s \\ge 0$ khi và chỉ khi \\\\ \n'
                        '$(%s)(%s)+(%s)(%s)+%s \\ge 0 \\Leftrightarrow %s \\ge 0 \\Leftrightarrow m \\ge %s$.'
                        %(latex(x0),latex(y0),latex(bpt),
                        latex(x0),latex(bt1),latex(y0),latex(bt2),latex(e),latex(bt3),latex(bt4)
                        ) )
            if a*x0+c*y0>0 and dau=='<':
                bpt=(a*m+b)*x+(c*m+d)*y+e
                bt1=a*m+b
                bt2=c*m+d
                bt3=expand((a*m+b)*x0+(c*m+d)*y0+e)
                bt4=-Rational(b*x0+d*y0+e,a*x0+c*y0)

                #Nội dung câu hỏi
                noidungcauhoi = ('Cho bất phương trình bậc nhất hai ẩn $%s<0$. Giá trị của tham số $m$ để cặp số $x=%s, y=%s$ là nghiệm của bất phương trình là'
                                    %(latex(bpt),latex(x0),latex(y0)))
                # Các đáp án
                da_d = '\\True $m < %s$'%(latex(bt4))
                da_s1 = '$m < %s$'%(latex(bt4+1))
                da_s2 = '$m > %s$'%(latex(bt4))
                da_s3 = '$m > %s$'%(latex(bt4+1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có $x=%s, y=%s$ là nghiệm của bất phương trình $%s<0$ khi và chỉ khi \\\\ \n'
                        '$(%s)(%s)+(%s)(%s)+%s<0 \\Leftrightarrow %s<0 \\Leftrightarrow m<%s$.'
                        %(latex(x0),latex(y0),latex(bpt),
                        latex(x0),latex(bt1),latex(y0),latex(bt2),latex(e),latex(bt3),latex(bt4)
                        ) )
            if a*x0+c*y0>0 and dau=='\\le':
                bpt=(a*m+b)*x+(c*m+d)*y+e
                bt1=a*m+b
                bt2=c*m+d
                bt3=expand((a*m+b)*x0+(c*m+d)*y0+e)
                bt4=-Rational(b*x0+d*y0+e,a*x0+c*y0)

                #Nội dung câu hỏi
                noidungcauhoi = ('Cho bất phương trình bậc nhất hai ẩn $%s \\le 0$. Giá trị của tham số $m$ để cặp số $x=%s, y=%s$ là nghiệm của bất phương trình là'
                                    %(latex(bpt),latex(x0),latex(y0)))
                # Các đáp án
                da_d = '\\True $m \\le %s$'%(latex(bt4))
                da_s1 = '$m \\le %s$'%(latex(bt4+1))
                da_s2 = '$m \\ge %s$'%(latex(bt4))
                da_s3 = '$m \\ge %s$'%(latex(bt4+1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có $x=%s, y=%s$ là nghiệm của bất phương trình $%s \\le 0$ khi và chỉ khi \\\\ \n'
                        '$(%s)(%s)+(%s)(%s)+%s \\le 0 \\Leftrightarrow %s \\le 0 \\Leftrightarrow m \\le %s$.'
                        %(latex(x0),latex(y0),latex(bpt),
                        latex(x0),latex(bt1),latex(y0),latex(bt2),latex(e),latex(bt3),latex(bt4)
                        ) )
            if a*x0+c*y0<0 and dau=='>':
                bpt=(a*m+b)*x+(c*m+d)*y+e
                bt1=a*m+b
                bt2=c*m+d
                bt3=expand((a*m+b)*x0+(c*m+d)*y0+e)
                bt4=-Rational(b*x0+d*y0+e,a*x0+c*y0)

                #Nội dung câu hỏi
                noidungcauhoi = ('Cho bất phương trình bậc nhất hai ẩn $%s>0$. Giá trị của tham số $m$ để cặp số $x=%s, y=%s$ là nghiệm của bất phương trình là'
                                    %(latex(bpt),latex(x0),latex(y0)))
                # Các đáp án
                da_d = ' $m>%s$'%(latex(bt4))
                da_s1 = '$\\True m<%s$'%(latex(bt4))
                da_s2 = '$m>%s$'%(latex(bt4+1))
                da_s3 = '$m<%s$'%(latex(bt4+1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có $x=%s, y=%s$ là nghiệm của bất phương trình $%s>0$ khi và chỉ khi \\\\ \n'
                        '$(%s)(%s)+(%s)(%s)+%s>0 \\Leftrightarrow %s>0 \\Leftrightarrow m<%s$.'
                        %(latex(x0),latex(y0),latex(bpt),
                        latex(x0),latex(bt1),latex(y0),latex(bt2),latex(e),latex(bt3),latex(bt4)
                        ) )
            if a*x0+c*y0<0 and dau=='\\ge':
                bpt=(a*m+b)*x+(c*m+d)*y+e
                bt1=a*m+b
                bt2=c*m+d
                bt3=expand((a*m+b)*x0+(c*m+d)*y0+e)
                bt4=-Rational(b*x0+d*y0+e,a*x0+c*y0)

                #Nội dung câu hỏi
                noidungcauhoi = ('Cho bất phương trình bậc nhất hai ẩn $%s \\ge 0$. Giá trị của tham số $m$ để cặp số $x=%s, y=%s$ là nghiệm của bất phương trình là'
                                    %(latex(bpt),latex(x0),latex(y0)))
                # Các đáp án
                da_d = ' $m \\ge %s$'%(latex(bt4))
                da_s1 = '$m \\ge %s$'%(latex(bt4+1))
                da_s2 = '\\True $m \\le %s$'%(latex(bt4))
                da_s3 = '$m \\le %s$'%(latex(bt4+1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có $x=%s, y=%s$ là nghiệm của bất phương trình $%s \\ge 0$ khi và chỉ khi \\\\ \n'
                        '$(%s)(%s)+(%s)(%s)+%s \\ge 0 \\Leftrightarrow %s \\ge 0 \\Leftrightarrow m \\le %s$.'
                        %(latex(x0),latex(y0),latex(bpt),
                        latex(x0),latex(bt1),latex(y0),latex(bt2),latex(e),latex(bt3),latex(bt4)
                        ) )
            if a*x0+c*y0<0 and dau=='<':
                bpt=(a*m+b)*x+(c*m+d)*y+e
                bt1=a*m+b
                bt2=c*m+d
                bt3=expand((a*m+b)*x0+(c*m+d)*y0+e)
                bt4=-Rational(b*x0+d*y0+e,a*x0+c*y0)

                #Nội dung câu hỏi
                noidungcauhoi = ('Cho bất phương trình bậc nhất hai ẩn $%s<0$. Giá trị của tham số $m$ để cặp số $x=%s, y=%s$ là nghiệm của bất phương trình là'
                                    %(latex(bpt),latex(x0),latex(y0)))
                # Các đáp án
                da_d = ' $m < %s$'%(latex(bt4))
                da_s1 = '$m < %s$'%(latex(bt4+1))
                da_s2 = '\\True $m > %s$'%(latex(bt4))
                da_s3 = '$m > %s$'%(latex(bt4+1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có $x=%s, y=%s$ là nghiệm của bất phương trình $%s<0$ khi và chỉ khi \\\\ \n'
                        '$(%s)(%s)+(%s)(%s)+%s<0 \\Leftrightarrow %s<0 \\Leftrightarrow m>%s$.'
                        %(latex(x0),latex(y0),latex(bpt),
                        latex(x0),latex(bt1),latex(y0),latex(bt2),latex(e),latex(bt3),latex(bt4)
                        ) )
            if a*x0+c*y0<0 and dau=='\\le':
                bpt=(a*m+b)*x+(c*m+d)*y+e
                bt1=a*m+b
                bt2=c*m+d
                bt3=expand((a*m+b)*x0+(c*m+d)*y0+e)
                bt4=-Rational(b*x0+d*y0+e,a*x0+c*y0)

                #Nội dung câu hỏi
                noidungcauhoi = ('Cho bất phương trình bậc nhất hai ẩn $%s \\le 0$. Giá trị của tham số $m$ để cặp số $x=%s, y=%s$ là nghiệm của bất phương trình là'
                                    %(latex(bpt),latex(x0),latex(y0)))
                # Các đáp án
                da_d = ' $m \\le %s$'%(latex(bt4))
                da_s1 = '$m \\le %s$'%(latex(bt4+1))
                da_s2 = '\\True $m \\ge %s$'%(latex(bt4))
                da_s3 = '$m \\ge %s$'%(latex(bt4+1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có $x=%s, y=%s$ là nghiệm của bất phương trình $%s \\le 0$ khi và chỉ khi \\\\ \n'
                        '$(%s)(%s)+(%s)(%s)+%s \\le 0 \\Leftrightarrow %s \\le 0 \\Leftrightarrow m \\ge %s$.'
                        %(latex(x0),latex(y0),latex(bpt),
                        latex(x0),latex(bt1),latex(y0),latex(bt2),latex(e),latex(bt3),latex(bt4)
                        ) )
                # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-','-').replace('+0','').replace('-0','').replace('\\frac','\\dfrac')
            return content

