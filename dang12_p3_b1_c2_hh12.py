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


def bt_dang12_p3_b1_c2_hh12(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':
                x,y,z=symbols('x,y,z')
                a1=randint(-7,7)
                b1=randint(-7,7)
                c1=randint(-7,7)
                d1=randint(-7,7)
                a2=a1
                b2=-c1
                c2=b1
                d2=randint(-7,7)
                while a1*b1*c1*d1==0 or a2*b2*c2*d2==0 or d1==-d2 or gcd(gcd(a1,b1),c1)!=1 or gcd(gcd(a2,b2),c2)!=1 or (-d1-d2)%(2*a1)!=0:
                    x,y,z=symbols('x,y,z')
                    a1=randint(-7,7)
                    b1=randint(-7,7)
                    c1=randint(-7,7)
                    d1=randint(-7,7)
                    a2=a1
                    b2=-c1
                    c2=b1
                    d2=randint(-7,7)
                pt1=a1*x+b1*y+c1*z+d1
                pt2=a2*x+b2*y+c2*z+d2
                kq=nsimplify((-d1-d2)/2*a1)
                # Nội dung câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho điểm $M(a;b;c)$ thuộc trục $Ox$ và cách đều hai mặt phẳng $(P):%s=0$ và $(Q):%s=0$. Hỏi giá trị của biểu thức $a+b+c$ bằng bao nhiêu?'
                            %(latex(pt1),latex(pt2)))

                # Nội dung lời giải
                loigiai = ('Vì điểm $M$ thuộc trục $Ox$ nên $M(a;0;0)$.\\\\ \n'
                        'Theo bài ta có\\\\ \n'
                        '\\hspace*{1.2cm} $\\text{d}(M,(P))=\\text{d}(M,(Q))$ \\\\ \n'
                        '\\hspace*{1.2cm} $\\Leftrightarrow \\dfrac{\\abs{%s\\cdot a+%s\\cdot 0+%s\\cdot 0+%s}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=\\dfrac{\\abs{%s\\cdot a+%s\\cdot 0+%s\\cdot 0+%s}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}$\\\\ \n'
                        '\\hspace*{1.2cm} $\\Leftrightarrow \\abs{%sa+%s}=\\abs{%sa+%s}\\Leftrightarrow \\hoac{&%sa+%s=%sa+%s\\\\&%sa+%s=-%sa-%s}\\Leftrightarrow a=%s$.\\\\ \n'
                        'Vậy $a+b+c=%s+0+0=%s$.'
                        %(latex(a1),latex(b1),latex(c1),latex(d1),latex(a1),latex(b1),latex(c1),latex(a2),latex(b2),latex(c2),latex(d2),latex(a2),latex(b2),latex(c2),
                            latex(a1),latex(d1),latex(a2),latex(d2),latex(a1),latex(d1),latex(a2),latex(d2),latex(a1),latex(d1),latex(a2),latex(d2),latex(kq),
                            latex(kq),latex(kq)
                            )
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='2':
                x,y,z=symbols('x,y,z')
                a1=randint(-7,7)
                b1=randint(-7,7)
                c1=randint(-7,7)
                d1=randint(-7,7)
                a2=-c1
                b2=b1
                c2=a1
                d2=randint(-7,7)
                while a1*b1*c1*d1==0 or a2*b2*c2*d2==0  or d1==-d2 or gcd(gcd(a1,b1),c1)!=1 or gcd(gcd(a2,b2),c2)!=1 or (-d1-d2)%(2*b1)!=0:
                    x,y,z=symbols('x,y,z')
                    a1=randint(-7,7)
                    b1=randint(-7,7)
                    c1=randint(-7,7)
                    d1=randint(-7,7)
                    a2=-c1
                    b2=b1
                    c2=a1
                    d2=randint(-7,7)
                pt1=a1*x+b1*y+c1*z+d1
                pt2=a2*x+b2*y+c2*z+d2
                kq=nsimplify((-d1-d2)/2*b1)
                # Nội dung câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho điểm $M(a;b;c)$ thuộc trục $Oy$ và cách đều hai mặt phẳng $(P):%s=0$ và $(Q):%s=0$. Hỏi giá trị của biểu thức $a+b+c$ bằng bao nhiêu?'
                            %(latex(pt1),latex(pt2)))

                # Nội dung lời giải
                loigiai = ('Vì điểm $M$ thuộc trục $Oy$ nên $M(0;b;0)$.\\\\ \n'
                        'Theo bài ta có\\\\ \n'
                        '\\hspace*{1.2cm} $\\text{d}(M,(P))=\\text{d}(M,(Q))$ \\\\ \n'
                        '\\hspace*{1.2cm} $\\Leftrightarrow \\dfrac{\\abs{%s\\cdot 0+%s\\cdot b+%s\\cdot 0+%s}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=\\dfrac{\\abs{%s\\cdot 0+%s\\cdot b+%s\\cdot 0+%s}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}$\\\\ \n'
                        '\\hspace*{1.2cm} $\\Leftrightarrow \\abs{%sb+%s}=\\abs{%sb+%s}\\Leftrightarrow \\hoac{&%sb+%s=%sb+%s\\\\&%sb+%s=-%sb-%s}\\Leftrightarrow b=%s$.\\\\ \n'
                        'Vậy $a+b+c=0+%s+0=%s$.'
                        %(latex(a1),latex(b1),latex(c1),latex(d1),latex(a1),latex(b1),latex(c1),latex(a2),latex(b2),latex(c2),latex(d2),latex(a2),latex(b2),latex(c2),
                            latex(b1),latex(d1),latex(b2),latex(d2),latex(b1),latex(d1),latex(b2),latex(d2),latex(b1),latex(d1),latex(b2),latex(d2),latex(kq),
                            latex(kq),latex(kq)
                            )
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='3':
                x,y,z=symbols('x,y,z')
                a1=randint(-7,7)
                b1=randint(-7,7)
                c1=randint(-7,7)
                d1=randint(-7,7)
                a2=b1
                b2=-a1
                c2=c1
                d2=randint(-7,7)
                while a1*b1*c1*d1==0 or a2*b2*c2*d2==0  or d1==-d2 or gcd(gcd(a1,b1),c1)!=1 or gcd(gcd(a2,b2),c2)!=1 or (-d1-d2)%(2*c1)!=0:
                    x,y,z=symbols('x,y,z')
                    a1=randint(-7,7)
                    b1=randint(-7,7)
                    c1=randint(-7,7)
                    d1=randint(-7,7)
                    a2=b1
                    b2=-a1
                    c2=c1
                    d2=randint(-7,7)
                pt1=a1*x+b1*y+c1*z+d1
                pt2=a2*x+b2*y+c2*z+d2
                kq=nsimplify((-d1-d2)/2*c1)
                # Nội dung câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho điểm $M(a;b;c)$ thuộc trục $Oz$ và cách đều hai mặt phẳng $(P):%s=0$ và $(Q):%s=0$. Hỏi giá trị của biểu thức $a+b+c$ bằng bao nhiêu?'
                            %(latex(pt1),latex(pt2)))

                # Nội dung lời giải
                loigiai = ('Vì điểm $M$ thuộc trục $Oz$ nên $M(0;0;c)$.\\\\ \n'
                        'Theo bài ta có\\\\ \n'
                        '\\hspace*{1.2cm} $\\text{d}(M,(P))=\\text{d}(M,(Q))$ \\\\ \n'
                        '\\hspace*{1.2cm} $\\Leftrightarrow \\dfrac{\\abs{%s\\cdot 0+%s\\cdot 0+%s\\cdot c+%s}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=\\dfrac{\\abs{%s\\cdot 0+%s\\cdot 0+%s\\cdot c+%s}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}$\\\\ \n'
                        '\\hspace*{1.2cm} $\\Leftrightarrow \\abs{%sc+%s}=\\abs{%sc+%s}\\Leftrightarrow \\hoac{&%sc+%s=%sc+%s\\\\&%sc+%s=-%sc-%s}\\Leftrightarrow c=%s$.\\\\ \n'
                        'Vậy $a+b+c=0+0+%s=%s$.'
                        %(latex(a1),latex(b1),latex(c1),latex(d1),latex(a1),latex(b1),latex(c1),latex(a2),latex(b2),latex(c2),latex(d2),latex(a2),latex(b2),latex(c2),
                            latex(c1),latex(d1),latex(c2),latex(d2),latex(c1),latex(d1),latex(c2),latex(d2),latex(c1),latex(d1),latex(c2),latex(d2),latex(kq),
                            latex(kq),latex(kq)
                            )
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('1a', 'a').replace('+-', '-').replace('--', '+').replace('+0}', '}').replace('1b', 'b').replace('1c', 'c').replace('=+', '=')
            return content  

