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


def bt_dang5_p1_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                xa=randint(-6,6)
                ya=randint(-6,6)
                za=randint(-6,6)
                u1=randint(-6,6)
                u2=randint(-6,6)
                u3=randint(-6,6)
                d=randint(-10,10)
                dk=gcd(gcd(u1,u2),u3)
                while u1==0 or u2==0 or u3==0 or xa==0 or ya==0 or za==0 or dk!=1:
                    xa=randint(-6,6)
                    ya=randint(-6,6)
                    za=randint(-6,6)
                    u1=randint(-6,6)
                    u2=randint(-6,6)
                    u3=randint(-6,6)
                    d=randint(-10,10)
                    dk=gcd(gcd(u1,u2),u3)
                pt=u1*x+u2*y+u3*z+d

                du = ['$\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$'%(latex(xa),latex(u1),latex(ya),latex(u2),latex(za),latex(u3))
                    ]
                da= random.choice(du)
                s = ['$\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$'%(latex(-xa),latex(u1),latex(-ya),latex(u2),latex(za),latex(u3)),
                    '$\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$'%(latex(xa),latex(u1),latex(-ya),latex(u2),latex(-za),latex(u3)),
                    '$\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$'%(latex(xa),latex(-u1),latex(ya),latex(-u2),latex(za),latex(u3)),
                    '$\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$'%(latex(xa),latex(u1),latex(ya),latex(-u2),latex(za),latex(-u3)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =  ('Trong không gian $Oxyz$, phương trình của đường thẳng $\\Delta$ đi qua điểm $A(%s;%s;%s)$ và vuông góc với mặt phẳng $(\\alpha):%s=0$ là'
                                %(latex(xa),latex(ya),latex(za),latex(pt))
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
                loigiai= ('Mặt phẳng $(\\alpha)$ có vectơ pháp tuyến là $\\vec{n}=(%s;%s;%s)$. Giá của $\\vec{n}=(%s;%s;%s)$ và $\\Delta$ cùng vuông góc với $(\\alpha)$ nên chúng trùng nhau hoặc song song với nhau. Do đó $\\Delta$ nhận $\\vec{n}=(%s;%s;%s)$ làm một vectơ chỉ phương.\\\\ \n'
                        'Vậy $\\Delta$ có phương trình là '
                        '$\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}.$'
                                %(latex(u1),latex(u2),latex(u3),
                                latex(u1),latex(u2),latex(u3),
                                latex(u1),latex(u2),latex(u3),
                                latex(xa),latex(u1),latex(ya),latex(u2),latex(za),latex(u3),


                                )
                            )
            if dang=='2':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                xa=randint(-6,6)
                ya=randint(-6,6)
                za=randint(-6,6)
                u1=randint(-6,6)
                u2=randint(-6,6)
                u3=randint(-6,6)
                d=randint(-10,10)
                dk=gcd(gcd(u1,u2),u3)
                while u1==0 or u2==0 or u3==0 or xa==0 or ya==0 or za==0 or dk!=1:
                    xa=randint(-6,6)
                    ya=randint(-6,6)
                    za=randint(-6,6)
                    u1=randint(-6,6)
                    u2=randint(-6,6)
                    u3=randint(-6,6)
                    d=randint(-10,10)
                    dk=gcd(gcd(u1,u2),u3)
                pt=u1*x+u2*y+u3*z+d

                du = ['$\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$'%(latex(xa),latex(u1),latex(ya),latex(u2),latex(za),latex(u3))
                    ]
                da= random.choice(du)
                s = ['$\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$'%(latex(-xa),latex(u1),latex(-ya),latex(u2),latex(za),latex(u3)),
                    '$\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$'%(latex(xa),latex(u1),latex(-ya),latex(u2),latex(-za),latex(u3)),
                    '$\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$'%(latex(xa),latex(-u1),latex(ya),latex(-u2),latex(za),latex(u3)),
                    '$\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$'%(latex(xa),latex(u1),latex(ya),latex(-u2),latex(za),latex(-u3)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =  ('Trong không gian $Oxyz$, phương trình tham số của đường thẳng $\\Delta$ đi qua điểm $A(%s;%s;%s)$ và vuông góc với mặt phẳng $(\\alpha):%s=0$ là'
                                %(latex(xa),latex(ya),latex(za),latex(pt))
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
                loigiai= ('Mặt phẳng $(\\alpha)$ có vectơ pháp tuyến là $\\vec{n}=(%s;%s;%s)$. Giá của $\\vec{n}=(%s;%s;%s)$ và $\\Delta$ cùng vuông góc với $(\\alpha)$ nên chúng trùng nhau hoặc song song với nhau. Do đó $\\Delta$ nhận $\\vec{n}=(%s;%s;%s)$ làm một vectơ chỉ phương.\\\\ \n'
                        'Vậy $\\Delta$ có phương trình tham số là '
                        '$\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}.$'
                                %(latex(u1),latex(u2),latex(u3),
                                latex(u1),latex(u2),latex(u3),
                                latex(u1),latex(u2),latex(u3),
                                latex(xa),latex(u1),latex(ya),latex(u2),latex(za),latex(u3),


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
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','+').replace('+-','-').replace('\\frac','\\dfrac').replace('+1t','+t').replace('-1t','-t')
            return content

