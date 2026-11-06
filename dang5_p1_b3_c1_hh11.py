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


def bt_dang5_p1_b3_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$MN//(ABCD)$',
                    '$NP//(SCD)$',
                    '$PQ//(SAD)$',
                    '$QM//(SAB)$',

                    '$MN//(SAC)$',
                    '$NP//(SAB)$',
                    '$QM//(SCD)$',


                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có $M\\in AB\\subset (ABCD) \\Rightarrow M\\in (ABCD)$.\\\\ \n'
                    'Vậy $MN$ không song song với $(ABCD)$.'),

                    ('Ta có $N\\in CD\\subset (SCD) \\Rightarrow N\\in (SCD)$.\\\\ \n'
                            'Vậy $NP$ không song song với $(SCD)$.'),

                    ('Ta có $Q\\in SA\\subset (SAD) \\Rightarrow Q\\in (SAD)$.\\\\ \n'
                            'Vậy $PQ$ không song song với $(SAD)$.'),

                    ('Ta có $M\\in AB\\subset (SAB) \\Rightarrow M\\in (SAB)$.\\\\ \n'
                            'Vậy $QM$ không song song với $(SAB)$.'),

                    ('Ta có $MN$, $AC$ cùng thuộc mặt phẳng $(ABCD)$ và $MN$ cắt $AC\\subset (SAC)$.\\\\ \n'
                            'Vậy $MN$ không song song với $(SAC)$.'),

                    ('Ta có $NP//SC$, mặt khác $SC$ cắt mặt phẳng $(SAB)$.\\\\ \n'
                            'Vậy $NP$ không song song với $(SAB)$.'),

                    ('Ta có $QM//SB$, mặt khác $SB$ cắt mặt phẳng $(SCD)$.\\\\ \n'
                            'Vậy $QM$ không song song với $(SCD)$.'),

                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$MN//(SBC)$',
                    '$MN//(SAD)$',
                    '$PQ//(SBC)$',
                    '$PN//(SBC)$',
                    '$MQ//(SBC)$',
                    '$MN//(SBC)$',
                    '$PQ//(ABCD)$',
                    '$MN//(CPQ)$',
                    '$MN//(BQP)$',
                    '$QP//(SMN)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-1.1598104124932853,-0.5949211567768103) rectangle (5.586878551004502,4.565746893059641);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (1.5,1.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.)-- (4.5,1.);\n'
            '\\draw (4.5,1.)-- (3.,0.);\n'
            '\\draw (3.,0.)-- (0.,0.);\n'
            '\\draw (2.,4.)-- (4.5,1.);\n'
            '\\draw (2.,4.)-- (3.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.,4.)-- (1.5,1.);\n'
            '\\draw (2.,4.)-- (0.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.75,2.5)-- (3.25,2.5);\n'
            '\\draw (3.25,2.5)-- (3.75,0.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (3.75,0.5)-- (0.75,0.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.75,0.5)-- (1.75,2.5);\n'
            '\\draw (1.8,4.5047460886880515) node[anchor=north west] {$S$};\n'
            '\\draw (-0.5,0.19808930005385003) node[anchor=north west] {$B$};\n'
            '\\draw (2.902843158654569,0.1004880130593072) node[anchor=north west] {$C$};\n'
            '\\draw (4.45,1.4181053874856353) node[anchor=north west] {$D$};\n'
            '\\draw (1.5,1.5767074788517674) node[anchor=north west] {$A$};\n'
            '\\draw (3.7446542589825027,0.6494952524036106) node[anchor=north west] {$N$};\n'
            '\\draw (0.25,1.0032999177588282) node[anchor=north west] {$M$};\n'
            '\\draw (1.25,2.8699245315294597) node[anchor=north west] {$Q$};\n'
            '\\draw (3.317648628381377,2.943125496775367) node[anchor=north west] {$P$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center} \n'
            )

                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Gọi $M,N,P,Q$ lần lượt là trung điểm các cạnh $AB, CD, SD$ và $SA$. Chọn khẳng định $\\textbf{sai}$ trong các khẳng định dưới đây.  \n'
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

