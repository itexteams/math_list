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


def bt_dang2_p3_b4_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                lis1=[1,4,9,16]
                j=random.choice(lis1)
                i=randint(6,10)
                m=randint(1,5)
                ab=2*i+1
                ah=randint(2,5)
                cd=ab-2*ah
                a=randint(1,9)
                b=a+m
                bc=sqrt(ah**2+j)
                bk=ah
                ck=sqrt(bc**2-bk**2)
                s_abcd=Rational(ab*ck+cd*ck,2)
                k=Rational(a,b)
                h1=k**2*s_abcd
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình chóp $S$zz$ABCD$ có đáy $ABCD$ là hình thang cân, cạnh bên $BC = %s$, hai đáy $AB = %s, CD = %s$$zz$ Mặt phẳng $(\\alpha)$ song song với $(ABCD)$ và cắt cạnh $SO$ tại $I$ sao cho $%sSO = %sSI$$zz$ Diện tích thiết diện tạo bởi mặt phẳng $(\\alpha)$ và hình chóp bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)$zz$ \n'
                                %(latex(bc),latex(ab),latex(cd),latex(a),latex(b)
                                ))

                # Nội dung lời giải
                loigiai = (

            '\\begin{center} \n'
                '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1$zz$0cm,y=1$zz$0cm] \n'
                    '\\clip(-1$zz$044812183895418,-1$zz$0748755369904883) rectangle (13$zz$300567505012086,5$zz$879745676202135); \n'
                    '\\draw (0$zz$,0$zz$)-- (4$zz$,0$zz$); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,1$zz$)-- (7$zz$,1$zz$); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,1$zz$)-- (0$zz$,0$zz$); \n'
                    '\\draw (4$zz$,0$zz$)-- (7$zz$,1$zz$); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,5$zz$)-- (2$zz$,1$zz$); \n'
                    '\\draw (2$zz$,5$zz$)-- (0$zz$,0$zz$); \n'
                    '\\draw (2$zz$,5$zz$)-- (4$zz$,0$zz$); \n'
                    '\\draw (2$zz$,5$zz$)-- (7$zz$,1$zz$); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,1$zz$)-- (4$zz$,0$zz$); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (0$zz$,0$zz$)-- (7$zz$,1$zz$); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (3$zz$111111111111111,0$zz$4444444444444444)-- (2$zz$,5$zz$); \n'
                    '\\draw (1$zz$1964601335653928,2$zz$991150333913482)-- (2$zz$795219673226293,3$zz$0119508169342684); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (1$zz$1964601335653928,2$zz$991150333913482)-- (2$zz$,3$zz$4043720240488273); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,3$zz$4043720240488273)-- (4$zz$008073134658506,3$zz$393541492273195); \n'
                    '\\draw (4$zz$008073134658506,3$zz$393541492273195)-- (2$zz$795219673226293,3$zz$0119508169342684); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,3$zz$4043720240488273)-- (2$zz$795219673226293,3$zz$0119508169342684); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (1$zz$1964601335653928,2$zz$991150333913482)-- (4$zz$008073134658506,3$zz$393541492273195); \n'
                    '\\draw (8$zz$,0$zz$)-- (12$zz$,0$zz$); \n'
                    '\\draw (8$zz$,0$zz$)-- (9$zz$,2$zz$); \n'
                    '\\draw (9$zz$,2$zz$)-- (11$zz$,2$zz$); \n'
                    '\\draw (11$zz$,2$zz$)-- (12$zz$,0$zz$); \n'
                    '\\draw (9$zz$,2$zz$)-- (9$zz$,0$zz$); \n'
                    '\\draw (11$zz$,2$zz$)-- (11$zz$,0$zz$); \n'
                    '\\draw (1$zz$8,5$zz$5) node[anchor=north west] {S}; \n'
                    '\\draw (1$zz$5,1$zz$5) node[anchor=north west] {A}; \n'
                    '\\draw (7$zz$088558387465451,1$zz$3) node[anchor=north west] {B}; \n'
                    '\\draw (3$zz$870572639666151,0) node[anchor=north west] {C}; \n'
                    '\\draw (-0$zz$5,0) node[anchor=north west] {D}; \n'
                    '\\draw (2$zz$7,0$zz$5) node[anchor=north west] {O}; \n'
                    '\\draw (2$zz$3,3$zz$6) node[anchor=north west] {I}; \n'
                    '\\draw (1$zz$4,3$zz$8) node[anchor=north west] {M}; \n'
                    '\\draw (4$zz$047385043391387,3$zz$8) node[anchor=north west] {N}; \n'
                    '\\draw (2$zz$998298114621652,3) node[anchor=north west] {P}; \n'
                    '\\draw (0$zz$6,3$zz$2) node[anchor=north west] {Q}; \n'
                    '\\draw (7$zz$5,0) node[anchor=north west] {A}; \n'
                    '\\draw (12,0) node[anchor=north west] {B}; \n'
                    '\\draw (10$zz$8,2$zz$5) node[anchor=north west] {C}; \n'
                    '\\draw (8$zz$573782578757436,2$zz$5) node[anchor=north west] {D}; \n'
                    '\\draw (8$zz$83310743755445,0) node[anchor=north west] {H}; \n'
                    '\\draw (10$zz$860556333603824,0) node[anchor=north west] {K}; \n'
                '\\end{tikzpicture}  \n'
            '\\end{center}  \n'

                            'Gọi $H, K$ lần lượt là hình chiếu vuông góc của $D, C$ lên $AB$$zz$ \\\\ \n'
                            'Vì $ABCD$ là hình thang cân nên $AH = BK = \\frac{AB-HK}{2} = \\frac{AB-CD}{2} = \\frac{%s-%s}{2} = %s$$zz$\\\\ \n'
                            'Ta có $CK = \\sqrt{BC^2 - BK^2} = \\sqrt{(%s)^2 - %s^2} = %s$$zz$\\\\ \n'
                            'Suy ra diện tích hình thang $ABCD$ là $S_{ABCD} = \\frac{(AB+CD)\\cdot CK}{2} = \\frac{(%s+%s)\\cdot %s}{2} = %s$$zz$\\\\ \n'
                            'Gọi $M, N, P, Q$ lần lượt là giao điểm của $(\\alpha)$ và các cạnh $SA, SB, SC, SD$$zz$\\\\ \n'
                            'Vì $(\\alpha)$ song song với $(ABCD)$ \\\\ \n'
                            'Nên theo định lí Thales, ta có $\\frac{SM}{SA} = \\frac{SN}{SB} = \\frac{SP}{SC} = \\frac{SQ}{SD} = \\frac{SI}{SO} = %s=k$$zz$\\\\ \n'
                            'Vậy diện tích thiết diện tạo bởi mặt phẳng $(\\alpha)$ và hình chóp là \\\\ \n'
                            '$S_{MNPQ} = k^2 \\cdot S_{ABCD} = \\left(%s\\right)^2 \\cdot %s = %s$$zz$'
                        %(latex(ab),latex(cd),latex(ah),
                            latex(bc),latex(bk),latex(ck),
                            latex(ab),latex(cd),latex(ck),latex(s_abcd),
                            latex(k),
                            latex(k),latex(s_abcd),latex(kq)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content                

