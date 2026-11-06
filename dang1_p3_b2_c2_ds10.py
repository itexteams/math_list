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


def bt_dang1_p3_b2_c2_ds10(self):
            # Khai báo biến
            x0 = randint(1,7) # b là số bất kỳ từ 1 đến 30
            y0 = randint(1,7) # b là số bất kỳ từ 1 đến 30
            a = randint(8,10) # b là số bất kỳ từ 1 đến 30
            b= randint(8,10)# b là số bất kỳ từ 1 đến 30
            c = randint(2,9) # b là số bất kỳ từ 1 đến 30
            d = randint(2,9)# b là số bất kỳ từ 1 đến 30


            while ((y0*b)/(b-x0))<=a:
                x0 = randint(1,7) # b là số bất kỳ từ 1 đến 30
                y0 = randint(1,7) # b là số bất kỳ từ 1 đến 30
                a = randint(8,10) # b là số bất kỳ từ 1 đến 30
                b= randint(8,10)# b là số bất kỳ từ 1 đến 30
            A1=a-y0
            B1=x0
            C1=x0*a
            A2=y0
            B2=b-x0
            C2=y0*b
            T = x0+y0

            gt0=0
            gta=c*0+d*100*a
            gtb=c*100*x0+d*100*y0
            gtc=c*100*b
            list2=[gt0,gta,gtb,gtc]
            ln=max(list2)
            nn=min(list2)
            list4=[200,-200]
            rd4 = random.choice(list4)
            lista=['Đạo','Nam','Bình','Sơn','Tài','Tiến','Cường','Lâm','Trọng']
            listb=['Chiến','Dũng','Hưng','Quang','Lập','Phi','Hòa','Hải','Chung']
            t1=random.choice(lista)
            t2=random.choice(listb)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một xưởng cơ khí có hai công nhân là %s và %s. Xưởng sản xuất loại sản phẩm $I$ và $II$. 
                            Mỗi sản phẩm $I$ bán lãi $%s$ nghìn đồng, mỗi sản phẩm $II$ bán lãi $%s$ nghìn đồng.
                            Để sản xuất được một sản phẩm $I$ thì %s phải làm việc trong $%s$ giờ, %s phải làm việc trong $%s$ giờ. 
                            Để sản xuất được một sản phẩm $II$ thì %s phải làm việc trong $%s$ giờ, %s phải làm việc trong $%s$ giờ. 
                            Một người không thể làm được đồng thời hai sản phẩm.
                            Biết rằng trong một tuần %s không thể làm việc quá $%s$ giờ và %s không thể làm việc quá $%s$ giờ. 
                            Số tiền lãi lớn nhất (đơn vị: Triệu đồng) có thể đạt được trong một tuần của xưởng là bao nhiêu? (kết quả làm tròn đến hàng phần chục). \n'''
                            %(str(t1),str(t2),latex(c*100),latex(d*100),
                            str(t1),latex(A1),str(t2),latex(A2),
                            str(t1),latex(B1),str(t2),latex(B2),
                            str(t1),latex(C1),str(t2),latex(C2),))

                # Nội dung lời giải
            hinhve = f'''\\begin{{center}}
            \\begin{{tikzpicture}}[>=stealth, scale=0.6, line width=1pt]
            \\draw[->] (-2, 0) -- ({b+2}, 0) node[below] {{$x$}};
            \\draw[->] (0, -2) -- (0, {a+2}) node[left] {{$y$}};
            \\node at (0,0) [below left] {{$O$}};
            \\clip (-2,-2) rectangle ({b+2},{a+2});
            \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle ({b+2},{a+2});
            \\fill[white] (0,0) -- (0,{a}) -- ({x0},{y0}) -- ({b},0) -- cycle;
            \\draw[black] (-2,0) -- ({b+2},0);
            \\draw[black] (0,-2) -- (0,{a+2});
            \\draw[black, smooth, domain=-2:{b+2}] plot(\\x, {{(({y0}-{a})/{x0})*\\x+{a}}});
            \\draw[black, smooth, domain=-2:{b+2}] plot(\\x, {{({y0}/({x0}-{b}))*\\x+({y0}*{b})/({b}-{x0})}});
            \\coordinate (A) at (0,{a});
            \\coordinate (B) at ({x0},{y0});
            \\coordinate (C) at ({b},0);
            \\fill (0,0) circle (0.5pt);
            \\fill (A) circle (0.5pt) node[above right] {{$A$}};
            \\fill (B) circle (0.5pt) node[above right] {{$B$}};
            \\fill (C) circle (0.5pt) node[above right] {{$C$}};
            \\draw[dashed, thin] ({x0},0) node[below] {{${x0}$}} -- (B) -- (0,{y0}) node[left] {{${y0}$}};
            \\node[left] at (0,{a}) {{${a}$}};
            \\node[below] at ({b},0) {{${b}$}};
            \\end{{tikzpicture}}
            \\end{{center}}'''
            loigiai =('Gọi $x,y$ lần lượt là số sản phẩm loại $I$ và loại $II$ được sản xuất ra. Điều kiện $x,y$ nguyên dương.\\\\\n'
                        'Khi đó $x,y$ thỏa mãn hệ bất phương trình $\\heva{& %sx+%sy\\le%s\\\\& %sx+%sy\\le%s\\\\& x>0\\\\& y>0}$.\\\\\n'
                        'Vẽ các đường thẳng:\\\\\n'
                        '$d_1:%sx+%sy=%s;\\\\\n' 
                        'd_2:%sx+%sy=%s;\\\\\n' 
                        'x=0;\\\\\n' 
                        'y=0$ trên cùng một hệ trục tọa độ $(Oxy)$.\\\\\n'
                        '\\begin{center} \n'
                        '%s' #Hìnhve
                        '\\end{center} \n'
                        'Miền nghiệm của hệ là miền tứ giác $OABC$ với tọa độ các đỉnh $O(0;0);A(0;%s);B(%s;%s);C(%s;0)$ (hình vẽ).\\\\\n' 
                        'Tiền lãi của xưởng là $F(x;y)=%sx+%sy$ ngàn đồng. Ta thấy $F(x;y)$ đạt giá trị lớn tại một trong các đỉnh của tứ giác $OABC$.\\\\\n'
                        'Ta có: \\\\\n'
                        '$F(0;0) = (%s)0+(%s)0= %s$.\\\\\n'
                        '$F(0;%s) = (%s)0+(%s)%s = %s$ triệu.\\\\\n'
                        '$F(%s;%s) = (%s)%s+(%s)%s= %s$ triệu.\\\\\n'
                        '$F(%s;0) = (%s)%s+(%s)0= %s$ triệu.\\\\\n'
                        'Vậy tiền lãi lớn nhất của xưởng có thể đạt được trong một tuần là $%s$ triệu đồng.'
                        %(latex(A1),latex(B1),latex(C1),latex(A2),latex(B2),latex(C2),
                            latex(A1),latex(B1),latex(C1),latex(A2),latex(B2),latex(C2),
                            str(hinhve),
                            latex(a),latex(x0),latex(y0),latex(b),
                            latex(c*100),latex(d*100),
                            latex(c*100),latex(d*100),latex(gt0/1000),
                            latex(a),latex(c*100),latex(d*100),latex(a),latex(gta/1000),
                            latex(x0),latex(y0),latex(c*100),latex(x0),latex(d*100),latex(y0),latex(gtb/1000),
                            latex(b),latex(c*100),latex(b),latex(d*100),latex(gtc/1000),latex(ln/1000)))
                #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(ln/1000))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac'). replace('1x','x').replace('-1x','-x'). replace('1y','y'). replace('.0',''). replace('+-','-')
            return content

