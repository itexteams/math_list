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


def bt_dang1_p1_b4_c2_hh11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8','9','10','11','12']
            dang=random.choice(lisdang)
            if dang=='12':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(SAC)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây

                hinhve=(
                        '\\begin{center}  \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-1.1871548320804681,-0.8944059272078285) rectangle (6.963837542588287,6.149020604618457); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (4.,0.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,2.)-- (2.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (2.,5.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,2.); \n'
                                '\\draw (1.7721226542642392,5.7) node[anchor=north west] {$S$}; \n'
                                '\\draw (1.339479746903902,2.6532659131469347) node[anchor=north west] {$A$}; \n'
                                '\\draw (-0.6506776269536497,0.247771348223461) node[anchor=north west] {$B$}; \n'
                                '\\draw (3.9180314747715124,0.10932561786815317) node[anchor=north west] {$C$}; \n'
                                '\\draw (6,2.5) node[anchor=north west] {$D$}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'
                        )

                lg = [
                    ('Ta có \\\\ \n'
                    '\\hspace*{1cm} $SA \\bot (ABCD)$ nên $SA \\bot BD$ \\hspace*{1cm} (1). \\\\ \n'
                    '\\hspace*{1cm} $ABCD$ là hình thoi nên $BD \\bot AC$ \\hspace*{1cm} (2). \\\\ \n'
                    'Từ (1) và (2) suy ra $BD \\bot (SAC)$. \\\\ \n'
                    'Mặt phẳng $(SBD)$ chứa đường thẳng $BD$ vuông góc với mặt phẳng $(SAC)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(SAB)$',
                    '$(SAD)$',
                    '$(SBC)$',
                    '$(SCD)$',
                    '$(ABCD)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thoi và $SA \\bot (ABCD)$. Mặt phẳng nào sau đây vuông góc với mặt phẳng $(SBD)$?  \n'
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


            if dang=='11':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(ABCD)$',
                    '$(SBD)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây

                hinhve=(
                        '\\begin{center}  \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-1.1871548320804681,-0.8944059272078285) rectangle (6.963837542588287,6.149020604618457); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (4.,0.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,2.)-- (2.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (2.,5.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,2.); \n'
                                '\\draw (1.7721226542642392,5.7) node[anchor=north west] {$S$}; \n'
                                '\\draw (1.339479746903902,2.6532659131469347) node[anchor=north west] {$A$}; \n'
                                '\\draw (-0.6506776269536497,0.247771348223461) node[anchor=north west] {$B$}; \n'
                                '\\draw (3.9180314747715124,0.10932561786815317) node[anchor=north west] {$C$}; \n'
                                '\\draw (6,2.5) node[anchor=north west] {$D$}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'
                        )

                lg = [('Vì mặt phẳng $(SAC)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                        ),
                    ('Ta có \\\\ \n'
                    '\\hspace*{1cm} $SA \\bot (ABCD)$ nên $SA \\bot BD$ \\hspace*{1cm} (1). \\\\ \n'
                    '\\hspace*{1cm} $ABCD$ là hình thoi nên $BD \\bot AC$ \\hspace*{1cm} (2). \\\\ \n'
                    'Từ (1) và (2) suy ra $BD \\bot (SAC)$. \\\\ \n'
                    'Mặt phẳng $(SBD)$ chứa đường thẳng $BD$ vuông góc với mặt phẳng $(SAC)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(SAB)$',
                    '$(SAD)$',
                    '$(SBC)$',
                    '$(SCD)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thoi và $SA \\bot (ABCD)$. Mặt phẳng nào sau đây vuông góc với mặt phẳng $(SAC)$?  \n'
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


            if dang=='10':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(SAB)$',
                    '$(SAC)$',
                    '$(SAD)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây

                hinhve=(
                        '\\begin{center}  \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-1.1871548320804681,-0.8944059272078285) rectangle (6.963837542588287,6.149020604618457); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (4.,0.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,2.)-- (2.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (2.,5.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,2.); \n'
                                '\\draw (1.7721226542642392,5.7) node[anchor=north west] {$S$}; \n'
                                '\\draw (1.339479746903902,2.6532659131469347) node[anchor=north west] {$A$}; \n'
                                '\\draw (-0.6506776269536497,0.247771348223461) node[anchor=north west] {$B$}; \n'
                                '\\draw (3.9180314747715124,0.10932561786815317) node[anchor=north west] {$C$}; \n'
                                '\\draw (6,2.5) node[anchor=north west] {$D$}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'
                        )

                lg = [('Vì mặt phẳng $(SAB)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                        ),
                    ('Vì mặt phẳng $(SAC)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ('Vì mặt phẳng $(SAD)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(SBC)$',
                    '$(SCD)$',
                    '$(SBD)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thoi và $SA \\bot (ABCD)$. Mặt phẳng nào sau đây vuông góc với mặt phẳng $(ABCD)$?  \n'
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
            if dang=='9':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(SAB)$',
                    '$(SAC)$',
                    '$(SAD)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây

                hinhve=(
                        '\\begin{center}  \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-1.1871548320804681,-0.8944059272078285) rectangle (6.963837542588287,6.149020604618457); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (4.,0.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,2.)-- (2.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (2.,5.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,2.); \n'
                                '\\draw (1.7721226542642392,5.7) node[anchor=north west] {$S$}; \n'
                                '\\draw (1.339479746903902,2.6532659131469347) node[anchor=north west] {$A$}; \n'
                                '\\draw (-0.6506776269536497,0.247771348223461) node[anchor=north west] {$B$}; \n'
                                '\\draw (3.9180314747715124,0.10932561786815317) node[anchor=north west] {$C$}; \n'
                                '\\draw (6,2.5) node[anchor=north west] {$D$}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'
                        )

                lg = [('Vì mặt phẳng $(SAB)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                        ),
                    ('Vì mặt phẳng $(SAC)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ('Vì mặt phẳng $(SAD)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(SBC)$',
                    '$(SCD)$',
                    '$(SBD)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành và $SA \\bot (ABCD)$. Mặt phẳng nào sau đây vuông góc với mặt phẳng $(ABCD)$?  \n'
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
            if dang=='8':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(SAC)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây

                hinhve=(
                        '\\begin{center}  \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-1.1871548320804681,-0.8944059272078285) rectangle (6.963837542588287,6.149020604618457); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (4.,0.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,2.)-- (2.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (2.,5.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,2.); \n'
                                '\\draw (1.7721226542642392,5.7) node[anchor=north west] {$S$}; \n'
                                '\\draw (1.339479746903902,2.6532659131469347) node[anchor=north west] {$A$}; \n'
                                '\\draw (-0.6506776269536497,0.247771348223461) node[anchor=north west] {$B$}; \n'
                                '\\draw (3.9180314747715124,0.10932561786815317) node[anchor=north west] {$C$}; \n'
                                '\\draw (6,2.5) node[anchor=north west] {$D$}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'
                        )

                lg = [
                    ('Ta có \\\\ \n'
                    '\\hspace*{1cm} $SA \\bot (ABCD)$ nên $SA \\bot BD$ \\hspace*{1cm} (1). \\\\ \n'
                    '\\hspace*{1cm} $ABCD$ là hình vuông nên $BD \\bot AC$ \\hspace*{1cm} (2). \\\\ \n'
                    'Từ (1) và (2) suy ra $BD \\bot (SAC)$. \\\\ \n'
                    'Mặt phẳng $(SBD)$ chứa đường thẳng $BD$ vuông góc với mặt phẳng $(SAC)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(SAB)$',
                    '$(SAD)$',
                    '$(SBC)$',
                    '$(SCD)$',
                    '$(ABCD)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông và $SA \\bot (ABCD)$. Mặt phẳng nào sau đây vuông góc với mặt phẳng $(SBD)$?  \n'
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


            if dang=='7':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(ABCD)$',
                    '$(SBD)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây

                hinhve=(
                        '\\begin{center}  \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-1.1871548320804681,-0.8944059272078285) rectangle (6.963837542588287,6.149020604618457); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (4.,0.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,2.)-- (2.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (2.,5.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,2.); \n'
                                '\\draw (1.7721226542642392,5.7) node[anchor=north west] {$S$}; \n'
                                '\\draw (1.339479746903902,2.6532659131469347) node[anchor=north west] {$A$}; \n'
                                '\\draw (-0.6506776269536497,0.247771348223461) node[anchor=north west] {$B$}; \n'
                                '\\draw (3.9180314747715124,0.10932561786815317) node[anchor=north west] {$C$}; \n'
                                '\\draw (6,2.5) node[anchor=north west] {$D$}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'
                        )

                lg = [('Vì mặt phẳng $(SAC)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                        ),
                    ('Ta có \\\\ \n'
                    '\\hspace*{1cm} $SA \\bot (ABCD)$ nên $SA \\bot BD$ \\hspace*{1cm} (1). \\\\ \n'
                    '\\hspace*{1cm} $ABCD$ là hình vuông nên $BD \\bot AC$ \\hspace*{1cm} (2). \\\\ \n'
                    'Từ (1) và (2) suy ra $BD \\bot (SAC)$. \\\\ \n'
                    'Mặt phẳng $(SBD)$ chứa đường thẳng $BD$ vuông góc với mặt phẳng $(SAC)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(SAB)$',
                    '$(SAD)$',
                    '$(SBC)$',
                    '$(SCD)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông và $SA \\bot (ABCD)$. Mặt phẳng nào sau đây vuông góc với mặt phẳng $(SAC)$?  \n'
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


            if dang=='6':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(ABCD)$',
                    '$(SAB)$',
                    '$(SCD)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây

                hinhve=(
                        '\\begin{center}  \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-1.1871548320804681,-0.8944059272078285) rectangle (6.963837542588287,6.149020604618457); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (4.,0.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,2.)-- (2.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (2.,5.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,2.); \n'
                                '\\draw (1.7721226542642392,5.7) node[anchor=north west] {$S$}; \n'
                                '\\draw (1.339479746903902,2.6532659131469347) node[anchor=north west] {$A$}; \n'
                                '\\draw (-0.6506776269536497,0.247771348223461) node[anchor=north west] {$B$}; \n'
                                '\\draw (3.9180314747715124,0.10932561786815317) node[anchor=north west] {$C$}; \n'
                                '\\draw (6,2.5) node[anchor=north west] {$D$}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'
                        )

                lg = [('Vì mặt phẳng $(SAD)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                        ),
                    ('Ta có \\\\ \n'
                    '\\hspace*{1cm} $SA \\bot (ABCD)$ nên $SA \\bot AB$ \\hspace*{1cm} (1). \\\\ \n'
                    '\\hspace*{1cm} $ABCD$ là hình vuông nên $AB \\bot AD$ \\hspace*{1cm} (2). \\\\ \n'
                    'Từ (1) và (2) suy ra $AB \\bot (SAD)$. \\\\ \n'
                    'Mặt phẳng $(SAB)$ chứa đường thẳng $AB$ vuông góc với mặt phẳng $(SAD)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ('Ta có \\\\ \n'
                    '\\hspace*{1cm} $SA \\bot (ABCD)$ nên $SA \\bot CD$ \\hspace*{1cm} (1). \\\\ \n'
                    '\\hspace*{1cm} $ABCD$ là hình vuông nên $AD \\bot CD$ \\hspace*{1cm} (2). \\\\ \n'
                    'Từ (1) và (2) suy ra $CD \\bot (SAD)$. \\\\ \n'
                    'Mặt phẳng $(SCD)$ chứa đường thẳng $CD$ vuông góc với mặt phẳng $(SAD)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(SAC)$',
                    '$(SBD)$',
                    '$(SBC)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông và $SA \\bot (ABCD)$. Mặt phẳng nào sau đây vuông góc với mặt phẳng $(SAD)$?  \n'
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


            if dang=='5':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(ABCD)$',
                    '$(SAD)$',
                    '$(SBC)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây

                hinhve=(
                        '\\begin{center}  \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-1.1871548320804681,-0.8944059272078285) rectangle (6.963837542588287,6.149020604618457); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (4.,0.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,2.)-- (2.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (2.,5.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,2.); \n'
                                '\\draw (1.7721226542642392,5.7) node[anchor=north west] {$S$}; \n'
                                '\\draw (1.339479746903902,2.6532659131469347) node[anchor=north west] {$A$}; \n'
                                '\\draw (-0.6506776269536497,0.247771348223461) node[anchor=north west] {$B$}; \n'
                                '\\draw (3.9180314747715124,0.10932561786815317) node[anchor=north west] {$C$}; \n'
                                '\\draw (6,2.5) node[anchor=north west] {$D$}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'
                        )

                lg = [('Vì mặt phẳng $(SAB)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                        ),
                    ('Ta có \\\\ \n'
                    '\\hspace*{1cm} $SA \\bot (ABCD)$ nên $SA \\bot AD$ \\hspace*{1cm} (1). \\\\ \n'
                    '\\hspace*{1cm} $ABCD$ là hình vuông nên $AD \\bot AB$ \\hspace*{1cm} (2). \\\\ \n'
                    'Từ (1) và (2) suy ra $AD \\bot (SAB)$. \\\\ \n'
                    'Mặt phẳng $(SAD)$ chứa đường thẳng $AD$ vuông góc với mặt phẳng $(SAB)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ('Ta có \\\\ \n'
                    '\\hspace*{1cm} $SA \\bot (ABCD)$ nên $SA \\bot BC$ \\hspace*{1cm} (1). \\\\ \n'
                    '\\hspace*{1cm} $ABCD$ là hình vuông nên $AB \\bot BC$ \\hspace*{1cm} (2). \\\\ \n'
                    'Từ (1) và (2) suy ra $BC \\bot (SAB)$. \\\\ \n'
                    'Mặt phẳng $(SBC)$ chứa đường thẳng $BC$ vuông góc với mặt phẳng $(SAB)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(SAC)$',
                    '$(SBD)$',
                    '$(SCD)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông và $SA \\bot (ABCD)$. Mặt phẳng nào sau đây vuông góc với mặt phẳng $(SAB)$?  \n'
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


            if dang=='4':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(SAB)$',
                    '$(SAC)$',
                    '$(SAD)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây

                hinhve=(
                        '\\begin{center}  \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-1.1871548320804681,-0.8944059272078285) rectangle (6.963837542588287,6.149020604618457); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (4.,0.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,2.)-- (2.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (2.,5.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,2.); \n'
                                '\\draw (1.7721226542642392,5.7) node[anchor=north west] {$S$}; \n'
                                '\\draw (1.339479746903902,2.6532659131469347) node[anchor=north west] {$A$}; \n'
                                '\\draw (-0.6506776269536497,0.247771348223461) node[anchor=north west] {$B$}; \n'
                                '\\draw (3.9180314747715124,0.10932561786815317) node[anchor=north west] {$C$}; \n'
                                '\\draw (6,2.5) node[anchor=north west] {$D$}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'
                        )

                lg = [('Vì mặt phẳng $(SAB)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                        ),
                    ('Vì mặt phẳng $(SAC)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ('Vì mặt phẳng $(SAD)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(SBC)$',
                    '$(SCD)$',
                    '$(SBD)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông và $SA \\bot (ABCD)$. Mặt phẳng nào sau đây vuông góc với mặt phẳng $(ABCD)$?  \n'
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
            if dang=='3':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(ABCD)$',
                    '$(SAB)$',
                    '$(SCD)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây

                hinhve=(
                        '\\begin{center}  \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-1.1871548320804681,-0.8944059272078285) rectangle (6.963837542588287,6.149020604618457); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (4.,0.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,2.)-- (2.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (2.,5.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,2.); \n'
                                '\\draw (1.7721226542642392,5.7) node[anchor=north west] {$S$}; \n'
                                '\\draw (1.339479746903902,2.6532659131469347) node[anchor=north west] {$A$}; \n'
                                '\\draw (-0.6506776269536497,0.247771348223461) node[anchor=north west] {$B$}; \n'
                                '\\draw (3.9180314747715124,0.10932561786815317) node[anchor=north west] {$C$}; \n'
                                '\\draw (6,2.5) node[anchor=north west] {$D$}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'
                        )

                lg = [('Vì mặt phẳng $(SAD)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                        ),
                    ('Ta có \\\\ \n'
                    '\\hspace*{1cm} $SA \\bot (ABCD)$ nên $SA \\bot AB$ \\hspace*{1cm} (1). \\\\ \n'
                    '\\hspace*{1cm} $ABCD$ là hình chữ nhật nên $AB \\bot AD$ \\hspace*{1cm} (2). \\\\ \n'
                    'Từ (1) và (2) suy ra $AB \\bot (SAD)$. \\\\ \n'
                    'Mặt phẳng $(SAB)$ chứa đường thẳng $AB$ vuông góc với mặt phẳng $(SAD)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ('Ta có \\\\ \n'
                    '\\hspace*{1cm} $SA \\bot (ABCD)$ nên $SA \\bot CD$ \\hspace*{1cm} (1). \\\\ \n'
                    '\\hspace*{1cm} $ABCD$ là hình chữ nhật nên $AD \\bot CD$ \\hspace*{1cm} (2). \\\\ \n'
                    'Từ (1) và (2) suy ra $CD \\bot (SAD)$. \\\\ \n'
                    'Mặt phẳng $(SCD)$ chứa đường thẳng $CD$ vuông góc với mặt phẳng $(SAD)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(SAC)$',
                    '$(SBD)$',
                    '$(SBC)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật và $SA \\bot (ABCD)$. Mặt phẳng nào sau đây vuông góc với mặt phẳng $(SAD)$?  \n'
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

            if dang=='2':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(ABCD)$',
                    '$(SAD)$',
                    '$(SBC)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây

                hinhve=(
                        '\\begin{center}  \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-1.1871548320804681,-0.8944059272078285) rectangle (6.963837542588287,6.149020604618457); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (4.,0.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,2.)-- (2.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (2.,5.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,2.); \n'
                                '\\draw (1.7721226542642392,5.7) node[anchor=north west] {$S$}; \n'
                                '\\draw (1.339479746903902,2.6532659131469347) node[anchor=north west] {$A$}; \n'
                                '\\draw (-0.6506776269536497,0.247771348223461) node[anchor=north west] {$B$}; \n'
                                '\\draw (3.9180314747715124,0.10932561786815317) node[anchor=north west] {$C$}; \n'
                                '\\draw (6,2.5) node[anchor=north west] {$D$}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'
                        )

                lg = [('Vì mặt phẳng $(SAB)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                        ),
                    ('Ta có \\\\ \n'
                    '\\hspace*{1cm} $SA \\bot (ABCD)$ nên $SA \\bot AD$ \\hspace*{1cm} (1). \\\\ \n'
                    '\\hspace*{1cm} $ABCD$ là hình chữ nhật nên $AD \\bot AB$ \\hspace*{1cm} (2). \\\\ \n'
                    'Từ (1) và (2) suy ra $AD \\bot (SAB)$. \\\\ \n'
                    'Mặt phẳng $(SAD)$ chứa đường thẳng $AD$ vuông góc với mặt phẳng $(SAB)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ('Ta có \\\\ \n'
                    '\\hspace*{1cm} $SA \\bot (ABCD)$ nên $SA \\bot BC$ \\hspace*{1cm} (1). \\\\ \n'
                    '\\hspace*{1cm} $ABCD$ là hình chữ nhật nên $AB \\bot BC$ \\hspace*{1cm} (2). \\\\ \n'
                    'Từ (1) và (2) suy ra $BC \\bot (SAB)$. \\\\ \n'
                    'Mặt phẳng $(SBC)$ chứa đường thẳng $BC$ vuông góc với mặt phẳng $(SAB)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(SAC)$',
                    '$(SBD)$',
                    '$(SCD)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật và $SA \\bot (ABCD)$. Mặt phẳng nào sau đây vuông góc với mặt phẳng $(SAB)$?  \n'
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


            if dang=='1':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(SAB)$',
                    '$(SAC)$',
                    '$(SAD)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây

                hinhve=(
                        '\\begin{center}  \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-1.1871548320804681,-0.8944059272078285) rectangle (6.963837542588287,6.149020604618457); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (4.,0.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,2.)-- (2.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (2.,5.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (2.,5.)-- (6.,2.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,2.); \n'
                                '\\draw (1.7721226542642392,5.7) node[anchor=north west] {$S$}; \n'
                                '\\draw (1.339479746903902,2.6532659131469347) node[anchor=north west] {$A$}; \n'
                                '\\draw (-0.6506776269536497,0.247771348223461) node[anchor=north west] {$B$}; \n'
                                '\\draw (3.9180314747715124,0.10932561786815317) node[anchor=north west] {$C$}; \n'
                                '\\draw (6,2.5) node[anchor=north west] {$D$}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'
                        )

                lg = [('Vì mặt phẳng $(SAB)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                        ),
                    ('Vì mặt phẳng $(SAC)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ('Vì mặt phẳng $(SAD)$ chứa đường thẳng $SA$ vuông góc với mặt phẳng $(ABCD)$ nên hai mặt phẳng vuông góc với nhau.'
                    ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(SBC)$',
                    '$(SCD)$',
                    '$(SBD)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật và $SA \\bot (ABCD)$. Mặt phẳng nào sau đây vuông góc với mặt phẳng $(ABCD)$?  \n'
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
                '\\loigiai{'+hinhve+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

