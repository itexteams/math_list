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


def bt_dang1_p3_b5_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(1,20)
                b=randint(1,20)
                c=randint(1,20)
                while a+b<=c or b+c<=a or c+a<=b:
                    a=randint(1,20)
                    b=randint(1,20)
                    c=randint(1,20)

                p=Rational(a+b+c,2)
                s=sqrt(p*(p-a)*(p-b)*(p-c))
                ah=2*s/a
                h1=ah  
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình lăng trụ đứng $ABC.A\'B\'C\'$ có $AB=%s, BC=%s, CA=%s$. Khoảng cách giữa hai đường thẳng $AA\'$ và $BC$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần mười). \n'
                                %(latex(c),latex(a),latex(b)
                                ))

                # Nội dung lời giải
                loigiai = (
                            '\\begin{center} \n'
                            '\\scalebox{0.7}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                    '\\clip(-1.3211481679328139,-2.872430708454342) rectangle (5.694061403550179,6.06600864111144); \n'
                                    '\\draw [line width=1.pt] (0.,0.)-- (1.,-2.); \n'
                                    '\\draw [line width=1.pt] (1.,-2.)-- (4.,0.); \n'
                                    '\\draw [line width=1.pt] (0.,0.)-- (0.,5.); \n'
                                    '\\draw [line width=1.pt] (0.,5.)-- (1.,3.); \n'
                                    '\\draw [line width=1.pt] (1.,3.)-- (4.,5.); \n'
                                    '\\draw [line width=1.pt] (0.,5.)-- (4.,5.); \n'
                                    '\\draw [line width=1.pt] (4.,5.)-- (4.,0.); \n'
                                    '\\draw [line width=1.pt] (1.,3.)-- (1.,-2.); \n'
                                    '\\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (0.,0.)-- (4.,0.); \n'
                                    '\\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (0.,0.)-- (2.1282885569542533,-1.2478076286971644); \n'
                                    '\\draw [line width=1.pt] (1.9104028848234922,-1.1200620732459556)-- (1.6461206325377993,-1.2788974637571635); \n'
                                    '\\draw [line width=1.pt] (1.6461206325377993,-1.2788974637571635)-- (1.941131992208366,-1.3725786718610893); \n'
                                    '\\draw (-0.6983880493155247,0.5710664180177216) node[anchor=north west] {$A$}; \n'
                                    '\\draw (0.5104992397650955,-2) node[anchor=north west] {$B$}; \n'
                                    '\\draw (4.192110529237893,0.4611675735558472) node[anchor=north west] {$C$}; \n'
                                    '\\draw (-0.771653945623441,5.4) node[anchor=north west] {$A\'$}; \n'
                                    '\\draw (0.2540686026873882,3.2) node[anchor=north west] {$B\'$}; \n'
                                    '\\draw (4.063895210699039,5.4) node[anchor=north west] {$C\'$}; \n'
                                    '\\draw (2.1040324844622766,-1.1506821452183102) node[anchor=north west] {$H$}; \n'
                                '\\end{tikzpicture} } \n'
                            '\\end{center} \n'
                            'Dựng $AH$ là đường cao hạ từ đỉnh $A$ của tam giác $ABC$, khi đó $AH$ là đường vuông góc chung của $AA\'$ và $BC$. \\\\ \n'
                            'Ta có $d(A,(BCC\'B\'))=AH$. \\\\ \n'
                            'Nửa chu vi của tam giác $ABC$ là $p=\\dfrac{AB+BC+CA}{2}=\\dfrac{%s+%s+%s}{2}=%s$. \\\\ \n'
                            'Diện tích tam giác $ABC$ là \\\\ \n'
                            '\\hspace*{1cm} $S=\\sqrt{p(p-AB)(p-BC)(p-CA)}=\\sqrt{%s(%s-%s)(%s-%s)(%s-%s)}=%s$. \\\\ \n'
                            'Mặt khác $S=\\dfrac{1}{2} AH \\cdot BC$ suy ra $AH=\\dfrac{2S}{BC}=\\dfrac{2 \\cdot %s}{%s}=%s$. \\\\ \n'
                            'Vậy khoảng cách giữa hai đường thẳng $AA\'$ và $BC$ là $%s \\approx %s$.'
                        %(latex(c),latex(a),latex(b),latex(p),
                            latex(p),latex(p),latex(c),latex(p),latex(a),latex(p),latex(b),latex(s),
                            latex(s),latex(a),latex(ah),
                            latex(ah),latex(kq)

                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

