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


def bt_dang3_p3_b2_c1_hh11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6']
            dang=random.choice(lisdang)
            if dang=='6':
                a=2
                h1=3 
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Các điểm $P, Q$ lần lượt là trung điểm của $AB$ và $CD$; điểm $R$ nằm trên cạnh $BC$ sao cho $BR = %sRC$. Gọi $S$ là giao điểm của $(PQR)$ và cạnh $AD$. Tỉ số $\\dfrac{SA}{SD}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục). \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

                        '\\begin{center}   \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n' 
                            '\\clip(-4.3,-3) rectangle (13.02,4); \n'
                            '\\draw (0.,0.)-- (2.,-2.); \n'
                            '\\draw (0.,0.)-- (2.,3.); \n'
                            '\\draw (2.,3.)-- (2.,-2.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (1.,1.5)-- (3.5,-1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (10.,0.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (5.658150289017341,-0.6679768786127168); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (5.592432432432432,0.7345945945945948); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (0.,0.)-- (5.,0.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (1.3333333333333333,-1.3333333333333333)-- (3.5,-1.); \n'
                            '\\draw (3.5,-1.)-- (10.,0.); \n'
                            '\\draw (2.,3.)-- (4.,1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (4.,1.)-- (5.,0.); \n'
                            '\\draw (2.,-2.)-- (3.5,-1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (3.5,-1.)-- (5.,0.); \n'
                            '\\draw (10.,0.)-- (4.,1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (4.,1.)-- (1.,1.5); \n'
                            '\\draw (1.8,3.52) node[anchor=north west] {A}; \n'
                            '\\draw (-0.6,0.2) node[anchor=north west] {B}; \n'
                            '\\draw (1.6,-2) node[anchor=north west] {C}; \n'
                            '\\draw (4.65,0) node[anchor=north west] {D}; \n'
                            '\\draw (5.6,-0.76) node[anchor=north west] {E}; \n'
                            '\\draw (5.46,1.3) node[anchor=north west] {F}; \n'
                            '\\draw (10.2,0.3) node[anchor=north west] {I}; \n'
                            '\\draw (0.4,2) node[anchor=north west] {P}; \n'
                            '\\draw (3.4,-0.9) node[anchor=north west] {Q}; \n'
                            '\\draw (0.8,-1.2) node[anchor=north west] {R}; \n'
                            '\\draw (4.,1.48) node[anchor=north west] {S}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'

                            'Trong mặt phẳng $(BCD)$, gọi $I = RQ \\cap BD$. \\\\ \n'
                        'Trong mặt phẳng $(ABD)$, gọi $S = PI \\cap AD \\Rightarrow S = AD \\cap (PQR)$. \\\\ \n'
                        'Trong mặt phẳng $(BCD)$, dựng $DE // BC \\Rightarrow DE$ là đường trung bình của $\\triangle IBR$. \\\\ \n'
                        'Suy ra $D$ là trung điểm của $BI$. \\\\ \n'
                        'Trong mặt phẳng $(ABD)$, dựng $DF // AB \\Rightarrow \\dfrac{DF}{BP} = \\dfrac{1}{2} \\Rightarrow \\dfrac{DF}{PA} = \\dfrac{1}{2} \\Rightarrow \\dfrac{SA}{SD} = 2 \\Rightarrow \\dfrac{AD}{SD} = 3$.'
                        %(
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='5':
                a=2
                h1=3/2  
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Các điểm $P, Q$ lần lượt là trung điểm của $AB$ và $CD$; điểm $R$ nằm trên cạnh $BC$ sao cho $BR = %sRC$. Gọi $S$ là giao điểm của $(PQR)$ và cạnh $AD$. Tỉ số $\\dfrac{SA}{SD}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục). \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

                        '\\begin{center}   \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n' 
                            '\\clip(-4.3,-3) rectangle (13.02,4); \n'
                            '\\draw (0.,0.)-- (2.,-2.); \n'
                            '\\draw (0.,0.)-- (2.,3.); \n'
                            '\\draw (2.,3.)-- (2.,-2.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (1.,1.5)-- (3.5,-1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (10.,0.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (5.658150289017341,-0.6679768786127168); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (5.592432432432432,0.7345945945945948); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (0.,0.)-- (5.,0.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (1.3333333333333333,-1.3333333333333333)-- (3.5,-1.); \n'
                            '\\draw (3.5,-1.)-- (10.,0.); \n'
                            '\\draw (2.,3.)-- (4.,1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (4.,1.)-- (5.,0.); \n'
                            '\\draw (2.,-2.)-- (3.5,-1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (3.5,-1.)-- (5.,0.); \n'
                            '\\draw (10.,0.)-- (4.,1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (4.,1.)-- (1.,1.5); \n'
                            '\\draw (1.8,3.52) node[anchor=north west] {A}; \n'
                            '\\draw (-0.6,0.2) node[anchor=north west] {B}; \n'
                            '\\draw (1.6,-2) node[anchor=north west] {C}; \n'
                            '\\draw (4.65,0) node[anchor=north west] {D}; \n'
                            '\\draw (5.6,-0.76) node[anchor=north west] {E}; \n'
                            '\\draw (5.46,1.3) node[anchor=north west] {F}; \n'
                            '\\draw (10.2,0.3) node[anchor=north west] {I}; \n'
                            '\\draw (0.4,2) node[anchor=north west] {P}; \n'
                            '\\draw (3.4,-0.9) node[anchor=north west] {Q}; \n'
                            '\\draw (0.8,-1.2) node[anchor=north west] {R}; \n'
                            '\\draw (4.,1.48) node[anchor=north west] {S}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'

                            'Trong mặt phẳng $(BCD)$, gọi $I = RQ \\cap BD$. \\\\ \n'
                        'Trong mặt phẳng $(ABD)$, gọi $S = PI \\cap AD \\Rightarrow S = AD \\cap (PQR)$. \\\\ \n'
                        'Trong mặt phẳng $(BCD)$, dựng $DE // BC \\Rightarrow DE$ là đường trung bình của $\\triangle IBR$. \\\\ \n'
                        'Suy ra $D$ là trung điểm của $BI$. \\\\ \n'
                        'Trong mặt phẳng $(ABD)$, dựng $DF // AB \\Rightarrow \\dfrac{DF}{BP} = \\dfrac{1}{2} \\Rightarrow \\dfrac{DF}{PA} = \\dfrac{1}{2} \\Rightarrow \\dfrac{SA}{SD} = 2 \\Rightarrow \\dfrac{AD}{SA} = \\dfrac{3}{2}$.'
                        %(
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='4':
                a=2
                h1=1/2    
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Các điểm $P, Q$ lần lượt là trung điểm của $AB$ và $CD$; điểm $R$ nằm trên cạnh $BC$ sao cho $BR = %sRC$. Gọi $S$ là giao điểm của $(PQR)$ và cạnh $AD$. Tỉ số $\\dfrac{SA}{SD}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục). \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

                        '\\begin{center}   \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n' 
                            '\\clip(-4.3,-3) rectangle (13.02,4); \n'
                            '\\draw (0.,0.)-- (2.,-2.); \n'
                            '\\draw (0.,0.)-- (2.,3.); \n'
                            '\\draw (2.,3.)-- (2.,-2.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (1.,1.5)-- (3.5,-1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (10.,0.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (5.658150289017341,-0.6679768786127168); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (5.592432432432432,0.7345945945945948); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (0.,0.)-- (5.,0.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (1.3333333333333333,-1.3333333333333333)-- (3.5,-1.); \n'
                            '\\draw (3.5,-1.)-- (10.,0.); \n'
                            '\\draw (2.,3.)-- (4.,1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (4.,1.)-- (5.,0.); \n'
                            '\\draw (2.,-2.)-- (3.5,-1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (3.5,-1.)-- (5.,0.); \n'
                            '\\draw (10.,0.)-- (4.,1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (4.,1.)-- (1.,1.5); \n'
                            '\\draw (1.8,3.52) node[anchor=north west] {A}; \n'
                            '\\draw (-0.6,0.2) node[anchor=north west] {B}; \n'
                            '\\draw (1.6,-2) node[anchor=north west] {C}; \n'
                            '\\draw (4.65,0) node[anchor=north west] {D}; \n'
                            '\\draw (5.6,-0.76) node[anchor=north west] {E}; \n'
                            '\\draw (5.46,1.3) node[anchor=north west] {F}; \n'
                            '\\draw (10.2,0.3) node[anchor=north west] {I}; \n'
                            '\\draw (0.4,2) node[anchor=north west] {P}; \n'
                            '\\draw (3.4,-0.9) node[anchor=north west] {Q}; \n'
                            '\\draw (0.8,-1.2) node[anchor=north west] {R}; \n'
                            '\\draw (4.,1.48) node[anchor=north west] {S}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'

                            'Trong mặt phẳng $(BCD)$, gọi $I = RQ \\cap BD$. \\\\ \n'
                        'Trong mặt phẳng $(ABD)$, gọi $S = PI \\cap AD \\Rightarrow S = AD \\cap (PQR)$. \\\\ \n'
                        'Trong mặt phẳng $(BCD)$, dựng $DE // BC \\Rightarrow DE$ là đường trung bình của $\\triangle IBR$. \\\\ \n'
                        'Suy ra $D$ là trung điểm của $BI$. \\\\ \n'
                        'Trong mặt phẳng $(ABD)$, dựng $DF // AB \\Rightarrow \\dfrac{DF}{BP} = \\dfrac{1}{2} \\Rightarrow \\dfrac{DF}{PA} = \\dfrac{1}{2} \\Rightarrow \\dfrac{SD}{SA} = \\dfrac{1}{2}$.'
                        %(
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(a))
            if dang=='3':
                a=2
                h1=1/3   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Các điểm $P, Q$ lần lượt là trung điểm của $AB$ và $CD$; điểm $R$ nằm trên cạnh $BC$ sao cho $BR = %sRC$. Gọi $S$ là giao điểm của $(PQR)$ và cạnh $AD$. Tỉ số $\\dfrac{SA}{SD}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục). \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

                        '\\begin{center}   \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n' 
                            '\\clip(-4.3,-3) rectangle (13.02,4); \n'
                            '\\draw (0.,0.)-- (2.,-2.); \n'
                            '\\draw (0.,0.)-- (2.,3.); \n'
                            '\\draw (2.,3.)-- (2.,-2.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (1.,1.5)-- (3.5,-1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (10.,0.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (5.658150289017341,-0.6679768786127168); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (5.592432432432432,0.7345945945945948); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (0.,0.)-- (5.,0.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (1.3333333333333333,-1.3333333333333333)-- (3.5,-1.); \n'
                            '\\draw (3.5,-1.)-- (10.,0.); \n'
                            '\\draw (2.,3.)-- (4.,1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (4.,1.)-- (5.,0.); \n'
                            '\\draw (2.,-2.)-- (3.5,-1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (3.5,-1.)-- (5.,0.); \n'
                            '\\draw (10.,0.)-- (4.,1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (4.,1.)-- (1.,1.5); \n'
                            '\\draw (1.8,3.52) node[anchor=north west] {A}; \n'
                            '\\draw (-0.6,0.2) node[anchor=north west] {B}; \n'
                            '\\draw (1.6,-2) node[anchor=north west] {C}; \n'
                            '\\draw (4.65,0) node[anchor=north west] {D}; \n'
                            '\\draw (5.6,-0.76) node[anchor=north west] {E}; \n'
                            '\\draw (5.46,1.3) node[anchor=north west] {F}; \n'
                            '\\draw (10.2,0.3) node[anchor=north west] {I}; \n'
                            '\\draw (0.4,2) node[anchor=north west] {P}; \n'
                            '\\draw (3.4,-0.9) node[anchor=north west] {Q}; \n'
                            '\\draw (0.8,-1.2) node[anchor=north west] {R}; \n'
                            '\\draw (4.,1.48) node[anchor=north west] {S}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'

                            'Trong mặt phẳng $(BCD)$, gọi $I = RQ \\cap BD$. \\\\ \n'
                        'Trong mặt phẳng $(ABD)$, gọi $S = PI \\cap AD \\Rightarrow S = AD \\cap (PQR)$. \\\\ \n'
                        'Trong mặt phẳng $(BCD)$, dựng $DE // BC \\Rightarrow DE$ là đường trung bình của $\\triangle IBR$. \\\\ \n'
                        'Suy ra $D$ là trung điểm của $BI$. \\\\ \n'
                        'Trong mặt phẳng $(ABD)$, dựng $DF // AB \\Rightarrow \\dfrac{DF}{BP} = \\dfrac{1}{2} \\Rightarrow \\dfrac{DF}{PA} = \\dfrac{1}{2} \\Rightarrow \\dfrac{SA}{SD} = 2 \\Rightarrow \\dfrac{SD}{AD} = \\dfrac{1}{3}$.'
                        %(
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='2':
                a=2
                h1=2/3   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Các điểm $P, Q$ lần lượt là trung điểm của $AB$ và $CD$; điểm $R$ nằm trên cạnh $BC$ sao cho $BR = %sRC$. Gọi $S$ là giao điểm của $(PQR)$ và cạnh $AD$. Tỉ số $\\dfrac{SA}{SD}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục). \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

                        '\\begin{center}   \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n' 
                            '\\clip(-4.3,-3) rectangle (13.02,4); \n'
                            '\\draw (0.,0.)-- (2.,-2.); \n'
                            '\\draw (0.,0.)-- (2.,3.); \n'
                            '\\draw (2.,3.)-- (2.,-2.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (1.,1.5)-- (3.5,-1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (10.,0.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (5.658150289017341,-0.6679768786127168); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (5.592432432432432,0.7345945945945948); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (0.,0.)-- (5.,0.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (1.3333333333333333,-1.3333333333333333)-- (3.5,-1.); \n'
                            '\\draw (3.5,-1.)-- (10.,0.); \n'
                            '\\draw (2.,3.)-- (4.,1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (4.,1.)-- (5.,0.); \n'
                            '\\draw (2.,-2.)-- (3.5,-1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (3.5,-1.)-- (5.,0.); \n'
                            '\\draw (10.,0.)-- (4.,1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (4.,1.)-- (1.,1.5); \n'
                            '\\draw (1.8,3.52) node[anchor=north west] {A}; \n'
                            '\\draw (-0.6,0.2) node[anchor=north west] {B}; \n'
                            '\\draw (1.6,-2) node[anchor=north west] {C}; \n'
                            '\\draw (4.65,0) node[anchor=north west] {D}; \n'
                            '\\draw (5.6,-0.76) node[anchor=north west] {E}; \n'
                            '\\draw (5.46,1.3) node[anchor=north west] {F}; \n'
                            '\\draw (10.2,0.3) node[anchor=north west] {I}; \n'
                            '\\draw (0.4,2) node[anchor=north west] {P}; \n'
                            '\\draw (3.4,-0.9) node[anchor=north west] {Q}; \n'
                            '\\draw (0.8,-1.2) node[anchor=north west] {R}; \n'
                            '\\draw (4.,1.48) node[anchor=north west] {S}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'

                            'Trong mặt phẳng $(BCD)$, gọi $I = RQ \\cap BD$. \\\\ \n'
                        'Trong mặt phẳng $(ABD)$, gọi $S = PI \\cap AD \\Rightarrow S = AD \\cap (PQR)$. \\\\ \n'
                        'Trong mặt phẳng $(BCD)$, dựng $DE // BC \\Rightarrow DE$ là đường trung bình của $\\triangle IBR$. \\\\ \n'
                        'Suy ra $D$ là trung điểm của $BI$. \\\\ \n'
                        'Trong mặt phẳng $(ABD)$, dựng $DF // AB \\Rightarrow \\dfrac{DF}{BP} = \\dfrac{1}{2} \\Rightarrow \\dfrac{DF}{PA} = \\dfrac{1}{2} \\Rightarrow \\dfrac{SA}{SD} = 2 \\Rightarrow \\dfrac{SA}{AD} = \\dfrac{2}{3}$.'
                        %(
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='1':
                a=2
                h1=a    
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Các điểm $P, Q$ lần lượt là trung điểm của $AB$ và $CD$; điểm $R$ nằm trên cạnh $BC$ sao cho $BR = %sRC$. Gọi $S$ là giao điểm của $(PQR)$ và cạnh $AD$. Tỉ số $\\dfrac{SA}{SD}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục). \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

                        '\\begin{center}   \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n' 
                            '\\clip(-4.3,-3) rectangle (13.02,4); \n'
                            '\\draw (0.,0.)-- (2.,-2.); \n'
                            '\\draw (0.,0.)-- (2.,3.); \n'
                            '\\draw (2.,3.)-- (2.,-2.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (1.,1.5)-- (3.5,-1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (10.,0.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (5.658150289017341,-0.6679768786127168); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (5.,0.)-- (5.592432432432432,0.7345945945945948); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (0.,0.)-- (5.,0.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (1.3333333333333333,-1.3333333333333333)-- (3.5,-1.); \n'
                            '\\draw (3.5,-1.)-- (10.,0.); \n'
                            '\\draw (2.,3.)-- (4.,1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (4.,1.)-- (5.,0.); \n'
                            '\\draw (2.,-2.)-- (3.5,-1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (3.5,-1.)-- (5.,0.); \n'
                            '\\draw (10.,0.)-- (4.,1.); \n'
                            '\\draw [dash pattern=on 5pt off 5pt] (4.,1.)-- (1.,1.5); \n'
                            '\\draw (1.8,3.52) node[anchor=north west] {A}; \n'
                            '\\draw (-0.6,0.2) node[anchor=north west] {B}; \n'
                            '\\draw (1.6,-2) node[anchor=north west] {C}; \n'
                            '\\draw (4.65,0) node[anchor=north west] {D}; \n'
                            '\\draw (5.6,-0.76) node[anchor=north west] {E}; \n'
                            '\\draw (5.46,1.3) node[anchor=north west] {F}; \n'
                            '\\draw (10.2,0.3) node[anchor=north west] {I}; \n'
                            '\\draw (0.4,2) node[anchor=north west] {P}; \n'
                            '\\draw (3.4,-0.9) node[anchor=north west] {Q}; \n'
                            '\\draw (0.8,-1.2) node[anchor=north west] {R}; \n'
                            '\\draw (4.,1.48) node[anchor=north west] {S}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'

                            'Trong mặt phẳng $(BCD)$, gọi $I = RQ \\cap BD$. \\\\ \n'
                        'Trong mặt phẳng $(ABD)$, gọi $S = PI \\cap AD \\Rightarrow S = AD \\cap (PQR)$. \\\\ \n'
                        'Trong mặt phẳng $(BCD)$, dựng $DE // BC \\Rightarrow DE$ là đường trung bình của $\\triangle IBR$. \\\\ \n'
                        'Suy ra $D$ là trung điểm của $BI$. \\\\ \n'
                        'Trong mặt phẳng $(ABD)$, dựng $DF // AB \\Rightarrow \\dfrac{DF}{BP} = \\dfrac{1}{2} \\Rightarrow \\dfrac{DF}{PA} = \\dfrac{1}{2} \\Rightarrow \\dfrac{SA}{SD} = 2$.'
                        %(
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(a))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content           

