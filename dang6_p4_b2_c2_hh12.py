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


def bt_dang6_p4_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x,y,z,t,s=symbols('x,y,z,t,s')
                a1=randint(-6,6)
                b1=randint(-6,6)
                c1=randint(-7,7)
                a2=randint(-6,6)
                b2=randint(-6,6)
                c2=randint(-7,7)
                xa=randint(-6,6)
                ya=randint(-6,6)
                za=randint(-7,7)
                xb=randint(-6,6)
                yb=randint(-6,6)
                zb=randint(-7,7)
                x1=xb-xa
                y1=yb-ya
                z1=zb-za
                h1=b1*c2-b2*c1
                h2=a2*c1-a1*c2
                h3=a1*b2-a2*b1
                tch=x1*h1+y1*h2+z1*h3
                while a1==0 or b1==0 or c1==0 or a2==0 or b2==0 or c2==0 or a1/a2==b1/b2 or xa==xb or x1==0 or y1==0 or z1==0 or tch!=0:
                    a1=randint(-6,6)
                    b1=randint(-6,6)
                    c1=randint(-7,7)
                    a2=randint(-6,6)
                    b2=randint(-6,6)
                    c2=randint(-7,7)
                    xa=randint(-6,6)
                    ya=randint(-6,6)
                    za=randint(-7,7)
                    xb=randint(-6,6)
                    yb=randint(-6,6)
                    zb=randint(-7,7)
                    x1=xb-xa
                    y1=yb-ya
                    z1=zb-za
                    h1=b1*c2-b2*c1
                    h2=a2*c1-a1*c2
                    h3=a1*b2-a2*b1
                    tch=x1*h1+y1*h2+z1*h3
                hd1=xa+a1*t
                td1=ya+b1*t
                cd1=za+c1*t
                hd2=xb+a2*s
                td2=yb+b2*s
                cd2=zb+c2*s




                # Nội dung câu hỏi
                noidungcauhoi = ('Trong không gian với hệ tọa độ $Oxyz$, xét vị trí tương đối của hai đường thẳng $$\\Delta_1: \\heva{&x=%s\\\\&y=%s\\\\&z=%s},\\hspace*{0.5cm}\\Delta_2: \\heva{&x=%s\\\\&y=%s\\\\&z=%s}.$$'
                                %(latex(hd1),latex(td1),latex(cd1),latex(hd2),latex(td2),latex(cd2)
                                ))

                # Nội dung lời giải
                loigiai =  ('Đường thẳng $\\Delta_1$ đi qua điêm $M_1=(%s;%s;%s)$ có $\\vec{u_1}=(%s;%s;%s)$ là vectơ chỉ phương.\\\\ \n'
                            'Đường thẳng $\\Delta_2$ đi qua điêm $M_2=(%s;%s;%s)$ có $\\vec{u_2}=(%s;%s;%s)$ là vectơ chỉ phương.\\\\ \n'
                            'Ta có $\\dfrac{%s}{%s}\\neq\\dfrac{%s}{%s}$, suy ra $\\vec{u_1},\\vec{u_2}$ không cùng phương;\\\\ \n'
                            '\\hspace*{1cm}$\\vec{M_1M_2}=(%s;%s;%s)$ và $\\left[\\vec{u_1},\\vec{u_2}\\right]=(%s;%s;%s)$.\\\\ \n'
                            'Do $\\vec{M_1M_2}\\cdot\\left[\\vec{u_1},\\vec{u_2}\\right]=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=0$ nên $\\vec{u_1},\\vec{u_2},\\vec{M_1M_2}$ đồng phẳng.\\\\ \n'
                            'Vậy $\\Delta_1$ cắt $\\Delta_2$.'
                        %(latex(xa),latex(ya),latex(za),
                        latex(a1),latex(b1),latex(c1),
                        latex(xb),latex(yb),latex(zb),
                        latex(a2),latex(b2),latex(c2),
                        latex(a1),latex(a2),latex(b1),latex(b2),
                        latex(x1),latex(y1),latex(z1), latex(h1),latex(h2),latex(h3),
                        latex(x1),latex(h1),latex(y1),latex(h2),latex(z1),latex(h3)


                        ))
            if dang=='2':
                # Khai báo biến
                x,y,z,t,s=symbols('x,y,z,t,s')
                a1=randint(-6,6)
                b1=randint(-6,6)
                c1=randint(-7,7)
                a2=randint(-6,6)
                b2=randint(-6,6)
                c2=randint(-7,7)
                xa=randint(-6,6)
                ya=randint(-6,6)
                za=randint(-7,7)
                xb=randint(-6,6)
                yb=randint(-6,6)
                zb=randint(-7,7)
                x1=xb-xa
                y1=yb-ya
                z1=zb-za
                h1=b1*c2-b2*c1
                h2=a2*c1-a1*c2
                h3=a1*b2-a2*b1
                tch=x1*h1+y1*h2+z1*h3
                while a1==0 or b1==0 or c1==0 or a2==0 or b2==0 or c2==0 or a1/a2==b1/b2 or xa==xb or x1==0 or y1==0 or z1==0 or tch!=0:
                    a1=randint(-6,6)
                    b1=randint(-6,6)
                    c1=randint(-7,7)
                    a2=randint(-6,6)
                    b2=randint(-6,6)
                    c2=randint(-7,7)
                    xa=randint(-6,6)
                    ya=randint(-6,6)
                    za=randint(-7,7)
                    xb=randint(-6,6)
                    yb=randint(-6,6)
                    zb=randint(-7,7)
                    x1=xb-xa
                    y1=yb-ya
                    z1=zb-za
                    h1=b1*c2-b2*c1
                    h2=a2*c1-a1*c2
                    h3=a1*b2-a2*b1
                    tch=x1*h1+y1*h2+z1*h3
                hd1=x-xa
                td1=y-ya
                cd1=z-za
                hd2=xb+a2*t
                td2=yb+b2*t
                cd2=zb+c2*t




                # Nội dung câu hỏi
                noidungcauhoi = ('Trong không gian với hệ tọa độ $Oxyz$, xét vị trí tương đối của hai đường thẳng $$\\Delta_1: \\dfrac{%s}{%s}=\\dfrac{%s}{%s}=\\dfrac{%s}{%s},\\hspace*{0.5cm}\\Delta_2: \\heva{&x=%s\\\\&y=%s\\\\&z=%s}.$$'
                                %(latex(hd1),latex(a1),latex(td1),latex(b1),latex(cd1),latex(c1),latex(hd2),latex(td2),latex(cd2)
                                ))

                # Nội dung lời giải
                loigiai =  ('Đường thẳng $\\Delta_1$ đi qua điêm $M_1=(%s;%s;%s)$ có $\\vec{u_1}=(%s;%s;%s)$ là vectơ chỉ phương.\\\\ \n'
                            'Đường thẳng $\\Delta_2$ đi qua điêm $M_2=(%s;%s;%s)$ có $\\vec{u_2}=(%s;%s;%s)$ là vectơ chỉ phương.\\\\ \n'
                            'Ta có $\\dfrac{%s}{%s}\\neq\\dfrac{%s}{%s}$, suy ra $\\vec{u_1},\\vec{u_2}$ không cùng phương;\\\\ \n'
                            '\\hspace*{1cm}$\\vec{M_1M_2}=(%s;%s;%s)$ và $\\left[\\vec{u_1},\\vec{u_2}\\right]=(%s;%s;%s)$.\\\\ \n'
                            'Do $\\vec{M_1M_2}\\cdot\\left[\\vec{u_1},\\vec{u_2}\\right]=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=0$ nên $\\vec{u_1},\\vec{u_2},\\vec{M_1M_2}$ đồng phẳng.\\\\ \n'
                            'Vậy $\\Delta_1$ cắt $\\Delta_2$.'
                        %(latex(xa),latex(ya),latex(za),
                        latex(a1),latex(b1),latex(c1),
                        latex(xb),latex(yb),latex(zb),
                        latex(a2),latex(b2),latex(c2),
                        latex(a1),latex(a2),latex(b1),latex(b2),
                        latex(x1),latex(y1),latex(z1), latex(h1),latex(h2),latex(h3),
                        latex(x1),latex(h1),latex(y1),latex(h2),latex(z1),latex(h3)


                        ))
            if dang=='3':
                # Khai báo biến
                x,y,z,t,s=symbols('x,y,z,t,s')
                a1=randint(-6,6)
                b1=randint(-6,6)
                c1=randint(-7,7)
                a2=randint(-6,6)
                b2=randint(-6,6)
                c2=randint(-7,7)
                xa=randint(-6,6)
                ya=randint(-6,6)
                za=randint(-7,7)
                xb=randint(-6,6)
                yb=randint(-6,6)
                zb=randint(-7,7)
                x1=xb-xa
                y1=yb-ya
                z1=zb-za
                h1=b1*c2-b2*c1
                h2=a2*c1-a1*c2
                h3=a1*b2-a2*b1
                tch=x1*h1+y1*h2+z1*h3
                while a1==0 or b1==0 or c1==0 or a2==0 or b2==0 or c2==0 or a1/a2==b1/b2 or xa==xb or x1==0 or y1==0 or z1==0 or tch!=0:
                    a1=randint(-6,6)
                    b1=randint(-6,6)
                    c1=randint(-7,7)
                    a2=randint(-6,6)
                    b2=randint(-6,6)
                    c2=randint(-7,7)
                    xa=randint(-6,6)
                    ya=randint(-6,6)
                    za=randint(-7,7)
                    xb=randint(-6,6)
                    yb=randint(-6,6)
                    zb=randint(-7,7)
                    x1=xb-xa
                    y1=yb-ya
                    z1=zb-za
                    h1=b1*c2-b2*c1
                    h2=a2*c1-a1*c2
                    h3=a1*b2-a2*b1
                    tch=x1*h1+y1*h2+z1*h3
                hd1=x-xa
                td1=y-ya
                cd1=z-za
                hd2=x-xb
                td2=y-yb
                cd2=z-zb




                # Nội dung câu hỏi
                noidungcauhoi =('Trong không gian với hệ tọa độ $Oxyz$, xét vị trí tương đối của hai đường thẳng $$\\Delta_1: \\dfrac{%s}{%s}=\\dfrac{%s}{%s}=\\dfrac{%s}{%s},\\hspace*{0.5cm}\\Delta_2: \\dfrac{%s}{%s}=\\dfrac{%s}{%s}=\\dfrac{%s}{%s}.$$'
                                %(latex(hd1),latex(a1),latex(td1),latex(b1),latex(cd1),latex(c1),latex(hd2),latex(a2),latex(td2),latex(b2),latex(cd2),latex(c2)
                                ))

                # Nội dung lời giải
                loigiai =  ('Đường thẳng $\\Delta_1$ đi qua điêm $M_1=(%s;%s;%s)$ có $\\vec{u_1}=(%s;%s;%s)$ là vectơ chỉ phương.\\\\ \n'
                            'Đường thẳng $\\Delta_2$ đi qua điêm $M_2=(%s;%s;%s)$ có $\\vec{u_2}=(%s;%s;%s)$ là vectơ chỉ phương.\\\\ \n'
                            'Ta có $\\dfrac{%s}{%s}\\neq\\dfrac{%s}{%s}$, suy ra $\\vec{u_1},\\vec{u_2}$ không cùng phương;\\\\ \n'
                            '\\hspace*{1cm}$\\vec{M_1M_2}=(%s;%s;%s)$ và $\\left[\\vec{u_1},\\vec{u_2}\\right]=(%s;%s;%s)$.\\\\ \n'
                            'Do $\\vec{M_1M_2}\\cdot\\left[\\vec{u_1},\\vec{u_2}\\right]=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=0$ nên $\\vec{u_1},\\vec{u_2},\\vec{M_1M_2}$ đồng phẳng.\\\\ \n'
                            'Vậy $\\Delta_1$ cắt $\\Delta_2$.'
                        %(latex(xa),latex(ya),latex(za),
                        latex(a1),latex(b1),latex(c1),
                        latex(xb),latex(yb),latex(zb),
                        latex(a2),latex(b2),latex(c2),
                        latex(a1),latex(a2),latex(b1),latex(b2),
                        latex(x1),latex(y1),latex(z1), latex(h1),latex(h2),latex(h3),
                        latex(x1),latex(h1),latex(y1),latex(h2),latex(z1),latex(h3)


                        ))



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('--','+').replace('+-','-')
            return content       

