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


def bt_dang11_p1_b1_c4_ds10(self):
            #Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='2':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(-\\infty;0)$',    
                    '$(-2;-1)$',  
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Từ hình vẽ ta thấy đồ thị hàm số "đi xuống" từ trái sang phải trên khoảng $(-\\infty;0)$ nên hàm số nghịch biến.'),
                    ('Từ hình vẽ ta thấy đồ thị hàm số "đi xuống" từ trái sang phải trên khoảng $(-2;-1)$ nên hàm số nghịch biến.'),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(-\\infty;1)$',  
                    '$(-1;+\\infty)$',  
                    '$(-\\infty;2)$',  
                    '$(-2;1)$',  
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Cho hàm số $y=f(x)$ có đồ thị như hình vẽ. Hàm số nghịch biến trên khoảng nào dưới đây?'
                                '}{'
                                '''
                                \\definecolor{qqqqff}{rgb}{0.,0.,1.}
                                \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
                                \\scalebox{0.6}{ 
                                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                                        \\clip(-3.1317113187576133,-1.1471113294260182) rectangle (3.1615873372055425,5);
                                        \\draw [samples=50,rotate around={0.:(0.,0.)},xshift=0.cm,yshift=0.cm,line width=1.pt,color=ffqqqq,domain=-4.0:4.0)] plot (\\x,{(\\x)^2/2/0.5});
                                        \\draw [->,line width=1.pt,color=qqqqff] (0.,-1.) -- (0.,5.);
                                        \\draw [->,line width=1.pt,color=qqqqff] (-3.,0.) -- (3.,0.);
                                        \\draw (2.5,0) node[anchor=north west] {$x$};
                                        \\draw (-0.5,5.071139472036734) node[anchor=north west] {$y$};
                                        \\draw (-0.6,0) node[anchor=north west] {$O$};
                                \\end{tikzpicture}}
                                '''
                                '}'

                                %(
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
                loigiai= shuffled_solutions[0]

            if dang=='1':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(0;+\\infty)$',    
                    '$(1;2)$',  
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Từ hình vẽ ta thấy đồ thị hàm số "đi lên" từ trái sang phải trên khoảng $(0;+\\infty)$ nên hàm số đồng biến.'),
                    ('Từ hình vẽ ta thấy đồ thị hàm số "đi lên" từ trái sang phải trên khoảng $(1;2)$ nên hàm số đồng biến.'),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(-\\infty;0)$',  
                    '$(-1;+\\infty)$',  
                    '$(-\\infty;2)$',  
                    '$(-2;1)$',  
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Cho hàm số $y=f(x)$ có đồ thị như hình vẽ. Hàm số đồng biến trên khoảng nào dưới đây?'
                                '}{'
                                '''
                                \\definecolor{qqqqff}{rgb}{0.,0.,1.}
                                \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
                                \\scalebox{0.6}{ 
                                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                                        \\clip(-3.1317113187576133,-1.1471113294260182) rectangle (3.1615873372055425,5);
                                        \\draw [samples=50,rotate around={0.:(0.,0.)},xshift=0.cm,yshift=0.cm,line width=1.pt,color=ffqqqq,domain=-4.0:4.0)] plot (\\x,{(\\x)^2/2/0.5});
                                        \\draw [->,line width=1.pt,color=qqqqff] (0.,-1.) -- (0.,5.);
                                        \\draw [->,line width=1.pt,color=qqqqff] (-3.,0.) -- (3.,0.);
                                        \\draw (2.5,0) node[anchor=north west] {$x$};
                                        \\draw (-0.5,5.071139472036734) node[anchor=north west] {$y$};
                                        \\draw (-0.6,0) node[anchor=north west] {$O$};
                                \\end{tikzpicture}}
                                '''
                                '}'

                                %(
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
                loigiai= shuffled_solutions[0]


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

