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


def bt_dang10_p1_b1_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                xa=randint(-8,8)
                ya=randint(-8,8)
                za=randint(-5,5)
                xb=randint(-6,6)
                yb=randint(-7,7)
                zb=randint(-5,6)
                xc=randint(-6,6)
                yc=randint(-7,7)
                zc=randint(-6,6)
                x1=xb-xa
                y1=yb-ya
                z1=zb-za
                x2=xc-xa
                y2=yc-ya
                z2=zc-za
                xn=y1*z2-z1*y2
                yn=z1*x2-x1*z2
                zn=x1*y2-y1*x2
                x3=xc-xb
                y3=yc-yb
                z3=zc-zb


                while xn==0 or yn==0 or zn==0 or x3*xa+y3*ya+z3*za==0 or xc-xb==0 or yc-yb==0 or zc-zb==0:
                    xa=randint(-8,8)
                    ya=randint(-8,8)
                    za=randint(-5,5)
                    xb=randint(-6,6)
                    yb=randint(-7,7)
                    zb=randint(-5,6)
                    xc=randint(-6,6)
                    yc=randint(-7,7)
                    zc=randint(-6,6)
                    x1=xb-xa
                    y1=yb-ya
                    z1=zb-za
                    x2=xc-xa
                    y2=yc-ya
                    z2=zc-za
                    xn=y1*z2-z1*y2
                    yn=z1*x2-x1*z2
                    zn=x1*y2-y1*x2
                    x3=xc-xb
                    y3=yc-yb
                    z3=zc-zb

                u=math.gcd(math.gcd(x3,y3),z3)
                a=nsimplify(x3/u)
                b=nsimplify(y3/u)
                c=nsimplify(z3/u)
                d=-nsimplify((x3*xa+y3*ya+z3*za)/u)


                du = ['$%sx+%sy+%sz+%s=0$'%(latex(a),latex(b),latex(c),latex(d))
                    ]
                da= random.choice(du)
                s = ['$%sx+%sy+%sz+%s=0$'%(latex(a),latex(b),latex(c),latex(d+1)),
                    '$%sx+%sy+%sz+%s=0$'%(latex(-a),latex(-b),latex(c),latex(d)),
                    '$%sx+%sy+%sz+%s=0$'%(latex(-a),latex(-b),latex(-c),latex(d)),
                    '$%sx+%sy+%sz+%s=0$'%(latex(a),latex(b),latex(c),latex(d+2))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho ba điểm $A(%s;%s;%s), B(%s;%s;%s)$ và $C(%s;%s;%s)$. Phương trình mặt phẳng $(P)$ đi qua điểm $A$ và vuông góc với đường thẳng $BC$ là'
                                %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb),latex(xc),latex(yc),latex(zc)))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì mặt phẳng $(P)$ vuông góc với đường thẳng $BC$ nên có vectơ pháp tuyến là\\\\ \n'
                        '$$\\vec{n}=\\vec{BC}=(%s;%s;%s).$$'
                        'Mặt phẳng $(P)$ đi qua điểm $A(%s;%s;%s)$ và nhận $\\vec{n}=(%s;%s;%s)$ làm một vectơ pháp tuyến nên có phương trình là\\\\ \n'
                        '\\hspace*{1cm}$%s(x-%s)+%s(y-%s)+%s(z-%s)=0 \\Leftrightarrow %sx+%sy+%sz+%s=0$.'

                        %(latex(x3),latex(y3),latex(z3),
                        latex(xa),latex(ya),latex(za),
                        latex(x3),latex(y3),latex(z3),
                        latex(x3),latex(xa),latex(y3),latex(ya),latex(z3),latex(za),latex(a),latex(b),latex(c),latex(d)


                        )
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('--','+').replace('+-','-').replace('\\Leftrightarrow 1x','\\Leftrightarrow x').replace('\\Leftrightarrow -1x','\\Leftrightarrow -x').replace('+1y','+y').replace('+1z','+z').replace('-1y','-y').replace('-1z','-z').replace('$1x','$x')


            return content

