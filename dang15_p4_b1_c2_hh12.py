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


def bt_dang15_p4_b1_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                xa=randint(-8,8)
                ya=randint(-8,8)
                za=randint(-5,5)
                xb=randint(-6,6)
                yb=randint(-7,7)
                zb=randint(-5,6)
                xc=randint(-6,6)
                yc=randint(-7,7)
                zc=randint(-6,6)
                xd=randint(-6,6)
                yd=randint(-7,7)
                zd=randint(-6,6)
                x1=xb-xa
                y1=yb-ya
                z1=zb-za
                x2=xc-xa
                y2=yc-ya
                z2=zc-za
                xn=y1*z2-z1*y2
                yn=z1*x2-x1*z2
                zn=x1*y2-y1*x2
                u=math.gcd(math.gcd(xn,yn),zn)
                a=nsimplify(xn/u)
                b=nsimplify(yn/u)
                c=nsimplify(zn/u)
                d=-nsimplify((xn*xa+yn*ya+zn*za)/u)
                dk=a*xd+b*yd+c*zd+d
                x_1=xc-xb
                y_1=yc-yb
                z_1=zc-zb
                x_2=xd-xa
                y_2=yd-ya
                z_2=zd-za
                x_n=y_1*z_2-z_1*y_2
                y_n=z_1*x_2-x_1*z_2
                z_n=x_1*y_2-y_1*x_2
                v=math.gcd(math.gcd(x_n,y_n),z_n)
                a1=nsimplify(x_n/v)
                b1=nsimplify(y_n/v)
                c1=nsimplify(z_n/v)
                d1=-nsimplify((x_n*xb+y_n*yb+z_n*zb)/v)
                pt=a1*x+b1*y+c1*z+d1


                while xa==xb or ya==yb or za==zb or x_n==0 or y_n==0 or z_n==0 or dk==0:
                    x,y,z=symbols('x,y,z')
                    xa=randint(-8,8)
                    ya=randint(-8,8)
                    za=randint(-5,5)
                    xb=randint(-6,6)
                    yb=randint(-7,7)
                    zb=randint(-5,6)
                    xc=randint(-6,6)
                    yc=randint(-7,7)
                    zc=randint(-6,6)
                    xd=randint(-6,6)
                    yd=randint(-7,7)
                    zd=randint(-6,6)
                    x1=xb-xa
                    y1=yb-ya
                    z1=zb-za
                    x2=xc-xa
                    y2=yc-ya
                    z2=zc-za
                    xn=y1*z2-z1*y2
                    yn=z1*x2-x1*z2
                    zn=x1*y2-y1*x2
                    u=math.gcd(math.gcd(xn,yn),zn)
                    a=nsimplify(xn/u)
                    b=nsimplify(yn/u)
                    c=nsimplify(zn/u)
                    d=-nsimplify((xn*xa+yn*ya+zn*za)/u)
                    dk=a*xd+b*yd+c*zd+d
                    x_1=xc-xb
                    y_1=yc-yb
                    z_1=zc-zb
                    x_2=xd-xa
                    y_2=yd-ya
                    z_2=zd-za
                    x_n=y_1*z_2-z_1*y_2
                    y_n=z_1*x_2-x_1*z_2
                    z_n=x_1*y_2-y_1*x_2
                    v=math.gcd(math.gcd(x_n,y_n),z_n)
                    a1=nsimplify(x_n/v)
                    b1=nsimplify(y_n/v)
                    c1=nsimplify(z_n/v)
                    d1=-nsimplify((x_n*xb+y_n*yb+z_n*zb)/v)
                    pt=a1*x+b1*y+c1*z+d1




                # Nội dung câu hỏi
                noidungcauhoi =  ('Trong không gian $Oxyz$, cho tứ diện $ABCD$ có các đỉnh $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s)$ và $D(%s;%s;%s)$. Viết phương trình mặt phẳng $(P)$ đi qua cạnh $BC$ và song song với cạnh $AD$.'
                                %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb),latex(xc),latex(yc),latex(zc),latex(xd),latex(yd),latex(zd)))

                # Nội dung lời giải
                loigiai = ('Mặt phẳng $(P)$ nhận $\\vec{BC}=(%s;%s;%s), \\vec{AD}=(%s;%s;%s)$ làm cặp vectơ chỉ phương nên có vectơ pháp tuyến là '
                        '$\\vec{n}=\\left[\\vec{BC},\\vec{AD}\\right]=(%s;%s;%s)$.\\\\ \n'
                        'Mặt phẳng $(P)$ đi qua điểm $B(%s;%s;%s)$ và nhận $\\vec{n}=(%s;%s;%s)$ làm một vectơ pháp tuyến nên có phương trình là\\\\ \n'
                        '\\hspace*{1cm}$%s(x-%s)+%s(x-%s)+%s(x-%s)=0 \\Leftrightarrow %s=0$.\\\\ \n'
                        'Vậy phương trình mặt phẳng $(P)$ là $%s=0$.'

                        %(latex(x_1),latex(y_1),latex(z_1),
                        latex(x_2),latex(y_2),latex(z_2),
                        latex(x_n),latex(y_n),latex(z_n),
                        latex(xb),latex(yb),latex(zb),
                        latex(x_n),latex(y_n),latex(z_n),
                        latex(x_n),latex(xb),latex(y_n),latex(yb),latex(z_n),latex(zb),latex(pt),
                        latex(pt)


                        )
                        )

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('--','+').replace('+-','-')
            return content 

