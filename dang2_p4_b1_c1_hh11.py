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


def bt_dang2_p4_b1_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(2,50)

                h1=a*sqrt(19)/15
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$ có các cạnh bằng nhau và bằng $%s$$zz$ Gọi $E$ là trung điểm $AB$, $F$ là điểm thuộc cạnh $BC$ sao cho $BF = 2FC$, $G$ là điểm thuộc cạnh $CD$ sao cho $CG = 2GD$$zz$ Gọi $N$ là giao điểm của $AD$ với mặt phẳng $(EFG)$$zz$ Tính độ dài đoạn giao tuyến $NG$ của mặt phẳng $(EFG)$ với mặt phẳng $(ACD)$$zz$ \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (                    
                        '\\begin{center} \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                            '\\clip(-5$zz$642634445907589,-3) rectangle (14$zz$076306342957361,4); \n'
                            '\\draw [line width=1$zz$pt,dash pattern=on 3pt off 3pt] (0$zz$,0$zz$)-- (3$zz$9638405731255526,0$zz$); \n'
                            '\\draw [line width=1$zz$pt] (0$zz$,0$zz$)-- (0$zz$9638405731255533,-2$zz$0120531422914825); \n'
                            '\\draw [line width=1$zz$pt] (0$zz$9638405731255533,-2$zz$0120531422914825)-- (1$zz$9638405731255533,2$zz$9879468577085175); \n'
                            '\\draw [line width=1$zz$pt] (1$zz$9638405731255533,2$zz$9879468577085175)-- (0$zz$,0$zz$); \n'
                            '\\draw [line width=1$zz$pt,dash pattern=on 3pt off 3pt] (3$zz$9638405731255526,0$zz$)-- (5$zz$963840573125553,-0$zz$012053142291482244); \n'
                            '\\draw [line width=1$zz$pt] (5$zz$963840573125553,-0$zz$012053142291482244)-- (0$zz$9085921800957586,1$zz$3824060805174574); \n'
                            '\\draw [line width=1$zz$pt] (3$zz$5208379664777825,0$zz$6618341232449442)-- (2$zz$9198051521687414,-0$zz$7002182497999206); \n'
                            '\\draw [line width=1$zz$pt] (0$zz$9085921800957586,1$zz$3824060805174574)-- (0$zz$5879557084125269,-1$zz$2273794687884942); \n'
                            '\\draw [line width=1$zz$pt] (1$zz$9638405731255533,2$zz$9879468577085175)-- (3$zz$5208379664777825,0$zz$6618341232449442); \n'
                            '\\draw [line width=1$zz$pt,dash pattern=on 3pt off 3pt] (3$zz$5208379664777825,0$zz$6618341232449442)-- (3$zz$9638405731255526,0$zz$); \n'
                            '\\draw [line width=1$zz$pt,dash pattern=on 3pt off 3pt] (0$zz$5879557084125269,-1$zz$2273794687884942)-- (2$zz$9198051521687414,-0$zz$7002182497999206); \n'
                            '\\draw [line width=1$zz$pt] (2$zz$9198051521687414,-0$zz$7002182497999206)-- (5$zz$963840573125553,-0$zz$012053142291482244); \n'
                            '\\draw [line width=1$zz$pt] (0$zz$9638405731255533,-2$zz$0120531422914825)-- (2$zz$9198051521687414,-0$zz$7002182497999206); \n'
                            '\\draw [line width=1$zz$pt,dash pattern=on 3pt off 3pt] (2$zz$9198051521687414,-0$zz$7002182497999206)-- (3$zz$9638405731255526,0$zz$); \n'
                            '\\draw (1$zz$6,3$zz$56) node[anchor=north west] {A}; \n'
                            '\\draw (-0$zz$6,0$zz$3) node[anchor=north west] {B}; \n'
                            '\\draw (0$zz$6,-2) node[anchor=north west] {C}; \n'
                            '\\draw (0$zz$4683086958739081,1$zz$9) node[anchor=north west] {E}; \n'
                            '\\draw (0$zz$15492699629536977,-1$zz$3291548022737703) node[anchor=north west] {F}; \n'
                            '\\draw (2$zz$8,-0$zz$6) node[anchor=north west] {G}; \n'
                            '\\draw (3$zz$3972222727040933,1$zz$1778987943545323) node[anchor=north west] {N}; \n'
                            '\\draw (3$zz$91550739123783,0$zz$5) node[anchor=north west] {D}; \n'
                            '\\draw (5$zz$9,0$zz$2) node[anchor=north west] {I}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center} \n'

                        'Trong mặt phẳng $(BCD)$, gọi $I = FG \\cap BD$$zz$ Trong mặt phẳng $(ADB)$, gọi $N = IE \\cap AD$$zz$ \\\\ \n'
                        'Khi đó, $NG = (EFG) \\cap (ACD)$$zz$ \\\\ \n'
                        'Áp dụng định lý Menelaus cho tam giác $BCD$ với ba điểm $I, G, F$ thẳng hàng ta có \\\\ \n'
                        '\\hspace*{1cm} $ \\frac{ID}{IB} \\cdot \\frac{FB}{FC} \\cdot \\frac{GC}{GD} = 1 \\Rightarrow \\frac{ID}{IB} = \\frac{1}{4}$$zz$ \\\\ \n'
                        'Áp dụng định lý Menelaus cho tam giác $ABD$ với ba điểm $I, N, E$ thẳng hàng ta có \\\\ \n'
                        '\\hspace*{1cm} $ \\frac{ND}{NA} \\cdot \\frac{EA}{EB} \\cdot \\frac{IB}{ID} = 1 \\Rightarrow \\frac{ND}{NA} = \\frac{1}{4} \\Rightarrow ND = \\frac{%s}{5} $$zz$ \\\\ \n'
                        'Áp dụng định lý Cosin vào tam giác $NDG$ ta có \\\\ \n'
                        '\\hspace*{1cm} $ NG^2 = ND^2 + DG^2 - 2 \\cdot ND \\cdot DG \\cdot \\cos 60^\\circ$ \\\\ \n'
                        '\\hspace*{2cm} $= \\frac{%s^2}{25} + \\frac{%s^2}{9} - \\frac{2\\cdot %s^2}{15} \\cdot \\frac{1}{2} = \\frac{19 \\cdot %s^2}{225} \\Rightarrow NG = \\frac{\\sqrt{19}\\cdot %s}{15}$$zz$'
                    %(latex(a),latex(a),latex(a),latex(a),latex(a),latex(a)
                            ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content   

