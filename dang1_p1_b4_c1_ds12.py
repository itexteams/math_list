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


def bt_dang1_p1_b4_c1_ds12(self):
            lisdang=['1','2']
            dang=random.choice(lisdang)
            # Khai báo biến
            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                x1=randint(-9,9)
                i=randint(1,5)
                x2=x1+i
                k=randint(1,3)
                a=-3*k
                hs_a=Rational(a,3)
                hs_b=Rational(-a*x1-a*x2,2)
                hs_c=a*x1*x2
                hs_d=randint(-9,9)

                f=hs_a*x**3+hs_b*x**2+hs_c*x+hs_d
                f1=hs_a*x1**3+hs_b*x1**2+hs_c*x1+hs_d
                f2=hs_a*x2**3+hs_b*x2**2+hs_c*x2+hs_d

                a1=randint(-9,9)
                while a1==0:
                    a1=randint(-9,9)
                b1=randint(-9,9)
                c1=randint(-9,9)
                f_b4=a1*x**4+b1*x**2+c1

                du = ['$y=%s$'%(latex(f)),
                    ]
                da= random.choice(du)
                s = ['$y=%s$'%(latex(-f)),
                    '$y=%s$'%(latex(f_b4)),
                    '$y=%s$'%(latex(-f_b4)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Hàm số nào có bảng biến thiên như sau?  \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                '\\tkzTabLine{,-,0,+,0,-,} \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$}  \n'
                                '\\end{tikzpicture} \n'
                                '\\end{center}'
                                %(latex(x1),latex(x2),
                                latex(f1),latex(f2),
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
                loigiai=('Từ bảng biến thiên ta thấy\\\\ \n'
                        '\\hspace*{1cm} Bảng biến thiên của hàm số bậc ba dạng $y=ax^3+bx^2+cx+d$ với $a \\ne 0$. \\\\ \n'
                        '\\hspace*{1cm} Khoảng ngoài cùng bên phải nghịch biến nên hệ số $a<0$.'
                        )

            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                x1=randint(-9,9)
                i=randint(1,5)
                x2=x1+i
                k=randint(1,3)
                a=3*k
                hs_a=Rational(a,3)
                hs_b=Rational(-a*x1-a*x2,2)
                hs_c=a*x1*x2
                hs_d=randint(-9,9)

                f=hs_a*x**3+hs_b*x**2+hs_c*x+hs_d
                f1=hs_a*x1**3+hs_b*x1**2+hs_c*x1+hs_d
                f2=hs_a*x2**3+hs_b*x2**2+hs_c*x2+hs_d

                a1=randint(-9,9)
                while a1==0:
                    a1=randint(-9,9)
                b1=randint(-9,9)
                c1=randint(-9,9)
                f_b4=a1*x**4+b1*x**2+c1

                du = ['$y=%s$'%(latex(f)),
                    ]
                da= random.choice(du)
                s = ['$y=%s$'%(latex(-f)),
                    '$y=%s$'%(latex(f_b4)),
                    '$y=%s$'%(latex(-f_b4)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Hàm số nào có bảng biến thiên như sau?  \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                '\\tkzTabLine{,+,0,-,0,+,} \n'
                                '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$}  \n'
                                '\\end{tikzpicture} \n'
                                '\\end{center}'
                                %(latex(x1),latex(x2),
                                latex(f1),latex(f2),
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
                loigiai=('Từ bảng biến thiên ta thấy\\\\ \n'
                        '\\hspace*{1cm} Bảng biến thiên của hàm số bậc ba dạng $y=ax^3+bx^2+cx+d$ với $a \\ne 0$. \\\\ \n'
                        '\\hspace*{1cm} Khoảng ngoài cùng bên phải đồng biến nên hệ số $a>0$.'
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('1x', 'x').replace('+0x^2', '').replace('+0x', '').replace('+0', '')
            return content

