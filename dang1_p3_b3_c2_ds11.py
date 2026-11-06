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


def bt_dang1_p3_b3_c2_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                u1=randint(5,20)
                h=randint(1,10)
                q=Rational(h,h+1)
                n=randint(9,16)
                un=u1*q**(n-1)
                sn=u1*(1-q**n)/(1-q)
                sn1=sn-u1
                h1=sn+sn1

                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Bạn An thả quả bóng cao su từ độ cao $%s$ m theo phương thẳng đứng. Mỗi khi chạm đất nó lại nảy lên theo phương thẳng đứng có độ cao bằng $%s$ độ cao trước đó. Tổng quãng đường bóng đi được bằng bao nhiêu sau khi bóng chạm đất $%s$ lần? (làm tròn kết quả đến hàng đơn vị).'
                                %(latex(u1),latex(q),latex(n)
                                ))

                # Nội dung lời giải
                loigiai = (
                            '\\begin{center} \n'
                            '\\definecolor{xdxdff}{rgb}{0.49019607843137253,0.49019607843137253,1.} \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n' 
                                '\\clip(-1.1057410954728755,-1.1320135348688098) rectangle (7.01239226842556,5.98880614796101); \n'
                                '\\draw [->,line width=1.pt] (0.,5.) -- (0.,0.); \n'
                                '\\draw [->,line width=1.pt,dash pattern=on 2pt off 2pt] (1.,0.) -- (1.,4.); \n'
                                '\\draw [->,line width=1.pt] (1.5,4.) -- (1.5,0.); \n'
                                '\\draw [->,line width=1.pt,dash pattern=on 2pt off 2pt] (2.5,0.) -- (2.5,3.); \n'
                                '\\draw [->,line width=1.pt] (3.,3.) -- (3.003191270529773,-0.06488789612540424); \n'
                                '\\draw [->,line width=1.pt,dash pattern=on 2pt off 2pt] (4.,0.) -- (4.,2.); \n'
                                '\\draw [->,line width=1.pt] (4.5,2.) -- (4.5,0.); \n'
                                '\\draw [->,line width=1.pt,dash pattern=on 2pt off 2pt] (5.5,0.) -- (5.5,1.); \n'
                                '\\draw [->,line width=1.pt] (6.,1.) -- (6.,0.); \n'
                                '\\draw (-0.6,-0.15) node[anchor=north west] {Lần 1}; \n'
                                '\\draw (0.7,-0.15) node[anchor=north west] {Lần 2}; \n'
                                '\\draw (2.2,-0.15) node[anchor=north west] {Lần 3}; \n'
                                '\\draw (3.6,-0.15) node[anchor=north west] {Lần 4}; \n'
                                '\\draw (5.1,-0.15) node[anchor=north west] {Lần 5}; \n'
                                '\\draw (0.26057864759111177,5.4) node[anchor=north west] {Bóng}; \n'
                                '\\begin{scriptsize} \n'
                                    '\\draw [fill=xdxdff] (0.,5.) circle (4.5pt); \n'
                                '\\end{scriptsize} \n'
                            '\\end{tikzpicture} \n'
                            '\\end{center} \n'

                            'Các quãng đường khi quả bóng di chuyển tạo thành một cấp số nhân với số hạng đầu $u_1=%s$ và công bội $q=%s$. \\\\ \n'
                        'Tổng quãng đường bóng di chuyển gồm tổng quãng đường bóng rơi xuống và tổng quãng đường bóng nảy lên. \\\\ \n'
                        'Tổng quãng đường bóng rơi xuống là \\\\ \n'
                        '\\hspace*{1cm} $S_1=u_1 \\dfrac{1-q^{%s}}{1-q}=%s\\dfrac{1- \\left(%s\\right)^{%s}}{1-%s}=%s$.\\\\ \n'
                        'Tổng quãng đường bóng nảy lên là \\\\ \n'
                        '\\hspace*{1cm} $S_2=u_1 \\dfrac{1-q^{%s}}{1-q}-u_1=%s\\dfrac{1- \\left(%s\\right)^{%s}}{1-%s}-%s=%s$.\\\\ \n'
                        'Vậy tổng quãng đường khi bóng rơi xuống là $S=S_1+S_2=%s+%s=%s \\approx %s$ m.'
                        %(latex(u1),latex(q),
                            latex(n),latex(u1),latex(q),latex(n),latex(q),latex(sn),
                            latex(n),latex(u1),latex(q),latex(n),latex(q),latex(u1),latex(sn1),
                            latex(sn),latex(sn1),latex(sn+sn1),latex(kq)                 
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

