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


def bt_dang6_p1_b3_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['${G}_{1}{G}_{2}//(ABD)$',
                    '${G}_{1}{G}_{2}//(ABC)$',
                    '$B{G}_{1},A{G}_{2}$ và $CD$ đồng qui',
                    '${G}_{1}{G}_{2}=\\dfrac{1}{3}AB$',
                    '$AB=3{G}_{1}{G}_{2}$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Gọi $M$ là trung điểm $CD$, vì ${G}_{2}$ là trọng tâm tam giác $ABD$ nên $\\dfrac{M{G}_{2}}{MA}=\\dfrac{1}{3}$, tương tự ${G}_{1}$ là trọng tâm tam giác $BCD$ nên $\\dfrac{M{G}_{1}}{MB}=\\dfrac{1}{3}$.\\\\ \n'
                    'Xét tam giác $MAB$ có $\\dfrac{M{G}_{2}}{MA}=\\dfrac{M{G}_{1}}{MB}=\\dfrac{1}{3}$ nên ${G}_{1}{G}_{2}//AB \\subset (ABD)\\Rightarrow {G}_{1}{G}_{2}//(ABD)$.'
                    ),

                    ('Gọi $M$ là trung điểm $CD$, vì ${G}_{2}$ là trọng tâm tam giác $ABD$ nên $\\dfrac{M{G}_{2}}{MA}=\\dfrac{1}{3}$, tương tự ${G}_{1}$ là trọng tâm tam giác $BCD$ nên $\\dfrac{M{G}_{1}}{MB}=\\dfrac{1}{3}$.\\\\ \n'
                            'Xét tam giác $MAB$ có $\\dfrac{M{G}_{2}}{MA}=\\dfrac{M{G}_{1}}{MB}=\\dfrac{1}{3}$ nên ${G}_{1}{G}_{2}//AB \\subset (ABC)\\Rightarrow {G}_{1}{G}_{2}//(ABC)$.'
                            ),

                    ('${G}_{1}$và ${G}_{2}$ lần lượt là trọng tâm các tam giác $BCD$ và $ACD$ nên $B{G}_{1}$, $A{G}_{2}$ và $CD$ đồng qui tại $M$ với $M$ là trung điểm $CD$.'
            ),

                    ('Gọi $M$ là trung điểm $CD$, vì ${G}_{2}$ là trọng tâm tam giác $ABD$ nên $\\dfrac{M{G}_{2}}{MA}=\\dfrac{1}{3}$, tương tự ${G}_{1}$ là trọng tâm tam giác $BCD$ nên $\\dfrac{M{G}_{1}}{MB}=\\dfrac{1}{3}$.\\\\ \n'
                            'Xét tam giác $MAB$ có $\\dfrac{M{G}_{2}}{MA}=\\dfrac{M{G}_{1}}{MB}=\\dfrac{1}{3}$ nên ${G}_{1}{G}_{2}//AB$ và ${G}_{1}{G}_{2}=\\dfrac{1}{3}AB$.'
                            ),

                    ('Gọi $M$ là trung điểm $CD$, vì ${G}_{2}$ là trọng tâm tam giác $ABD$ nên $\\dfrac{M{G}_{2}}{MA}=\\dfrac{1}{3}$, tương tự ${G}_{1}$ là trọng tâm tam giác $BCD$ nên $\\dfrac{M{G}_{1}}{MB}=\\dfrac{1}{3}$.\\\\ \n'
                            'Xét tam giác $MAB$ có $\\dfrac{M{G}_{2}}{MA}=\\dfrac{M{G}_{1}}{MB}=\\dfrac{1}{3}$ nên ${G}_{1}{G}_{2}//AB$ và ${G}_{1}{G}_{2}=\\dfrac{1}{3}AB \\Rightarrow AB=3{G}_{1}{G}_{2}$.'
                            ),

                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['${G}_{1}{G}_{2}=\\dfrac{2}{3}AB$',
                    '${G}_{1}{G}_{2}=\\dfrac{1}{2}AB$',
                    '${G}_{1}{G}_{2}//(ACD)$',
                    '${G}_{1}{G}_{2}//(BCD)$',
                    '$A{G}_{2}//(BCD)$',
                    '$B{G}_{1}//(ACD)$',
                    '${G}_{1}{G}_{2}$ cắt BD',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-1.0944539836395393,-2.7304882514924036) rectangle (5.0442429856099436,3.730043316144896);\n'
            '\\draw (2.,3.)-- (0.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (4.,0.);\n'
            '\\draw (4.,0.)-- (1.,-2.);\n'
            '\\draw (1.,-2.)-- (0.,0.);\n'
            '\\draw (2.,3.)-- (1.,-2.);\n'
            '\\draw (2.,3.)-- (4.,0.);\n'
            '\\draw (2.,3.)-- (2.5,-1.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (2.5,-1.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.3333333333333335,0.3333333333333333)-- (1.744186046511628,-0.6976744186046512);\n'
            '\\draw (1.8735762014927348,3.610845316741994) node[anchor=north west] {$A$};\n'
            '\\draw (-0.7,0.24946173358015156) node[anchor=north west] {$B$};\n'
            '\\draw (0.7650348070457409,-1.9795408552541198) node[anchor=north west] {$C$};\n'
            '\\draw (4,0.22562213369957113) node[anchor=north west] {$D$};\n'
            '\\draw (2.5053255983281186,-0.859079660866839) node[anchor=north west] {$M$};\n'
            '\\draw (2.398047398865506,0.7500933310723408) node[anchor=north west] {${G}_{2}$};\n'
            '\\draw (1.2,-0.644523261941615) node[anchor=north west] {${G}_{1}$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center} \n'
            )

                # Câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Gọi ${G}_{1}$ và ${G}_{2}$ lần lượt là trọng tâm các tam giác $BCD$ và $ACD$. Chọn khẳng định đúng?  \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(hinhve)+''+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

