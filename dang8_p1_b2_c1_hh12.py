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


def bt_dang8_p1_b2_c1_hh12(self):
            # Khai báo biến
            xa = randint(-10,10)
            ya = randint(-10,10)
            za = randint(-10,10)
            xb = randint(-10,10)
            yb = randint(-10,10)
            zb = randint(-10,10)
            xd = randint(-10,10)
            yd = randint(-10,10)
            zd = randint(-10,10)
            x1 = randint(-10,10)
            y1 = randint(-10,10)
            z1 = randint(-10,10)
            while (yb-ya)*(zd-za)-(zb-za)*(yd-ya)==0 or (zb-za)*(xd-xa)-(xb-xa)*(zd-za)==0 or (xb-xa)*(yd-ya)-(yb-ya)*(xd-xa)==0 or ((yb-ya)*(zd-za)-(zb-za)*(yd-ya))*(x1-xa)+((zb-za)*(xd-xa)-(xb-xa)*(zd-za))*(y1-ya)+((xb-xa)*(yd-ya)-(yb-ya)*(xd-xa))*(z1-za)==0:
                xa = randint(-10,10)
                ya = randint(-10,10)
                za = randint(-10,10)
                xb = randint(-10,10)
                yb = randint(-10,10)
                zb = randint(-10,10)
                xd = randint(-10,10)
                yd = randint(-10,10)
                zd = randint(-10,10)
                x1 = randint(-10,10)
                y1 = randint(-10,10)
                z1 = randint(-10,10)
            xc=xb-xa+xd
            yc=yb-ya+yd
            zc=zb-za+zd
            x3=x1-xa+xb
            y3=y1-ya+yb
            z3=z1-za+zb
            x4=x1-xa+xc
            y4=y1-ya+yc
            z4=z1-za+zc
            x5=x1-xa+xd
            y5=y1-ya+yd
            z5=z1-za+zd


            du = ['$C(%s;%s;%s)$'%(latex(xc),latex(yc),latex(zc)),
                        '$B\'(%s;%s;%s)$'%(latex(x3),latex(y3),latex(z3)),
                        '$C\'(%s;%s;%s)$'%(latex(x4),latex(y4),latex(z4)),
                        '$D\'(%s;%s;%s)$'%(latex(x5),latex(y5),latex(z5)),
                                ]
            da= random.choice(du)

            s = ['$C(%s;%s;%s)$'%(latex(xc+1),latex(yc),latex(zc)),
                '$B\'(%s;%s;%s)$'%(latex(x3+1),latex(y3),latex(z3)),
                '$C\'(%s;%s;%s)$'%(latex(x4+1),latex(y4),latex(z4)),
                '$D\'(%s;%s;%s)$'%(latex(x5+1),latex(y5-1),latex(z5)),
                '$C(%s;%s;%s)$'%(latex(xc),latex(yc-1),latex(zc)),
                '$B\'(%s;%s;%s)$'%(latex(x3),latex(y3-1),latex(z3)),
                '$C\'(%s;%s;%s)$'%(latex(x4),latex(y4-1),latex(z4)),
                '$D\'(%s;%s;%s)$'%(latex(x5),latex(y5-1),latex(z5)),
                '$C(%s;%s;%s)$'%(latex(xc),latex(yc),latex(zc+1)),
                '$B\'(%s;%s;%s)$'%(latex(x3),latex(y3),latex(z3+1)),
                '$C\'(%s;%s;%s)$'%(latex(x4),latex(y4),latex(z4+1)),
                '$D\'(%s;%s;%s)$'%(latex(x5),latex(y5-1),latex(z5+1)),
                            ]
            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)
                    # Câu hỏi
            noidungcauhoi = '''Trong không gian $Oxyz$, Cho hình hộp $ABCD.A\'B\'C\'D\'$ và các điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$, $D(%s;%s;%s)$, $A\'(%s;%s;%s)$. Khẳng định nào sau đây là đúng? \n'''%(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb),latex(xd),latex(yd),latex(zd),latex(x1),latex(y1),latex(z1))
                    # Các đáp án
            da_d = ('\\True ' +str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=('Ta có\\\\ \n'
            '\\hspace*{1cm} $ \\overrightarrow{AA\'}=(%s;%s;%s)$, $ \\overrightarrow{AB}=(%s;%s;%s)$.\\\\ \n'
            'Vì $ABCD$ là hình bình hành nên\\\\ \n'
            '\\hspace*{1cm} $\\overrightarrow{DC}=\\overrightarrow{AB}\\Leftrightarrow \\heva{&x_C-%s=%s\\\\&y_C-%s=%s\\\\&z_C-%s=%s} \\Leftrightarrow \\heva{&x_C=%s+%s\\\\&y_C=%s+%s\\\\&z_C=%s+%s} \\Leftrightarrow \\heva{&x_C=%s\\\\&y_C=%s\\\\&z_C=%s} \n'
            '\\Rightarrow C(%s;%s;%s) $.\\\\ \n'
            'Vì $ABCD.A\'B\'C\'D\'$ là hình hộp nên\\\\ \n'
            '\\hspace*{1cm} $\\overrightarrow{BB\'}=\\overrightarrow{AA\'}\\Leftrightarrow \\heva{&x_{B\'}-%s=%s\\\\&y_{B\'}-%s=%s\\\\&z_{B\'}-%s=%s} \\Leftrightarrow \\heva{&x_{B\'}=%s+%s\\\\&y_{B\'}=%s+%s\\\\&z_{B\'}=%s+%s} \\Leftrightarrow \\heva{&x_{B\'}=%s\\\\&y_{B\'}=%s\\\\&z_{B\'}=%s} \\Rightarrow B\'(%s;%s;%s) $.\\\\ \n'
            '\\hspace*{1cm} $\\overrightarrow{CC\'}=\\overrightarrow{AA\'}\\Leftrightarrow \\heva{&x_{C\'}-%s=%s\\\\&y_{C\'}-%s=%s\\\\&z_{C\'}-%s=%s} \\Leftrightarrow \\heva{&x_{C\'}=%s+%s\\\\&y_{C\'}=%s+%s\\\\&z_{C\'}=%s+%s} \\Leftrightarrow \\heva{&x_{C\'}=%s\\\\&y_{C\'}=%s\\\\&z_{C\'}=%s} \\Rightarrow C\'(%s;%s;%s) $.\\\\ \n'  
            '\\hspace*{1cm} $\\overrightarrow{DD\'}=\\overrightarrow{AA\'}\\Leftrightarrow \\heva{&x_{D\'}-%s=%s\\\\&y_{D\'}-%s=%s\\\\&z_{D\'}-%s=%s} \\Leftrightarrow \\heva{&x_{D\'}=%s+%s\\\\&y_{D\'}=%s+%s\\\\&z_{D\'}=%s+%s} \\Leftrightarrow \\heva{&x_{D\'}=%s\\\\&y_{D\'}=%s\\\\&z_{D\'}=%s} \\Rightarrow D\'(%s;%s;%s) $.\\\\ \n' 



                %(latex(x1-xa),latex(y1-ya),latex(z1-za),latex(xb-xa),latex(yb-ya),latex(zb-za),
                latex(xd),latex(xb-xa), latex(yd),latex(yb-ya), latex(zd),latex(zb-za),latex(xb-xa),latex(xd),latex(yb-ya),latex(yd),latex(zb-za),latex(zd),latex(xc),latex(yc),latex(zc),latex(xc),latex(yc),latex(zc),
                latex(xb),latex(x1-xa),latex(yb),latex(y1-ya),latex(zb),latex(z1-za),latex(x1-xa),latex(xb),latex(y1-ya),latex(yb),latex(z1-za),latex(zb),latex(x3),latex(y3),latex(z3),latex(x3),latex(y3),latex(z3),            
                latex(xc),latex(x1-xa),latex(yc),latex(y1-ya),latex(zc),latex(z1-za),latex(x1-xa),latex(xc),latex(y1-ya),latex(yc),latex(z1-za),latex(zc),latex(x4),latex(y4),latex(z4),latex(x4),latex(y4),latex(z4),
                latex(xd),latex(x1-xa),latex(yd),latex(y1-ya),latex(zd),latex(z1-za),latex(x1-xa),latex(xd),latex(y1-ya),latex(yd),latex(z1-za),latex(zd),latex(x5),latex(y5),latex(z5),latex(x5),latex(y5),latex(z5),             
                            ))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice[2] \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('--', '+').replace('-+', '-')
            return content

