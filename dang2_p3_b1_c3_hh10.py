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


def bt_dang2_p3_b1_c3_hh10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                #Khai báo biến
                x=symbols('x')
                y=symbols('y')
                xd=randint(-9,9)
                yd=randint(-9,9)
                xe=randint(-9,9)
                ye=randint(-9,9)
                xf=randint(-9,9)
                yf=randint(-9,9)



                while xf-xe==xe-xf or xd-xe==xe-xd or (xd+xf)%2==1 or (yd+yf)%2==1 or xf-xe==0:
                    xd=randint(-9,9)
                    yd=randint(-9,9)
                    xe=randint(-9,9)
                    ye=randint(-9,9)
                    xf=randint(-9,9)
                    yf=randint(-9,9)

                xi=Rational((xe+xf),2)
                yi=Rational((ye+yf),2)
                xi2=Rational((xe+xd),2)
                yi2=Rational((ye+yd),2)

                xm=Rational((xd+xf),2)
                ym=Rational((yd+yf),2)
                dcd1=(xf-xe)*x+(yf-ye)*y-(xf-xe)*xd-(yf-ye)*yd
                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd((xf-xe),(yf-ye)),-(xf-xe)*xd-(yf-ye)*yd)
                # Rút gọn các hệ số
                hs_a1 = (xf-xe) // gcd
                hs_b1 = (yf-ye) // gcd
                hs_c1 = (-(xf-xe)*xd-(yf-ye)*yd) // gcd
                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                dcd = hs_a1*x+hs_b1*y+hs_c1



                # Nội dung câu hỏi
                noidungcauhoi =('Trong mặt phẳng $(Oxy)$, cho tam giác $D(%s;%s),E(%s;%s)$ và $F(%s;%s)$. Phương trình tổng quát đường cao của tam giác $DEF$ kẻ từ $D$ có dạng $%s x+by+c=0$. Khi đó $b+c$ bằng bao nhiêu?\n'
                                %(latex(xd),latex(yd),latex(xe),latex(ye),latex(xf),latex(yf),latex(hs_a1),))

                # Nội dung lời giải
                loigiai = ('Đường cao kẻ từ $D$ đi qua $D(%s;%s)$ và có một vectơ pháp tuyến là $\\vec{EF}=(%s;%s)$ nên có phương trình tổng quát là \\\\ \n'
                                '$%s(x-%s)+%s(y-%s)=0\\Leftrightarrow %s=0 \\Rightarrow b=%s;c=%s$. Vậy $b+c=%s$.'
                                %(latex(xd),latex(yd),latex(xf-xe),latex(yf-ye),
                                latex(xf-xe),latex(xd),latex(yf-ye),latex(yd),latex(dcd),latex(hs_b1),latex(hs_c1),latex(hs_b1+hs_c1),)
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(hs_b1+hs_c1))

            if dang=='2':
                #Khai báo biến
                x=symbols('x')
                y=symbols('y')
                xd=randint(-9,9)
                yd=randint(-9,9)
                xe=randint(-9,9)
                ye=randint(-9,9)
                xf=randint(-9,9)
                yf=randint(-9,9)



                while xf-xe==xe-xf or xd-xe==xe-xd or (xd+xf)%2==1 or (yd+yf)%2==1 or yd-ye==0:
                    xd=randint(-9,9)
                    yd=randint(-9,9)
                    xe=randint(-9,9)
                    ye=randint(-9,9)
                    xf=randint(-9,9)
                    yf=randint(-9,9)

                xi=Rational((xe+xf),2)
                yi=Rational((ye+yf),2)
                xi2=Rational((xe+xd),2)
                yi2=Rational((ye+yd),2)

                xm=Rational((xd+xf),2)
                ym=Rational((yd+yf),2)


                dcf1=(xd-xe)*x+(yd-ye)*y-(xd-xe)*xf-(yd-ye)*yf
                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd((xd-xe),(yd-ye)),-(xd-xe)*xf-(yd-ye)*yf)
                # Rút gọn các hệ số
                hs_a2 = (xd-xe) // gcd
                hs_b2 = (yd-ye) // gcd
                hs_c2 = (-(xd-xe)*xf-(yd-ye)*yf) // gcd
                dcf = hs_a2*x+hs_b2*y+hs_c2

                # Nội dung câu hỏi
                noidungcauhoi =('Trong mặt phẳng $(Oxy)$, cho tam giác $D(%s;%s),E(%s;%s)$ và $F(%s;%s)$. Phương trình tổng quát đường cao của tam giác $DEF$ kẻ từ $F$ có dạng $ax+%s y+c=0$. Khi đó $a+c$ bằng bao nhiêu?\n'
                                %(latex(xd),latex(yd),latex(xe),latex(ye),latex(xf),latex(yf),latex(hs_b2),))

                # Nội dung lời giải
                loigiai = ('Đường cao kẻ từ $F$ đi qua $F(%s;%s)$ và có một vectơ pháp tuyến là $\\vec{ED}=(%s;%s)$ nên có phương trình tổng quát là\\\\ \n'
                                '$%s(x-%s)+%s(y-%s)=0\\Leftrightarrow %s=0 \\Rightarrow a=%s;c=%s$. Vậy $a+c=%s$.'
                                %(latex(xf),latex(yf),latex(xd-xe),latex(yd-ye),
                                latex(xd-xe),latex(xf),latex(yd-ye),latex(yf),latex(dcf),latex(hs_a2),latex(hs_c2),latex(hs_a2+hs_c2),)
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(hs_a2+hs_c2))



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('-+','-').replace('+-', '-').replace('--', '+').replace('11 x', '11f x').replace('1 x', 'x').replace('11f x', '11 x').replace('11 y', '11f y').replace('1 y', 'y').replace('11f y', '11 y')
            return content                   

