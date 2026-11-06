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


def bt_dang2_p4_b3_c2_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                lisgoc=[45,30,60]
                goc=random.choice(lisgoc)

                a=randint(2,5)
                n=randint(4,20)

                oa2=n**2+n**2-2*n*n*cos(pi-2*goc*pi/180)
                oa=sqrt(oa2)
                f1=Rational(1,a-1)*oa
                f2=a*f1

                h1=f2      
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\begin{center} \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                    '\\clip(-8.72,-2.94) rectangle (5.14,3.32); \n'
                                    '\\draw [line width=1.pt] (0.,0.) circle (1.cm); \n'
                                    '\\draw [->,line width=1.pt] (0.,0.) -- (5,0.); \n'
                                    '\\draw [->,line width=1.pt] (0.,0.) -- (-8.,0.); \n'
                                    '\\draw [->,line width=1.pt] (0.,0.) -- (2.,2.); \n'
                                    '\\draw [->,line width=1.pt] (0.,0.) -- (2.,-2.); \n'
                                    '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                                    '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,-2.)-- (4.,0.); \n'
                                    '\\draw (-0.34,0.6) node[anchor=north west] {O}; \n'
                                    '\\draw (3.8,0) node[anchor=north west] {A}; \n'
                                    '\\draw (1.9,2.5) node[anchor=north west] {C}; \n'
                                    '\\draw (1.86,-2.16) node[anchor=north west] {D}; \n'
                                    '\\draw (-7.88,-0.3) node[anchor=north west] {B}; \n'
                                    '\\draw (4.5,0.9) node[anchor=north west] {$\\vec{F_1}$}; \n'
                                    '\\draw (-6.98,1) node[anchor=north west] {$\\vec{F_2}$}; \n'
                                    '\\draw (0.78,2.3) node[anchor=north west] {$\\vec{F_3}$}; \n'
                                    '\\draw (0.72,-1.28) node[anchor=north west] {$\\vec{F_4}$}; \n'
                                    '\\draw (1.04,1.02) node[anchor=north west] {$%s^\\circ$}; \n'
                                    '\\draw (0.94,-0.12) node[anchor=north west] {$%s^\\circ$}; \n'
                                '\\end{tikzpicture} \n'
                            '\\end{center} \n'

                                'Một vật đang ở vị trí $O$ chịu tác dụng của hai lực ngược chiều nhau là $\\vec{F_1}$ và $\\vec{F_2}$, trong đó độ lớn lực $\\vec{F_2}$ lớn gấp $%s$ độ lớn lực $\\vec{F_1}$. '
                                'Người ta muốn vật dừng lại nên cần tác dụng vào vật hai lực $\\vec{F_3}, \\vec{F_4}$ có phương hợp với lực $\\vec{F_1}$ các góc $%s^\\circ$ như hình vẽ, chúng có độ lớn bằng nhau và bằng $%s$ N. Tính độ lớn của mỗi lực $\\vec{F_2}$. (làm tròn kết quả đến hàng phần chục).'
                                %(latex(goc),latex(goc),
                                latex(a),
                                latex(goc),latex(n)

                                ))

                # Nội dung lời giải
                loigiai = ('Ta có $\\vec{F_2}=-%s \\vec{F_1}$.\\\\ \n'
                        'Để vật trở về trạng thái cân bằng thì hợp lực bằng $\\vec{0}$. \\\\ \n'
                        'Tức là \\\\ \n'
                        '\\hspace*{1cm} $\\vec{F_1}+\\vec{F_2}+\\vec{F_3}+\\vec{F_4}=\\vec{0} \\Leftrightarrow \\vec{F_1}-%s \\vec{F_1}+\\vec{F_3}+\\vec{F_4}=\\vec{0} \\Leftrightarrow \\vec{F_3}+\\vec{F_4}=%s \\vec{F_1}$. \\\\ \n'
                        'Đặt $\\vec{F_3}=\\vec{OC}, \\vec{F_4}=\\vec{OD}, \\vec{F_3}+\\vec{F_4}=\\vec{OA}$. \\\\ \n'
                        'Theo giả thiết $OC=OD=%s$ N, $\\widehat{AOC}=\\widehat{AOD}=%s^\\circ$ nên $OCAD$ là hình thoi. \\\\ \n'
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $OA^2=OC^2+AC^2-2 OC \\cdot OA \\cdot \\cos \\widehat{ACO}$. \\\\ \n'
                        '\\hspace*{1.9cm} $=%s^2+%s^2-2 \\cdot %s \\cdot %s \\cdot \\cos {%s^\\circ}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Suy ra $\\left| \\vec{F_1} \\right|=%s OA=%s$. \\\\ \n'
                        'Vậy độ lớn của lực $\\vec{F_2}$ là $\\left| \\vec{F_2} \\right|=%s \\approx %s$.'

                        %(latex(a),
                            latex(a),latex(a-1),
                            latex(n),latex(goc),
                            latex(n),latex(n),latex(n),latex(n),latex(180-2*goc),latex(oa2),
                            latex(Rational(1,a-1)),latex(f1),
                            latex(f2),latex(kq)
                            ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')
            return content

