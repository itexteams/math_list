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


def bt_dang1_p3_b4_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(1,20)
                s=Rational(4,9)*(a**2)*sqrt(3)/4
                h1=s  
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$ có tất cả các cạnh đều bằng $%s$ và $G$ là trọng tâm của tam giác $ABC$$zz$ Cắt tứ diện bởi mặt phẳng $(P)$ qua $G$ và song song với mặt phẳng $(BCD)$$zz$ Diện tích thiết diện thu được bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)$zz$  \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

                        '\\begin{center} \n'
                            '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1$zz$0cm,y=1$zz$0cm] \n'
                                '\\clip(-1$zz$4153486136146074,-2$zz$7336445502608933) rectangle (6$zz$309219838892137,4$zz$861198325180836); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (0$zz$,0$zz$)-- (5$zz$,0$zz$); \n'
                                '\\draw (5$zz$,0$zz$)-- (3$zz$,-2$zz$); \n'
                                '\\draw (3$zz$,-2$zz$)-- (0$zz$,0$zz$); \n'
                                '\\draw (0$zz$,0$zz$)-- (3$zz$,4$zz$); \n'
                                '\\draw (3$zz$,4$zz$)-- (3$zz$,-2$zz$); \n'
                                '\\draw (3$zz$,4$zz$)-- (5$zz$,0$zz$); \n'
                                '\\draw (3$zz$,4$zz$)-- (1$zz$4867145481136244,-0$zz$9911430320757495); \n'
                                '\\draw (1$zz$0274847477154552,1$zz$369979663620607)-- (3$zz$,0$zz$28006286403423974); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (1$zz$0274847477154552,1$zz$369979663620607)-- (4$zz$3305106734616565,1$zz$338978653076686); \n'
                                '\\draw (4$zz$3305106734616565,1$zz$338978653076686)-- (3$zz$,0$zz$28006286403423974); \n'
                                '\\draw (2$zz$7,4$zz$5) node[anchor=north west] {A}; \n'
                                '\\draw (-0$zz$5,0$zz$2) node[anchor=north west] {B}; \n'
                                '\\draw (2$zz$7,-2) node[anchor=north west] {C}; \n'
                                '\\draw (4$zz$94,0$zz$27) node[anchor=north west] {D}; \n'
                                '\\draw (0$zz$9,-1) node[anchor=north west] {M}; \n'
                                '\\draw (1$zz$4,1) node[anchor=north west] {G}; \n'
                                '\\draw (0$zz$5,1$zz$8) node[anchor=north west] {K}; \n'
                                '\\draw (3$zz$0778736465458043,0$zz$5) node[anchor=north west] {H}; \n'
                                '\\draw (4$zz$32,1$zz$7) node[anchor=north west] {I}; \n'
                            '\\end{tikzpicture} \n'
                        '\\end{center} \n'

                        'Trong mặt phẳng $(ABC)$ kẻ đường thẳng qua $G$ và song song với $BC$ cắt $AC, AB$ lần lượt tại $H, K$$zz$ \\\\ \n'
                        'Trong mặt phẳng $(ACD)$ kẻ đường thẳng qua $H$ và song song với $CD$ cắt $AD$ tại $I$$zz$ \\\\ \n'
                        'Thiết diện cần tìm là tam giác $HKI$$zz$ \\\\ \n'
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\Delta HKI \\sim \\Delta BCD \\text{ theo tỉ số đồng dạng } k = \\frac{2}{3}$$zz$ \\\\ \n'
                        'Do đó \\\\ \n'
                        '\\hspace*{1cm} $S_{HKI} = k^2 \\cdot S_{BCD} = \\frac{4}{9} \\cdot \\frac{%s\\sqrt{3}}{4} =%s \\approx %s$$zz$'

                        %(latex(a**2),latex(s),latex(kq)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content

