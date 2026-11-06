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


def bt_dang47_p3_b2_c3_hh10(self):
    # Khai báo biến và tạo ngẫu nhiên
    a = random.randint(14, 20)  # Chiều dài AD (tương đương BC)
    b = random.randint(10, 13)  # Chiều rộng AB (tương đương CD)
    e = random.randint(4, a - 5) # Đoạn AE
    f = random.randint(3, b - 4) # Đoạn CF


    vec_EF_x = a - e
    vec_EF_y = f - b

    # Vectơ pháp tuyến của đường thẳng EF
    n_x = b - f
    n_y = a - e

    # Phương trình đường thẳng EF: n_x(x - e) + n_y(y - b) = 0 => n_x*x + n_y*y + c_val = 0
    c_val = -(n_x * e + n_y * b)

    # Khoảng cách từ B(0,0) đến EF
    tu = abs(c_val)
    mau = math.sqrt(n_x**2 + n_y**2)
    d = tu / mau

    # Làm tròn kết quả đến 2 chữ số thập phân
    kq_decimal = Decimal(float(d)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    kq = str(kq_decimal).replace('.', ',')
    kq_float = float(kq_decimal)

    # Các đáp án trắc nghiệm
    du = ['$%s$' % (kq)]
    da = random.choice(du)

    # Tạo các đáp án sai không trùng lặp
    s = [
        '$%s$' % (str(Decimal(float(kq_float + 1.25)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')),
        '$%s$' % (str(Decimal(float(kq_float + 0.85)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')),
        '$%s$' % (str(Decimal(float(kq_float + 2.15)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')),
        '$%s$' % (str(Decimal(float(kq_float - 1.15)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')),
        '$%s$' % (str(Decimal(float(kq_float - 0.75)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')),
        '$%s$' % (str(Decimal(float(kq_float - 1.55)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')),
    ]

    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)

    # Câu hỏi
    noidungcauhoi = ('''Nhân dịp nghỉ hè, Nam về quê ở với ông bà nội. Nhà ông bà nội có một ao cá có dạng hình chữ nhật $ABCD$ với chiều dài $AD = %s$ m, chiều rộng $AB = %s$ m. Phần tam giác $DEF$ là nơi ông bà nuôi vịt, $AE = %s$ m, $CF = %s$ m (tham khảo hình vẽ). Nam đứng ở vị trí $B$ câu cá. Hỏi để lưỡi câu có thể vào nơi nuôi vịt thì Nam cần quăng lưỡi câu ít nhất bao nhiêu mét? (làm tròn kết quả đến hàng phần chục).
                     \\vspace{-3.5cm} \\begin{center} 
                    \\begin{tikzpicture}[ scale=0.5]
                        \\usetikzlibrary{fadings}
                        \\tikzfading[name=cloudfade,inner color=transparent!0,outer color=transparent!100]
                        \\tikzset{x=.025cm,y=-.025cm,line cap=round,line join=round}
                        \\path[use as bounding box] (0,0) rectangle (662.48,501.76);
                        \\begin{scope}[scale=.56,transform shape]
                            \\definecolor{paper}{HTML}{FAF9F0}
                            \\definecolor{grass}{HTML}{8CAE51}
                            \\definecolor{grasslight}{HTML}{A9C663}
                            \\definecolor{grassdark}{HTML}{587E37}
                            \\definecolor{ink}{HTML}{202C1D}
                            \\definecolor{water}{HTML}{8ECDE0}
                            \\definecolor{waterdeep}{HTML}{6CB8D3}
                            \\definecolor{waterlight}{HTML}{C7E6E9}
                            \\definecolor{leafdark}{HTML}{48783E}
                            \\definecolor{leafmid}{HTML}{719B49}
                            \\definecolor{leaflight}{HTML}{B2C965}
                            \\definecolor{duckcream}{HTML}{EBE4CD}
                            \\definecolor{duckbrown}{HTML}{A18966}
                            \\definecolor{duckgreen}{HTML}{60825A}
                            \\definecolor{bill}{HTML}{D3B164}
                            \\definecolor{skin}{HTML}{F1C999}
                            \\definecolor{shirt}{HTML}{D79048}
                            \\definecolor{vest}{HTML}{B89D59}
                            \\definecolor{labelblue}{HTML}{137393}
                            \\definecolor{segment}{HTML}{BA4A37}
                            \\newcommand{\\leaf}[5]{
                                \\begin{scope}[shift={(#1,#2)},rotate=#3]
                                    \\path[fill=#5,draw=ink,line width=0.58464pt]
                                    (0,0) .. controls ({-.34*#4},{-.33*#4}) and ({-.28*#4},{-.77*#4}) .. (0,{-#4}) .. controls ({.30*#4},{-.72*#4}) and ({.34*#4},{-.25*#4}) .. cycle;
                                    \\draw[ink!80!#5,line width=0.34272pt] (0,0) .. controls ({.045*#4},{-.38*#4}) .. (0,{-.85*#4});
                            \\end{scope}}
                            \\newcommand{\\bush}[4]{
                                \\begin{scope}[shift={(#1,#2)},scale=#3]
                                    \\path[fill=grassdark,opacity=.78]
                                    (4,17) \\foreach \\angle in {0,5,...,355}{-- ({4+(101+7*sin(13*\\angle))*sin(\\angle)},
                                        {17+(101+7*sin(13*\\angle))*cos(\\angle)})} -- cycle;
                                    \\path[fill=#4,draw=ink,line width=0.8064pt,line join=round]
                                    (0,92) \\foreach \\angle in {0,18,...,342}{ .. controls ({110*sin(\\angle+3)},{110*cos(\\angle+3)})
                                        and ({110*sin(\\angle+11)},{110*cos(\\angle+11)}) .. ({92*sin(\\angle+14)},{92*cos(\\angle+14)})-- ({85*sin(\\angle+16)},{85*cos(\\angle+16)}) -- ({92*sin(\\angle+18)},{92*cos(\\angle+18)})} -- cycle;
                                    \\foreach \\ring/\\count/\\offset in {75/15/12,53/12/28,30/8/5}{
                                        \\foreach \\index in {1,...,\\count}{
                                            \\pgfmathsetmacro{\\angle}{\\index*360/\\count+\\offset}
                                            \\pgfmathsetmacro{\\px}{\\ring*sin(\\angle)}
                                            \\pgfmathsetmacro{\\py}{\\ring*cos(\\angle)}
                                            \\path[fill=leafmid,opacity=.68]
                                            (\\px,\\py) ellipse [x radius=11,y radius=15,rotate=-\\angle];
                                            \\draw[ink,line width=0.68544pt,line cap=round]
                                            ({\\px-4},{\\py+4}) .. controls ({\\px-13},{\\py+1}) and ({\\px-8},{\\py-10}) .. ({\\px-2},{\\py-5}) .. controls ({\\px+2},{\\py-16}) and ({\\px+11},{\\py-6}) .. ({\\px+8},{\\py+1});  }}
                                    \\foreach \\index in {1,...,43}{
                                        \\pgfmathsetmacro{\\angle}{rnd*360}
                                        \\pgfmathsetmacro{\\radius}{sqrt(rnd)*76}
                                        \\pgfmathsetmacro{\\px}{\\radius*sin(\\angle)}
                                        \\pgfmathsetmacro{\\py}{\\radius*cos(\\angle)}
                                        \\path[fill=leaflight,opacity=.45] (\\px,\\py) ellipse [x radius={2+rnd*2.6},y radius={2+rnd*3.4},rotate=\\angle];	}
                            \\end{scope}}
                            \\newcommand{\\rosette}[3]{
                                \\begin{scope}[shift={(#1,#2)},scale=#3]
                                    \\foreach \\angle in {0,15,...,345}{
                                        \\pgfmathsetmacro{\\length}{78+14*sin(\\angle*7)}
                                        \\leaf{{19*sin(\\angle)}}{{-19*cos(\\angle)}}{\\angle}{\\length}{leafdark}  }
                                    \\foreach \\angle in {8,28,...,348}{
                                        \\pgfmathsetmacro{\\length}{68+10*sin(\\angle*5)}
                                        \\leaf{{12*sin(\\angle)}}{{-12*cos(\\angle)}}{\\angle}{\\length}{leafmid}  }
                                    \\foreach \\angle in {0,36,...,324}{
                                        \\leaf{0}{0}{\\angle}{56}{leaflight}  }
                                    \\foreach \\angle in {18,78,...,318}{\\leaf{0}{0}{\\angle}{35}{leafmid}}
                            \\end{scope}}
                            \\newcommand{\\tuft}[3]{
                                \\begin{scope}[shift={(#1,#2)},scale=#3]
                                    \\draw[grassdark!85!ink,line width=0.46368pt,line cap=round]
                                    (-7,0) -- (-10,-10) (-3,1) .. controls (-5,-10) .. (-6,-16)
                                    (1,0) .. controls (0,-9) .. (3,-18)
                                    (5,0) .. controls (6,-7) .. (10,-13);
                            \\end{scope}}
                            \\newcommand{\\flower}[4]{
                                \\begin{scope}[shift={(#1,#2)},scale=#3]
                                    \\draw[grassdark!60!ink,line width=0.48384pt] (0,21) .. controls (2,8) and (-3,1) .. (0,-1);
                                    \\draw[grassdark!60!ink,line width=0.44352pt] (0,15) -- (-6,10) (1,11) -- (6,5);
                                    \\foreach \\angle in {0,72,...,288}{
                                        \\path[fill=#4,draw=#4!60!ink,line width=0.26208pt]
                                        (0,0) .. controls ({-4*sin(\\angle)-2*cos(\\angle)},{-4*cos(\\angle)+2*sin(\\angle)})
                                        and ({-9*sin(\\angle)-3*cos(\\angle)},{-9*cos(\\angle)+3*sin(\\angle)})
                                        .. ({-9*sin(\\angle)},{-9*cos(\\angle)})
                                        .. controls ({-9*sin(\\angle)+3*cos(\\angle)},{-9*cos(\\angle)-3*sin(\\angle)})
                                        and ({-4*sin(\\angle)+2*cos(\\angle)},{-4*cos(\\angle)-2*sin(\\angle)}) .. cycle;  }
                                    \\fill[bill] (0,0) circle [radius=1.8];
                            \\end{scope}}
                            \\newcommand{\\dragonfly}[4]{
                                \\begin{scope}[shift={(#1,#2)},rotate=#3,scale=#4]
                                    \\path[fill=paper,draw=ink,line width=0.4032pt]
                                    (0,0) .. controls (-8,-17) and (-22,-27) .. (-20,-18) .. controls (-15,-8) .. cycle
                                    (0,0) .. controls (8,-17) and (22,-27) .. (20,-18) .. controls (15,-8) .. cycle
                                    (0,1) .. controls (-10,-3) and (-27,-6) .. (-23,1) .. controls (-17,6) .. cycle
                                    (0,1) .. controls (10,-3) and (27,-6) .. (23,1) .. controls (17,6) .. cycle;
                                    \\draw[grassdark,line width=0.28224pt] (-18,-18)--(0,0)--(18,-18) (-20,1)--(0,0)--(20,1);
                                    \\draw[ink,line width=0.8064pt,line cap=round] (0,-4)--(0,17);
                                    \\draw[waterdeep,line width=0.32256pt] (0,0)--(0,14);
                                    \\fill[ink] (0,-4) circle[radius=2.5];
                                    \\draw[ink,line width=0.26208pt] (-1,-5)--(-3,-9) (1,-5)--(3,-9);
                            \\end{scope}}
                            \\newcommand{\\smallbutterfly}[5]{
                                \\begin{scope}[shift={(#1,#2)},rotate=#3,scale=#4]
                                    \\path[fill=#5,draw=ink,line width=0.4032pt]
                                    (0,0) .. controls (-16,-17) and (-16,4) .. (-5,6) .. controls (-13,10) and (-4,14) .. (0,5) .. controls (4,14) and (14,8) .. (5,4) .. controls (17,-6) and (5,-20) .. (0,0);
                                    \\draw[ink,line width=0.4032pt] (0,-2)--(0,7) (0,-2)--(-3,-6) (0,-2)--(3,-6);
                                    \\draw[ink!55!#5,line width=0.26208pt] (-8,-4)--(-2,4) (6,-7)--(2,3);
                            \\end{scope}}
                            \\newcommand{\\ripples}[3]{
                                \\begin{scope}[shift={(#1,#2)},scale=#3]
                                    \\draw[waterlight!80!white,line width=0.8064pt,line cap=round]
                                    (-39,-4) .. controls (-62,7) and (-38,21) .. (-6,22)
                                    (15,21) .. controls (45,18) and (58,7) .. (45,-4)
                                    (-51,5) .. controls (-67,16) and (-48,29) .. (-21,30)
                                    (3,32) .. controls (29,31) and (50,24) .. (55,15);
                                    \\draw[waterdeep!75!white,line width=0.4032pt]
                                    (-38,12) .. controls (-26,21) and (20,23) .. (34,15);
                                    \\draw[white,opacity=.7,line width=0.4032pt] (-32,22) .. controls (-18,27) .. (-2,26) (28,28)--(41,23);
                            \\end{scope}}
                            \\newcommand{\\duck}[5]{
                                \\begin{scope}[shift={(#1,#2)},scale=#3]
                                    \\ripples{0}{0}{1}
                                    \\path[fill=waterdeep,opacity=.27] (-39,9) ellipse [x radius=44,y radius=10];
                                    \\path[fill=#4,draw=ink,line width=0.56448pt,line join=round]
                                    (-48,-7) .. controls (-37,-5) and (-20,-26) .. (11,-15) .. controls (16,-12) and (20,-13) .. (20,-21) .. controls (16,-30) and (19,-39) .. (28,-39) .. controls (40,-40) and (44,-29) .. (37,-19) .. controls (32,-11) and (35,-3) .. (29,2) .. controls (15,17) and (-23,15) .. (-38,2) -- cycle;
                                    \\path[fill=#5,draw=ink,line width=0.52416pt] (17,-18) .. controls (20,-24) and (17,-31) .. (22,-36) .. controls (32,-46) and (45,-32) .. (38,-23) -- (33,-14) .. controls (27,-14) .. cycle;
                                    \\path[fill=bill,draw=ink,line width=0.44352pt] (38,-29) .. controls (41,-26) .. (47,-24) -- (52,-22) .. controls (46,-18) and (40,-20) .. (36,-22) -- cycle;
                                    \\fill[ink] (30,-30) circle[radius=1.5];
                                    \\path[fill=#4!85!white,draw=ink,line width=0.4032pt]  (-40,-9) .. controls (-22,-17) and (-3,-19) .. (12,-11) .. controls (6,1) and (-14,7) .. (-31,-1) -- cycle;
                                    \\draw[ink!85!#4,line width=0.34272pt,line cap=round]  (-39,-7)--(-26,-3)--(-31,-9) (-30,-13)--(-17,-6)--(-23,-13)  (-19,-15)--(-9,-8) (-24,-1) .. controls (-14,5) .. (0,1) (-45,-6)--(-38,0) (-39,-2)--(-32,3);
                                    \\draw[#4!60!white,line width=0.48384pt] (-30,5) .. controls (-13,13) and (15,10) .. (23,3);
                            \\end{scope}}
                            \\newcommand{\\pointmark}[2]{
                                \\shade[ball color=waterdeep,draw=ink,line width=0.6048pt] (#1,#2) circle[radius=8];
                                \\fill[duckbrown!70!white] ({#1-2.2},{#2-2.4}) circle[radius=2.2];
                                \\fill[leaflight!80!white] ({#1+2.8},{#2+2}) circle[radius=1.25];
                                \\fill[segment!55!waterdeep] ({#1-2},{#2+3.5}) circle[radius=1.3];}
                            \\newcommand{\\vertexlabel}[3]{
                                \\node[inner sep=0pt,text=labelblue] at (#1,#2)
                                {\\fontfamily{phv}\\itshape\\fontsize{52}{52}\\selectfont
                                    \\pdfliteral direct {q 1.8 w 0.70 0.82 0.52 RG 2 Tr}#3\\pdfliteral direct {Q}};}
                            \\clip (0,0) rectangle (1183,896);
                            \\fill[paper] (0,0) rectangle (1183,896);
                            \\pgfmathsetseed{271828}
                            \\path[fill=duckbrown,opacity=.035]
                            \\foreach \\index in {1,...,350}{
                                \\pgfextra{
                                    \\pgfmathsetmacro{\\px}{rnd*1183}
                                    \\pgfmathsetmacro{\\py}{rnd*896}
                                }
                                (\\px,\\py) ellipse [x radius={.3+rnd*.9},y radius={.3+rnd*1.4}]
                            };
                            \\path[fill=grass]
                            (75,190)
                            .. controls (72,140) and (70,102) .. (119,77)
                            .. controls (158,53) and (201,63) .. (242,65)
                            .. controls (308,69) and (374,51) .. (425,57)
                            .. controls (475,51) and (518,72) .. (563,65)
                            .. controls (626,52) and (665,60) .. (702,68)
                            .. controls (767,76) and (813,59) .. (859,57)
                            .. controls (916,53) and (962,55) .. (1009,62)
                            .. controls (1065,62) and (1100,85) .. (1109,133)
                            .. controls (1128,207) and (1105,290) .. (1117,365)
                            .. controls (1127,451) and (1127,526) .. (1116,594)
                            .. controls (1111,669) and (1110,723) .. (1110,777)
                            .. controls (1115,827) and (1097,854) .. (1063,865)
                            .. controls (1010,878) and (962,863) .. (901,864)
                            .. controls (834,858) and (797,866) .. (748,866)
                            .. controls (669,864) and (618,875) .. (560,867)
                            .. controls (492,866) and (439,879) .. (382,875)
                            .. controls (321,880) and (279,868) .. (233,863)
                            .. controls (182,866) and (142,864) .. (114,849)
                            .. controls (79,832) and (84,789) .. (79,749)
                            .. controls (73,690) and (81,635) .. (85,576)
                            .. controls (81,497) and (71,436) .. (77,366)
                            .. controls (83,294) and (78,240) .. cycle;
                            \\begin{scope}
                                \\clip (75,190) .. controls (72,115) and (82,80) .. (147,64)
                                -- (220,65)--(420,55)--(550,67)--(640,56)--(733,73)--(874,55)
                                --(1009,62) .. controls (1091,65) and (1115,105) .. (1117,179)
                                --(1124,453)--(1113,677)--(1110,786)
                                .. controls (1117,846) and (1084,866) .. (1040,867)
                                --(803,864)--(570,869)--(390,878)--(235,863)
                                .. controls (124,872) and (84,853) .. (82,784)
                                --(79,697)--(85,576)--(74,437)--cycle;
                                \\path[fill=grasslight,opacity=.12]
                                \\foreach \\index in {1,...,600}{
                                    \\pgfextra{
                                        \\pgfmathsetmacro{\\px}{75+rnd*1050}
                                        \\pgfmathsetmacro{\\py}{55+rnd*820}
                                        \\pgfmathsetmacro{\\radius}{1+rnd*4}
                                    }
                                    (\\px,\\py) ellipse[x radius=\\radius,y radius={\\radius*.65}]
                                };
                                \\path[fill=grassdark,opacity=.06]
                                \\foreach \\index in {1,...,210}{
                                    \\pgfextra{
                                        \\pgfmathsetmacro{\\px}{75+rnd*1050}
                                        \\pgfmathsetmacro{\\py}{55+rnd*820}
                                    }
                                    (\\px,\\py) ellipse[x radius={1+rnd*2},y radius={1+rnd*3}]
                                };
                            \\end{scope}
                            \\foreach \\index in {0,...,159}{
                                \\pgfmathsetmacro{\\px}{117+\\index*6}
                                \\pgfmathsetmacro{\\py}{62+5*sin(\\index*13)+3*cos(\\index*7)}
                                \\path[fill=grass] (\\px,{\\py+4}) .. controls ({\\px-1},{\\py-2}) and ({\\px+5},{\\py-6-rnd*7}) .. ({\\px+7},{\\py-5-rnd*5}) -- ({\\px+5},{\\py+6}) -- cycle;
                                \\pgfmathsetmacro{\\by}{868+5*sin(\\index*17)}
                                \\path[fill=grass] (\\px,{\\by-5}) -- ({\\px+2},{\\by+4+rnd*6}) -- ({\\px+8},{\\by-1}) -- ({\\px+10},{\\by-6}) -- cycle;
                            }
                            \\foreach \\index in {0,...,109}{
                                \\pgfmathsetmacro{\\py}{124+\\index*6.5}
                                \\pgfmathsetmacro{\\lx}{79+4*sin(\\index*11)}
                                \\pgfmathsetmacro{\\rx}{1118+4*sin(\\index*9)}
                                \\path[fill=grass] (\\lx,\\py)--({\\lx-7-rnd*5},{\\py-8})--({\\lx-3},{\\py+3})--({\\lx+5},{\\py+9})--cycle;
                                \\path[fill=grass] (\\rx,\\py)--({\\rx+5+rnd*7},{\\py-7})--({\\rx+3},{\\py+4})--({\\rx-5},{\\py+9})--cycle;
                            }
                            \\fill[water] (247,188) rectangle (949,746);
                            \\begin{scope}
                                \\clip (250,191) rectangle (946,743);
                                \\shade[top color=waterlight!35!water,bottom color=waterdeep!85!water]
                                (247,188) rectangle (949,746);
                                \\path[fill=waterdeep,opacity=.15,path fading=cloudfade]
                                (598,545) ellipse[x radius=450,y radius=365];
                                \\path[fill=waterlight,opacity=.035]
                                \\foreach \\index in {1,...,325}{
                                    \\pgfextra{
                                        \\pgfmathsetmacro{\\px}{249+rnd*700}
                                        \\pgfmathsetmacro{\\py}{190+rnd*556}
                                    }
                                    (\\px,\\py) ellipse[x radius={1+rnd*8},y radius={1+rnd*4}]
                                };
                                \\foreach \\px/\\py/\\rx/\\ry in {
                                    291/261/70/44,325/254/58/53,345/272/74/44,391/308/62/47,
                                    437/311/55/37,314/318/63/38,455/343/53/29,495/330/55/28,
                                    840/544/62/45,822/581/56/39,865/625/80/52,913/650/53/41,
                                    808/649/61/42,741/657/67/35,690/681/61/27,615/678/53/32,
                                    594/419/44/29,656/421/57/26,730/406/58/27,781/416/52/29,
                                    396/547/45/27,366/584/52/38,421/637/66/41}{
                                    \\path[fill=white,opacity=.33,path fading=cloudfade]
                                    (\\px,\\py) ellipse[x radius=\\rx,y radius=\\ry];
                                }
                                \\foreach \\px/\\py/\\rx/\\ry in {
                                    335/261/40/40,371/292/46/33,410/317/51/29,
                                    820/580/43/29,850/643/52/40,700/672/58/24,608/678/35/26}{
                                    \\path[fill=white,opacity=.28,path fading=cloudfade]
                                    (\\px,\\py) ellipse[x radius=\\rx,y radius=\\ry];
                                }
                                \\begin{scope}[draw=waterlight,opacity=.72,line width=0.784pt]
                                    \\draw (298,378) .. controls (307,351) and (318,341) .. (335,331);
                                    \\draw (361,268) .. controls (383,254) and (403,245) .. (430,239);
                                    \\draw (432,247) .. controls (443,242) .. (461,240);
                                    \\draw (484,293) .. controls (507,286) .. (555,282);
                                    \\draw (447,314) .. controls (460,307) .. (477,305);
                                    \\draw (591,237) .. controls (608,232) .. (626,235);
                                    \\draw (300,451) .. controls (300,425) and (306,401) .. (316,390);
                                    \\draw (294,508) .. controls (284,480) and (287,450) .. (291,434);
                                    \\draw (343,550) .. controls (316,511) and (312,462) .. (331,423);
                                    \\draw (430,532) .. controls (407,495) and (425,437) .. (461,402);
                                    \\draw (433,553) .. controls (410,529) and (405,504) .. (407,477);
                                    \\draw (477,467) .. controls (481,429) and (502,408) .. (520,400);
                                    \\draw (486,405) .. controls (499,391) .. (535,374);
                                    \\draw (482,380) .. controls (520,360) and (558,349) .. (603,349);
                                    \\draw (640,336) .. controls (674,335) and (715,351) .. (737,373);
                                    \\draw (639,405) .. controls (648,403) .. (658,414);
                                    \\draw (584,379) .. controls (613,373) and (642,379) .. (656,386);
                                    \\draw (520,420) .. controls (546,403) and (573,396) .. (597,401);
                                    \\draw (511,444) .. controls (505,461) .. (508,472);
                                    \\draw (462,456) .. controls (436,511) and (460,544) .. (492,563);
                                    \\draw (508,511) .. controls (514,517) .. (526,522);
                                    \\draw (529,543) .. controls (545,551) .. (570,554);
                                    \\draw (573,542) .. controls (582,544) .. (590,544);
                                    \\draw (600,546) .. controls (619,546) and (636,541) .. (647,536);
                                    \\draw (601,567) .. controls (630,566) and (651,558) .. (673,543);
                                    \\draw (682,500) .. controls (694,482) and (694,465) .. (688,454);
                                    \\draw (707,526) .. controls (721,509) and (723,493) .. (717,477);
                                    \\draw (749,464) .. controls (747,439) and (738,423) .. (728,414);
                                    \\draw (762,504) .. controls (770,482) and (770,462) .. (764,446);
                                    \\draw (696,558) .. controls (703,554) .. (711,544);
                                    \\draw (637,605) .. controls (685,596) and (722,573) .. (750,544);
                                    \\draw (511,575) .. controls (539,589) and (570,590) .. (594,583);
                                    \\draw (468,581) .. controls (484,590) .. (504,596);
                                    \\draw (523,606) .. controls (546,613) .. (577,615);
                                    \\draw (582,634) .. controls (606,633) .. (643,625);
                                    \\draw (440,589) .. controls (453,607) and (481,619) .. (508,625);
                                    \\draw (827,467) .. controls (836,533) and (816,590) .. (784,614);
                                    \\draw (866,419) .. controls (873,438) .. (868,465);
                                    \\draw (897,505) .. controls (905,556) and (865,630) .. (823,656);
                                    \\draw (885,616) .. controls (869,656) and (821,686) .. (786,694);
                                    \\draw (731,659) .. controls (769,651) and (797,631) .. (815,607);
                                    \\draw (608,703) .. controls (634,708) and (661,706) .. (688,699);
                                    \\draw (275,576) .. controls (285,618) and (306,652) .. (338,672);
                                    \\draw (309,676) .. controls (321,693) and (342,707) .. (360,712);
                                    \\draw (309,711) .. controls (313,718) .. (329,725);
                                    \\draw (347,660) .. controls (372,683) and (398,695) .. (431,700);
                                    \\draw (434,683) .. controls (463,693) .. (491,694);
                                    \\draw (886,723) .. controls (902,718) .. (916,703);
                                \\end{scope}
                                \\duck{685}{243}{.85}{duckcream}{duckcream}
                                \\duck{797}{243}{.85}{duckbrown}{duckgreen}
                                \\duck{770}{296}{.85}{duckcream}{duckcream}
                                \\duck{883}{329}{.91}{duckbrown}{duckgreen}
                                \\duck{886}{383}{.86}{duckcream}{duckcream}
                                \\begin{scope}[shift={(885,260)},rotate=-28,scale=.91]
                                    \\ripples{0}{0}{.76}
                                    \\path[fill=duckcream,draw=ink,line width=0.56448pt]
                                    (-27,-5) .. controls (-31,-21) and (-14,-26) .. (7,-25)
                                    -- (36,-29) .. controls (26,-12) and (22,1) .. (9,8)
                                    .. controls (-10,15) and (-22,10) .. cycle;
                                    \\path[fill=duckbrown!60!duckcream,draw=ink,line width=0.4032pt]
                                    (-13,-12) .. controls (-2,-21) and (12,-20) .. (30,-26)
                                    .. controls (20,-6) and (4,8) .. (-10,1) -- cycle;
                                    \\draw[ink,line width=0.3024pt] (-6,-12)--(18,-21) (-4,-6)--(19,-17) (3,-4)--(16,-12) (12,-22)--(33,-30);
                                    \\path[fill=duckcream,draw=ink,line width=0.48384pt]
                                    (-29,-8) .. controls (-36,-10) and (-35,-31) .. (-25,-33)
                                    .. controls (-12,-36) and (-9,-23) .. (-18,-16) -- cycle;
                                    \\path[fill=bill,draw=ink,line width=0.4032pt] (-33,-24)--(-42,-18)--(-31,-17)--cycle;
                                    \\fill[ink] (-27,-25) circle[radius=1.4];
                                \\end{scope}
                            \\end{scope}
                            \\draw[ink!85!black,line width=1.89504pt] (247,188)--(949,188)--(949,746)--(249,746)--cycle;
                            \\draw[segment,line width=1.8144pt] (476,188)--(949,466);
                            \\bush{100}{249}{.95}{leafmid}
                            \\bush{111}{486}{1.13}{leafmid}
                            \\foreach \\angle in {12,42,...,342}{
                                \\leaf{{111+66*sin(\\angle)}}{{486+66*cos(\\angle)}}{180-\\angle}{27}{leaflight}
                            }
                            \\foreach \\angle in {0,60,...,300}{\\leaf{111}{486}{\\angle}{37}{leaflight}}
                            \\rosette{1098}{235}{1.02}
                            \\bush{1097}{423}{.69}{leafmid}
                            \\bush{1068}{829}{1.03}{leafmid}
                            \\foreach \\px/\\py/\\scale in {
                                144/118/.55,176/122/.5,194/151/.6,304/169/.85,351/170/.45,
                                216/223/.44,771/105/.47,788/164/.5,1038/104/.45,1047/123/.48,
                                931/160/.55,973/227/.36,221/390/.42,226/407/.28,
                                1057/545/.55,1094/557/.57,1038/615/.55,976/622/.6,
                                1085/626/.58,1050/678/.6,1074/677/.64,1077/696/.5,
                                214/610/.7,159/631/.55,126/724/.7,110/720/.45,
                                116/773/.38,137/826/.53,224/840/.6,254/804/.58,
                                351/784/.6,346/848/.75,413/809/.53,441/798/.4,467/798/.48,
                                490/822/.65,444/855/.6,545/784/.38,592/805/.72,645/778/.55,
                                691/833/.82,744/811/.7,798/826/.58,851/841/.67,928/816/.58,
                                289/844/.4}{\\tuft{\\px}{\\py}{\\scale}}
                            \\foreach \\px/\\py in {293/126,308/143,327/136,329/157,359/165,
                                1056/518,1064/524,1072/516,1085/546,1097/543,1051/597,
                                1022/648,1013/658,1009/650,1002/632,1030/641,
                                123/685,129/689,98/729,104/735,113/733,117/743,
                                131/825,123/691,383/782,391/794,381/807,388/804,
                                621/833,617/838,626/840,785/808,793/819,782/832,797/834,
                                910/834,946/776,879/815}{
                                \\fill[leaflight!65!yellow] (\\px,\\py) ellipse[x radius=2.2,y radius=2.8,rotate=25];
                            }
                            \\foreach \\px/\\py in {209/283,216/302,228/295,229/275,219/315,
                                987/282,990/293,982/314,721/799,725/794,317/836,321/832,317/844}{
                                \\fill[paper] (\\px,\\py) circle[radius=2.3];
                            }
                            \\flower{326}{136}{.48}{yellow!60!duckcream}
                            \\flower{345}{811}{1}{paper}
                            \\flower{373}{831}{.7}{paper}
                            \\flower{1057}{648}{1}{yellow!65!duckcream}
                            \\flower{1079}{594}{.46}{waterdeep}
                            \\flower{1093}{600}{.52}{waterdeep}
                            \\flower{900}{793}{1}{waterdeep!50!blue}
                            \\flower{844}{796}{.62}{shirt!65!yellow}
                            \\flower{868}{814}{.48}{yellow!65!duckcream}
                            \\flower{757}{780}{.6}{shirt}
                            \\flower{100}{690}{.56}{shirt!80!red}
                            \\dragonfly{210}{345}{-49}{.91}
                            \\dragonfly{865}{144}{-52}{.9}
                            \\dragonfly{992}{347}{46}{.94}
                            \\smallbutterfly{920}{116}{-27}{.8}{shirt!45!white}
                            \\smallbutterfly{1008}{554}{-31}{.94}{shirt!45!white}
                            \\smallbutterfly{131}{656}{28}{.89}{waterdeep!60!white}
                            \\begin{scope}[every path/.style={draw=ink},line width=0.68544pt]
                                \\path[fill=grassdark,opacity=.55,draw=none] (185,819) ellipse[x radius=48,y radius=13];
                                \\path[fill=duckbrown] (155,775)--(154,811)--(161,819)--(165,780)--cycle;
                                \\path[fill=duckbrown] (177,783)--(179,819)--(185,820)--(190,781)--cycle;
                                \\path[fill=duckbrown] (204,777)--(203,808)--(209,812)--(213,775)--cycle;
                                \\path[fill=duckbrown!85!black] (151,765)--(174,756)--(210,766)--(214,775)
                                .. controls (197,783) and (174,786) .. (151,774)--cycle;
                                \\path[fill=duckbrown!70!shirt] (151,765) .. controls (166,773) and (194,775) .. (211,766)
                                --(208,760)--(168,753)--cycle;
                                \\path[fill=duckgreen!65!gray] (184,738)
                                .. controls (203,739) and (214,746) .. (229,745)
                                .. controls (243,746) and (240,759) .. (235,774)
                                --(221,780)--(211,772)--(215,760)
                                .. controls (196,775) and (178,773) .. (170,762)--cycle;
                                \\draw[ink!70!duckgreen,line width=0.48384pt] (184,754) .. controls (204,759) and (222,751) .. (230,751)
                                (191,760) .. controls (204,765) .. (215,758);
                                \\path[fill=duckbrown!75!grassdark] (217,778)--(233,779)--(234,795)
                                .. controls (242,795) and (247,800) .. (244,805)
                                --(220,810)--(216,806)--cycle;
                                \\draw[ink,line width=0.44352pt] (220,805)--(243,803);
                                \\path[fill=skin] (186,672)--(184,692)--(204,703)--(212,683)--cycle;
                                \\path[fill=skin] (194,650)
                                .. controls (208,647) and (218,652) .. (220,663)
                                --(225,669)--(222,672)--(222,680)
                                .. controls (216,690) and (206,688) .. (201,681)
                                --(190,672)--cycle;
                                \\path[fill=duckbrown!75!ink] (188,657)--(201,652)--(204,665)--(196,675)--(190,671)--cycle;
                                \\fill[ink] (215,667) circle[radius=1.5];
                                \\draw[ink,line width=0.36288pt] (218,679)--(221,678);
                                \\path[fill=duckbrown!90!grassdark] (178,665)
                                .. controls (183,657) and (193,647) .. (209,641)
                                .. controls (219,641) and (225,644) .. (231,644)
                                .. controls (233,649) and (211,658) .. (199,665)
                                .. controls (189,670) and (176,672) .. cycle;
                                \\path[fill=duckbrown!85!leaflight] (182,655)--(184,640)
                                .. controls (190,632) and (207,628) .. (214,634)
                                --(222,646) .. controls (211,652) and (196,660) .. (181,659)--cycle;
                                \\draw[ink,line width=0.6048pt] (184,650) .. controls (198,649) and (209,643) .. (214,638);
                                \\path[fill=vest] (173,690)
                                .. controls (180,684) and (187,686) .. (201,695)
                                .. controls (207,709) and (210,727) .. (209,745)
                                .. controls (210,755) and (191,762) .. (174,757)
                                .. controls (155,753) and (146,744) .. (152,726)
                                .. controls (154,711) and (161,698) .. cycle;
                                \\path[fill=vest!70!shirt] (152,737)
                                .. controls (166,748) and (190,753) .. (208,744)
                                --(208,752) .. controls (190,765) and (161,754) .. (151,746)--cycle;
                                \\path[fill=vest!65!duckcream] (166,694)
                                .. controls (177,700) and (190,701) .. (200,708)
                                --(198,717) .. controls (181,713) and (167,709) .. (159,705)--cycle;
                                \\path[fill=vest!85!duckcream] (155,715)
                                .. controls (165,720) and (180,724) .. (192,725)
                                --(194,740) .. controls (180,741) and (163,735) .. (153,730)--cycle;
                                \\draw[ink!65!vest,line width=0.44352pt] (161,714)--(159,725)--(175,731)--(177,720)
                                (180,725)--(179,737)--(192,739)--(192,728);
                                \\draw[duckcream,line width=0.56448pt] (176,704)--(175,707) (180,705)--(179,708)
                                (184,707)--(183,710) (159,720)--(159,723) (162,721)--(162,724)
                                (165,722)--(165,725) (168,723)--(168,726);
                                \\path[fill=shirt] (201,698)
                                .. controls (210,696) and (216,707) .. (222,716)
                                --(242,710)--(250,723)
                                .. controls (235,733) and (226,741) .. (215,738)
                                .. controls (205,731) and (195,711) .. (197,704)--cycle;
                                \\path[fill=shirt!65!segment,draw=none] (200,702)
                                .. controls (204,716) and (208,729) .. (218,735)
                                --(226,731) .. controls (213,720) .. (208,703)--cycle;
                                \\draw[ink,line width=0.48384pt] (225,716)--(230,731) (240,712)--(246,724);
                                \\path[fill=skin] (244,711)--(249,703)--(256,701)--(263,707)
                                --(268,709)--(266,717)--(258,720)--(250,719)--cycle;
                                \\path[fill=duckgreen!55!waterdeep] (261,706)--(268,701)
                                .. controls (274,700) and (277,703) .. (281,707)
                                --(279,714)--(271,722)--(266,724)--(260,720)--cycle;
                                \\draw[ink,line width=0.4032pt] (266,708)--(276,715) (264,711)--(273,719)
                                (264,716)--(269,721) (269,704)--(279,711);
                                \\path[fill=duckbrown!70!shirt,draw=ink,line width=0.56448pt]
                                (258,706)--(408,552)--(412,550)--(269,702)--cycle;
                                \\draw[ink,line width=0.48384pt] (268,699)--(412,550);
                                \\draw[ink,line width=0.44352pt]
                                (306,656) .. controls (309,664) and (313,662) .. (313,652)
                                (342,616) .. controls (346,625) and (350,622) .. (349,610)
                                (376,580) .. controls (381,588) and (385,585) .. (383,575);
                                \\draw[ink,line width=0.6048pt] (412,550)
                                .. controls (425,590) and (390,646) .. (381,680)
                                .. controls (374,706) and (375,734) .. (397,751)
                                .. controls (414,761) and (444,759) .. (461,773)
                                .. controls (475,787) and (453,797) .. (429,797)
                                .. controls (420,797) and (420,804) .. (425,807);
                                \\path[fill=segment,draw=ink,line width=0.4032pt] (459,787)
                                .. controls (466,786) and (464,794) .. (458,794)
                                .. controls (453,793) .. cycle;
                            \\end{scope}
                            \\begin{scope}[shift={(462,658)}]
                                \\draw[waterlight,line width=0.56448pt]
                                (-16,-9) .. controls (-31,-3) .. (-30,6)
                                (14,-8) .. controls (23,-4) .. (22,1)
                                (-23,8) .. controls (-19,16) and (17,18) .. (27,9)
                                (-16,4) .. controls (-12,11) and (9,12) .. (16,5)
                                (-18,-2) .. controls (-23,0) .. (-22,5);
                                \\draw[ink,line width=0.52416pt] (0,-8)--(2,-22);
                                \\path[fill=shirt!80!red,draw=ink,line width=0.6048pt]
                                (-6,1) .. controls (-9,-10) and (4,-15) .. (6,-3)
                                --(6,1)--cycle;
                                \\path[fill=duckcream,draw=ink,line width=0.48384pt]
                                (-6,1)--(6,1) .. controls (7,9) and (-6,9) .. cycle;
                                \\draw[ink,line width=0.3024pt] (-4,13)--(4,13) (-3,18)--(3,18) (-2,21)--(2,21);
                            \\end{scope}
                            \\pointmark{247}{188}
                            \\pointmark{476}{188}
                            \\pointmark{949}{188}
                            \\pointmark{949}{466}
                            \\pointmark{949}{746}
                            \\pointmark{249}{746}
                            \\vertexlabel{237}{135}{A}
                            \\vertexlabel{471}{135}{E}
                            \\vertexlabel{992}{145}{D}
                            \\vertexlabel{990}{457}{F}
                            \\vertexlabel{993}{710}{C}
                            \\vertexlabel{290}{784}{B}
                        \\end{scope}
                    \\end{tikzpicture} \\end{center}'''
                     % (latex(a), latex(b), latex(e), latex(f)))

    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # Nội dung lời giải
    loigiai = ('''Chọn hệ trục tọa độ $Oxy$ sao cho $B(0;0)$, tia $BC$ trùng với tia $Ox$, tia $BA$ trùng với tia $Oy$. \\\\
    Khi đó, $B(0;0)$, $C(%s;0)$, $A(0;%s)$, suy ra $D(%s;%s)$. \\\\
    Vì $E$ thuộc đoạn $AD$ và $AE = %s$ nên $E(%s;%s)$. \\\\
    Vì $F$ thuộc đoạn $CD$ và $CF = %s$ nên khoảng cách từ $F$ đến trục $Ox$ là $f_y = %s$, hoành độ của $F$ là $x_F = %s$. Do đó $F(%s;%s)$. \\\\
    Vectơ chỉ phương của đường thẳng $EF$ là $\\overrightarrow{EF} = (%s; %s)$. \\\\
    Suy ra vectơ pháp tuyến của $EF$ là $\\overrightarrow{n} = (%s; %s)$. \\\\
    Phương trình đường thẳng $EF$ đi qua $E(%s;%s)$ là: \\\\
    $ %s(x - %s) + %s(y - %s) = 0 \\Leftrightarrow %sx + %sy %s = 0$. \\\\
    Để lưỡi câu vào được nơi nuôi vịt, Nam cần quăng lưỡi câu một khoảng ít nhất bằng khoảng cách từ $B$ đến đường thẳng $EF$. \\\\
    Khoảng cách đó là: $d(B, EF) = \\frac{|%s \\cdot 0 + %s \\cdot 0 %s|}{\\sqrt{%s^2 + %s^2}} = \\frac{%s}{\\sqrt{%s}} \\approx %s$ (m).'''
               % (latex(a), latex(b), latex(a), latex(b),
                  latex(e), latex(e), latex(b),
                  latex(f), latex(f), latex(a), latex(a), latex(f),
                  latex(vec_EF_x), latex(vec_EF_y),
                  latex(n_x), latex(n_y),
                  latex(e), latex(b),
                  latex(n_x), latex(e), latex(n_y), latex(b), latex(n_x), latex(n_y), latex(c_val),
                  latex(n_x), latex(n_y), latex(c_val), latex(n_x), latex(n_y), latex(tu), latex(n_x**2 + n_y**2), kq
                  ))
    dapan='\\shortans[0]{$%s$}\n'%(kq)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n\\end{minipage} \n\n')
    return content 

