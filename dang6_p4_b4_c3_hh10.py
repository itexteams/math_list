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


def bt_dang6_p4_b4_c3_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                a=randint(3,10)
                b=randint(2,9)

                while a<=b:
                    x=symbols('x')
                    y=symbols('y')
                    a=randint(3,10)
                    b=randint(2,9)
                c=sqrt(a**2+b**2)
                # Câu hỏi
                noidungcauhoi = ('''Để chụp toàn cảnh, ta có thể sử dụng một gương hypebol. Máy ảnh được hướng về phía đỉnh của gương và tâm quang học của máy ảnh được đặt tại một tiêu điểm của gương (xem hình).
                                Tìm khoảng cách từ quang tâm của máy ảnh đến đỉnh của gương, biết rằng phương trình cho mặt cắt của gương là $\\dfrac{x^2}{%s^2}-\\dfrac{y^2}{%s^2}= 1$.
                                \\begin{center}
                                \\scalebox{0.7}{
                \\definecolor{ffffqq}{rgb}{1.,1.,0.}
                \\definecolor{qqwuqq}{rgb}{0.,0.39215686274509803,0.}
                \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-5.3879179085574895,-3.153230717482938) rectangle (6.23458193573728,3.1369683740720515);
                    \\draw [line width=1.pt,color=ffqqqq,fill=ffqqqq,fill opacity=1.0] (-2.5,0.) circle (0.1cm);
                    \\draw [line width=1.pt,color=ffqqqq,fill=ffqqqq,fill opacity=1.0] (2.5,0.) circle (0.1cm);
                    \\fill[line width=1.pt,color=qqwuqq,fill=qqwuqq,fill opacity=1.0] (2.5,0.4) -- (2.5,-0.4) -- (2.6,-0.4) -- (2.7,-0.3) -- (3.,-0.3) -- (3.,0.3) -- (2.7,0.3) -- (2.6,0.4) -- cycle;
                    \\fill[line width=1.pt,color=qqwuqq,fill=qqwuqq,fill opacity=1.0] (3.6,0.6) -- (4.,0.6) -- (4.,-0.6) -- (3.6,-0.6) -- cycle;
                    \\fill[line width=1.pt,color=qqwuqq,fill=qqwuqq,fill opacity=1.0] (4.8,0.3) -- (5.,0.2) -- (5.1,0.3) -- (5.3,0.3) -- (5.3,-0.3) -- (5.1,-0.3) -- (5.,-0.2) -- (4.8,-0.3) -- cycle;
                    \\fill[line width=1.pt,color=ffffqq,fill=ffffqq,fill opacity=1.0] (3.,0.5) -- (3.6,0.6) -- (3.6,-0.6) -- (3.,-0.5) -- cycle;
                    \\fill[line width=1.pt,color=ffffqq,fill=ffffqq,fill opacity=1.0] (4.,0.6) -- (4.8,0.4) -- (4.8,-0.4) -- (4.,-0.6) -- cycle;
                    \\draw [line width=1.pt] (2.5,0.4)-- (2.5,-0.4);
                    \\draw [line width=1.pt] (2.5,-0.4)-- (2.6,-0.4);
                    \\draw [line width=1.pt] (2.6,-0.4)-- (2.6,0.4);
                    \\draw [line width=1.pt] (2.6,0.4)-- (2.5,0.4);
                    \\draw [line width=1.pt] (2.6,0.4)-- (2.7,0.3);
                    \\draw [line width=1.pt] (2.7,0.3)-- (2.7,-0.3);
                    \\draw [line width=1.pt] (2.7,-0.3)-- (2.6,-0.4);
                    \\draw [line width=1.pt] (2.7,-0.3)-- (3.,-0.3);
                    \\draw [line width=1.pt] (3.,-0.3)-- (3.,0.3);
                    \\draw [line width=1.pt] (3.,0.3)-- (2.7,0.3);
                    \\draw [line width=1.pt] (3.,0.3)-- (3.,0.5);
                    \\draw [line width=1.pt] (3.,0.5)-- (3.6,0.6);
                    \\draw [line width=1.pt] (3.6,0.6)-- (4.,0.6);
                    \\draw [line width=1.pt] (4.,0.6)-- (4.8,0.4);
                    \\draw [line width=1.pt] (4.8,0.4)-- (4.8,-0.4);
                    \\draw [line width=1.pt] (4.8,-0.4)-- (4.,-0.6);
                    \\draw [line width=1.pt] (4.,-0.6)-- (3.6,-0.6);
                    \\draw [line width=1.pt] (3.6,-0.6)-- (3.,-0.5);
                    \\draw [line width=1.pt] (3.,-0.5)-- (3.,-0.3);
                    \\draw [line width=1.pt] (3.6,-0.6)-- (3.6,0.6);
                    \\draw [line width=1.pt] (4.,0.6)-- (4.,-0.6);
                    \\draw [line width=1.pt] (4.8,0.3)-- (5.,0.2);
                    \\draw [line width=1.pt] (5.,0.2)-- (5.,-0.2);
                    \\draw [line width=1.pt] (5.,-0.2)-- (4.8,-0.3);
                    \\draw [line width=1.pt] (5.,0.2)-- (5.1,0.3);
                    \\draw [line width=1.pt] (5.1,0.3)-- (5.3,0.3);
                    \\draw [line width=1.pt] (5.3,0.3)-- (5.3,-0.3);
                    \\draw [line width=1.pt] (5.3,-0.3)-- (5.1,-0.3);
                    \\draw [line width=1.pt] (5.1,-0.3)-- (5.,-0.2);
                    \\draw [line width=1.pt] (-2.4,0.)-- (2.6,0.);
                    \\draw [line width=1.pt] (-4.008799369069373,1.7371292684664406)-- (-3.9815825850655284,-1.7214092977628168);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (-3.9951291233337147,0.)-- (-2.3213587608310133,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.6,0.)-- (5.3,0.);
                    \\draw [->,line width=1.pt] (5.3,0.) -- (6.,0.);
                    \\draw [->,line width=1.pt] (0.,-3.) -- (0.,3.);
                    \\draw (5.595983043193612,0) node[anchor=north west] {$x$};
                    \\draw (-0.5,3) node[anchor=north west] {$y$};
                    \\draw (-0.6,0) node[anchor=north west] {$O$};
                    \\draw (1.620704937109274,-0.966029510520924) node[anchor=north west] {\\parbox{1.5455657931940545 cm}{Tâm máy ảnh}};
                    \\draw (-2.546152836738164,2.274859869138119) node[anchor=north west] {\\parbox{1.5455657931940545 cm}{Gương hypebol}};
                    \\draw [line width=1.pt] (-3.3054787892900275,1.3158827860457658)-- (-2.7189700543805135,1.7397124261892085);
                    \\draw [line width=1.pt] (2.4329490537256557,-0.15282307192697722)-- (2.0237592222183216,-0.8628877795426282);
                    \\draw[domain=2:5, samples=200, smooth, variable=\\x, red, thick]
                    plot ({\\x}, {sqrt(0.25*\\x*\\x - 1)});
                    \\draw[domain=2:5, samples=200, smooth, variable=\\x, red, thick]
                    plot ({\\x}, {-sqrt(0.25*\\x*\\x - 1)});
                    \\draw[domain=-5:-2, samples=200, smooth, variable=\\x, red, thick]
                    plot ({\\x}, {sqrt(0.25*\\x*\\x - 1)});
                    \\draw[domain=-5:-2, samples=200, smooth, variable=\\x, red, thick]
                    plot ({\\x}, {-sqrt(0.25*\\x*\\x - 1)});
                \\end{tikzpicture}}
            \\end{center}'''


                                %(latex(a**2), latex(b**2)))

                # Nội dung lời giải
                loigiai=('Gọi $(H):\\dfrac{x^2}{%s^2}-\\dfrac{y^2}{%s^2}= 1 \\Rightarrow \\heva{& a^2=%s\\\\&b^2=%s} \\Rightarrow \\heva{& a=%s\\\\&b=%s}\\Rightarrow c=\\sqrt{a^2+b^2}=%s$.\\\\ \n'
                        'Tiêu điểm của gương là $F_1(%s;0)$ và $F_2(%s;0)$.\\\\ \n'
                        'Đỉnh của gương là $A_1(%s;0)$.\\\\ \n'
                        'Vậy khoảng cách từ tâm của máy ảnh tới đỉnh của gương là\\\\ \n'
                        '$F_2A_1=\\sqrt{(-%s-%s)^2}=%s$.'
                        %(latex(a**2),latex(b**2),latex(a**2),latex(b**2),latex(a),latex(b),latex(c),
                        latex(-c),latex(c),
                        latex(a),
                        latex(c),latex(a),latex(c+a),

                        ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('- +','-').replace('+ -', '-').replace('- -', '+')
            return content 

