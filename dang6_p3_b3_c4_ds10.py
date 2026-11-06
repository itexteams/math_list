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


def bt_dang6_p3_b3_c4_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                a1=randint(1,40)
                b1=randint(1,40)
                c1=randint(1,40)
                d1=randint(1,40)
                a=a1/100
                b=b1*100
                c=c1*100
                d=d1*10**4
                x1 = ((b - c) - ((b-c)**2-4*a*(d+10**5))**(1/2))/(2 * a)
                while b<=c or (b-c)**2<=4*a*(d+10**5) or x1<1000 or x1>6000:
                    a1=randint(1,20)
                    b1=randint(20,40)
                    c1=randint(1,40)
                    d1=randint(1,20)
                    a=a1/100
                    b=b1*100
                    c=c1*100
                    d=d1*10**4
                    x1 = ((b - c) - ((b-c)**2-4*a*(d+10**5))**(1/2))/(2 * a)

                hsF=-a*x**2+b*x
                hsG=d/x+c
                hsP=-a*x**2+(b-c)*x-d
                hsQ=-a*x**2+(b-c)*x-d-10**5
                bpt=-a*x**2+(b-c)*x-d-10**5>0
                nbpt=solve(bpt, x)
                x3=math.ceil(x1) 
                # Câu hỏi
                noidungcauhoi = ('''Nếu một doanh nghiệp sản xuất $x$ sản phẩm trong một tháng $\\left(x \\in \\mathbb{N}^*;\\, 1 \\leq x \\leq 6000\\right)$ thì doanh thu nhận được khi bán hết số sản phẩm đó là $F(x)=%s$ (nghìn đồng), trong khi chi phí sản xuất bình quân cho mỗi sản phẩm là $G(x)=\\dfrac{%s}{x}+%s$ (nghìn đồng). Giả sử số sản phẩm sản xuất ra luôn được bán hết. Trong một tháng, doanh nghiệp đó cần sản xuất ít nhất bao nhiêu sản phẩm để lợi nhuận thu được lớn hơn $100$ triệu đồng?'''
                                %(latex(hsF),latex(d),latex(c)
                                ))
                # Nội dung lời giải
                loigiai=('''Gọi $C(x)=x\\cdot G(x)$ (nghìn đồng) là chi phí sản xuất cho $x$ sản phẩmzz\\\\
                        Lợi nhuận trong một tháng là 
                    \\begin{eqnarray*}
                        P(x)&=&F(x)-C(x)=F(x)-x\\cdot G(x)\\\\
                            &=&\\left(%s\\right)-x\\left(%s\\right)\\\\
                            &=&%szz
                    \\end{eqnarray*}
                    Để lợi nhuận thu được lớn hơn $100$ triệu đồng thì
                    \\begin{eqnarray*}
                        &&%s>100\\cdot 10^3\\\\
                        &\\Leftrightarrow& %s>0\\\\
                        &\\Leftrightarrow&%s\\\\
                        &\\Rightarrow& x_{\\text{min}}=%s\\,\\text{(sản phẩm)}zz
                    \\end{eqnarray*}
                    Vậy doanh nghiệp cần sản xuất ít nhất $%s$ sản phẩm trong một tháng để lợi nhuận thu được lớn hơn $100$ triệu đồngzz'''
                        %(latex(hsF),latex(hsG),latex(hsP),latex(hsP),latex(hsQ),latex(nbpt),latex(x3),latex(x3)
                        ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}'%(latex(x3))
            # Xuất câu tự luận
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{\n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\wedge x',"").replace('.','{,}').replace('zz','.').replace('\\frac', '\\dfrac')
            return content

