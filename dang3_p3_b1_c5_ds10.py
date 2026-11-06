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


def bt_dang3_p3_b1_c5_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                k=randint(1,9)
                ab=3*k
                ac=1*k
                bc=6*k
                bd=7*k
                be=2*k
                cd=4*k
                ce=5*k
                de=10*k
                df=9*k
                ef=8*k

                c1=ac
                b1=ab
                d1=c1+cd
                e1=b1+be
                f1=e1+ef

                h1=f1
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{
                                Khoảng cách (đơn vị: km) giữa các thành phố $A, B, C, D, E, F$ được mô tả trong
                                hình bên. Độ dài ngắn nhất để đi từ $A$ đến $F$ là bao nhiêu?
                                }{
            \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                \\clip(-0.5,-2) rectangle (5,1.5);
                \\draw [line width=1.pt] (0.,0.)-- (1.,1.);
                \\draw [line width=1.pt] (0.,0.)-- (1.,-1.);
                \\draw [line width=1.pt] (1.,1.)-- (3.,-1.);
                \\draw [line width=1.pt] (1.,-1.)-- (3.,1.);
                \\draw [line width=1.pt] (3.,1.)-- (4.,0.);
                \\draw [line width=1.pt] (4.,0.)-- (3.,-1.);
                \\draw [line width=1.pt] (1.,1.)-- (3.,1.);
                \\draw [line width=1.pt] (3.,1.)-- (3.,-1.);
                \\draw [line width=1.pt] (3.,-1.)-- (1.,-1.);
                \\draw [line width=1.pt] (1.,-1.)-- (1.,1.);
                \\draw (-0.6,0.34) node[anchor=north west] {$A$};
                \\draw (0.7,1.6) node[anchor=north west] {$B$};
                \\draw (0.7,-1) node[anchor=north west] {$C$};
                \\draw (2.8,1.6) node[anchor=north west] {$D$};
                \\draw (2.8,-1) node[anchor=north west] {$E$};
                \\draw (4,0.3) node[anchor=north west] {$F$};
                \\draw (0.1,-0.4) node[anchor=north west] {$%s$};
                \\draw (0.1,1) node[anchor=north west] {$%s$};
                \\draw (1,0.3) node[anchor=north west] {$%s$};
                \\draw (2,0.8) node[anchor=north west] {$%s$};
                \\draw (2,-0.3) node[anchor=north west] {$%s$};
                \\draw (2,-1) node[anchor=north west] {$%s$};
                \\draw (3.4,-0.4) node[anchor=north west] {$%s$};
                \\draw (3.5,1) node[anchor=north west] {$%s$};
                \\draw (3,0.3) node[anchor=north west] {$%s$};
                \\draw (1.8,1.5) node[anchor=north west] {$%s$};
                \\begin{scriptsize}
                    \\draw [fill=black] (0.,0.) circle (2.0pt);
                    \\draw [fill=black] (1.,1.) circle (2.0pt);
                    \\draw [fill=black] (1.,-1.) circle (2.0pt);
                    \\draw [fill=black] (3.,-1.) circle (2.0pt);
                    \\draw [fill=black] (3.,1.) circle (2.0pt);
                    \\draw [fill=black] (4.,0.) circle (2.0pt);
                \\end{scriptsize}
            \\end{tikzpicture}
                                }'''
                                %(latex(ac),latex(ab),latex(bc),latex(cd),latex(be),latex(ce),latex(ef),latex(df),latex(de),latex(bd)
                                ))

                # Nội dung lời giải
                loigiai = ('''Bước 1: \\\\
                        Gán vị trí $A$ nhãn vĩnh viễn bằng $0$, các đỉnh kề của $A$ là $B$ và $C$. \\\\ 
                        Ta gán một nhãn tạm thời vào $B$ là $%s$ và $C$ là $%s$. \\\\
                            Trong hai nhãn tạm thời trên ta thấy nhãn tại $C$ nhỏ hơn nên ta lấy nhẫn vĩnh viễn tại điểm $C$ là $%s$. \\\\
                            Bước 2: \\\\
                                Xuất phát từ $C$ ta tìm các đỉnh kề với $C$ mà chưa được gán nhãn vĩnh viễn là $B, D, E$. \\\\
                            Ta gán một nhãn tạm thời vào $B$ là $%s$, $D$ là $%s$ và $E$ là $%s$. \\\\
                                Trong các nhãn tạm thời ta thấy nhãn tại $B$ nhỏ hơn nên ta lấy nhẫn vĩnh viễn tại điểm $B$ là $%s$. \\\\
                        Bước 3: \\\\
                            Xuất phát từ $B$ ta tìm các đỉnh kề với $B$ mà chưa được gán nhãn vĩnh viễn là $D, E$. \\\\
                        Ta gán một nhãn tạm thời vào $D$ là $%s$ và $E$ là $%s$. \\\\
                            Trong các nhãn tạm thời ta lấy nhẫn vĩnh viễn tại điểm $D$ là $%s$ và $E$ là $%s$. \\\\
                            Bước 4: \\\\
                                Khi đó đỉnh $F$ có hai nhãn tạm thời là $%s$ và $%s$. \\\\
                                    Suy ra nhãn vĩnh viễn tại điểm $F$ là $%s$. \\\\
                            Vậy quãng đường ngắn nhất đi từ $A$ đến $F$ là $%s$ km.'''

                        %(latex(ab),latex(ac),
                        latex(ac),
                        latex(ac+bc),latex(ac+cd),latex(ac+ce),
                        latex(ab),
                        latex(ab+bd),latex(ab+be),
                        latex(d1),latex(e1),
                        latex(d1+df),latex(e1+ef),
                        latex(f1),
                        latex(f1)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(f1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

