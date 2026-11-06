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


def bt_dang1_p3_b2_c1_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x1=randint(-15,15)
                y1=randint(-15,15)
                z1=randint(-15,15)
                x2=nsimplify(-x1/3)
                y2=-y1
                z2=-3*z1
                kq1=x2+y2+z2
                while  x1==y1==z1==0 or kq1>=99 or kq1<=-9:
                    x1=randint(-15,15)
                    y1=randint(-15,15)
                    z1=randint(-15,15)
                    x2=nsimplify(-x1/3)
                    y2=-y1
                    z2=-3*z1
                    kq1=x2+y2+z2

                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                if kq1==int(kq):
                    k_q='=%s'%(latex(nsimplify(kq1)))
                    kq2='%s'%(latex(nsimplify(kq1)))
                else:
                    k_q='\\approx %s'%(latex(kq))
                    kq2=kq

                # Nội dung câu hỏi
                noidungcauhoi = ('Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $A(%s;%s;%s),B(a;b;c)$$zz$ Gọi $M,N,P$ lần lượt là giao điểm của đường thẳng $AB$ với các mặt phẳng tọa độ $(Oxy),(Oxz)$ và $(Oyz)$$zz$ Biết $M,N,P$ nằm trên đoạn $AB$ sao cho $AM=MN=NP=PB$$zz$ Hỏi giá trị của biểu thức $T=a+b+c$ bằng bao nhiêu?(Kết quả làm tròn đến hàng phần chục)$zz$ '
                                %(latex(x1),latex(y1),latex(z1)))

                # Nội dung lời giải
                loigiai = ('Vì $M,N,P$ thuộc đoạn $AB$ sao cho $AM=MN=NP=PB$ nên $N$ là trung điểm của đoạn $AB$, $M$ là trung điểm của đoạn $AN$, $P$ là trung điểm đoạn $NB$$zz$\\\\ \n'
                        'Từ đó ta có $N\\left(\\dfrac{a+%s}{2};\\dfrac{b+%s}{2};\\dfrac{c+%s}{2}\\right)$$zz$\\\\ \n'
                        'Vì $M$ là trung điểm của $AN$ nên $M\\left(\\dfrac{x_A+x_N}{2};\\dfrac{y_A+y_N}{2};\\dfrac{z_A+z_N}{2}\\right)$ hay\\\\ \n'
                        '\\hspace*{1cm}$\\heva{&x_M=\\dfrac{%s+\\dfrac{a+%s}{2}}{2}\\\\&y_M=\\dfrac{%s+\\dfrac{b+%s}{2}}{2}\\\\&z_M=\\dfrac{%s+\\dfrac{c+%s}{2}}{2}}\\Leftrightarrow \\heva{&x_M=\\dfrac{a+%s}{4}\\\\&y_M=\\dfrac{b+%s}{4}\\\\&z_M=\\dfrac{c+%s}{4}}\\Rightarrow M\\left(\\dfrac{a+%s}{4};\\dfrac{b+%s}{4};\\dfrac{c+%s}{4}\\right)$$zz$\\\\ \n'
                        'Tương tự ta có $P\\left(\\dfrac{3a+%s}{4};\\dfrac{3b+%s}{4};\\dfrac{3c+%s}{4}\\right)$$zz$\\\\ \n'
                        'Lại có $M \\in (Oxy)$ nên $\\dfrac{c+%s}{4}=0 \\Leftrightarrow c=%s$\\\\ \n'
                        '\\hspace*{1cm} $N \\in (Oxz)$ nên $\\dfrac{b+%s}{2}=0 \\Leftrightarrow b=%s$\\\\ \n'
                        '\\hspace*{1cm} $P \\in (Oyz)$ nên $\\dfrac{3a+%s}{4}=0 \\Leftrightarrow a=%s$\\\\ \n'
                        'Vậy $T=a+b+c=%s+%s+%s %s$$zz$'
                        %(latex(x1),latex(y1),latex(z1),
                            latex(x1),latex(x1),latex(y1),latex(y1),latex(z1),latex(z1),latex(3*x1),latex(3*y1),latex(3*z1),latex(3*x1),latex(3*y1),latex(3*z1),
                            latex(x1),latex(y1),latex(z1),
                            latex(3*z1),latex(z2),latex(z1),latex(y2),latex(x1),latex(x2),
                            latex(x2),latex(y2),latex(z2),k_q


                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq2))
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('--', '+').replace('-+', '-').replace('+1x', '+x').replace('.', ',').replace('$zz$', '.').replace('\\text{-', '\\text{$-$').replace('{0+', '{').replace('+0', '')
            return content

