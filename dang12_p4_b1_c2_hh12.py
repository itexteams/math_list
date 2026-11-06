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


def bt_dang12_p4_b1_c2_hh12(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a=randint(2,12)
                b=randint(2,12)
                h=randint(2,12)
                u=lcm(lcm(a,b),h)
                a1=nsimplify(u/a)
                b1=nsimplify(u/b)
                c1=nsimplify(u/h)
                d1=-u
                pt=a1*x+b1*y+c1*z+d1
                tu=abs(a1*0+b1*0+c1*0+d1)
                mau=sqrt(a1**2+b1**2+c1**2)
                kq=nsimplify(tu/mau)





                # Nội dung câu hỏi
                noidungcauhoi =  ('\\immini{'
                                    'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật với $AB=%sa,AD=%sa,SA=%sa$ và $SA\\perp (ABCD)$. Bằng cách thiết lập hệ trục tọa độ $Oxyz$ như hình vẽ. Tính khoảng cách từ điểm $A$ đến mặt phẳng $(SBD)$.'
                                '}{'
                        '\\scalebox{0.6}{ '          
                '\\begin{tikzpicture}[scale=0.9,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                '\\clip(-6.5,-2.46) rectangle (4.16,5.58);\n'
                '\\draw[dashed]  (-3,1)-- (-5,-1);\n'
                '\\draw (-5,-1)-- (0,-1);\n'
                '\\draw (0,-1)-- (2,1);\n'
                '\\draw[dashed] (2,1)-- (-3,1);\n'
                '\\draw[dashed] (-3,4)-- (-3,1);\n'
                '\\draw (-3,4)-- (0,-1);\n'
                '\\draw  (-3,4)-- (2,1);\n'
                '\\draw (-3,4)-- (-5,-1);\n'
                '\\draw (-3,4.2) node[left] {$S$};\n'
                '\\draw (-2.8,0.8) node[below] {$A$};\n'
                '\\draw (-6,-1.7) node[above] {$x$};\n'
                '\\draw (2.1,0.8) node[below] {$D$};\n'
                '\\draw (0,-1.2) node[below] {$C$};\n'
                '\\draw [->] (2,1) -- (4,1);\n'
                '\\draw [->] (-5,-1) -- (-6,-2);\n'
                '\\draw (-4.8,-1.2) node[below] {$B$};\n'
                '\\draw (3.2,1) node[above] {$y$};\n'
                '\\draw [->] (-3,4) -- (-3,5.52);\n'
                '\\draw (-2.9,5) node[right] {$z$};\n'
                '\\end{tikzpicture}}}\n'

                    %(latex(a),latex(b),latex(h)))

                # Nội dung lời giải
                loigiai = ('Chọn gốc tọa độ $O(0;0;0)$ trùng với điểm $A$ ta có\\\\ \n'
                        '$A(0;0;0),B(%sa;0;0),C(%sa;%sa;0),D(0;%sa;0),S(0;0;%sa)$.\\\\ \n'
                        'Vì mặt phẳng $(SBD)$ đi qua các điểm $S(0;0;%sa),B(0;%sa;0),D(0;%sa;0)$ nên có phương trình là\\\\ \n'
                        '$$\\dfrac{x}{%sa}+\\dfrac{y}{%sa}+\\dfrac{z}{%sa}=1\\Leftrightarrow %s+%sa=0.$$\\\\ \n'
                        'Khoảng cách từ điểm $A$ đến mặt phẳng $(SBD)$ là\\\\ \n'
                        '$$d(A,(SBD))=\\dfrac{\\abs{%s\\cdot 0+%s\\cdot 0+%s\\cdot 0+%sa}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%sa.$$'

                        %(latex(a),latex(a),latex(b),latex(b),latex(h),
                            latex(h),latex(a),latex(b),
                            latex(a),latex(b),latex(h),latex(pt-d1),latex(d1),
                            latex(a1),latex(b1),latex(c1),latex(d1),latex(a1),latex(b1),latex(c1),
                            latex(kq),

                            )
                        )
            if dang=='2':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a=randint(2,12)
                b=randint(2,12)
                h=randint(2,12)
                u=lcm(lcm(a,b),h)
                a1=nsimplify(u/a)
                b1=nsimplify(u/b)
                c1=nsimplify(u/h)
                d1=-u
                pt=a1*x+b1*y+c1*z+d1
                tu=abs(a1*a+b1*b+c1*0+d1)
                mau=sqrt(a1**2+b1**2+c1**2)
                kq=nsimplify(tu/mau)





                # Nội dung câu hỏi
                noidungcauhoi =  ('\\immini{'
                                    'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật với $AB=%sa,AD=%sa,SA=%sa$ và $SA\\perp (ABCD)$. Bằng cách thiết lập hệ trục tọa độ $Oxyz$ như hình vẽ. Tính khoảng cách từ điểm $C$ đến mặt phẳng $(SBD)$.'
                                '}{'
                        '\\scalebox{0.6}{ '          
                '\\begin{tikzpicture}[scale=0.9,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                '\\clip(-6.5,-2.46) rectangle (4.16,5.58);\n'
                '\\draw[dashed]  (-3,1)-- (-5,-1);\n'
                '\\draw (-5,-1)-- (0,-1);\n'
                '\\draw (0,-1)-- (2,1);\n'
                '\\draw[dashed] (2,1)-- (-3,1);\n'
                '\\draw[dashed] (-3,4)-- (-3,1);\n'
                '\\draw (-3,4)-- (0,-1);\n'
                '\\draw  (-3,4)-- (2,1);\n'
                '\\draw (-3,4)-- (-5,-1);\n'
                '\\draw (-3,4.2) node[left] {$S$};\n'
                '\\draw (-2.8,0.8) node[below] {$A$};\n'
                '\\draw (-6,-1.7) node[above] {$x$};\n'
                '\\draw (2.1,0.8) node[below] {$D$};\n'
                '\\draw (0,-1.2) node[below] {$C$};\n'
                '\\draw [->] (2,1) -- (4,1);\n'
                '\\draw [->] (-5,-1) -- (-6,-2);\n'
                '\\draw (-4.8,-1.2) node[below] {$B$};\n'
                '\\draw (3.2,1) node[above] {$y$};\n'
                '\\draw [->] (-3,4) -- (-3,5.52);\n'
                '\\draw (-2.9,5) node[right] {$z$};\n'
                '\\end{tikzpicture}}}\n'

                    %(latex(a),latex(b),latex(h)))

                # Nội dung lời giải
                loigiai = ('Chọn gốc tọa độ $O(0;0;0)$ trùng với điểm $A$ ta có\\\\ \n'
                        '$A(0;0;0),B(%sa;0;0),C(%sa;%sa;0),D(0;%sa;0),S(0;0;%sa)$.\\\\ \n'
                        'Vì mặt phẳng $(SBD)$ đi qua các điểm $S(0;0;%sa),B(0;%sa;0),D(0;%sa;0)$ nên có phương trình là\\\\ \n'
                        '$$\\dfrac{x}{%sa}+\\dfrac{y}{%sa}+\\dfrac{z}{%sa}=1\\Leftrightarrow %s+%sa=0.$$\\\\ \n'
                        'Khoảng cách từ điểm $C$ đến mặt phẳng $(SBD)$ là\\\\ \n'
                        '$$d(C,(SBD))=\\dfrac{\\abs{%s\\cdot %sa+%s\\cdot %sa+%s\\cdot 0+%sa}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%sa.$$'

                        %(latex(a),latex(a),latex(b),latex(b),latex(h),
                            latex(h),latex(a),latex(b),
                            latex(a),latex(b),latex(h),latex(pt-d1),latex(d1),
                            latex(a1),latex(a),latex(b1),latex(b),latex(c1),latex(d1),latex(a1),latex(b1),latex(c1),
                            latex(kq),

                            )
                        )
            if dang=='3':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a=randint(2,12)
                b=randint(2,12)
                h=randint(2,12)
                xg=nsimplify(a/3)
                yg=nsimplify(b/3)
                zg=nsimplify(h/3)
                u=gcd(b*h,a*b)
                x1=b*h
                y1=0
                z1=a*b
                a1=nsimplify(x1/u)
                b1=nsimplify(y1/u)
                c1=nsimplify(z1/u)
                d1=nsimplify((-b*h*a)/u)
                pt=a1*x+b1*y+c1*z+d1
                tu=abs(a1*xg+b1*yg+c1*zg+d1)
                mau=sqrt(a1**2+b1**2+c1**2)
                kq=nsimplify(tu/mau)





                # Nội dung câu hỏi
                noidungcauhoi =  ('\\immini{'
                                    'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật với $AB=%sa,AD=%sa,SA=%sa$ và $SA\\perp (ABCD)$. Bằng cách thiết lập hệ trục tọa độ $Oxyz$ như hình vẽ. Tính khoảng cách từ trọng tâm $G$ của tam giác $SBD$ đến mặt phẳng $(SBC)$.'
                                '}{'
                        '\\scalebox{0.6}{ '          
                '\\begin{tikzpicture}[scale=0.9,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                '\\clip(-6.5,-2.46) rectangle (4.16,5.58);\n'
                '\\draw[dashed]  (-3,1)-- (-5,-1);\n'
                '\\draw (-5,-1)-- (0,-1);\n'
                '\\draw (0,-1)-- (2,1);\n'
                '\\draw[dashed] (2,1)-- (-3,1);\n'
                '\\draw[dashed] (-3,4)-- (-3,1);\n'
                '\\draw (-3,4)-- (0,-1);\n'
                '\\draw  (-3,4)-- (2,1);\n'
                '\\draw (-3,4)-- (-5,-1);\n'
                '\\draw (-3,4.2) node[left] {$S$};\n'
                '\\draw (-2.8,0.8) node[below] {$A$};\n'
                '\\draw (-6,-1.7) node[above] {$x$};\n'
                '\\draw (2.1,0.8) node[below] {$D$};\n'
                '\\draw (0,-1.2) node[below] {$C$};\n'
                '\\draw [->] (2,1) -- (4,1);\n'
                '\\draw [->] (-5,-1) -- (-6,-2);\n'
                '\\draw (-4.8,-1.2) node[below] {$B$};\n'
                '\\draw (3.2,1) node[above] {$y$};\n'
                '\\draw [->] (-3,4) -- (-3,5.52);\n'
                '\\draw (-2.9,5) node[right] {$z$};\n'
                '\\end{tikzpicture}}}\n'

                    %(latex(a),latex(b),latex(h)))

                # Nội dung lời giải
                loigiai = ('Chọn gốc tọa độ $O(0;0;0)$ trùng với điểm $A$ ta có\\\\ \n'
                        '$A(0;0;0),B(%sa;0;0),C(%sa;%sa;0),D(0;%sa;0),S(0;0;%sa)$.\\\\ \n'
                        'Trọng tâm $G$ của tam giác $SBD$ có tọa độ là $G\\left(%sa;%sa;%sa\\right)$.\\\\ \n'
                        'Mặt phẳng $(SBC)$ nhận $\\vec{SB}=(%sa;0;-%sa),\\vec{SC}=(%sa;%sa;-%sa)$ làm cặp vectơ chỉ phương nên có vectơ pháp tuyến là\\\\ \n' 
                        '$$\\vec{n}=\\left[\\vec{SB},\\vec{SC}\\right]=(%sa^2;%s;%sa^2)$$'
                        'Mặt phẳng (SBC) đi qua điểm $B(%sa;0;0)$ và nhận $\\vec{n}=(%sa^2;%s;%sa^2)$ làm một vectơ pháp tuyến nên có phương trình là\\\\ \n'
                        '\\hspace*{1cm}$%sa^2(x-%sa)+%s(y-0)+%sa^2(z-0)=0 \\Leftrightarrow %s+%sa=0$.\\\\ \n'
                        'Khoảng cách từ điểm $G$ đến mặt phẳng $(SBC)$ là\\\\ \n'
                        '$$d(G,(SBC))=\\dfrac{\\abs{%s\\cdot \\left(%sa\\right)+%s\\cdot \\left(%sa\\right)+%s\\cdot\\left(%sa\\right)+%sa}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%sa.$$'
                        %(latex(a),latex(a),latex(b),latex(b),latex(h),
                            latex(xg),latex(yg),latex(zg),
                            latex(a),latex(h),latex(a),latex(b),latex(h),
                            latex(x1),latex(y1),latex(z1),
                            latex(a),latex(x1),latex(y1),latex(z1),
                            latex(x1),latex(a),latex(0),latex(z1),latex(pt-d1),latex(d1),
                            latex(a1),latex(xg),latex(b1),latex(yg),latex(c1),latex(zg),latex(d1),latex(a1),latex(b1),latex(c1),
                            latex(kq),

                            )
                        )
            if dang=='4':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a=randint(2,12)
                b=randint(2,12)
                h=randint(2,12)
                xg=nsimplify(a/3)
                yg=nsimplify(b/3)
                zg=nsimplify(h/3)
                u=gcd(-a*h,-a*b)
                x1=0
                y1=-a*h
                z1=-a*b
                a1=nsimplify(x1/u)
                b1=nsimplify(y1/u)
                c1=nsimplify(z1/u)
                d1=nsimplify((b*h*a)/u)
                pt=a1*x+b1*y+c1*z+d1
                tu=abs(a1*xg+b1*yg+c1*zg+d1)
                mau=sqrt(a1**2+b1**2+c1**2)
                kq=nsimplify(tu/mau)





                # Nội dung câu hỏi
                noidungcauhoi =  ('\\immini{'
                                    'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật với $AB=%sa,AD=%sa,SA=%sa$ và $SA\\perp (ABCD)$. Bằng cách thiết lập hệ trục tọa độ $Oxyz$ như hình vẽ. Tính khoảng cách từ trọng tâm $G$ của tam giác $SBD$ đến mặt phẳng $(SCD)$.'
                                '}{'
                        '\\scalebox{0.6}{ '          
                '\\begin{tikzpicture}[scale=0.9,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                '\\clip(-6.5,-2.46) rectangle (4.16,5.58);\n'
                '\\draw[dashed]  (-3,1)-- (-5,-1);\n'
                '\\draw (-5,-1)-- (0,-1);\n'
                '\\draw (0,-1)-- (2,1);\n'
                '\\draw[dashed] (2,1)-- (-3,1);\n'
                '\\draw[dashed] (-3,4)-- (-3,1);\n'
                '\\draw (-3,4)-- (0,-1);\n'
                '\\draw  (-3,4)-- (2,1);\n'
                '\\draw (-3,4)-- (-5,-1);\n'
                '\\draw (-3,4.2) node[left] {$S$};\n'
                '\\draw (-2.8,0.8) node[below] {$A$};\n'
                '\\draw (-6,-1.7) node[above] {$x$};\n'
                '\\draw (2.1,0.8) node[below] {$D$};\n'
                '\\draw (0,-1.2) node[below] {$C$};\n'
                '\\draw [->] (2,1) -- (4,1);\n'
                '\\draw [->] (-5,-1) -- (-6,-2);\n'
                '\\draw (-4.8,-1.2) node[below] {$B$};\n'
                '\\draw (3.2,1) node[above] {$y$};\n'
                '\\draw [->] (-3,4) -- (-3,5.52);\n'
                '\\draw (-2.9,5) node[right] {$z$};\n'
                '\\end{tikzpicture}}}\n'

                    %(latex(a),latex(b),latex(h)))

                # Nội dung lời giải
                loigiai = ('Chọn gốc tọa độ $O(0;0;0)$ trùng với điểm $A$ ta có\\\\ \n'
                        '$A(0;0;0),B(%sa;0;0),C(%sa;%sa;0),D(0;%sa;0),S(0;0;%sa)$.\\\\ \n'
                        'Trọng tâm $G$ của tam giác $SBD$ có tọa độ là $G\\left(%sa;%sa;%sa\\right)$.\\\\ \n'
                        'Mặt phẳng $(SCD)$ nhận $\\vec{SD}=(0;%sa;-%sa),\\vec{SC}=(%sa;%sa;-%sa)$ làm cặp vectơ chỉ phương nên có vectơ pháp tuyến là\\\\ \n' 
                        '$$\\vec{n}=\\left[\\vec{SB},\\vec{SC}\\right]=(0;%sa^2;%sa^2)$$'
                        'Mặt phẳng (SCD) đi qua điểm $D(0;%sa;0)$ và nhận $\\vec{n}=(0;%sa^2;%sa^2)$ làm một vectơ pháp tuyến nên có phương trình là\\\\ \n'
                        '\\hspace*{1cm}$%sa^2(y-%sa)+%sa^2(z-0)=0 \\Leftrightarrow %s+%sa=0$.\\\\ \n'
                        'Khoảng cách từ điểm $G$ đến mặt phẳng $(SCD)$ là\\\\ \n'
                        '$$d(G,(SCD))=\\dfrac{\\abs{%s\\cdot \\left(%sa\\right)+%s\\cdot\\left(%sa\\right)+%sa}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%sa.$$'
                        %(latex(a),latex(a),latex(b),latex(b),latex(h),
                            latex(xg),latex(yg),latex(zg),

                            latex(b),latex(h),latex(a),latex(b),latex(h),

                            latex(y1),latex(z1),
                            latex(b),latex(y1),latex(z1),

                            latex(y1),latex(b),latex(z1),latex(pt-d1),latex(d1),
                            latex(b1),latex(yg),latex(c1),latex(zg),latex(d1),latex(a1),latex(b1),latex(c1),
                            latex(kq),

                            )
                        )
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-').replace('-1\\cdot','-').replace('+1\\cdot','+').replace('{1\\cdot','{').replace('\\left(1a','\\left(a').replace('1a\\right)','a\\right)').replace(';1a;',';a;')
            return content 

