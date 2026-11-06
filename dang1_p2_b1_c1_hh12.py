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


def bt_dang1_p2_b1_c1_hh12(self):
            # Khai báo biến
            a = randint(1,9)
            b = randint(1,9)
            c = randint(1,9)

            # Nội dung câu hỏi
            noidungcauhoi = '''Cho hình hộp chữ nhật $ABCD.A\'B\'C\'D\'$ có $AB=%s, AD=%s, AA\'=%s$. \n''' %(latex(a),latex(b),latex(c))

            # Các đáp án
            da_1_d = '\\True Hai vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{D\'C\'}$ bằng nhau'
            da_1_s = 'Hai vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{D\'C\'}$ đối nhau'
            list_da_1=[da_1_d,da_1_s]
            da_1=random.choice(list_da_1)

            da_2_d = '\\True $\\left| \\overrightarrow{BC\'} \\right|=\\left| \\overrightarrow{A\'D} \\right|$'
            da_2_s = '$\\left| \\overrightarrow{BC\'} \\right| \\ne \\left| \\overrightarrow{A\'D} \\right|$'
            list_da_2=[da_2_d,da_2_s]
            da_2=random.choice(list_da_2)

            da_3_d = '\\True Số các vectơ khác $\\vec{0}$ được tạo ra từ các đỉnh của hình hộp chữ nhật là $56$'
            da_3_s = 'Số các vectơ khác $\\vec{0}$ được tạo ra từ các đỉnh của hình hộp chữ nhật là $66$'
            list_da_3=[da_3_d,da_3_s]
            da_3=random.choice(list_da_3)

            da_4_d = '\\True $\\left| \\overrightarrow{CD} \\right|=%s$'%(latex(a))
            da_4_s = '$\\left| \\overrightarrow{CD} \\right|=%s$'%(latex(a+1))
            list_da_4=[da_4_d,da_4_s]
            da_4=random.choice(list_da_4)

            da_5_d = '\\True $\\left| \\overrightarrow{AB} +\\overrightarrow{AD}\\right|=%s$'%(latex(sqrt(a**2+b**2)))
            da_5_s = '$\\left| \\overrightarrow{AB} +\\overrightarrow{AC}\\right|=%s$'%(latex(sqrt(a**2+b**2+1)))
            list_da_5=[da_5_d,da_5_s]
            da_5=random.choice(list_da_5)

            da_6_d = '\\True $\\left| \\overrightarrow{AB} +\\overrightarrow{AD}+\\overrightarrow{AA\'}\\right|=%s$'%(latex(sqrt(a**2+b**2+c**2)))
            da_6_s = '$\\left| \\overrightarrow{AB} +\\overrightarrow{AD}+\\overrightarrow{AA\'}\\right|=%s$'%(latex(sqrt(a**2+b**2+c**2+1)))
            list_da_6=[da_6_d,da_6_s]
            da_6=random.choice(list_da_6)

            da_7_d = '\\True $\\overrightarrow{BD}=\\overrightarrow{BD\'}-\\overrightarrow{DD\'}$'
            da_7_s = '$\\overrightarrow{BD}=\\overrightarrow{BD\'}+\\overrightarrow{DD\'}$'
            list_da_7=[da_7_d,da_7_s]
            da_7=random.choice(list_da_7)

            da_8_d = '\\True $\\overrightarrow{AB} \\cdot \\overrightarrow{DD\'}=0$'
            da_8_s = '$\\overrightarrow{AB} \\cdot \\overrightarrow{DD\'}=1$'
            list_da_8=[da_8_d,da_8_s]
            da_8=random.choice(list_da_8)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_1, da_2, da_3, da_4, da_5, da_6, da_7, da_8]

            # Nội dung lời giải
            loigiai_1 = ('Hai vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{D\'C\'}$ cùng hướng và cùng độ dài nên bằng nhau.'

                        )
            loigiai_2 = ('Hai cạnh $BC\'$ và $A\'D$ bằng nhau nên $\\left| \\overrightarrow{BC\'} \\right|=\\left| \\overrightarrow{A\'D} \\right|$.'

                        )
            loigiai_3 = ('Số các vectơ khác $\\vec{0}$ được tạo ra từ các đỉnh của hình hộp chữ nhật là $A^2_8=56$.'

                        )
            loigiai_4 = ('$\\left| \\overrightarrow{CD} \\right|=CD=AB=%s$.'
                        %(latex(a))
                        )
            loigiai_5 = ('Ta có $AC=\\sqrt{AB^2+BC^2}=\\sqrt{%s^2+%s^2}=%s$.\\\\ \n'
                        '$\\left| \\overrightarrow{AB} +\\overrightarrow{AD}\\right|=\\left| \\overrightarrow{AC} \\right|=%s$.'
                        %(latex(a),latex(b),latex(sqrt(a**2+b**2)),
                        latex(sqrt(a**2+b**2)),
                        ))
            loigiai_6 = ('Ta có $AC=\\sqrt{AB^2+BC^2}=\\sqrt{%s^2+%s^2}=%s$.\\\\ \n'
                        '$AC\'=\\sqrt{AC^2+AA\'^2}=\\sqrt{(%s)^2+%s^2}=%s$.\\\\ \n'
                        '$\\left| \\overrightarrow{AB} +\\overrightarrow{AD}\\right|=\\left| \\overrightarrow{AC} \\right|=%s$.'
                        %(latex(a),latex(b),latex(sqrt(a**2+b**2)),
                        latex(sqrt(a**2+b**2)),latex(c),latex(sqrt(a**2+b**2+c**2)),
                        latex(sqrt(a**2+b**2+c**2)),
                        ))
            loigiai_7 = ('Theo quy tắc ba điểm ta có\\\\ \n'
                        '$\\overrightarrow{BD}+\\overrightarrow{DD\'}=\\overrightarrow{BD\'} \\Leftrightarrow \\overrightarrow{BD}=\\overrightarrow{BD\'}-\\overrightarrow{DD\'}$.'
                        )

            loigiai_8 = ('Vì $AB$ và $DD\'$ vuông góc với nhau nên $\\overrightarrow{AB} \\cdot \\overrightarrow{DD\'}=0$.'

                        )

            # Đưa các lời giải vào danh sách lời giải
            list_2 = [loigiai_1, loigiai_2, loigiai_3, loigiai_4, loigiai_5, loigiai_6, loigiai_7, loigiai_8]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined = list(zip(list_1, list_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers, shuffled_solutions = zip(*combined)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{center} \n'
                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                '\\clip(-0.8492177589851994,-1.1656236786469323) rectangle (7.319915433403805,6.2085835095137405); \n'
                '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                '\\draw [line width=1.pt] (4.,0.)-- (6.,2.); \n'
                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,2.)-- (2.,2.); \n'
                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,0.); \n'
                '\\draw [line width=1.pt] (0.,0.)-- (0.,3.); \n'
                '\\draw [line width=1.pt] (0.,3.)-- (2.,5.); \n'
                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,5.)-- (2.,2.); \n'
                '\\draw [line width=1.pt] (2.,5.)-- (6.,5.); \n'
                '\\draw [line width=1.pt] (6.,5.)-- (6.,2.); \n'
                '\\draw [line width=1.pt] (6.,5.)-- (4.,3.); \n'
                '\\draw [line width=1.pt] (4.,3.)-- (4.,0.); \n'
                '\\draw [line width=1.pt] (4.,3.)-- (0.,3.); \n'
                '\\draw (-0.409471458773783,0.1874418604651178) node[anchor=north west] {$A$}; \n'
                '\\draw (3.8695983086680767,0.1197885835095153) node[anchor=north west] {$B$}; \n'
                '\\draw (6.135983086680762,2.3692600422832983) node[anchor=north west] {$C$}; \n'
                '\\draw (1.4002536997885846,2.504566596194503) node[anchor=north west] {$D$}; \n'
                '\\draw (-0.6124312896405906,3.553192389006342) node[anchor=north west] {$A\'$}; \n'
                '\\draw (4.106384778012686,3.2994926004228327) node[anchor=north west] {$B\'$}; \n'
                '\\draw (6.119069767441861,5.718097251585622) node[anchor=north west] {$C\'$}; \n'
                '\\draw (1.4509936575052864,5.7688372093023235) node[anchor=north west] {$D\'$}; \n'
                '\\end{tikzpicture} \n'
                '\\end{center} \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

