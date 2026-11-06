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


def bt_dang5_p3_b3_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                z=symbols('z')

                x0=randint(-9,9)
                y0=randint(-9,9)
                z0=randint(-9,9)

                a1=randint(-9,9)
                b1=randint(-9,9)
                c1=randint(-9,9)

                xa=randint(-9,9)
                ya=randint(-9,9)
                za=randint(-9,9)

                xb=randint(-9,9)
                yb=randint(-9,9)
                zb=randint(-9,9)

                xc=randint(-9,9)
                yc=randint(-9,9)
                zc=randint(-9,9)

                x1=xb-xa
                y1=yb-ya
                z1=zb-za

                x2=xc-xa
                y2=yc-ya
                z2=zc-za
                while a1==0 or b1==0 or c1==0 or x1*y2==x2*y1:
                    x0=randint(-9,9)
                    y0=randint(-9,9)
                    z0=randint(-9,9)

                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-9,9)

                    xa=randint(-9,9)
                    ya=randint(-9,9)
                    za=randint(-9,9)

                    xb=randint(-9,9)
                    yb=randint(-9,9)
                    zb=randint(-9,9)

                    xc=randint(-9,9)
                    yc=randint(-9,9)
                    zc=randint(-9,9)

                    x1=xb-xa
                    y1=yb-ya
                    z1=zb-za

                    x2=xc-xa
                    y2=yc-ya
                    z2=zc-za

                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd(a1,b1),c1)
                # Rút gọn các hệ số
                a = a1 // gcd
                b = b1 // gcd
                c = c1// gcd

                x3=y1*z2-y2*z1
                y3=z1*x2-z2*x1
                z3=x1*y2-x2*y1
                daiu=sqrt(a**2+b**2+c**2)
                dain=sqrt(x3**2+y3**2+z3**2)
                tu=abs(a*x3+b*y3+c*z3)
                mau=daiu*dain

                gtsin=tu/mau

                g=math.degrees(math.asin(gtsin))
                kq1=g
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)


                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho đường thẳng $d$ có phương trình $\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$ và ba điểm '
                                '$A(%s;%s;%s),B(%s;%s;%s),C(%s;%s;%s)$. Góc giữa đường thẳng $d$ và mặt phẳng $(ABC)$ bằng bao nhiêu độ (kết quả làm tròn đến hàng đơn vị)?'
                                %(latex(x0),latex(a),latex(y0),latex(b),latex(z0),latex(c),
                                latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb),latex(xc),latex(yc),latex(zc))
                                )

                # Nội dung lời giải
                loigiai = ('Đường thẳng $d$ có một vectơ chỉ phương là $\\vec{u}_d=(%s;%s;%s)$.\\\\ \n'
                        '$\\vec{AB}=(%s;%s;%s)$ và $\\vec{AC}=(%s;%s;%s)$, dễ thấy $\\vec{AB}$ không cùng phương với $\\vec{AC}$. \\\\ \n'
                        'Khi đó mặt phẳng $(ABC)$ có một vectơ pháp tuyến $\\vec{n}=[\\vec{AB},\\vec{AC}]=(%s;%s;%s)$.\\\\ \n'
                        'Ta có $\\sin(d,(ABC))=\\dfrac{|%s\\cdot (%s)+%s\\cdot (%s)+%s\\cdot (%s)|}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}\\cdot \\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%s$.\\\\ \n'
                        '$\\Rightarrow (d,(ABC)) \\approx %s^0$.'


                        %(latex(a),latex(b),latex(c),
                            latex(x1),latex(y1),latex(z1),latex(x2),latex(y2),latex(z2),
                            latex(x3),latex(y3),latex(z3),
                            latex(a),latex(x3),latex(b),latex(y3),latex(c),latex(z3), latex(a),latex(b),latex(c),latex(x3),latex(y3),latex(z3),latex(gtsin),latex(kq),
                        ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))





            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('--','+').replace('+-','-')
            return content

