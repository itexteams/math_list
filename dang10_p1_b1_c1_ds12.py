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


def bt_dang10_p1_b1_c1_ds12(self):
            # Khai báo biến
            x1=randint(-20,20)
            i1=randint(1,5)
            x2=x1+i1
            i2=randint(1,5)
            x3=x2+i2
            while x1==0 or x2==0 or x3==0:
                x1=randint(-20,20)
                i1=randint(1,5)
                x2=x1+i1
                i2=randint(1,5)
                x3=x2+i2
            lisdang=['1','2','3','4','5','6']
            dang=random.choice(lisdang)
            if dang=='6':
                d = ['$(%s;%s)$' %(latex(x1),latex(x3)),
                    '$(%s;%s)$' %(latex(x1),latex(x2)),
                    '$(%s;%s)$' %(latex(x2),latex(x3)),
                    ]
                da= random.choice(d)
                s = [ 
                    '$(-\\infty;%s)$' %(latex(x2)),
                    '$(-\\infty;%s)$' %(latex(x3)),
                    '$(%s;+\\infty)$' %(latex(x2)),
                    '$(%s;+\\infty)$' %(latex(x1)), 
                    '$(-\\infty;%s)$' %(latex(x1)),
                    '$(-\\infty;%s)$' %(latex(x1-i1)),
                    '$(%s;+\\infty)$' %(latex(x3)),
                    '$(%s;+\\infty)$' %(latex(x3+i1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đạo hàm $f\'(x)=(x+%s)(x+%s)^2(x+%s)^3, \\forall x\\in \\mathbb{R}$. Hàm số đã cho nghịch biến trên khoảng nào dưới đây?   \n'
                                %(latex(-x1),latex(-x2),latex(-x3) )   )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,+,0,-,0,-,0,+,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy hàm số nghịch biến trên khoảng $(%s;%s)$. \\\\ \n'
                        %(latex(x1),latex(x2),latex(x3),
                        latex(x1),latex(x2), latex(x3),
                        latex(x1), latex(x3),
                        ))
            if dang=='5':
                d = ['$(-\\infty;%s)$' %(latex(x1)),
                    '$(-\\infty;%s)$' %(latex(x1-i1)),
                    '$(%s;+\\infty)$' %(latex(x3)),
                    '$(%s;+\\infty)$' %(latex(x3+i1)),
                    ]
                da= random.choice(d)
                s = [ 
                    '$(-\\infty;%s)$' %(latex(x2)),
                    '$(-\\infty;%s)$' %(latex(x3)),
                    '$(%s;+\\infty)$' %(latex(x2)),
                    '$(%s;+\\infty)$' %(latex(x1)),
                    '$(%s;%s)$' %(latex(x1),latex(x3)), 
                    '$(%s;%s)$' %(latex(x1),latex(x2)),
                    '$(%s;%s)$' %(latex(x2),latex(x3)),  
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đạo hàm $f\'(x)=(x+%s)(x+%s)^2(x+%s)^3, \\forall x\\in \\mathbb{R}$. Hàm số đã cho đồng biến trên khoảng nào dưới đây?   \n'
                                %(latex(-x1),latex(-x2),latex(-x3) )   )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,+,0,-,0,-,0,+,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy hàm số đồng biến trên khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$. \\\\ \n'
                        %(latex(x1),latex(x2),latex(x3),
                        latex(x1),latex(x2), latex(x3),
                        latex(x1), latex(x3),
                        ))
            if dang=='4':
                d = ['$(-\\infty;%s)$' %(latex(x1-i1)),
                    '$(-\\infty;%s)$' %(latex(x1)),
                    '$(%s;%s)$' %(latex(x2),latex(x3)), 
                    ]
                da= random.choice(d)
                s = [ 
                    '$(-\\infty;%s)$' %(latex(x2)),
                    '$(-\\infty;%s)$' %(latex(x3)),
                    '$(%s;+\\infty)$' %(latex(x2)),
                    '$(%s;+\\infty)$' %(latex(x1)),
                    '$(%s;%s)$' %(latex(x1),latex(x3)), 
                    '$(%s;%s)$' %(latex(x1),latex(x2)),  
                    '$(%s;+\\infty)$' %(latex(x3)),
                    '$(%s;+\\infty)$' %(latex(x3+i1)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đạo hàm $f\'(x)=(x+%s)(x+%s)(x+%s), \\forall x\\in \\mathbb{R}$. Hàm số đã cho nghịch biến trên khoảng nào dưới đây?   \n'
                                %(latex(-x1),latex(-x2),latex(-x3) )   )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy hàm số nghịch biến trên khoảng $(-\\infty;%s)$ và $(%s;%s)$. \\\\ \n'
                        %(latex(x1),latex(x2),latex(x3),
                        latex(x1),latex(x2), latex(x3),
                        latex(x1),latex(x2), latex(x3),
                        ))
            if dang=='3':
                d = ['$(%s;%s)$' %(latex(x1),latex(x2)),  
                    '$(%s;+\\infty)$' %(latex(x3)),
                    '$(%s;+\\infty)$' %(latex(x3+i1)),
                    ]
                da= random.choice(d)
                s = ['$(-\\infty;%s)$' %(latex(x1)),
                    '$(%s;%s)$' %(latex(x2),latex(x3)),  
                    '$(-\\infty;%s)$' %(latex(x2)),
                    '$(-\\infty;%s)$' %(latex(x3)),
                    '$(%s;+\\infty)$' %(latex(x2)),
                    '$(%s;+\\infty)$' %(latex(x1)),
                    '$(%s;%s)$' %(latex(x1),latex(x3)),  

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đạo hàm $f\'(x)=(x+%s)(x+%s)(x+%s), \\forall x\\in \\mathbb{R}$. Hàm số đã cho đồng biến trên khoảng nào dưới đây?  \n'
                                %(latex(-x1),latex(-x2),latex(-x3) )   )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy hàm số đồng biến trên khoảng $(%s;%s)$ và $(%s;+\\infty)$. \\\\ \n'
                        %(latex(x1),latex(x2),latex(x3),
                        latex(x1),latex(x2), latex(x3),
                        latex(x1),latex(x2), latex(x3),
                        ))
            if dang=='2':
                d = ['$(%s;%s)$' %(latex(x1),latex(x2)),  
                    ]
                da= random.choice(d)
                s = ['$(-\\infty;%s)$' %(latex(x1)),
                    '$(%s;+\\infty)$' %(latex(x2)),
                    '$(-\\infty;%s)$' %(latex(x2)),
                    '$(%s;+\\infty)$' %(latex(x1)),
                    '$(%s;+\\infty)$' %(latex(x2)),
                    '$(-\\infty;%s)$' %(latex(x1+i1)),
                    '$(%s;+\\infty)$' %(latex(x2-i1)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đạo hàm $f\'(x)=(x+%s)(x+%s), \\forall x\\in \\mathbb{R}$. Hàm số đã cho nghịch biến trên khoảng nào dưới đây?  \n'
                                %(latex(-x1),latex(-x2) )   )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,+,0,-,0,+,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy hàm số đồng biến trên khoảng $(%s;%s)$. \\\\ \n'
                        %(latex(x1),latex(x2), 
                        latex(x1),latex(x2), 
                        latex(x1),latex(x2), 
                        ))
            if dang=='1':
                d = ['$(-\\infty;%s)$' %(latex(x1)),
                    '$(-\\infty;%s)$' %(latex(x1-i1)),
                    '$(%s;+\\infty)$' %(latex(x2)),
                    '$(%s;+\\infty)$' %(latex(x2+i1)),    
                    ]
                da= random.choice(d)
                s = ['$(-\\infty;%s)$' %(latex(x2)),
                    '$(%s;+\\infty)$' %(latex(x1)),
                    '$(%s;%s)$' %(latex(x1),latex(x2)),
                    '$(-\\infty;%s)$' %(latex(x1+6)),
                    '$(%s;+\\infty)$' %(latex(x2-6)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đạo hàm $f\'(x)=(x+%s)(x+%s), \\forall x\\in \\mathbb{R}$. Hàm số đã cho đồng biến trên khoảng nào dưới đây?  \n'
                                %(latex(-x1),latex(-x2) )   )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,+,0,-,0,+,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy hàm số đồng biến trên khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$. \\\\ \n'
                        %(latex(x1),latex(x2), 
                        latex(x1),latex(x2), 
                        latex(x1),latex(x2), 
                        ))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')
            return content

