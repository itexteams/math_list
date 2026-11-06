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


def bt_dang11_p4_b1_c3_hh10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                xd=randint(-9,9)
                yd=randint(-9,9)
                xe=randint(-9,9)
                ye=randint(-9,9)
                xf=randint(-9,9)
                yf=randint(-9,9)



                while xf-xe==xe-xf or xd-xe==xe-xd or (xd+xf)%2==1 or (yd+yf)%2==1:
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

                dcf1=(xd-xe)*x+(yd-ye)*y-(xd-xe)*xf-(yd-ye)*yf
                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd((xd-xe),(yd-ye)),-(xd-xe)*xf-(yd-ye)*yf)
                # Rút gọn các hệ số
                hs_a2 = (xd-xe) // gcd
                hs_b2 = (yd-ye) // gcd
                hs_c2 = (-(xd-xe)*xf-(yd-ye)*yf) // gcd
                dcf = hs_a2*x+hs_b2*y+hs_c2

                dtte1=(ym-ye)*x+(xe-xm)*y-(ym-ye)*xe-(xe-xm)*ye
                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd((ym-ye),(xe-xm)),-(ym-ye)*xe-(xe-xm)*ye)
                # Rút gọn các hệ số
                hs_a3 = (ym-ye) // gcd
                hs_b3 = (xe-xm) // gcd
                hs_c3 = (-(ym-ye)*xe-(xe-xm)*ye) // gcd
                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                dtte = hs_a3*x+hs_b3*y+hs_c3
                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng $(Oxy)$, cho tam giác $D(%s;%s),E(%s;%s)$ và $F(%s;%s)$. Lập phương trình tổng quát đường trung tuyến của tam giác $DEF$ kẻ từ $E$.'
                                %(latex(xd),latex(yd),latex(xe),latex(ye),latex(xf),latex(yf),))

                # Nội dung lời giải
                loigiai = ('Gọi $M$ là trung điểm $DF\\Rightarrow M\\left(\\dfrac{%s+%s}{2};\\dfrac{%s+%s}{2}\\right)=(%s;%s)$ \\\\ \n'
                                'Đường trung tuyến của $E$ đi qua $E(%s;%s)$ và có vectơ chỉ phương là $\\vec{ME}=(%s;%s)\\\\ \n'
                                '\\Rightarrow$ vectơ pháp tuyến $\\vec{n}=(%s;%s)$.\\\\ \n'
                                'Vậy phương trình tổng quát của đường trung tuyến xuất phát từ điểm $E$ là '
                                '$$%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0.$$'
                                %(latex(xd),latex(xf),latex(yd),latex(yf),latex(xm),latex(ym),
                                latex(xe),latex(ye),latex(xe-xm),latex(ye-ym),latex(ym-ye),latex(xe-xm),
                                latex(ym-ye),latex(xe),latex(xe-xm),latex(ye),latex(dtte),)
                            )


            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                xd=randint(-9,9)
                yd=randint(-9,9)
                xe=randint(-9,9)
                ye=randint(-9,9)
                xf=randint(-9,9)
                yf=randint(-9,9)



                while xf-xe==xe-xf or xd-xe==xe-xd or (xd+xe)%2==1 or (yd+ye)%2==1:
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

                xm=Rational((xd+xe),2)
                ym=Rational((yd+ye),2)
                dcd1=(xf-xe)*x+(yf-ye)*y-(xf-xe)*xd-(yf-ye)*yd
                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd((xf-xe),(yf-ye)),-(xf-xe)*xd-(yf-ye)*yd)
                # Rút gọn các hệ số
                hs_a1 = (xf-xe) // gcd
                hs_b1 = (yf-ye) // gcd
                hs_c1 = (-(xf-xe)*xd-(yf-ye)*yd) // gcd
                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                dcd = hs_a1*x+hs_b1*y+hs_c1

                dcf1=(xd-xe)*x+(yd-ye)*y-(xd-xe)*xf-(yd-ye)*yf
                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd((xd-xe),(yd-ye)),-(xd-xe)*xf-(yd-ye)*yf)
                # Rút gọn các hệ số
                hs_a2 = (xd-xe) // gcd
                hs_b2 = (yd-ye) // gcd
                hs_c2 = (-(xd-xe)*xf-(yd-ye)*yf) // gcd
                dcf = hs_a2*x+hs_b2*y+hs_c2



                dttf1=(ym-yf)*x+(xf-xm)*y-(ym-yf)*xf-(xf-xm)*yf
                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd((ym-yf),(xf-xm)),-(ym-yf)*xf-(xf-xm)*yf)
                # Rút gọn các hệ số
                hs_a3 = (ym-yf) // gcd
                hs_b3 = (xf-xm) // gcd
                hs_c3 = (-(ym-yf)*xf-(xf-xm)*yf) // gcd
                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                dttf = hs_a3*x+hs_b3*y+hs_c3
                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng $(Oxy)$, cho tam giác $D(%s;%s),E(%s;%s)$ và $F(%s;%s)$. Lập phương trình tổng quát đường trung tuyến của tam giác $DEF$ kẻ từ $F$.'
                                %(latex(xd),latex(yd),latex(xe),latex(ye),latex(xf),latex(yf),))

                # Nội dung lời giải
                loigiai = ('Gọi $M$ là trung điểm $DE\\Rightarrow M\\left(\\dfrac{%s+%s}{2};\\dfrac{%s+%s}{2}\\right)=(%s;%s)$ \\\\ \n'
                                'Đường trung tuyến từ $F$ đi qua $F(%s;%s)$ và có vectơ chỉ phương là $\\vec{MF}=(%s;%s)\\\\ \n'
                                '\\Rightarrow$ vectơ pháp tuyến $\\vec{n}=(%s;%s)$.\\\\ \n'
                                'Vậy phương trình tổng quát của đường trung tuyến xuất phát từ điểm $F$ là '
                                '$$%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0.$$'
                                %(latex(xd),latex(xe),latex(yd),latex(ye),latex(xm),latex(ym),
                                latex(xf),latex(yf),latex(xf-xm),latex(yf-ym),latex(ym-yf),latex(xf-xm),
                                latex(ym-yf),latex(xf),latex(xf-xm),latex(yf),latex(dttf),)
                            )

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+').replace('\\pm 0', '0').replace('1{x}', '{x}').replace('+0', '').replace('-0', '')
            return content  

