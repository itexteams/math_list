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


def bt_dang4_p3_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3 - Random các số liệu trong bài toán
                R = random.choice([15, 20, 25, 30, 35, 40]) # Bán kính (cm)
                h_min = random.choice([5, 8, 10, 12, 15, 20]) # Độ cao thấp nhất (cm)
                T = random.choice([2, 3, 4, 5, 6]) # Thời gian quay 1 vòng (giây)

                # Tính toán các hệ số
                a = R
                c = R + h_min
                b_val = Rational(2, T) # Hệ số của pi trong b (b = b_val * pi)
                shift = Rational(T, 4) # Giá trị pha ban đầu trong ngoặc
                h_max = h_min + 2*R

                # Kết quả cần tìm: P = (a*b) / (c*pi) = (a * 2*pi/T) / (c*pi) = (2*a) / (c*T)
                kq = Rational(2 * a, c * T)

                # Xử lý kết quả ra số thập phân làm tròn đến phần trăm (2 chữ số)
                kq_dec = Decimal(float(kq)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_dec).replace('.', ',') # Đổi dấu chấm thành dấu phẩy
                hinhve=r'''\definecolor{chamoisee}{rgb}{0.63, 0.47, 0.35}
            \definecolor{bistre}{rgb}{0.24, 0.17, 0.12}
            \begin{tikzpicture}[scale=0.9,line join=round, line cap=round]
            	\fill[black] 
            	(2.54,2.82).. controls ++(130:0.06) and ++(120:0.08)..(2.54,2.73)--(2.87,2.79)--(2.85,2.88)	--cycle
            	(2.57,2.5).. controls ++(130:0.06) and ++(120:0.08)..(2.57,2.41)--(2.9,2.47)--(2.88,2.56)--cycle
            	;
            	\draw[black,line width=1] (2.94,2.69)--(3.04,2.4);
            	\draw[gray, line width=1] 
            	(2.87,2.84).. controls ++(0:0.2) and ++(30:0.2).. (2.94,2.69).. controls ++(-10:0.1) and ++(30:0.2).. (2.9,2.52)
            	;
            	\draw[gray!50!white, line width=1.75] (3.02,2.34)--(3.08,2.36)
            	(1.18,2.27)--(1.16,2.34);
            	\draw[gray,line width=0.75] (1.54,2.53).. controls ++(-70:0.1) and ++(20:0.3).. (1.15,2.38)--(0.91,2.32)
            	;
            	\draw[gray,line width=0.75,decoration={aspect=0.3, segment length=0.4mm, amplitude=0.3mm,coil},decorate]  (0.91,2.32)--(0.91,2.55);
            	\fill[brown] (1.66,2.56)--(1.58,2.61).. controls ++(150:0.1) and ++(-10:0.4).. (0.87,2.66).. controls ++(-180:0.08) and ++(150:0.08).. (0.86,2.57).. controls ++(-30:0.1) and ++(140:0.2).. (1.19,2.42)--(1.22,2.42)--cycle
            	;
            	\tikzset{van/.pic={ 
            			\draw[gray,line width=1] (0.1,0)--(0.1,0.2);
            			\fill [black!40!gray] (0,0.1)--(0,0.3).. controls ++(60:0.1) and ++(120:0.1)..(0.2,0.3)--(0.2,0.1)--cycle;
            	}}
            	\path 
            	(3,0)pic[scale=0.4,shift=(60:0.1),rotate=-45]{van}
            	(-1,0)pic[scale=0.4,shift=(50:1),rotate=-70]{van}
            	;
            	\path 
            	(.28, .75) coordinate (I)
            	(3.78, .75) coordinate (J)
            	(1.84, .51) coordinate (K)
            	;
            	\def\R{1.1}
            	\foreach \n/\m in {I/7,J/0}{
            		\begin{scope}[shift={(\n)},scale=1]
            			\foreach \i in {1,2,...,12}{
            				\pgfmathsetmacro{\goc}{\i*360/12+\m}
            				\draw[gray!90!black] (0,0) -- ($(0,0)+(\goc:\R)$);
            			}
            		\end{scope}
            		\draw[chamoisee,line width=1.5] (\n) circle (\R);
            		\draw[white!70!gray,line width=1] (\n) circle (\R-.05);
            	}
            	\draw[bistre!80!, line width=0.5] (I)--(-.65,1.35) (J)--(2.7,.69);
            	\fill [red] (-0.78,1.5).. controls ++(90:0.08) and ++(150:0.1).. (-0.63,1.5)--cycle;
            	\fill [white!70!gray] 
            	(-0.78,1.22).. controls ++(100:0.1) and ++(-180:0.04).. (-0.8,1.5)--(-0.58,1.51)--cycle;
            	\fill[bistre!70!black]
            	(2.7,0.3).. controls ++(110:1) and ++(180:0.7).. (3.73,1.9).. controls ++(-90:0.05) and ++(80:0.04)..(3.72,1.82).. controls ++(180:0.7) and ++(90:0.5).. (2.76,.69).. controls ++(-70:0.2)  and ++(50:0.2).. cycle
            	(-0.87,0.95).. controls ++(75:1.4) and ++(100:1.3).. (1.42,0.85)--(1.29,0.86).. controls ++(100:1.36) and ++(75:1).. (-0.76,0.98)--cycle
            	;
            	\fill[bistre!90!] (.18,.56).. controls ++(140:0.25) and ++(-170:0.15).. (.24,.91)--
            	(1.88,.84).. controls ++(-20:0.1) and ++(90:0.3)..(2.17,0.45).. controls ++(-100:0.24) and ++(-6:0.1).. (1.77,.19)--cycle
            	;
            	\fill[white!80!gray] 
            	(.71,.58).. controls ++(150:0.17) and ++(-180:0.1).. (.76,.75)--(1.4,.7).. controls ++(-20:0.05) and ++(90:0.1)..(1.5,0.57).. controls ++(-100:0.1) and ++(-6:0.05).. (1.37,.45)--cycle
            	;
            	\draw[line width=1] (1.18,2.15)--(.39,.92)
            	(.97,1.86)--(.71,2)--(-.23,2).. controls ++(180:.1) and ++(90:.1).. (-.37,1.83)--(.21,.9)
            	;
            	\draw[line width=1.75] (1.24,2.23)--(3.09,2.23)--(3.07,2.29)
            	(3.09,2.24)--(3.23,1.84)
            	(2.04,.77)--(3.1,1.91)--(3.2,1.91)--(3.47,1.15)
            	;
            	\fill[black] (3.43,1.16).. controls ++(-80:.21) and ++(150:0).. (3.75, .75)--(3.79, .76).. controls ++(150:.2) and ++(-70:.02)..(3.5,1.17)--cycle ;
            	\draw[line width=2,line cap=butt] (1.18,2.27)--(1.73,.78);
            	\fill (I) circle (.05) (J) circle (.05);
            	\draw[white] (K) circle (.3);
            	\fill[white] (K) circle (0.15);
            	\draw[line width=1] (K)--(1.75,0.79) (1.96,0.2)--(2,0.1);
            	\tikzset{bandap/.pic={
            			\fill[bistre] (0,0) rectangle ++(2.5,1);
            			\fill[bistre] (.2,0).. controls ++(-60:.08) and ++(180:.08).. (.5,-.3)--(2,-.3).. controls ++(40:.1) and ++(-90:.08).. (2.3,0)--cycle;
            			\fill[gray](.4,0).. controls ++(-60:.08) and ++(180:.08).. (.65,-.2)--(1.75,-.2).. controls ++(40:.1) and ++(-90:.08).. (2,0)--cycle;
            	}}
            	\path
            	(2,0)pic[scale=.1,shift=(117:8.2),rotate=-20]{bandap}
            	(2,0)pic[scale=.1,shift=(-180:0.9),rotate=-15]{bandap}
            	;
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một người đang đi xe đạp và quay bàn đạp với tốc độ không đổi. Bán kính của đường tròn mà bàn đạp xe đạp vạch ra là $%s$ cm, và khi bàn đạp đi qua vị trí thấp nhất thì độ cao của nó so với mặt đất là $%s$ cm. Nếu bàn đạp của chiếc xe đạp này quay được một vòng trong $%s$ giây, thì độ cao của bàn đạp so với mặt đất sau $x$ giây kể từ khi bàn đạp đi qua vị trí thấp nhất được biểu diễn bởi hàm số $f\left( x \right)$ (cm) theo $x$ là $f\left( x \right) = a \sin b \left( x - %s \right) + c$. Khi đó, với ba hằng số $a, b, c$, hãy tìm giá trị của $\frac{ab}{c\pi}$ (làm tròn kết quả đến hàng phần trăm). (Biết rằng $a > 0, b > 0$).}{%s}'''
                                 %(latex(R), latex(h_min), latex(T), latex(shift),hinhve))

                # Nội dung lời giải
                loigiai=('''Bán kính của đường tròn là $R = %s$. Độ cao thấp nhất là $h_{\\min} = %s$.\\\\
                         Khi đó, biên độ dao động của bàn đạp là $a = R = %s$.\\\\
                         Độ cao lớn nhất của bàn đạp so với mặt đất là $h_{\\max} = h_{\\min} + 2R = %s + 2 \\cdot %s = %s$.\\\\
                         Trục đối xứng của hàm số (cũng chính là giá trị $c$) là $c = \\frac{h_{\\max} + h_{\\min}}{2} = \\frac{%s + %s}{2} = %s$.\\\\
                         Chu kì quay là $T = %s$, suy ra tần số góc $b = \\frac{2\\pi}{T} = \\frac{2\\pi}{%s} = %s \\pi$.\\\\
                         Do đó, giá trị của biểu thức cần tìm là $\\frac{ab}{c\\pi} = \\frac{%s \\cdot %s \\pi}{%s \\cdot \\pi} = %s \\approx %s$.'''
                         %(latex(R), latex(h_min),
                           latex(a),
                           latex(h_min), latex(R), latex(h_max),
                           latex(h_max), latex(h_min), latex(c),
                           latex(T), latex(T), latex(b_val),
                           latex(a), latex(b_val), latex(c), latex(kq), kq_str))

                # Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n' + str(dapan)+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

