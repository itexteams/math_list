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


def bt_dang2_p3_b5_c2_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                n=randint(50,90)
                g=60
                i=randint(25,50)
                s=2*i
                f=n*s*cos(60*pi/180)
                h1=1    
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Một người dùng một lực $\\vec{F}$ có độ lớn $%s$ N làm một vật di chuyển một đoạn $%s$ m. Biết lực $\\vec{F}$ hợp với hướng dịch chuyển một góc $%s^\\circ$. '
                                'Công của lực $\\vec{F}$ bằng bao nhiêu?'
                                '}{'
                                '\\definecolor{ttzzqq}{rgb}{0.2,0.6,0.}  \n'
                                '\\definecolor{zzttqq}{rgb}{0.6,0.2,0.}  \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                        '\\clip(-0.36778595549584264,-1.3573396272660232) rectangle (5.415084332448732,2.369727668289045); \n'
                                        '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,pattern=north east lines,pattern color=zzttqq] (0.,0.) -- (5.,0.) -- (5.,-1.) -- (0.,-1.) -- cycle; \n'
                                        '\\fill[line width=1.pt,color=ttzzqq,fill=ttzzqq,fill opacity=0.10000000149011612] (1.5,0.5) -- (2.,0.5) -- (2.,0.) -- (1.5,0.) -- cycle; \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (0.,0.)-- (5.,0.); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (5.,0.)-- (5.,-1.); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (5.,-1.)-- (0.,-1.); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (0.,-1.)-- (0.,0.); \n'
                                        '\\draw [line width=1.pt,color=ttzzqq] (1.5,0.5)-- (2.,0.5); \n'
                                        '\\draw [line width=1.pt,color=ttzzqq] (2.,0.5)-- (2.,0.); \n'
                                        '\\draw [line width=1.pt,color=ttzzqq] (2.,0.)-- (1.5,0.); \n'
                                        '\\draw [line width=1.pt,color=ttzzqq] (1.5,0.)-- (1.5,0.5); \n'
                                        '\\draw [->,line width=1.pt] (1.7397818604430368,0.2325799531790953) -- (4.010039121822812,0.2547648775573993); \n'
                                        '\\draw [->,line width=1.pt] (1.7397818604430368,0.2325799531790953) -- (2.5,2.); \n'
                                        '\\draw (1,0.520983970097047) node[anchor=north west] {$O$}; \n'
                                        '\\draw (3.9804592226517403,0.528378944889815) node[anchor=north west] {$M$}; \n'
                                        '\\draw (1.8,2.5) node[anchor=north west] {$\\vec{F}$}; \n'
                                '\\end{tikzpicture}  \n'
                                '}'
                                %(latex(n),latex(s),latex(g)
                                ))

                # Nội dung lời giải
                loigiai = (

                            'Đặt $OM$ là đoạn đường mà vật di chuyển được với $O$ là điểm đặt vật ban đầu. \\\\ \n'
                        'Khi đó công sinh ra bởi lực $\\vec{F}$ là \\\\ \n'
                        '\\hspace*{1cm} $A=\\left| \\vec{F} \\right| \\cdot \\left| \\vec{OM} \\right| \\cdot \\cos \\left( \\vec{F}, \\vec{OM} \\right)=%s \\cdot %s \\cdot \\cos %s^\\circ =%s$ J.'

                        %(latex(n),latex(s),latex(g),latex(f)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(f))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

