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


def bt_dang2_p2_b4_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                e=randint(-20,20)
                f1=randint(1,9)
                f=f1**2
                g=randint(-6,6)
                a=1
                b=e+g
                c=e*g+f
                d=1
                e=g
                x=symbols('x')
                y=(a*x**2+b*x+c)/(d*x+e)
                x1=-f1-g
                x2=f1-g
                y1=y.subs(x,x1)
                y2=y.subs(x,x2)
                tcd=-g
                while y2>=6 or y2<=-6 or y1>=6 or y1<=-6 or x2>=6 or x2<=-8 or x1>=8 or x1<=-8 or g==0 or x1==0 or x2==0 or y1==0 or y2==0:
                    e=randint(-20,20)
                    f1=randint(1,9)
                    f=f1**2
                    g=randint(-6,6)
                    a=1
                    b=e+g
                    c=e*g+f
                    d=1
                    e=g
                    x=symbols('x')
                    y=(a*x**2+b*x+c)/(d*x+e)
                    x1=-f1-g
                    x2=f1-g
                    y1=y.subs(x,x1)
                    y2=y.subs(x,x2)
                    tcd=-g
                if x1>0 and x2>0:
                    o1='below left'
                    t1='below left'
                    c1='left'
                    c2='below left'
                    c3='below right'
                    c4='left'
                    x_m=-5
                    x_M=x2+5
                if x1<0 and x2<0:
                    o1='below right'
                    t1='below left'
                    c1='right'
                    c2='below left'
                    c3='below'
                    c4='right'
                    x_m=x1-5
                    x_M=5
                if x1<0 and x2>0:
                    o1='below right'
                    t1='above left'
                    c1='right'
                    c2='below left'
                    c3='below right'
                    c4='left'
                    x_m=x1-5
                    x_M=x2+5

                # Nội dung câu hỏi
                noidungcauhoi=('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ.' )
                hinhve=(   '\\scalebox{0.6}{ \\\\'
                            '\\begin{tikzpicture}[scale=0.6,>=stealth, font=\\footnotesize, line join=round, line cap=round] \\\\'
                            '\\def\\a{%s} \\def\\b{%s} \\def\\c{%s} \\def\\d{%s} \\def\\e{%s} \\\\'
                            '\\def\\xmin{%s} \\def\\xmax{%s} \\\\'
                            '\\def\\ymin{%s} \\def\\ymax{%s} \\\\'
                            '\\draw[->] (\\xmin,0)--(\\xmax,0) node [below]{$x$}; \\\\'
                            '\\draw[->] (0,\\ymin)--(0,\\ymax) node [left]{$y$}; \\\\'
                            '\\node at (0,0) [%s]{$O$}; \\\\'
                            '\\clip (\\xmin+0.1,\\ymin+0.1) rectangle (\\xmax-0.1,\\ymax-0.1); \\\\'
                            '\\draw[smooth,samples=300,domain=\\xmin:(-\\e/\\d-0.1)] plot(\\x,{(\\a*(\\x)^2+\\b*(\\x)+\\c)/(\\d*(\\x)+\\e)}); \\\\'
                            '\\draw[smooth,samples=300,domain=(-\\e/\\d+0.1):\\xmax]  plot(\\x,{(\\a*(\\x)^2+\\b*(\\x)+\\c)/(\\d*(\\x)+\\e)}); \\\\'
                            '\\draw[thin] (-\\e/\\d,\\ymin)--(-\\e/\\d,\\ymax); \\\\'
                            '\\draw[smooth,thin,samples=300,domain=\\xmin:\\xmax] plot(\\x,{(\\a*(\\x)/(\\d)+(\\d*\\b-\\e*\\a)/((\\d)^2)}); \\\\'	
                            '\\node at (-\\e/\\d,0) [%s]{$%s$}; \\\\'
                            '\\node at (0,%s) [%s]{$%s$}; \\\\'
                            '\\node at (%s,0) [%s]{$%s$}; \\\\'
                            '\\node at (%s,0) [%s]{$%s$}; \\\\'
                            '\\node at (0,%s) [%s]{$%s$}; \\\\'
                            '\\draw[dashed] (%s,0)--(%s,%s)--(0,%s); \\\\'
                            '\\draw[dashed] (%s,0)--(%s,%s)--(0,%s); \\\\'
                        '\\end{tikzpicture} } \\\\'
                    %(latex(a),latex(b),latex(c),latex(d),latex(e),x_m,x_M,y1-3,y2+3,o1,
                    t1,latex(tcd),y1,c1,latex(y1),latex(x1),c2,latex(x1),latex(x2),c3,latex(x2),y2,c4,latex(y2),
                    latex(x2),latex(x2),y2,y2,latex(x1),latex(x1),y1,y1) )


                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Hàm số $f(x)$ đồng biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2))
                nb_da_1_s = 'Hàm số $f(x)$ nghịch biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True  Hàm số $f(x)$ nghịch biến trên các khoảng $(%s;%s)$ và $(%s;%s)$'%(latex(x1),latex(tcd),latex(tcd),latex(x2))
                nb_da_2_s = 'Hàm số $f(x)$ đồng biến trên các khoảng $(%s;%s)$ và $(%s;%s)$'%(latex(x1),latex(tcd),latex(tcd),latex(x2))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]

                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = ('Hàm số $f(x)$ đồng biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$.'%(latex(x1),latex(x2))
                            )
                loigiai_nb_2 = ('Hàm số $f(x)$ nghịch biến trên các khoảng $(%s;%s)$ và $(%s;%s)$.'%(latex(x1),latex(tcd),latex(tcd),latex(x2))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Đồ thị hàm số $f(x)$ có hai đường tiệm cận'
                th_da_1_s = 'Đồ thị hàm số $f(x)$ có một đường tiệm cận'
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                th_da_2_d = '\\True $x=%s$ là tiệm cận đứng của đồ thị hàm số $f(x)$'%(latex(tcd))
                th_da_2_s = 'Đồ thị hàm số $f(x)$ có hai đường tiệm cận đứng'
                list_th_da_2=[th_da_2_d,th_da_2_s]

                th_da_2=random.choice(list_th_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1, th_da_2]

                # Nội dung lời giải
                loigiai_th_1 = ('Ta thấy đồ thị hàm số $f(x)$ có một đường tiệm cận đứng và một đường tiệm cận ngang. Suy ra đồ thị hàm số $f(x)$ có hai đường tiệm cận.'
                            )
                loigiai_th_2 = ('Từ đồ thị ta thấy $x=%s$ là tiệm cận đứng của đồ thị hàm số $f(x)$.'%(latex(tcd))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1, loigiai_th_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Hàm số $f(x)$ đạt cực đại tại điểm $x=%s$'%(latex(x1))
                vd_da_1_s = 'Hàm số $f(x)$ đạt cực tiểu tại điểm $x=%s$'%(latex(x1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True Hàm số $f(x)$ đạt cực tiểu tại điểm $x=%s$'%(latex(x2))
                vd_da_2_s = 'Hàm số $f(x)$ đạt cực đại tại điểm $x=%s$'%(latex(x2))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]
                vd_da_2=random.choice(list_vd_da_2)

                vd_da_3_d = '\\True Giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$'%(latex(y1))
                vd_da_3_s = 'Giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$'%(latex(y1))
                list_vd_da_3=[vd_da_3_d,vd_da_3_s]
                vd_da_3=random.choice(list_vd_da_3)

                vd_da_4_d = '\\True Giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$'%(latex(y2))
                vd_da_4_s = 'Giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$'%(latex(y2))
                list_vd_da_4=[vd_da_4_d,vd_da_4_s]
                vd_da_4=random.choice(list_vd_da_4)



                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2,vd_da_3,vd_da_4]

                # Nội dung lời giải
                loigiai_vd_1 = ('Hàm số $f(x)$ đạt cực đại tại điểm $x=%s$.'%(latex(x1))
                            )
                loigiai_vd_2 = ('Hàm số $f(x)$ đạt cực tiểu tại điểm $x=%s$.'%(latex(x2))
                            )
                loigiai_vd_3 = ('Giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$.'%(latex(y1))
                            )
                loigiai_vd_4 = ('Giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$.'%(latex(y2))
                            )


                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1, loigiai_vd_2,loigiai_vd_3,loigiai_vd_4]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Điểm cực đại của đồ thị hàm số $f(x)$ là $\\left(%s;%s\\right)$'%(latex(x1),latex(y1))
                vdc_da_1_s = 'Điểm cực đại của đồ thị hàm số $f(x)$ là $\\left(%s;%s\\right)$'%(latex(x2),latex(y2))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Điểm cực tiểu của đồ thị hàm số $f(x)$ là $\\left(%s;%s\\right)$'%(latex(x2),latex(y2))
                vdc_da_2_s = 'Điểm cực tiểu của đồ thị hàm số $f(x)$ là $\\left(%s;%s\\right)$'%(latex(x1),latex(y1))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Điểm cực đại của đồ thị hàm số $f(x)$ là $\\left(%s;%s\\right)$.'%(latex(x1),latex(y1))
                            )
                loigiai_vdc_2 = ('Điểm cực tiểu của đồ thị hàm số $f(x)$ là $\\left(%s;%s\\right)$.'%(latex(x2),latex(y2))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='2':
                # Khai báo biến
                e=randint(-20,20)
                f1=randint(1,9)
                f=-f1**2
                g=randint(-6,6)
                a=-1
                b=e+g
                c=e*g+f
                d=1
                e=g
                x=symbols('x')
                y=(a*x**2+b*x+c)/(d*x+e)
                x1=-f1-g
                x2=f1-g
                y1=y.subs(x,x1)
                y2=y.subs(x,x2)
                tcd=-g
                while x1==0 or x2==0 or x1<=-6 or x2>=6 or y1>=8 or g==0 or y2<=-8:
                    e=randint(-20,20)
                    f1=randint(1,9)
                    f=-f1**2
                    g=randint(-6,6)
                    a=-1
                    b=e+g
                    c=e*g+f
                    d=1
                    e=g
                    x=symbols('x')
                    y=(a*x**2+b*x+c)/(d*x+e)
                    x1=-f1-g
                    x2=f1-g
                    y1=y.subs(x,x1)
                    y2=y.subs(x,x2)
                    tcd=-g
                if x1>0 and x2>0:
                    o1='below left'
                    t1='below left'
                    c1='left'
                    c2='below left'
                    c3='below right'
                    c4='left'
                    x_m=-5
                    x_M=x2+5
                if x1<0 and x2<0:
                    o1='below right'
                    t1='below left'
                    c1='right'
                    c2='below left'
                    c3='below'
                    c4='right'
                    x_m=x1-5
                    x_M=5
                if x1<0 and x2>0:
                    o1='below right'
                    t1='below right'
                    c1='right'
                    c2='below left'
                    c3='below right'
                    c4='left'
                    x_m=x1-5
                    x_M=x2+5

                # Nội dung câu hỏi
                noidungcauhoi=('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ.' )
                hinhve=(  '\\scalebox{0.6}{ \\\\'
                        '\\begin{tikzpicture}[scale=0.6,>=stealth, font=\\footnotesize, line join=round, line cap=round] \\\\'
                            '\\def\\a{%s} \\def\\b{%s} \\def\\c{%s} \\def\\d{%s} \\def\\e{%s} \\\\'
                            '\\def\\xmin{%s} \\def\\xmax{%s} \\\\'
                            '\\def\\ymin{%s} \\def\\ymax{%s} \\\\'
                            '\\draw[->] (\\xmin,0)--(\\xmax,0) node [below]{$x$}; \\\\'
                            '\\draw[->] (0,\\ymax)--(0,\\ymin) node [left]{$y$}; \\\\'
                            '\\node at (0,0) [%s]{$O$}; \\\\'
                            '\\clip (\\xmin+0.1,\\ymin+0.1) rectangle (\\xmax-0.1,\\ymax-0.1); \\\\'
                            '\\draw[smooth,samples=300,domain=\\xmin:(-\\e/\\d-0.1)] plot(\\x,{(\\a*(\\x)^2+\\b*(\\x)+\\c)/(\\d*(\\x)+\\e)}); \\\\'
                            '\\draw[smooth,samples=300,domain=(-\\e/\\d+0.1):\\xmax]  plot(\\x,{(\\a*(\\x)^2+\\b*(\\x)+\\c)/(\\d*(\\x)+\\e)}); \\\\'
                            '\\draw[thin] (-\\e/\\d,\\ymin)--(-\\e/\\d,\\ymax); \\\\'
                            '\\draw[smooth,thin,samples=300,domain=\\xmin:\\xmax] plot(\\x,{(\\a*(\\x)/(\\d)+(\\d*\\b-\\e*\\a)/((\\d)^2)}); \\\\'	
                            '\\node at (-\\e/\\d,0) [%s]{$%s$}; \\\\'
                            '\\node at (0,%s) [%s]{$%s$}; \\\\'
                            '\\node at (%s,0) [%s]{$%s$}; \\\\'
                            '\\node at (%s,0) [%s]{$%s$}; \\\\'
                            '\\node at (0,%s) [%s]{$%s$}; \\\\'
                            '\\draw[dashed] (%s,0)--(%s,%s)--(0,%s); \\\\'
                            '\\draw[dashed] (%s,0)--(%s,%s)--(0,%s); \\\\'
                        '\\end{tikzpicture} } \\\\'
                    %(latex(a),latex(b),latex(c),latex(d),latex(e),x_m,x_M,y1+3,y2-3,o1,
                    t1,latex(tcd),y1,c1,latex(y1),latex(x1),c2,latex(x1),latex(x2),c3,latex(x2),y2,c4,latex(y2),
                    latex(x2),latex(x2),y2,y2,latex(x1),latex(x1),y1,y1))


                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Hàm số $f(x)$ nghịch biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2))
                nb_da_1_s = 'Hàm số $f(x)$ đồng biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Hàm số $f(x)$ đồng biến trên các khoảng $(%s;%s)$ và $(%s;%s)$'%(latex(x1),latex(tcd),latex(tcd),latex(x2))
                nb_da_2_s = 'Hàm số $f(x)$ nghịch biến trên các khoảng $(%s;%s)$ và $(%s;%s)$'%(latex(x1),latex(tcd),latex(tcd),latex(x2))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]

                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = (' Hàm số $f(x)$ nghịch biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$.'%(latex(x1),latex(x2))
                            )
                loigiai_nb_2 = ('Hàm số $f(x)$ đồng biến trên các khoảng $(%s;%s)$ và $(%s;%s)$.'%(latex(x1),latex(tcd),latex(tcd),latex(x2))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Đồ thị hàm số $f(x)$ có hai đường tiệm cận'
                th_da_1_s = 'Đồ thị hàm số $f(x)$ có một đường tiệm cận'
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                th_da_2_d = '\\True $x=%s$ là tiệm cận đứng của đồ thị hàm số $f(x)$'%(latex(tcd))
                th_da_2_s = 'Đồ thị hàm số $f(x)$ có hai đường tiệm cận đứng'
                list_th_da_2=[th_da_2_d,th_da_2_s]

                th_da_2=random.choice(list_th_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1, th_da_2]

                # Nội dung lời giải
                loigiai_th_1 = ('Ta thấy đồ thị hàm số $f(x)$ có một đường tiệm cận đứng và một đường tiệm cận ngang. Suy ra đồ thị hàm số $f(x)$ có hai đường tiệm cận.'
                            )
                loigiai_th_2 = ('Từ đồ thị ta thấy $x=%s$ là tiệm cận đứng của đồ thị hàm số $f(x)$.'%(latex(tcd))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1, loigiai_th_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Hàm số $f(x)$ đạt cực đại tại điểm $x=%s$'%(latex(x2))
                vd_da_1_s = 'Hàm số $f(x)$ đạt cực đại tại điểm $x=%s$'%(latex(x1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True Hàm số $f(x)$ đạt cực tiểu tại điểm $x=%s$'%(latex(x1))
                vd_da_2_s = 'Hàm số $f(x)$ đạt cực tiểu tại điểm $x=%s$'%(latex(x2))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]
                vd_da_2=random.choice(list_vd_da_2)

                vd_da_3_d = '\\True Giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$'%(latex(y2))
                vd_da_3_s = 'Giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CT}}=%s$'%(latex(y1))
                list_vd_da_3=[vd_da_3_d,vd_da_3_s]
                vd_da_3=random.choice(list_vd_da_3)

                vd_da_4_d = '\\True Giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$'%(latex(y1))
                vd_da_4_s = 'Giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$'%(latex(y2))
                list_vd_da_4=[vd_da_4_d,vd_da_4_s]
                vd_da_4=random.choice(list_vd_da_4)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2]

                # Nội dung lời giải
                loigiai_vd_1 = ('Hàm số $f(x)$ đạt cực đại tại điểm $x=%s$.'%(latex(x2))
                            )
                loigiai_vd_2 = ('Hàm số $f(x)$ đạt cực tiểu tại điểm $x=%s$.'%(latex(x1))
                            )
                loigiai_vd_3 = ('Giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$.'%(latex(y2))
                            )
                loigiai_vd_4 = ('Giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$.'%(latex(y1))
                            )


                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Điểm cực đại của đồ thị hàm số $f(x)$ là $\\left(%s;%s\\right)$'%(latex(x2),latex(y2))
                vdc_da_1_s = 'Điểm cực đại của đồ thị hàm số $f(x)$ là $\\left(%s;%s\\right)$'%(latex(x1),latex(y1))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Điểm cực tiểu của đồ thị hàm số $f(x)$ là $\\left(%s;%s\\right)$'%(latex(x1),latex(y1))
                vdc_da_2_s = 'Điểm cực tiểu của đồ thị hàm số $f(x)$ là $\\left(%s;%s\\right)$'%(latex(x2),latex(y2))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Điểm cực đại của đồ thị hàm số $f(x)$ là $\\left(%s;%s\\right)$.'%(latex(x2),latex(y2))
                            )
                loigiai_vdc_2 = ('Điểm cực tiểu của đồ thị hàm số $f(x)$ là $\\left(%s;%s\\right)$.'%(latex(x1),latex(y1))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n \\immini{'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n }{'+hinhve+'}'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

