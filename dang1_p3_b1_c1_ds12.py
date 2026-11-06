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


def bt_dang1_p3_b1_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='2':
                t=symbols('t')
                docao=randint(1,9)
                a=randint(-20,-2)
                b=randint(2,20)
                c=randint(2,20)
                h=a*t**2+b*t+c
                daoham=2*a*t+b
                h1=a*(Rational(-b,2*a))**2+b*(Rational(-b,2*a))+c
                v=randint(20,40)
                while h1<=docao:
                    docao=randint(1,9)
                    a=randint(-20,-2)
                    b=randint(2,20)
                    c=randint(2,20)
                    h=a*t**2+b*t+c
                    daoham=2*a*t+b
                    h1=a*(Rational(-b,2*a))**2+b*(Rational(-b,2*a))+c

                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một vật được phóng thẳng đứng lên trên từ độ cao $%s$ m với vận tốc ban đầu là $%s$ m/s$zz$ Trong Vật lí, ta biết rằng khi bỏ qua sức cản của không khí thì độ cao $h$ (mét) của vật sau $t$ (giây) được cho bởi công thức $h(t)=%s$$zz$ Độ cao lớn nhất của vật đạt được là bao nhiêu? (Làm tròn kết quả đến hàng phần chục)$zz$ \n'
                                %(latex(docao),latex(v),latex(h))
                                )

                # Nội dung lời giải
                loigiai = ('Ta có \\\\ \n'
                        '\\hspace*{1cm} $h\'(t)=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} $h\'(t)=0 \\Leftrightarrow t=%s$$zz$ \\\\ \n'
                        'Bảng biến thiên \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}    \n'
                        '\\tkzTabInit[espcl=2$zz$5,lgt=1$zz$5]   \n'
                        '{$t$/1,$h\'(t)$/0$zz$7,$h(t)$/2$zz$1}   \n'
                        '{$0$,$%s$,$+\\infty$}   \n'
                        '\\tkzTabLine{,+,0,-,}   \n'
                        '\\tkzTabVar{-/$%s$,+/$%s$,-/$0$}   \n'
                        '\\end{tikzpicture}   \\\\ \n'
                        'Từ bảng biến thiên ta thấy cao lớn nhất của vật đạt được là $h(t)=%s \\approx %s$ (mét)$zz$'
                        %(latex(daoham),
                            latex(Rational(-b,2*a)),
                            latex(Rational(-b,2*a)),
                            latex(docao),latex(h1),
                            latex(h1), latex(kq),
                            )
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='1':
                t=symbols('t')
                docao=randint(1,9)
                a=randint(-20,-2)
                b=randint(2,20)
                c=randint(2,20)
                h=a*t**2+b*t+c
                daoham=2*a*t+b
                h1=a*(Rational(-b,2*a))**2+b*(Rational(-b,2*a))+c
                v=randint(20,40)
                while h1<=docao:
                    docao=randint(1,9)
                    a=randint(-20,-2)
                    b=randint(2,20)
                    c=randint(2,20)
                    h=a*t**2+b*t+c
                    daoham=2*a*t+b
                    h1=a*(Rational(-b,2*a))**2+b*(Rational(-b,2*a))+c
                zz=-b/(2*a)


                number = Decimal(float(zz))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một vật được phóng thẳng đứng lên trên từ độ cao $%s$ m với vận tốc ban đầu là $%s$ m/s$zz$ Trong Vật lí, ta biết rằng khi bỏ qua sức cản của không khí thì độ cao $h$ (mét) của vật sau $t$ (giây) được cho bởi công thức $h(t)=%s$$zz$ Tại thời điểm nào thì vật đạt độ cao lớn nhất? (Làm tròn kết quả đến hàng phần chục)$zz$ \n'
                                %(latex(docao),latex(v),latex(h))
                                )

                # Nội dung lời giải
                loigiai = ('Ta có \\\\ \n'
                        '\\hspace*{1cm} $h\'(t)=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} $h\'(t)=0 \\Leftrightarrow t=%s$$zz$ \\\\ \n'
                        'Bảng biến thiên \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}    \n'
                        '\\tkzTabInit[espcl=2$zz$5,lgt=1$zz$5]   \n'
                        '{$t$/1,$h\'(t)$/0$zz$7,$h(t)$/2$zz$1}   \n'
                        '{$0$,$%s$,$+\\infty$}   \n'
                        '\\tkzTabLine{,+,0,-,}   \n'
                        '\\tkzTabVar{-/$%s$,+/$%s$,-/$0$}   \n'
                        '\\end{tikzpicture}   \\\\ \n'
                        'Từ bảng biến thiên ta thấy thời điểm vật đạt độ cao lớn nhất là $t=%s \\approx %s$ (giây)$zz$'
                        %(latex(daoham),
                            latex(Rational(-b,2*a)),
                            latex(Rational(-b,2*a)),
                            latex(docao),latex(h1),
                            latex(Rational(-b,2*a)), latex(kq),
                            )
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content

