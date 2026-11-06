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


def bt_dang6_p1_b3_c4_ds10(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6']
            dang=random.choice(lisdang)

            if dang=='1':
                #Khai báo biến
                x1=randint(1,10)
                x2=4*x1
                c=4*x1
                # Câu hỏi
                noidungcauhoi = ('\\immini{Cho hàm số $y=f(x)=ax^2+bx+c$. Đặt $\\Delta=b^2-4ac$, xác định dấu của $a$ và $\\Delta$}'
                                '{'
                                '''\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,scale=0.6]
                \\draw[->,color=black] (-1.7,0.) -- (6.04,0.);
                \\foreach \\x in {}
                \\draw[shift={(\\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\\footnotesize $\\x$};
                \\draw[->,color=black] (0.,-2.86) -- (0.,4.54);
                \\foreach \\y in {.}
                \\draw[shift={(0,\\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\\footnotesize $\\y$};
                \\clip(-1.7,-2.5) rectangle (6.04,4.5);
                \\draw [samples=50,rotate around={0.:(2.5,-2.25)},xshift=2.5cm,yshift=-2.25cm,domain=-4.0:4.0)] plot (\\x,{(\\x)^2/2/0.5});
                \\draw[color=black] (-0.4,-0.4) node {$O$};
                \\draw[color=black] (0.6,-0.4) node {$%s$};
                \\draw[color=black] (4+0.2,-0.5) node {$%s$};
                \\draw[color=black] (-0.5,4) node {$%s$};
                \\draw[color=black] (5.7,-0.3) node {$x$};
                \\draw[color=black] (0.3,4.2) node {$y$};
            \\end{tikzpicture}}'''

                %(latex(x1),
                latex(x2),
                latex(c)))

                # Nội dung lời giải
                loigiai=('Đồ thị hàm số là một Parabol có bề lõm quay lên trên nên $a>0$ và đồ thị hàm số cắt trục $Ox$ tại hai điểm phân biệt nên $\\Delta>0$.'
                        )

                du = ['$a>0;\\Delta>0$',

                    ]
                da= random.choice(du)
                s = ['$a<0;\\Delta>0$',
                    '$a>0;\\Delta<0$',
                    '$a<0;\\Delta<0$',
                    '$a>0;\\Delta\\le0$',
                    '$a>0;\\Delta\\ge0$',

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
                #Khai báo biến
                x1=randint(1,10)
                x2=2*x1

                # Câu hỏi
                noidungcauhoi = ('\\immini{Cho hàm số $y=f(x)=ax^2+bx+c$. Đặt $\\Delta=b^2-4ac$, xác định dấu của $a$ và $\\Delta$}'
                                '{'
                                '''\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,scale=0.6]
                \\draw[->,color=black] (-0.96,0.) -- (4.68,0.);
                \\foreach\\x in {}
                \\draw[shift={(\\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\\footnotesize $\\x$};
                \\draw[->,color=black] (0.,-0.82) -- (0.,5.44);
                \\foreach \\y in {}
                \\draw[shift={(0,\\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\\footnotesize $\\y$};
                \\clip(-0.96,-0.82) rectangle (4.68,5.44);
                \\draw [samples=50,rotate around={0.:(2.,0.)},xshift=2.cm,yshift=0.cm,domain=-4.0:4.0)] plot (\\x,{(\\x)^2/2/0.5});
                \\draw[color=black] (-0.4,-0.4) node {$O$};
                \\draw[color=black] (2,-0.4) node {$%s$};
                \\draw[color=black] (-0.4,4) node {$%s$};
                \\draw[color=black] (4.5,-0.3) node {$x$};
                \\draw[color=black] (0.3,5) node {$y$};
            \\end{tikzpicture}}'''

                %(latex(x1),
                latex(x2),
            ))

                # Nội dung lời giải
                loigiai=('Đồ thị hàm số là một Parabol có bề lõm quay lên trên nên $a>0$ và đồ thị hàm số tiếp xúc trục $Ox$ nên $\\Delta=0$.'
                        )

                du = ['$a>0;\\Delta=0$',

                    ]
                da= random.choice(du)
                s = ['$a>0;\\Delta>0$',
                    '$a>0;\\Delta<0$',
                    '$a<0;\\Delta<0$',
                    '$a>0;\\Delta\\le0$',
                    '$a>0;\\Delta\\ge0$',

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
                #Khai báo biến
                x1=randint(1,10)
                x2=2*x1

                # Câu hỏi
                noidungcauhoi = ('\\immini{Cho hàm số $y=f(x)=ax^2+bx+c$. Đặt $\\Delta=b^2-4ac$, xác định dấu của $a$ và $\\Delta$}'
                                '{'
                                '''\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,scale=0.6]
                \\draw[->,color=black] (-1.38,0.) -- (5.12,0.);
                \\foreach \\x in {}
                \\draw[shift={(\\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\\footnotesize $\\x$};
                \\draw[->,color=black] (0.,-0.88) -- (0.,6.4);
                \\foreach \\y in {}
                \\draw[shift={(0,\\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\\footnotesize $\\y$};
                \\clip(-1.38,-0.88) rectangle (5.12,6.4);
                \\draw [samples=50,rotate around={0.:(2.,1.)},xshift=2.cm,yshift=1.cm,domain=-4.0:4.0)] plot (\\x,{(\\x)^2/2/0.5});
                \\draw[color=black] (-0.5,-0.5) node {$O$};
                \\draw[color=black] (-0.5,5) node {$%s$};
                \\draw[color=black] (5,-0.3) node {$x$};
                \\draw[color=black] (0.3,6.3) node {$y$};
            \\end{tikzpicture}}'''

                %(latex(x1),

            ))

                # Nội dung lời giải
                loigiai=('Đồ thị hàm số là một Parabol có bề lõm quay lên trên nên $a>0$ và đồ thị hàm số không cắt trục $Ox$ nên $\\Delta<0$.'
                        )

                du = ['$a>0;\\Delta<0$',

                    ]
                da= random.choice(du)
                s = ['$a>0;\\Delta>0$',
                    '$a>0;\\Delta=0$',
                    '$a<0;\\Delta<0$',
                    '$a>0;\\Delta\\le0$',
                    '$a>0;\\Delta\\ge0$',

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

            if dang=='4':
                #Khai báo biến
                x1=randint(1,10)
                x2=3*x1
                c=3*x1
                # Câu hỏi
                noidungcauhoi = ('\\immini{Cho hàm số $y=f(x)=ax^2+bx+c$. Đặt $\\Delta=b^2-4ac$, xác định dấu của $a$ và $\\Delta$}'
                                '{'
                                '''\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,scale=0.6]
                \\draw[->,color=black] (-4.62,0.) -- (2.74,0.);
                \\foreach \\x in {}
                \\draw[shift={(\\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\\footnotesize $\\x$};
                \\draw[->,color=black] (0.,-1.48) -- (0.,4.62);
                \\foreach \\y in {}
                \\draw[shift={(0,\\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\\footnotesize $\\y$};
                \\clip(-4.62,-1.48) rectangle (2.74,4.62);
                \\draw [samples=50,rotate around={-180.:(-1.,4.)},xshift=-1.cm,yshift=4.cm,domain=-4.0:4.0)] plot (\\x,{(\\x)^2/2/0.5});
                \\draw[color=black] (-0.4,-0.4) node {$O$};
                \\draw[color=black] (-0.4,3) node {$%s$};
                \\draw[color=black] (-3.9,-0.3) node {$%s$};
                \\draw[color=black] (1.4,-0.3) node {$%s$};
                \\draw[color=black] (2.6,-0.3) node {$x$};
                \\draw[color=black] (-0.2,4.4) node {$y$};

            \\end{tikzpicture}}'''

                %(latex(c),
                latex(-x2),
                latex(x1)))

                # Nội dung lời giải
                loigiai=('Đồ thị hàm số là một Parabol có bề lõm quay xuống dưới nên $a<0$ và đồ thị hàm số cắt trục $Ox$ tại hai điểm phân biệt nên $\\Delta>0$.'
                        )

                du = ['$a<0;\\Delta>0$',

                    ]
                da= random.choice(du)
                s = ['$a>0;\\Delta>0$',
                    '$a>0;\\Delta<0$',
                    '$a<0;\\Delta<0$',
                    '$a<0;\\Delta\\le0$',
                    '$a<0;\\Delta\\ge0$',

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

            if dang=='5':
                #Khai báo biến
                x1=randint(1,10)
                x2=3*x1
                c=3*x1
                # Câu hỏi
                noidungcauhoi = ('\\immini{Cho hàm số $y=f(x)=ax^2+bx+c$. Đặt $\\Delta=b^2-4ac$, xác định dấu của $a$ và $\\Delta$}'
                                '{'
                                '''\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,scale=0.6]
                \\draw[->,color=black] (-4.74,0.) -- (1.24,0.);
                \\foreach \\x in {}
                \\draw[shift={(\\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\\footnotesize $\\x$};
                \\draw[->,color=black] (0.,-5.72) -- (0.,1.12);
                \\foreach \\y in {}
                \\draw[shift={(0,\\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\\footnotesize $\\y$};
                \\clip(-4.74,-5.72) rectangle (1.24,1.12);
                \\draw [samples=50,rotate around={-180.:(-2.,0.)},xshift=-2.cm,yshift=0.cm,domain=-4.0:4.0)] plot (\\x,{(\\x)^2/2/0.5});
                \\draw[color=black] (-0.4,-0.4) node {$O$};
                \\draw[color=black] (-2,-0.5) node {$%s$};
                \\draw[color=black] (-0.7,-4) node {$%s$};
                \\draw[color=black] (1,-0.3) node {$x$};
                \\draw[color=black] (-0.3,1) node {$y$};
            \\end{tikzpicture}}'''

                %(latex(-x1),
                latex(-2*x1),
            ))

                # Nội dung lời giải
                loigiai=('Đồ thị hàm số là một Parabol có bề lõm quay xuống dưới nên $a<0$ và đồ thị hàm số tiếp xúc với trục $Ox$ nên $\\Delta=0$.'
                        )

                du = ['$a<0;\\Delta=0$',

                    ]
                da= random.choice(du)
                s = ['$a>0;\\Delta=0$',
                    '$a<0;\\Delta>0$',
                    '$a<0;\\Delta<0$',
                    '$a<0;\\Delta\\le0$',
                    '$a<0;\\Delta\\ge0$',

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

            if dang=='6':
                #Khai báo biến
                x1=randint(1,10)
                x2=3*x1
                c=3*x1
                # Câu hỏi
                noidungcauhoi = ('\\immini{Cho hàm số $y=f(x)=ax^2+bx+c$. Đặt $\\Delta=b^2-4ac$, xác định dấu của $a$ và $\\Delta$}'
                                '{'
                                '''\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,scale=0.6]
                \\draw[->,color=black] (-1.56,0.) -- (4.48,0.);
                \\foreach \\x in {}
                \\draw[shift={(\\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\\footnotesize $\\x$};
                \\draw[->,color=black] (0.,-4.58) -- (0.,1.42);
                \\foreach \\y in {}
                \\draw[shift={(0,\\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\\footnotesize $\\y$};
                \\clip(-1.56,-4.58) rectangle (4.48,1.42);
                \\draw [samples=50,rotate around={-180.:(1.5,-0.75)},xshift=1.5cm,yshift=-0.75cm,domain=-3.0:3.0)] plot (\\x,{(\\x)^2/2/0.5});
                \\draw[color=black] (-0.7,-3) node {$%s$};
                \\draw[color=black] (4.2,-0.3) node {$x$};
                \\draw[color=black] (-0.3,1.2) node {$y$};
            \\end{tikzpicture}}'''

                %(latex(-x1),

            ))

                # Nội dung lời giải
                loigiai=('Đồ thị hàm số là một Parabol có bề lõm quay xuống dưới nên $a<0$ và đồ thị hàm số không cắt trục $Ox$ nên $\\Delta<0$.'
                        )

                du = ['$a<0;\\Delta<0$',

                    ]
                da= random.choice(du)
                s = ['$a<0;\\Delta=0$',
                    '$a>0;\\Delta<0$',
                    '$a>0;\\Delta<0$',
                    '$a<0;\\Delta\\le0$',
                    '$a<0;\\Delta\\ge0$',

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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

