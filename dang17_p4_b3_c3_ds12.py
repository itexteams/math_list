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


def bt_dang17_p4_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang == '1':
                # Khai báo biến
                x=symbols('x')
                r1=randint(6,16)
                r=r1*10
                d=(r1-2)*10
                t=nsimplify(-d/2)
                p=-t
                f=(r**2)*x-(x**3)/3
                s2=f.subs(x,p)
                s1=f.subs(x,t)
                v=nsimplify(s2-s1)

                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Cho khối tròn xoay như hình vẽ. Hai đường cong cắt trục $Oy$ biểu diễn bề mặt của khối là một phần của đường tròn tâm $O$ bán kính $%s$ cm. Tính thể tích khối tròn xoay.'
                            '}{'
                            '\\scalebox{0.6}{ ' 
                            '\\begin{tikzpicture}[scale=0.7,>=stealth, font=\\footnotesize, line join=round, line cap=round] \n'
                    '\\draw[->] (-6,0)--(6,0) node [below]{$x$};\n'
                    '\\draw[->] (0,-6.5)--(0,6.5) node [left]{$y$};\n'
                    '\\node[below] at (-0.3,0) {$O$};\n'
                    '\\draw[thick] plot[domain=-90:270, samples=100] ({4+0.7*cos(\\x)}, {4*sin(\\x)});\n'
                    '\\draw[thick] plot[domain=90:270, samples=100] ({-4+0.7*cos(\\x)}, {4*sin(\\x)});\n'
                    '\\draw[dashed] plot[domain=-90:90, samples=100] ({-4+0.7*cos(\\x)}, {4*sin(\\x)});\n'
                    '\\draw[thick,domain=-4:4,samples=100] \n'
                    'plot (\\x, {1/10*\\x*\\x-5.6});\n'
                    '\\draw[thick,domain=-4:4,samples=100] \n'
                    'plot (\\x, {-1/10*\\x*\\x+5.6});\n'
                    '\\draw [<->] (0,-1)--(4,-1);\n'
                    '\\draw [<->] (-4,-1)--(0,-1);\n'
                    '\\draw[fill=black](4,0)circle(2pt); \n' 
                    '\\draw[fill=black](-4,0)circle(2pt); \n'
                    '\\node at (-2,-1)[below]{$%s\\text{cm}$};\n'
                    '\\node at (2,-1)[below]{$%s\\text{cm}$};\n'
                    '\\node at (0,3)[right]{$%s\\text{cm}$};\n'
                    '\\end{tikzpicture}}}\n'
                    %(latex(r),latex(p),latex(p),latex(r)))

                # Nội dung lời giải
                loigiai = ('Vì đường cong cắt trục $Oy$ biểu diễn bề mặt của khối là một phần của đường tròn tâm $O$ bán kính $%s$ cm và hai mặt cắt khối vuông góc '
                        'với trục $Ox$ đi qua hai điểm có tọa độ $(%s;0),(%s;0)$ nên hình phẳng được giới hạn bởi đồ thị hàm số $y=\\sqrt{%s-x^2}$, trục hoành và hai đường thẳng $x=%s,x=%s$.\\\\ \n'
                        'Thể tích của khối tròn xoay là\\\\ \n'
                        '\\hspace*{1cm}$V=\\pi\\displaystyle\\int\\limits_{%s}^{%s}\\left(\\sqrt{%s-x^2}\\right)^2\\text{d}x=\\pi\\displaystyle\\int\\limits_{%s}^{%s}\\left(%s-x^2\\right)\\text{d}x=%s\\pi$ cm$^3$.'
                        %(latex(r),latex(t),latex(p),latex(r**2), latex(t),latex(p),
                            latex(t),latex(p),latex(r**2),latex(t),latex(p),latex(r**2),latex(v)
                            ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

