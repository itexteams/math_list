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


def bt_dang6_p4_b1_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                xa=randint(-5,5)
                ya=randint(-5,5)
                za=randint(-5,5)
                xb=randint(-5,5)
                yb=randint(-5,5)
                zb=randint(-5,5)
                a=randint(-5,5)
                b=randint(-5,5)
                c=randint(-6,6)
                d=randint(-15,15)
                x1=xb-xa
                y1=yb-ya
                z1=zb-za
                pt1=a*x+b*y+c*z+d
                a1=y1*c-z1*b
                b1=a*z1-c*x1
                c1=b*x1-a*y1
                d1=-(a1*xa+b1*ya+c1*za)
                u=gcd(gcd(a1,b1),c1)
                a2=nsimplify(a1/u)
                b2=nsimplify(b1/u)
                c2=nsimplify(c1/u)
                d2=nsimplify(d1/u)
                pt2=a2*x+b2*y+c2*z+d2


                while a1==0 or b1==0 or c1==0 or xa==xb or ya==yb or za==zb or a==0 or b==0 or c==0 or a*xa+b*ya+c*za+d==0 or a*xb+b*yb+c*zb+d==0:
                    x,y,z=symbols('x,y,z')
                    xa=randint(-5,5)
                    ya=randint(-5,5)
                    za=randint(-5,5)
                    xb=randint(-5,5)
                    yb=randint(-5,5)
                    zb=randint(-5,5)
                    a=randint(-5,5)
                    b=randint(-5,5)
                    c=randint(-6,6)
                    d=randint(-15,15)
                    x1=xb-xa
                    y1=yb-ya
                    z1=zb-za
                    pt1=a*x+b*y+c*z+d
                    a1=y1*c-z1*b
                    b1=a*z1-c*x1
                    c1=b*x1-a*y1
                    d1=-(a1*xa+b1*ya+c1*za)
                    u=gcd(gcd(a1,b1),c1)
                    a2=nsimplify(a1/u)
                    b2=nsimplify(b1/u)
                    c2=nsimplify(c1/u)
                    d2=nsimplify(d1/u)
                    pt2=a2*x+b2*y+c2*z+d2



                # Nội dung câu hỏi
                noidungcauhoi =  ('Trong không gian $Oxyz$, cho hai điểm $A(%s;%s;%s), B(%s;%s;%s)$ và mặt phẳng $(P)$ có phương trình $%s=0$. Viết phương trình mặt phẳng $(Q)$ đi qua hai điểm $A,B$ và vuông góc với mặt phẳng $(P)$.'
                                %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb),latex(pt1)))

                # Nội dung lời giải
                loigiai = ('Ta có $\\vec{AB}=(%s;%s;%s)$, vectơ pháp tuyến của mặt phẳng $(P)$ là $\\vec{n_p}=(%s;%s;%s)$. \\\\ \n'
                        'Từ giả thiết suy ra $\\vec{n}=[\\vec{AB},\\vec{n_p}]=(%s;%s;%s)$ là vectơ pháp tuyến của mặt phẳng $(Q)$.\\\\ \n'
                        'Mặt phẳng $(Q)$ đi qua điểm $A(%s;%s;%s)$ và nhận $\\vec{n}=(%s;%s;%s)$ làm một vectơ pháp tuyến nên có phương trình là\\\\ \n'
                        '\\hspace*{1cm}$%s(x-%s)+%s(y-%s)+%s(z-%s)=0 \\Leftrightarrow %s=0$.\\\\ \n'
                        'Vậy phương trình mặt phẳng $(Q)$ là $%s=0$.'

                        %(latex(x1),latex(y1),latex(z1),
                        latex(a),latex(b),latex(c),
                        latex(a1),latex(b1),latex(c1),
                        latex(xa),latex(ya),latex(za),
                        latex(a1),latex(b1),latex(c1),
                        latex(a1),latex(xa),latex(b1),latex(ya),latex(c1),latex(za),latex(pt2),
                        latex(pt2)


                        )
                        )

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('--','+').replace('+-','-').replace('+1\\cdot','+').replace('+-','-').replace('-1\\cdot','-').replace('$$1\\cdot','').replace('$$-1\\cdot','-')
            return content 

