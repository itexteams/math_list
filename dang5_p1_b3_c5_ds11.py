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


def bt_dang5_p1_b3_c5_ds11(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(2,9)
                b=Rational(1,a)


                du = ['$y=\\left(%s\\right)^x$'%(latex(b)),
                    ]
                da= random.choice(du)
                s = ['$y=%s^x$'%(latex(a)),
                    '$y=\\log_%s x$'%(latex(a)),
                    '$y=\\log_{\\tfrac{1}{%s}} x$'%(latex(a)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Hình vẽ bên là đồ thị của hàm số nào sau đây?'
                                '}{'
                                '''
                                \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
                                \\scalebox{0.8}{ 
                            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                                    \\clip(-2.1318916133261863,-0.9789768066127603) rectangle (3.8453597807200888,3.716579398730203);
                                    \\draw[line width=1.pt,color=ffqqqq,smooth,samples=100,domain=-2.1318916133261863:3.8453597807200888] plot(\\x,{0.5^((\\x))});
                                    \\draw [line width=1.pt,dashed] (1.,0.5)-- (1.,0.);
                                    \\draw [line width=1.pt,dashed] (1.,0.5)-- (0.,0.5114867630424972);
                                    \\draw [->,line width=1.pt] (-2.1318916133261863,0.) -- (3.7734890224750433,0.);
                                    \\draw [->,line width=1.pt] (0.,-1.) -- (0.,3.7046009390226953);
                                    \\draw (-0.6,0.05117072823288984) node[anchor=north west] {$O$};
                                    \\draw (3.4,0) node[anchor=north west] {$x$};
                                    \\draw (-0.56,3.7) node[anchor=north west] {$y$};
                                    \\draw (0.8,0.05117072823288984) node[anchor=north west] {$1$};
                                    \\draw (-0.5,0.9615336660034643) node[anchor=north west] {$\\tfrac{1}{%s}$};
                                    \\draw (0,1.4) node[anchor=north west] {$1$};
                            \\end{tikzpicture} }
                                '''
                                '}'
                                %(latex(a)
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
                loigiai=('Từ hình vẽ ta thấy\\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số đi qua điểm $(0;1)$ và $\\left(1; %s\\right)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến. \\\\ \n'
                        'Suy ra hình vẽ là đồ thị của hàm số $y=\\left(%s\\right)^x$.'
                        %(latex(b),latex(b)
                        ))

            if dang=='2':
                a=randint(2,9)
                b=Rational(1,a)


                du = ['$y=%s^x$'%(latex(a)),
                    ]
                da= random.choice(du)
                s = ['$y=\\left(%s\\right)^x$'%(latex(b)),
                    '$y=\\log_%s x$'%(latex(a)),
                    '$y=\\log_{\\tfrac{1}{%s}} x$'%(latex(a)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Hình vẽ bên là đồ thị của hàm số nào sau đây?'
                                '}{'
                                '''
                                \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
                                \\scalebox{0.8}{ 
                            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                                    \\clip(-3.,-0.98) rectangle (3.42,5);
                                    \\draw[line width=1.pt,color=ffqqqq,smooth,samples=100,domain=-3.000000000000001:3.4200000000000013] plot(\\x,{2.0^((\\x))});
                                    \\draw [line width=1.pt,dashed] (1.,2.)-- (1.,0.);
                                    \\draw [line width=1.pt,dashed] (1.,2.)-- (0.,2.);
                                    \\draw [->,line width=1.pt] (-3.,0.) -- (3.,0.);
                                    \\draw [->,line width=1.pt] (0.,-1.) -- (0.,5.);
                                    \\draw (-0.58,0) node[anchor=north west] {$O$};
                                    \\draw (2.52,0) node[anchor=north west] {$x$};
                                    \\draw (-0.52,5.) node[anchor=north west] {$y$};
                                    \\draw (0.75,0.06) node[anchor=north west] {$1$};
                                    \\draw (-0.58,2.22) node[anchor=north west] {$%s$};
                                    \\draw (-0.46,1.62) node[anchor=north west] {$1$};
                            \\end{tikzpicture} }
                                '''
                                '}'
                                %(latex(a)
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
                loigiai=('Từ hình vẽ ta thấy\\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số đi qua điểm $(0;1)$ và $\\left(1; %s\\right)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến. \\\\ \n'
                        'Suy ra hình vẽ là đồ thị của hàm số $y=%s^x$.'
                        %(latex(a),latex(a)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

