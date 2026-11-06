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


def bt_dang19_p1_b4_c2_hh12(self):
            lisdang=['1','2','3']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                z=symbols('z')

                a=randint(-9,10)
                b=randint(-9,10)
                c=randint(-9,10)
                d=randint(-9,10)
                m=randint(-9,10)
                n=randint(-9,10)
                p=randint(-9,10)
                q=randint(-9,10)

                while a==0 or b==0 or c==0 or m==0 or n==0 or p==0 or a**2+b**2+c**2-d<=0 or abs(m*a+n*b+p*c+d)/sqrt(m**2+n**2+p**2)!=sqrt(a**2+b**2+c**2-d):
                    x=symbols('x')
                    y=symbols('y')
                    z=symbols('z')

                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)
                    m=randint(-9,9)
                    n=randint(-9,9)
                    p=randint(-9,9)
                    q=randint(-9,9)

                mc=-2*a*x-2*b*y-2*c*z+d
                mp=m*x+n*y+p*z+q
                r=sqrt(a**2+b**2+c**2-d)
                kc=abs(m*a+n*b+p*c+d)/sqrt(m**2+n**2+p**2)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, Cho mặt cầu $(S):x^2+y^2+z^2+%s=0$ và mặt phẳng $(P):%s=0$. Vị trí tương đối của mặt cầu $(S)$ và mặt phẳng $(P)$ là'
                                %(latex(mc),latex(mp)))

                # Nội dung lời giải
                loigiai=('Mặt cầu $(S)$ có tâm $I(%s;%s;%s)$ và bán kính $R=\\sqrt{(%s)^2+(%s)^2+(%s)^2-(%s)}=%s$.\\\\ \n'
                        'Với $(P): %s=0$ thì $d(I,(P))=\\frac{|%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)+%s|}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%s=R$.\\\\ \n'
                        'Vậy mặt phẳng $(P)$ tiếp xúc mặt cầu $(S)$.'
                        %(latex(a),latex(b),latex(c),latex(a),latex(b),latex(c),latex(d),latex(r),
                        latex(mp),latex(m),latex(a),latex(n),latex(b),latex(p),latex(c),latex(d),latex(m),latex(n),latex(p),latex(kc),

                        ))

                du = ['Mặt phẳng $(P)$ tiếp xúc mặt cầu $(S)$',

                    ]
                da= random.choice(du)
                s = ['Mặt phẳng $(P)$  không cắt mặt cầu $(S)$',
                    'Mặt phẳng $(P)$ cắt mặt cầu $(S)$',
                    'Không xét được',

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Các đáp án
                da_d = ('\\True ' +str(da))     
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                z=symbols('z')

                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                d=randint(-9,9)
                m=randint(-9,9)
                n=randint(-9,9)
                p=randint(-9,9)
                q=randint(-9,9)

                while a==0 or b==0 or c==0 or m==0 or n==0 or p==0 or a**2+b**2+c**2-d<=0 or abs(m*a+n*b+p*c+d)/sqrt(m**2+n**2+p**2)>=sqrt(a**2+b**2+c**2-d):
                    x=symbols('x')
                    y=symbols('y')
                    z=symbols('z')

                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)
                    m=randint(-9,9)
                    n=randint(-9,9)
                    p=randint(-9,9)
                    q=randint(-9,9)

                mc=-2*a*x-2*b*y-2*c*z+d
                mp=m*x+n*y+p*z+q
                r=sqrt(a**2+b**2+c**2-d)
                kc=abs(m*a+n*b+p*c+d)/sqrt(m**2+n**2+p**2)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, Cho mặt cầu $(S):x^2+y^2+z^2+%s=0$ và mặt phẳng $(P):%s=0$. Vị trí tương đối của mặt cầu $(S)$ và mặt phẳng $(P)$ là'
                                %(latex(mc),latex(mp)))

                # Nội dung lời giải
                loigiai=('Mặt cầu $(S)$ có tâm $I(%s;%s;%s)$ và bán kính $R=\\sqrt{(%s)^2+(%s)^2+(%s)^2-(%s)}=%s$.\\\\ \n'
                        'Với $(P): %s=0$ thì $d(I,(P))=\\frac{|%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)+%s|}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%s<R$.\\\\ \n'
                        ' Vậy mặt phẳng $(P)$ cắt mặt cầu $(S)$.'
                        %(latex(a),latex(b),latex(c),latex(a),latex(b),latex(c),latex(d),latex(r),
                        latex(mp),latex(m),latex(a),latex(n),latex(b),latex(p),latex(c),latex(d),latex(m),latex(n),latex(p),latex(kc),

                        ))

                du = ['Mặt phẳng $(P)$ cắt mặt cầu $(S)$',

                    ]
                da= random.choice(du)
                s = ['Mặt phẳng $(P)$  không cắt mặt cầu $(S)$',
                    'Mặt phẳng $(P)$ tiếp xúc mặt cầu $(S)$',
                    'Không xét được',

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Các đáp án
                da_d = ('\\True ' +str(da))     
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                z=symbols('z')

                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                d=randint(-9,9)
                m=randint(-9,9)
                n=randint(-9,9)
                p=randint(-9,9)
                q=randint(-9,9)

                while a==0 or b==0 or c==0 or m==0 or n==0 or p==0 or a**2+b**2+c**2-d<=0 or abs(m*a+n*b+p*c+d)/sqrt(m**2+n**2+p**2)<=sqrt(a**2+b**2+c**2-d):
                    x=symbols('x')
                    y=symbols('y')
                    z=symbols('z')

                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)
                    m=randint(-9,9)
                    n=randint(-9,9)
                    p=randint(-9,9)
                    q=randint(-9,9)

                mc=-2*a*x-2*b*y-2*c*z+d
                mp=m*x+n*y+p*z+q
                r=sqrt(a**2+b**2+c**2-d)
                kc=abs(m*a+n*b+p*c+q)/sqrt(m**2+n**2+p**2)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, Cho mặt cầu $(S):x^2+y^2+z^2+%s=0$ và mặt phẳng $(P):%s=0$. Vị trí tương đối của mặt cầu $(S)$ và mặt phẳng $(P)$ là'
                                %(latex(mc),latex(mp)))

                # Nội dung lời giải
                loigiai=('Mặt cầu $(S)$ có tâm $I(%s;%s;%s)$ và bán kính $R=\\sqrt{(%s)^2+(%s)^2+(%s)^2-(%s)}=%s$.\\\\ \n'
                        'Với $(P): %s=0$ thì $d(I,(P))=\\frac{|%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)+%s|}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%s>R$.\\\\ \n'
                        'Vậy mặt phẳng $(P)$ không cắt mặt cầu $(S)$.'
                        %(latex(a),latex(b),latex(c),latex(a),latex(b),latex(c),latex(d),latex(r),
                        latex(mp),latex(m),latex(a),latex(n),latex(b),latex(p),latex(c),latex(q),latex(m),latex(n),latex(p),latex(kc),

                        ))

                du = ['Mặt phẳng $(P)$ không cắt mặt cầu $(S)$',

                    ]
                da= random.choice(du)
                s = ['Mặt phẳng $(P)$ cắt mặt cầu $(S)$',
                    'Mặt phẳng $(P)$ tiếp xúc mặt cầu $(S)$',
                    'Không xét được',

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Các đáp án
                da_d = ('\\True ' +str(da))     
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('frac','dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+')
            return content

