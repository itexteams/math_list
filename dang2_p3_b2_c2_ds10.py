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


def bt_dang2_p3_b2_c2_ds10(self):
            # Khai báo biến
            x0 = randint(4,9) # b là số bất kỳ từ 1 đến 30
            y0 = randint(2,4) # b là số bất kỳ từ 1 đến 30
            a = randint(5,8) # b là số bất kỳ từ 1 đến 30
            b = randint(2,6) # b là số bất kỳ từ 1 đến 30
            c = randint(2,6) # b là số bất kỳ từ 1 đến 30
            d = randint(2,6)# b là số bất kỳ từ 1 đến 30
            e= randint(12,20)# b là số bất kỳ từ 1 đến 30
            while a>=x0+y0:
                x0 = randint(4,9) # b là số bất kỳ từ 1 đến 30
                y0 = randint(2,4) # b là số bất kỳ từ 1 đến 30
                a = randint(5,8) # b là số bất kỳ từ 1 đến 30
            T=x0+y0
            A1=a-y0
            B1=x0
            C1=x0*a

            gt0=0
            gta=c*0+d*a
            gtb=c*x0+d*y0
            gtc=c*T
            list2=[gt0,gta,gtb,gtc]
            ln=max(list2)
            nn=min(list2)
            list4=[2,-2]
            list3=['dang3']
            rd = random.choice(list3)
            rd4 = random.choice(list4)
            lista=['Khoai','Sắn','Cà tím','Dứa','Cà phê','Hành']
            listb=['Lúa','Ngô','Bưởi','Cam','Quýt']
            t1=random.choice(lista)
            t2=random.choice(listb)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một hộ nông dân định trồng %s và %s trên diện tích $%sha$. Trên diện tích mỗi $ha$,
                            nếu trồng %s thì cần $%s$ công và thu $%s$ triệu đồng,
                            nếu trồng %s thì cần $%s$ công và thu $%s$ triệu đồng.
                            Hỏi hộ nông dân đó có thể thu được số tiền (đơn vị: Triệu đồng) nhiều nhất là bao nhiêu, biết rằng tổng số công không quá $%s$? (kết quả làm tròn đến hàng phần chục).\\\\'''
                            %(str(t1),str(t2),latex(T),
                            str(t1),latex(A1*10),latex(c),
                            str(t2),latex(B1*10),latex(d),
                            latex(C1*10)))

                # Nội dung lời giải
            hinhve = f'''\\begin{{center}}
            \\begin{{tikzpicture}}[>=stealth, scale=0.6, line width=1pt]
            \\draw[->] (-2, 0) -- ({T+2}, 0) node[below] {{$x$}};
            \\draw[->] (0, -2) -- (0, {a+2}) node[left] {{$y$}};
            \\node at (0,0) [below left] {{$O$}};
            \\clip (-2,-2) rectangle ({T+2},{a+2});
            \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle ({T+2},{a+2});
            \\fill[white] (0,0) -- (0,{a}) -- ({x0},{y0}) -- ({T},0) -- cycle;
            \\draw[black] (-2,0) -- ({T+2},0);
            \\draw[black] (0,-2) -- (0,{a+2});
            \\draw[black, smooth, domain=-2:{T+2}] plot(\\x, {{(({y0}-{a})/{x0})*\\x+{a}}});
            \\draw[black, smooth, domain=-2:{T+2}] plot(\\x, {{-\\x+{T}}});
            \\coordinate (A) at (0,{a});
            \\coordinate (B) at ({x0},{y0});
            \\coordinate (C) at ({T},0);
            \\fill (0,0) circle (0.5pt);
            \\fill (A) circle (0.5pt) node[above right] {{$A$}};
            \\fill (B) circle (0.5pt) node[above right] {{$B$}};
            \\fill (C) circle (0.5pt) node[above right] {{$C$}};
            \\draw[dashed, thin] ({x0},0) node[below] {{${x0}$}} -- (B) -- (0,{y0}) node[left] {{${y0}$}};
            \\node[left] at (0,{a}) {{${a}$}};
            \\node[below] at ({T},0) {{${T}$}};
            \\end{{tikzpicture}}
            \\end{{center}}'''
            loigiai =('Gọi $x,y$ lần lượt là số $ha$ trồng %s và trồng %s.\\\\\n'
                    'Có $0\\le x \\le %s; 0\\le y\\le %s; x+y\\le %s; %sx+%sy \\le %s \\Rightarrow %sx+%sy \\le %s$.\\\\\n'
                    'Số tiền thu được là $T(x;y)=%sx+%sy$.\\\\\n'
                    'Khi đó ta có hệ hệ bất phương trình $\\heva{& x+y\\le%s\\\\& %sx+%sy\\le%s\\\\& 0\\le x\\le %s\\\\& 0\\le y\\le %s}$.\\\\\n'
                    'Vẽ các đường thẳng:\\\\\n'
                    '$d_1:x+y=%s;\\\\\n' 
                    'd_2:%sx+%sy=%s;\\\\\n' 
                    '0\\le x\\le %s;\\\\\n' 
                    '0\\le y\\le %s$ trên cùng một hệ trục tọa độ $(Oxy)$.\\\\\n'
                    '\\begin{center} \n'
                    '%s' #Hìnhve
                    '\\end{center} \n'
                    'Miền nghiệm của hệ là miền tứ giác $OABC$ với tọa độ các đỉnh $O(0;0);A(0;%s);B(%s;%s);C(%s;0)$ (hình vẽ).\\\\\n' 
                    'Ta thấy $T(x;y)$ đạt giá trị lớn tại một trong các đỉnh của tứ giác $OABC$.\\\\\n'
                    'Ta có: \\\\\n'
                    '$F(0;0) = (%s)0+(%s)0= %s$.\\\\\n'
                    '$F(0;%s) = (%s)0+(%s)%s = %s$ triệu.\\\\\n'
                    '$F(%s;%s) = (%s)%s+(%s)%s= %s$ triệu.\\\\\n'
                    '$F(%s;0) = (%s)%s+(%s)0= %s$ triệu.\\\\\n'
                    'Vậy số tiền có thể thu được lớn nhất là $%s$ triệu đồng.'
                    %(str(t1),str(t2),
                        latex(T),latex(T),latex(T),latex(A1*10),latex(B1*10),latex(C1*10),latex(A1),latex(B1),latex(C1),
                        latex(c),latex(d),
                        latex(T),latex(A1),latex(B1),latex(C1),latex(T),latex(T),
                        latex(T),
                        latex(A1),latex(B1),latex(C1),
                        latex(T),
                        latex(T),
                        str(hinhve),
                        latex(a),latex(x0),latex(y0),latex(T),
                        latex(c),latex(d),latex(gt0),
                        latex(a),latex(c),latex(d),latex(a),latex(gta),
                        latex(x0),latex(y0),latex(c),latex(x0),latex(d),latex(y0),latex(gtb),
                        latex(T),latex(c),latex(T),latex(d),latex(gtc),
                        latex(ln)))
                #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(ln))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex} \n \\end{minipage} \n\n').replace('\\frac','\\dfrac'). replace('1x','x').replace('-1x','-x'). replace('1y','y'). replace('.0',''). replace('+-','-')
            return content

