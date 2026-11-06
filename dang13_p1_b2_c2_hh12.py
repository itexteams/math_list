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


def bt_dang13_p1_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                x0=randint(-9,9)
                y0=randint(-9,9)
                z0=randint(-9,9)
                a1=randint(-9,9)
                b1=randint(-9,9)
                c1=randint(-9,9)
                a2=randint(-9,9)
                b2=randint(-9,9)
                c2=randint(-9,9)
                d=randint(-20,20)
                k=gcd(gcd(a2,b2),c2)
                dk=a1*a2+b1*b2+c1*c2
                a=d+a2*x0+b2*y0+c2*z0
                b=a1*a2+b1*b2+c1*c2
                while a1==0 or b1==0 or c1==0 or a2==0 or b2==0 or c2==0 or x0==0 or y0==0 or z0==0 or k!=1 or dk==0 or a%b!=0: 
                    x,y,z=symbols('x,y,z')
                    x0=randint(-9,9)
                    y0=randint(-9,9)
                    z0=randint(-9,9)
                    a1=randint(-9,9)
                    b1=randint(-9,9)
                    c1=randint(-9,9)
                    a2=randint(-9,9)
                    b2=randint(-9,9)
                    c2=randint(-9,9)
                    d=randint(-20,20)
                    k=gcd(gcd(a2,b2),c2)
                    dk=a1*a2+b1*b2+c1*c2
                    a=d+a2*x0+b2*y0+c2*z0
                    b=a1*a2+b1*b2+c1*c2
                pt=a2*x+b2*y+c2*z+d
                t=-nsimplify(a/b)
                x1=x0+a1*t
                y1=y0+b1*t
                z1=z0+c1*t

                du = ['$(%s;%s;%s)$'%(latex(x1),latex(y1),latex(z1))

                    ]
                da= random.choice(du)
                s = ['$(%s;%s;%s)$'%(latex(x1),latex(y1+1),latex(z1)),
                    '$(%s;%s;%s)$'%(latex(x1),latex(y1),latex(z1+1)),
                    '$(%s;%s;%s)$'%(latex(x1+1),latex(y1),latex(z1)),
                    '$(%s;%s;%s)$'%(latex(x1+1),latex(y1+1),latex(z1+1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =  ('Trong không gian $Oxyz$, cho mặt phẳng $(P):%s=0$ và đường thẳng $\\Delta:\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$. Giao điểm của đường thẳng $\\Delta$ và mặt phẳng $(P)$ có tọa độ là'
                                %(latex(pt),latex(x0),latex(a1),latex(y0),latex(b1),latex(z0),latex(c1))
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
                loigiai= ('Gọi $M(%s+%st;%s+%st;%s+%st)$ là giao điểm của đường thẳng $\\Delta$ và mặt phẳng $(P)$.\\\\ \n'
                        'Vì $M\\in (P)$ nên ta có\\\\ \n'
                        '\\hspace*{1cm}$%s(%s+%st)+%s(%s+%st)+%s(%s+%st)+%s=0\\Leftrightarrow t=%s$.\\\\ \n'
                        'Vậy $M(%s;%s;%s)$.'
                        %(latex(x0),latex(a1),latex(y0),latex(b1),latex(z0),latex(c1),
                            latex(a2),latex(x0),latex(a1),latex(b2),latex(y0),latex(b1),latex(c2),latex(z0),latex(c1),latex(d),
                            latex(t),latex(x1),latex(y1),latex(z1))
                            )


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','+').replace('+-','-').replace('\\frac','\\dfrac').replace('1t','t').replace('+0','').replace('1\\cdot','')
            return content

