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


def bt_dang13_p1_b2_c2_ds10(self):
            #Khai báo biến
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
            list3=['dang3']
            rd = random.choice(list3)
            rd4 = random.choice(list4)
            lista=['Đạo','Nam','Bình','Sơn','Tài','Tiến','Cường','Lâm','Trọng']
            listb=['Chiến','Dũng','Hưng','Quang','Lập','Phi','Hòa','Hải','Chung']
            t1=random.choice(lista)
            t2=random.choice(listb)
            #Nội ung câu hỏi
            if rd=='dang3':
                noidungcauhoi = ('''Một xưởng cơ khí có hai công nhân là %s và %s. Xưởng sản xuất loại sản phẩm $I$ và $II$. 
                                Mỗi sản phẩm $I$ bán lãi $%s$ nghìn đồng, mỗi sản phẩm $II$ bán lãi $%s$ nghìn đồng.
                                Để sản xuất được một sản phẩm $I$ thì %s phải làm việc trong $%s$ giờ, %s phải làm việc trong $%s$ giờ. 
                                Để sản xuất được một sản phẩm $II$ thì %s phải làm việc trong $%s$ giờ, %s phải làm việc trong $%s$ giờ. 
                                Một người không thể làm được đồng thời hai sản phẩm.
                                Biết rằng trong một tuần %s không thể làm việc quá $%s$ giờ và %s không thể làm việc quá $%s$ giờ. 
                                Số tiền lãi lớn nhất có thể đạt được trong một tuần của xưởng là \n'''
                                %(str(t1),str(t2),latex(c*100),latex(d*100),
                                str(t1),latex(A1),str(t2),latex(A2),
                                str(t1),latex(B1),str(t2),latex(B2),
                                str(t1),latex(C1),str(t2),latex(C2),))
            # Các đáp án
                da_d = '\\True $%s$ triệu'%(latex(ln/1000))
                da_s1 = '$%s$ triệu'%(latex((ln+rd4)/1000))
                da_s2 = '$%s$ triệu'%(latex((ln-100)/1000))
                da_s3 = '$%s$ triệu'%(latex((ln+100)/1000))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                hinhve = ('\\begin{tikzpicture}[>=stealth, scale=0.8, line width=1pt]\n'
                          '\\draw[->] (-2, 0) -- (%s, 0) node[below] {$x$};\n'
                          '\\draw[->] (0, -2) -- (0, %s) node[left] {$y$};\n'
                          '\\node at (0,0) [below left] {$O$};\n'
                          '\\clip (-2,-2) rectangle (%s,%s);\n'
                          '\\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (%s,%s);\n'
                          '\\fill[white] (0,0) -- (0,%s) -- (%s,%s) -- (%s,0) -- cycle;\n' 
                          '\\draw[black] (-2,0) -- (%s,0);\n'
                          '\\draw[black] (0,-2) -- (0,%s);\n'
                          '\\draw[black, smooth, domain=-2:%s] plot(\\x, {%s*\\x+%s});\n' 
                          '\\draw[black, smooth, domain=-2:%s] plot(\\x, {%s*\\x+%s});\n' 
                          '\\coordinate (A) at (0,%s);\n'
                          '\\coordinate (B) at (%s,%s);\n'
                          '\\coordinate (C) at (%s,0);\n'
                          '\\fill (A) circle (0.5pt) node[left] {$A$};\n'
                          '\\fill (B) circle (0.5pt) node[above right] {$B$};\n'
                          '\\fill (C) circle (0.5pt) node[below] {$C$};\n'
                          '\\end{tikzpicture}\\\\'
                          %(latex(b+2), latex(a+2), 
                            latex(b+2), latex(a+2), 
                            latex(b+2), latex(a+2), 
                            latex(a), latex(x0), latex(y0), latex(b), 
                            latex(b+2), latex(a+2), 
                            latex(b+2), latex((y0-a)/x0), latex(a), 
                            latex(b+2), latex(y0/(x0-b)), latex((y0*b)/(b-x0)), 
                            latex(a), 
                            latex(x0), latex(y0), 
                            latex(b) 
                          ))
                loigiai =('Gọi $x,y$ lần lượt là số sản phẩm loại $I$ và loại $II$ được sản xuất ra. Điều kiện $x,y$ nguyên dương.\\\\\n'
                        'Khi đó $x,y$ thỏa mãn hệ bất phương trình $\\heva{& %sx+%sy\\le%s\\\\& %sx+%sy\\le%s\\\\& x>0\\\\& y>0}$.\\\\\n'
                        'Vẽ các đường thẳng:\\\\\n'
                        '$d_1:%sx+%sy=%s;\\\\\n' 
                        'd_2:%sx+%sy=%s;\\\\\n' 
                        'd_3:x=0;\\\\\n' 
                        'd_4:y=0$ trên cùng một hệ trục tọa độ $(Oxy)$.'
                        '\\begin{center}'
                        '%s' #Hìnhve
                        '\\end{center}'
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
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
            '\\begin{ex}\n' 
            + str(noidungcauhoi)+
            '\\choice \n'
            '{'+str(list_1[1])+'}\n'
            '{'+str(list_1[2])+'}\n'
            '{'+str(list_1[3])+'}\n'
            '{'+str(list_1[0])+'}\n'
            '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac'). replace('1x','x').replace('-1x','-x'). replace('1y','y'). replace('.0',''). replace('+-','-')
            return content

