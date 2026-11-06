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


def bt_dang2_p4_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                h=randint(2,6)
                r=randint(4,10)
                r1=r/2
                A=Rational(-h,r1*r1)
                A1=round(((-h)/(r1*r1)),5)
                B=h
                x0=((A/3)*(r1**3)+B*r1)*2
                x1=math.sqrt(-A)
                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một chiếc cổng hình dạng là một parabol có khoảng cách giữa hai chân cổng là $%s$ m và chiều cao là $%s$ m. \n'
                                'Tính diện tích của chiếc cổng (Nếu kết quả không là số nguyên làm tròn đến hàng phần chục). \n'
                                %(latex(r),latex(h))
                                )

                # Nội dung lời giải
                loigiai = ('Xét hệ trục tọa độ như hình vẽ mà trục đối xứng của parabol trùng với trục tung, trục hoành trùng với đường tiếp đất của cổng. \n'
                        'Khi đó parabol có phương trình dạng $y=ax^2+b$.\\\\ \n'
                        'Parabol đi qua đỉnh $I(0;%s)$ nên ta có $b=%s$. \\\\ \n'
                        'Parabol cắt trục hoành tại hai điểm $(%s;0)$ và $(%s;0)$ nên ta có \\\\ \n'
                        '$$0=a\\cdot \\left(%s\\right)^2+ %s \\Rightarrow a = %s.$$ \\\\ \n'
                        'Khi đó parabol có phương trình $y=%sx^2+%s$. \\\\ \n'
                        'Vậy diện tích của cổng là $\\displaystyle\\int\\limits_{%s}^{%s}{\\left(%sx^2+%s\\right)} \\text{d}x \\approx%s$ m$^2$. \\\\ \n'

                    %(latex(B),latex(B),
                    latex(-r1),latex(r1),
                    latex(r1),latex(B),latex(A),
                        latex(A),latex(B),
                        latex(-r1),latex(r1),latex(A),latex(B),latex(kq), 
                        ))

                hinhve =('\\begin{center} \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                        '\\draw[->,color=black] (-%s,0.) -- (%s,0.) node[below left] {$x$};\n'
                        '\\foreach \\x in {%s,%s} \n'
                        '\\draw[shift={(\\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\\footnotesize $\\x$}; \n'
                        '\\draw[->,color=black] (0.,-1) -- (0.,%s) node[below left] {$y$}; \n'
                        '\\foreach \\y in {} \n'
                        '\\draw[shift={(0,\\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\\footnotesize $\\y$}; \n'
                        '\\draw[color=black] (0pt,-10pt) node[right] {\\footnotesize $0$}; \n'
                        '\\clip(-%s,-1) rectangle (%s,%s);\n'
                        '\\draw [samples=1000,rotate around={0:(0,0)},xshift=0.cm,yshift=0cm,domain=-9:9)] plot (\\x,{(%s/(%s*%s))*(\\x)^2+%s}); \n'
                        '\\begin{scriptsize}\n'
                        '\\draw [fill=black] (0,%s) circle (1.5pt); \n'
                        '\\draw[color=black] (0.3,%s+0.2) node {$A$}; \n'
                        '\\draw [fill=black] (-%s,0.) circle (1.5pt); \n'
                        '\\draw[color=black] (-%s-0.2,0.4) node {$B$}; \n'
                        '\\draw [fill=black] (%s,0.) circle (1.5pt); \n'
                        '\\draw[color=black] (%s+0.2,0.4) node {$C$}; \n'
                        '\\draw[color=black] (-0.3,%s+0.2) node {$%s$}; \n'
                        '\\end{scriptsize} \n'
                        '\\end{tikzpicture} \n'
                '\\end{center} \n'
                %(latex(r1+0.9),latex(r1+0.9),
                    latex(-r1),latex(r1),
                    latex(B+1.2),

                    latex(r1+1),latex(r1+1),latex(B+1),
                    latex(-h),latex(r1),latex(r1),latex(B),
                    latex(B),
                    latex(B),
                    latex(r1),
                    latex(r1),
                    latex(r1),
                    latex(r1),
                    latex(B),latex(B),)
                )

                #Đáp án


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(hinhve)+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('-+', '-').replace('.0', '')
            return content                   

